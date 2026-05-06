"""Bloque G: mapeo preregistrado de variables a las 4 sub-preguntas."""

from __future__ import annotations

import fnmatch
import re

import numpy as np
import pandas as pd

from .config import OUTPUTS_DIR, get_question_mapping
from .load import load_dictionary, load_wide


def _tokens(text: str) -> list[str]:
    return [t for t in re.split(r"[_\W]+", text.lower()) if len(t) >= 3 and t not in {"all", "score"}]


def _match_variables(pattern: str, dictionary: pd.DataFrame, block_hint: str | None = None) -> list[str]:
    variables = dictionary["variable_matriz"].astype(str).tolist()
    if "*" in pattern:
        matched = [v for v in variables if fnmatch.fnmatch(v, pattern)]
    elif pattern.endswith("_all_binary"):
        prefix = pattern.replace("_all_binary", "_")
        matched = dictionary[
            dictionary["variable_matriz"].str.startswith(prefix)
            & dictionary["tipo_matriz"].eq("binary")
        ]["variable_matriz"].tolist()
    elif pattern.endswith("_all"):
        prefix = pattern.replace("_all", "_")
        matched = [v for v in variables if v.startswith(prefix)]
    else:
        matched = [pattern] if pattern in variables else []
    return matched


def _candidate_rows(
    qname: str,
    role: str,
    configured: list[str],
    dictionary: pd.DataFrame,
    wide: pd.DataFrame,
    block_hint: str | None = None,
) -> list[dict]:
    rows = []
    seen = set()
    for item in configured:
        matches = _match_variables(str(item), dictionary, block_hint=block_hint)
        if not matches:
            rows.append({
                "subpregunta": qname, "role": role, "configured_variable": item,
                "variable_matriz": "", "match_status": "not_found",
                "bloque_tematico": "", "tipo_matriz": "", "pct_complete": 0.0,
                "n_countries_available": 0,
            })
            continue
        for var in matches:
            if (role, var) in seen:
                continue
            seen.add((role, var))
            drow = dictionary[dictionary["variable_matriz"].eq(var)].iloc[0]
            rows.append({
                "subpregunta": qname,
                "role": role,
                "configured_variable": item,
                "variable_matriz": var,
                "match_status": "exact_or_pattern" if var == item or "*" in str(item) else "fallback_token_match",
                "bloque_tematico": drow.get("bloque_tematico", ""),
                "tipo_matriz": drow.get("tipo_matriz", ""),
                "pct_complete": round(float(wide[var].notna().mean() * 100), 2) if var in wide else 0.0,
                "n_countries_available": int(wide[var].notna().sum()) if var in wide else 0,
            })
    return rows


def _effective_n(wide: pd.DataFrame, vars_a: list[str], vars_b: list[str]) -> int:
    cols = [c for c in vars_a + vars_b if c in wide.columns]
    if not cols:
        return 0
    return int(wide[cols].notna().all(axis=1).sum())


def build_question_outputs(wide: pd.DataFrame, dictionary: pd.DataFrame) -> dict[str, pd.DataFrame]:
    mapping = get_question_mapping()
    outputs: dict[str, pd.DataFrame] = {}
    viability_rows = []

    for qname, cfg in mapping.items():
        rows = []
        if qname == "Q4_content":
            rows.extend(_candidate_rows(qname, "content_variable", cfg.get("variables_relevantes", []), dictionary, wide, "regulatory_treatment"))
            for method in cfg.get("metodos", []):
                rows.append({
                    "subpregunta": qname, "role": "method", "configured_variable": str(method),
                    "variable_matriz": "", "match_status": "method_preregistered",
                    "bloque_tematico": "regulatory_treatment", "tipo_matriz": "method",
                    "pct_complete": np.nan, "n_countries_available": np.nan,
                })
        else:
            outcome_key = "outcomes_candidatos" if "outcomes_candidatos" in cfg else "outcomes_candidatas"
            treatment_key = "tratamientos_candidatos" if "tratamientos_candidatos" in cfg else "tratamientos_candidatos"
            rows.extend(_candidate_rows(qname, "outcome_candidate", cfg.get(outcome_key, []), dictionary, wide))
            rows.extend(_candidate_rows(qname, "treatment_candidate", cfg.get(treatment_key, []), dictionary, wide, "regulatory_treatment"))
            rows.extend(_candidate_rows(qname, "control_recommended", cfg.get("controles_recomendados", []), dictionary, wide))

        df = pd.DataFrame(rows)
        real_outcomes = df.loc[df["role"].eq("outcome_candidate") & df["variable_matriz"].ne(""), "variable_matriz"].tolist()
        real_treatments = df.loc[df["role"].eq("treatment_candidate") & df["variable_matriz"].ne(""), "variable_matriz"].tolist()
        n_eff = _effective_n(wide, real_outcomes[:3], real_treatments[:2]) if real_outcomes and real_treatments else int(df["n_countries_available"].fillna(0).max())
        viability = "viable_descriptive" if n_eff >= 30 else ("requires_extension" if n_eff > 0 else "not_estimable")
        df["n_effective_cross_coverage"] = n_eff
        df["viability"] = viability
        outputs[_filename_for_q(qname)] = df
        viability_rows.append({
            "subpregunta": qname,
            "n_effective": n_eff,
            "n_candidates_mapped": int(df["variable_matriz"].ne("").sum()),
            "viability": viability,
            "main_gap": "IAPP/regulatory coverage bottleneck" if qname != "Q4_content" and n_eff < 30 else "NLP corpus reserved for Fase 5" if qname == "Q4_content" else "",
        })

    outputs["eda_question_viability"] = pd.DataFrame(viability_rows)
    return outputs


def _filename_for_q(qname: str) -> str:
    return {
        "Q1_investment": "eda_question_q1_investment",
        "Q2_adoption": "eda_question_q2_adoption",
        "Q3_innovation": "eda_question_q3_innovation",
        "Q4_content": "eda_question_q4_content",
    }.get(qname, f"eda_question_{qname.lower()}")


def run_question_mapping(
    wide: pd.DataFrame | None = None,
    dictionary: pd.DataFrame | None = None,
    save: bool = True,
) -> dict[str, pd.DataFrame]:
    if wide is None:
        wide = load_wide()
    if dictionary is None:
        dictionary = load_dictionary()
    outputs = build_question_outputs(wide, dictionary)
    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        for name, df in outputs.items():
            df.to_csv(OUTPUTS_DIR / f"{name}.csv", index=False)
    return outputs
