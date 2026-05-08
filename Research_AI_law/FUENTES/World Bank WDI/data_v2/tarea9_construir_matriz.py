"""Tarea 9: Construir MATRIZ_COMPLETA unificada.
- Carga todos los CSV individuales de los 6 bloques
- Carga metadata de paises
- Genera MATRIZ larga (long) y MATRIZ ancha (wide)
- Guarda como CSV
"""
import pandas as pd
import os
import glob
from datetime import datetime

RAW_DIR = "/Users/francoia/Documents/Research_AI_law/World Bank WDI/data_v2/raw"
OUTPUT_DIR = "/Users/francoia/Documents/Research_AI_law/World Bank WDI/data_v2"
COUNTRIES_FILE = os.path.join(RAW_DIR, "tarea2_paises_metadata.csv")

def main():
    print("=" * 80)
    print("TAREA 9: Construir MATRIZ_COMPLETA")
    print(f"Hora: {datetime.now().isoformat()}")
    print("=" * 80)
    
    # 1. Cargar metadata paises
    print("\n1. Cargando metadata paises...")
    paises = pd.read_csv(COUNTRIES_FILE)
    print(f"   Paises: {len(paises)}")
    print(f"   Regiones: {paises['wb_region'].nunique()}")
    print(f"   Income groups: {paises['wb_income_group'].nunique()}")
    
    # 2. Cargar todos los CSV de indicadores
    print("\n2. Cargando CSVs de indicadores...")
    csv_files = glob.glob(os.path.join(RAW_DIR, "tarea3_*.csv")) + \
                glob.glob(os.path.join(RAW_DIR, "tarea47_*.csv")) + \
                glob.glob(os.path.join(RAW_DIR, "tarea8_*.csv"))
    
    dfs = []
    for f in sorted(csv_files):
        fname = os.path.basename(f)
        try:
            df = pd.read_csv(f)
            # Keep only needed columns
            df = df[["iso3", "year", "value", "wb_indicator", "canonical_name"]]
            # Ensure types
            df["year"] = df["year"].astype(int)
            df["value"] = pd.to_numeric(df["value"], errors="coerce")
            n = len(df)
            indicator = df["canonical_name"].iloc[0]
            years = sorted(df["year"].unique())
            print(f"   {fname:50s} | {n:5d} rows | {indicator:40s} | years: {min(years)}-{max(years)}")
            dfs.append(df)
        except Exception as e:
            print(f"   {fname:50s} | ERROR: {e}")
    
    df_long = pd.concat(dfs, ignore_index=True)
    print(f"\n   Total rows (long): {len(df_long)}")
    print(f"   Unique indicators: {df_long['canonical_name'].nunique()}")
    print(f"   Unique countries: {df_long['iso3'].nunique()}")
    print(f"   Year range: {df_long['year'].min()}-{df_long['year'].max()}")
    
    # 3. Pivot long -> wide: iso3 + year -> column = canonical_name + year
    print("\n3. Pivoteando long -> wide...")
    # Create column name: {canonical_name}_{year}
    df_long["var_year"] = df_long["canonical_name"] + "_" + df_long["year"].astype(str)
    
    df_wide = df_long.pivot_table(
        index="iso3",
        columns="var_year",
        values="value",
        aggfunc="first"  # solo debe haber 1 valor por iso3-var_year
    )
    
    # 4. Merge metadata
    print("\n4. Merge con metadata paises...")
    df_wide = paises[["iso3", "country_name", "wb_region", "wb_income_group"]].merge(
        df_wide, on="iso3", how="left"
    )
    
    # Reorder: metadata columns first
    meta_cols = ["iso3", "country_name", "wb_region", "wb_income_group"]
    var_cols = sorted([c for c in df_wide.columns if c not in meta_cols])
    df_wide = df_wide[meta_cols + var_cols]
    
    print(f"   Filas (paises):      {len(df_wide)}")
    print(f"   Columnas totales:    {len(df_wide.columns)}")
    print(f"   Columnas metadata:   {len(meta_cols)}")
    print(f"   Columnas variables:  {len(var_cols)}")
    
    # 5. Guardar MATRIZ_COMPLETA
    output_path = os.path.join(OUTPUT_DIR, "MATRIZ_COMPLETA.csv")
    df_wide.to_csv(output_path, index=False)
    print(f"\n5. Guardado: {output_path}")
    
    # 6. Guardar version LONG (para referencia)
    long_path = os.path.join(OUTPUT_DIR, "MATRIZ_COMPLETA_LONG.csv")
    df_long.to_csv(long_path, index=False)
    print(f"   Guardado: {long_path}")
    
    # Resumen
    completeness = df_wide[var_cols].notna().sum().sum()
    total_cells = len(df_wide) * len(var_cols)
    print(f"\n{'='*80}")
    print(f"MATRIZ_COMPLETA - RESUMEN")
    print(f"  Paises:            {len(df_wide)}")
    print(f"  Variables x año:   {len(var_cols)}")
    print(f"  Celdas totales:    {total_cells}")
    print(f"  Celdas con datos:  {completeness} ({100*completeness/total_cells:.1f}%)")
    print(f"  Celdas vacias:     {total_cells - completeness} ({100*(total_cells-completeness)/total_cells:.1f}%)")
    
    # Top/bottom countries by completeness
    comp_by_country = df_wide.set_index("iso3")[var_cols].notna().sum(axis=1)
    print(f"\n  Top 5 paises mas completos:")
    for iso3, count in comp_by_country.nlargest(5).items():
        name = paises[paises["iso3"] == iso3]["country_name"].values[0] if len(paises[paises["iso3"] == iso3]) > 0 else iso3
        print(f"    {iso3} ({name}): {count}/{len(var_cols)}")
    
    print(f"\n  Bottom 5 paises menos completos:")
    for iso3, count in comp_by_country.nsmallest(5).items():
        name = paises[paises["iso3"] == iso3]["country_name"].values[0] if len(paises[paises["iso3"] == iso3]) > 0 else iso3
        print(f"    {iso3} ({name}): {count}/{len(var_cols)}")

if __name__ == "__main__":
    main()
