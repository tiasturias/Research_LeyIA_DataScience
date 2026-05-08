"""
build_detalle_2020_2024.py — Paso 3.0
Stack 2020-2024 con 3 pilares y 10 dimensiones.
Unifica Size (2020-2021) y Maturity (2022-2024) en columna 'dimensión_tamaño_madurez'.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import *
import pandas as pd
import numpy as np

frames = []
for year in [2020, 2021, 2022, 2024]:
    df = pd.read_csv(output_path(f"consolidado_{year}.csv"))
    frames.append(df)
# 2023 is stored as consolidado_2023_pillars.csv
df_2023 = pd.read_csv(output_path("consolidado_2023_pillars.csv"))
frames.append(df_2023)

df_stack = pd.concat(frames, ignore_index=True)

df_iso = pd.read_csv(output_path("iso3_mapping.csv"))
df_stack = df_stack.merge(df_iso[["pais_original", "iso3", "entity_type"]],
                          on="pais_original", how="left")

# Unify size/maturity: create single column
df_stack["dim_size_maturity"] = np.where(
    df_stack["size"].notna() & df_stack["maturity"].isna(),
    df_stack["size"],
    np.where(
        df_stack["maturity"].notna(),
        df_stack["maturity"],
        np.nan
    )
)

ordered = ["iso3", "entity_type", "pais_original", "year", "scale", "framework",
           "total_score", "government", "technology_sector", "data_infrastructure",
           "vision", "governance_ethics", "digital_capacity", "adaptability",
           "dim_size_maturity", "size", "maturity",
           "innovation_capacity", "human_capital", "infrastructure",
           "data_availability", "data_representativeness"]

# Add ranking_detail for 2024
if "ranking_detail" in df_stack.columns:
    ordered.append("ranking_detail")

df_out = df_stack[ordered]

total_expected = sum(EXPECTED_COUNTS[y] for y in [2020,2021,2022,2023,2024])
validate_row_count(df_out, total_expected, "Detalle_2020_2024")
print(f"  Columnas: {len(ordered)}")

out_path = output_path("detalle_2020_2024.csv")
df_out.to_csv(out_path, index=False)
print(f"Guardado: {out_path}")
