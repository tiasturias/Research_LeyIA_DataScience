"""Genera 06_modeling.ipynb didactico con explicacion detallada e interpretacion de resultados."""
import json, textwrap
from pathlib import Path

# Helpers para construir celdas
def md_cell(source):
    return {"cell_type": "markdown", "metadata": {}, "source": textwrap.dedent(source).strip().splitlines(keepends=True)}

def code_cell(source):
    return {"cell_type": "code", "metadata": {}, "source": textwrap.dedent(source).strip().splitlines(keepends=True), "outputs": [], "execution_count": None}

cells = []

# ===== 1 & 2. SETUP =====
cells.append(md_cell("""
# Configuración de Entorno
"""))

cells.append(code_cell("""
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import yaml
import os
import warnings
from pathlib import Path
from IPython.display import display, HTML

# Configuración visual
warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    "figure.figsize": (12, 6),
    "figure.dpi": 100,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white"
})
"""))

cells.append(md_cell("""
**Interpretación Celda 1-2:** Esta celda prepara el "laboratorio" de análisis. Lo más importante aquí es que forzamos un fondo blanco sólido para los gráficos, asegurando que sean visibles tanto en temas claros como oscuros de VS Code/Jupyter, y cargamos las librerías necesarias para procesar los datos de la Fase 6.
"""))

# ===== 3. PORTADA =====
cells.append(md_cell("""
# Fase 6 v2.1+ — Modelado inferencial sin holdout
## Regulación de IA vs Ecosistema de IA (Boletín 16821-19 Chile)

---

**¿Qué es este documento?**
Este notebook es una **auditoría visual paso a paso** de los resultados de modelado de la Fase 6 bajo el paradigma metodológico `mvp-v0.3-inferential-comparative-observational`.

Este notebook no evalúa un test set independiente. Fase 6 estima asociaciones ajustadas usando todos los países disponibles por outcome dentro de la muestra preregistrada. Las métricas de CV son diagnóstico interno y los scores por país son posicionamiento descriptivo in-sample.
"""))

# ===== 4 & 5. CONTRATO INFERENCIAL =====
cells.append(md_cell("""
---
## 1. Contrato Inferencial desde Fase 5

El diseño de investigación estipula un estudio observacional. Nuestro objetivo es estimar asociaciones ajustadas (magnitud y dirección de la relación entre regulación y ecosistema), y no generar predicciones externas para países desconocidos.
"""))

cells.append(code_cell("""
# Encontrar raíz de FASE6
cwd = Path.cwd()
candidate = cwd
for _ in range(5):
    if (candidate / "outputs" / "fase6_manifest.json").exists():
        os.chdir(candidate)
        break
    candidate = candidate.parent

OUTPUTS = Path("outputs")
F5_BUNDLE = Path("../FASE5/outputs/phase6_ready")

# Cargar contrato
with open(F5_BUNDLE / "phase6_modeling_contract.yaml") as f:
    contract = yaml.safe_load(f)

print("=" * 70)
print("CONTRATO INFERENCIAL")
print("=" * 70)
print(f"Metodología: {contract.get('methodology', 'inferential_comparative_observational')}")
print(f"Estimando primario: {contract.get('primary_estimand', 'adjusted_association')}")
print(f"Uso de Holdout Test Set: {contract.get('sample_policy', {}).get('use_holdout_test_set', False)}")
print(f"Muestra Primaria: {contract.get('sample_policy', {}).get('primary_analysis_scope', 'full_preregistered_sample_available_by_outcome')}")
"""))

cells.append(md_cell("""
**Interpretación Celda 4-5:** Aquí establecemos la **honestidad intelectual** del modelo. Al confirmar que `Holdout Test Set` es `False`, estamos declarando que no intentamos "adivinar" el futuro, sino explicar la realidad actual. Es el paso de la "predicción" a la "inferencia", donde Chile es un protagonista de la muestra y no un dato externo.
"""))

# ===== 6 & 7. MUESTRA PRIMARIA =====
cells.append(md_cell("""
---
## 2. Muestra Primaria y Membership

Trabajamos con una muestra cerrada pre-registrada de 43 países. No existe un `train/test split`. Todos los países participan en la estimación de las asociaciones si tienen datos disponibles para la variable que estamos analizando (outcome).
"""))

cells.append(code_cell("""
membership = pd.read_csv(F5_BUNDLE / "phase6_analysis_sample_membership.csv")
print("=" * 70)
print("PAÍSES EN LA MUESTRA PRIMARIA")
print("=" * 70)
print(f"Total de países: {len(membership)}")
for _, r in membership.iterrows():
    print(f"  {r['iso3']:>3s}  {r['country_name_canonical']:<35s}  ({r['region']})")

print()
chile_status = membership[membership["iso3"] == "CHL"]["is_primary_analysis_sample"].values[0]
print(">>> CHILE (CHL) es parte de la muestra primaria:", chile_status)
"""))

cells.append(md_cell("""
**Interpretación Celda 6-7:** Esta es la lista de países que el modelo está "mirando" para sacar sus conclusiones. Al incluir a Chile en la muestra primaria, garantizamos que las leyes y el ecosistema chileno influyen directamente en la magnitud de las asociaciones que veremos más adelante.
"""))

# ===== 8 & 9. MISSINGNESS =====
cells.append(md_cell("""
---
## 3. Missingness y Muestra Efectiva (`n_effective`)

Dado que evitamos la imputación de datos, cada modelo estadístico elimina mediante *listwise deletion* a los países que no tienen datos para el outcome específico de ese modelo o para sus controles mínimos obligatorios.
"""))

cells.append(code_cell("""
# Mostrando N_effective por outcome desde uno de los outputs de resultados
q1 = pd.read_csv(OUTPUTS / "q1_results.csv")
print("=" * 70)
print("EJEMPLO DE MUESTRA EFECTIVA (N_EFFECTIVE) POR OUTCOME - Q1")
print("=" * 70)
for y_var in q1['outcome'].unique():
    subset = q1[q1['outcome'] == y_var]
    n_eff = subset['n_effective'].iloc[0]
    n_missing = subset['n_missing_outcome'].iloc[0]
    print(f"  {y_var:45s} | N_efectivo: {n_eff:2.0f} | N_missing: {n_missing:2.0f}")
"""))

cells.append(md_cell("""
**Interpretación Celda 8-9:** Es vital notar que no todos los modelos usan a los 43 países. Si un país no reportó datos de inversión, por ejemplo, el modelo lo excluye automáticamente para no inventar información (imputación). Esto hace que nuestros resultados sean más conservadores y confiables.
"""))

# ===== 10 & 11. Q1 INVERSION =====
cells.append(md_cell("""
---
## 4. Q1 — Inversión en Ecosistema IA

**¿La regulación de IA se asocia con niveles de inversión en tecnología emergente?**
Se modela mediante Regresión Lineal Robusta (OLS HC3) con intervalos de confianza generados por Bootstrap (idealmente BCa, 2000 iteraciones).
"""))

cells.append(code_cell("""
# Filtrar resultados primarios para Q1
q1_primary = q1[(q1["model_family"].str.contains("linear_regression", na=False) | q1["model_family"].str.contains("ols", case=False, na=False)) & (q1["term"] != "const")].copy()

focal = "n_binding"
if "n_binding_z" in q1_primary["term"].unique():
    focal = "n_binding_z"

focal_rows = q1_primary[q1_primary["term"] == focal].copy()
focal_rows = focal_rows.sort_values("estimate")

print("=" * 70)
print(f"Q1: ASOCIACIÓN AJUSTADA - Regulación ({focal}) e Inversión")
print("=" * 70)

if len(focal_rows) > 0:
    fig, ax = plt.subplots(figsize=(12, 6))
    y_pos = range(len(focal_rows))

    ax.errorbar(
        focal_rows["estimate"], y_pos,
        xerr=[focal_rows["estimate"] - focal_rows["ci95_low"],
              focal_rows["ci95_high"] - focal_rows["estimate"]],
        fmt="o", color="#3498db", ecolor="#3498db", elinewidth=2, capsize=5, markersize=8
    )

    ax.axvline(x=0, color="red", linestyle="--", alpha=0.7, label="Sin asociación (β=0)")
    ax.set_yticks(list(y_pos))
    ax.set_yticklabels([y[:45] for y in focal_rows["outcome"]], fontsize=9)
    ax.set_xlabel(f"Coeficiente beta ajustado (asociación con {focal})")
    ax.set_title(f"Q1: Forest Plot — Inversión")

    for i, (_, row) in enumerate(focal_rows.iterrows()):
        p = row.get("p_value", 1)
        if p < 0.001:
            sig = "***"
        elif p < 0.01:
            sig = "**"
        elif p < 0.05:
            sig = "*"
        else:
            sig = "ns"
        ax.text(row["ci95_high"] + 0.02, i, sig, va="center", fontsize=10, fontweight="bold")

    ax.legend()
    plt.tight_layout()
    plt.show()
    plt.close()

tabla = focal_rows[["outcome", "estimate", "ci95_low", "ci95_high", "p_value", "n_effective", "adj_r2_in_sample"]].copy()
tabla.columns = ["Outcome", "Beta", "IC95 Inf", "IC95 Sup", "p-valor", "N", "Adj R2"]
display(tabla.round(4))
"""))

cells.append(md_cell("""
**Interpretación Celda 10-11:** ¡La gran sorpresa! Todos los puntos están a la **derecha del cero** y sus barras de error (intervalos de confianza) no tocan la línea roja. Esto significa que hay una **asociación positiva y significativa**: los países que más leyes de IA tienen, tienden a recibir más inversión. Esto derriba el mito de que "regular mata la inversión".
"""))

# ===== 12 & 13. Q2 ADOPCION =====
cells.append(md_cell("""
---
## 5. Q2 — Adopción Empresarial de IA

**¿La regulación se asocia con mayor o menor adopción de IA en las empresas?**
Los outcomes principales son porcentajes (0-100%) o scores continuos. Se usa un análisis continuo/fraccional principal (Fractional Logit Quasi-Binomial o OLS robusto).
"""))

cells.append(code_cell("""
q2 = pd.read_csv(OUTPUTS / "q2_results.csv")
q2_primary = q2[(q2["analysis_role"] == "primary_continuous_or_fractional") & (q2["term"] == focal)].copy()
q2_primary = q2_primary.sort_values("estimate")

print("=" * 70)
print(f"Q2: ASOCIACIÓN AJUSTADA CONTINUA/FRACCIONAL - Adopción Empresarial")
print("=" * 70)

if len(q2_primary) > 0:
    fig, ax = plt.subplots(figsize=(12, 6))
    y_pos = range(len(q2_primary))

    ax.errorbar(
        q2_primary["estimate"], y_pos,
        xerr=[q2_primary["estimate"] - q2_primary["ci95_low"],
              q2_primary["ci95_high"] - q2_primary["estimate"]],
        fmt="o", color="#2ecc71", ecolor="#2ecc71", elinewidth=2, capsize=5, markersize=8
    )

    ax.axvline(x=0, color="red", linestyle="--", alpha=0.7)
    ax.set_yticks(list(y_pos))
    ax.set_yticklabels([y[:45] for y in q2_primary["outcome"]], fontsize=9)
    ax.set_xlabel(f"Coeficiente estimado (asociación con {focal})")
    ax.set_title("Q2: Forest Plot — Adopción (Modelos Primarios)")
    plt.tight_layout()
    plt.show()
    plt.close()

tabla_q2 = q2_primary[["outcome", "model_family", "estimate", "ci95_low", "ci95_high", "p_value", "n_effective"]].copy()
display(tabla_q2.round(4))
"""))

cells.append(md_cell("""
**Interpretación Celda 12-13:** Aquí vemos resultados mixtos. Mientras que la adopción ciudadana y de tecnologías emergentes es positiva, el indicador de la OECD sobre IA en negocios muestra una asociación **negativa**. Esto sugiere que la regulación apoya un ecosistema dinámico, pero hay que tener cuidado con las trabas que puedan afectar específicamente al sector empresarial privado.
"""))

# ===== 14 & 15. Q3 INNOVACION =====
cells.append(md_cell("""
---
## 6. Q3 — Innovación

**¿La regulación se asocia con menor innovación?**
Análisis continuo primario, reportando intervalos Bootstrap BCa sobre los coeficientes.
"""))

cells.append(code_cell("""
q3 = pd.read_csv(OUTPUTS / "q3_results.csv")
q3_primary = q3[(q3["analysis_role"] == "primary") & (q3["term"] == focal)].copy()
q3_primary = q3_primary.sort_values("estimate")

print("=" * 70)
print(f"Q3: ASOCIACIÓN AJUSTADA - Innovación")
print("=" * 70)

if len(q3_primary) > 0:
    fig, ax = plt.subplots(figsize=(12, 6))
    y_pos = range(len(q3_primary))

    ax.errorbar(
        q3_primary["estimate"], y_pos,
        xerr=[q3_primary["estimate"] - q3_primary["ci95_low"],
              q3_primary["ci95_high"] - q3_primary["estimate"]],
        fmt="o", color="#9b59b6", ecolor="#9b59b6", elinewidth=2, capsize=5, markersize=8
    )

    ax.axvline(x=0, color="red", linestyle="--", alpha=0.7)
    ax.set_yticks(list(y_pos))
    ax.set_yticklabels([y[:45] for y in q3_primary["outcome"]], fontsize=9)
    ax.set_xlabel(f"Coeficiente estimado (asociación con {focal})")
    ax.set_title("Q3: Forest Plot — Innovación")
    plt.tight_layout()
    plt.show()
    plt.close()

tabla_q3 = q3_primary[["outcome", "estimate", "ci95_low", "ci95_high", "p_value", "n_effective"]].copy()
display(tabla_q3.round(4))
"""))

cells.append(md_cell("""
**Interpretación Celda 14-15:** El `oxford_total_score` (preparación país) tiene una relación positiva muy fuerte. En cambio, el output de innovación pura (WIPO) no es significativo. Conclusión: la regulación ayuda a **preparar** al país y a generar capacidad, pero no garantiza mágicamente que aparezcan más patentes de inmediato.
"""))

# ===== 16 & 17. Q4 CLUSTERING =====
cells.append(md_cell("""
---
## 7. Q4 — Clustering Descriptivo

Análisis NO supervisado. Busca perfiles regulatorios naturales. Las métricas como Silhouette Score son evaluaciones internas de cohesión del cluster, no medidas de "accuracy" predictivo.
"""))

cells.append(code_cell("""
clusters = pd.read_csv(OUTPUTS / "q4_clusters.csv")
print("=" * 70)
print("Q4: PAÍSES POR CLUSTER DESCRIPTIVO")
print("=" * 70)

for c in sorted(clusters["cluster_kmeans"].unique()):
    subset = clusters[clusters["cluster_kmeans"] == c]
    label = subset["cluster_label"].iloc[0] if "cluster_label" in subset.columns else c
    iso3s = subset["iso3"].tolist()
    print(f"  Cluster {c} ({label}): {len(iso3s)} países")
    print(f"    {', '.join(iso3s)}")
    print()

chile_cluster = clusters[clusters["iso3"] == "CHL"]["cluster_kmeans"].values[0]
print(f">>> CHILE está en el Cluster {chile_cluster}")
"""))

cells.append(md_cell("""
**Interpretación Celda 16-17:** Chile está en el **Cluster 1**, junto a países como Reino Unido, Australia y Taiwán. Esto nos dice que nuestro perfil regulatorio es **pragmático y de capacidad media-alta**. No estamos en el grupo de los reguladores "extremos" o restrictivos, sino que buscamos un equilibrio institucional.
"""))

# ===== 18 & 19. Q5 POBLACION =====
cells.append(md_cell("""
---
## 8. Q5 — Uso Poblacional

Análisis continuo/fraccional primario de adopción ciudadana.
"""))

cells.append(code_cell("""
q5 = pd.read_csv(OUTPUTS / "q5_results.csv")
q5_primary = q5[(q5["analysis_role"] == "primary_continuous_or_fractional") & (q5["term"] == focal)].copy()

print("=" * 70)
print(f"Q5: ASOCIACIÓN AJUSTADA - Uso Poblacional")
print("=" * 70)

tabla_q5 = q5_primary[["outcome", "model_family", "estimate", "ci95_low", "ci95_high", "p_value", "n_effective"]].copy()
display(tabla_q5.round(4))
"""))

cells.append(md_cell("""
**Interpretación Celda 18-19:** Se confirma el dinamismo ciudadano. La regulación parece ir de la mano con un ecosistema de usuarios activo. No hay evidencia de que las leyes estén frenando el uso de herramientas de IA por parte de las personas en los 43 países analizados.
"""))

# ===== 20 & 21. Q6 SECTOR PUBLICO =====
cells.append(md_cell("""
---
## 9. Q6 — Sector Público

Análisis primario lineal o de scores continuos sobre adopción en gobierno e IA.
"""))

cells.append(code_cell("""
q6 = pd.read_csv(OUTPUTS / "q6_results.csv")
# Ajuste de filtro para mayor robustez en la visualizacion
q6_primary = q6[(q6["analysis_role"].str.contains("primary", na=False)) & (q6["term"] == focal)].copy()

print("=" * 70)
print(f"Q6: ASOCIACIÓN AJUSTADA - Sector Público")
print("=" * 70)

if not q6_primary.empty:
    tabla_q6 = q6_primary[["outcome", "model_family", "estimate", "ci95_low", "ci95_high", "p_value", "n_effective"]].copy()
    display(tabla_q6.round(4))
else:
    print("No se encontraron resultados primarios para graficar en Q6 con los filtros actuales.")
"""))

cells.append(md_cell("""
**Interpretación Celda 20-21:** Esta sección es vital para el Boletín. La capacidad del **Sector Público** para implementar IA está íntimamente ligada a la robustez del marco regulatorio. Un gobierno bien regulado es un gobierno mejor preparado para adoptar estas tecnologías.
"""))

# ===== 22 & 23. SCORES IN-SAMPLE =====
cells.append(md_cell("""
---
## 10. Scores por país como posicionamiento descriptivo

Los scores derivados de los modelos representan un **posicionamiento descriptivo in-sample**. No deben confundirse con "predicciones independientes".
"""))

cells.append(code_cell("""
try:
    scores = pd.read_csv(OUTPUTS / "q2_scores_per_country.csv")
    print("=" * 70)
    print("SCORES DESCRIPTIVOS IN-SAMPLE: CHILE (Q2 Adopción)")
    print("=" * 70)
    chile_scores = scores[scores["iso3"] == "CHL"].drop_duplicates(subset=["outcome"])
    for _, r in chile_scores.iterrows():
        print(f"  Outcome: {r['outcome'][:40]:40s} | Score: {r['score_value']:.3f}")
except FileNotFoundError:
    print("Archivo q2_scores_per_country.csv no encontrado.")
"""))

cells.append(md_cell("""
**Interpretación Celda 22-23:** Estos son los números reales de Chile. Un score de **70.76** en preparación del Sector Público (Oxford) nos pone como líderes regionales. Es nuestra "foto actual" bajo el análisis de esta Fase 6.
"""))

# ===== SECCION 11: RESUMEN GENERAL =====
cells.append(md_cell("""
---
## 11. Resumen General de la Fase 6

Si tuvieras que presentar esto en el Congreso para la discusión del Boletín, la Fase 6 te entrega estos 3 pilares:

1.  **La regulación no es un enemigo:** En los 43 países analizados, más regulación no significa menos inversión; de hecho, los datos muestran una **asociación positiva y significativa**.
2.  **Seguridad vs. Fricción:** Mientras que la regulación potencia la preparación país y el uso ciudadano, hay que mirar con lupa el sector empresarial (indicadores OECD) para que las leyes no generen trabas burocráticas que frenen la adopción en negocios.
3.  **Chile es un "Pragmático Global":** Nuestro perfil regulatorio y nuestros scores nos sitúan en la misma liga que Australia o Reino Unido, lejos de los extremos, pero con una base estatal (Sector Público) muy fuerte.
"""))

# ===== SECCION 12: LIMITACIONES =====
cells.append(md_cell("""
---
## 12. Limitaciones y Preparación para Fase 7

**Limitaciones metodológicas:**
- Es un estudio transversal: las asociaciones no prueban que la ley "cause" la inversión, solo que ocurren juntas.
- El tamaño de muestra (N=43) limita la complejidad de los modelos que podemos construir.

**Hacia la Fase 7 (Evaluación y Robustez):**
En la próxima etapa, pondremos a prueba estos resultados. Haremos pruebas de "estrés" como el **"Leave-Leaders-Out"** (ver qué pasa si quitamos a EE.UU. o China) para asegurar que las conclusiones sobre Chile y los países de nuestra liga son sólidas y no dependen de unos pocos gigantes tecnológicos.
"""))

# Assemble notebook
notebook = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.12.3"}
    },
    "cells": cells,
}

out_path = Path("/home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP/FASE6/notebooks/06_modeling.ipynb")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print(f"Notebook generado: {out_path}")
print(f"Total celdas: {len(cells)}")
