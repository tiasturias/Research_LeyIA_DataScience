# BLUEPRINT MAESTRO — Reestructuración Arquitectónica Fases 5 a 8

**Proyecto:** Research_AI_law — Boletín 16821-19 Ley Marco de IA Chile  
**Documento:** Blueprint de modificación integral de arquitectura F5–F8  
**Versión propuesta:** `mvp-v0.3-architecture-methodology-correction`  
**Base documental:** `5.PLAN_FASE_MVP_END_TO_END.md`, `6.PLAN_FASE5_V2.1_UPDATE.md`, `8.FASE6_V2.1_UPDATE.md`, `new_met.md`, `MVP_AUDITABLE.xlsx`, investigación metodológica final y blueprints Fase 5 / Fase 6 generados posteriormente.  
**Audiencia:** LLM ejecutor, auditor técnico, investigador principal.  
**Objetivo:** transformar el pipeline F5–F8 completo desde una arquitectura heredada con residuos predictivos hacia una arquitectura observacional, inferencial, auditable, contractual y políticamente defendible.

---

## 0. Instrucción de uso para el LLM ejecutor

Este archivo debe ser tratado como **documento rector de arquitectura**. No es un comentario ni una sugerencia. Su función es indicar, de manera ejecutable, qué debe modificarse en el proyecto completo desde Fase 5 hasta Fase 8.

El LLM ejecutor debe:

1. Leer este documento completo antes de editar código.
2. No tocar Fase 3 ni Fase 4 salvo para lectura vía API.
3. Crear backup de outputs actuales antes de regenerar artefactos.
4. Modificar primero Fase 5, luego Fase 6, luego Fase 7 y finalmente Fase 8.
5. No avanzar de una fase a la siguiente si los tests de la fase anterior fallan.
6. No introducir `train/test split`, `holdout`, `split`, `test set independiente` ni lenguaje causal fuerte.
7. Documentar toda desviación en `mvp_decisions.yaml` y en el manifest global.
8. Generar outputs auditablemente trazables y reproducibles.

**Regla de oro:** si una decisión no puede explicarse a partir del contrato metodológico, no debe implementarse.

---

## 1. Decisión metodológica central

La arquitectura completa F5–F8 debe quedar formalmente redefinida como un:

> **Estudio observacional comparativo de asociaciones ajustadas entre rasgos regulatorios de IA y desarrollo del ecosistema de IA, con robustez interna, sensibilidad y trazabilidad completa.**

No debe ser presentada como:

- un sistema predictivo puro;
- un clasificador de países nuevos;
- una validación externa;
- un estudio causal fuerte;
- un modelo que “predice” inversión, adopción o innovación de Chile.

El objetivo correcto es estimar, para una muestra preregistrada de 43 países y variables observadas, si determinados rasgos regulatorios se asocian con inversión, adopción, innovación, uso poblacional, capacidad pública o perfiles regulatorios, controlando por factores socioeconómicos e institucionales.

---

## 2. Cambio conceptual de arquitectura

### 2.1 Arquitectura heredada que debe eliminarse

```text
FASE5: prepara matriz + crea split train/test 34/9
   ↓
FASE6: usa todos los países, pero conserva narrativa de modelado predictivo
   ↓
FASE7: trata grupos como validación o pseudo-test
   ↓
FASE8: corre riesgo de comunicar predicciones o efectos causales
```

Esta arquitectura es incorrecta para este proyecto porque:

- usa una muestra pequeña `N=43`;
- el supuesto test set no es validación externa real;
- Fase 6 termina usando países que supuestamente eran test;
- se pierde potencia estadística;
- se genera ambigüedad ante auditoría;
- se sobrepromete capacidad predictiva;
- se debilita la utilidad política de los resultados.

### 2.2 Arquitectura correcta

```text
FASE3 / FASE4 inmutables
   ↓ lectura API-only
FASE5: preparación auditable + contrato analítico
   ↓ bundle phase6_ready sin split
FASE6: estimación inferencial por outcome
   ↓ resultados con n_effective, IC95, bootstrap BCa, scores in-sample
FASE7: robustez, sensibilidad, leave-group-out, baselines
   ↓ matriz de estabilidad de conclusiones
FASE8: traducción político-legislativa con lenguaje no causal/no predictivo
```

La nueva arquitectura no elimina la utilidad de modelos; redefine su función. Los modelos no sirven para “predecir países nuevos”, sino para estimar asociaciones, incertidumbre, dirección, magnitud, estabilidad y posicionamiento relativo.

---

## 3. Principios no negociables F5–F8

Estos principios aplican a todas las fases:

1. **Fase 3 y Fase 4 son inmutables.** Solo lectura vía API o archivos de trazabilidad.
2. **No existe holdout externo.** Ningún output puede afirmar validación externa.
3. **No existe `train/test split`.** Prohibido crear o consumir `phase6_train_test_split.csv`.
4. **No existe columna `split`.** Prohibida en feature matrix, schema, workbook, diccionario, contratos y outputs.
5. **Muestra primaria:** 43 países preregistrados.
6. **Variables observadas:** 46 variables core reales cuando corresponda; resolver ambigüedad documental 40 vs 46.
7. **Cero imputación.** Missing se preserva y se documenta.
8. **No usar `fillna(0)` para ocultar ausencia de datos.** En agregados regulatorios, distinguir explícitamente entre ausencia real de característica y dato no observado.
9. **Transformaciones degeneradas se excluyen.** Cualquier z-score, log o derivado no estimable debe marcarse y no entrar al set primario.
10. **Fase 6 usa muestra completa disponible por outcome.** `dropna()` solo sobre columnas estrictamente necesarias del modelo.
11. **Todo modelo reporta `n_effective`.** Sin `n_effective`, el resultado no es aceptable.
12. **Bootstrap BCa por defecto para incertidumbre.** Percentil solo como fallback documentado.
13. **LOOCV no se usa para AUC ni R².** Métricas no definidas con folds unitarios deben quedar como `not_computed`.
14. **Q2/Q5/Q6 usan outcomes continuos o fraccionales como análisis principal.** Binarización alta/baja queda solo como sensibilidad.
15. **Fase 7 es robustez, no test externo.** Leave-group-out no es validación externa.
16. **Fase 8 comunica asociación ajustada, no causalidad fuerte.**
17. **Todas las conclusiones deben llevar nivel de confianza.** `alta`, `media`, `baja`, `no estimable`.
18. **Toda fase genera manifest.** Hashes, versiones, inputs, outputs, decisiones y estado de tests.

---

## 4. Nueva arquitectura de carpetas

La estructura debe quedar organizada así:

```text
F5_F8_MVP/
├── README.md
├── pyproject.toml
├── manifest_mvp.json
├── config/
│   ├── mvp_architecture.yaml
│   ├── methodology_policy.yaml
│   ├── language_policy.yaml
│   ├── analysis_questions.yaml
│   └── forbidden_terms.yaml
│
├── _common/
│   ├── __init__.py
│   ├── paths.py
│   ├── load.py
│   ├── contracts.py
│   ├── validation.py
│   ├── language_guard.py
│   └── manifest.py
│
├── FASE5/
│   ├── README.md
│   ├── config/
│   │   ├── mvp_sample.yaml
│   │   ├── mvp_variables.yaml
│   │   ├── mvp_pipeline.yaml
│   │   ├── mvp_decisions.yaml
│   │   └── phase6_contract_template.yaml
│   ├── src/
│   │   ├── sample.py
│   │   ├── variables.py
│   │   ├── transform.py
│   │   ├── engineer.py
│   │   ├── missingness.py
│   │   ├── membership.py
│   │   ├── phase6_bundle.py
│   │   ├── audit_excel.py
│   │   ├── validate.py
│   │   └── build.py
│   ├── tests/
│   ├── notebooks/
│   └── outputs/
│       ├── feature_matrix_mvp.csv
│       ├── coverage_report_mvp.csv
│       ├── missingness_report_mvp.csv
│       ├── transform_params_mvp.csv
│       ├── transform_exclusion_report.csv
│       ├── regulatory_aggregates_audit.csv
│       ├── analysis_sample_membership.csv
│       ├── MVP_AUDITABLE.xlsx
│       ├── fase5_manifest.json
│       └── phase6_ready/
│
├── FASE6/
│   ├── README.md
│   ├── config/
│   │   ├── fase6_decisions.yaml
│   │   ├── analysis_design_registry.yaml
│   │   ├── model_specs.yaml
│   │   └── output_semantics.yaml
│   ├── src/
│   │   ├── _common_data.py
│   │   ├── _common_estimation.py
│   │   ├── _common_bootstrap.py
│   │   ├── _common_fractional.py
│   │   ├── _common_regression.py
│   │   ├── _common_classification.py
│   │   ├── q1_investment.py
│   │   ├── q2_adoption.py
│   │   ├── q3_innovation.py
│   │   ├── q4_regulatory_profiles.py
│   │   ├── q5_population_usage.py
│   │   ├── q6_public_sector.py
│   │   ├── outputs.py
│   │   ├── validate.py
│   │   └── run_all.py
│   ├── tests/
│   ├── notebooks/
│   └── outputs/
│       ├── primary_results_long.csv
│       ├── model_diagnostics.csv
│       ├── effective_n_by_model.csv
│       ├── q1_results.csv
│       ├── q2_results.csv
│       ├── q3_results.csv
│       ├── q4_clusters.csv
│       ├── q5_results.csv
│       ├── q6_results.csv
│       ├── country_positioning_scores.csv
│       ├── exploratory_binary_sensitivity.csv
│       ├── inferential_appendix.csv
│       └── fase6_manifest.json
│
├── FASE7/
│   ├── README.md
│   ├── config/
│   │   ├── robustness_plan.yaml
│   │   ├── sensitivity_groups.yaml
│   │   └── robustness_decisions.yaml
│   ├── src/
│   │   ├── baselines.py
│   │   ├── sensitivity.py
│   │   ├── leave_group_out.py
│   │   ├── outliers.py
│   │   ├── stability.py
│   │   ├── conclusion_matrix.py
│   │   ├── validate.py
│   │   └── run_all.py
│   ├── tests/
│   ├── notebooks/
│   └── outputs/
│       ├── baseline_comparisons.csv
│       ├── sensitivity_analysis.csv
│       ├── leave_group_out_analysis.csv
│       ├── outlier_influence.csv
│       ├── robustness_registry.csv
│       ├── conclusion_stability_matrix.csv
│       └── fase7_manifest.json
│
└── FASE8/
    ├── README.md
    ├── config/
    │   ├── reporting_policy.yaml
    │   ├── findings_templates.yaml
    │   └── policy_translation_rules.yaml
    ├── src/
    │   ├── findings.py
    │   ├── chile_focal.py
    │   ├── deep_dives.py
    │   ├── narrative.py
    │   ├── excel_final.py
    │   ├── reporting.py
    │   ├── validate.py
    │   └── run_all.py
    ├── tests/
    ├── notebooks/
    └── outputs/
        ├── EXECUTIVE_SUMMARY.md
        ├── POLICY_BRIEF_CHILE.md
        ├── METHODOLOGICAL_APPENDIX.md
        ├── MVP_AUDITABLE_FINAL.xlsx
        ├── chile_findings.csv
        ├── findings_consolidados.csv
        ├── recommendation_matrix.csv
        └── fase8_manifest.json
```

---

## 5. Contratos entre fases

La arquitectura correcta depende de contratos explícitos. Cada fase debe validar el contrato de la fase anterior antes de ejecutarse.

### 5.1 Contrato Fase 5 → Fase 6

Archivo obligatorio:

```text
FASE5/outputs/phase6_ready/phase6_modeling_contract.yaml
```

Contenido mínimo:

```yaml
version: "0.3"
methodology_version: "mvp-v0.3-architecture-methodology-correction"
methodology: "inferential_comparative_observational"
primary_estimand: "adjusted_association"
grain: "country_iso3"
primary_key: "iso3"

sample_policy:
  n_primary_sample: 43
  primary_analysis_scope: "full_preregistered_sample_available_by_outcome"
  use_holdout_test_set: false
  train_test_split_created: false
  split_column_present: false
  external_validation_available: false
  effective_n_rule: "listwise_deletion_per_model_on_required_y_x_only"

missingness_policy:
  no_imputation: true
  missing_values_preserved: true
  missingness_must_be_reported: true
  fillna_zero_allowed_only_when_semantically_true_zero: true
  fillna_zero_for_unknown_missing_forbidden: true

transformation_policy:
  robust_zscore_allowed: true
  zero_mad_or_not_estimable_policy: "flag_and_exclude_from_primary_models"
  log_transform_policy: "apply_only_when_defined_and_documented"
  transform_params_file: "phase6_transform_params.csv"
  transform_exclusion_file: "phase6_transform_exclusion_report.csv"

validation_policy:
  primary_uncertainty: "bootstrap_bca_confidence_intervals"
  internal_validation:
    - repeated_kfold_cv_where_appropriate
    - bootstrap_optimism_where_appropriate
  loocv_policy: "not_for_auc_or_r2"
  robustness_phase: "FASE7"
  leave_group_out_is_external_test: false

output_semantics:
  country_level_scores: "in_sample_descriptive_positioning"
  independent_predictions: false
  causal_claims_allowed: false

language_policy:
  allowed:
    - "association"
    - "adjusted association"
    - "uncertainty"
    - "confidence interval"
    - "internal validation"
    - "robustness"
    - "sensitivity"
    - "descriptive positioning"
  forbidden_without_extra_design:
    - "causal effect"
    - "impacto causal"
    - "test set independiente"
    - "external validation"
    - "predicción independiente"
```

### 5.2 Contrato Fase 6 → Fase 7

Archivo obligatorio:

```text
FASE6/outputs/phase7_robustness_contract.yaml
```

Contenido mínimo:

```yaml
version: "0.3"
source_phase: "FASE6"
required_inputs:
  - primary_results_long.csv
  - model_diagnostics.csv
  - effective_n_by_model.csv
  - country_positioning_scores.csv

robustness_scope:
  purpose: "evaluate_stability_not_external_validation"
  baseline_comparisons_required: true
  sensitivity_required: true
  leave_group_out_required: true
  outlier_influence_required: true

sensitivity_groups:
  - exclude_usa
  - exclude_china
  - exclude_usa_china
  - exclude_large_ai_powers
  - exclude_ai_leaders
  - leave_region_out
  - leave_income_group_out
  - latam_only_sensitivity
  - europe_without_eu_laggards

conclusion_policy:
  stability_labels:
    - stable
    - directionally_stable
    - fragile
    - not_estimable
  sign_flip_must_be_reported: true
  n_effective_change_must_be_reported: true
```

### 5.3 Contrato Fase 7 → Fase 8

Archivo obligatorio:

```text
FASE7/outputs/phase8_reporting_contract.yaml
```

Contenido mínimo:

```yaml
version: "0.3"
source_phase: "FASE7"
required_inputs:
  - conclusion_stability_matrix.csv
  - robustness_registry.csv
  - baseline_comparisons.csv
  - leave_group_out_analysis.csv

reporting_policy:
  only_report_findings_with_traceability: true
  every_finding_requires:
    - question_id
    - outcome
    - main_association_direction
    - n_effective
    - uncertainty
    - robustness_label
    - limitation_note
    - political_translation

forbidden_reporting:
  - "causal effect"
  - "proof"
  - "demonstrates causality"
  - "external validation"
  - "independent prediction"
```

---

## 6. Fase 5 — Nueva función arquitectónica

### 6.1 Qué debe ser Fase 5

Fase 5 debe ser una fase de:

- preparación de datos;
- congelamiento de muestra;
- curaduría de variables;
- trazabilidad;
- control de missingness;
- definición de membresía analítica;
- construcción del contrato para Fase 6;
- generación de Excel auditable.

Fase 5 **no** debe ser:

- pre-modelado predictivo;
- partición train/test;
- imputación;
- selección oportunista de variables por performance;
- modificación de Fase 3 o Fase 4.

### 6.2 Cambios obligatorios en Fase 5

1. Eliminar cualquier import de `train_test_split`.
2. Eliminar función `_build_split()` si existe.
3. Eliminar outputs:
   - `outputs/mvp_train_test_split.csv`
   - `outputs/phase6_ready/phase6_train_test_split.csv`
4. Eliminar columna `split` de:
   - `feature_matrix_mvp.csv`
   - `phase6_feature_matrix.csv`
   - `phase6_schema.csv`
   - `phase6_schema.json`
   - `phase6_column_groups.yaml`
   - `MVP_AUDITABLE.xlsx`
   - diccionario de columnas
5. Crear `analysis_sample_membership.csv`.
6. Crear `phase6_analysis_sample_membership.csv` dentro de `phase6_ready`.
7. Reescribir `phase6_modeling_contract.yaml` bajo la lógica inferencial.
8. Crear `missingness_report_mvp.csv`.
9. Crear `regulatory_aggregates_audit.csv`.
10. Crear `transform_exclusion_report.csv`.
11. Actualizar `MVP_AUDITABLE.xlsx` para que no mencione split.
12. Actualizar `fase5_manifest.json`.
13. Actualizar tests.

### 6.3 Política correcta de agregados regulatorios

El Excel actual mostró un riesgo crítico: construir agregados regulatorios con `fillna(0)` puede convertir datos ausentes en ceros. Eso no es aceptable salvo que el cero tenga significado sustantivo verificado.

La nueva regla es:

```python
# PROHIBIDO como regla general
n_binding = df[binding_cols].fillna(0).sum(axis=1)
```

Debe reemplazarse por una lógica auditable:

```python
def audited_binary_sum(df, cols, min_observed_share=0.5):
    observed = df[cols].notna().sum(axis=1)
    possible = len(cols)
    values_sum = df[cols].sum(axis=1, skipna=True)
    observed_share = observed / possible

    out = values_sum.where(observed_share >= min_observed_share, pd.NA)
    return pd.DataFrame({
        "value": out,
        "n_observed_components": observed,
        "n_possible_components": possible,
        "observed_share": observed_share,
        "aggregate_estimable": observed_share >= min_observed_share,
    })
```

Cada agregado debe tener columnas auxiliares:

```text
n_binding
n_binding_n_observed_components
n_binding_n_possible_components
n_binding_observed_share
n_binding_estimable

n_non_binding
n_non_binding_n_observed_components
n_non_binding_n_possible_components
n_non_binding_observed_share
n_non_binding_estimable

n_hybrid
n_hybrid_n_observed_components
n_hybrid_n_possible_components
n_hybrid_observed_share
n_hybrid_estimable
```

### 6.4 Política de transformaciones no estimables

Si una transformación no puede estimarse, no se debe reemplazar silenciosamente por cero.

Casos típicos:

- MAD = 0 en z-score robusto;
- variable constante;
- variable con menos de 2 valores no nulos;
- log sobre valores inválidos;
- variable categórica sin variación;
- derivado con cobertura insuficiente.

Regla:

```yaml
transform_status:
  ok: "puede usarse en modelos primarios"
  zero_mad_or_not_estimable: "excluir de modelos primarios; permitir solo descripción si aporta contexto"
  insufficient_coverage: "excluir"
  invalid_domain: "excluir"
```

Debe generarse:

```text
FASE5/outputs/transform_exclusion_report.csv
```

Columnas mínimas:

```text
source_variable
derived_variable
transform_type
status
reason
n_non_null
n_unique
mad
included_in_primary_models
included_in_descriptive_outputs
```

### 6.5 `analysis_sample_membership.csv`

Debe reemplazar totalmente al split.

Columnas mínimas:

```text
iso3
country_name_canonical
region
income_group
is_primary_analysis_sample
sample_inclusion_category
inclusion_reason
is_chile_focal
is_ai_leader_sensitivity
is_large_ai_power_sensitivity
is_latam_peer_sensitivity
is_eu_member_sensitivity
is_eu_laggard_sensitivity
has_complete_region_metadata
has_complete_income_metadata
leave_group_region
leave_group_income
notes
```

Prohibido incluir:

```text
split
train
test
holdout
```

### 6.6 Outputs finales de Fase 5

```text
FASE5/outputs/
├── feature_matrix_mvp.csv
├── coverage_report_mvp.csv
├── missingness_report_mvp.csv
├── mvp_countries.csv
├── mvp_variables_catalog.csv
├── mvp_transform_params.csv
├── transform_exclusion_report.csv
├── regulatory_aggregates_audit.csv
├── analysis_sample_membership.csv
├── MVP_AUDITABLE.xlsx
├── fase5_manifest.json
└── phase6_ready/
    ├── phase6_feature_matrix.csv
    ├── phase6_schema.csv
    ├── phase6_schema.json
    ├── phase6_variables_catalog.csv
    ├── phase6_transform_params.csv
    ├── phase6_transform_exclusion_report.csv
    ├── phase6_column_groups.yaml
    ├── phase6_missingness_by_column.csv
    ├── phase6_missingness_by_country.csv
    ├── phase6_regulatory_aggregates_audit.csv
    ├── phase6_llm_context.json
    ├── phase6_modeling_contract.yaml
    ├── phase6_analysis_sample_membership.csv
    └── phase6_ready_manifest.json
```

---

## 7. Fase 6 — Nueva función arquitectónica

### 7.1 Qué debe ser Fase 6

Fase 6 debe ser una fase de:

- estimación de asociaciones ajustadas;
- diseño analítico por outcome;
- cálculo de incertidumbre;
- validación interna auxiliar;
- generación de scores descriptivos in-sample;
- producción de outputs normalizados para robustez y reporting.

Fase 6 **no** debe ser:

- evaluación out-of-sample;
- test externo;
- predicción independiente;
- causalidad fuerte;
- clasificación primaria cuando el outcome es continuo o fraccional.

### 7.2 Pre-flight obligatorio

Antes de ejecutar Fase 6:

```python
from pathlib import Path
import pandas as pd
import yaml

bundle = Path("FASE5/outputs/phase6_ready")
assert bundle.exists()
assert (bundle / "phase6_feature_matrix.csv").exists()
assert (bundle / "phase6_modeling_contract.yaml").exists()
assert (bundle / "phase6_analysis_sample_membership.csv").exists()
assert not (bundle / "phase6_train_test_split.csv").exists()

fm = pd.read_csv(bundle / "phase6_feature_matrix.csv")
assert len(fm) == 43
assert "split" not in fm.columns

contract = yaml.safe_load((bundle / "phase6_modeling_contract.yaml").read_text())
assert contract["methodology"] == "inferential_comparative_observational"
assert contract["sample_policy"]["use_holdout_test_set"] is False
assert contract["sample_policy"]["train_test_split_created"] is False
assert contract["sample_policy"]["split_column_present"] is False
```

Si falla, abortar.

### 7.3 Registro de diseños analíticos

Debe existir:

```text
FASE6/config/analysis_design_registry.yaml
```

Estructura mínima:

```yaml
Q1_investment:
  primary_outcome_type: "continuous"
  primary_estimators:
    - robust_ols
    - ols_bootstrap_bca
  auxiliary_estimators:
    - ridge_cv_internal
    - lasso_cv_internal
  psm_policy: "exploratory_only"

Q2_adoption:
  primary_outcome_type: "continuous_or_fractional"
  primary_estimators:
    - fractional_logit_if_pct_0_1
    - robust_ols_if_score_0_100
    - ols_bootstrap_bca
  sensitivity_estimators:
    - median_binarized_logistic
    - random_forest_classifier_internal_cv
  binary_primary_forbidden: true

Q3_innovation:
  primary_outcome_type: "continuous"
  primary_estimators:
    - robust_ols
    - ols_bootstrap_bca
  auxiliary_estimators:
    - ridge_cv_internal
    - gradient_boosting_internal_cv

Q4_regulatory_profiles:
  primary_outcome_type: "unsupervised_descriptive"
  primary_methods:
    - hierarchical_clustering_jaccard
    - kmeans_sensitivity
  external_validation: false

Q5_population_usage:
  primary_outcome_type: "fractional_or_continuous"
  primary_estimators:
    - fractional_logit_if_pct_0_1
    - robust_ols_if_score_0_100
    - ols_bootstrap_bca
  sensitivity_estimators:
    - median_binarized_logistic
  binary_primary_forbidden: true

Q6_public_sector:
  primary_outcome_type: "continuous_score"
  primary_estimators:
    - robust_ols
    - ols_bootstrap_bca
  sensitivity_estimators:
    - median_binarized_logistic_if_needed
  binary_primary_forbidden: true
```

### 7.4 Reglas de modelado por outcome

Cada modelo debe:

1. leer `phase6_feature_matrix.csv`;
2. validar contrato inferencial;
3. seleccionar columnas requeridas;
4. aplicar `dropna()` solo sobre Y + X necesarias;
5. calcular `n_effective`;
6. abortar si `n_effective` es insuficiente;
7. ajustar modelo primario;
8. calcular IC95 con bootstrap BCa cuando corresponda;
9. guardar coeficientes, incertidumbre, p-values/FDR si aplica;
10. guardar diagnósticos;
11. etiquetar scope;
12. no generar test metrics.

Columnas obligatorias en resultados:

```text
question_id
outcome
model_id
model_family
analysis_scope
validation_scope
holdout_used
n_primary_sample
n_effective
n_missing_required
predictor
coefficient
std_error
ci95_low
ci95_high
p_value
p_value_fdr
bootstrap_method
n_bootstrap
estimable
estimation_status
interpretation_label
```

### 7.5 Q2/Q5/Q6: regla metodológica reforzada

La investigación final concluyó que binarizar porcentajes o scores por mediana destruye información. Por tanto:

- Si Y es porcentaje 0–100, convertir a 0–1 y usar modelo fraccional o robust OLS según viabilidad.
- Si Y es score 0–100, usar análisis continuo.
- Si Y es porcentaje con muchos 0/1 o borde, documentar y usar fractional logit o quasi-binomial si viable.
- La variable binaria alta/baja por mediana solo puede ir a `exploratory_binary_sensitivity.csv`.
- La narrativa principal nunca debe decir “el país será de alta adopción”; debe decir “posición descriptiva relativa en la muestra”.

### 7.6 Bootstrap BCa

Fase 6 debe implementar `bootstrap_bca` como método primario de IC cuando sea viable.

Fallbacks permitidos:

```yaml
bootstrap_policy:
  primary: "BCa"
  fallback_1: "basic_bootstrap_if_bca_fails"
  fallback_2: "percentile_bootstrap_only_if_documented"
  min_resamples: 2000
  seed: 42
  fail_if_all_bootstrap_invalid: true
```

### 7.7 LOOCV

Prohibido reportar:

```text
LOOCV AUC
LOOCV R2
```

Debe reemplazarse por:

```text
auc_loocv = NaN
r2_loocv = NaN
loocv_note = "not_computed_metric_undefined_for_single_observation_test_folds"
```

### 7.8 Outputs finales de Fase 6

```text
FASE6/outputs/
├── primary_results_long.csv
├── model_diagnostics.csv
├── effective_n_by_model.csv
├── q1_results.csv
├── q2_results.csv
├── q3_results.csv
├── q4_clusters.csv
├── q4_distance_matrix.csv
├── q5_results.csv
├── q6_results.csv
├── country_positioning_scores.csv
├── exploratory_binary_sensitivity.csv
├── psm_exploratory_results.csv
├── inferential_appendix.csv
├── phase7_robustness_contract.yaml
└── fase6_manifest.json
```

---

## 8. Fase 7 — Nueva función arquitectónica

### 8.1 Qué debe ser Fase 7

Fase 7 debe ser el guardián de robustez científica. No reinterpreta la muestra como test externo. Evalúa si las conclusiones sobreviven a perturbaciones razonables.

Debe responder:

- ¿La dirección de la asociación se mantiene?
- ¿La magnitud cambia de manera sustantiva?
- ¿El resultado depende de USA, China o líderes extremos?
- ¿El resultado depende de Europa o LATAM?
- ¿Las variables regulatorias agregan información sobre controles socioeconómicos?
- ¿La conclusión es estable, direccional, frágil o no estimable?

### 8.2 Inputs de Fase 7

```text
FASE6/outputs/primary_results_long.csv
FASE6/outputs/model_diagnostics.csv
FASE6/outputs/effective_n_by_model.csv
FASE6/outputs/country_positioning_scores.csv
FASE6/outputs/phase7_robustness_contract.yaml
FASE5/outputs/phase6_ready/phase6_analysis_sample_membership.csv
```

### 8.3 Robustez obligatoria

Fase 7 debe ejecutar:

1. Baseline trivial.
2. Baseline solo controles.
3. Modelo completo con variables regulatorias.
4. Exclusión USA.
5. Exclusión China.
6. Exclusión USA + China.
7. Exclusión grandes potencias IA.
8. Exclusión AI leaders.
9. Leave-region-out.
10. Leave-income-group-out.
11. LATAM-only sensitivity si N lo permite.
12. Exclusión EU laggards.
13. Influencia de outliers.
14. Estabilidad de clusters Q4.
15. Comparación de signos, magnitudes e intervalos.

### 8.4 Etiquetas de estabilidad

Cada hallazgo debe recibir una etiqueta:

```yaml
stable:
  definition: "signo y conclusión sustantiva se mantienen en la mayoría de sensibilidades clave"

directionally_stable:
  definition: "signo general se mantiene, pero magnitud o significancia varía"

fragile:
  definition: "conclusión cambia ante exclusiones razonables o depende de pocos países"

not_estimable:
  definition: "n_effective insuficiente o modelo no converge"
```

### 8.5 Outputs finales de Fase 7

```text
FASE7/outputs/
├── baseline_comparisons.csv
├── sensitivity_analysis.csv
├── leave_group_out_analysis.csv
├── outlier_influence.csv
├── cluster_stability.csv
├── robustness_registry.csv
├── conclusion_stability_matrix.csv
├── phase8_reporting_contract.yaml
└── fase7_manifest.json
```

Columnas mínimas de `conclusion_stability_matrix.csv`:

```text
question_id
outcome
primary_model
main_predictor
full_sample_direction
full_sample_n_effective
full_sample_ci95
baseline_gain
sensitivity_tests_passed
sensitivity_tests_failed
sign_flip_detected
largest_magnitude_change
robustness_label
reportable_in_phase8
limitation_note
```

---

## 9. Fase 8 — Nueva función arquitectónica

### 9.1 Qué debe ser Fase 8

Fase 8 debe traducir resultados técnicos en conclusiones político-legislativas prudentes, trazables y defendibles.

Debe producir:

- resumen ejecutivo;
- brief para Chile;
- matriz de hallazgos;
- recomendaciones con nivel de confianza;
- Excel final auditado;
- apéndice metodológico;
- notebook maestro.

Fase 8 no recalcula modelos. Solo consume outputs cerrados de Fases 5–7.

### 9.2 Inputs de Fase 8

```text
FASE5/outputs/MVP_AUDITABLE.xlsx
FASE6/outputs/primary_results_long.csv
FASE6/outputs/country_positioning_scores.csv
FASE7/outputs/conclusion_stability_matrix.csv
FASE7/outputs/robustness_registry.csv
FASE7/outputs/phase8_reporting_contract.yaml
```

### 9.3 Política de lenguaje

Permitido:

```text
se observa una asociación ajustada
la asociación es consistente con
la evidencia comparada sugiere
el resultado es estable/direccional/frágil
Chile se ubica en una posición relativa
el hallazgo debe interpretarse con cautela
```

Prohibido:

```text
la regulación causa
impacto causal
predice que Chile tendrá
test externo demuestra
validación independiente prueba
se comprueba que
```

### 9.4 Estructura de `EXECUTIVE_SUMMARY.md`

```markdown
# Informe Ejecutivo — Research_AI_law MVP F5–F8

## 1. Mensaje principal
- Respuesta sintética a la hipótesis.
- Qué se puede afirmar y qué no.

## 2. Metodología en lenguaje claro
- 43 países.
- Variables observadas.
- Estudio observacional comparativo.
- Sin test externo.
- Asociación ajustada, no causalidad fuerte.

## 3. Hallazgos principales
- Tabla Q1–Q6.
- Dirección, magnitud, incertidumbre, robustez.

## 4. Chile en perspectiva comparada
- Posición relativa.
- Vecinos estadísticos.
- Cluster regulatorio.
- Fortalezas y brechas.

## 5. Qué tipo de regulación aparece asociado a mejores ecosistemas IA
- Lectura prudente.
- Diferencia entre binding, non-binding, hybrid.

## 6. Robustez y sensibilidad
- Qué hallazgos sobreviven.
- Qué hallazgos son frágiles.

## 7. Implicancias para Boletín 16821-19
- Recomendaciones prudentes.
- Qué evitar.
- Qué reforzar.

## 8. Limitaciones
- N pequeño.
- Sin causalidad fuerte.
- Sin validación externa.
- Variables faltantes.
- Snapshot temporal.

## 9. Próximos pasos
- Validación experta.
- NLP legal.
- multiverse analysis.
- validación externa futura.
```

### 9.5 Matriz de recomendaciones

Archivo:

```text
FASE8/outputs/recommendation_matrix.csv
```

Columnas:

```text
recommendation_id
policy_area
finding_source
question_id
technical_finding
robustness_label
confidence_level
recommendation_text
political_risk
technical_limitation
suggested_wording
forbidden_overclaim
```

### 9.6 Outputs finales de Fase 8

```text
FASE8/outputs/
├── EXECUTIVE_SUMMARY.md
├── POLICY_BRIEF_CHILE.md
├── METHODOLOGICAL_APPENDIX.md
├── MVP_AUDITABLE_FINAL.xlsx
├── chile_findings.csv
├── findings_consolidados.csv
├── recommendation_matrix.csv
├── notebook_execution_report.csv
└── fase8_manifest.json
```

---

## 10. Tests globales anti-regresión

Deben existir tests globales en:

```text
F5_F8_MVP/tests_global/
```

### 10.1 Test: no split artifacts

```python
def test_no_split_artifacts_anywhere(project_root):
    forbidden_files = [
        "mvp_train_test_split.csv",
        "phase6_train_test_split.csv",
    ]
    for path in project_root.rglob("*"):
        assert path.name not in forbidden_files
```

### 10.2 Test: no split column

```python
def test_no_split_column_in_csv_outputs(project_root):
    import pandas as pd
    for path in project_root.rglob("*.csv"):
        df = pd.read_csv(path, nrows=5)
        assert "split" not in df.columns, f"split column found in {path}"
```

### 10.3 Test: forbidden language

```python
def test_forbidden_language_in_reports(project_root):
    forbidden = [
        "test set independiente",
        "external validation",
        "predicción independiente",
        "impacto causal",
        "causal effect",
    ]
    text_files = list(project_root.rglob("*.md")) + list(project_root.rglob("*.ipynb"))
    for path in text_files:
        txt = path.read_text(encoding="utf-8", errors="ignore").lower()
        for term in forbidden:
            assert term.lower() not in txt, f"Forbidden term {term} in {path}"
```

### 10.4 Test: outputs report `n_effective`

```python
def test_phase6_outputs_have_effective_n(project_root):
    import pandas as pd
    outputs = project_root / "FASE6" / "outputs"
    for name in ["primary_results_long.csv", "q1_results.csv", "q2_results.csv", "q3_results.csv", "q5_results.csv", "q6_results.csv"]:
        path = outputs / name
        if path.exists():
            df = pd.read_csv(path)
            assert "n_effective" in df.columns
            assert df["n_effective"].notna().all()
```

### 10.5 Test: no holdout used

```python
def test_holdout_used_false(project_root):
    import pandas as pd
    for path in (project_root / "FASE6" / "outputs").glob("*.csv"):
        df = pd.read_csv(path)
        if "holdout_used" in df.columns:
            assert (df["holdout_used"] == False).all()
```

---

## 11. Manifiesto global

Debe generarse:

```text
F5_F8_MVP/manifest_mvp.json
```

Contenido mínimo:

```json
{
  "project": "Research_AI_law",
  "methodology_version": "mvp-v0.3-architecture-methodology-correction",
  "methodology": "inferential_comparative_observational",
  "primary_estimand": "adjusted_association",
  "created_at": "<ISO8601>",
  "git_sha": "<git_sha>",
  "sample_n": 43,
  "observed_core_variables": 46,
  "holdout_used": false,
  "train_test_split_created": false,
  "external_validation_available": false,
  "causal_claims_allowed": false,
  "phases": {
    "FASE5": {
      "status": "completed",
      "manifest": "FASE5/outputs/fase5_manifest.json",
      "tests_passed": true
    },
    "FASE6": {
      "status": "completed",
      "manifest": "FASE6/outputs/fase6_manifest.json",
      "tests_passed": true
    },
    "FASE7": {
      "status": "completed",
      "manifest": "FASE7/outputs/fase7_manifest.json",
      "tests_passed": true
    },
    "FASE8": {
      "status": "completed",
      "manifest": "FASE8/outputs/fase8_manifest.json",
      "tests_passed": true
    }
  },
  "forbidden_artifacts_absent": true,
  "language_guard_passed": true,
  "input_hashes": {},
  "output_hashes": {}
}
```

---

## 12. Orden de implementación

El LLM ejecutor debe seguir este orden:

### Paso 0 — Backup y diagnóstico

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP
cp -r FASE5/outputs FASE5/outputs.pre_architecture_correction || true
cp -r FASE6/outputs FASE6/outputs.pre_architecture_correction || true
cp -r FASE7/outputs FASE7/outputs.pre_architecture_correction || true
cp -r FASE8/outputs FASE8/outputs.pre_architecture_correction || true
```

Luego buscar residuos:

```bash
rg -n "train_test|train/test|test set|holdout|split|external validation|predicción independiente|impacto causal" .
```

Clasificar cada hallazgo en:

```text
must_remove
allowed_as_forbidden_term_test
allowed_in_methodological_explanation_only
```

### Paso 1 — Actualizar configuración global

Crear:

```text
config/mvp_architecture.yaml
config/methodology_policy.yaml
config/language_policy.yaml
config/analysis_questions.yaml
config/forbidden_terms.yaml
```

### Paso 2 — Corregir Fase 5

Aplicar blueprint Fase 5 v2.1 reforzado:

- eliminar split;
- crear membership;
- corregir agregados;
- corregir transformaciones;
- regenerar bundle;
- regenerar Excel;
- correr tests.

### Paso 3 — Corregir Fase 6

Aplicar blueprint Fase 6 v2.1+:

- validar bundle Fase 5;
- registrar diseños;
- usar outcomes continuos/fraccionales;
- mover binarios a sensibilidad;
- eliminar LOOCV inválido;
- generar outputs normalizados;
- crear contrato Fase 7;
- correr tests.

### Paso 4 — Corregir Fase 7

Implementar robustez:

- baselines;
- sensibilidad;
- leave-group-out;
- outliers;
- estabilidad;
- contrato Fase 8;
- correr tests.

### Paso 5 — Corregir Fase 8

Implementar reporting:

- resumen ejecutivo;
- policy brief;
- apéndice metodológico;
- Excel final;
- matriz de recomendaciones;
- guard de lenguaje;
- correr tests.

### Paso 6 — Manifest global y cierre

- generar `manifest_mvp.json`;
- correr tests globales;
- ejecutar notebooks si existen;
- crear tag git;
- redactar cierre técnico.

---

## 13. Criterios de aceptación global

El proyecto F5–F8 está correctamente actualizado solo si se cumplen todos estos criterios:

### 13.1 Arquitectura

- [ ] Existe `config/mvp_architecture.yaml`.
- [ ] Cada fase tiene README actualizado.
- [ ] Cada fase tiene manifest.
- [ ] Cada fase tiene tests.
- [ ] Cada fase consume outputs de la fase anterior vía contrato.
- [ ] Ninguna fase escribe en outputs de otra fase.

### 13.2 Metodología

- [ ] El proyecto se declara como `inferential_comparative_observational`.
- [ ] `primary_estimand = adjusted_association`.
- [ ] No existe holdout externo.
- [ ] No existe train/test split.
- [ ] Fase 6 usa muestra disponible por outcome.
- [ ] Fase 7 es sensibilidad/robustez.
- [ ] Fase 8 no comunica causalidad fuerte.

### 13.3 Datos

- [ ] 43 países preregistrados.
- [ ] Chile presente en todos los outputs relevantes.
- [ ] Variables core armonizadas como 46 observadas.
- [ ] Missing preservado.
- [ ] No imputación.
- [ ] Agregados regulatorios auditados.
- [ ] Transformaciones no estimables excluidas.

### 13.4 Modelado

- [ ] Cada modelo reporta `n_effective`.
- [ ] Cada resultado tiene `holdout_used = False`.
- [ ] Q2/Q5/Q6 no usan binarización como análisis principal.
- [ ] Bootstrap BCa o fallback documentado.
- [ ] No LOOCV AUC/R².
- [ ] PSM marcado como exploratorio.

### 13.5 Robustez

- [ ] Baseline trivial.
- [ ] Baseline solo controles.
- [ ] Leave-group-out.
- [ ] Exclusión USA/China/líderes.
- [ ] Stability matrix.
- [ ] Etiqueta de robustez por hallazgo.

### 13.6 Reporting

- [ ] `EXECUTIVE_SUMMARY.md` generado.
- [ ] `POLICY_BRIEF_CHILE.md` generado.
- [ ] `METHODOLOGICAL_APPENDIX.md` generado.
- [ ] `MVP_AUDITABLE_FINAL.xlsx` generado.
- [ ] `recommendation_matrix.csv` generado.
- [ ] Lenguaje prohibido ausente.
- [ ] Cada recomendación tiene confianza y limitación.

---

## 14. Cambios específicos al plan maestro `5.PLAN_FASE_MVP_END_TO_END.md`

El plan maestro debe modificarse así:

### 14.1 Versión

Reemplazar:

```text
mvp-v0.2-methodology-correction
```

por:

```text
mvp-v0.3-architecture-methodology-correction
```

### 14.2 Decisión metodológica

Agregar que F5–F8 no solo corrige train/test, sino que reorganiza responsabilidades:

```text
Fase 5 = contrato auditable de datos y muestra.
Fase 6 = estimación inferencial por outcome.
Fase 7 = robustez y sensibilidad.
Fase 8 = traducción político-legislativa no causal.
```

### 14.3 Variables 40 vs 46

Resolver ambigüedad:

```text
El MVP conserva 46 variables observadas reales. Cuando se hable de 40 variables core, debe aclararse si se refiere a núcleo v1.0 previo a expansión Q5/Q6. La versión v0.3 usa 46 observadas como contrato operativo.
```

### 14.4 Q2/Q5/Q6

Reemplazar clasificación primaria por:

```text
Los outcomes de adopción, uso poblacional y sector público se modelan como continuos/fraccionales en el análisis primario. La binarización por mediana se conserva únicamente como sensibilidad exploratoria.
```

### 14.5 Fase 7

Reescribir como:

```text
Fase 7 no evalúa generalización externa. Evalúa robustez interna, estabilidad de conclusiones y sensibilidad a decisiones razonables de muestra y especificación.
```

### 14.6 Fase 8

Agregar:

```text
Fase 8 no puede convertir asociaciones en causalidad ni scores descriptivos en predicciones independientes. Toda recomendación política debe vincularse a un hallazgo, una etiqueta de robustez y una limitación.
```

---

## 15. Riesgos de la migración y mitigaciones

| Riesgo | Impacto | Mitigación |
|---|---:|---|
| Se borra el split en CSV pero queda en notebook o README | Alto | Test global de lenguaje y búsqueda `rg` |
| Fase 6 sigue usando binarios como primarios | Alto | `analysis_design_registry.yaml` + tests de Q2/Q5/Q6 |
| Agregados regulatorios siguen usando `fillna(0)` | Alto | `regulatory_aggregates_audit.csv` + test de missingness |
| Transformaciones degeneradas entran a modelos | Medio/alto | `transform_exclusion_report.csv` + validación de columnas primarias |
| Fase 7 se presenta como validación externa | Alto | `phase8_reporting_contract.yaml` + language guard |
| Fase 8 sobrevende causalidad | Alto | matriz de recomendaciones con `forbidden_overclaim` |
| Outputs anteriores sobreviven y contaminan lectura | Alto | limpiar outputs o mover a carpeta backup pre-corrección |
| N efectivo insuficiente en algunos outcomes | Medio | reportar `not_estimable`, no forzar resultado |
| Chile falta por `dropna` en algún score | Medio | reportar score no estimable y explicar missingness |

---

## 16. Plantilla de cierre técnico

Al finalizar, crear:

```text
F5_F8_MVP/CIERRE_TECNICO_MVP_V0_3.md
```

Estructura:

```markdown
# Cierre técnico MVP v0.3 — Research_AI_law

## 1. Resumen de corrección
- Qué se corrigió.
- Por qué se corrigió.
- Qué fases fueron modificadas.

## 2. Estado de artefactos
- Tabla por fase con outputs.
- Hashes principales.

## 3. Estado de tests
- FASE5.
- FASE6.
- FASE7.
- FASE8.
- Globales.

## 4. Decisiones metodológicas firmadas
- Sin split.
- Asociación ajustada.
- Q2/Q5/Q6 continuos/fraccionales.
- Robustez no externa.
- Lenguaje no causal.

## 5. Limitaciones pendientes
- N pequeño.
- No validación externa.
- No causalidad fuerte.
- No NLP legal.
- No panel temporal.

## 6. Próxima iteración recomendada
- Multiverse.
- NLP legal.
- validación experta.
- nuevos países/datos para validación externa real.
```

---

## 17. Resultado final esperado

Al terminar esta reestructuración, el proyecto debe poder ser defendido así:

> “Research_AI_law F5–F8 es un MVP inferencial-comparativo observacional, construido sobre 43 países preregistrados y variables auditables. No usa un holdout artificial ni pretende validación externa. Estima asociaciones ajustadas por outcome, reporta incertidumbre, evalúa robustez y traduce los hallazgos a recomendaciones prudentes para Chile. Cada número es trazable y cada conclusión tiene una etiqueta de estabilidad.”

Ese es el camino correcto para que el proyecto sea técnicamente serio, políticamente útil y metodológicamente defendible.

---

## 18. Checklist corto para el LLM ejecutor

Antes de terminar, responder internamente:

- [ ] ¿Existe algún archivo con `phase6_train_test_split.csv`?
- [ ] ¿Existe alguna columna `split` en CSVs finales?
- [ ] ¿Algún README/notebook habla de test externo?
- [ ] ¿Q2/Q5/Q6 siguen usando binarización como análisis principal?
- [ ] ¿Los agregados regulatorios convierten missing en cero sin auditoría?
- [ ] ¿Hay z-scores con MAD=0 usados en modelos?
- [ ] ¿Cada modelo reporta `n_effective`?
- [ ] ¿Fase 7 está etiquetada como robustez y no validación externa?
- [ ] ¿Fase 8 evita causalidad fuerte?
- [ ] ¿Existe manifest global?
- [ ] ¿Chile aparece en outputs finales o se explica por qué no?

Si alguna respuesta es negativa, el proyecto no está cerrado.

---

**Fin del blueprint maestro.**
