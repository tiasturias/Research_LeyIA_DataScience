"""
iso3_mapping.py — Paso 0.2
Extrae todos los nombres de país de los 7 Excels fuente y construye el mapping a ISO3.
Output: UNIFICADO/output/iso3_mapping.csv
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd

# --- 1. Extraer nombres de país de cada año ---

all_country_names = {}  # {year: [list of country names]}

# 2019
df_2019 = read_sheet(2019, "Data", header=None)
# Countries start at row 7 (index 7), col 0
countries_2019 = []
for i in range(7, len(df_2019)):
    val = df_2019.iloc[i, 0]
    if pd.notna(val):
        countries_2019.append(clean_country(val))
all_country_names[2019] = countries_2019

# 2020
df_2020 = read_sheet(2020, "Detailed scores", header=1)
df_2020 = df_2020.loc[:, ~df_2020.columns.str.contains("^Unnamed", na=False)]
all_country_names[2020] = [clean_country(c) for c in df_2020.iloc[:, 0].tolist()]

# 2021
df_2021 = read_sheet(2021, "Detailed scores", header=1)
df_2021 = df_2021.loc[:, ~df_2021.columns.str.contains("^Unnamed", na=False)]
all_country_names[2021] = [clean_country(c) for c in df_2021.iloc[:, 0].tolist()]

# 2022
df_2022 = read_sheet(2022, "Detailed scores", header=1)
df_2022 = df_2022.loc[:, ~df_2022.columns.str.contains("^Unnamed", na=False)]
all_country_names[2022] = [clean_country(c) for c in df_2022.iloc[:, 0].tolist()]

# 2023
df_2023 = read_sheet(2023, "Pillar & dimension scores", header=1)
df_2023 = df_2023.loc[:, ~df_2023.columns.str.contains("^Unnamed", na=False)]
all_country_names[2023] = [clean_country(c) for c in df_2023.iloc[:, 0].tolist()]

# 2024
df_2024 = read_sheet(2024, "Scores per pillar and dimension", header=1)
df_2024 = df_2024.loc[:, ~df_2024.columns.str.contains("^Unnamed", na=False)]
all_country_names[2024] = [clean_country(c) for c in df_2024.iloc[:, 0].tolist()]

# 2025 — ATENCION: columna A es Ranking, columna B es Country
df_2025 = read_sheet(2025, "Dimensions-Pillars", header=1)
df_2025 = df_2025.loc[:, ~df_2025.columns.str.contains("^Unnamed", na=False)]
all_country_names[2025] = [clean_country(c) for c in df_2025.iloc[:, 1].tolist()]

# --- 2. Build unique set (filtrando numeros sueltos) ---
unique_names = set()
for year, names in all_country_names.items():
    for n in names:
        if n.isdigit():
            continue  # filtrar numeros de ranking que puedan colarse
        unique_names.add(n)

unique_sorted = sorted(unique_names)
print(f"Total paises unicos en todos los anos: {len(unique_sorted)}")

# --- 3. Create ISO3 mapping ---
# Manual mapping based on ISO 3166-1 alpha-3
iso3_map = {
    "Afghanistan": "AFG",
    "Albania": "ALB",
    "Algeria": "DZA",
    "Andorra": "AND",
    "Angola": "AGO",
    "Antigua and Barbuda": "ATG",
    "Argentina": "ARG",
    "Armenia": "ARM",
    "Australia": "AUS",
    "Austria": "AUT",
    "Azerbaijan": "AZE",
    "Bahamas": "BHS",
    "Bahrain": "BHR",
    "Bangladesh": "BGD",
    "Barbados": "BRB",
    "Belarus": "BLR",
    "Belgium": "BEL",
    "Belize": "BLZ",
    "Benin": "BEN",
    "Bhutan": "BTN",
    "Bolivia (Plurinational State of)": "BOL",
    "Bosnia and Herzegovina": "BIH",
    "Botswana": "BWA",
    "Brazil": "BRA",
    "Brunei Darussalam": "BRN",
    "Bulgaria": "BGR",
    "Burkina Faso": "BFA",
    "Burundi": "BDI",
    "Cabo Verde": "CPV",
    "Cambodia": "KHM",
    "Cameroon": "CMR",
    "Canada": "CAN",
    "Central African Republic": "CAF",
    "Chad": "TCD",
    "Chile": "CHL",
    "China": "CHN",
    "Colombia": "COL",
    "Comoros": "COM",
    "Congo": "COG",
    "Costa Rica": "CRI",
    "Côte d'Ivoire": "CIV",
    "Croatia": "HRV",
    "Cuba": "CUB",
    "Cyprus": "CYP",
    "Czechia": "CZE",
    "Czech Republic": "CZE",
    "Democratic People's Republic of Korea": "PRK",
    "Democratic Republic of the Congo": "COD",
    "Denmark": "DNK",
    "Djibouti": "DJI",
    "Dominica": "DMA",
    "Dominican Republic": "DOM",
    "Ecuador": "ECU",
    "Egypt": "EGY",
    "El Salvador": "SLV",
    "Equatorial Guinea": "GNQ",
    "Eritrea": "ERI",
    "Estonia": "EST",
    "Eswatini": "SWZ",
    "Swaziland": "SWZ",
    "Ethiopia": "ETH",
    "Fiji": "FJI",
    "Finland": "FIN",
    "France": "FRA",
    "Gabon": "GAB",
    "Gambia": "GMB",
    "Gambia (Republic of The)": "GMB",
    "Georgia": "GEO",
    "Germany": "DEU",
    "Ghana": "GHA",
    "Greece": "GRC",
    "Grenada": "GRD",
    "Guatemala": "GTM",
    "Guinea": "GIN",
    "Guinea-Bissau": "GNB",
    "Guinea Bissau": "GNB",
    "Guyana": "GUY",
    "Haiti": "HTI",
    "Honduras": "HND",
    "Hungary": "HUN",
    "Iceland": "ISL",
    "India": "IND",
    "Indonesia": "IDN",
    "Iran": "IRN",
    "Iran (Islamic Republic of)": "IRN",
    "Iraq": "IRQ",
    "Ireland": "IRL",
    "Israel": "ISR",
    "Italy": "ITA",
    "Jamaica": "JAM",
    "Japan": "JPN",
    "Jordan": "JOR",
    "Kazakhstan": "KAZ",
    "Kenya": "KEN",
    "Kiribati": "KIR",
    "Kuwait": "KWT",
    "Kyrgyzstan": "KGZ",
    "Lao People's Democratic Republic": "LAO",
    "Latvia": "LVA",
    "Lebanon": "LBN",
    "Lesotho": "LSO",
    "Liberia": "LBR",
    "Libya": "LBY",
    "Liechtenstein": "LIE",
    "Lithuania": "LTU",
    "Luxembourg": "LUX",
    "Madagascar": "MDG",
    "Malawi": "MWI",
    "Malaysia": "MYS",
    "Maldives": "MDV",
    "Mali": "MLI",
    "Malta": "MLT",
    "Marshall Islands": "MHL",
    "Mauritania": "MRT",
    "Mauritius": "MUS",
    "Mexico": "MEX",
    "Micronesia (Federated States of)": "FSM",
    "Micronesia": "FSM",
    "Monaco": "MCO",
    "Mongolia": "MNG",
    "Montenegro": "MNE",
    "Morocco": "MAR",
    "Mozambique": "MOZ",
    "Myanmar": "MMR",
    "Namibia": "NAM",
    "Nauru": "NRU",
    "Nepal": "NPL",
    "Netherlands": "NLD",
    "New Zealand": "NZL",
    "Nicaragua": "NIC",
    "Niger": "NER",
    "Nigeria": "NGA",
    "North Macedonia": "MKD",
    "Norway": "NOR",
    "Oman": "OMN",
    "Pakistan": "PAK",
    "Palau": "PLW",
    "Panama": "PAN",
    "Papua New Guinea": "PNG",
    "Paraguay": "PRY",
    "Peru": "PER",
    "Philippines": "PHL",
    "Poland": "POL",
    "Portugal": "PRT",
    "Qatar": "QAT",
    "Republic of Korea": "KOR",
    "Republic of Moldova": "MDA",
    "Romania": "ROU",
    "Russian Federation": "RUS",
    "Rwanda": "RWA",
    "Saint Kitts and Nevis": "KNA",
    "Saint Lucia": "LCA",
    "Saint Vincent and the Grenadines": "VCT",
    "Samoa": "WSM",
    "San Marino": "SMR",
    "Sao Tome and Principe": "STP",
    "Saudi Arabia": "SAU",
    "Senegal": "SEN",
    "Serbia": "SRB",
    "Seychelles": "SYC",
    "Sierra Leone": "SLE",
    "Singapore": "SGP",
    "Slovakia": "SVK",
    "Slovenia": "SVN",
    "Solomon Islands": "SLB",
    "Somalia": "SOM",
    "South Africa": "ZAF",
    "South Sudan": "SSD",
    "Spain": "ESP",
    "Sri Lanka": "LKA",
    "State of Palestine": "PSE",
    "Sudan": "SDN",
    "Suriname": "SUR",
    "Sweden": "SWE",
    "Switzerland": "CHE",
    "Syrian Arab Republic": "SYR",
    "Taiwan": "TWN",
    "Tajikistan": "TJK",
    "Tanzania": "TZA",
    "Thailand": "THA",
    "The former Yugoslav Republic of Macedonia": "MKD",
    "Timor-Leste": "TLS",
    "Togo": "TGO",
    "Tonga": "TON",
    "Trinidad and Tobago": "TTO",
    "Tunisia": "TUN",
    "Turkey": "TUR",
    "Turkmenistan": "TKM",
    "Tuvalu": "TUV",
    "Türkiye": "TUR",
    "Uganda": "UGA",
    "Ukraine": "UKR",
    "United Arab Emirates": "ARE",
    "United Kingdom": "GBR",
    "United Kingdom of Great Britain and Northern Ireland": "GBR",
    "United Republic of Tanzania": "TZA",
    "United States of America": "USA",
    "Uruguay": "URY",
    "Uzbekistan": "UZB",
    "Vanuatu": "VUT",
    "Venezuela": "VEN",
    "Venezuela (Bolivarian Republic of)": "VEN",
    "Viet Nam": "VNM",
    "Yemen": "YEM",
    "Zambia": "ZMB",
    "Zimbabwe": "ZWE",
}

# --- 4. Handle "(the)" variants from 2019 ---
# 2019 uses "Netherlands (the)", "Philippines (the)", etc.
# We create entries for these variants
the_variants = {}
for name in unique_sorted:
    if name.endswith(" (the)"):
        base = name[:-6]
        if base in iso3_map:
            the_variants[name] = iso3_map[base]
        else:
            print(f"  WARNING: No mapping for '(the)' variant: {name}")

iso3_map.update(the_variants)

# Handle variant country names (different spelling across years)
name_variants = {
    "Bolivia": "BOL",
    "Côte D'Ivoire": "CIV",
    "Venezuela, Bolivarian Republic of": "VEN",
}
iso3_map.update(name_variants)

# Also handle "the" prefix in some 2019 names
more_variants = {
    "Bahamas (the)": "BHS",
    "Gambia (the)": "GMB",
    "Netherlands (the)": "NLD",
    "Niger (the)": "NER",
    "Philippines (the)": "PHL",
    "Republic of Korea (the)": "KOR",
    "Republic of Moldova (the)": "MDA",
    "Sudan (the)": "SDN",
    "United Kingdom of Great Britain and Northern Ireland (the)": "GBR",
    "United States of America (the)": "USA",
    "Congo (the)": "COG",
    "Democratic Republic of the Congo (the)": "COD",
    "Central African Republic (the)": "CAF",
    "Comoros (the)": "COM",
    "Dominican Republic (the)": "DOM",
    "Democratic People's Republic of Korea (the)": "PRK",
    "Syrian Arab Republic (the)": "SYR",
    "Lao People's Democratic Republic (the)": "LAO",
    "Russian Federation (the)": "RUS",
}
iso3_map.update(more_variants)

# --- 5. Check all unique names have mapping ---
unmapped = []
for name in unique_sorted:
    if name not in iso3_map:
        unmapped.append(name)

if unmapped:
    print(f"ATENCION: {len(unmapped)} paises sin mapping ISO3:")
    for n in unmapped:
        print(f"  - '{n}'")
else:
    print("  Todos los paises tienen mapping ISO3.")

# --- 6. Build output dataframe ---
rows = []
for name in unique_sorted:
    code = iso3_map.get(name, "")
    rows.append({
        "pais_original": name,
        "iso3": code,
        "entity_type": "pais",
    })

df_map = pd.DataFrame(rows)

# Add year columns: which years each name appears in
for year in [2019, 2020, 2021, 2022, 2023, 2024, 2025]:
    col = f"aparece_{year}"
    names_this_year = all_country_names[year]
    df_map[col] = df_map["pais_original"].isin(names_this_year)

# Count appearances
df_map["total_apariciones"] = df_map[[f"aparece_{y}" for y in [2019,2020,2021,2022,2023,2024,2025]]].sum(axis=1)

# Sort
df_map = df_map.sort_values("pais_original").reset_index(drop=True)

# --- 7. Save ---
out_path = output_path("iso3_mapping.csv")
df_map.to_csv(out_path, index=False)
print(f"\nMapping guardado: {out_path}")
print(f"Total entradas: {len(df_map)}")
print(f"Con ISO3: {df_map['iso3'].notna().sum()}")
print(f"Sin ISO3: {df_map['iso3'].isna().sum()}")

# Verify counts match expectations
for year in [2019, 2020, 2021, 2022, 2023, 2024, 2025]:
    actual = len(all_country_names[year])
    expected = EXPECTED_COUNTS[year]
    status = "OK" if actual == expected else "ERROR"
    print(f"  {year}: {actual} paises (esperado {expected}) [{status}]")
