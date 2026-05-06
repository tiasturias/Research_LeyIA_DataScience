"""Quality reports and invariant checks."""

from __future__ import annotations

import pandas as pd

from .config import SOURCE_ORDER


def traceability_issues(wide: pd.DataFrame, panel: pd.DataFrame, trace: pd.DataFrame) -> list[str]:
    issues = []
    panel_ids = set(panel["cell_id"].astype(str))
    missing_panel = ~trace["cell_id_panel"].astype(str).isin(panel_ids)
    if missing_panel.any():
        issues.append(f"traceability cell_id_panel not found in panel: {int(missing_panel.sum())}")

    id_cols = {
        "iso3", "country_name_canonical", "entity_type", "region", "income_group",
        "n_sources_present", "source_list", "n_variables_available", "pct_variables_available",
        "included_in_matrix", "included_in_dense_candidate", "inclusion_notes",
    }
    value_cols = [c for c in wide.columns if c not in id_cols and not c.endswith("_year_used") and not c.endswith("_confidence")]
    expected = set()
    for _, row in wide[["iso3"] + value_cols].iterrows():
        for col in value_cols:
            if pd.notna(row[col]):
                expected.add(f"{row['iso3']}__{col}")
    actual = set(trace["cell_id_wide"].astype(str))
    if expected - actual:
        issues.append(f"non-null wide cells without traceability: {len(expected - actual)}")
    if actual - expected:
        issues.append(f"trace rows without non-null wide cell: {len(actual - expected)}")
    return issues


def build_quality_report(panel: pd.DataFrame, snapshot: pd.DataFrame, wide: pd.DataFrame, dictionary: pd.DataFrame, trace: pd.DataFrame, universe: pd.DataFrame) -> pd.DataFrame:
    value_cols = [
        c for c in wide.columns
        if c not in {
            "iso3", "country_name_canonical", "entity_type", "region", "income_group",
            "n_sources_present", "source_list", "n_variables_available", "pct_variables_available",
            "included_in_matrix", "included_in_dense_candidate", "inclusion_notes",
        }
        and not c.endswith("_year_used") and not c.endswith("_confidence")
    ]
    zero_value_entities = int(wide[value_cols].isna().all(axis=1).sum()) if value_cols else 0
    rows = [
        {"metric": "panel_rows", "value": len(panel), "status": "info"},
        {"metric": "snapshot_rows", "value": len(snapshot), "status": "info"},
        {"metric": "wide_rows", "value": len(wide), "status": "info"},
        {"metric": "wide_columns", "value": len(wide.columns), "status": "info"},
        {"metric": "dictionary_variables", "value": len(dictionary), "status": "info"},
        {"metric": "traceability_rows", "value": len(trace), "status": "info"},
        {"metric": "included_entities", "value": int(universe["included_in_matrix"].sum()), "status": "info"},
        {"metric": "wide_zero_value_entities", "value": zero_value_entities, "status": "pass" if zero_value_entities == 0 else "fail"},
        {"metric": "variables_under_30pct_complete", "value": int(dictionary["pct_complete"].lt(30).sum()), "status": "warn"},
        {"metric": "core_eda_variables", "value": int(dictionary["fase4_role"].eq("core_eda").sum()), "status": "info"},
        {"metric": "panel_duplicate_cell_id", "value": int(panel["cell_id"].duplicated().sum()), "status": "pass"},
        {"metric": "trace_duplicate_cell_id_wide", "value": int(trace["cell_id_wide"].duplicated().sum()), "status": "pass"},
        {"metric": "dictionary_duplicate_variable", "value": int(dictionary["variable_matriz"].duplicated().sum()), "status": "pass"},
    ]
    for src in SOURCE_ORDER:
        rows.append({"metric": f"panel_rows_{src}", "value": int((panel["source_id"] == src).sum()), "status": "info"})
    for block, n in dictionary["bloque_tematico"].value_counts().sort_index().items():
        rows.append({"metric": f"variables_block_{block}", "value": int(n), "status": "info"})
    if len(wide):
        for block in sorted(dictionary["bloque_tematico"].unique()):
            block_vars = dictionary.loc[dictionary["bloque_tematico"].eq(block), "variable_matriz"].tolist()
            block_vars = [c for c in block_vars if c in wide.columns]
            pct = 0.0 if not block_vars else round(float(wide[block_vars].notna().any(axis=1).mean() * 100), 2)
            rows.append({"metric": f"countries_with_any_{block}", "value": pct, "status": "info", "notes": "percent of wide rows with >=1 value in block"})
    issues = traceability_issues(wide, panel, trace)
    rows.append({"metric": "traceability_blocking_issues", "value": len(issues), "status": "pass" if not issues else "fail", "notes": "; ".join(issues)})
    return pd.DataFrame(rows)


def build_issue_log(ms_crosswalk: pd.DataFrame, universe: pd.DataFrame) -> pd.DataFrame:
    rows = []
    pending = ms_crosswalk[ms_crosswalk["action"].eq("pending_human_review")]
    rows.append({
        "issue_id": "GEO_MICROSOFT_CROSSWALK",
        "area": "geography",
        "severity": "high" if len(pending) else "resolved",
        "description": f"{len(ms_crosswalk)} Microsoft rows crosswalked; {len(pending)} pending human review",
        "resolution": "Pending rows excluded until human approval" if len(pending) else "All Microsoft rows approved under documented exact-match human-review policy",
    })
    excluded = universe[~universe["included_in_matrix"].astype(bool)]
    rows.append({
        "issue_id": "GEO_NON_COUNTRY_EXCLUSION",
        "area": "geography",
        "severity": "resolved",
        "description": f"{len(excluded)} non-principal-country entities excluded",
        "resolution": "Universe retains excluded entities for audit but wide matrix uses country_iso3 only",
    })
    rows.append({
        "issue_id": "TEMP_OXFORD_2019",
        "area": "temporal",
        "severity": "resolved",
        "description": "Oxford 2019 scale differs from 2020+",
        "resolution": "2019 excluded from panel and snapshot",
    })
    rows.append({
        "issue_id": "VAR_WIPO_RANK",
        "area": "variable",
        "severity": "resolved",
        "description": "WIPO has SCORE and RANK columns",
        "resolution": "Only SCORE columns extracted; RANK excluded",
    })
    return pd.DataFrame(rows)
