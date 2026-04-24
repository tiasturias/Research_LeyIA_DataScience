"""
Derive deterministic X2 controls: oecd_member and region.

These are not sourced from external APIs — they are static lookups by iso3.
- oecd_member: binary (1/0) from the official OECD membership list (38 members as of 2024)
- region: categorical from WIPO GII region_un, with manual fills for TWN and BLZ

Output: data/interim/derived_controls.csv
"""

import pandas as pd
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent

# ── OECD members (38 as of 2024-12) ─────────────────────────────────────────
OECD_MEMBERS = {
    "AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE",
    "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN", "ISL",
    "IRL", "ISR", "ITA", "JPN", "KOR", "LVA", "LTU", "LUX",
    "MEX", "NLD", "NZL", "NOR", "POL", "PRT", "SVK", "SVN",
    "ESP", "SWE", "CHE", "TUR", "GBR", "USA",
}

# ── Manual region fills for countries missing from WIPO ──────────────────────
MANUAL_REGION = {
    "TWN": "South East Asia, East Asia, and Oceania",
    "BLZ": "Latin America and the Caribbean",
}


def build():
    # Load the 86 study iso3 codes from IAPP baseline
    iapp = pd.read_csv(BASE / "data/raw/IAPP/iapp_x1_core.csv", usecols=["iso3"])
    iso3_list = sorted(iapp["iso3"].unique())

    # Load WIPO region_un mapping
    wipo = pd.read_csv(BASE / "data/raw/WIPO Global Innovation Index/wipo_gii_snapshot_latest.csv",
                        usecols=["iso3", "region_un"])
    wipo_map = wipo.drop_duplicates("iso3").set_index("iso3")["region_un"].to_dict()

    rows = []
    for iso3 in iso3_list:
        region = wipo_map.get(iso3) or MANUAL_REGION.get(iso3)
        if region is None:
            print(f"WARNING: no region for {iso3}")
        rows.append({
            "iso3": iso3,
            "oecd_member": 1 if iso3 in OECD_MEMBERS else 0,
            "region": region,
        })

    df = pd.DataFrame(rows)

    out_path = BASE / "data/interim/derived_controls.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)

    # Summary
    print(f"Derived controls: {len(df)} countries")
    print(f"  oecd_member=1: {df['oecd_member'].sum()}")
    print(f"  oecd_member=0: {(df['oecd_member']==0).sum()}")
    print(f"  Regions: {df['region'].value_counts().to_dict()}")
    print(f"  Missing region: {df['region'].isna().sum()}")
    print(f"Saved to {out_path}")
    return df


if __name__ == "__main__":
    build()
