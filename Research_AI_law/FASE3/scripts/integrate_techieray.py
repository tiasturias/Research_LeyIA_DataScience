import pandas as pd
from pathlib import Path

BASE_DIR = Path("/home/pablo/Research_LeyIA_DataScience/Research_AI_law")
FASE3_OUT = BASE_DIR / "FASE3/outputs"

# Update both the CSV and the Excel to persist the change across regenerations.
wide_csv_path = FASE3_OUT / "matriz_madre_wide.csv"
matriz_df = pd.read_csv(wide_csv_path)
techieray = pd.read_csv(BASE_DIR / "FUENTES/TECHIERAY/tr_regulatory_metadata.csv")

cols_to_drop = [c for c in techieray.columns if c != 'iso3' and c in matriz_df.columns]
if cols_to_drop:
    matriz_df = matriz_df.drop(columns=cols_to_drop)

matriz_df = matriz_df.merge(techieray, left_on="iso3", right_on="iso3", how="left")
matriz_df.to_csv(wide_csv_path, index=False)
print("CSV wide updated.")
