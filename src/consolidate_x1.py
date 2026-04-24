"""
Consolidate X1 regulatory variables from OECD (panel, 68 countries) + IAPP (snapshot, 86 countries).

Strategy:
  - OECD provides the panel backbone (2013–2024, 68 countries).
  - IAPP provides the latest cross-section for all 86 countries (Feb 2026 coding).
  - For the 18 IAPP-only countries, the IAPP snapshot is replicated as a single-year
    observation (year=2025) to capture their current regulatory state.
  - For the 68 overlapping countries, the OECD panel is preserved and the IAPP snapshot
    is appended as the 2025 row (latest authoritative coding).
  - Adds `regulatory_status_group` as a derived variable for comparative analysis.

Output: data/interim/x1_consolidated.csv
"""

import pandas as pd
import numpy as np
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent

# ── Regulatory status group mapping ──────────────────────────────────────────
# Maps regulatory_approach to a 4-level grouping for the "¿Regular o no regular?" analysis.
#   none          -> no_framework       (no AI-specific regulation)
#   light_touch   -> soft_framework     (voluntary guidelines, principles)
#   strategy_led  -> strategy_only      (national strategy, no binding regulation)
#   regulation_focused -> binding_regulation  (binding sectoral rules)
#   comprehensive -> binding_regulation (comprehensive binding law like EU AI Act)
STATUS_GROUP_MAP = {
    "none": "no_framework",
    "light_touch": "soft_framework",
    "strategy_led": "strategy_only",
    "regulation_focused": "binding_regulation",
    "comprehensive": "binding_regulation",
}


def build():
    # Load sources
    oecd = pd.read_csv(BASE / "data/raw/OECD/oecd_x1_core.csv")
    iapp = pd.read_csv(BASE / "data/raw/IAPP/iapp_x1_core.csv")

    x1_cols = [
        "iso3", "year", "has_ai_law", "regulatory_approach",
        "regulatory_intensity", "year_enacted", "enforcement_level",
        "thematic_coverage",
    ]

    # ── Prepare OECD panel ───────────────────────────────────────────────────
    oecd_panel = oecd[x1_cols].copy()

    # ── Prepare IAPP snapshot as year=2025 ───────────────────────────────────
    iapp_snap = iapp[["iso3", "has_ai_law", "regulatory_approach",
                       "regulatory_intensity", "year_enacted",
                       "enforcement_level", "thematic_coverage"]].copy()
    iapp_snap["year"] = 2025
    iapp_snap = iapp_snap[x1_cols]

    # ── Merge: OECD panel + IAPP 2025 row ───────────────────────────────────
    # Remove any existing 2025 rows in OECD to avoid duplication
    oecd_panel = oecd_panel[oecd_panel["year"] != 2025]
    consolidated = pd.concat([oecd_panel, iapp_snap], ignore_index=True)
    consolidated.sort_values(["iso3", "year"], inplace=True)

    # ── year_enacted: treat as structural NaN when has_ai_law == 0 ───────────
    # Convert empty strings to NaN
    consolidated["year_enacted"] = pd.to_numeric(
        consolidated["year_enacted"], errors="coerce"
    )

    # ── Derive regulatory_status_group ───────────────────────────────────────
    consolidated["regulatory_status_group"] = (
        consolidated["regulatory_approach"].map(STATUS_GROUP_MAP)
    )

    # ── Source provenance ────────────────────────────────────────────────────
    oecd_keys = set(zip(oecd["iso3"], oecd["year"])) if "year" in oecd.columns else set()
    consolidated["x1_source"] = consolidated.apply(
        lambda r: "IAPP" if r["year"] == 2025
        else ("OECD" if (r["iso3"], r["year"]) in oecd_keys else "IAPP"),
        axis=1,
    )

    # ── Save ─────────────────────────────────────────────────────────────────
    out_path = BASE / "data/interim/x1_consolidated.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    consolidated.to_csv(out_path, index=False)

    # ── Summary ──────────────────────────────────────────────────────────────
    print(f"X1 consolidated: {len(consolidated)} rows, {consolidated['iso3'].nunique()} countries")
    print(f"Years: {sorted(consolidated['year'].unique())}")
    print(f"Source breakdown: {consolidated['x1_source'].value_counts().to_dict()}")
    print()
    # Snapshot for 2025 (latest year)
    snap = consolidated[consolidated["year"] == 2025]
    print(f"2025 snapshot: {len(snap)} countries")
    print(f"  regulatory_approach: {snap['regulatory_approach'].value_counts().to_dict()}")
    print(f"  regulatory_status_group: {snap['regulatory_status_group'].value_counts().to_dict()}")
    print(f"  has_ai_law: {snap['has_ai_law'].value_counts().to_dict()}")
    print(f"  year_enacted non-null: {snap['year_enacted'].notna().sum()}")
    print(f"Saved to {out_path}")
    return consolidated


if __name__ == "__main__":
    build()
