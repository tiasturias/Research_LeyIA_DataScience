# Blueprint de cambios requeridos en Fase 6 v2.1+ — Research_AI_law

**Proyecto:** Research_AI_law — Boletín 16821-19 Ley Marco de IA Chile  
**Documento:** Blueprint operativo para actualizar Fase 6  
**Versión objetivo:** `fase6-v2.1-methodology-correction-plus`  
**Tipo de documento:** Instrucciones ejecutables para un LLM / agente técnico / auditor metodológico  
**Fecha de emisión:** 2026-05-08  
**Estado:** Listo para implementación  
**Nivel de obligatoriedad:** Normativo para la corrección de Fase 6  
**Fase CRISP-DM:** Modeling / estimación inferencial  
**Dependencia obligatoria:** Fase 5 v2.1 cerrada y bundle `phase6_ready` sin `split`

---

## 0. Instrucción principal para el LLM ejecutor

Debes actualizar la **Fase 6** del proyecto `Research_AI_law` para que deje de funcionar como una fase de performance predictiva con semántica heredada de `train/test` y se convierta en una fase de **estimación inferencial-comparativa de asociaciones ajustadas por outcome**, con validación interna honesta, incertidumbre explícita, outputs auditables y lenguaje técnicamente defendible.

La Fase 6 corregida **no debe entrenar en un subconjunto y evaluar en un test set ficticio**. Debe:

1. validar que Fase 5 v2.1 entregó un bundle inferencial correcto;
2. fallar si encuentra cualquier archivo, columna o narrativa de `split`, `train`, `test` u `holdout` como frontera metodológica;
3. usar todos los países disponibles por outcome dentro de la muestra preregistrada de 43 países;
4. construir una muestra analítica específica por cada outcome mediante `dropna()` solo sobre `Y + X` requeridas;
5. reportar siempre `n_effective`, `n_missing_outcome`, `n_missing_predictors`, `analysis_scope` y `validation_scope`;
6. estimar asociaciones ajustadas con modelos parsimoniosos, interpretables y compatibles con N pequeño;
7. usar bootstrap, preferentemente BCa cuando sea técnicamente posible, para intervalos de confianza de coeficientes y estimandos principales;
8. usar validación cruzada repetida únicamente como diagnóstico interno, no como validación externa;
9. eliminar LOOCV para AUC y R² cuando esas métricas no están definidas con folds unitarios;
10. reetiquetar todos los archivos tipo `*_predictions_per_country.csv` como **scores descriptivos in-sample** o **posicionamiento relativo**, no predicciones independientes;
11. fortalecer Q2/Q5/Q6 para que los outcomes porcentuales o scores continuos sean tratados como continuos/fraccionales en el análisis principal, dejando la dicotomización por mediana solo como sensibilidad;
12. producir resultados listos para Fase 7 y Fase 8, con semántica honesta y trazabilidad completa.

El objetivo no es demostrar que el modelo “predice Chile”. El objetivo es responder, con rigor, si ciertos rasgos regulatorios están asociados con inversión, adopción, innovación o capacidad pública en IA, cuánto mide esa asociación, cuánta incertidumbre tiene, qué tan estable es y qué puede decirse honestamente para la discusión legislativa.

---

## 1. Tesis metodológica obligatoria

La Fase 6 debe partir de esta premisa:

> Research_AI_law es un estudio observacional comparativo de asociaciones ajustadas, no un producto de predicción externa.

Por tanto, la Fase 6 debe reportar:

- coeficientes o estimandos interpretables;
- intervalos de confianza, idealmente IC95 bootstrap BCa;
- p-values o FDR cuando corresponda;
- dirección y magnitud de asociación;
- `n_effective` por outcome;
- métricas internas auxiliares, no headline;
- sensibilidad y robustez delegadas o preparadas para Fase 7;
- límites explícitos de causalidad y generalización.

La Fase 6 no debe reportar:

- `test set` independiente;
- `train/test split`;
- validación externa;
- predicciones independientes por país;
- causalidad fuerte;
- “impacto causal” de la regulación;
- rankings normativos sin incertidumbre;
- conclusiones legislativas sin advertir N pequeño y diseño observacional.

---

## 2. Diferencia entre Fase 6 v2.1 original y Fase 6 v2.1+ correcta

El blueprint original de Fase 6 v2.1 corrige correctamente el problema del `split`, elimina deuda de holdout, cambia la semántica de outputs y crea tests de no-holdout. Sin embargo, la investigación metodológica posterior identificó una mejora adicional necesaria: **Q2/Q5/Q6 no deben depender como análisis principal de binarizaciones alta/baja por mediana cuando los outcomes reales son porcentajes o scores continuos**.

La versión `fase6-v2.1-methodology-correction-plus` mantiene todo lo correcto de Fase 6 v2.1, pero agrega tres fortalecimientos:

| Área | Fase 6 v2.1 base | Fase 6 v2.1+ correcta |
|---|---|---|
| Contrato no-holdout | Elimina split y test externo | Igual, pero falla con mayor severidad ante residuos de split |
| Q2/Q5/Q6 | Tolera modelos logísticos alta/baja | Usa outcomes continuos/fraccionales como análisis principal; binario queda como sensibilidad |
| Bootstrap | Menciona bootstrap 2000 | Estándar explícito: BCa preferente; percentil solo fallback documentado |
| LOOCV | Corrige AUC/R² inválidos | Igual, y exige tests automáticos por métrica |
| Outputs por país | Scores descriptivos in-sample | Igual, pero agrega nomenclatura recomendada `*_scores_per_country.csv` |
| Reporte | Corrige lenguaje | Agrega diccionario obligatorio de lenguaje permitido/prohibido por archivo |

---

## 3. Fuentes locales y artefactos que gobiernan esta implementación

El LLM ejecutor debe tratar estos insumos como corpus normativo:

```text
CONTEXTOS/5.PLAN_FASE_MVP_END_TO_END.md
CONTEXTOS/6.PLAN_FASE5_V2.1_UPDATE.md
CONTEXTOS/8.FASE6_V2.1_UPDATE.md
CONTEXTOS/new_met.md
CONTEXTOS/reestructuracion-final.md
FASE5/outputs/MVP_AUDITABLE.xlsx
FASE5/outputs/phase6_ready/
```

Si algún archivo no existe en esa ruta exacta, buscarlo por nombre dentro del repositorio, pero no cambiar el alcance metodológico.

El orden jerárquico de decisión es:

1. `reestructuracion-final.md` — decisión metodológica superior;
2. este blueprint — instrucciones ejecutables de Fase 6 v2.1+;
3. `8.FASE6_V2.1_UPDATE.md` — base operativa original;
4. `6.PLAN_FASE5_V2.1_UPDATE.md` — contrato que Fase 6 debe consumir;
5. `5.PLAN_FASE_MVP_END_TO_END.md` — arquitectura global F5-F8;
6. `new_met.md` — memo ejecutivo de cambio de paradigma.

Si hay contradicción entre una lógica predictiva vieja y este blueprint, prevalece este blueprint.

---

## 4. Precondiciones obligatorias antes de tocar Fase 6

No comenzar Fase 6 si Fase 5 v2.1 no está cerrada. La Fase 6 correcta depende de un contrato limpio.

Ejecutar desde la raíz del MVP:

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP

python3 - <<'PY'
from pathlib import Path
import pandas as pd
import yaml

bundle = Path('FASE5/outputs/phase6_ready')
assert bundle.exists(), 'No existe FASE5/outputs/phase6_ready'

required = [
    'phase6_feature_matrix.csv',
    'phase6_modeling_contract.yaml',
    'phase6_analysis_sample_membership.csv',
    'phase6_schema.csv',
    'phase6_variables_catalog.csv',
    'phase6_column_groups.yaml',
]
for fname in required:
    assert (bundle / fname).exists(), f'Falta {fname}'

for forbidden in [
    'phase6_train_test_split.csv',
    'mvp_train_test_split.csv',
]:
    assert not (bundle / forbidden).exists(), f'Archivo prohibido presente: {forbidden}'

fm = pd.read_csv(bundle / 'phase6_feature_matrix.csv')
assert fm.shape[0] == 43, f'feature_matrix debe tener 43 filas, tiene {fm.shape[0]}'
assert 'iso3' in fm.columns, 'Falta iso3'
assert 'CHL' in set(fm['iso3']), 'Chile debe estar en la muestra'
assert 'split' not in fm.columns, 'La matriz no debe tener columna split'
assert not any(c.lower() in {'train','test','holdout'} for c in fm.columns), 'Columnas train/test/holdout prohibidas'

membership = pd.read_csv(bundle / 'phase6_analysis_sample_membership.csv')
assert len(membership) == 43, 'membership debe tener 43 filas'
assert membership['iso3'].nunique() == 43, 'membership debe tener 43 ISO3 únicos'
assert membership['is_primary_analysis_sample'].fillna(False).all(), 'Todos deben ser primary sample'
assert 'split' not in membership.columns, 'membership no debe tener split'
assert not any(c.lower() in {'train','test','holdout'} for c in membership.columns), 'membership no debe tener train/test/holdout'

contract = yaml.safe_load((bundle / 'phase6_modeling_contract.yaml').read_text())
assert contract['methodology'] == 'inferential_comparative_observational'
assert contract['primary_estimand'] == 'adjusted_association'
assert contract['sample_policy']['use_holdout_test_set'] is False
assert contract['sample_policy']['train_test_split_created'] is False
assert contract['sample_policy']['split_column_present'] is False
assert contract['sample_policy']['primary_analysis_scope'] in [
    'full_preregistered_sample_available_by_outcome',
    'full_preregistered_sample',
]
assert 'Q5' in contract.get('questions', {}) or 'Y_Q5_population_usage' in str(contract)
assert 'Q6' in contract.get('questions', {}) or 'Y_Q6_public_sector' in str(contract)

print('PASS: Fase 5 v2.1 está lista para Fase 6 v2.1+')
PY
```

Si este pre-flight falla, detenerse. No implementar hacks en Fase 6 para compensar un bundle incorrecto de Fase 5. La corrección debe hacerse primero en Fase 5.

---

## 5. Diagnóstico de deuda técnica en Fase 6 que debe corregirse

Buscar residuos antes de modificar:

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP/FASE6

rg -n "get_train_test_split|phase6_train_test_split|mvp_train_test_split|test_split_integrity|\\bsplit\\b|TRAIN|TEST|holdout|test set independiente|external validation|predicción independiente|efecto causal|impacto causal" .
```

Residuos esperables en la versión antigua:

```text
src/_common_data.py
  - get_train_test_split()
  - lectura de phase6_train_test_split.csv

src/q1_investment.py
  - import get_train_test_split

tests/test_split_integrity.py
  - espera 34 train / 9 test / CHL in train

config/fase6_decisions.yaml
  - F6-H acepta train/test split

notebooks/generate_notebook.py
  - carga phase6_train_test_split.csv
  - muestra países TRAIN y TEST
  - afirma que los 9 TEST servirán para generalización

README.md
  - usa lenguaje predictivo sin aclarar que son scores in-sample

outputs/
  - q2_predictions_per_country.csv
  - q5_predictions_per_country.csv
  - q6_predictions_per_country.csv
  - fase6_manifest.json puede declarar metodología antigua o holdout
```

La Fase 6 v2.1+ debe eliminar estos residuos en código activo, tests, notebook, README, outputs y manifiestos.

---

## 6. Alcance de cambios

### 6.1 Lo que SÍ cambia

| Componente | Cambio obligatorio |
|---|---|
| `config/fase6_decisions.yaml` | Reescribir decisiones metodológicas v2.1+ sin holdout y con outcome continuo/fraccional para Q2/Q5/Q6 |
| `src/_common_data.py` | Eliminar `get_train_test_split()`, agregar `get_analysis_sample_membership()` y `validate_inferential_contract()` |
| `src/_common_regression.py` | Bootstrap BCa preferente, repeated K-fold como diagnóstico, no LOOCV R² |
| `src/_common_classification.py` | No LOOCV AUC; clasificación solo sensibilidad cuando outcome continuo/fraccional exista |
| `src/_common_fractional.py` | Crear módulo para outcomes fraccionales/porcentuales, si no existe |
| `src/_common_bootstrap.py` | Crear módulo central de bootstrap/IC si no existe |
| `src/q1_investment.py` | Usar muestra completa por outcome, reportar IC, `n_effective`, no split |
| `src/q2_adoption.py` | Cambiar análisis principal a continuo/fraccional; binario solo sensibilidad |
| `src/q3_innovation.py` | Mantener regresión parsimoniosa con IC bootstrap y validación interna |
| `src/q4_clustering.py` | Tratar clustering como descriptivo/no supervisado; sin holdout |
| `src/q5_population_usage.py` | Cambiar análisis principal a continuo/fraccional; binario solo sensibilidad |
| `src/q6_public_sector.py` | Cambiar análisis principal a continuo/score; binario solo sensibilidad |
| `src/run_all.py` | Validar contrato al inicio y fallar ante split |
| `src/api.py` | Documentar outputs como asociaciones/scores descriptivos |
| `tests/` | Eliminar test de split y crear tests anti-holdout, contrato, outcomes y semántica |
| `notebooks/generate_notebook.py` | Regenerar narrativa: contrato inferencial primero |
| `README.md` | Reescribir lenguaje, limitaciones y descripción de outputs |
| `outputs/` | Regenerar resultados con columnas de alcance y semántica correcta |
| `fase6_manifest.json` | Declarar metodología, no-holdout, scopes, checks y hashes |

### 6.2 Lo que NO cambia

- No modificar Fase 3.
- No modificar Fase 4.
- No modificar outputs de Fase 5.
- No cambiar la lista de 43 países.
- No cambiar la lista de 46 variables observadas.
- No agregar PCA como requisito.
- No introducir GridSearch extenso.
- No introducir deep learning.
- No introducir modelos de lenguaje ni NLP en Fase 6.
- No eliminar outliers como decisión primaria.
- No convertir PSM en prueba causal.
- No vender CV o bootstrap como validación externa.

### 6.3 Cambios prohibidos

El LLM ejecutor tiene prohibido:

```text
- Crear un nuevo train/test split.
- Leer phase6_train_test_split.csv.
- Crear phase6_train_test_split.csv.
- Usar fm[fm['split'] == 'train'].
- Usar fm[fm['split'] == 'test'].
- Reportar métricas sobre test.
- Llamar external validation a cualquier remuestreo interno.
- Llamar independent prediction a scores de países usados en estimación.
- Presentar p_high_* como probabilidad predictiva independiente.
- Usar LOOCV para AUC o R².
- Usar outcome binario por mediana como headline cuando existe outcome continuo/fraccional.
- Eliminar países influyentes en el análisis principal.
- Interpretar asociaciones como causalidad.
```

---

## 7. Arquitectura correcta de Fase 6 v2.1+

La Fase 6 debe tener esta estructura mínima:

```text
FASE6/
├── README.md
├── config/
│   ├── fase6_decisions.yaml
│   └── phase6_analysis_plan.yaml                 # NUEVO recomendado
├── src/
│   ├── __init__.py
│   ├── _common_data.py
│   ├── _common_design.py                         # NUEVO recomendado
│   ├── _common_bootstrap.py                      # NUEVO recomendado
│   ├── _common_regression.py
│   ├── _common_fractional.py                     # NUEVO recomendado
│   ├── _common_classification.py
│   ├── _common_outputs.py                        # NUEVO recomendado
│   ├── q1_investment.py
│   ├── q2_adoption.py
│   ├── q3_innovation.py
│   ├── q4_clustering.py
│   ├── q5_population_usage.py
│   ├── q6_public_sector.py
│   ├── run_all.py
│   └── api.py
├── tests/
│   ├── test_no_holdout_methodology.py            # NUEVO obligatorio
│   ├── test_membership_contract.py               # NUEVO obligatorio
│   ├── test_analysis_scope_outputs.py            # NUEVO recomendado
│   ├── test_q2_q5_q6_primary_not_binary.py       # NUEVO obligatorio en v2.1+
│   ├── test_no_invalid_loocv_metrics.py          # NUEVO obligatorio
│   ├── test_scores_semantics.py                  # NUEVO obligatorio
│   ├── test_outputs_no_causal_language.py
│   ├── test_bundle_integrity.py
│   ├── test_q1_investment.py
│   ├── test_q2_adoption.py
│   ├── test_q3_innovation.py
│   ├── test_q4_clustering.py
│   ├── test_q5_population_usage.py
│   └── test_q6_public_sector.py
├── notebooks/
│   ├── generate_notebook.py
│   └── 06_modeling.ipynb                         # regenerado
└── outputs/
    ├── q1_results.csv
    ├── q2_results.csv
    ├── q2_scores_per_country.csv                 # recomendado
    ├── q2_predictions_per_country.csv            # opcional por compatibilidad, con metadata correcta
    ├── q3_results.csv
    ├── q4_clusters.csv
    ├── q4_cluster_profiles.csv
    ├── q5_results.csv
    ├── q5_scores_per_country.csv                 # recomendado
    ├── q6_results.csv
    ├── q6_scores_per_country.csv                 # recomendado
    ├── phase6_model_specs.csv                    # NUEVO recomendado
    ├── phase6_effective_n_by_outcome.csv         # NUEVO obligatorio
    ├── phase6_quality_checks.csv                 # NUEVO recomendado
    ├── phase6_language_audit.csv                 # NUEVO recomendado
    └── fase6_manifest.json
```

---

## 8. Plan analítico por outcome

Crear `config/phase6_analysis_plan.yaml` para preregistrar cómo se modela cada pregunta. Este archivo impide que el LLM improvise modelos inconsistentes.

```yaml
version: "2.1+"
methodology_version: "mvp-v0.2-methodology-correction-plus"
methodology: "inferential_comparative_observational"
primary_estimand: "adjusted_association"
primary_sample_policy: "full_preregistered_sample_available_by_outcome"
no_holdout: true
external_validation_available: false

common_policies:
  missingness: "listwise_deletion_per_model_on_required_y_x"
  no_imputation: true
  outliers: "preserve_in_primary_analysis"
  uncertainty_primary: "bootstrap_bca_ci95_when_feasible"
  bootstrap_resamples: 2000
  bootstrap_fallback: "percentile_ci95_with_reason_logged"
  internal_validation: "repeated_kfold_adaptive"
  loocv_policy: "not_for_auc_or_r2"
  multiple_testing: "benjamini_hochberg_fdr_when_multiple_outcomes_same_family"
  language: "association_not_causation"

model_complexity:
  max_predictors_primary_default: 4
  minimum_n_per_predictor_soft: 8
  if_n_effective_lt_25: "use_minimal_adjusted_model"
  if_n_effective_lt_18: "descriptive_or_exploratory_only"

predictor_sets:
  regulatory_core:
    - n_binding
    - n_non_binding
    - iapp_ley_ia_vigente
    - iapp_categoria_obligatoriedad
  controls_minimal:
    - wb_gdp_per_capita_ppp_log
    - wb_internet_penetration
  controls_institutional:
    - wb_government_effectiveness
    - wb_rule_of_law
  controls_extended:
    - wb_gdp_per_capita_ppp_log
    - wb_internet_penetration
    - wb_rd_expenditure_pct_gdp
    - wb_government_effectiveness

questions:
  Q1_investment:
    primary_outcomes:
      - oxford_ind_company_investment_emerging_tech
      - oxford_ind_ai_unicorns_log
      - oxford_ind_vc_availability
      - wipo_c_vencapdeal_score
    primary_model_family: "linear_regression_parsimonious"
    primary_output: "adjusted_coefficients_ci95"
    sensitivity_models:
      - ridge_repeated_kfold_internal
      - robust_regression_if_influential_points

  Q2_adoption:
    primary_outcomes:
      - ms_h2_2025_ai_diffusion_pct
      - oecd_5_ict_business_oecd_biz_ai_pct
      - anthropic_usage_pct
      - oxford_public_sector_adoption
      - oxford_ind_adoption_emerging_tech
    primary_model_family: "fractional_or_linear_by_scale"
    primary_output: "adjusted_association_continuous_or_fractional"
    binary_median_model: "sensitivity_only"
    scores_per_country: "descriptive_in_sample_positioning"

  Q3_innovation:
    primary_outcomes:
      - oxford_total_score
      - wipo_out_score
      - stanford_fig_6_3_5_volume_of_publications
      - stanford_fig_6_3_4_ai_patent_count
    primary_model_family: "linear_or_log_linear_by_distribution"
    primary_output: "adjusted_coefficients_ci95"
    sensitivity_models:
      - ridge_repeated_kfold_internal
      - spearman_partial_descriptive

  Q4_content_clustering:
    primary_outcomes: []
    primary_model_family: "unsupervised_descriptive_clustering"
    distance_policy: "jaccard_or_gower_by_variable_type"
    validation_policy: "silhouette_internal_not_external_test"
    output_semantics: "typology_not_prediction"

  Q5_population_usage:
    primary_outcomes:
      - anthropic_usage_pct
      - anthropic_collaboration_pct
      - oxford_ind_adoption_emerging_tech
    primary_model_family: "fractional_or_linear_by_scale"
    primary_output: "adjusted_association_continuous_or_fractional"
    binary_median_model: "sensitivity_only"
    scores_per_country: "descriptive_in_sample_positioning"

  Q6_public_sector:
    primary_outcomes:
      - oxford_public_sector_adoption
      - oxford_e_government_delivery
      - oxford_government_digital_policy
      - oxford_ind_data_governance
      - oxford_governance_ethics
      - oecd_2_indigo_oecd_indigo_score
    auxiliary_outcomes:
      - oecd_4_digital_gov_oecd_digital_gov_overall
    primary_model_family: "linear_score_model_or_fractional_if_rescaled"
    primary_output: "adjusted_association_continuous_score"
    binary_median_model: "sensitivity_only"
    scores_per_country: "descriptive_in_sample_positioning"
```

Regla: si una variable listada no existe en `phase6_feature_matrix.csv`, no inventarla. Registrar en `phase6_quality_checks.csv` como `missing_variable_in_bundle` y continuar con outcomes disponibles.

---

## 9. Selección correcta de modelo según tipo de outcome

### 9.1 Clasificación de outcomes

Fase 6 debe clasificar cada outcome antes de modelar:

| Tipo de outcome | Ejemplos | Modelo primario recomendado | Modelo secundario |
|---|---|---|---|
| Score 0-100 continuo | Oxford, WIPO, adopción pública | OLS parsimonioso con IC bootstrap | Ridge CV interna |
| Porcentaje 0-100 | Microsoft, Anthropic, OECD adoption | Fraccional si se reescala a 0-1; OLS robusto si distribución lo justifica | Binario por mediana solo sensibilidad |
| Conteo sesgado | patentes, publicaciones | Log1p + OLS o Poisson/NegBin solo si N y distribución lo permiten | Spearman parcial descriptivo |
| Binario real | ley vigente, tratado sí/no | Logística solo si es predictor/tratamiento, no outcome principal salvo pregunta específica | Fisher/descriptivo si eventos escasos |
| Categórico regulatorio | obligatoriedad/gobernanza | One-hot o contrastes preregistrados | Agrupación descriptiva |
| Clustering | perfiles regulatorios | HCA/KMeans/Gower/Jaccard descriptivo | Silhouette interno |

### 9.2 Regla para Q2/Q5/Q6

Q2, Q5 y Q6 deben seguir esta regla:

```text
Si el outcome original es porcentaje o score continuo, el análisis principal debe conservar la escala continua/fraccional. La binarización alta/baja por mediana solo puede usarse como sensibilidad o visualización secundaria, nunca como headline.
```

Esto implica:

- `q2_results.csv` debe contener filas de modelos primarios continuos/fraccionales.
- `q5_results.csv` debe contener filas de modelos primarios continuos/fraccionales.
- `q6_results.csv` debe contener filas de modelos primarios continuos/score.
- Las filas logísticas binarias deben incluir `analysis_role = "sensitivity_binary_median"`.
- Ningún README o notebook debe decir que la probabilidad alta/baja es el resultado principal si existe outcome continuo.

---

## 10. Construcción de muestra analítica por modelo

Crear un módulo `src/_common_design.py`.

```python
from dataclasses import dataclass
import pandas as pd

@dataclass(frozen=True)
class ModelDesign:
    question: str
    outcome: str
    predictors: list[str]
    controls: list[str]
    model_family: str
    analysis_role: str = "primary"
    scale: str | None = None


def build_model_frame(
    fm: pd.DataFrame,
    design: ModelDesign,
    min_n: int = 15,
) -> tuple[pd.DataFrame, dict]:
    """Construye la muestra efectiva por outcome sin imputación y sin split."""
    if "split" in fm.columns:
        raise RuntimeError("Fase 6 no acepta columna split.")

    required = ["iso3", design.outcome] + list(design.predictors) + list(design.controls)
    missing_cols = [c for c in required if c not in fm.columns]
    if missing_cols:
        return pd.DataFrame(), {
            "question": design.question,
            "outcome": design.outcome,
            "status": "missing_required_columns",
            "missing_columns": ";".join(missing_cols),
            "n_effective": 0,
        }

    raw = fm[required].copy()
    n_primary = len(raw)
    n_missing_outcome = raw[design.outcome].isna().sum()
    n_missing_predictors = raw[design.predictors + design.controls].isna().any(axis=1).sum()

    sub = raw.dropna(subset=[design.outcome] + design.predictors + design.controls).copy()
    n_effective = len(sub)

    meta = {
        "question": design.question,
        "outcome": design.outcome,
        "model_family": design.model_family,
        "analysis_role": design.analysis_role,
        "n_primary_sample": n_primary,
        "n_effective": n_effective,
        "n_missing_outcome": int(n_missing_outcome),
        "n_missing_predictors": int(n_missing_predictors),
        "missingness_policy": "listwise_deletion_on_required_y_x_no_imputation",
        "analysis_scope": "full_preregistered_sample_available_by_outcome",
        "validation_scope": "internal_resampling_not_external_test",
        "holdout_used": False,
        "status": "ok" if n_effective >= min_n else "low_n_exploratory_only",
    }
    return sub, meta
```

Reglas:

- `dropna()` solo puede operar sobre columnas requeridas para ese modelo.
- Nunca eliminar países por pertenecer a un supuesto test.
- Si `n_effective < 15`, el modelo no debe reportarse como confirmatorio; marcar `low_n_exploratory_only`.
- Si `n_effective < 10`, preferir descriptivos y no ajustar multivariado.

---

## 11. Política de predictores y parsimonia

Con N=43 y menor N efectivo por outcome, la Fase 6 debe evitar modelos saturados. Usar sets jerárquicos:

### 11.1 Modelos primarios

Modelo primario recomendado por outcome:

```text
Y ~ regulatory_core + controls_minimal
```

Donde:

```text
regulatory_core = uno o dos predictores regulatorios preregistrados, no todos a la vez.
controls_minimal = log GDP per capita + internet penetration o equivalente disponible.
```

No usar simultáneamente demasiadas variantes regulatorias altamente correlacionadas.

### 11.2 Modelos ajustados extendidos

Modelo extendido, si `n_effective` lo permite:

```text
Y ~ regulatory_core + controls_minimal + institutional_control
```

Solo si:

```text
n_effective >= 8 * número_de_parámetros_estimados
```

Si no se cumple, marcar como exploratorio.

### 11.3 Modelos penalizados

Ridge/Lasso se permiten como diagnóstico interno, no como fuente principal de interpretación legislativa. Deben reportar:

```text
model_family = ridge_internal_cv / lasso_internal_cv
analysis_role = sensitivity_or_diagnostic
validation_scope = internal_resampling_not_external_test
holdout_used = false
```

---

## 12. Bootstrap e intervalos de confianza

Crear `src/_common_bootstrap.py`.

### 12.1 Política general

- Usar `n_resamples = 2000` por defecto.
- Usar BCa cuando la implementación sea estable.
- Si BCa falla por degeneración, usar percentil como fallback y registrar motivo.
- Bootstrap debe remuestrear países, no filas generadas artificialmente.
- Cada remuestreo debe re-ajustar el modelo completo.
- No usar bootstrap como validación externa.

### 12.2 Estructura recomendada

```python
import numpy as np
import pandas as pd


def bootstrap_coefficients(
    fit_func,
    data: pd.DataFrame,
    term_names: list[str],
    n_resamples: int = 2000,
    random_state: int = 20260508,
    ci_method: str = "bca_preferred_percentile_fallback",
) -> pd.DataFrame:
    """Bootstrap de coeficientes por remuestreo de países.

    fit_func debe recibir un DataFrame y devolver un dict term -> coef.
    """
    rng = np.random.default_rng(random_state)
    estimates = []
    n = len(data)
    for _ in range(n_resamples):
        idx = rng.integers(0, n, size=n)
        sample = data.iloc[idx].copy()
        try:
            est = fit_func(sample)
            estimates.append(est)
        except Exception:
            continue

    boot = pd.DataFrame(estimates)
    rows = []
    for term in term_names:
        vals = boot[term].dropna() if term in boot else pd.Series(dtype=float)
        if len(vals) < max(100, n_resamples * 0.25):
            rows.append({
                "term": term,
                "ci_low": np.nan,
                "ci_high": np.nan,
                "bootstrap_success_rate": len(vals) / n_resamples,
                "ci_method": "not_estimable_low_bootstrap_success",
            })
            continue
        rows.append({
            "term": term,
            "ci_low": float(np.percentile(vals, 2.5)),
            "ci_high": float(np.percentile(vals, 97.5)),
            "bootstrap_success_rate": len(vals) / n_resamples,
            "ci_method": "percentile_fallback_or_bca_if_available",
        })
    return pd.DataFrame(rows)
```

Nota: si se usa `scipy.stats.bootstrap(method="BCa")`, documentar en output `ci_method = "bca"`. Si se usa percentil por fallback, documentarlo explícitamente; no ocultarlo.

---

## 13. Modelos comunes

### 13.1 Regresión lineal parsimoniosa

Crear o actualizar `src/_common_regression.py`.

```python
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import RepeatedKFold, cross_val_score
from sklearn.linear_model import RidgeCV


def fit_ols_adjusted(sub, outcome: str, predictors: list[str]) -> dict:
    X = sm.add_constant(sub[predictors], has_constant="add")
    y = sub[outcome]
    model = sm.OLS(y, X).fit(cov_type="HC3")
    rows = []
    for term in model.params.index:
        rows.append({
            "term": term,
            "estimate": float(model.params[term]),
            "std_error_hc3": float(model.bse[term]),
            "p_value": float(model.pvalues[term]),
            "r2_in_sample": float(model.rsquared),
            "adj_r2_in_sample": float(model.rsquared_adj),
        })
    return {"model": model, "rows": rows}


def repeated_kfold_regression_diagnostic(X, y, estimator=None, n_splits=5, n_repeats=20):
    n = len(y)
    if n < 12:
        return {"cv_r2_mean": np.nan, "cv_rmse_mean": np.nan, "cv_note": "not_computed_low_n"}
    k = min(n_splits, max(3, n // 5))
    cv = RepeatedKFold(n_splits=k, n_repeats=n_repeats, random_state=20260508)
    if estimator is None:
        estimator = RidgeCV(alphas=np.logspace(-3, 3, 25))
    r2_scores = cross_val_score(estimator, X, y, cv=cv, scoring="r2")
    neg_mse = cross_val_score(estimator, X, y, cv=cv, scoring="neg_mean_squared_error")
    return {
        "cv_r2_mean": float(np.nanmean(r2_scores)),
        "cv_r2_sd": float(np.nanstd(r2_scores)),
        "cv_rmse_mean": float(np.sqrt(-np.nanmean(neg_mse))),
        "cv_note": "repeated_kfold_internal_not_external_test",
    }


def loocv_r2_policy():
    return {
        "loo_r2": np.nan,
        "loocv_note": "not_computed_r2_undefined_for_single_observation_test_folds",
    }
```

### 13.2 Modelos fraccionales / porcentuales

Crear `src/_common_fractional.py`.

```python
import statsmodels.api as sm


def rescale_percent_to_fraction(y):
    y = y.astype(float)
    if y.max(skipna=True) > 1.0:
        return y / 100.0
    return y


def fit_fractional_logit_or_ols(sub, outcome: str, predictors: list[str]) -> dict:
    """Ajusta GLM binomial fraccional si el outcome está en [0,1]; fallback OLS HC3."""
    y_frac = rescale_percent_to_fraction(sub[outcome])
    X = sm.add_constant(sub[predictors], has_constant="add")

    if y_frac.notna().all() and y_frac.between(0, 1).all() and y_frac.nunique() > 2:
        try:
            glm = sm.GLM(y_frac, X, family=sm.families.Binomial()).fit(cov_type="HC3")
            rows = []
            for term in glm.params.index:
                rows.append({
                    "term": term,
                    "estimate": float(glm.params[term]),
                    "std_error_hc3": float(glm.bse[term]),
                    "p_value": float(glm.pvalues[term]),
                    "model_family": "fractional_logit_quasi_binomial",
                    "outcome_scale_used": "fraction_0_1",
                })
            return {"model": glm, "rows": rows, "fit_status": "ok_fractional_logit"}
        except Exception as e:
            fallback_reason = str(e)[:250]
    else:
        fallback_reason = "outcome_not_fractional_or_not_variable_enough"

    ols = sm.OLS(y_frac, X).fit(cov_type="HC3")
    rows = []
    for term in ols.params.index:
        rows.append({
            "term": term,
            "estimate": float(ols.params[term]),
            "std_error_hc3": float(ols.bse[term]),
            "p_value": float(ols.pvalues[term]),
            "model_family": "ols_on_fraction_or_score_fallback",
            "outcome_scale_used": "fraction_or_original",
            "fallback_reason": fallback_reason,
        })
    return {"model": ols, "rows": rows, "fit_status": "ok_ols_fallback"}
```

### 13.3 Clasificación binaria solo sensibilidad

Actualizar `src/_common_classification.py`.

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score


def fit_binary_median_sensitivity(X, y_binary):
    """Modelo logístico solo para sensibilidad alta/baja, nunca headline."""
    result = {
        "analysis_role": "sensitivity_binary_median",
        "primary_analysis": False,
        "holdout_used": False,
        "validation_scope": "internal_resampling_not_external_test",
    }
    if len(set(y_binary.dropna())) < 2:
        result.update({
            "auc_repeated_kfold": np.nan,
            "auc_note": "not_computed_single_class",
            "loocv_auc": np.nan,
            "loocv_note": "not_computed_auc_undefined_for_single_observation_test_folds",
        })
        return result

    min_class = y_binary.value_counts().min()
    if min_class < 3:
        result.update({
            "auc_repeated_kfold": np.nan,
            "auc_note": "not_computed_too_few_cases_per_class",
            "loocv_auc": np.nan,
            "loocv_note": "not_computed_auc_undefined_for_single_observation_test_folds",
        })
        return result

    k = min(5, int(min_class))
    cv = RepeatedStratifiedKFold(n_splits=k, n_repeats=20, random_state=20260508)
    clf = LogisticRegression(max_iter=2000, solver="liblinear")
    auc = cross_val_score(clf, X, y_binary, scoring="roc_auc", cv=cv)
    result.update({
        "auc_repeated_kfold": float(np.nanmean(auc)),
        "auc_sd": float(np.nanstd(auc)),
        "auc_note": "repeated_stratified_kfold_internal_not_external_test",
        "loocv_auc": np.nan,
        "loocv_note": "not_computed_auc_undefined_for_single_observation_test_folds",
    })
    return result
```

---

## 14. Implementación por módulo Q

## 14.1 Q1 — Inversión

Archivo: `src/q1_investment.py`

### Objetivo

Estimar asociación ajustada entre rasgos regulatorios y outcomes de inversión privada/ecosistema de capital, usando todos los países disponibles por outcome.

### Outcomes candidatos

```text
oxford_ind_company_investment_emerging_tech
oxford_ind_ai_unicorns_log
oxford_ind_vc_availability
wipo_c_vencapdeal_score
```

### Modelo primario

```text
Y_investment ~ predictor_regulatorio + controles_minimales
```

Donde `predictor_regulatorio` puede iterar por separado sobre:

```text
n_binding
n_non_binding
regulatory_intensity
has_binding_law / iapp_ley_ia_vigente
```

No poner todos en el mismo modelo principal si genera multicolinealidad.

### Outputs obligatorios

`q1_results.csv` debe contener:

```text
question
outcome
model_id
model_family
analysis_role
term
estimate
std_error_hc3
ci_low
ci_high
ci_method
p_value
p_value_fdr
n_primary_sample
n_effective
n_missing_outcome
n_missing_predictors
predictors_used
controls_used
r2_in_sample
adj_r2_in_sample
cv_r2_mean
cv_r2_sd
cv_rmse_mean
analysis_scope
validation_scope
holdout_used
external_validation_used
causal_claim
limitations
```

Valores fijos esperados:

```text
analysis_scope = full_preregistered_sample_available_by_outcome
validation_scope = internal_resampling_not_external_test
holdout_used = false
external_validation_used = false
causal_claim = false
```

---

## 14.2 Q2 — Adopción

Archivo: `src/q2_adoption.py`

### Cambio central de v2.1+

Q2 no debe tener como headline una clasificación alta/baja por mediana. Sus outcomes principales son porcentajes o scores de adopción. El análisis principal debe mantener esa escala.

### Outcomes primarios

```text
ms_h2_2025_ai_diffusion_pct
oecd_5_ict_business_oecd_biz_ai_pct
anthropic_usage_pct
oxford_public_sector_adoption
oxford_ind_adoption_emerging_tech
```

### Modelo primario

Si outcome es porcentaje:

```text
fractional_logit_quasi_binomial o OLS sobre fracción 0-1 como fallback documentado
```

Si outcome es score 0-100:

```text
OLS HC3 parsimonioso con bootstrap CI
```

### Modelo de sensibilidad

```text
high_adoption = Y >= median(Y observado)
LogisticRegression solo como sensitivity_binary_median
```

### Outputs obligatorios

`q2_results.csv` debe incluir filas con:

```text
analysis_role = primary_continuous_or_fractional
```

Las filas binarias deben estar claramente marcadas:

```text
analysis_role = sensitivity_binary_median
primary_analysis = false
```

### Scores por país

Crear preferentemente:

```text
outputs/q2_scores_per_country.csv
```

Si se conserva por compatibilidad:

```text
outputs/q2_predictions_per_country.csv
```

Debe incluir:

```text
iso3
country_name_canonical
question
outcome
score_name
score_value
score_scope = in_sample_descriptive_positioning
independent_prediction = false
holdout_used = false
analysis_scope = full_preregistered_sample_available_by_outcome
score_interpretation
model_id
```

No usar `prediction_probability` como nombre semántico primario. Si se conserva `p_high_adoption`, agregar `p_high_adoption_semantics = "binary_median_sensitivity_score_not_independent_prediction"`.

---

## 14.3 Q3 — Innovación

Archivo: `src/q3_innovation.py`

### Outcomes primarios

```text
oxford_total_score
wipo_out_score
stanford_fig_6_3_5_volume_of_publications
stanford_fig_6_3_4_ai_patent_count
```

### Reglas de modelado

- Scores 0-100: OLS HC3 + bootstrap.
- Conteos: usar `log1p` si la variable cruda es altamente sesgada y la transformación existe en bundle.
- Ridge/Lasso: diagnóstico interno.
- GBR u otros modelos no lineales: solo exploratorio, no headline.

### Output

`q3_results.csv` con esquema equivalente a Q1.

Si se reporta feature importance de modelos no lineales, marcar:

```text
analysis_role = exploratory_nonparametric_diagnostic
not_primary_inference = true
```

---

## 14.4 Q4 — Clustering de contenido regulatorio

Archivo: `src/q4_clustering.py`

### Naturaleza correcta

Q4 no es un modelo supervisado y no tiene test set. Es una tipología descriptiva de perfiles regulatorios.

### Reglas

- No usar train/test.
- No reportar accuracy.
- Usar variables regulatorias/categóricas preregistradas.
- Elegir distancia según tipo de variable: Jaccard para binarias, Gower si hay mixtas, Hamming para categóricas simples.
- Reportar silhouette como métrica interna descriptiva, no validación externa.
- Reportar estabilidad de clusters si se hace bootstrap, pero como sensibilidad.

### Outputs

```text
q4_clusters.csv
q4_cluster_profiles.csv
q4_distance_matrix.csv
q4_cluster_stability.csv  # opcional
```

Columnas mínimas de `q4_clusters.csv`:

```text
iso3
country_name_canonical
cluster_id
cluster_label
cluster_method
distance_metric
analysis_scope = full_preregistered_sample_unsupervised
validation_scope = cluster_internal_silhouette_not_external_test
holdout_used = false
```

---

## 14.5 Q5 — Uso poblacional / uso social

Archivo: `src/q5_population_usage.py`

### Cambio central

Q5 debe tratar `anthropic_usage_pct`, `anthropic_collaboration_pct` y otros porcentajes/scores como outcomes continuos o fraccionales. La clasificación alta/baja por mediana es sensibilidad.

### Outcomes primarios

```text
anthropic_usage_pct
anthropic_collaboration_pct
oxford_ind_adoption_emerging_tech
```

### Modelo primario

```text
fractional_logit_quasi_binomial para porcentajes reescalados a 0-1
OLS HC3 fallback si fractional falla o outcome no es proporción estricta
```

### Output principal

`q5_results.csv` debe tener:

```text
analysis_role = primary_continuous_or_fractional
primary_analysis = true
```

### Scores por país

Crear:

```text
q5_scores_per_country.csv
```

Si se conserva `q5_predictions_per_country.csv`, debe incluir:

```text
score_scope = in_sample_descriptive_positioning
independent_prediction = false
holdout_used = false
```

---

## 14.6 Q6 — Sector público y capacidad estatal IA/digital

Archivo: `src/q6_public_sector.py`

### Cambio central

Q6 debe tratar los scores de capacidad pública como continuos. No convertirlos a high/low como análisis principal.

### Outcomes primarios

```text
oxford_public_sector_adoption
oxford_e_government_delivery
oxford_government_digital_policy
oxford_ind_data_governance
oxford_governance_ethics
oecd_2_indigo_oecd_indigo_score
```

Outcome auxiliar:

```text
oecd_4_digital_gov_oecd_digital_gov_overall
```

### Modelo primario

```text
OLS HC3 parsimonioso + bootstrap IC95
```

Si se reescala un score 0-100 a 0-1 y se usa fraccional, registrar:

```text
outcome_scale_used = fraction_0_1_rescaled_from_score_0_100
```

### Output

`q6_results.csv` con el mismo esquema que Q1/Q3.

`q6_scores_per_country.csv` debe ser posicionamiento descriptivo, no predicción.

---

## 15. Control de multiplicidad

Cuando se estiman múltiples outcomes dentro de una misma familia Q, aplicar FDR Benjamini-Hochberg a los p-values de términos regulatorios.

Crear función en `src/_common_outputs.py` o equivalente:

```python
from statsmodels.stats.multitest import multipletests
import pandas as pd


def add_fdr(results: pd.DataFrame, group_cols=None) -> pd.DataFrame:
    if group_cols is None:
        group_cols = ["question", "term"]
    out = results.copy()
    out["p_value_fdr"] = pd.NA
    for _, idx in out.groupby(group_cols).groups.items():
        p = out.loc[idx, "p_value"]
        mask = p.notna()
        if mask.sum() == 0:
            continue
        _, qvals, _, _ = multipletests(p[mask].astype(float), method="fdr_bh")
        out.loc[p[mask].index, "p_value_fdr"] = qvals
    return out
```

No esconder p-values no significativos. Reportar dirección, magnitud e incertidumbre, no solo significancia.

---

## 16. Semántica obligatoria de outputs

Todos los outputs supervisados deben incluir columnas de semántica:

```text
analysis_scope
validation_scope
holdout_used
external_validation_used
independent_prediction
causal_claim
analysis_role
primary_analysis
```

Valores estándar:

```text
analysis_scope = full_preregistered_sample_available_by_outcome
validation_scope = internal_resampling_not_external_test
holdout_used = false
external_validation_used = false
independent_prediction = false
causal_claim = false
```

Para clustering:

```text
analysis_scope = full_preregistered_sample_unsupervised
validation_scope = cluster_internal_silhouette_not_external_test
```

Para scores por país:

```text
score_scope = in_sample_descriptive_positioning
score_interpretation = relative_position_among_preregistered_sample_not_external_prediction
```

---

## 17. Nombres de archivos recomendados

### 17.1 Mantener compatibilidad

Se permite conservar estos nombres si Fase 8 ya los consume:

```text
q2_predictions_per_country.csv
q5_predictions_per_country.csv
q6_predictions_per_country.csv
```

Pero dentro deben declarar:

```text
independent_prediction = false
score_scope = in_sample_descriptive_positioning
```

### 17.2 Nombres preferidos

Crear además, o migrar en Fase 8:

```text
q2_scores_per_country.csv
q5_scores_per_country.csv
q6_scores_per_country.csv
```

Esto reduce riesgo de que un lector interprete “prediction” como predicción externa.

---

## 18. Actualización de `config/fase6_decisions.yaml`

Reemplazar decisiones antiguas por:

```yaml
version: "2.1+"
methodology_version: "mvp-v0.2-methodology-correction-plus"
fecha: "2026-05-08"

methodological_decisions:
  - id: F6-V2.1P-001
    decision: "Fase 6 no usa train/test split ni holdout externo"
    justificacion: "La hipótesis principal es inferencial/comparativa; Fase 5 v2.1 entrega muestra completa N=43 y membership, no partición predictiva."
    estado: approved

  - id: F6-V2.1P-002
    decision: "Usar muestra completa disponible por outcome"
    justificacion: "Cada modelo aplica listwise deletion solo sobre Y y X requeridas, reportando n_effective."
    estado: approved

  - id: F6-V2.1P-003
    decision: "Q2/Q5/Q6 usan outcomes continuos o fraccionales como análisis principal"
    justificacion: "Dichos outcomes son porcentajes o scores; dicotomizarlos por mediana pierde información y queda solo como sensibilidad."
    estado: approved

  - id: F6-V2.1P-004
    decision: "Bootstrap BCa preferente para IC95"
    justificacion: "La incertidumbre de coeficientes es más relevante que performance out-of-sample en este diseño."
    fallback: "percentile_ci95_logged_if_bca_not_estimable"
    estado: approved

  - id: F6-V2.1P-005
    decision: "No calcular LOOCV para AUC ni R2"
    justificacion: "AUC y R2 no son métricas apropiadas con folds de prueba unitarios."
    estado: approved

  - id: F6-V2.1P-006
    decision: "Scores por país son posicionamiento descriptivo in-sample"
    justificacion: "Los países participan en la estimación primaria; por tanto no son predicciones independientes."
    estado: approved

  - id: F6-V2.1P-007
    decision: "PSM es exploratorio y no causal"
    justificacion: "El diseño observacional cross-section no permite causalidad fuerte sin supuestos adicionales."
    estado: approved

  - id: F6-V2.1P-008
    decision: "Fase 6 debe fallar si encuentra split, holdout o phase6_train_test_split.csv"
    justificacion: "Evita regresión metodológica al paradigma predictivo heredado."
    estado: approved
```

---

## 19. Actualización de `src/_common_data.py`

Eliminar:

```python
def get_train_test_split() -> pd.DataFrame:
    ...
```

Agregar:

```python
from pathlib import Path
import pandas as pd
import yaml

FASE6_ROOT = Path(__file__).resolve().parents[1]
MVP_ROOT = FASE6_ROOT.parents[0]
FASE5_BUNDLE = MVP_ROOT / "FASE5" / "outputs" / "phase6_ready"


def get_analysis_sample_membership() -> pd.DataFrame:
    path = FASE5_BUNDLE / "phase6_analysis_sample_membership.csv"
    if not path.exists():
        raise FileNotFoundError("Falta phase6_analysis_sample_membership.csv. Cerrar Fase 5 v2.1 primero.")
    membership = pd.read_csv(path)
    forbidden = {"split", "train", "test", "holdout"}
    bad = forbidden.intersection(set(c.lower() for c in membership.columns))
    if bad:
        raise RuntimeError(f"Membership contiene columnas prohibidas: {bad}")
    return membership


def load_feature_matrix() -> pd.DataFrame:
    path = FASE5_BUNDLE / "phase6_feature_matrix.csv"
    if not path.exists():
        raise FileNotFoundError("Falta phase6_feature_matrix.csv")
    fm = pd.read_csv(path)
    if "split" in fm.columns:
        raise RuntimeError("Fase 6 v2.1+ no acepta columna split")
    return fm


def load_modeling_contract() -> dict:
    path = FASE5_BUNDLE / "phase6_modeling_contract.yaml"
    if not path.exists():
        raise FileNotFoundError("Falta phase6_modeling_contract.yaml")
    return yaml.safe_load(path.read_text())


def validate_inferential_contract() -> dict:
    if (FASE5_BUNDLE / "phase6_train_test_split.csv").exists():
        raise RuntimeError("Archivo prohibido: phase6_train_test_split.csv")

    fm = load_feature_matrix()
    membership = get_analysis_sample_membership()
    contract = load_modeling_contract()

    assert len(fm) == 43
    assert len(membership) == 43
    assert membership["is_primary_analysis_sample"].fillna(False).all()
    assert contract["methodology"] == "inferential_comparative_observational"
    assert contract["sample_policy"]["use_holdout_test_set"] is False
    assert contract["sample_policy"]["train_test_split_created"] is False
    assert contract["sample_policy"]["split_column_present"] is False

    return {
        "status": "ok",
        "methodology": contract["methodology"],
        "primary_estimand": contract.get("primary_estimand", "adjusted_association"),
        "n_feature_matrix": len(fm),
        "n_membership": len(membership),
        "holdout_used": False,
    }
```

---

## 20. Actualización de `src/run_all.py`

Al inicio del orquestador:

```python
from ._common_data import validate_inferential_contract


def run_all():
    contract_status = validate_inferential_contract()
    print(f"Contrato inferencial validado: {contract_status}")
    # luego ejecutar Q1-Q6
```

El manifiesto final debe incluir:

```json
{
  "fase6_version": "2.1+",
  "methodology_version": "mvp-v0.2-methodology-correction-plus",
  "methodology": "inferential_comparative_observational",
  "primary_estimand": "adjusted_association",
  "analysis_sample_n": 43,
  "holdout_used": false,
  "train_test_split_used": false,
  "external_validation_used": false,
  "q2_q5_q6_primary_scale": "continuous_or_fractional",
  "binary_median_models": "sensitivity_only",
  "loocv_auc_used": false,
  "loocv_r2_used": false,
  "bootstrap_policy": "bca_preferred_percentile_fallback_logged",
  "outputs_semantics": {
    "q2_scores_per_country.csv": "in_sample_descriptive_positioning",
    "q5_scores_per_country.csv": "in_sample_descriptive_positioning",
    "q6_scores_per_country.csv": "in_sample_descriptive_positioning"
  }
}
```

---

## 21. Tests obligatorios

### 21.1 Eliminar test heredado

Eliminar, no skipear:

```bash
rm FASE6/tests/test_split_integrity.py
```

### 21.2 Crear `tests/test_no_holdout_methodology.py`

```python
from pathlib import Path
import pandas as pd
import yaml

FASE6_ROOT = Path(__file__).resolve().parents[1]
MVP_ROOT = FASE6_ROOT.parents[0]
FASE5_BUNDLE = MVP_ROOT / "FASE5" / "outputs" / "phase6_ready"
OUTPUTS = FASE6_ROOT / "outputs"


def test_no_split_artifacts_in_bundle():
    assert not (FASE5_BUNDLE / "phase6_train_test_split.csv").exists()
    fm = pd.read_csv(FASE5_BUNDLE / "phase6_feature_matrix.csv")
    assert "split" not in fm.columns


def test_contract_declares_no_holdout():
    contract = yaml.safe_load((FASE5_BUNDLE / "phase6_modeling_contract.yaml").read_text())
    assert contract["methodology"] == "inferential_comparative_observational"
    assert contract["sample_policy"]["use_holdout_test_set"] is False
    assert contract["sample_policy"]["train_test_split_created"] is False
    assert contract["sample_policy"]["split_column_present"] is False


def test_outputs_do_not_use_holdout():
    for fname in ["q1_results.csv", "q2_results.csv", "q3_results.csv", "q5_results.csv", "q6_results.csv"]:
        path = OUTPUTS / fname
        if not path.exists():
            continue
        df = pd.read_csv(path)
        assert "holdout_used" in df.columns, fname
        assert df["holdout_used"].fillna(False).eq(False).all(), fname
        assert "split" not in df.columns, fname
```

### 21.3 Crear `tests/test_membership_contract.py`

```python
from pathlib import Path
import pandas as pd

FASE6_ROOT = Path(__file__).resolve().parents[1]
MVP_ROOT = FASE6_ROOT.parents[0]
FASE5_BUNDLE = MVP_ROOT / "FASE5" / "outputs" / "phase6_ready"


def test_membership_exists_and_has_43_primary_countries():
    path = FASE5_BUNDLE / "phase6_analysis_sample_membership.csv"
    assert path.exists()
    m = pd.read_csv(path)
    assert len(m) == 43
    assert m["iso3"].nunique() == 43
    assert m["is_primary_analysis_sample"].fillna(False).all()
    forbidden = {"split", "train", "test", "holdout"}
    assert not forbidden.intersection(set(c.lower() for c in m.columns))
```

### 21.4 Crear `tests/test_q2_q5_q6_primary_not_binary.py`

```python
from pathlib import Path
import pandas as pd

FASE6_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE6_ROOT / "outputs"


def _check_primary_not_binary(fname):
    df = pd.read_csv(OUTPUTS / fname)
    assert "analysis_role" in df.columns
    primary = df[df["analysis_role"].astype(str).str.contains("primary", na=False)]
    assert not primary.empty, f"{fname} no tiene análisis primario"
    assert not primary["analysis_role"].astype(str).str.contains("binary_median", na=False).any(), fname
    if "primary_analysis" in df.columns:
        bad = df[(df["primary_analysis"] == True) & (df["analysis_role"].astype(str).str.contains("binary_median", na=False))]
        assert bad.empty, f"{fname} usa binario mediana como primario"


def test_q2_primary_is_continuous_or_fractional():
    _check_primary_not_binary("q2_results.csv")


def test_q5_primary_is_continuous_or_fractional():
    _check_primary_not_binary("q5_results.csv")


def test_q6_primary_is_continuous_or_score():
    _check_primary_not_binary("q6_results.csv")
```

### 21.5 Crear `tests/test_no_invalid_loocv_metrics.py`

```python
from pathlib import Path
import pandas as pd

FASE6_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE6_ROOT / "outputs"


def test_no_loocv_auc_or_r2_as_valid_metric():
    for path in OUTPUTS.glob("q*_results.csv"):
        df = pd.read_csv(path)
        for col in df.columns:
            lc = col.lower()
            if "loocv" in lc and ("auc" in lc or "r2" in lc):
                # Puede existir, pero debe ser NaN y tener nota explicativa.
                assert df[col].isna().all(), f"{path.name}:{col} debe ser NaN"
        note_cols = [c for c in df.columns if "loocv_note" in c.lower()]
        for c in note_cols:
            assert df[c].astype(str).str.contains("undefined|not_computed|not applicable", case=False, na=False).any()
```

### 21.6 Crear `tests/test_scores_semantics.py`

```python
from pathlib import Path
import pandas as pd

FASE6_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE6_ROOT / "outputs"


def test_country_scores_are_descriptive_not_independent_predictions():
    candidates = [
        "q2_scores_per_country.csv",
        "q5_scores_per_country.csv",
        "q6_scores_per_country.csv",
        "q2_predictions_per_country.csv",
        "q5_predictions_per_country.csv",
        "q6_predictions_per_country.csv",
    ]
    existing = [OUTPUTS / f for f in candidates if (OUTPUTS / f).exists()]
    assert existing, "Debe existir al menos un archivo de scores por país"
    for path in existing:
        df = pd.read_csv(path)
        assert "score_scope" in df.columns, path.name
        assert df["score_scope"].eq("in_sample_descriptive_positioning").all(), path.name
        assert "independent_prediction" in df.columns, path.name
        assert df["independent_prediction"].fillna(False).eq(False).all(), path.name
        assert "holdout_used" in df.columns, path.name
        assert df["holdout_used"].fillna(False).eq(False).all(), path.name
```

---

## 22. Auditoría de lenguaje

Crear un chequeo automático de lenguaje en README, notebook generator y outputs textuales.

### 22.1 Lenguaje permitido

```text
asociación ajustada
estimación primaria
muestra preregistrada
muestra efectiva por outcome
validación interna
remuestreo interno
bootstrap
IC95
robustez
sensibilidad
posicionamiento descriptivo
score in-sample
```

### 22.2 Lenguaje prohibido salvo cita histórica explícita

```text
test set independiente
external validation
validación externa
predicción independiente
predigo que Chile
impacto causal
efecto causal
la regulación causa
train/test split
holdout
```

Permitir estos términos solo en una sección llamada `Lenguaje prohibido` o `histórico/deprecado`, nunca en narrativa metodológica activa.

---

## 23. Notebook `06_modeling.ipynb`

El notebook regenerado debe iniciar con una celda Markdown titulada:

```text
Fase 6 v2.1+ — Modelado inferencial sin holdout
```

Debe decir explícitamente:

```text
Este notebook no evalúa un test set independiente. Fase 6 estima asociaciones ajustadas usando todos los países disponibles por outcome dentro de la muestra preregistrada. Las métricas de CV son diagnóstico interno y los scores por país son posicionamiento descriptivo in-sample.
```

Estructura recomendada:

1. Contrato inferencial recibido desde Fase 5.
2. Muestra primaria y membership.
3. Missingness y `n_effective` por outcome.
4. Q1 inversión.
5. Q2 adopción — análisis continuo/fraccional principal.
6. Q3 innovación.
7. Q4 clustering descriptivo.
8. Q5 uso poblacional — análisis continuo/fraccional principal.
9. Q6 sector público — análisis continuo/score principal.
10. Scores por país como posicionamiento descriptivo.
11. Limitaciones y preparación para Fase 7.

No debe tener secciones “Train countries”, “Test countries”, “Generalización con test set”, “predicciones independientes”.

---

## 24. README de Fase 6

El README debe explicar:

```text
Fase 6 estima asociaciones ajustadas por outcome en un estudio observacional comparativo. No usa holdout ni test set independiente. Cada modelo usa todos los países disponibles para el outcome correspondiente, con eliminación por lista solo sobre columnas requeridas. Los outputs por país son scores descriptivos in-sample y no predicciones externas.
```

Debe incluir tabla de outputs:

| Output | Significado correcto | No debe interpretarse como |
|---|---|---|
| `q1_results.csv` | Asociación ajustada con outcomes de inversión | Prueba causal |
| `q2_results.csv` | Asociación continua/fraccional con adopción | Clasificador principal alta/baja |
| `q2_scores_per_country.csv` | Posicionamiento descriptivo in-sample | Predicción independiente |
| `q3_results.csv` | Asociación ajustada con innovación | Causalidad |
| `q4_clusters.csv` | Tipología descriptiva de perfiles | Accuracy predictiva |
| `q5_results.csv` | Asociación continua/fraccional con uso poblacional | Clasificador principal |
| `q6_results.csv` | Asociación continua/score con sector público | Predicción externa |
| `fase6_manifest.json` | Auditoría de ejecución | Resultado estadístico |

---

## 25. Manifest final

`outputs/fase6_manifest.json` debe contener como mínimo:

```json
{
  "fase6_version": "2.1+",
  "created_at": "<ISO8601>",
  "methodology_version": "mvp-v0.2-methodology-correction-plus",
  "methodology": "inferential_comparative_observational",
  "primary_estimand": "adjusted_association",
  "analysis_scope": "full_preregistered_sample_available_by_outcome",
  "validation_scope": "internal_resampling_not_external_test",
  "analysis_sample_n": 43,
  "holdout_used": false,
  "train_test_split_used": false,
  "external_validation_used": false,
  "split_column_present": false,
  "phase6_train_test_split_present": false,
  "q2_q5_q6_primary_model_policy": "continuous_or_fractional_primary_binary_median_sensitivity_only",
  "bootstrap_policy": {
    "n_resamples_default": 2000,
    "ci_method_preferred": "BCa",
    "fallback": "percentile_logged"
  },
  "loocv_policy": {
    "auc_loocv_used": false,
    "r2_loocv_used": false,
    "reason": "undefined_for_single_observation_test_folds"
  },
  "language_policy": {
    "causal_claim": false,
    "independent_prediction_claim": false,
    "external_validation_claim": false
  },
  "outputs": {
    "q1_results.csv": "adjusted_associations",
    "q2_results.csv": "continuous_or_fractional_adjusted_associations",
    "q2_scores_per_country.csv": "in_sample_descriptive_positioning",
    "q3_results.csv": "adjusted_associations",
    "q4_clusters.csv": "descriptive_typology",
    "q5_results.csv": "continuous_or_fractional_adjusted_associations",
    "q5_scores_per_country.csv": "in_sample_descriptive_positioning",
    "q6_results.csv": "continuous_score_adjusted_associations",
    "q6_scores_per_country.csv": "in_sample_descriptive_positioning"
  }
}
```

---

## 26. Criterios de aceptación

La implementación se considera aceptada solo si pasa este checklist:

```text
FASE 6 v2.1+ — CRITERIOS DE ACEPTACIÓN

Pre-flight
[ ] Fase 5 v2.1 cerrada
[ ] phase6_feature_matrix.csv existe
[ ] phase6_analysis_sample_membership.csv existe
[ ] phase6_modeling_contract.yaml existe
[ ] phase6_train_test_split.csv NO existe
[ ] phase6_feature_matrix.csv NO tiene split
[ ] membership NO tiene split/train/test/holdout

Código
[ ] _common_data.py no define get_train_test_split()
[ ] _common_data.py define get_analysis_sample_membership()
[ ] _common_data.py define validate_inferential_contract()
[ ] run_all.py valida contrato antes de ejecutar Q1-Q6
[ ] Q1-Q6 usan full sample by outcome y dropna solo sobre columnas requeridas
[ ] Q2/Q5/Q6 tienen análisis primario continuo/fraccional o score
[ ] Binarios por mediana aparecen solo como sensitivity_binary_median
[ ] _common_classification.py no calcula LOOCV AUC
[ ] _common_regression.py no calcula LOOCV R²
[ ] PSM, si existe, queda como exploratorio

Outputs
[ ] q1_results.csv tiene analysis_scope, validation_scope, holdout_used=false
[ ] q2_results.csv tiene análisis primario no binario
[ ] q3_results.csv tiene analysis_scope, validation_scope, holdout_used=false
[ ] q4_clusters.csv no habla de test externo
[ ] q5_results.csv tiene análisis primario no binario
[ ] q6_results.csv tiene análisis primario no binario
[ ] q2/q5/q6 scores por país tienen score_scope=in_sample_descriptive_positioning
[ ] q2/q5/q6 scores por país tienen independent_prediction=false
[ ] phase6_effective_n_by_outcome.csv existe
[ ] fase6_manifest.json declara methodology=inferential_comparative_observational
[ ] fase6_manifest.json declara train_test_split_used=false
[ ] fase6_manifest.json declara external_validation_used=false

Tests
[ ] tests/test_split_integrity.py eliminado
[ ] test_no_holdout_methodology.py pasa
[ ] test_membership_contract.py pasa
[ ] test_q2_q5_q6_primary_not_binary.py pasa
[ ] test_no_invalid_loocv_metrics.py pasa
[ ] test_scores_semantics.py pasa
[ ] pytest completo pasa

Notebook/README
[ ] Notebook no carga phase6_train_test_split.csv
[ ] Notebook empieza con contrato inferencial
[ ] README no promete test externo
[ ] README describe scores por país como descriptivos/in-sample
[ ] No hay lenguaje causal fuerte
[ ] No hay “predicción independiente”
```

---

## 27. Comandos de verificación final

Ejecutar:

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP/FASE6

# 1. Buscar residuos prohibidos en código activo
rg -n "get_train_test_split|phase6_train_test_split|mvp_train_test_split|test_split_integrity|fm\[.*split|split ==|TRAIN|TEST|test set independiente|external validation|validación externa|predicción independiente|efecto causal|impacto causal" src tests README.md notebooks || true

# 2. Ejecutar Fase 6 completa
python3 -m src.run_all

# 3. Tests
python3 -m pytest tests/ -q

# 4. Validación rápida de outputs
python3 - <<'PY'
from pathlib import Path
import pandas as pd
import json

out = Path('outputs')
for fname in ['q1_results.csv','q2_results.csv','q3_results.csv','q5_results.csv','q6_results.csv']:
    path = out / fname
    assert path.exists(), f'Falta {fname}'
    df = pd.read_csv(path)
    assert 'analysis_scope' in df.columns, fname
    assert 'validation_scope' in df.columns, fname
    assert 'holdout_used' in df.columns, fname
    assert df['holdout_used'].fillna(False).eq(False).all(), fname
    assert 'split' not in df.columns, fname

for fname in ['q2_scores_per_country.csv','q5_scores_per_country.csv','q6_scores_per_country.csv']:
    path = out / fname
    if not path.exists():
        continue
    df = pd.read_csv(path)
    assert df['score_scope'].eq('in_sample_descriptive_positioning').all(), fname
    assert df['independent_prediction'].fillna(False).eq(False).all(), fname
    assert df['holdout_used'].fillna(False).eq(False).all(), fname

manifest = json.loads((out / 'fase6_manifest.json').read_text())
assert manifest['methodology'] == 'inferential_comparative_observational'
assert manifest['holdout_used'] is False
assert manifest['train_test_split_used'] is False
assert manifest['external_validation_used'] is False
print('PASS: Fase 6 v2.1+ outputs coherentes')
PY
```

Si el `rg` encuentra términos prohibidos solo en secciones de “lenguaje prohibido” o “histórico/deprecado”, documentarlo. Si aparecen en narrativa activa, corregir.

---

## 28. Rollback seguro

Si la implementación falla:

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP/FASE6

git status

# Restaurar solo Fase 6, sin tocar Fase 5
git restore config/ src/ tests/ README.md notebooks/generate_notebook.py

# No usar git reset --hard salvo instrucción explícita del investigador.
# No restaurar FASE5/outputs.
```

Si outputs quedaron corruptos:

```bash
rm -rf outputs
python3 -m src.run_all
python3 -m pytest tests/ -q
```

---

## 29. Reporte final esperado del LLM ejecutor

Al terminar, el LLM debe entregar este reporte:

```text
FASE 6 v2.1+ — REPORTE DE EJECUCIÓN

1. Pre-flight Fase 5 v2.1
- phase6_feature_matrix.csv: PASS/FAIL
- phase6_analysis_sample_membership.csv: PASS/FAIL
- phase6_modeling_contract.yaml: PASS/FAIL
- phase6_train_test_split.csv ausente: PASS/FAIL
- columna split ausente: PASS/FAIL

2. Archivos modificados
- config/fase6_decisions.yaml: SÍ/NO
- config/phase6_analysis_plan.yaml: SÍ/NO
- src/_common_data.py: SÍ/NO
- src/_common_design.py: SÍ/NO
- src/_common_bootstrap.py: SÍ/NO
- src/_common_fractional.py: SÍ/NO
- src/_common_regression.py: SÍ/NO
- src/_common_classification.py: SÍ/NO
- src/q1_investment.py: SÍ/NO
- src/q2_adoption.py: SÍ/NO
- src/q3_innovation.py: SÍ/NO
- src/q4_clustering.py: SÍ/NO
- src/q5_population_usage.py: SÍ/NO
- src/q6_public_sector.py: SÍ/NO
- src/run_all.py: SÍ/NO
- src/api.py: SÍ/NO
- README.md: SÍ/NO
- notebooks/generate_notebook.py: SÍ/NO

3. Archivos eliminados
- tests/test_split_integrity.py: SÍ/NO

4. Tests creados
- test_no_holdout_methodology.py: SÍ/NO
- test_membership_contract.py: SÍ/NO
- test_q2_q5_q6_primary_not_binary.py: SÍ/NO
- test_no_invalid_loocv_metrics.py: SÍ/NO
- test_scores_semantics.py: SÍ/NO

5. Resultados regenerados
- q1_results.csv: shape=...
- q2_results.csv: shape=..., primary_continuous_or_fractional=PASS/FAIL
- q2_scores_per_country.csv: shape=..., score_scope OK=PASS/FAIL
- q3_results.csv: shape=...
- q4_clusters.csv: shape=...
- q5_results.csv: shape=..., primary_continuous_or_fractional=PASS/FAIL
- q5_scores_per_country.csv: shape=..., score_scope OK=PASS/FAIL
- q6_results.csv: shape=..., primary_continuous_or_score=PASS/FAIL
- q6_scores_per_country.csv: shape=..., score_scope OK=PASS/FAIL
- phase6_effective_n_by_outcome.csv: SÍ/NO
- fase6_manifest.json: v2.1+ OK=PASS/FAIL

6. Política metodológica confirmada
- methodology: inferential_comparative_observational
- primary_estimand: adjusted_association
- holdout_used: false
- train_test_split_used: false
- external_validation_used: false
- Q2/Q5/Q6 binarización por mediana: sensitivity_only
- LOOCV AUC/R²: not_computed
- causal_claim: false

7. pytest
- Resultado: PASS/FAIL
- Tests ejecutados: ...
- Fallas restantes: ...

8. Limitaciones documentadas
- N pequeño
- Diseño observacional
- No validación externa
- Missingness por outcome
- Scores por país in-sample
```

---

## 30. Filosofía de cierre

La Fase 6 v2.1+ no busca “mejorar el AUC” ni “predecir Chile”. Busca estimar asociaciones ajustadas de manera honesta, con todos los países disponibles por outcome, con incertidumbre explícita y sin vender capacidades que el diseño no tiene.

La respuesta correcta ante un auditor es:

> No existe test set independiente en este MVP. La Fase 6 estima asociaciones ajustadas sobre la muestra preregistrada disponible por outcome. La validación es interna y la robustez se evalúa en Fase 7. Los scores por país son posicionamiento descriptivo in-sample, no predicciones externas.

La respuesta correcta ante una autoridad política es:

> El estudio no afirma causalidad fuerte ni predice el futuro de Chile. Muestra patrones comparados, ajustados por controles, con incertidumbre y sensibilidad, para orientar una discusión legislativa más seria sobre regulación de IA.

Fin del blueprint.
