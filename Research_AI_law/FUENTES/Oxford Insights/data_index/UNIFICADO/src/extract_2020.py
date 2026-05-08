"""
extract_2020_to_consolidado.py — Paso 1.2
Extrae datos 2020 (Detailed scores) al formato Consolidado.
Output: UNIFICADO/output/consolidado_2020.csv
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

YEAR = 2020

df = read_sheet(YEAR, "Detailed scores", header=1)
df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

# Column mapping 2020: Country, Overall score, Government, Technology Sector,
# Data and Infrastructure, Vision, Governance and Ethics, Digital Capacity,
# Adaptability, Size, Innovation Capacity, Human Capital, Infrastructure,
# Data Availability, Data Representativeness
COL_MAP = {
    "total_score": "Overall score",
    "government": "Government",
    "technology_sector": "Technology Sector",
    "data_infrastructure": "Data and Infrastructure",
    "vision": "Vision",
    "governance_ethics": "Governance and Ethics",
    "digital_capacity": "Digital Capacity",
    "adaptability": "Adaptability",
    "size": "Size",
    "innovation_capacity": "Innovation Capacity",
    "human_capital": "Human Capital",
    "infrastructure": "Infrastructure",
    "data_availability": "Data Availability",
    "data_representativeness": "Data Representativeness",
}

rows_data = []
for _, row in df.iterrows():
    entry = {
        "pais_original": clean_country(row.iloc[0]),
        "year": YEAR,
        "scale": "0-100",
        "framework": "3_pillars_10_dims",
    }
    for var_name, source_col in COL_MAP.items():
        val = row[source_col]
        try:
            entry[var_name] = float(val) if pd.notna(val) else np.nan
        except (ValueError, TypeError):
            entry[var_name] = np.nan
    rows_data.append(entry)

df_out = pd.DataFrame(rows_data)

ok = validate_row_count(df_out, EXPECTED_COUNTS[YEAR], f"{YEAR} Consolidado")
if ok:
    ts = df_out["total_score"].dropna()
    print(f"  total_score range: {ts.min():.4f} a {ts.max():.4f}")
    print(f"  total_score NaN: {df_out['total_score'].isna().sum()}")
    print(f"  data_representativeness NaN: {df_out['data_representativeness'].isna().sum()}")
    print(f"  Columnas: {list(df_out.columns)}")

out_path = output_path(f"consolidado_{YEAR}.csv")
df_out.to_csv(out_path, index=False)
print(f"Guardado: {out_path}")
