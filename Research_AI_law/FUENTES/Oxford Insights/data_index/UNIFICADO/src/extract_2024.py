"""
extract_2024_to_consolidado.py — Paso 1.7
Extrae Scores per pillar and dimension de 2024.
Incluye columna Ranking (82 missing).
Output: UNIFICADO/output/consolidado_2024.csv
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

YEAR = 2024
df = read_sheet(YEAR, "Scores per pillar and dimension", header=1)
df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

COL_MAP = {
    "total_score": "Total",
    "ranking_detail": "Ranking",
    "government": "Government",
    "technology_sector": "Technology Sector",
    "data_infrastructure": "Data and Infrastructure",
    "vision": "Vision",
    "governance_ethics": "Governance and Ethics",
    "digital_capacity": "Digital Capacity",
    "adaptability": "Adaptability",
    "maturity": "Maturity",
    "innovation_capacity": "Innovation Capacity",
    "human_capital": "Human Capital",
    "infrastructure": "Infrastructure",
    "data_availability": "Data Availability",
    "data_representativeness": "Data Representativeness",
}

rows = []
for _, row in df.iterrows():
    entry = {"pais_original": clean_country(row.iloc[0]), "year": YEAR,
             "scale": "0-100", "framework": "3_pillars_10_dims"}
    for var, src in COL_MAP.items():
        v = row[src]
        entry[var] = float(v) if pd.notna(v) else np.nan
    rows.append(entry)

df_out = pd.DataFrame(rows)
validate_row_count(df_out, EXPECTED_COUNTS[YEAR], f"{YEAR}")
ts = df_out["total_score"].dropna()
print(f"  total_score: {ts.min():.4f} a {ts.max():.4f}")
print(f"  ranking_detail NaN: {df_out['ranking_detail'].isna().sum()} (esperado 82)")
print(f"  data_representativeness NaN: {df_out['data_representativeness'].isna().sum()}")
out_path = output_path(f"consolidado_{YEAR}.csv")
df_out.to_csv(out_path, index=False)
print(f"Guardado: {out_path}")
