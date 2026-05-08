"""
build_consolidado.py — Paso 1.9
Concatena todos los anos en un solo CSV con el schema completo de 126 columnas.
Output: UNIFICADO/output/consolidado_final.csv
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

# 1. Load all partial files
years_data = {}
for year in [2019, 2020, 2021, 2022, 2024, 2025]:
    years_data[year] = pd.read_csv(output_path(f"consolidado_{year}.csv"))

# 2023: load pillars and indicators separately
df_2023_p = pd.read_csv(output_path("consolidado_2023_pillars.csv"))
df_2023_i = pd.read_csv(output_path("consolidado_2023_indicators.csv"))
# Merge on pais_original
df_2023 = df_2023_p.merge(df_2023_i, on="pais_original", how="left",
                           suffixes=("", "_ind"))
# Drop duplicate columns from indicators
ind_cols = [c for c in df_2023_i.columns if c != "pais_original"]
# Remove any _ind suffixed duplicates
for c in list(df_2023.columns):
    if c.endswith("_ind"):
        del df_2023[c]
years_data[2023] = df_2023

# 2. Load ISO3 mapping
df_iso = pd.read_csv(output_path("iso3_mapping.csv"))

# 3. Load schema to get full column list
df_schema = pd.read_csv(output_path("schema_consolidado.csv"))
schema_vars = df_schema["variable"].tolist()

# 4. Add iso3 and entity_type to each year's data
for year, df_yr in years_data.items():
    # Merge using pais_original
    df_yr = df_yr.merge(df_iso[["pais_original", "iso3", "entity_type"]],
                         on="pais_original", how="left")
    years_data[year] = df_yr

# 5. Stack all years
all_dfs = []
for year in sorted(years_data.keys()):
    df_yr = years_data[year]
    all_dfs.append(df_yr)

df_all = pd.concat(all_dfs, ignore_index=True)

# 6. Reindex to full schema (adds missing columns as NaN)
for var in schema_vars:
    if var not in df_all.columns:
        df_all[var] = np.nan

# Ensure schema columns in order + iso3/entity_type at front
base_cols = ["iso3", "entity_type", "pais_original", "year"]
data_cols = [c for c in schema_vars if c not in base_cols]
final_cols = base_cols + data_cols

# Add any other columns not in schema (shouldn't happen)
for c in df_all.columns:
    if c not in final_cols and c not in base_cols:
        print(f"  WARNING: columna extra no en schema: {c}")

df_all = df_all[final_cols]

# 7. Validate
total_expected = sum(EXPECTED_COUNTS.values())
ok = validate_row_count(df_all, total_expected, "Consolidado FINAL")
print(f"  Columnas total: {len(df_all.columns)}")

# Check schema coverage
present = [c for c in schema_vars if c in df_all.columns]
missing = [c for c in schema_vars if c not in df_all.columns]
print(f"  Variables del schema presentes: {len(present)}/{len(schema_vars)}")
if missing:
    print(f"  Ausentes: {missing}")

# Check total_score by year
for year in sorted(years_data.keys()):
    subset = df_all[df_all["year"] == year]
    ts = subset["total_score"].dropna()
    print(f"  {year}: {len(subset)} filas, total_score {ts.min():.4f}-{ts.max():.4f} ({len(ts)} valores)")

# Check iso3 coverage
print(f"  iso3 missing: {df_all['iso3'].isna().sum()}")

# 8. Save
out_path = output_path("consolidado_final.csv")
df_all.to_csv(out_path, index=False)
print(f"\nGuardado: {out_path}")
print(f"Dimension: {df_all.shape[0]} filas x {df_all.shape[1]} columnas")
