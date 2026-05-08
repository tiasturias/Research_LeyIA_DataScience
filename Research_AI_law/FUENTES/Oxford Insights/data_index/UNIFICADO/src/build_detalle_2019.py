"""
build_detalle_2019.py — Paso 2.0
Construye hoja Detalle_2019: 1 fila por pais con todas las variables de 2019.
Incluye iso3, entity_type, pais_original + 27 variables de 2019.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd

df_consol = pd.read_csv(output_path("consolidado_2019.csv"))
df_iso = pd.read_csv(output_path("iso3_mapping.csv"))

# Add iso3
df_out = df_consol.merge(df_iso[["pais_original", "iso3", "entity_type"]],
                          on="pais_original", how="left")

# Select and order columns: iso3, entity_type, pais_original, year, scale, framework,
# total_score, and all 2019 specific vars
cols_2019 = ["privacy_laws", "ai_strategy", "data_availability",
             "govt_procurement_advanced_tech", "data_capability_govt",
             "technology_skills", "ai_startups", "log_ai_startups",
             "innovation_capability", "digital_public_services",
             "govt_effectiveness", "ict_govt_vision",
             "norm_privacy_laws", "norm_ai_strategy", "norm_data_availability",
             "norm_govt_procurement", "norm_data_capability",
             "norm_technology_skills", "norm_log_ai_startups",
             "norm_innovation_capability", "norm_digital_public_services",
             "norm_govt_effectiveness", "norm_ict_govt_vision",
             "total_score", "avg_governance", "avg_infrastructure_data",
             "avg_skills_education", "avg_govt_public_services"]

ordered = ["iso3", "entity_type", "pais_original", "year", "scale", "framework"] + cols_2019
df_out = df_out[ordered]

validate_row_count(df_out, 194, "Detalle_2019")
out_path = output_path("detalle_2019.csv")
df_out.to_csv(out_path, index=False)
print(f"Guardado: {out_path} (28 columnas)")
