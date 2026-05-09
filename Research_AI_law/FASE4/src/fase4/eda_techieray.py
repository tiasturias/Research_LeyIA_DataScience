import pandas as pd
from pathlib import Path
import json

BASE_DIR = Path("/home/pablo/Research_LeyIA_DataScience/Research_AI_law")
MATRIZ_PATH = BASE_DIR / "FASE3/outputs/matriz_madre_wide.csv"
OUT_DIR = BASE_DIR / "FASE4/outputs/eda_techieray"
OUT_DIR.mkdir(parents=True, exist_ok=True)

print("Cargando Matriz Madre...")
df = pd.read_csv(MATRIZ_PATH)

# Filtrar solo países que tengan ambas fuentes no nulas para poder comparar (IAPP original tenía N=18)
df_compare = df.dropna(subset=['iapp_ley_ia_vigente', 'tr_ley_ia_vigente'])
n_overlap = len(df_compare)
print(f"Países con solapamiento (IAPP y Techieray): {n_overlap}")

if n_overlap > 0:
    # Comparar 'Ley Vigente'
    df_compare['match_ley'] = df_compare['iapp_ley_ia_vigente'] == df_compare['tr_ley_ia_vigente']
    match_rate_ley = df_compare['match_ley'].mean() * 100
    
    # Comparar 'Proyecto de Ley'
    # Nota: IAPP y Techieray a veces codifican diferente si no hay datos, limpiemos a int si es posible
    df_compare['match_proy'] = df_compare['iapp_proyecto_ley_ia'] == df_compare['tr_proyecto_ley_ia']
    match_rate_proy = df_compare['match_proy'].mean() * 100

    report = f"""# Reporte de Validación Cruzada: IAPP vs Techieray

## Resumen de Muestra
- **Total países analizados (solapamiento):** {n_overlap}
- Estos son los países que originalmente tenían datos de IAPP, contra los cuales cruzamos la rigurosa extracción de Techieray.

## Tasa de Concordancia (Concordance Rate)
- **Variable `Ley Vigente`:** {match_rate_ley:.1f}% de concordancia.
- **Variable `Proyecto de Ley`:** {match_rate_proy:.1f}% de concordancia.

## Análisis de Discrepancias en Ley Vigente
"""
    discrepancias_ley = df_compare[~df_compare['match_ley']][['iso3', 'country_name_canonical', 'iapp_ley_ia_vigente', 'tr_ley_ia_vigente']]
    if discrepancias_ley.empty:
        report += "No se encontraron discrepancias en esta variable. Ambas metodologías están perfectamente alineadas.\n"
    else:
        report += discrepancias_ley.to_string(index=False) + "\n"

    report += "\n## Análisis de Discrepancias en Proyecto de Ley\n"
    discrepancias_proy = df_compare[~df_compare['match_proy']][['iso3', 'country_name_canonical', 'iapp_proyecto_ley_ia', 'tr_proyecto_ley_ia']]
    if discrepancias_proy.empty:
        report += "No se encontraron discrepancias en esta variable.\n"
    else:
        report += discrepancias_proy.to_string(index=False) + "\n"

    report_path = OUT_DIR / "cross_validation_report.md"
    report_path.write_text(report, encoding='utf-8')
    print(f"\nReporte guardado en {report_path}")
    print("\n--- RESUMEN EN CONSOLA ---")
    print(report)
else:
    print("No se encontraron países superpuestos para comparar.")
