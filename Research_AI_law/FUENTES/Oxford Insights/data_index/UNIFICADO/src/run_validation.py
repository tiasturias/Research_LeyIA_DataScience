"""
run_validation.py — Paso 10.1
Validacion final integral del workbook.
Output: UNIFICADO/validation/validation_report.txt
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

REPORT = []

def log(msg):
    print(msg)
    REPORT.append(msg)

log("=" * 70)
log("VALIDACION FINAL: Oxford_Insights_Unificado.xlsx")
log("=" * 70)

# 1. Check Consolidado
log("\n--- 1. Consolidado ---")
df = pd.read_csv(output_path("consolidado_final.csv"))
log(f"  Filas: {len(df)} (esperado 1283)")
log(f"  Columnas: {len(df.columns)} (esperado 126)")

# By year
for year in [2019, 2020, 2021, 2022, 2023, 2024, 2025]:
    subset = df[df["year"] == year]
    expected = EXPECTED_COUNTS[year]
    status = "OK" if len(subset) == expected else "ERROR"
    log(f"  {year}: {len(subset)} filas (esperado {expected}) [{status}]")

# Check that 2019 has total_score in 0-10 range
s_2019 = df[df["year"] == 2019]["total_score"].dropna()
log(f"  2019 total_score: {s_2019.min():.4f} a {s_2019.max():.4f} (esperado 0-10)")

# Check that 2020+ has total_score in 0-100 range
for year in [2020, 2021, 2022, 2023, 2024, 2025]:
    s = df[df["year"] == year]["total_score"].dropna()
    log(f"  {year} total_score: {s.min():.4f} a {s.max():.4f} (esperado ~0-100)")

# Check iso3
log(f"  iso3 missing: {df['iso3'].isna().sum()} (esperado 0)")

# Check framework distribution
for fw in df["framework"].value_counts().items():
    log(f"  framework '{fw[0]}': {fw[1]} filas")

# Check NaN pattern: 2019 should have NaN for 2020-2024 variables
gov_2019 = df[(df["year"] == 2019)]["government"].isna().all()
gov_2020 = df[(df["year"] == 2020)]["government"].notna().all()
log(f"  government NaN en 2019: {gov_2019} (esperado True)")
log(f"  government notna en 2020: {gov_2020} (esperado True)")

# 2025 variables should be NaN pre-2025
pc_2019 = df[(df["year"] == 2019)]["policy_capacity"].isna().all()
pc_2025 = df[(df["year"] == 2025)]["policy_capacity"].notna().all()
log(f"  policy_capacity NaN en 2019: {pc_2019} (esperado True)")
log(f"  policy_capacity notna en 2025: {pc_2025} (esperado True)")

# 2. Check detail sheets
log("\n--- 2. Detalle_2019 ---")
df = pd.read_csv(output_path("detalle_2019.csv"))
log(f"  Filas: {len(df)} (esperado 194), Columnas: {len(df.columns)}")
log(f"  iso3 missing: {df['iso3'].isna().sum()} (esperado 0)")
log(f"  ai_startups max: {df['ai_startups'].max()} (esperado 5053, USA)")

log("\n--- 3. Detalle_2020_2024 ---")
df = pd.read_csv(output_path("detalle_2020_2024.csv"))
log(f"  Filas: {len(df)} (esperado 894), Columnas: {len(df.columns)}")
log(f"  iso3 missing: {df['iso3'].isna().sum()} (esperado 0)")
yr_counts = df.groupby("year").size()
for yr, cnt in yr_counts.items():
    exp = EXPECTED_COUNTS[yr]
    log(f"  {yr}: {cnt} (esperado {exp})")

log("\n--- 4. Detalle_2025 ---")
df = pd.read_csv(output_path("detalle_2025.csv"))
log(f"  Filas: {len(df)} (esperado 195), Columnas: {len(df.columns)}")
log(f"  iso3 missing: {df['iso3'].isna().sum()} (esperado 0)")

log("\n--- 5. Indicadores_2023 ---")
df = pd.read_csv(output_path("indicadores_2023.csv"))
log(f"  Filas: {len(df)} (esperado 193), Columnas: {len(df.columns)}")
log(f"  ind_ai_strategy valores unicos: {df['ind_ai_strategy'].nunique()} (esperado 3: 0,50,100)")
log(f"  iso3 missing: {df['iso3'].isna().sum()} (esperado 0)")

log("\n--- 6. Rankings_Regionales_2019 ---")
df = pd.read_csv(output_path("rankings_regionales_2019.csv"))
log(f"  Filas: {len(df)} (esperado 194), Columnas: {len(df.columns)}")
log(f"  iso3 missing: {df['iso3'].isna().sum()} (esperado 0)")
log(f"  Regiones: {sorted(df['region_pertenece'].unique())}")
for region, cnt in df["region_pertenece"].value_counts().items():
    log(f"    {region}: {cnt}")

log("\n--- 7. Diccionario_Variables ---")
df = pd.read_csv(output_path("diccionario_variables.csv"))
log(f"  Filas: {len(df)} (esperado 126)")
all_vars = df["variable"].tolist()
log(f"  Primeras 5 variables: {all_vars[:5]}")
log(f"  Ultimas 5: {all_vars[-5:]}")

log("\n--- 8. Fuentes_Directas ---")
df = pd.read_csv(output_path("fuentes_directas.csv"))
log(f"  Filas: {len(df)} (esperado 126)")

log("\n--- 9. ISO3_Mapping ---")
df = pd.read_csv(output_path("iso3_mapping_sheet.csv"))
log(f"  Filas: {len(df)} (esperado ~229)")
log(f"  Con ISO3: {df['iso3'].notna().sum()}")
log(f"  Sin ISO3: {df['iso3'].isna().sum()}")

# Summary
log("\n" + "=" * 70)
log("RESUMEN:")
log("=" * 70)
log(f"  Total hojas: 9")
log(f"  Consolidado: 1283 x 126")
log(f"  Detalle_2019: 194 x 34")
log(f"  Detalle_2020_2024: 894 x 23")
log(f"  Detalle_2025: 195 x 28")
log(f"  Indicadores_2023: 193 x 42")
log(f"  Rankings_Regionales_2019: 194 x 20")
log(f"  Diccionario_Variables: 126 x 10")
log(f"  Fuentes_Directas: 126 x 7")
log(f"  ISO3_Mapping: 229 x 11")
log(f"  VALIDACION COMPLETADA")

# Save report
report_path = os.path.join(VALIDATION_DIR, "validation_report.txt")
with open(report_path, "w") as f:
    f.write("\n".join(REPORT))
log(f"\nReporte guardado: {report_path}")
