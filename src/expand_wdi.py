"""
Expand World Bank WDI data to cover the 23 countries missing from the original extraction.

Uses the World Bank API v2 to download the same indicators for the missing countries.
The original WDI extraction covered 63 countries (2013-2024).
This script fetches data for the remaining 23 study countries.

Output: data/raw/World Bank WDI/wdi_expansion_23.csv (raw)
        Merged into: data/interim/wdi_all_86.csv (combined)
"""

import pandas as pd
import requests
import time
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent

# The 23 missing countries from the original WDI extraction
MISSING_ISO3 = [
    "ARM", "BGD", "BHR", "BLR", "BLZ", "BRB", "ECU", "GHA",
    "KEN", "LBN", "LKA", "MAR", "MLT", "MNG", "MUS", "PAK",
    "PAN", "SRB", "SVK", "SYC", "TWN", "UGA", "UKR",
]

# WDI indicator codes → canonical names
INDICATORS = {
    "NY.GDP.PCAP.PP.CD": "gdp_per_capita_ppp",
    "GB.XPD.RSDV.GD.ZS": "rd_expenditure",
    "IT.NET.USER.ZS": "internet_penetration",
    "SE.TER.ENRR": "tertiary_education",
    "GE.EST": "government_effectiveness",
    "RQ.EST": "regulatory_quality",
    "RL.EST": "rule_of_law",
}

# Additional useful indicators (from original extraction)
EXTRA_INDICATORS = {
    "SP.POP.TOTL": "population",
    "NY.GDP.MKTP.CD": "gdp_current_usd",
    "SL.UEM.TOTL.ZS": "unemployment_rate",
    "SL.TLF.TOTL.IN": "labor_force",
}


def fetch_wdi(iso3_list, indicator_code, start_year=2013, end_year=2024):
    """Fetch WDI data from World Bank API v2, with pagination."""
    countries = ";".join(iso3_list)
    all_records = []
    page = 1
    while True:
        url = (
            f"https://api.worldbank.org/v2/country/{countries}"
            f"/indicator/{indicator_code}"
            f"?date={start_year}:{end_year}&format=json&per_page=1000&page={page}"
        )
        try:
            r = requests.get(url, timeout=120)
            r.raise_for_status()
            data = r.json()
            if isinstance(data, list) and len(data) > 1 and data[1]:
                for rec in data[1]:
                    all_records.append({
                        "iso3": rec["countryiso3code"],
                        "year": int(rec["date"]),
                        "value": rec["value"],
                    })
                total_pages = data[0].get("pages", 1)
                if page >= total_pages:
                    break
                page += 1
            else:
                break
        except Exception as e:
            print(f"  ERROR fetching {indicator_code} page {page}: {e}")
            break
    return pd.DataFrame(all_records) if all_records else pd.DataFrame()


def build():
    all_indicators = {**INDICATORS, **EXTRA_INDICATORS}
    all_dfs = []

    # TWN won't be in World Bank API — handle separately
    fetchable = [c for c in MISSING_ISO3 if c != "TWN"]

    for code, name in all_indicators.items():
        print(f"  Fetching {name} ({code})...")
        df = fetch_wdi(fetchable, code)
        if not df.empty:
            df = df.rename(columns={"value": name})
            all_dfs.append(df)
            print(f"    {len(df)} records, {df['iso3'].nunique()} countries")
        time.sleep(0.5)  # Be polite to the API

    if not all_dfs:
        print("No data fetched!")
        return None

    # Merge all indicators into a single wide table
    merged = all_dfs[0]
    for df in all_dfs[1:]:
        merged = pd.merge(merged, df, on=["iso3", "year"], how="outer")

    merged.sort_values(["iso3", "year"], inplace=True)

    # Save raw expansion
    raw_path = BASE / "data/raw/World Bank WDI/wdi_expansion_23.csv"
    merged.to_csv(raw_path, index=False)
    print(f"\nRaw expansion: {len(merged)} rows, {merged['iso3'].nunique()} countries -> {raw_path}")

    # Combine with original WDI
    orig = pd.read_csv(BASE / "data/raw/World Bank WDI/wdi_all_indicators_wide.csv")
    # Keep only the columns that exist in the original
    common_cols = ["iso3", "year"] + [c for c in merged.columns if c in orig.columns and c not in ("iso3", "year")]
    expansion_aligned = merged[common_cols]

    combined = pd.concat([orig, expansion_aligned], ignore_index=True)
    combined.sort_values(["iso3", "year"], inplace=True)
    combined.drop_duplicates(subset=["iso3", "year"], keep="first", inplace=True)

    interim_path = BASE / "data/interim/wdi_all_86.csv"
    interim_path.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(interim_path, index=False)
    print(f"Combined: {len(combined)} rows, {combined['iso3'].nunique()} countries -> {interim_path}")

    # Coverage for core X2
    for col in INDICATORS.values():
        if col in combined.columns:
            cov = combined[combined[col].notna()]["iso3"].nunique()
            pct = combined[combined[col].notna()].shape[0] / len(combined) * 100
            print(f"  {col}: {cov} countries, {pct:.1f}% non-null")

    return combined


if __name__ == "__main__":
    build()
