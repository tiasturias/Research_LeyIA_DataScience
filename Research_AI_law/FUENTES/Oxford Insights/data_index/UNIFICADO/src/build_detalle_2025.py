"""
build_detalle_2025.py — Paso 4.0
Hoja Detalle_2025: 1 fila por pais con 6 pilares y 14 dimensiones.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd

df = pd.read_csv(output_path("consolidado_2025.csv"))
df_iso = pd.read_csv(output_path("iso3_mapping.csv"))
df = df.merge(df_iso[["pais_original", "iso3", "entity_type"]],
              on="pais_original", how="left")

ordered = ["iso3", "entity_type", "pais_original", "year", "scale", "framework",
           "rank", "total_score",
           "policy_capacity", "ai_infrastructure", "governance_2025",
           "public_sector_adoption", "development_diffusion", "resilience",
           "policy_vision", "policy_commitment", "compute_capacity",
           "enabling_technical_infrastructure", "data_quality",
           "governance_principles", "regulatory_compliance",
           "government_digital_policy", "e_government_delivery",
           "human_capital_2025", "ai_sector_maturity",
           "ai_technology_diffusion", "societal_transition", "safety_security"]

df_out = df[ordered]
validate_row_count(df_out, 195, "Detalle_2025")
print(f"  Columnas: {len(ordered)}")

out_path = output_path("detalle_2025.csv")
df_out.to_csv(out_path, index=False)
print(f"Guardado: {out_path}")
