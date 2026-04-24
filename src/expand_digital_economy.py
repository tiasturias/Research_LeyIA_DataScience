"""
Fetch digital economy proxy indicators from World Bank WDI for all 86 study
countries.

Context (Tarea A sub-task A.5, 2026-04):
    UNCTAD's Digital Economy Report does NOT publish country-level
    "digital economy as % of GDP" for the 86 study countries. UNCTAD reports
    such figures only globally (~15% GDP) and regionally. For country-level
    analysis, we use two complementary WDI proxies:

      - BX.GSR.CCIS.ZS : ICT service exports (% of service exports)
        Captures the "size" of the digital services export economy (software,
        telecom, computer services). Key proxy for digital economy intensity.

      - TX.VAL.TECH.MF.ZS : High-technology exports (% of manufactured exports)
        Captures the "advanced-technology manufacturing" dimension (aerospace,
        computers, pharma, scientific instruments).

    These two proxies are non-redundant with `internet_penetration` (WDI
    already included) which measures digital CONSUMPTION / access. The new
    variables measure digital PRODUCTION / export capacity.

Output:
    data/raw/World Bank WDI/digital_economy_86.csv  (raw panel, wide format)

Temporal window: 2019-2024 (latest available per variable).

Coverage expectation: ~75-80/86 (lower than core WDI controls due to
reporting gaps in ICT trade statistics from emerging economies).
"""

import pandas as pd
import pathlib
import wbgapi as wb

BASE = pathlib.Path(__file__).resolve().parent.parent

# All 86 study countries (minus TWN which is absent from WB API per D-004)
STUDY_ISO3 = sorted(
    pd.read_csv(
        BASE / "data/raw/IAPP/iapp_x1_core.csv", usecols=["iso3"]
    )["iso3"].unique()
)
FETCHABLE = [c for c in STUDY_ISO3 if c != "TWN"]

# WDI indicator codes → canonical names
DIGITAL_INDICATORS = {
    "BX.GSR.CCIS.ZS": "ict_service_exports_pct",
    "TX.VAL.TECH.MF.ZS": "high_tech_exports_pct",
}

WINDOW_START = 2019
WINDOW_END = 2024


def build():
    series_codes = list(DIGITAL_INDICATORS.keys())
    print(f"Fetching {len(series_codes)} digital economy indicators for "
          f"{len(FETCHABLE)} countries ({WINDOW_START}-{WINDOW_END})...")

    records = list(wb.data.fetch(
        series_codes,
        FETCHABLE,
        time=range(WINDOW_START, WINDOW_END + 1),
    ))
    print(f"  Raw records fetched: {len(records)}")

    rows = []
    for r in records:
        rows.append({
            "iso3": r["economy"],
            "year": int(r["time"].replace("YR", "")),
            "canonical_name": DIGITAL_INDICATORS[r["series"]],
            "value": r["value"],
        })

    long_df = pd.DataFrame(rows)

    wide = long_df.pivot_table(
        index=["iso3", "year"],
        columns="canonical_name",
        values="value",
        aggfunc="first",
    ).reset_index()
    wide.columns.name = None

    raw_path = BASE / "data/raw/World Bank WDI/digital_economy_86.csv"
    wide.to_csv(raw_path, index=False)
    print(f"\n  Wrote {raw_path.name}: {len(wide)} rows, "
          f"{wide['iso3'].nunique()} countries")

    print(f"\n  Country coverage per indicator (any year in window):")
    for col in DIGITAL_INDICATORS.values():
        if col in wide.columns:
            n = wide[wide[col].notna()]["iso3"].nunique()
            print(f"    {col:30s}: {n}/86 (TWN excluded from WB API)")

    return wide


if __name__ == "__main__":
    build()
