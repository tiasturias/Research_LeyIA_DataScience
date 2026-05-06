"""Bloque B: Diagnóstico de calidad y missingness por país, variable, bloque, región."""

from __future__ import annotations

import pandas as pd
import numpy as np

from .config import BLOCKS, OUTPUTS_DIR
from .load import get_block_var_cols, get_variable_cols, load_dictionary, load_wide


def compute_missingness_by_variable(
    wide: pd.DataFrame, dictionary: pd.DataFrame
) -> pd.DataFrame:
    """Missingness por variable: n_non_null, pct_complete, bloque, source."""
    var_cols = get_variable_cols(wide, dictionary)
    records = []
    for vc in var_cols:
        n_total = len(wide)
        n_non_null = int(wide[vc].notna().sum())
        row = dictionary[dictionary["variable_matriz"] == vc]
        records.append({
            "variable_matriz": vc,
            "source_id": row["source_id"].iloc[0] if len(row) else "",
            "bloque_tematico": row["bloque_tematico"].iloc[0] if len(row) else "",
            "unit": row["unit"].iloc[0] if len(row) else "",
            "direction": row["direction"].iloc[0] if len(row) else "",
            "is_primary": row["is_primary"].iloc[0] if len(row) else None,
            "n_total": n_total,
            "n_non_null": n_non_null,
            "n_missing": n_total - n_non_null,
            "pct_complete": round(n_non_null / n_total * 100, 2),
            "pct_missing": round((n_total - n_non_null) / n_total * 100, 2),
        })
    return pd.DataFrame(records).sort_values("pct_complete", ascending=False).reset_index(drop=True)


def compute_missingness_by_country(
    wide: pd.DataFrame, dictionary: pd.DataFrame
) -> pd.DataFrame:
    """Missingness por país: cuántas variables tiene cada país."""
    var_cols = get_variable_cols(wide, dictionary)
    n_vars = len(var_cols)
    df = wide[["iso3", "country_name_canonical", "region", "income_group"]].copy()
    df["n_vars_total"] = n_vars
    df["n_vars_available"] = wide[var_cols].notna().sum(axis=1).astype(int)
    df["n_vars_missing"] = n_vars - df["n_vars_available"]
    df["pct_vars_available"] = (df["n_vars_available"] / n_vars * 100).round(2)

    # Por bloque
    for block in BLOCKS:
        b_cols = get_block_var_cols(block, wide, dictionary)
        if b_cols:
            df[f"pct_{block}"] = (wide[b_cols].notna().sum(axis=1) / len(b_cols) * 100).round(2)
        else:
            df[f"pct_{block}"] = 0.0

    df["n_blocks_with_data"] = sum(
        (df[f"pct_{b}"] > 0).astype(int) for b in BLOCKS
    )
    df["included_in_dense_candidate"] = wide["included_in_dense_candidate"]
    return df.sort_values("pct_vars_available", ascending=False).reset_index(drop=True)


def compute_missingness_by_block(
    wide: pd.DataFrame, dictionary: pd.DataFrame
) -> pd.DataFrame:
    """Missingness agregada por bloque: N variables, cobertura promedio."""
    records = []
    for block in BLOCKS:
        b_cols = get_block_var_cols(block, wide, dictionary)
        if not b_cols:
            continue
        n_vars = len(b_cols)
        coverage_per_var = wide[b_cols].notna().mean()
        records.append({
            "bloque_tematico": block,
            "n_variables": n_vars,
            "pct_complete_mean": round(coverage_per_var.mean() * 100, 2),
            "pct_complete_median": round(coverage_per_var.median() * 100, 2),
            "pct_complete_min": round(coverage_per_var.min() * 100, 2),
            "pct_complete_max": round(coverage_per_var.max() * 100, 2),
            "n_vars_above_70pct": int((coverage_per_var >= 0.70).sum()),
            "n_vars_above_30pct": int((coverage_per_var >= 0.30).sum()),
            "n_vars_below_30pct": int((coverage_per_var < 0.30).sum()),
            "n_countries_with_any_data": int(wide[b_cols].notna().any(axis=1).sum()),
            "pct_countries_with_any_data": round(wide[b_cols].notna().any(axis=1).mean() * 100, 2),
        })
        if block == "regulatory_treatment":
            iapp_cols = [c for c in b_cols if c.startswith("iapp_")]
            records[-1]["n_iapp_variables"] = len(iapp_cols)
            records[-1]["n_countries_with_any_iapp_data"] = int(wide[iapp_cols].notna().any(axis=1).sum()) if iapp_cols else 0
            records[-1]["pct_iapp_complete_mean"] = round(wide[iapp_cols].notna().mean().mean() * 100, 2) if iapp_cols else 0.0
        else:
            records[-1]["n_iapp_variables"] = 0
            records[-1]["n_countries_with_any_iapp_data"] = 0
            records[-1]["pct_iapp_complete_mean"] = np.nan
    return pd.DataFrame(records)


def compute_missingness_by_region(
    wide: pd.DataFrame, dictionary: pd.DataFrame
) -> pd.DataFrame:
    """Cobertura promedio por región geográfica y grupo de ingresos."""
    var_cols = get_variable_cols(wide, dictionary)
    n_vars = len(var_cols)
    wide_copy = wide.copy()
    wide_copy["pct_vars_available"] = wide[var_cols].notna().sum(axis=1) / n_vars * 100

    records = []
    for region, grp in wide_copy.groupby("region", dropna=False):
        records.append({
            "dimension": "region",
            "value": str(region) if pd.notna(region) else "Unknown",
            "n_countries": len(grp),
            "pct_vars_mean": round(grp["pct_vars_available"].mean(), 2),
            "pct_vars_median": round(grp["pct_vars_available"].median(), 2),
        })
    for ig, grp in wide_copy.groupby("income_group", dropna=False):
        records.append({
            "dimension": "income_group",
            "value": str(ig) if pd.notna(ig) else "Unknown",
            "n_countries": len(grp),
            "pct_vars_mean": round(grp["pct_vars_available"].mean(), 2),
            "pct_vars_median": round(grp["pct_vars_available"].median(), 2),
        })
    return pd.DataFrame(records).sort_values(["dimension", "pct_vars_mean"], ascending=[True, False]).reset_index(drop=True)


def compute_quality_overview(wide: pd.DataFrame, dictionary: pd.DataFrame) -> pd.DataFrame:
    """Resumen global de calidad de la Matriz Madre."""
    var_cols = get_variable_cols(wide, dictionary)
    n_vars = len(var_cols)
    n_countries = len(wide)

    total_cells = n_vars * n_countries
    non_null_cells = int(wide[var_cols].notna().sum().sum())

    rows = [
        {"metric": "n_countries", "value": n_countries, "status": "info"},
        {"metric": "n_variables", "value": n_vars, "status": "info"},
        {"metric": "total_cells", "value": total_cells, "status": "info"},
        {"metric": "non_null_cells", "value": non_null_cells, "status": "info"},
        {"metric": "pct_overall_coverage", "value": round(non_null_cells / total_cells * 100, 2), "status": "info"},
        {"metric": "n_vars_above_70pct", "value": int((wide[var_cols].notna().mean() >= 0.70).sum()), "status": "info"},
        {"metric": "n_vars_above_30pct", "value": int((wide[var_cols].notna().mean() >= 0.30).sum()), "status": "info"},
        {"metric": "n_vars_below_30pct", "value": int((wide[var_cols].notna().mean() < 0.30).sum()), "status": "warn"},
        {"metric": "chile_n_vars_available", "value": int(wide[wide["iso3"] == "CHL"][var_cols].notna().sum().sum()), "status": "info"},
        {"metric": "chile_pct_coverage", "value": round(wide[wide["iso3"] == "CHL"][var_cols].notna().sum().sum() / n_vars * 100, 2), "status": "info"},
    ]
    return pd.DataFrame(rows)


def run_coverage_analysis(
    wide: pd.DataFrame | None = None,
    dictionary: pd.DataFrame | None = None,
    save: bool = True,
) -> dict[str, pd.DataFrame]:
    """Ejecuta análisis completo de cobertura y retorna dict de DataFrames."""
    if wide is None:
        wide = load_wide()
    if dictionary is None:
        dictionary = load_dictionary()

    results = {
        "eda_quality_overview": compute_quality_overview(wide, dictionary),
        "eda_missingness_by_variable": compute_missingness_by_variable(wide, dictionary),
        "eda_missingness_by_country": compute_missingness_by_country(wide, dictionary),
        "eda_missingness_by_block": compute_missingness_by_block(wide, dictionary),
        "eda_missingness_by_region": compute_missingness_by_region(wide, dictionary),
    }

    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        for name, df in results.items():
            df.to_csv(OUTPUTS_DIR / f"{name}.csv", index=False)

    return results
