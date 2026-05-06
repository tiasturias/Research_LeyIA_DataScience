"""Transform panel data into snapshot, dictionary, wide matrix and traceability."""

from __future__ import annotations

import pandas as pd

from .config import BLOCKS, SOURCE_ORDER
from .utils import slugify


TEMPORAL_RULES = {
    "iapp": ("cross_section", "IAPP snapshot 2026-01; no temporal collapse"),
    "microsoft": ("h2_2025_if_available", "Prefer H2 2025; H1/change retained as separate variables"),
    "oxford": ("latest_year_per_country", "Latest year after excluding incompatible 2019 scale"),
    "wb": ("latest_available_per_country_per_indicator", "Latest available year per country-indicator"),
    "wipo": ("year_2025_if_available", "Prefer 2025 score, fallback latest available score"),
    "stanford": ("latest_available_per_figure", "Latest year per figure/variable; no-year rows retained as cross-section"),
    "oecd": ("latest_available_per_country_per_indicator", "Latest available year per country-indicator"),
    "anthropic": ("latest_window_available", "Latest available country window/metric"),
}


def build_snapshot(panel: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (_, source_id, _), group in panel.groupby(["iso3", "source_id", "variable_matriz"], dropna=False):
        group = group.copy()
        rule, _ = TEMPORAL_RULES.get(source_id, ("latest_available", "Default latest available"))
        selected = _select_row(group, rule)
        if selected is None:
            continue
        d = selected.to_dict()
        d["snapshot_rule"] = rule
        d["year_used"] = "" if pd.isna(selected["year"]) else str(int(selected["year"]))
        d["years_collapsed"] = _years_collapsed(group)
        d["temporal_warning"] = _temporal_warning(selected, rule)
        rows.append(d)
    snapshot = pd.DataFrame(rows)
    snapshot["year"] = pd.to_numeric(snapshot["year"], errors="coerce").astype("Int64")
    return snapshot.sort_values(["iso3", "source_id", "variable_matriz"]).reset_index(drop=True)


def build_dictionary(panel: pd.DataFrame, snapshot: pd.DataFrame, universe: pd.DataFrame) -> pd.DataFrame:
    included_iso3 = set(universe[universe["included_in_matrix"].astype(bool)]["iso3"])
    snap_included = snapshot[snapshot["iso3"].isin(included_iso3)]
    n_entities = max(len(included_iso3), 1)
    coverage = snap_included.groupby("variable_matriz")["iso3"].nunique().to_dict()
    rows = []
    for variable, group in panel.groupby("variable_matriz"):
        source_id = group["source_id"].iloc[0]
        table_id = _join_unique(group["table_id"])
        original_variable = _join_unique(group["original_variable"], limit=8)
        unit = _mode(group["unit"])
        direction = _mode(group["direction"])
        tipo = _infer_type(group, unit)
        block = _block_for(source_id, variable, table_id)
        n_available = int(coverage.get(variable, 0))
        pct = round(100 * n_available / n_entities, 2)
        redundant_with = _redundant_with(variable)
        is_primary = _is_primary(variable, source_id)
        fase4_role = _fase4_role(variable, source_id, block, pct)
        rows.append({
            "variable_matriz": variable,
            "source_id": source_id,
            "table_id": table_id,
            "original_variable": original_variable,
            "tipo_original": _mode(group["unit"]),
            "tipo_matriz": tipo,
            "unit": unit,
            "direction": direction,
            "bloque_tematico": block,
            "regla_temporal_default": TEMPORAL_RULES.get(source_id, ("latest_available", ""))[0],
            "regla_transformacion": "raw_value_no_imputation",
            "is_primary": is_primary,
            "redundant_with": redundant_with,
            "pct_complete": pct,
            "n_countries_available": n_available,
            "fase4_role": fase4_role,
            "included_in_fase4_eda": fase4_role != "excluded_from_eda",
            "known_limitations": _known_limitations(variable, pct),
            "human_review_status": "review_required_low_coverage" if pct < 30 else "approved_by_methodological_rules",
            "notes": "generated from real source columns; no synthetic values; no Fase 3 imputation",
        })
    dictionary = pd.DataFrame(rows).sort_values(["source_id", "variable_matriz"]).reset_index(drop=True)
    bad_blocks = set(dictionary["bloque_tematico"]) - set(BLOCKS)
    if bad_blocks:
        raise ValueError(f"Invalid dictionary blocks: {bad_blocks}")
    return dictionary


def build_wide_and_traceability(snapshot: pd.DataFrame, universe: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    included = universe[universe["included_in_matrix"].astype(bool)].copy()
    id_cols = [
        "iso3", "country_name_canonical", "entity_type", "region", "income_group",
        "n_sources_present", "source_list", "included_in_matrix",
        "included_in_dense_candidate", "inclusion_notes",
    ]
    wide = included[id_cols].sort_values("iso3").reset_index(drop=True)
    snap = snapshot[snapshot["iso3"].isin(set(wide["iso3"]))].copy()

    trace_rows = []
    for variable in sorted(snap["variable_matriz"].unique()):
        var_data = snap[snap["variable_matriz"].eq(variable)].copy()
        value_map = {}
        for _, row in var_data.iterrows():
            value = row["value_numeric"] if pd.notna(row["value_numeric"]) else row["value_text"]
            if pd.notna(value):
                value_map[row["iso3"]] = value
                trace_rows.append({
                    "cell_id_wide": f"{row['iso3']}__{variable}",
                    "cell_id_snapshot": row["cell_id"],
                    "cell_id_panel": row["cell_id"],
                    "iso3": row["iso3"],
                    "variable_matriz": variable,
                    "source_id": row["source_id"],
                    "source_file": row["source_file"],
                    "source_sheet": row["source_sheet"],
                    "original_variable": row["original_variable"],
                    "row_identifier": row["row_identifier"],
                    "year_used": row["year_used"],
                    "snapshot_rule": row["snapshot_rule"],
                    "confidence_level": row["confidence_level"],
                    "extraction_rule": row["extraction_rule"],
                })
        wide[variable] = wide["iso3"].map(value_map)
        wide[f"{variable}_year_used"] = wide["iso3"].map(var_data.set_index("iso3")["year_used"].to_dict())
        wide[f"{variable}_confidence"] = wide["iso3"].map(var_data.set_index("iso3")["confidence_level"].to_dict())

    value_cols = [c for c in wide.columns if c not in id_cols and not c.endswith("_confidence") and not c.endswith("_year_used")]
    wide["n_variables_available"] = wide[value_cols].notna().sum(axis=1)
    wide["pct_variables_available"] = round(100 * wide["n_variables_available"] / max(len(value_cols), 1), 2)
    wide = wide[wide["n_variables_available"].gt(0)].reset_index(drop=True)
    dense = wide["n_sources_present"].ge(5) & wide["pct_variables_available"].ge(20)
    wide["included_in_dense_candidate"] = dense
    trace = pd.DataFrame(trace_rows)
    trace = trace[trace["iso3"].isin(set(wide["iso3"]))].copy()

    first = id_cols[:7] + ["n_variables_available", "pct_variables_available"] + id_cols[7:]
    rest = sorted([c for c in wide.columns if c not in first])
    wide = wide[first + rest]
    trace = trace.sort_values(["iso3", "variable_matriz"]).reset_index(drop=True)
    return wide, trace


def build_temporal_rules_table() -> pd.DataFrame:
    return pd.DataFrame([
        {"source_id": src, "default_rule": rule, "notes": notes}
        for src, (rule, notes) in TEMPORAL_RULES.items()
    ])


def _select_row(group: pd.DataFrame, rule: str) -> pd.Series | None:
    if len(group) == 0:
        return None
    with_year = group[group["year"].notna()].copy()
    if rule == "cross_section" or len(with_year) == 0:
        return group.iloc[0]
    if rule == "year_2025_if_available":
        y2025 = with_year[with_year["year"].eq(2025)]
        if len(y2025):
            return y2025.iloc[0]
    return with_year.sort_values("year").iloc[-1]


def _years_collapsed(group: pd.DataFrame) -> str:
    years = sorted({int(y) for y in group["year"].dropna().tolist()})
    return ",".join(str(y) for y in years)


def _temporal_warning(row: pd.Series, rule: str) -> str:
    if pd.isna(row.get("year")):
        return ""
    year = int(row["year"])
    return "older_than_2022" if year < 2022 and rule != "cross_section" else ""


def _join_unique(s: pd.Series, limit: int | None = None) -> str:
    vals = [str(v) for v in s.dropna().astype(str).unique().tolist() if str(v)]
    if limit is not None and len(vals) > limit:
        return "; ".join(vals[:limit]) + f"; ... (+{len(vals)-limit})"
    return "; ".join(vals)


def _mode(s: pd.Series) -> str:
    m = s.dropna().mode()
    return str(m.iloc[0]) if len(m) else "unknown"


def _infer_type(group: pd.DataFrame, unit: str) -> str:
    if unit == "binary":
        return "binary"
    if unit in {"categorical", "text"}:
        return "categorical"
    text_non_null = group["value_text"].dropna()
    if len(text_non_null) and group["value_numeric"].notna().sum() == 0:
        return "categorical"
    return "numeric"


def _block_for(source_id: str, variable: str, table_id: str) -> str:
    text = f"{variable} {table_id}".lower()
    if source_id == "iapp":
        return "regulatory_treatment"
    if source_id == "microsoft":
        return "adoption_diffusion"
    if source_id == "oxford":
        return "ecosystem_outcome"
    if source_id == "wipo":
        if any(k in text for k in ["out_", "brand", "crea", "pat", "scite", "gii_score", "wikiedit", "industdes", "utilmod"]):
            return "ecosystem_outcome"
        if any(k in text for k in ["goveff", "regqua", "ruleol", "polstab", "ease", "credit", "market"]):
            return "institutional_control"
        if any(k in text for k in ["tertenrol", "scienggrad", "pisa", "expedu", "rdexp", "research"]):
            return "socioeconomic_control"
        return "tech_infrastructure_control"
    if source_id == "anthropic":
        return "socioeconomic_control" if "gdp" in text else "adoption_diffusion"
    if source_id == "stanford":
        return "regulatory_treatment" if "fig_3" in text else "ecosystem_outcome"
    if source_id == "oecd":
        if any(k in text for k in ["digital_stri", "regulatory_gov", "fdi_restrictiveness", "pmr"]):
            return "institutional_control"
        if any(k in text for k in ["ict_business"]):
            return "adoption_diffusion"
        if any(k in text for k in ["gbard", "rd_tax"]):
            return "socioeconomic_control"
        return "tech_infrastructure_control"
    if source_id == "wb":
        if any(k in text for k in ["corruption", "effectiveness", "stability", "regulatory", "rule_of_law", "voice"]):
            return "institutional_control"
        if any(k in text for k in ["internet", "broadband", "electric", "patent"]):
            return "tech_infrastructure_control"
        return "socioeconomic_control"
    return "socioeconomic_control"


def _redundant_with(variable: str) -> str:
    groups = {
        "wb_tertiary_education_enrollment": "wipo_tertenrol_score",
        "wipo_tertenrol_score": "wb_tertiary_education_enrollment",
        "anthropic_gdp_total": "wb_gdp_current_usd",
        "wb_gdp_current_usd": "anthropic_gdp_total",
        "wb_government_effectiveness": "wipo_goveff_score; oxford_ind_govt_effectiveness",
        "wipo_goveff_score": "wb_government_effectiveness; oxford_ind_govt_effectiveness",
        "oxford_ind_govt_effectiveness": "wb_government_effectiveness; wipo_goveff_score",
        "wb_regulatory_quality": "wipo_regqua_score; oxford_ind_regulatory_quality",
        "wipo_regqua_score": "wb_regulatory_quality; oxford_ind_regulatory_quality",
        "oxford_ind_regulatory_quality": "wb_regulatory_quality; wipo_regqua_score",
    }
    return groups.get(variable, "")


def _is_primary(variable: str, source_id: str) -> bool:
    non_primary = {
        "anthropic_gdp_total", "wipo_tertenrol_score", "wipo_goveff_score",
        "oxford_ind_govt_effectiveness", "wipo_regqua_score", "oxford_ind_regulatory_quality",
    }
    return variable not in non_primary


def _fase4_role(variable: str, source_id: str, block: str, pct: float) -> str:
    if variable.endswith("_se"):
        return "supporting_context"
    if pct < 10 and block != "regulatory_treatment":
        return "excluded_from_eda"
    if source_id in {"iapp", "microsoft"} or variable in {
        "oxford_total_score", "wipo_gii_score", "wb_gdp_current_usd",
        "wb_gdp_per_capita_ppp", "wb_government_effectiveness", "wb_regulatory_quality",
        "wb_rule_of_law",
    }:
        return "core_eda"
    if block in {"regulatory_treatment", "ecosystem_outcome", "socioeconomic_control", "institutional_control"} and pct >= 30:
        return "core_eda"
    return "supporting_context"


def _known_limitations(variable: str, pct: float) -> str:
    notes = []
    if pct < 30:
        notes.append("low_coverage_under_30pct_requires_fase4_caution")
    if variable.endswith("_se"):
        notes.append("standard_error_not_primary_substantive_indicator")
    if variable.startswith("wipo_"):
        notes.append("wipo_score_scale_0_100_not_raw_indicator")
    return "; ".join(notes)
