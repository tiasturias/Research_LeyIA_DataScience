"""
extract_2025_to_consolidado.py — Paso 1.8
Extrae Dimensions-Pillars de 2025 (6 pilares, 14 dimensiones).
Output: UNIFICADO/output/consolidado_2025.csv
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

YEAR = 2025
df = read_sheet(YEAR, "Dimensions-Pillars", header=1)
df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

# Columns after unnamed removal: Ranking, Country, Total Score, Policy Capacity,
# AI Infrastructure, Governance, Public Sector Adoption, Development & Diffusion,
# Resilience, Policy vision, Policy commitment, Compute capacity, ...
COL_MAP = {
    "rank": "Ranking",
    "total_score": "Total Score",
    "policy_capacity": "Policy Capacity",
    "ai_infrastructure": "AI Infrastructure",
    "governance_2025": "Governance",
    "public_sector_adoption": "Public Sector Adoption",
    "development_diffusion": "Development & Diffusion",
    "resilience": "Resilience",
    "policy_vision": "Policy vision",
    "policy_commitment": "Policy commitment",
    "compute_capacity": "Compute capacity",
    "enabling_technical_infrastructure": "Enabling technical infrastructure",
    "data_quality": "Data quality",
    "governance_principles": "Governance principles",
    "regulatory_compliance": "Regulatory compliance",
    "government_digital_policy": "Government digital policy",
    "e_government_delivery": "e-Government delivery",
    "human_capital_2025": "Human capital",
    "ai_sector_maturity": "AI sector maturity",
    "ai_technology_diffusion": "AI technology diffusion",
    "societal_transition": "Societal transition",
    "safety_security": "Safety and security",
}

rows = []
for _, row in df.iterrows():
    # Country is at index 1 (columna B), ranking is at index 0
    country_val = row.iloc[1] if len(row) > 1 else row.iloc[0]
    entry = {"pais_original": clean_country(country_val), "year": YEAR,
             "scale": "0-100", "framework": "6_pillars_14_dims"}
    for var, src in COL_MAP.items():
        try:
            v = row[src]
            entry[var] = float(v) if pd.notna(v) else np.nan
        except (KeyError):
            entry[var] = np.nan
    rows.append(entry)

df_out = pd.DataFrame(rows)
validate_row_count(df_out, EXPECTED_COUNTS[YEAR], f"{YEAR}")
ts = df_out["total_score"].dropna()
print(f"  total_score: {ts.min():.4f} a {ts.max():.4f}")
print(f"  rank NaN: {df_out['rank'].isna().sum()}")

out_path = output_path(f"consolidado_{YEAR}.csv")
df_out.to_csv(out_path, index=False)
print(f"Guardado: {out_path}")
