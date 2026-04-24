"""
Standardise Stanford AI Index Y variables (patents, startups, investment) into iso3-keyed files.

Sources:
  - fig_1.2.4.csv : Granted AI patents per 100k inhabitants, 2023 (55 geos)
  - fig_4.3.8.csv : AI investment by country, 2024 (67 geos)
  - fig_4.3.9.csv : AI investment cumulative 2013-24 (91 geos)
  - fig_4.3.12.csv: Newly funded AI companies, 2024 (62 geos)
  - fig_4.3.13.csv: Newly funded AI companies cumulative 2013-2024 (91 geos)

Output:
  - data/interim/stanford_ai_patents.csv
  - data/interim/stanford_ai_investment.csv
  - data/interim/stanford_ai_startups.csv
"""

import pandas as pd
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent

# ── Stanford geographic label → iso3 mapping ─────────────────────────────────
# Only includes entities that map to the 86 study countries.
GEO_TO_ISO3 = {
    "Argentina": "ARG", "Armenia": "ARM", "Australia": "AUS", "Austria": "AUT",
    "Bahrain": "BHR", "Bangladesh": "BGD", "Barbados": "BRB", "Belarus": "BLR",
    "Belgium": "BEL", "Belize": "BLZ", "Brazil": "BRA", "Bulgaria": "BGR",
    "Cameroon": "CMR", "Canada": "CAN", "Chile": "CHL", "China": "CHN",
    "Colombia": "COL", "Costa Rica": "CRI", "Croatia": "HRV", "Cyprus": "CYP",
    "Czech Republic": "CZE", "Denmark": "DNK", "Ecuador": "ECU", "Egypt": "EGY",
    "Estonia": "EST", "Finland": "FIN", "France": "FRA", "Germany": "DEU",
    "Ghana": "GHA", "Greece": "GRC", "Hungary": "HUN", "Iceland": "ISL",
    "India": "IND", "Indonesia": "IDN", "Ireland": "IRL", "Israel": "ISR",
    "Italy": "ITA", "Japan": "JPN", "Jordan": "JOR", "Kazakhstan": "KAZ",
    "Kenya": "KEN", "Latvia": "LVA", "Lebanon": "LBN", "Lithuania": "LTU",
    "Luxembourg": "LUX", "Malaysia": "MYS", "Malta": "MLT", "Mauritius": "MUS",
    "Mexico": "MEX", "Mongolia": "MNG", "Morocco": "MAR", "Netherlands": "NLD",
    "New Zealand": "NZL", "Nigeria": "NGA", "Norway": "NOR", "Pakistan": "PAK",
    "Panama": "PAN", "Peru": "PER", "Philippines": "PHL", "Poland": "POL",
    "Portugal": "PRT", "Romania": "ROU", "Russia": "RUS", "Saudi Arabia": "SAU",
    "Serbia": "SRB", "Seychelles": "SYC", "Singapore": "SGP",
    "Slovak Republic": "SVK", "Slovakia": "SVK", "Slovenia": "SVN",
    "South Africa": "ZAF", "South Korea": "KOR", "Spain": "ESP",
    "Sri Lanka": "LKA", "Sweden": "SWE", "Switzerland": "CHE",
    "Taiwan": "TWN", "Thailand": "THA", "Tunisia": "TUN", "Turkey": "TUR",
    "Uganda": "UGA", "Ukraine": "UKR", "United Arab Emirates": "ARE",
    "United Kingdom": "GBR", "United States": "USA", "Uruguay": "URY",
    "Viet Nam": "VNM", "Vietnam": "VNM",
}


def build_patents():
    """fig_1.2.4: Granted AI patents per 100k, 2023 snapshot."""
    df = pd.read_csv(BASE / "data/raw/STANFORD AI INDEX 25/1. Research and Development/Data/fig_1.2.4.csv")
    df = df.rename(columns={
        "Geographic Area": "geo",
        df.columns[1]: "ai_patents_per100k",
    })
    df["iso3"] = df["geo"].map(GEO_TO_ISO3)
    mapped = df[df["iso3"].notna()].copy()
    unmapped = df[df["iso3"].isna()]
    if len(unmapped):
        print(f"  Patents unmapped geos: {unmapped['geo'].tolist()}")
    out = mapped[["iso3", "ai_patents_per100k"]].copy()
    out["year"] = 2023
    out["source"] = "Stanford_AI_Index_25_fig_1.2.4"
    return out


def build_investment():
    """fig_4.3.8 (2024) + fig_4.3.9 (cumulative 2013-24)."""
    econ = BASE / "data/raw/STANFORD AI INDEX 25/4. Economy/Data"

    # 2024 snapshot
    df8 = pd.read_csv(econ / "fig_4.3.8.csv")
    df8 = df8.rename(columns={
        "Geographic area": "geo",
        df8.columns[1]: "ai_investment_usd_bn_2024",
    })
    df8["iso3"] = df8["geo"].map(GEO_TO_ISO3)

    # Cumulative 2013-24
    df9 = pd.read_csv(econ / "fig_4.3.9.csv")
    df9 = df9.rename(columns={
        "Geographic area": "geo",
        df9.columns[1]: "ai_investment_usd_bn_cumulative",
    })
    df9["iso3"] = df9["geo"].map(GEO_TO_ISO3)

    m8 = df8[df8["iso3"].notna()][["iso3", "ai_investment_usd_bn_2024"]]
    m9 = df9[df9["iso3"].notna()][["iso3", "ai_investment_usd_bn_cumulative"]]
    merged = pd.merge(m9, m8, on="iso3", how="outer")
    merged["year"] = 2024
    merged["source"] = "Stanford_AI_Index_25_fig_4.3.8_4.3.9"

    unmapped8 = df8[df8["iso3"].isna()]
    unmapped9 = df9[df9["iso3"].isna()]
    if len(unmapped8):
        print(f"  Investment(8) unmapped: {unmapped8['geo'].tolist()}")
    if len(unmapped9):
        print(f"  Investment(9) unmapped: {unmapped9['geo'].tolist()}")
    return merged


def build_startups():
    """fig_4.3.12 (2024) + fig_4.3.13 (cumulative 2013-24)."""
    # 2024 snapshot
    df12 = pd.read_csv(BASE / "data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.3.12.csv")
    df12 = df12.rename(columns={
        "Geographic area": "geo",
        df12.columns[1]: "ai_startups_2024",
    })
    df12["iso3"] = df12["geo"].map(GEO_TO_ISO3)

    # Cumulative 2013-24
    df13 = pd.read_csv(BASE / "data/raw/STANFORD AI INDEX 25/4. Economy/Data/fig_4.3.13.csv")
    df13 = df13.rename(columns={
        "Geographic area": "geo",
        df13.columns[1]: "ai_startups_cumulative",
    })
    df13["iso3"] = df13["geo"].map(GEO_TO_ISO3)

    # Merge
    m12 = df12[df12["iso3"].notna()][["iso3", "ai_startups_2024"]]
    m13 = df13[df13["iso3"].notna()][["iso3", "ai_startups_cumulative"]]
    merged = pd.merge(m13, m12, on="iso3", how="outer")
    merged["year"] = 2024
    merged["source"] = "Stanford_AI_Index_25_fig_4.3.12_4.3.13"

    unmapped12 = df12[df12["iso3"].isna()]
    unmapped13 = df13[df13["iso3"].isna()]
    if len(unmapped12):
        print(f"  Startups(12) unmapped: {unmapped12['geo'].tolist()}")
    if len(unmapped13):
        print(f"  Startups(13) unmapped: {unmapped13['geo'].tolist()}")
    return merged


def build():
    print("Building Stanford patents...")
    patents = build_patents()
    pat_path = BASE / "data/interim/stanford_ai_patents.csv"
    patents.to_csv(pat_path, index=False)
    print(f"  {len(patents)} countries with AI patent data -> {pat_path}")

    print("Building Stanford investment...")
    investment = build_investment()
    inv_path = BASE / "data/interim/stanford_ai_investment.csv"
    investment.to_csv(inv_path, index=False)
    print(f"  {len(investment)} countries with AI investment data -> {inv_path}")

    print("Building Stanford startups...")
    startups = build_startups()
    su_path = BASE / "data/interim/stanford_ai_startups.csv"
    startups.to_csv(su_path, index=False)
    print(f"  {len(startups)} countries with startup data -> {su_path}")

    # Show coverage vs 86 study countries
    iapp = pd.read_csv(BASE / "data/raw/IAPP/iapp_x1_core.csv", usecols=["iso3"])
    study = set(iapp["iso3"])
    pat_cov = set(patents["iso3"]) & study
    inv_cov = set(investment["iso3"]) & study
    su_cov = set(startups["iso3"]) & study
    print(f"\nCoverage vs 86 study countries:")
    print(f"  ai_patents: {len(pat_cov)}/86")
    print(f"  ai_investment (cumulative): {investment['ai_investment_usd_bn_cumulative'].notna().sum()} total, {len(inv_cov)} study")
    print(f"  ai_investment (2024): {investment['ai_investment_usd_bn_2024'].notna().sum()} total")
    print(f"  ai_startups (cumulative): {startups['ai_startups_cumulative'].notna().sum()} total, {len(su_cov)} study")
    print(f"  ai_startups (2024): {startups['ai_startups_2024'].notna().sum()} total")

    # Missing
    print(f"\n  Missing patents: {sorted(study - pat_cov)}")
    print(f"  Missing investment: {sorted(study - inv_cov)}")
    print(f"  Missing startups: {sorted(study - su_cov)}")
    return patents, investment, startups


if __name__ == "__main__":
    build()
