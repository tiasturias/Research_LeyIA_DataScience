# Índice Arquitectónico — FASE6/outputs

**Proyecto:** Research_AI_law — Boletín 16821-19 Ley Marco de IA Chile  
**Versión auditada:** Fase 6 v2.2 (Fase 6.1 + Fase 6.2 Country Intelligence Layer)  
**Metodología:** `inferential_comparative_observational` — estudio observacional sin holdout, sin split, sin validación externa  
**Muestra preregistrada:** 43 países (N=43 para feature matrix; N efectivo varía por outcome según listwise deletion)  
**Fecha de documentación:** 2026-05-08

---

## Arquitectura del directorio `outputs/`

```
outputs/
│
├── [FASE 6.1 — MODELADO INFERENCIAL BASE] ────────────────────────────
│   ├── fase6_manifest.json              # Manifiesto canónico v2.1+
│   ├── q1_results.csv                   # Asociaciones Inversión
│   ├── q2_results.csv                   # Asociaciones Adopción (fraccional + sensibilidad binaria)
│   ├── q2_scores_per_country.csv        # Scores descriptivos in-sample Q2
│   ├── q3_results.csv                   # Asociaciones Innovación
│   ├── q4_clusters.csv                  # Tipología regulatoria (18 países IAPP)
│   ├── q4_distance_matrix.csv           # Matriz distancia Jaccard 18×18
│   ├── q5_results.csv                   # Asociaciones Uso Poblacional (fraccional + sensibilidad)
│   ├── q5_scores_per_country.csv        # Scores descriptivos in-sample Q5
│   ├── q6_results.csv                   # Asociaciones Sector Público (fraccional + sensibilidad)
│   └── q6_scores_per_country.csv        # Scores descriptivos in-sample Q6
│
├── [FASE 6.2 — COUNTRY INTELLIGENCE LAYER] ──────────────────────────
│   └── country_intelligence/
│       ├── phase6_2_country_intelligence_manifest.json
│       ├── phase6_2_quality_checks.csv
│       ├── README.md
│       │
│       ├── [PERFILES PAÍS] ─────────────────────────────────
│       │   ├── country_q_profile_long.csv       # ARCHIVO CENTRAL — 903 filas
│       │   └── country_q_profile_wide.csv       # 1 fila por país, 42 países
│       │
│       ├── [RANKINGS] ──────────────────────────────────────
│       │   ├── country_rankings_by_outcome.csv  # 903 filas, 18 outcomes
│       │   ├── country_rankings_by_group.csv    # 3,297 filas, 16 grupos
│       │   └── country_best_worst_by_q.csv      # 1,896 filas, best/worst
│       │
│       ├── [DRIVERS + BRECHAS] ────────────────────────────
│       │   ├── country_model_contributions.csv  # 2,537 filas, drivers descriptivos
│       │   └── country_residuals_and_gaps.csv   # 854 filas, over/underperformers
│       │
│       ├── [ANÁLISIS ESTRATÉGICO] ─────────────────────────
│       │   ├── country_cluster_profile.csv      # Q4 tipología regulatoria
│       │   ├── country_headline_flags.csv       # Pioneros/rezagados consistentes
│       │   ├── country_learning_patterns.csv    # Lecciones de pioneros/rezagados
│       │   └── country_comparison_pairs.csv     # CHL vs 7 benchmarks
│       │
│       ├── [GRÁFICOS] ──────────────────────────────────────
│       │   ├── country_graphics_catalog.csv     # Catálogo de 38 figuras
│       │   └── figures/
│       │       ├── q_heatmaps/                  # 1 heatmap país×Q
│       │       ├── q_rankings/                  # 5 rankings (Q1-Q6)
│       │       ├── country_cards/               # 10 radares (CHL,SGP,...)
│       │       ├── chile_vs_benchmarks/         # 1 comparación CHL vs SGP
│       │       ├── pioneer_vs_laggard/          # 1 panel top/bottom
│       │       └── residuals/                   # 1 scatter observado vs ajustado
│       │
│       └── [COUNTRY CARDS DATA] ─────────────────────────────
│           └── country_cards_data/
│               ├── CHL_country_card_data.csv    # Ficha Chile (5 secciones)
│               ├── SGP_country_card_data.csv    # Ficha Singapur
│               ├── EST_country_card_data.csv    # Ficha Estonia
│               ├── IRL_country_card_data.csv    # Ficha Irlanda
│               ├── ARE_country_card_data.csv    # Ficha Emiratos Árabes
│               ├── KOR_country_card_data.csv    # Ficha Corea del Sur
│               ├── JPN_country_card_data.csv    # Ficha Japón
│               ├── USA_country_card_data.csv    # Ficha Estados Unidos
│               ├── CHN_country_card_data.csv    # Ficha China
│               ├── BRA_country_card_data.csv    # Ficha Brasil
│               ├── URY_country_card_data.csv    # Ficha Uruguay
│               └── README_country_cards.md
```

---

# PARTE I — FASE 6.1: MODELADO INFERENCIAL BASE

Los 11 outputs originales producidos por `src/run_all.py`. Cada modelo aplica **listwise deletion** sobre Y y X requeridas (sin imputación), reportando `n_effective`. Los intervalos de confianza se estiman por **bootstrap (2000 iteraciones, BCa preferente, fallback percentil)**. El lenguaje es **asociación ajustada**, no causalidad.

---

## 1. `fase6_manifest.json`

**Tipo:** JSON — metadata de auditoría de Fase 6.1  
**Tamaño:** 1,816 bytes

### Claves principales

| Clave | Valor | Significado |
|---|---|---|
| `fase6_version` | `2.1+` | Versión del pipeline de modelado |
| `methodology` | `inferential_comparative_observational` | Paradigma: estudio observacional sin holdout |
| `primary_estimand` | `adjusted_association` | El estimando primario es asociación ajustada, no efecto causal |
| `analysis_sample_n` | 43 | Países en la muestra preregistrada |
| `holdout_used` | `false` | No existe conjunto de test independiente |
| `train_test_split_used` | `false` | No se particionó la muestra |
| `external_validation_used` | `false` | No se validó contra datos externos |
| `split_column_present` | `false` | No existe columna `split` en ningún output |
| `q2_q5_q6_primary_model_policy` | `continuous_or_fractional_primary_binary_median_sensitivity_only` | Los outcomes de Q2/Q5/Q6 se tratan como continuos/fraccionales en el análisis principal |
| `bootstrap_policy.n_resamples_default` | 2000 | Iteraciones de bootstrap |
| `bootstrap_policy.ci_method_preferred` | `BCa` | Método preferido de intervalo de confianza |
| `language_policy.causal_claim` | `false` | No se afirma causalidad |
| `language_policy.independent_prediction_claim` | `false` | No se afirma predicción independiente |

### Mensaje del archivo
Este manifiesto es el **contrato metodológico** de Fase 6.1. Todo auditor, consumidor o fase downstream (Fase 7, Fase 8) debe leerlo primero para entender que los resultados son **asociaciones ajustadas observacionales**, no predicciones ni efectos causales.

---

## 2. `q1_results.csv`

**Tipo:** CSV — asociaciones ajustadas entre regulación de IA e inversión  
**Shape:** (12 filas, 30 columnas)  
**Grano:** 1 fila por combinación de **predictor × outcome de inversión**

### Columnas principales

| Columna | Tipo | Descripción |
|---|---|---|
| `question` | str | `Q1` |
| `outcome` | str | Variable dependiente de inversión (4 outcomes) |
| `model_family` | str | `linear_regression_parsimonious` — OLS con errores robustos HC3 |
| `analysis_role` | str | `primary` — análisis principal |
| `n_primary_sample` | int | 43 (muestra preregistrada) |
| `n_effective` | int | Países efectivos tras listwise deletion (17–42) |
| `n_missing_outcome` | int | Países sin dato en el outcome |
| `n_missing_predictors` | int | Países sin dato en predictores/controles |
| `term` | str | Predictor regulatorio: `n_binding`, `n_non_binding`, `iapp_ley_ia_vigente` |
| `estimate` | float | Coeficiente beta ajustado (OLS HC3) |
| `std_error_hc3` | float | Error estándar robusto HC3 |
| `p_value` | float | p-value del coeficiente |
| `r2_in_sample` | float | R² in-sample |
| `adj_r2_in_sample` | float | R² ajustado in-sample |
| `ci95_low` | float | Límite inferior del intervalo de confianza 95% bootstrap |
| `ci95_high` | float | Límite superior del IC95 bootstrap |
| `ci_method` | str | `percentile_fallback_or_bca_if_available` |
| `bootstrap_success_rate` | float | Tasa de éxito del bootstrap (1.0 = 100%) |
| `cv_r2_mean` | float | R² medio en validación cruzada repetida (diagnóstico interno) |
| `cv_rmse_mean` | float | RMSE medio en CV repetida |
| `holdout_used` | bool | `False` |
| `external_validation_used` | bool | `False` |
| `independent_prediction` | bool | `False` |
| `causal_claim` | bool | `False` |

### Outcomes de Q1
1. `oxford_ind_company_investment_emerging_tech` — Inversión empresarial en tecnologías emergentes
2. `oxford_ind_ai_unicorns_log` — Unicornios de IA (log)
3. `oxford_ind_vc_availability` — Disponibilidad de venture capital
4. `wipo_c_vencapdeal_score` — Score de deals de VC (WIPO)

### Mensaje del archivo
Los coeficientes para `n_binding` y `n_non_binding` son **consistentemente positivos y significativos** (p < 0.05 en 7 de 8 modelos). Los países con más legislación vinculante y no vinculante de IA tienden a tener **mayor inversión** en tecnologías emergentes, más unicornios, más VC. El predictor `iapp_ley_ia_vigente` (ley IA vigente binaria) no es significativo con n=17 efectivo (los IC95 cruzan el cero ampliamente), reflejando la baja potencia estadística de la muestra IAPP (18 países).

---

## 3. `q2_results.csv`

**Tipo:** CSV — asociaciones ajustadas entre regulación y adopción empresarial de IA  
**Shape:** (29 filas, 32 columnas)  
**Grano:** 1 fila por combinación de **predictor × outcome × analysis_role**

### Columnas principales

| Columna | Tipo | Descripción |
|---|---|---|
| `question` | str | `Q2` |
| `outcome` | str | Variable de adopción (5 outcomes) |
| `model_family` | str | `fractional_logit_quasi_binomial` (primario) o `fractional_or_linear_by_scale` (sensibilidad) |
| `analysis_role` | str | `primary_continuous_or_fractional` o `sensitivity_binary_median` |
| `n_effective` | int | Países efectivos (10–42) |
| `term` | str | `n_binding`, `n_non_binding`, `iapp_ley_ia_vigente` |
| `estimate` | float | Coeficiente del fractional logit |
| `p_value` | float | p-value |
| `fit_status` | str | `ok_fractional_logit` |
| `primary_analysis` | bool | `True` para el modelo primario continuo/fraccional, `False` para la sensibilidad binaria |
| `ci95_low`, `ci95_high` | float | IC95 bootstrap |
| `auc_repeated_kfold` | float | AUC en CV estratificada repetida (solo filas de sensibilidad binaria) |
| `auc_note` | str | `repeated_stratified_kfold_internal_not_external_test` |
| `loocv_auc` | float | `NaN` — política: no se calcula LOOCV para AUC |
| `loocv_note` | str | `not_computed_auc_undefined_for_single_observation_test_folds` |
| `causal_claim` | bool | `False` |

### Outcomes de Q2
1. `ms_h2_2025_ai_diffusion_pct` — Difusión de IA (Microsoft 2025)
2. `oecd_5_ict_business_oecd_biz_ai_pct` — IA en negocios (OECD)
3. `anthropic_usage_pct` — Uso de Claude/IA (Anthropic)
4. `oxford_public_sector_adoption` — Adopción sector público (Oxford)
5. `oxford_ind_adoption_emerging_tech` — Adopción tecnologías emergentes (Oxford)

### Mensaje del archivo
Resultados **mixtos según el outcome**: la asociación es positiva y significativa para `anthropic_usage_pct` y `oxford_ind_adoption_emerging_tech`, pero **negativa y significativa** para `oecd_5_ict_business_oecd_biz_ai_pct` (las leyes de IA se asocian con **menor** adopción empresarial OECD). La sensibilidad binaria por mediana es **siempre auxiliar** (`primary_analysis=false`) y su AUC es diagnóstico interno, no validación externa. Los modelos con `iapp_ley_ia_vigente` tienen n=10-17 efectivo y status `low_n_exploratory_only`.

---

## 4. `q2_scores_per_country.csv`

**Tipo:** CSV — scores descriptivos in-sample de adopción por país  
**Shape:** (461 filas, 10 columnas)  
**Grano:** 1 fila por **país × outcome × predictor**

### Columnas

| Columna | Descripción |
|---|---|
| `iso3` | Código ISO3 del país |
| `country_name_canonical` | Nombre canónico del país |
| `question` | `Q2` |
| `outcome` | Variable de adopción (5 outcomes) |
| `predictor` | Predictor regulatorio (`n_binding`, `n_non_binding`, `iapp_ley_ia_vigente`) |
| `score_value` | Valor observado del outcome para ese país |
| `score_scope` | `in_sample_descriptive_positioning` |
| `independent_prediction` | `False` |
| `holdout_used` | `False` |
| `analysis_scope` | `full_preregistered_sample_available_by_outcome` |

### Mensaje del archivo
Estos scores **no son predicciones**. Son los valores observados reales de cada país en los outcomes de adopción, presentados junto con el predictor usado. Permiten ver, por ejemplo, que Chile tiene un `anthropic_usage_pct` de 0.272 y un `ms_h2_2025_ai_diffusion_pct` de 20.8. El archivo es consumido por Fase 6.2 para construir percentiles y rankings.

---

## 5. `q3_results.csv`

**Tipo:** CSV — asociaciones ajustadas entre regulación e innovación  
**Shape:** (6 filas, 30 columnas)  
**Grano:** 1 fila por **predictor × outcome de innovación**

### Columnas
Estructura idéntica a Q1 (OLS HC3 con bootstrap). Mismas columnas de metadatos metodológicos.

### Outcomes de Q3
1. `oxford_total_score` — Score total de preparación país (Oxford)
2. `wipo_out_score` — Score de output de innovación (WIPO)

### Mensaje del archivo
La asociación es **positiva y significativa** para `oxford_total_score` (β=1.08–2.25, p<0.001 con n=42), pero **no significativa** para `wipo_out_score` (los IC95 cruzan el cero). La regulación se asocia con **mayor preparación institucional** para IA, pero no con mayor output de innovación pura (patentes). 6 filas solamente porque los outcomes de Stanford (`stanford_fig_6_3_5_volume_of_publications`, `stanford_fig_6_3_4_ai_patent_count`) no estaban disponibles en la feature matrix al momento de ejecución.

---

## 6. `q4_clusters.csv`

**Tipo:** CSV — tipología descriptiva de perfiles regulatorios (clustering no supervisado)  
**Shape:** (18 filas, 9 columnas)  
**Grano:** 1 fila por país con datos IAPP completos

### Columnas

| Columna | Descripción |
|---|---|
| `iso3` | Código ISO3 |
| `country_name_canonical` | Nombre del país |
| `iapp_ley_ia_vigente` | ¿Tiene ley de IA vigente? (0/1) |
| `iapp_proyecto_ley_ia` | ¿Tiene proyecto de ley de IA? (0/1) |
| `cluster_hca` | Cluster asignado por Agglomerative Hierarchical Clustering (distancia Jaccard) |
| `cluster_kmeans` | Cluster asignado por KMeans (sensibilidad) |
| `analysis_scope` | `full_preregistered_sample_unsupervised` |
| `validation_scope` | `cluster_internal_silhouette_not_external_test` |
| `holdout_used` | `False` |

### Clusters y países
| Cluster | Países | Perfil |
|---|---|---|
| 0 | NZL, SGP, ISR, CAN | Sin ley ni proyecto de ley IA |
| 1 | GBR, AUS, TWN, **CHL**, IND, ARG, BRA, COL | Con proyecto de ley, sin ley vigente (pragmáticos) |
| 2 | ARE, KOR, JPN, PER | Con ley vigente, sin proyecto |
| 3 | USA, CHN | Con ley vigente Y proyecto (potencias regulatorias duales) |

### Mensaje del archivo
Chile está en el **Cluster 1** junto a Reino Unido, Australia, India, Brasil. Este cluster agrupa países con **proyecto de ley en curso pero sin ley vigente aún** — un perfil "pragmático" de capacidad institucional media-alta que está construyendo su marco regulatorio. **Q4 es tipología descriptiva, no ranking normativo**: ningún cluster es "mejor" que otro sin relacionarlo con outcomes. Solo 18 países tienen datos IAPP completos.

---

## 7. `q4_distance_matrix.csv`

**Tipo:** CSV — matriz de distancias Jaccard entre perfiles regulatorios  
**Shape:** (18 filas, 19 columnas) — matriz simétrica con `iso3` como índice y columnas  
**Valores:** Distancia de Jaccard ∈ [0, 1] entre cada par de países

### Mensaje del archivo
Permite identificar qué países tienen perfiles regulatorios más cercanos. Por ejemplo, Chile (CHL) tiene distancia 0 con Brasil, Argentina, Reino Unido y Australia en esta matriz, y distancia 1 con Singapur (perfiles regulatorios completamente diferentes). Sirve para seleccionar **pares comparables** en Fase 7 y Fase 8.

---

## 8. `q5_results.csv`

**Tipo:** CSV — asociaciones entre regulación y uso poblacional de IA  
**Shape:** (18 filas, 33 columnas)  
**Grano:** 1 fila por **predictor × outcome × analysis_role**

### Estructura
Igual que Q2: modelo primario fraccional + sensibilidad binaria por mediana. Incluye columna `fallback_reason` cuando el fractional logit no es aplicable.

### Outcomes de Q5
1. `anthropic_usage_pct` — Uso de Claude/IA por población
2. `anthropic_collaboration_pct` — Colaboración con IA
3. `oxford_ind_adoption_emerging_tech` — Adopción tecnologías emergentes

### Mensaje del archivo
`anthropic_collaboration_pct` tiene **poca variación** (valores cercanos a cero), lo que fuerza fallback a OLS con estimaciones cercanas a cero y `fallback_reason = outcome_not_fractional_or_not_variable_enough`. Para `anthropic_usage_pct`, la asociación es **positiva y significativa** con `n_binding` (β=0.569, p=0.003) y `n_non_binding` (β=0.222, p<0.001). La sensibilidad binaria es auxiliar.

---

## 9. `q5_scores_per_country.csv`

**Tipo:** CSV — scores descriptivos in-sample de uso poblacional  
**Shape:** (297 filas, 10 columnas)  
**Estructura:** Idéntica a `q2_scores_per_country.csv` pero para Q5.

### Mensaje del archivo
Valores observados reales de uso poblacional de IA por país. Chile tiene `anthropic_usage_pct` de 0.272 y `oxford_ind_adoption_emerging_tech` de 35.15.

---

## 10. `q6_results.csv`

**Tipo:** CSV — asociaciones entre regulación y capacidad del sector público en IA  
**Shape:** (36 filas, 32 columnas)  
**Grano:** 1 fila por **predictor × outcome × analysis_role**

### Outcomes de Q6
1. `oxford_public_sector_adoption` — Adopción IA en sector público
2. `oxford_e_government_delivery` — Entrega de e-government
3. `oxford_government_digital_policy` — Política digital gubernamental
4. `oxford_ind_data_governance` — Gobernanza de datos
5. `oxford_governance_ethics` — Gobernanza ética
6. `oecd_2_indigo_oecd_indigo_score` — Score INDIGO (OECD)

### Mensaje del archivo
Resultados mixtos según la dimensión del sector público:
- **Positivo y significativo:** `oxford_government_digital_policy` (β=0.09–0.19, p<0.01 para ambos predictores)
- **Negativo y significativo:** `oxford_e_government_delivery` (β=-0.11, p=0.01 para n_non_binding) y `oecd_2_indigo_oecd_indigo_score` (β=-0.05, p=0.04 para n_binding)
- **No significativo:** `oxford_public_sector_adoption`, `oxford_ind_data_governance`, `oxford_governance_ethics`

La regulación se asocia con **mayor política digital** pero con **menor delivery de e-government** y **menor score INDIGO**. Esto sugiere que las leyes de IA pueden fortalecer el marco normativo digital pero no necesariamente la implementación operativa de servicios.

---

## 11. `q6_scores_per_country.csv`

**Tipo:** CSV — scores descriptivos in-sample de sector público  
**Shape:** (606 filas, 10 columnas)  
**Estructura:** Idéntica a `q2_scores_per_country.csv` pero para Q6 (6 outcomes).

### Mensaje del archivo
El archivo más grande de scores (606 filas = 6 outcomes × ~3 predictores × ~42 países). Chile destaca con `oxford_public_sector_adoption` de 70.76 (alto en contexto LATAM). Países como Estonia (99.63), Francia (97.18) y Emiratos (97.27) lideran en adopción pública de IA.

---

# PARTE II — FASE 6.2: COUNTRY INTELLIGENCE LAYER

La capa `country_intelligence/` agrega inteligencia país-por-país sobre los resultados de Fase 6.1. Todos los rankings, percentiles y perfiles son **posicionamiento descriptivo in-sample**. No son predicciones independientes ni estimaciones causales.

---

## 12. `country_intelligence/phase6_2_country_intelligence_manifest.json`

**Tipo:** JSON — metadata de la capa Fase 6.2  
**Tamaño:** 2,957 bytes

| Clave | Valor | Significado |
|---|---|---|
| `fase6_2_version` | `2.2` | Versión de la capa |
| `module` | `country_intelligence_layer` | Módulo que la genera |
| `methodology` | `inferential_comparative_observational` | Consistente con Fase 6.1 |
| `scope` | `descriptive_country_level_positioning` | Solo posicionamiento descriptivo |
| `holdout_used` | `false` | Sin holdout |
| `independent_prediction` | `false` | Sin predicción independiente |
| `causal_claim` | `false` | Sin afirmación causal |
| `preserved_existing_fase6_outputs` | `true` | Los 11 outputs de Fase 6.1 se preservaron |
| `n_countries_profiled` | 42 | Países perfilados (TWN ausente por missingness en wide) |
| `n_figures` | 38 | Figuras PNG+SVG generadas |
| `key_country_cards_written` | 11 | Country cards exportadas |

---

## 13. `country_intelligence/phase6_2_quality_checks.csv`

**Tipo:** CSV — bitácora de validación pre-flight  
**Shape:** (16 filas, 5 columnas)

### Columnas

| Columna | Descripción |
|---|---|
| `check` | Nombre del check (ej. `exists_q1_results.csv`) |
| `status` | `PASS` / `FAIL` |
| `severity` | `P0` (bloqueante), `INFO` |
| `path` | Ruta del archivo verificado |
| `observed` | Valor observado (ej. 43 filas en feature matrix) |

### Mensaje del archivo
16 checks, todos `PASS`. Confirma que los 11 outputs de Fase 6.1 existen, que el manifiesto base declara no holdout/no external validation, que la feature matrix tiene 43 filas y no tiene columna `split`. Si algún P0 fallara, `run_country_intelligence.py` abortaría.

---

## 14. `country_intelligence/README.md`

**Tipo:** Markdown — documentación de la capa Fase 6.2

### Contenido
- Qué contiene: rankings, perfiles, gráficos, country cards
- Qué NO contiene: predicciones, validación externa, causalidad, recomendaciones políticas finales
- Cómo interpretar: los scores son posicionamiento descriptivo in-sample
- **Frase metodológica obligatoria:** _"Los rankings, scores y perfiles país-por-país son posicionamientos descriptivos in-sample dentro de la muestra preregistrada. No son predicciones independientes ni estimaciones causales. Su robustez debe evaluarse en Fase 7 antes de convertirse en recomendación política."_

---

## 15. `country_q_profile_long.csv` ★ ARCHIVO CENTRAL DE FASE 6.2

**Shape:** (903 filas, 23 columnas)  
**Grano:** 1 fila por **país × question × outcome × predictor**  
**Cobertura:** 43 países, 5 preguntas (Q1, Q2, Q3, Q5, Q6), 18 outcomes distintos

### Schema completo

| # | Columna | Tipo | Descripción |
|---|---|---|---|
| 1 | `iso3` | str | Código ISO3 del país (43 únicos) |
| 2 | `country_name` | str | Nombre canónico del país |
| 3 | `region` | str | Región geográfica (6 regiones) |
| 4 | `income_group` | str | Grupo de ingreso (High/Upper middle/Lower middle) |
| 5 | `question_id` | str | Q1, Q2, Q3, Q5, Q6 |
| 6 | `question_label` | str | Inversión, Adopción, Innovación, Uso poblacional, Sector público |
| 7 | `dimension_type` | str | `question_outcome` |
| 8 | `outcome` | str | Variable específica (18 outcomes distintos) |
| 9 | `observed_value` | float | Valor crudo observado del outcome para ese país |
| 10 | `score_value` | float | Igual a observed_value (score = valor observado) |
| 11 | `score_source` | str | `observed_or_phase6_score` |
| 12 | `rank_global` | float | Ranking descendente (1 = mejor) entre todos los países |
| 13 | `percentile_global` | float | Percentil [0,1] del país en ese outcome |
| 14 | `rank_desc` | float | Ranking descendente (duplicado de rank_global) |
| 15 | `n_comparable_countries` | int | Países con dato en ese outcome (32–43) |
| 16 | `missing_observed_value` | bool | ¿Falta el valor observado? |
| 17 | `missing_score_value` | bool | ¿Falta el score? |
| 18 | `interpretation_label` | str | `top_pioneer` (≥0.90), `high_performer` (≥0.75), `middle_performer` (≥0.40), `low_performer` (≥0.20), `bottom_laggard` (<0.20), `not_ranked_missing` |
| 19 | `strength_weakness_label` | str | `strength` (≥0.75), `weakness` (≤0.25), `neutral`, `missing` |
| 20 | `score_scope` | str | `in_sample_descriptive_positioning` |
| 21 | `independent_prediction` | bool | `False` |
| 22 | `causal_claim` | bool | `False` |
| 23 | `notes` | str | "Descriptive country-level position; not external prediction or causality." |

### Cobertura por pregunta
| Q | Países | Outcomes |
|---|---|---|
| Q1 | 43 | oxford_ind_company_investment_emerging_tech, oxford_ind_ai_unicorns_log, oxford_ind_vc_availability, wipo_c_vencapdeal_score |
| Q2 | 43 | ms_h2_2025_ai_diffusion_pct, oecd_5_ict_business_oecd_biz_ai_pct, anthropic_usage_pct, oxford_public_sector_adoption, oxford_ind_adoption_emerging_tech |
| Q3 | 43 | oxford_total_score, wipo_out_score |
| Q5 | 43 | anthropic_usage_pct, anthropic_collaboration_pct, oxford_ind_adoption_emerging_tech |
| Q6 | 43 | oxford_public_sector_adoption, oxford_e_government_delivery, oxford_government_digital_policy, oxford_ind_data_governance, oxford_governance_ethics, oecd_2_indigo_oecd_indigo_score |

### Mensaje del archivo
Este es el archivo más importante de Fase 6.2. Permite responder **cualquier pregunta sobre el posicionamiento relativo de un país en cualquier dimensión del ecosistema de IA**. Por ejemplo: "¿En qué percentil está Chile en inversión?" → percentil 0.406. "¿Singapur es top pioneer en adopción?" → percentil 0.811, label `high_performer`. Es la fuente de verdad para todos los rankings, perfiles y gráficos derivados.

---

## 16. `country_q_profile_wide.csv`

**Shape:** (42 filas, 25 columnas)  
**Grano:** 1 fila por **país** (42 de 43 — TWN ausente por missingness en dimensiones Q)  
**Score general:** Promedio descriptivo de percentiles disponibles en Q1, Q2, Q3, Q5, Q6.

### Schema completo

| # | Columna | Descripción |
|---|---|---|
| 1 | `iso3` | Código ISO3 |
| 2 | `country_name` | Nombre del país |
| 3 | `region` | Región geográfica |
| 4 | `income_group` | Grupo de ingreso |
| 5 | `Q1_percentile` | Percentil descriptivo promedio en outcomes Q1 |
| 6 | `Q1_label` | Etiqueta interpretativa Q1 |
| 7 | `Q2_percentile` | Percentil descriptivo promedio en outcomes Q2 |
| 8 | `Q2_label` | Etiqueta Q2 |
| 9 | `Q3_percentile` | Percentil descriptivo promedio en outcomes Q3 |
| 10 | `Q3_label` | Etiqueta Q3 |
| 11 | `Q5_percentile` | Percentil descriptivo promedio en outcomes Q5 |
| 12 | `Q5_label` | Etiqueta Q5 |
| 13 | `Q6_percentile` | Percentil descriptivo promedio en outcomes Q6 |
| 14 | `Q6_label` | Etiqueta Q6 |
| 15 | `overall_country_profile_score` | **Score general descriptivo** (promedio Q1-Q6) |
| 16 | `overall_country_profile_rank` | Ranking global (1 = mejor) |
| 17 | `overall_country_profile_label` | `top_pioneer`, `high_performer`, `middle_performer`, `low_performer`, `bottom_laggard` |
| 18 | `main_strengths` | Qs donde el país tiene percentil ≥ 0.75 (separadas por `;`) |
| 19 | `main_weaknesses` | Qs donde el país tiene percentil ≤ 0.25 |
| 20 | `missingness_warnings` | Dimensiones Q faltantes |
| 21 | `recommended_use_in_phase8` | `benchmark_case`, `positive_comparator`, `context_case`, `gap_case`, `warning_case` |
| 22 | `cluster_hca` | Cluster Q4 (HCA Jaccard) — solo 18 países |
| 23 | `cluster_kmeans` | Cluster Q4 (KMeans) — solo 18 países |
| 24 | `overall_country_profile_score_is_descriptive` | `True` — este score ES descriptivo, NO causal |
| 25 | `not_a_causal_or_predictive_index` | `True` — NO es un índice causal ni predictivo |

### Top 5 países por score general
| Rank | País | Score | Label |
|---|---|---|---|
| 1 | USA | — | top_pioneer |
| 2 | GBR | — | high_performer |
| 3 | FRA | — | high_performer |
| 4 | **SGP** | 0.772 | high_performer |
| 5 | NLD | — | high_performer |

### Mensaje del archivo
Lectura ejecutiva de una página. Cada fila es un país con su "radiografía" en las 5 dimensiones del ecosistema IA. Chile tiene score 0.336 (rank 31/42), label `low_performer`, debilidad principal en Q3 (Innovación), sin fortalezas destacadas, y se recomienda como `gap_case` para Fase 8.

---

## 17. `country_rankings_by_outcome.csv`

**Shape:** (903 filas, 19 columnas)  
**Grano:** 1 fila por **outcome × país**

### Schema

| Columna | Descripción |
|---|---|
| `question_id` | Q1–Q6 |
| `question_label` | Etiqueta legible |
| `outcome` | Variable específica |
| `outcome_label` | Nombre del outcome |
| `iso3`, `country_name` | Identificación del país |
| `region`, `income_group` | Agrupaciones |
| `value_used_for_ranking` | Valor crudo usado para rankear |
| `value_type` | `observed_or_score` |
| `rank_desc` | Ranking descendente (1 = mejor) |
| `rank_asc` | Ranking ascendente (1 = peor) |
| `percentile` | Percentil [0,1] |
| `n_ranked` | Países con dato (32–43) |
| `is_top_5_global` | ¿Está en el top 5 mundial? |
| `is_bottom_5_global` | ¿Está en el bottom 5? |
| `interpretation_label` | `top_pioneer` a `bottom_laggard` |
| `why_high_or_low_short` | Explicación corta |
| `missingness_flag` | ¿Dato faltante? |

### Mensaje del archivo
Ranking crudo por cada uno de los 18 outcomes. Permite responder "¿quién es #1 en venture capital?" → USA. "¿quién es último en adopción OECD?" → URY. Es la base para todos los demás archivos de rankings.

---

## 18. `country_rankings_by_group.csv`

**Shape:** (3,297 filas, 30 columnas)  
**Grano:** 1 fila por **outcome × país × grupo**  
**Grupos:** 16 (ver abajo)

### Grupos disponibles

| Grupo | Tipo | Países |
|---|---|---|
| `global_43` | global | 43 |
| `East Asia & Pacific` | region | ~6 |
| `Europe & Central Asia` | region | ~20 |
| `Latin America & Caribbean` | region | ~8 |
| `Middle East, North Africa...` | region | ~2 |
| `North America` | region | ~2 |
| `South Asia` | region | ~1 |
| `High income` | income | ~35 |
| `Upper middle income` | income | ~5 |
| `Lower middle income` | income | ~2 |
| `ai_pioneers` | custom | SGP, ARE, IRL, EST, KOR, ISR, USA, CHN |
| `chile_latam_peers` | custom | ARG, BRA, COL, CRI, MEX, PER, URY |
| `chile_priority_benchmarks` | custom | SGP, EST, IRL, ARE, KOR, URY, BRA |
| `eu_laggards` | custom | GRC, ROU, HRV |
| `focal` | custom | CHL (solo Chile) |
| `large_ai_powers` | custom | USA, CHN, IND, JPN |

### Columnas clave adicionales (vs rankings_by_outcome)

| Columna | Descripción |
|---|---|
| `group_name` | Nombre del grupo |
| `group_type` | `global`, `region`, `income`, `custom` |
| `rank_within_group` | Ranking del país **dentro de ese grupo** |
| `percentile_within_group` | Percentil dentro del grupo |
| `n_group_ranked` | Países rankeados en ese grupo |
| `is_best_in_group` | ¿Es el #1 del grupo? |
| `is_worst_in_group` | ¿Es el último del grupo? |
| `distance_to_group_best` | Diferencia vs el mejor del grupo |
| `distance_to_group_median` | Diferencia vs la mediana del grupo |
| `distance_to_chile` | Diferencia del valor de este país vs Chile |
| `why_best_or_worst` | Explicación si es best/worst del grupo |

### Mensaje del archivo
Permite responder preguntas comparativas con contexto: "¿Quién es el mejor de LATAM en Q2?" → consultar grupo `chile_latam_peers`. "¿Chile está arriba o abajo de sus pares de ingreso?" → grupo `High income`. "¿Singapur lidera entre los pioneros?" → grupo `ai_pioneers`. Los `distance_to_chile` permiten cuantificar exactamente qué tan lejos está cada país de Chile en cada outcome.

---

## 19. `country_best_worst_by_q.csv`

**Shape:** (1,896 filas, 15 columnas)  
**Grano:** 1 fila por **pregunta × grupo × tipo_ranking × país**

### Schema

| Columna | Descripción |
|---|---|
| `question_id`, `question_label` | Q y su etiqueta |
| `group_name` | Grupo de referencia |
| `rank_type` | `best_global`, `worst_global`, `best_group`, `worst_group` |
| `iso3`, `country_name` | País |
| `rank` | Posición |
| `percentile` | Percentil |
| `value_summary` | Valor resumen |
| `main_driver_1` | Outcome principal (driver descriptivo) |
| `why_this_country_is_best_or_worst` | Explicación textual |
| `lesson_for_chile` | Lección preliminar para política pública |
| `caution_note` | "ranking descriptivo in-sample; no causalidad" |

### Mensaje del archivo
Archivo ejecutivo para identificar rápidamente **quiénes lideran y quiénes están rezagados** en cada dimensión. Incluye `lesson_for_chile` y `caution_note` en cada fila. Ejemplos:
- Q1 best_global: USA (líder en inversión)
- Q2 worst_global: URY, QAT, EST (rezagados en adopción)
- Q6 best_global: GBR, FRA, IRL (líderes en sector público)

---

## 20. `country_model_contributions.csv`

**Shape:** (2,537 filas, 17 columnas)  
**Grano:** 1 fila por **país × question × outcome × término del modelo**

### Schema

| Columna | Descripción |
|---|---|
| `iso3`, `country_name` | País |
| `question_id` | Q1–Q6 |
| `outcome` | Variable dependiente |
| `model_id` | `phase6_primary_or_available` |
| `term` | Predictor (`n_binding`, `n_non_binding`, `regulatory_intensity`) |
| `term_value` | Valor crudo del predictor para ese país |
| `term_percentile` | Percentil del país en ese predictor |
| `coefficient_or_weight` | Coeficiente β del modelo de Fase 6.1 |
| `standardized_contribution` | **Contribución estandarizada** = term_z × coefficient |
| `contribution_direction` | `positive`, `negative`, `neutral_or_missing` |
| `contribution_rank_within_country` | Ranking de contribución (por valor absoluto) dentro del país |
| `contribution_label` | `descriptive_driver_not_causal` |
| `driver_type` | `model_term` |
| `interpretation` | "Descriptive contribution based on in-sample model coefficient..." |
| `causal_claim` | `False` |
| `abs_contribution` | Valor absoluto de la contribución estandarizada |

### Mensaje del archivo
Explica **por qué un país aparece arriba o abajo** en un outcome, usando los coeficientes de los modelos de Fase 6.1 aplicados a los valores del país. Por ejemplo, Singapur tiene `n_binding=3` (percentil 0.71) y el coeficiente de `n_binding` para `oxford_ind_company_investment_emerging_tech` es β=4.73, lo que produce una contribución positiva estandarizada de +4.05. **No es causalidad**: es una descomposición descriptiva de la asociación ajustada.

---

## 21. `country_residuals_and_gaps.csv`

**Shape:** (854 filas, 17 columnas)  
**Grano:** 1 fila por **país × question × outcome × modelo simple ajustado**

### Schema

| Columna | Descripción |
|---|---|
| `iso3`, `country_name` | País |
| `question_id`, `outcome` | Q y variable |
| `model_id` | `simple_adjusted_internal` (OLS con controles mínimos) |
| `observed_value` | Valor real observado |
| `fitted_value` | Valor predicho por el modelo interno |
| `residual` | observed − fitted (positivo = rinde mejor de lo esperado) |
| `absolute_residual` | \|residual\| |
| `residual_rank`, `residual_percentile` | Ranking por magnitud absoluta del residual |
| `overperformer_underperformer` | `overperformer`, `underperformer`, `as_expected` |
| `gap_vs_best` | Diferencia vs el mejor valor observado en ese outcome |
| `gap_vs_group_best` | Diferencia vs el mejor del grupo |
| `gap_vs_chile` | Diferencia del valor de este país vs Chile |
| `gap_vs_singapore` | Diferencia del valor de este país vs Singapur |
| `interpretation` | "Observed minus fitted within in-sample descriptive model; not causal." |

### Mensaje del archivo
Detecta **overperformers** (países que rinden mejor de lo esperado según sus características) y **underperformers** (rinden peor). Los gaps vs Chile y Singapur permiten cuantificar exactamente la brecha. Ejemplo: si un país tiene `gap_vs_singapore = -50` en `oxford_ind_company_investment_emerging_tech`, significa que está 50 puntos por debajo de Singapur en ese indicador.

---

## 22. `country_cluster_profile.csv`

**Shape:** (18 filas, 12 columnas)  
**Grano:** 1 fila por país con datos IAPP

### Schema
Estructura base de Q4 (`q4_clusters.csv`) enriquecida con columnas semánticas de Fase 6.2:

| Columna adicional | Valor |
|---|---|
| `score_scope` | `descriptive_regulatory_typology` |
| `independent_prediction` | `False` |
| `causal_claim` | `False` |

### Mensaje del archivo
Reafirma que Q4 es **tipología descriptiva, no ranking normativo**. Los clusters no son "mejores" o "peores" automáticamente. La relación entre cluster y desempeño debe evaluarse cruzando con outcomes en Fase 7.

---

## 23. `country_headline_flags.csv`

**Shape:** (42 filas, 19 columnas)  
**Grano:** 1 fila por país

### Schema

| Columna | Descripción |
|---|---|
| `iso3`, `country_name` | País |
| `is_top_5_q1` … `is_bottom_5_q6` | Flags booleanas de top/bottom 5 en cada Q |
| **`is_consistent_pioneer`** | **Percentil ≥ 0.75 en ≥3 de 5 Qs** |
| **`is_consistent_laggard`** | **Percentil ≤ 0.25 en ≥3 de 5 Qs** |
| `is_chile_benchmark` | País en la lista de benchmarks prioritarios para Chile |
| `is_latam_leader` | ¿Es el mejor de LATAM? |
| `headline_candidate` | ¿Es candidato a headline narrativo? |
| `suggested_headline` | "caso pionero consistente", "caso rezagado...", "benchmark relevante para Chile" |
| `caution_note` | "Descriptive flag; verify robustness in Fase 7." |

### Pioneros consistentes (6)
DEU, FRA, GBR, NLD, **SGP**, USA

### Rezagados consistentes (3)
CHN, CRI, ROU

### Mensaje del archivo
Identifica los **países más interesantes para la narrativa de Fase 8**: los que consistentemente brillan o consistentemente fallan. Chile no es ni pionero ni rezagado consistente, pero aparece como `gap_case`. Los benchmarks (SGP, EST, IRL, ARE, KOR, URY, BRA) están marcados para comparación prioritaria.

---

## 24. `country_learning_patterns.csv`

**Shape:** (2 filas, 13 columnas)  
**Grano:** 1 fila por patrón de aprendizaje identificado

### Schema

| Columna | Descripción |
|---|---|
| `pattern_id` | Identificador del patrón |
| `question_id` | `Q_ALL` (aplica a todas) |
| `group_name` | `global_43` |
| `pattern_type` | `pioneer_pattern`, `laggard_pattern` |
| `countries_in_pattern` | Lista de países (separados por `;`) |
| `shared_strengths` | Fortalezas compartidas por los países del patrón |
| `shared_weaknesses` | Debilidades compartidas |
| `regulatory_profile_summary` | Resumen del perfil regulatorio |
| `ecosystem_profile_summary` | Resumen del ecosistema |
| `lesson_for_chile` | **Lección para política pública chilena** |
| `risk_of_overinterpretation` | **Riesgo de sobreinterpretar el patrón** |
| `evidence_strength` | `pre_robustness_descriptive` (debe validarse en Fase 7) |
| `recommended_phase8_use` | Cómo usar este patrón en Fase 8 |

### Patrones identificados

| Patrón | Países | Lección para Chile |
|---|---|---|
| **Pioneer pattern** | DEU, FRA, GBR, NLD, SGP, USA | Estudiar capacidades institucionales, de adopción y de sector público de los high performers antes de copiar la forma legal |
| **Laggard pattern** | ARG, BGR, CHL, CHN, COL, CRI, GRC, HRV, HUN, MEX | Identificar brechas de capacidad recurrentes; no asumir que la ley por sí sola resuelve debilidades del ecosistema |

### Mensaje del archivo
El archivo más **estratégico** de Fase 6.2. Destila lecciones accionables para Chile a partir de los patrones observados en pioneros y rezagados, siempre con la cautela de no afirmar causalidad y con la advertencia explícita de que Fase 7 debe validar la robustez antes de convertirlas en recomendación.

---

## 25. `country_comparison_pairs.csv`

**Shape:** (35 filas, 7 columnas)  
**Grano:** 1 fila por **dimensión Q × país benchmark**

### Schema

| Columna | Descripción |
|---|---|
| `country_a` | `CHL` (siempre) |
| `country_b` | País benchmark (SGP, EST, IRL, ARE, KOR, URY, BRA) |
| `dimension` | Q1, Q2, Q3, Q5, Q6 |
| `country_a_percentile` | Percentil de Chile en esa dimensión |
| `country_b_percentile` | Percentil del benchmark en esa dimensión |
| `gap_b_minus_a` | Diferencia (positivo = benchmark supera a Chile) |
| `interpretation` | "positive gap means benchmark above Chile" |

### Mensaje del archivo
Cuantifica exactamente la brecha entre Chile y cada benchmark prioritario. Ejemplo: Chile vs Singapur en Q3 → gap de +0.624 (Singapur está 62 puntos percentiles arriba). La brecha más pequeña es en Q5 (0.242). Este archivo alimenta directamente los gráficos de comparación y las country cards.

---

## 26. `country_graphics_catalog.csv`

**Shape:** (38 filas, 3 columnas)  
**Grano:** 1 fila por figura generada

### Schema

| Columna | Descripción |
|---|---|
| `figure_path` | Ruta absoluta al archivo PNG o SVG |
| `figure_type` | Categoría: `q_heatmaps`, `q_rankings`, `country_cards`, `chile_vs_benchmarks`, `pioneer_vs_laggard`, `residuals` |
| `methodology_note` | "descriptive in-sample positioning; not causal or external prediction" |

---

## 27. `figures/` — Gráficos profesionales

**Total:** 19 PNG + 19 SVG (38 archivos) en 7 subcarpetas.  
**Calidad:** 180 DPI, tamaños entre 75 KB y 226 KB (no vacíos).  
**Destacados:** CHL, SGP, EST, IRL, ARE, USA, CHN, BRA, URY.

### 27.1 `figures/q_heatmaps/`
| Archivo | Descripción |
|---|---|
| `heatmap_country_by_q_percentiles.png` (152 KB) | Mapa de calor con 42 países (filas) × 5 preguntas (columnas). Escala RdYlGn (rojo=bajo percentil, verde=alto). Países ordenados por score general descendente. |

### 27.2 `figures/q_rankings/`
| Archivo | Descripción |
|---|---|
| `q1_ranking.png` | Ranking de inversión — todos los países |
| `q2_ranking.png` | Ranking de adopción empresarial |
| `q3_ranking.png` | Ranking de innovación |
| `q5_ranking.png` | Ranking de uso poblacional |
| `q6_ranking.png` | Ranking de sector público |

Cada gráfico muestra barra horizontal con percentil, colores distintivos para CHL (rojo), SGP (verde) y resto de países destacados (azul).

### 27.3 `figures/country_cards/`
Radares polares (spider charts) para 10 países: CHL, SGP, EST, IRL, ARE, KOR, USA, CHN, BRA, URY. Cada radar muestra 5 ejes (Q1–Q6) con percentiles [0,1]. Incluye nota metodológica al pie.

### 27.4 `figures/chile_vs_benchmarks/`
| Archivo | Descripción |
|---|---|
| `chile_vs_singapore_q_profile.png` (75 KB) | Gráfico de líneas comparando Chile (rojo) vs Singapur (verde) en Q1–Q6. Ambos perfiles superpuestos para visualizar brechas. |

### 27.5 `figures/pioneer_vs_laggard/`
| Archivo | Descripción |
|---|---|
| `top_bottom_by_q_panel.png` (140 KB) | Panel de 5×2 subplots mostrando Top 5 y Bottom 5 de cada Q. Verde para top, rojo para bottom. |

### 27.6 `figures/residuals/`
| Archivo | Descripción |
|---|---|
| `observed_vs_expected_selected_outcomes.png` (226 KB) | Scatter plot de valores observados vs ajustados con línea de 45°. Permite identificar visualmente overperformers y underperformers. |

---

## 28. `country_cards_data/` — Fichas consolidadas por país

**Total:** 11 archivos CSV (uno por país clave) + README.

Cada country card contiene **5 secciones** consolidadas en un solo archivo long:

| Sección | Origen | Contenido |
|---|---|---|
| `summary` | `country_q_profile_wide.csv` | Score general, percentiles Q1–Q6, strengths, weaknesses, cluster Q4 |
| `q_profile_long` | `country_q_profile_long.csv` | Todas las filas de ese país en el perfil long (outcomes × Q) |
| `group_rankings` | `country_rankings_by_group.csv` | Rankings del país en cada grupo (LATAM, global, high income, etc.) |
| `model_contributions` | `country_model_contributions.csv` | Contribuciones descriptivas de cada término del modelo para ese país |
| `residuals` | `country_residuals_and_gaps.csv` | Residuales, gaps vs Chile/Singapur, over/underperformer |

### Países con country card

| ISO3 | País | Filas | Relevancia |
|---|---|---|---|
| **CHL** | Chile | 185 | País focal del boletín |
| **SGP** | Singapur | 205 | Benchmark prioritario #1 |
| **USA** | Estados Unidos | 206 | Pionero consistente, líder global |
| **CHN** | China | 202 | Gran potencia IA, rezagado consistente (por missingness/estructura) |
| **EST** | Estonia | 206 | Benchmark digital |
| **IRL** | Irlanda | 207 | Benchmark adopción |
| **ARE** | Emiratos Árabes | 205 | Benchmark inversión/innovación |
| **KOR** | Corea del Sur | 207 | Benchmark tecnológico |
| **BRA** | Brasil | 207 | Par LATAM |
| **URY** | Uruguay | 205 | Par LATAM |
| **JPN** | Japón | 186 | Gran potencia IA |

### Mensaje del archivo
Las country cards son el **insumo directo para Fase 8**. Un analista de política pública puede abrir `CHL_country_card_data.csv`, filtrar por `section='summary'` para ver el perfil general, o por `section='group_rankings'` para ver dónde está Chile en cada submuestra. Todo está en un solo archivo para facilitar la construcción de dashboards, briefings y presentaciones.

---

# PARTE III — RESUMEN DE CONSUMO POR FASE

### Para Fase 7 (Robustez)
Fase 7 debe consumir:
- `country_q_profile_long.csv` y `country_q_profile_wide.csv` para verificar si los pioneros/rezagados son estables al excluir outliers (Leave-Leaders-Out)
- `country_rankings_by_group.csv` para verificar estabilidad de rankings intra-grupo
- `country_headline_flags.csv` y `country_learning_patterns.csv` para validar patrones
- `country_residuals_and_gaps.csv` para sensitivity de over/underperformers

### Para Fase 8 (Narrativa y Política Pública)
Fase 8 debe consumir:
- `country_cards_data/*.csv` para construir Country Cards y Benchmark Briefs
- `figures/` para gráficos ejecutivos listos para presentación
- `country_learning_patterns.csv` para lecciones y recomendaciones (solo las validadas por Fase 7 como `stable`)
- `country_comparison_pairs.csv` para cuantificar brechas Chile vs benchmarks
- `country_headline_flags.csv` para identificar los casos más narrativos

**Regla de oro:** Solo lo que Fase 7 marque como `stable` o `directionally_stable` puede usarse como hallazgo principal en Fase 8. Lo marcado como `fragile` debe ir a anexos o cautelas.

---

*Documento generado automáticamente por el pipeline de auditoría Fase 6.2 — Research_AI_law. Última actualización: 2026-05-08.*
