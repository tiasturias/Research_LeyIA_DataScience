"""
Expand World Bank WGI (Worldwide Governance Indicators) coverage for the 22
study countries missing from the original wdi_governance.csv extraction.

Context:
    The original WGI raw file (data/raw/World Bank WDI/wdi_governance.csv)
    covered 63 of 86 study countries. The 23 expansion countries processed
    by expand_wdi.py were fetched from WB API v2 with series codes RQ.EST,
    RL.EST, GE.EST — which no longer resolve (404) because WGI was migrated
    to WB DataBank source=3 with new series codes GOV_WGI_*.EST.

    This script fetches the 22 expansion countries (TWN excluded — structural
    absence per D-004) using the correct WGI endpoint, covering:
      - regulatory_quality  (GOV_WGI_RQ.EST)  - CONFOUNDER CORE (added 2026-04)
      - rule_of_law         (GOV_WGI_RL.EST)  - CONFOUNDER CORE (added 2026-04)
      - government_effectiveness (GOV_WGI_GE.EST) - ROBUSTNESS (existing)
      - control_of_corruption (GOV_WGI_CC.EST) - auxiliary robustness

Output:
    data/raw/World Bank WDI/wgi_expansion_22.csv  (raw, wide format)

Temporal window: 2019-2023 (2023 is latest WGI publication as of 2026-04).
"""

import pandas as pd
import pathlib
import wbgapi as wb

BASE = pathlib.Path(__file__).resolve().parent.parent

# 22 study countries missing from original wdi_governance.csv extraction
# (TWN excluded — structural absence from WB per D-004)
MISSING_ISO3 = [
    "ARM", "BGD", "BHR", "BLR", "BLZ", "BRB", "ECU", "GHA",
    "KEN", "LBN", "LKA", "MAR", "MLT", "MNG", "MUS", "PAK",
    "PAN", "SRB", "SVK", "SYC", "UGA", "UKR",
]

# WGI series codes (db=3) → canonical names
WGI_INDICATORS = {
    "GOV_WGI_RQ.EST": "regulatory_quality",
    "GOV_WGI_RL.EST": "rule_of_law",
    "GOV_WGI_GE.EST": "government_effectiveness",
    "GOV_WGI_CC.EST": "control_of_corruption",
}

WINDOW_START = 2019
WINDOW_END = 2023


def build():
    series_codes = list(WGI_INDICATORS.keys())
    print(f"Fetching {len(series_codes)} WGI indicators for {len(MISSING_ISO3)} countries "
          f"({WINDOW_START}-{WINDOW_END}) via WB DataBank db=3...")

    records = list(wb.data.fetch(
        series_codes,
        MISSING_ISO3,
        time=range(WINDOW_START, WINDOW_END + 1),
        db=3,
    ))
    print(f"  Raw records fetched: {len(records)}")

    # Normalize: {'value': X, 'series': 'GOV_WGI_RQ.EST', 'economy': 'ARM', 'time': 'YR2023'}
    rows = []
    for r in records:
        rows.append({
            "iso3": r["economy"],
            "year": int(r["time"].replace("YR", "")),
            "wb_indicator": r["series"].replace("GOV_WGI_", ""),  # strip prefix → RQ.EST, etc.
            "canonical_name": WGI_INDICATORS[r["series"]],
            "value": r["value"],
        })

    long_df = pd.DataFrame(rows)

    # Pivot to wide format consistent with wdi_all_86.csv schema
    wide = long_df.pivot_table(
        index=["iso3", "year"],
        columns="canonical_name",
        values="value",
        aggfunc="first",
    ).reset_index()
    wide.columns.name = None

    raw_path = BASE / "data/raw/World Bank WDI/wgi_expansion_22.csv"
    wide.to_csv(raw_path, index=False)
    print(f"\n  Wrote {raw_path.name}: {len(wide)} rows, {wide['iso3'].nunique()} countries")

    # Coverage summary
    print(f"\n  Coverage per WGI indicator (latest in [{WINDOW_START},{WINDOW_END}]):")
    for col in WGI_INDICATORS.values():
        if col in wide.columns:
            n_countries = wide[wide[col].notna()]["iso3"].nunique()
            print(f"    {col:28s}: {n_countries}/{len(MISSING_ISO3)} expansion countries")

    return wide


if __name__ == "__main__":
    build()
