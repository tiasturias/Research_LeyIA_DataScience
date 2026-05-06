"""Bloque H: taxonomías exploratorias binding/non-binding y habilitantes."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import OUTPUTS_DIR, get_binding_taxonomy
from .load import get_block_var_cols, load_dictionary, load_wide


def build_binding_classification(wide: pd.DataFrame, dictionary: pd.DataFrame) -> pd.DataFrame:
    taxonomy = get_binding_taxonomy()
    rows = wide[["iso3", "country_name_canonical", "region", "income_group"]].copy()
    for cls in ["binding", "non_binding", "hybrid", "unknown"]:
        vars_cls = [v for v in taxonomy.get(cls, []) if v in wide.columns]
        numeric_like = []
        for v in vars_cls:
            if pd.api.types.is_numeric_dtype(wide[v]):
                numeric_like.append(wide[v].fillna(0).astype(float).gt(0))
            else:
                numeric_like.append(wide[v].notna())
        rows[f"n_{cls}"] = sum(numeric_like).astype(int) if numeric_like else 0
        rows[f"has_{cls}"] = rows[f"n_{cls}"].gt(0).astype(int)
    reg_cols = get_block_var_cols("regulatory_treatment", wide, dictionary)
    rows["has_iapp_record"] = wide[reg_cols].notna().any(axis=1).astype(int) if reg_cols else 0
    rows["taxonomy_status"] = np.where(rows["has_iapp_record"].eq(1), "classified_exploratory", "no_iapp_record")
    return rows


def build_enabling_classification(wide: pd.DataFrame, dictionary: pd.DataFrame) -> pd.DataFrame:
    rows = wide[["iso3", "country_name_canonical", "region", "income_group"]].copy()
    positive_tokens = [
        "rule_of_law", "gov_effectiveness", "regulatory_quality", "internet",
        "tertiary", "research", "rd", "broadband", "mobile", "cyber",
        "innovation", "readiness",
    ]
    control_blocks = ["socioeconomic_control", "institutional_control", "tech_infrastructure_control"]
    cols = []
    for block in control_blocks:
        cols.extend(get_block_var_cols(block, wide, dictionary))
    cols = [c for c in cols if c in wide.columns and pd.api.types.is_numeric_dtype(wide[c])]
    selected = [c for c in cols if any(tok in c.lower() for tok in positive_tokens)]
    if not selected:
        selected = cols[:20]
    high_flags = []
    low_flags = []
    for col in selected:
        s = wide[col]
        q75 = s.quantile(0.75)
        q25 = s.quantile(0.25)
        high_flags.append(s.ge(q75) & s.notna())
        low_flags.append(s.le(q25) & s.notna())
    rows["n_habilitantes_alto"] = sum(high_flags).astype(int) if high_flags else 0
    rows["n_inhabilitantes_alto"] = sum(low_flags).astype(int) if low_flags else 0
    rows["n_variables_taxonomia"] = len(selected)
    rows["taxonomy_status"] = "exploratory_counts_not_index"
    return rows


def build_binding_vs_outcome(wide: pd.DataFrame, dictionary: pd.DataFrame, binding: pd.DataFrame) -> pd.DataFrame:
    outcome_cols = get_block_var_cols("ecosystem_outcome", wide, dictionary)
    outcome_cols = [c for c in outcome_cols if pd.api.types.is_numeric_dtype(wide[c]) and wide[c].notna().mean() >= 0.30]
    rows = []
    merged = wide[["iso3", *outcome_cols]].merge(binding[["iso3", "has_binding", "has_non_binding"]], on="iso3", how="left")
    for col in outcome_cols[:80]:
        for group_col in ["has_binding", "has_non_binding"]:
            g1 = merged.loc[merged[group_col].eq(1), col].dropna()
            g0 = merged.loc[merged[group_col].eq(0), col].dropna()
            rows.append({
                "variable_matriz": col,
                "comparison": f"{group_col}_1_vs_0",
                "n_group_1": len(g1),
                "n_group_0": len(g0),
                "median_group_1": round(float(g1.median()), 6) if len(g1) else np.nan,
                "median_group_0": round(float(g0.median()), 6) if len(g0) else np.nan,
                "median_difference": round(float(g1.median() - g0.median()), 6) if len(g1) and len(g0) else np.nan,
                "status": "descriptive_not_causal",
            })
    return pd.DataFrame(rows) if rows else pd.DataFrame(columns=[
        "variable_matriz", "comparison", "n_group_1", "n_group_0",
        "median_group_1", "median_group_0", "median_difference", "status",
    ])


def run_taxonomy_analysis(
    wide: pd.DataFrame | None = None,
    dictionary: pd.DataFrame | None = None,
    save: bool = True,
) -> dict[str, pd.DataFrame]:
    if wide is None:
        wide = load_wide()
    if dictionary is None:
        dictionary = load_dictionary()
    binding = build_binding_classification(wide, dictionary)
    enabling = build_enabling_classification(wide, dictionary)
    binding_vs = build_binding_vs_outcome(wide, dictionary, binding)
    outputs = {
        "eda_binding_classification": binding,
        "eda_enabling_classification": enabling,
        "eda_binding_vs_outcome": binding_vs,
    }
    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        for name, df in outputs.items():
            df.to_csv(OUTPUTS_DIR / f"{name}.csv", index=False)
    return outputs
