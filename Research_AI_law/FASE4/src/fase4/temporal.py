"""Bloque J: sensibilidad temporal snapshot vs panel."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import OUTPUTS_DIR
from .load import load_dictionary, load_panel, load_snapshot


def compute_year_used_distribution(snapshot: pd.DataFrame) -> pd.DataFrame:
    if "year_used" not in snapshot.columns:
        return pd.DataFrame([{"scope": "all", "year_used": np.nan, "n_cells": 0, "status": "year_used_missing"}])
    out = snapshot.groupby("year_used", dropna=False).size().reset_index(name="n_cells")
    out["pct_cells"] = (out["n_cells"] / out["n_cells"].sum() * 100).round(2)
    out["scope"] = "snapshot"
    return out[["scope", "year_used", "n_cells", "pct_cells"]]


def compute_temporal_stability(panel: pd.DataFrame, dictionary: pd.DataFrame) -> pd.DataFrame:
    numeric = panel.dropna(subset=["value_numeric"]).copy()
    numeric = numeric[numeric["variable_matriz"].isin(dictionary["variable_matriz"])]
    rows = []
    for var, grp in numeric.groupby("variable_matriz"):
        if grp["year"].nunique() < 2:
            rows.append({
                "variable_matriz": var,
                "n_countries": grp["iso3"].nunique(),
                "n_years": grp["year"].nunique(),
                "median_abs_yoy_change": np.nan,
                "status": "single_year_or_static",
            })
            continue
        g = grp.sort_values(["iso3", "year"])
        g["abs_yoy_change"] = g.groupby("iso3")["value_numeric"].diff().abs()
        rows.append({
            "variable_matriz": var,
            "n_countries": g["iso3"].nunique(),
            "n_years": g["year"].nunique(),
            "median_abs_yoy_change": round(float(g["abs_yoy_change"].median()), 6) if g["abs_yoy_change"].notna().any() else np.nan,
            "p90_abs_yoy_change": round(float(g["abs_yoy_change"].quantile(0.90)), 6) if g["abs_yoy_change"].notna().any() else np.nan,
            "status": "panel_variation_available",
        })
    return pd.DataFrame(rows)


def compute_snapshot_vs_panel(snapshot: pd.DataFrame, panel: pd.DataFrame) -> pd.DataFrame:
    snap = snapshot[["iso3", "variable_matriz", "year_used", "value_numeric"]].dropna(subset=["year_used"]).copy()
    snap["previous_year"] = snap["year_used"].astype(float) - 1
    prev = panel[["iso3", "variable_matriz", "year", "value_numeric"]].rename(columns={"value_numeric": "previous_value"})
    merged = snap.merge(
        prev,
        left_on=["iso3", "variable_matriz", "previous_year"],
        right_on=["iso3", "variable_matriz", "year"],
        how="left",
    )
    merged["abs_delta_previous_year"] = (merged["value_numeric"] - merged["previous_value"]).abs()
    rows = []
    for var, grp in merged.groupby("variable_matriz"):
        rows.append({
            "variable_matriz": var,
            "n_snapshot_cells": len(grp),
            "n_previous_year_available": int(grp["previous_value"].notna().sum()),
            "pct_previous_year_available": round(float(grp["previous_value"].notna().mean() * 100), 2),
            "median_abs_delta_previous_year": round(float(grp["abs_delta_previous_year"].median()), 6) if grp["abs_delta_previous_year"].notna().any() else np.nan,
            "status": "descriptive_temporal_check",
        })
    return pd.DataFrame(rows)


def run_temporal_analysis(
    panel: pd.DataFrame | None = None,
    snapshot: pd.DataFrame | None = None,
    dictionary: pd.DataFrame | None = None,
    save: bool = True,
) -> dict[str, pd.DataFrame]:
    if panel is None:
        panel = load_panel()
    if snapshot is None:
        snapshot = load_snapshot()
    if dictionary is None:
        dictionary = load_dictionary()
    outputs = {
        "eda_year_used_distribution": compute_year_used_distribution(snapshot),
        "eda_temporal_stability": compute_temporal_stability(panel, dictionary),
        "eda_snapshot_vs_panel": compute_snapshot_vs_panel(snapshot, panel),
    }
    if save:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        for name, df in outputs.items():
            df.to_csv(OUTPUTS_DIR / f"{name}.csv", index=False)
    return outputs
