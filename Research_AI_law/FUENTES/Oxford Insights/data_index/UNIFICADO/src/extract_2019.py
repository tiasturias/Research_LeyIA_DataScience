"""
extract_2019_to_consolidado.py — Paso 1.1
Extrae datos 2019 (Data sheet) al formato Consolidado.
Output: UNIFICADO/output/consolidado_2019.csv
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

YEAR = 2019

df = read_sheet(YEAR, "Data", header=None)

# Column mapping for 2019 Data sheet:
# Col 0: Country, Col 1-12: raw indicators, Col 14-24: normalised (col 13 is gap)
# Col 26: INDEX SCORE, Col 28: Sum of cluster averages, Col 29-32: cluster averages
COL_MAP = {
    "privacy_laws": 1, "ai_strategy": 2, "data_availability": 3,
    "govt_procurement_advanced_tech": 4, "data_capability_govt": 5,
    "technology_skills": 6, "ai_startups": 7, "log_ai_startups": 8,
    "innovation_capability": 9, "digital_public_services": 10,
    "govt_effectiveness": 11, "ict_govt_vision": 12,
    "norm_privacy_laws": 14, "norm_ai_strategy": 15,
    "norm_data_availability": 16, "norm_govt_procurement": 17,
    "norm_data_capability": 18, "norm_technology_skills": 19,
    "norm_log_ai_startups": 20, "norm_innovation_capability": 21,
    "norm_digital_public_services": 22, "norm_govt_effectiveness": 23,
    "norm_ict_govt_vision": 24,
    "index_score": 26,
    "avg_governance": 29, "avg_infrastructure_data": 30,
    "avg_skills_education": 31, "avg_govt_public_services": 32,
}

# Read country data (rows 7 to end, col 0)
rows_data = []
for i in range(7, len(df)):
    country_val = df.iloc[i, 0]
    if pd.isna(country_val):
        continue
    row = {"pais_original": clean_country(country_val)}
    for var_name, col_idx in COL_MAP.items():
        val = df.iloc[i, col_idx]
        try:
            row[var_name] = float(val) if pd.notna(val) else np.nan
        except (ValueError, TypeError):
            row[var_name] = np.nan
    rows_data.append(row)

df_out = pd.DataFrame(rows_data)

# Rename index_score to total_score
df_out = df_out.rename(columns={"index_score": "total_score"})

# Add metadata columns
df_out["year"] = YEAR
df_out["scale"] = "0-10"
df_out["framework"] = "4_clusters"

# Validate
ok = validate_row_count(df_out, EXPECTED_COUNTS[YEAR], f"2019 Consolidado")

# Check total_score range (should be 0-10)
if ok:
    ts = df_out["total_score"].dropna()
    print(f"  total_score range: {ts.min():.4f} a {ts.max():.4f}")
    print(f"  total_score NaN: {df_out['total_score'].isna().sum()}")
    print(f"  Columnas: {list(df_out.columns)}")

# Save
out_path = output_path("consolidado_2019.csv")
df_out.to_csv(out_path, index=False)
print(f"Guardado: {out_path}")
