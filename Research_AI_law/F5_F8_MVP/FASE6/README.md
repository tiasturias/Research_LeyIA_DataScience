# Fase 6 — Modelado MVP (v0.4)

**Proyecto:** Research_AI_law — Boletín 16821-19 Ley Marco IA Chile
**Fase CRISP-DM:** Paso 4 — Modeling
**Directorio:** `F5_F8_MVP/FASE6/`
**Pre-requisito:** Fase 5 v2.0 (bundle `phase6_ready/` con 12 archivos, 46 vars)

## Hipótesis principal

> ¿Existe una asociación estadísticamente significativa entre las características de la regulación de IA de un país y el desarrollo de su ecosistema de IA, después de controlar por factores socioeconómicos e institucionales?

## Sub-preguntas

| Sub-pregunta | Tipo | Output principal |
|---|---|---|
| Q1 Inversión | Regresión | Coeficientes + IC bootstrap |
| Q2 Adopción empresarial | Clasificación | AUC + predicciones por país |
| Q3 Innovación | Regresión | Coeficientes + IC |
| Q4 Contenido regulatorio | Clustering | Etiquetas país × cluster |
| Q5 Uso IA población | Regresión + Clasificación | β + AUC |
| Q6 Uso IA sector público | Regresión + Clasificación | β + AUC |

## Outputs (20 archivos)

- Q1: `q1_results.csv`, `q1_consistency.csv`, `q1_psm_matched_pairs.csv`, `q1_psm_balance_diagnostics.csv`
- Q2: `q2_results.csv`, `q2_predictions_per_country.csv`
- Q3: `q3_results.csv`, `q3_consistency.csv`
- Q4: `q4_clusters.csv`, `q4_distance_matrix_n43.csv`, `q4_distance_matrix_n18.csv`, `q4_silhouette_scores.csv`, `q4_centroids.csv`
- Q5: `q5_results.csv`, `q5_consistency.csv`, `q5_predictions_per_country.csv`
- Q6: `q6_results.csv`, `q6_consistency.csv`, `q6_predictions_per_country.csv`
- Manifest: `fase6_manifest.json`

## Decisiones técnicas (F6-A a F6-M)

Ver `config/fase6_decisions.yaml`.

## Cómo correr

```bash
# Pipeline completo
make fase6-all

# Tests
make fase6-test

# Notebook
make fase6-notebook

# Validar que no hay PCA
make fase6-validate-no-pca
```

## Decisiones clave

- **PCA fuera de scope** (Decisión L) — análisis exploratorio delegado a Fase 4
- **Lenguaje conservador** (Decisión I) — "asociación" no "efecto"
- **Hyperparams fijos** (Decisión F) — GridSearch solo en Fase 7 como verificación
- **Bootstrap 2000** como IC principal (Decisión B, D)
- **FDR Benjamini-Hochberg** para corrección múltiple (Decisión E)

## Limitaciones documentadas

- N=18 países con datos IAPP completos
- N=26 para Stanford publications (tier auxiliary)
- PSM exploratorio con caliper 0.20 (3-6 pares)
- Sin sensitivity analysis (Fase 7)
- Sin inferencia causal robusta (post-MVP)
