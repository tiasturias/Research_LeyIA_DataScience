"""Consolida todos los CSVs de proxies en dos archivos master.

Lee los 5 CSVs raw generados por los scrapers:
    data/raw/proxies/jll_dc_outlook_2026.csv
    data/raw/proxies/eurostat_electricity_prices_2024_2025.csv
    data/raw/proxies/wri_aqueduct_2025.csv
    data/raw/proxies/worldbank_bready_2024_2025.csv
    data/raw/proxies/eu_eed_registry_2025.csv
    data/raw/proxies/country_dc_policies_pilots.csv

Genera:
    data/interim/proxy_infra_pilots.csv   — 6 pilotos × 33 variables
    data/interim/proxy_infra_universal.csv — Top 30 × 7 variables universales

Uso:
    python src/build_proxy_pilots_master.py
"""
from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "proxies"
INTERIM = ROOT / "data" / "interim"

PILOT_ISOS = ["SGP", "JPN", "FRA", "IRL", "GBR", "ESP"]

# Universal subset columns (propagable to top30_master.csv)
UNIVERSAL_COLS = [
    "iso3",
    "water_stress_score_2020",
    "water_stress_label",
    "time_construction_permit_days",
    "time_get_electricity_days",
    "industrial_electricity_price_eur_kwh_2024",
    "industrial_electricity_price_eur_kwh_2025",
]


def load_csv(path: Path, label: str) -> pd.DataFrame:
    """Load a CSV with error handling."""
    if not path.exists():
        log.warning("[master] %s not found: %s", label, path)
        return pd.DataFrame()
    df = pd.read_csv(path)
    log.info("[master] Loaded %s: %d rows × %d cols", label, len(df), len(df.columns))
    return df


def main():
    INTERIM.mkdir(parents=True, exist_ok=True)

    # Load all raw CSVs
    jll = load_csv(RAW / "jll_dc_outlook_2026.csv", "JLL DC Outlook")
    elec = load_csv(RAW / "eurostat_electricity_prices_2024_2025.csv", "Eurostat electricity")
    wri = load_csv(RAW / "wri_aqueduct_2025.csv", "WRI Aqueduct")
    wb = load_csv(RAW / "worldbank_bready_2024_2025.csv", "World Bank B-READY")
    eed = load_csv(RAW / "eu_eed_registry_2025.csv", "EU EED registry")
    policy = load_csv(RAW / "country_dc_policies_pilots.csv", "Country DC policies")

    # ------------------------------------------------------------------
    # Build pilots master (6 rows × all proxy variables)
    # ------------------------------------------------------------------
    dfs_to_merge = []

    # JLL: capacity, costs, pipeline
    if not jll.empty:
        jll_cols = [c for c in [
            "iso3", "dc_count_2024", "dc_count_2025",
            "dc_capacity_mw_2024", "dc_capacity_mw_2025", "dc_capacity_mw_2030_proj",
            "dc_construction_cost_per_watt_2026", "dc_pipeline_capacity_mw",
            "dc_yoy_growth_pct_2024_2025",
        ] if c in jll.columns]
        dfs_to_merge.append(jll[jll_cols])

    # EED: mandates
    if not eed.empty:
        eed_cols = [c for c in [
            "iso3", "dc_eu_eed_compliance_required",
            "dc_waste_heat_mandate", "dc_waste_heat_pct_required", "dc_waste_heat_year",
            "dc_renewable_mandate_pct", "dc_renewable_mandate_year",
            "dc_pue_max_mandate", "dc_pue_year",
        ] if c in eed.columns]
        dfs_to_merge.append(eed[eed_cols])

    # Policy: moratorium, grid, CNI, AIGZs
    if not policy.empty:
        pol_cols = [c for c in [
            "iso3",
            "dc_moratorium_year_start", "dc_moratorium_year_end", "dc_moratorium_active_2025",
            "grid_connection_wait_years", "grid_connection_fast_track_available",
            "grid_pipeline_request_gw",
            "dc_critical_infrastructure_designation", "dc_designation_year",
            "dc_planning_nsip_eligible", "dc_ai_growth_zones_program",
            "dc_subsidies_regional_program", "water_dc_use_published",
        ] if c in policy.columns]
        dfs_to_merge.append(policy[pol_cols])

    # Electricity prices
    if not elec.empty:
        elec_cols = [c for c in [
            "iso3",
            "industrial_electricity_price_eur_kwh_2024",
            "industrial_electricity_price_eur_kwh_2025",
        ] if c in elec.columns]
        dfs_to_merge.append(elec[elec_cols])

    # WRI water stress
    if not wri.empty:
        wri_cols = [c for c in [
            "iso3", "water_stress_score_2020", "water_stress_label",
        ] if c in wri.columns]
        dfs_to_merge.append(wri[wri_cols])

    # World Bank B-READY
    if not wb.empty:
        wb_cols = [c for c in [
            "iso3", "time_construction_permit_days", "time_get_electricity_days",
        ] if c in wb.columns]
        dfs_to_merge.append(wb[wb_cols])

    if not dfs_to_merge:
        log.error("[master] No input data found. Run scrapers first.")
        return

    # Merge all on iso3, starting from JLL (pilots only) or WRI (universal)
    pilots_base = pd.DataFrame({"iso3": PILOT_ISOS})
    master = pilots_base.copy()
    for df in dfs_to_merge:
        if df.empty:
            continue
        master = master.merge(df, on="iso3", how="left")

    # Deduplicate columns (in case multiple dfs have 'country' etc.)
    master = master.loc[:, ~master.columns.duplicated()]

    pilots_out = INTERIM / "proxy_infra_pilots.csv"
    master.to_csv(pilots_out, index=False)
    log.info("[master] proxy_infra_pilots.csv: %d rows × %d cols → %s",
             len(master), len(master.columns), pilots_out)

    # ------------------------------------------------------------------
    # Build universal subset (Top 30 × 7 vars) from WRI + WB + Electricity
    # ------------------------------------------------------------------
    universal_frames = []
    if not wri.empty:
        universal_frames.append(wri[["iso3", "water_stress_score_2020", "water_stress_label"]])
    if not wb.empty:
        universal_frames.append(wb[["iso3", "time_construction_permit_days", "time_get_electricity_days"]])
    if not elec.empty:
        universal_frames.append(elec[["iso3", "industrial_electricity_price_eur_kwh_2024",
                                       "industrial_electricity_price_eur_kwh_2025"]])

    if universal_frames:
        univ = universal_frames[0]
        for df in universal_frames[1:]:
            univ = univ.merge(df, on="iso3", how="outer")
        univ = univ.loc[:, ~univ.columns.duplicated()].sort_values("iso3").reset_index(drop=True)

        univ_out = INTERIM / "proxy_infra_universal.csv"
        univ.to_csv(univ_out, index=False)
        log.info("[master] proxy_infra_universal.csv: %d rows × %d cols → %s",
                 len(univ), len(univ.columns), univ_out)

    # ------------------------------------------------------------------
    # Print SGP row (user's priority for entrega de avance)
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SINGAPUR (SGP) — Proxy Variables Summary")
    print("=" * 70)
    sgp = master[master["iso3"] == "SGP"]
    if not sgp.empty:
        for col in master.columns:
            val = sgp.iloc[0][col]
            if pd.notna(val):
                print(f"  {col:<45} {val}")
    print("=" * 70)

    # Completeness report for all pilots
    print("\nCompleteness by pilot:")
    for iso3 in PILOT_ISOS:
        row = master[master["iso3"] == iso3]
        if not row.empty:
            filled = row.iloc[0].notna().sum()
            total = len(master.columns)
            print(f"  {iso3}: {filled}/{total} ({100*filled//total}%)")
    print()


if __name__ == "__main__":
    main()
