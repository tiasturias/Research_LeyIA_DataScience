"""
extract_2022_to_consolidado.py — Paso 1.4
Idem 2020 pero Size renombrado a Maturity.
Output: UNIFICADO/output/consolidado_2022.csv
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

YEAR = 2022
df = read_sheet(YEAR, "Detailed scores", header=1)
df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

COL_MAP = {
    "total_score": "Overall score",
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
print(f"  maturity NaN: {df_out['maturity'].isna().sum()}")
out_path = output_path(f"consolidado_{YEAR}.csv")
df_out.to_csv(out_path, index=False)
print(f"Guardado: {out_path}")
