"""
build_rankings_2019.py — Pasos 6.1 + 6.2 + 6.3
Parsea la hoja Rankings de 2019 (7 regiones lado a lado)
y construye hoja Rankings_Regionales_2019.
Output: UNIFICADO/output/rankings_regionales_2019.csv
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

YEAR = 2019
df = read_sheet(YEAR, "Rankings", header=None)
df_iso = pd.read_csv(output_path("iso3_mapping.csv"))

# Step 6.1: Understand layout
# Row 1 (index 0): Region headers
# Row 2 (index 1): Sub-headers (Rank, Country, Score per region)
# Row 3+ (index 2+): Data
# Each region block = 3 columns (Rank, Country, Score)

# Region blocks: col start positions
# Col 0: Global (Rank), Col 1: Global (Country), Col 2: Global (Score)
# Col 3: Asia-Pacific (Rank), Col 4: Asia-Pacific (Country), Col 5: Asia-Pacific (Score)
# Col 6: Africa (Rank), Col 7: Africa (Country), Col 8: Africa (Score)
# Col 9: Latin America (Rank), Col 10: Latin America (Country), Col 11: Latin America (Score)
# Col 12: North America (Rank), Col 13: North America (Country), Col 14: North America (Score)
# Col 15: Eastern Europe (Rank), Col 16: Eastern Europe (Country), Col 17: Eastern Europe (Score)
# Col 18: Australia/NZ (Rank), Col 19: Australia/NZ (Country), Col 20: Australia/NZ (Score)
# Col 21: Western Europe (Rank), Col 22: Western Europe (Country), Col 23: Western Europe (Score)

print("=== Step 6.1: Layout parseado ===")
regions = {
    "global": (0, 1, 2),
    "asia_pacific": (4, 5, 6),
    "africa": (8, 9, 10),
    "latam": (12, 13, 14),
    "north_america": (16, 17, 18),
    "eastern_europe": (20, 21, 22),
    "australasia": (24, 25, 26),
    "western_europe": (28, 29, 30),
}

for region_name, (col_rank, col_country, col_score) in regions.items():
    sample_country = df.iloc[2, col_country]
    sample_score = df.iloc[2, col_score]
    print(f"  {region_name}: col rank={col_rank}, country={col_country}, score={col_score}  |  eg: {sample_country} = {sample_score}")

# Step 6.2: Extract data
# Build a dict mapping each country to its regional entries
print("\n=== Step 6.2: Extrayendo datos por region ===")

# We'll build a flat table: one row per country-region appearance
# But each country appears in exactly ONE region, so we need to find its home region
all_entries = {}  # {country_name: {region: {rank, score}}}

# Additional name variants for Rankings sheet (different naming from Data sheet)
rankings_name_map = {
    "Bolivia": "Bolivia (Plurinational State of)",
    "Brunei": "Brunei Darussalam",
    "Cape Verde": "Cabo Verde",
    "Czech Republic": "Czechia",
    "Ivory Coast": "Côte d'Ivoire",
    "Laos": "Lao People's Democratic Republic",
    "Micronesia": "Micronesia (Federated States of)",
    "Moldova": "Republic of Moldova",
    "North Korea": "Democratic People's Republic of Korea",
    "Republic of North Macedonia": "North Macedonia",
    "Russia": "Russian Federation",
    "South Korea": "Republic of Korea",
    "Syria": "Syrian Arab Republic",
    "Swaziland": "Eswatini",
    "Tanzania": "United Republic of Tanzania",
    "Vietnam": "Viet Nam",
    "The former Yugoslav Republic of Macedonia": "North Macedonia",
}

for region_name, (col_rank, col_country, col_score) in regions.items():
    for i in range(2, len(df)):
        country_val = df.iloc[i, col_country]
        if pd.isna(country_val):
            continue
        country_str = clean_country(country_val)
        if country_str == "":
            continue
        # Skip non-country rows
        if country_str.upper() == "AVERAGE" or country_str == "Average" or country_str == "Max Score":
            continue
        # Map to canonical name from Data sheet if possible
        if country_str in rankings_name_map:
            country_str = rankings_name_map[country_str]

        if country_str not in all_entries:
            all_entries[country_str] = {}

        rank_val = df.iloc[i, col_rank]
        score_val = df.iloc[i, col_score]

        all_entries[country_str][region_name] = {
            "rank": float(rank_val) if pd.notna(rank_val) else np.nan,
            "score": float(score_val) if pd.notna(score_val) else np.nan,
        }

print(f"  Total entries encontradas: {len(all_entries)}")

# Determine each country's home region (where it has a score AND it's NOT global)
home_regions = {}
for country, entries in all_entries.items():
    # Home region is the NON-global region where this country has data
    for region in ["asia_pacific", "africa", "latam", "north_america",
                    "eastern_europe", "australasia", "western_europe"]:
        if region in entries and pd.notna(entries[region]["score"]):
            home_regions[country] = region
            break
    if country not in home_regions:
        # Geographic fallback for countries not in any regional block
        fallback_region = {
            "Kiribati": "asia_pacific",
        }
        home_regions[country] = fallback_region.get(country, "unknown")

# Step 6.3: Build output
print("\n=== Step 6.3: Construyendo output ===")
rows = []
for country, entries in all_entries.items():
    row = {"pais_original": country}
    for region_name in regions.keys():
        if region_name in entries:
            row[f"rank_{region_name}"] = entries[region_name]["rank"]
            row[f"score_{region_name}"] = entries[region_name]["score"]
        else:
            row[f"rank_{region_name}"] = np.nan
            row[f"score_{region_name}"] = np.nan
    row["region_pertenece"] = home_regions.get(country, "unknown")
    rows.append(row)

df_out = pd.DataFrame(rows)

# Add iso3
df_out = df_out.merge(df_iso[["pais_original", "iso3", "entity_type"]],
                      on="pais_original", how="left")

ordered = ["iso3", "entity_type", "pais_original", "region_pertenece"]
for region_name in regions.keys():
    ordered.append(f"rank_{region_name}")
    ordered.append(f"score_{region_name}")

df_out = df_out[ordered]

# Validate
validate_row_count(df_out, EXPECTED_COUNTS[YEAR], "Rankings_Regionales_2019")
print(f"  Columnas: {len(ordered)}")
print(f"  iso3 missing: {df_out['iso3'].isna().sum()}")

# Distribution of home regions
print("\n  Distribucion por region de pertenencia:")
for region, count in df_out["region_pertenece"].value_counts().items():
    print(f"    {region}: {count} paises")

out_path = output_path("rankings_regionales_2019.csv")
df_out.to_csv(out_path, index=False)
print(f"\nGuardado: {out_path}")
