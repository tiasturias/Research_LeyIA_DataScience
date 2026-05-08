# BLUEPRINT DE IMPLEMENTACIÓN — Fase 7 Robustez y Sensibilidad

**Proyecto:** Research_AI_law — Boletín 16821-19 Ley Marco de IA Chile  
**Documento:** Plan ultra detallado de implementación de Fase 7  
**Versión objetivo:** `fase7-v1.0-robustness-methodology-correction`  
**Dependencia obligatoria:** Fase 6 v2.1+ auditada, completa y aprobada  
**Audiencia:** LLM ejecutor / agente técnico / auditor metodológico  
**Nivel de obligatoriedad:** Normativo para implementar Fase 7 de inicio a fin  
**Fase CRISP-DM:** Evaluation / Robustness / Sensitivity  
**Fecha sugerida:** 2026-05-08  

---

## 0. Instrucción principal para el LLM ejecutor

Debes implementar **Fase 7** solo después de que una auditoría de Fase 6 confirme que Fase 6 v2.1+ está lista y completa para pasar a robustez. No debes corregir Fase 6 dentro de Fase 7, no debes modificar Fase 5, no debes modificar Fase 6 y no debes reinterpretar ningún archivo como `test set`.

La Fase 7 correcta debe funcionar como el **guardián de robustez científica** del proyecto. Su propósito no es mejorar modelos ni producir nuevas conclusiones por oportunismo, sino verificar si las conclusiones de Fase 6 son estables frente a perturbaciones razonables de muestra, especificación y grupos influyentes.

La Fase 7 debe responder:

1. ¿Los hallazgos principales de Fase 6 se mantienen al comparar contra baselines?
2. ¿Las variables regulatorias aportan información incremental frente a controles socioeconómicos?
3. ¿La dirección de las asociaciones cambia al excluir USA, China, líderes IA, regiones o grupos de ingreso?
4. ¿Algún resultado depende excesivamente de outliers o países influyentes?
5. ¿Los resultados Q2/Q5/Q6 siguen siendo coherentes bajo la sensibilidad binaria por mediana, sin convertirla en análisis principal?
6. ¿Los clusters regulatorios de Q4 son estables o frágiles?
7. ¿Qué hallazgos pueden pasar a Fase 8 como reportables, con qué etiqueta de robustez y con qué limitaciones?

**Regla de oro:** Fase 7 no es validación externa. Fase 7 es robustez, sensibilidad y estabilidad de conclusiones.

---

## 1. Contexto metodológico obligatorio

El proyecto `Research_AI_law` quedó redefinido como un:

> **Estudio observacional comparativo de asociaciones ajustadas entre rasgos regulatorios de IA y desarrollo del ecosistema de IA, con robustez interna, sensibilidad y trazabilidad completa.**

Por tanto:

- Fase 5 prepara datos, membresía y contrato.
- Fase 6 estima asociaciones ajustadas por outcome.
- Fase 7 evalúa robustez y sensibilidad.
- Fase 8 traduce hallazgos a lenguaje político-legislativo prudente.

Fase 7 debe heredar sin alterar estas decisiones:

```yaml
methodology: "inferential_comparative_observational"
primary_estimand: "adjusted_association"
holdout_used: false
train_test_split_used: false
external_validation_used: false
causal_claims_allowed: false
```

Fase 7 debe prohibir:

```text
test set independiente
external validation
validación externa
predicción independiente
impacto causal
efecto causal
la regulación causa
train/test split
holdout
```

Estos términos solo pueden aparecer en secciones de lenguaje prohibido, auditoría histórica o tests anti-regresión.

---

## 2. Gate obligatorio de entrada desde Fase 6

Antes de implementar o ejecutar Fase 7, el LLM debe verificar que Fase 6 fue auditada y aprobada.

### 2.1 Estado aceptable de auditoría

Fase 7 solo puede iniciarse si el dictamen de auditoría de Fase 6 es uno de:

```text
APROBADA
APROBADA_CON_OBSERVACIONES
```

Fase 7 **no debe iniciarse** si la auditoría de Fase 6 es:

```text
APROBADA_CONDICIONAL
RECHAZADA
NO_AUDITADA
```

Si no existe informe de auditoría, ejecutar pre-flight técnico mínimo y declarar el estado como `NO_AUDITADA`; luego detenerse.

### 2.2 Archivos de auditoría esperados

Buscar, en este orden:

```text
F5_F8_MVP/FASE6/outputs/FASE6_AUDIT_REPORT.md
F5_F8_MVP/FASE6/outputs/fase6_audit_report.md
F5_F8_MVP/FASE6/AUDITORIA_FASE6.md
F5_F8_MVP/FASE6/outputs/audit_phase6.json
F5_F8_MVP/FASE6/outputs/fase6_audit_verdict.json
```

Si ninguno existe, crear un registro en `FASE7/outputs/fase7_preflight_report.csv` con:

```text
gate_name = fase6_audit_report_present
status = FAIL
severity = P0
action = abort_phase7_until_fase6_audit_exists
```

### 2.3 Pre-flight técnico mínimo aunque exista auditoría

Ejecutar desde la raíz del MVP:

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP

python3 - <<'PY'
from pathlib import Path
import json
import pandas as pd
import yaml

root = Path(".")
f5_bundle = root / "FASE5" / "outputs" / "phase6_ready"
f6_out = root / "FASE6" / "outputs"

required_f6 = [
    "fase6_manifest.json",
    "q1_results.csv",
    "q2_results.csv",
    "q3_results.csv",
    "q4_clusters.csv",
    "q5_results.csv",
    "q6_results.csv",
]
for fname in required_f6:
    assert (f6_out / fname).exists(), f"Falta output Fase 6: {fname}"

manifest = json.loads((f6_out / "fase6_manifest.json").read_text())
assert manifest["methodology"] == "inferential_comparative_observational"
assert manifest["holdout_used"] is False
assert manifest["train_test_split_used"] is False
assert manifest["external_validation_used"] is False

contract = yaml.safe_load((f5_bundle / "phase6_modeling_contract.yaml").read_text())
assert contract["sample_policy"]["use_holdout_test_set"] is False
assert contract["sample_policy"]["train_test_split_created"] is False
assert contract["sample_policy"]["split_column_present"] is False

fm = pd.read_csv(f5_bundle / "phase6_feature_matrix.csv")
assert len(fm) == 43
assert "CHL" in set(fm["iso3"])
assert "split" not in fm.columns

membership = pd.read_csv(f5_bundle / "phase6_analysis_sample_membership.csv")
assert len(membership) == 43
assert membership["iso3"].nunique() == 43
assert membership["is_primary_analysis_sample"].fillna(False).all()

for fname in required_f6[1:]:
    df = pd.read_csv(f6_out / fname)
    if "holdout_used" in df.columns:
        assert df["holdout_used"].fillna(False).eq(False).all(), fname
    assert "split" not in df.columns, fname

print("PASS: Gate técnico Fase 6 -> Fase 7 aprobado")
PY
```

Si falla cualquier assert, abortar Fase 7.

---

## 3. Misión exacta de Fase 7

Fase 7 debe producir una evaluación sistemática de robustez de los resultados de Fase 6.

Debe generar:

1. **Baselines:** comparación de modelos de Fase 6 contra baseline trivial y baseline solo controles.
2. **Sensitivity analysis:** exclusión de países influyentes y grupos de sensibilidad.
3. **Leave-group-out:** exclusión por región, ingreso, líderes IA, LATAM, Europa, etc.
4. **Outlier influence:** influencia de casos extremos sobre dirección y magnitud.
5. **Cluster stability:** estabilidad de Q4.
6. **Binary sensitivity registry:** revisión de sensibilidad binaria Q2/Q5/Q6, sin elevarla a principal.
7. **Stability matrix:** matriz final de estabilidad de conclusiones.
8. **Reporting contract:** contrato hacia Fase 8 con hallazgos reportables y no reportables.

Fase 7 no debe:

- seleccionar nuevos outcomes por conveniencia;
- cambiar la muestra primaria;
- crear un train/test split;
- calcular métricas de test externo;
- convertir sensibilidad en validación externa;
- reetiquetar causalidad;
- sobreescribir outputs de Fase 6;
- borrar resultados frágiles;
- ocultar sign flips;
- “arreglar” modelos para que parezcan más robustos.

---

## 4. Arquitectura objetivo de Fase 7

Crear o normalizar esta estructura:

```text
F5_F8_MVP/FASE7/
├── README.md
├── config/
│   ├── robustness_plan.yaml
│   ├── sensitivity_groups.yaml
│   ├── baseline_specs.yaml
│   ├── stability_thresholds.yaml
│   ├── phase8_reporting_template.yaml
│   └── fase7_decisions.yaml
├── src/
│   ├── __init__.py
│   ├── _common_data.py
│   ├── _common_specs.py
│   ├── baselines.py
│   ├── sensitivity.py
│   ├── leave_group_out.py
│   ├── outliers.py
│   ├── cluster_stability.py
│   ├── binary_sensitivity.py
│   ├── stability.py
│   ├── conclusion_matrix.py
│   ├── phase8_contract.py
│   ├── validate.py
│   ├── api.py
│   └── run_all.py
├── tests/
│   ├── test_fase6_gate.py
│   ├── test_no_external_validation_language.py
│   ├── test_baselines_outputs.py
│   ├── test_sensitivity_outputs.py
│   ├── test_leave_group_out_not_test.py
│   ├── test_outlier_influence_outputs.py
│   ├── test_cluster_stability_outputs.py
│   ├── test_conclusion_stability_matrix.py
│   ├── test_phase8_reporting_contract.py
│   └── test_fase7_manifest.py
├── notebooks/
│   ├── generate_notebook.py
│   └── 07_robustness_sensitivity.ipynb
└── outputs/
    ├── fase7_preflight_report.csv
    ├── baseline_comparisons.csv
    ├── sensitivity_analysis.csv
    ├── leave_group_out_analysis.csv
    ├── outlier_influence.csv
    ├── cluster_stability.csv
    ├── binary_sensitivity_registry.csv
    ├── robustness_registry.csv
    ├── conclusion_stability_matrix.csv
    ├── phase8_reporting_contract.yaml
    ├── fase7_quality_checks.csv
    └── fase7_manifest.json
```

---

## 5. Inputs canónicos de Fase 7

Fase 7 debe leer, no modificar, estos archivos:

### 5.1 Desde Fase 5

```text
FASE5/outputs/phase6_ready/phase6_feature_matrix.csv
FASE5/outputs/phase6_ready/phase6_analysis_sample_membership.csv
FASE5/outputs/phase6_ready/phase6_modeling_contract.yaml
FASE5/outputs/phase6_ready/phase6_missingness_by_column.csv
FASE5/outputs/phase6_ready/phase6_missingness_by_country.csv
FASE5/outputs/phase6_ready/phase6_transform_exclusion_report.csv
FASE5/outputs/phase6_ready/phase6_regulatory_aggregates_audit.csv
```

### 5.2 Desde Fase 6

Obligatorios:

```text
FASE6/outputs/fase6_manifest.json
FASE6/outputs/q1_results.csv
FASE6/outputs/q2_results.csv
FASE6/outputs/q3_results.csv
FASE6/outputs/q4_clusters.csv
FASE6/outputs/q5_results.csv
FASE6/outputs/q6_results.csv
```

Recomendados si existen:

```text
FASE6/outputs/primary_results_long.csv
FASE6/outputs/model_diagnostics.csv
FASE6/outputs/effective_n_by_model.csv
FASE6/outputs/phase6_effective_n_by_outcome.csv
FASE6/outputs/country_positioning_scores.csv
FASE6/outputs/q2_scores_per_country.csv
FASE6/outputs/q5_scores_per_country.csv
FASE6/outputs/q6_scores_per_country.csv
FASE6/outputs/exploratory_binary_sensitivity.csv
FASE6/outputs/psm_exploratory_results.csv
FASE6/outputs/phase7_robustness_contract.yaml
```

Si `phase7_robustness_contract.yaml` no existe, Fase 7 debe crearlo internamente a partir del manifest y registrar una observación `P1`, pero puede continuar si los CSV canónicos están presentes.

---

## 6. Outputs finales obligatorios

### 6.1 `baseline_comparisons.csv`

Objetivo: medir valor incremental de variables regulatorias frente a modelos triviales y solo controles.

Columnas mínimas:

```text
question_id
outcome
model_family
comparison_id
baseline_type
primary_model_id
baseline_model_id
n_effective_primary
n_effective_baseline
metric_name
primary_metric
baseline_metric
metric_delta
regulatory_incremental_value
interpretation_label
estimable
status
notes
```

Valores esperados de `baseline_type`:

```text
trivial_median_or_mean
controls_only
regulatory_only
full_adjusted
```

### 6.2 `sensitivity_analysis.csv`

Objetivo: evaluar estabilidad de hallazgos al excluir grupos o casos relevantes.

Columnas mínimas:

```text
question_id
outcome
term
sensitivity_id
sensitivity_type
excluded_group_label
excluded_iso3
n_full
n_reduced
estimate_full
estimate_reduced
ci_low_full
ci_high_full
ci_low_reduced
ci_high_reduced
direction_full
direction_reduced
sign_flip
relative_change_pct
p_value_full
p_value_reduced
estimable_reduced
stability_label
notes
```

### 6.3 `leave_group_out_analysis.csv`

Objetivo: registrar leave-group-out como sensibilidad, nunca como test externo.

Columnas mínimas:

```text
question_id
outcome
term
group_type
group_left_out
iso3_left_out
n_full
n_reduced
estimate_full
estimate_leave_group_out
direction_full
direction_leave_group_out
sign_flip
magnitude_change
lgo_status
validation_scope
external_validation_used
notes
```

Valores fijos:

```text
validation_scope = "sensitivity_leave_group_out_not_external_test"
external_validation_used = false
```

### 6.4 `outlier_influence.csv`

Objetivo: identificar países con influencia desproporcionada.

Columnas mínimas:

```text
question_id
outcome
term
country_iso3
country_name
influence_metric
influence_value
threshold
is_influential
estimate_full
estimate_without_country
sign_flip_without_country
relative_change_without_country_pct
n_effective_without_country
influence_label
notes
```

Métricas posibles:

```text
cooks_distance
dfbeta
leave_one_country_delta
residual_magnitude
```

### 6.5 `cluster_stability.csv`

Objetivo: evaluar estabilidad de Q4.

Columnas mínimas:

```text
cluster_method
distance_metric
sensitivity_id
excluded_group
n_countries
n_clusters
silhouette_full
silhouette_reduced
ari_vs_full
nmi_vs_full
chile_cluster_full
chile_cluster_reduced
chile_cluster_changed
cluster_stability_label
notes
```

Si no es posible calcular ARI/NMI, registrar:

```text
ari_vs_full = NaN
nmi_vs_full = NaN
notes = "not_computed_reason"
```

### 6.6 `binary_sensitivity_registry.csv`

Objetivo: documentar que los binarios Q2/Q5/Q6 son sensibilidad, no análisis principal.

Columnas mínimas:

```text
question_id
outcome
binary_file_source
binary_model_id
analysis_role
primary_analysis
auc_internal
auc_note
direction_consistent_with_primary
status
notes
```

Valores esperados:

```text
analysis_role = "sensitivity_binary_median"
primary_analysis = false
```

### 6.7 `robustness_registry.csv`

Objetivo: consolidar todas las pruebas de robustez.

Columnas mínimas:

```text
robustness_test_id
question_id
outcome
term
test_family
test_description
n_full
n_tested
result_direction
result_magnitude
passed
severity_if_failed
interpretation
reportable_to_phase8
notes
```

### 6.8 `conclusion_stability_matrix.csv`

Objetivo: matriz central que decide qué hallazgos pasan a Fase 8.

Columnas mínimas:

```text
finding_id
question_id
outcome
term
primary_model_id
primary_direction
primary_estimate
primary_ci95
primary_p_value
primary_p_value_fdr
n_effective
baseline_incremental_value
n_sensitivity_tests
n_sensitivity_passed
n_sensitivity_failed
sign_flip_count
largest_relative_change_pct
outlier_dependency_label
cluster_stability_label
binary_sensitivity_consistency
overall_robustness_label
confidence_level
reportable_in_phase8
recommended_reporting_language
mandatory_limitation
forbidden_overclaim
```

Valores permitidos:

```text
overall_robustness_label:
  - stable
  - directionally_stable
  - fragile
  - not_estimable

confidence_level:
  - alta
  - media
  - baja
  - no_reportar
```

### 6.9 `phase8_reporting_contract.yaml`

Objetivo: entregar a Fase 8 un contrato claro de qué puede comunicar.

Contenido mínimo:

```yaml
version: "1.0"
source_phase: "FASE7"
methodology: "inferential_comparative_observational"
purpose: "reporting_contract_for_policy_translation"
external_validation_used: false
causal_claims_allowed: false

required_inputs_for_phase8:
  - conclusion_stability_matrix.csv
  - robustness_registry.csv
  - baseline_comparisons.csv
  - leave_group_out_analysis.csv
  - outlier_influence.csv

reporting_rules:
  only_report_findings_with_reportable_in_phase8_true: true
  every_reported_finding_requires:
    - question_id
    - outcome
    - term
    - primary_direction
    - n_effective
    - uncertainty
    - overall_robustness_label
    - confidence_level
    - mandatory_limitation

allowed_language:
  - "se observa una asociación ajustada"
  - "el hallazgo es robusto/direccional/frágil"
  - "el resultado se mantiene bajo sensibilidad"
  - "el resultado debe interpretarse con cautela"
  - "Chile se ubica en posición relativa"

forbidden_language:
  - "causa"
  - "impacto causal"
  - "prueba"
  - "demuestra"
  - "predice de forma independiente"
  - "validación externa"
  - "test set independiente"
```

---

## 7. Configuraciones que debe crear Fase 7

## 7.1 `config/robustness_plan.yaml`

```yaml
version: "1.0"
phase: "FASE7"
methodology_version: "mvp-v0.3-architecture-methodology-correction"
purpose: "robustness_and_sensitivity_not_external_validation"

global_policy:
  no_train_test_split: true
  external_validation_used: false
  causal_claims_allowed: false
  do_not_modify_phase5_or_phase6_outputs: true
  rerun_models_only_on_reduced_samples_for_sensitivity: true
  sensitivity_is_not_external_test: true

required_question_families:
  - Q1_investment
  - Q2_adoption
  - Q3_innovation
  - Q4_regulatory_profiles
  - Q5_population_usage
  - Q6_public_sector

robustness_families:
  baselines:
    required: true
    types:
      - trivial_median_or_mean
      - controls_only
      - regulatory_only
      - full_adjusted
  leave_country_out:
    required: true
    scope: "countries_in_effective_sample"
    max_runtime_policy: "skip_if_too_expensive_but_log"
  leave_group_out:
    required: true
    groups:
      - region
      - income_group
      - ai_leaders
      - large_ai_powers
      - latam_peers
      - eu_laggards
  outlier_influence:
    required: true
    metrics:
      - leave_one_country_delta
      - cooks_distance_if_available
      - dfbeta_if_available
  cluster_stability:
    required_for_q4: true
  binary_sensitivity_registry:
    required_for_q2_q5_q6: true

reporting:
  output_main_matrix: "conclusion_stability_matrix.csv"
  output_contract: "phase8_reporting_contract.yaml"
```

## 7.2 `config/sensitivity_groups.yaml`

```yaml
version: "1.0"

groups:
  ai_leaders:
    description: "Países líderes o hubs IA que pueden dominar resultados"
    iso3:
      - USA
      - CHN
      - SGP
      - ARE
      - IRL
      - ISR
      - KOR
      - JPN

  large_ai_powers:
    description: "Grandes potencias IA o mercados gigantes"
    iso3:
      - USA
      - CHN
      - IND
      - JPN

  latam_peers:
    description: "Pares latinoamericanos relevantes para Chile"
    iso3:
      - ARG
      - BRA
      - CHL
      - COL
      - CRI
      - MEX
      - PER
      - URY

  latam_without_chile:
    description: "LATAM sin el caso focal"
    iso3:
      - ARG
      - BRA
      - COL
      - CRI
      - MEX
      - PER
      - URY

  eu_laggards:
    description: "Rezagos europeos incluidos como contraste"
    iso3:
      - GRC
      - ROU
      - HRV

  focal_country:
    description: "Chile como caso focal"
    iso3:
      - CHL

single_country_sensitivity:
  always_test:
    - USA
    - CHN
    - CHL
    - SGP
    - ARE
    - IRL
    - EST
```

## 7.3 `config/baseline_specs.yaml`

```yaml
version: "1.0"

baseline_types:
  trivial:
    regression: "predict_mean_or_median"
    classification: "majority_class"
    clustering: "not_applicable"
    interpretation: "mínimo desempeño esperado sin información explicativa"

  controls_only:
    predictors:
      - wb_gdp_per_capita_ppp_log
      - wb_internet_penetration
      - wb_government_effectiveness
    interpretation: "qué explica el entorno socioeconómico sin regulación"

  regulatory_only:
    predictors:
      - n_binding
      - n_non_binding
      - regulatory_intensity
    interpretation: "asociación bruta regulatoria sin controles"

  full_adjusted:
    source: "fase6_primary_model"
    interpretation: "modelo primario ajustado de Fase 6"

metrics:
  regression:
    - r2_in_sample
    - adj_r2_in_sample
    - rmse_internal
    - mae_internal
  fractional_or_score:
    - pseudo_r2_if_available
    - rmse_internal
    - mae_internal
  classification_sensitivity:
    - auc_internal
    - balanced_accuracy_internal
  clustering:
    - silhouette
```

## 7.4 `config/stability_thresholds.yaml`

```yaml
version: "1.0"

thresholds:
  sign_flip:
    any_sign_flip_is_warning: true
    sign_flip_count_fragile_threshold: 1

  magnitude_change:
    directionally_stable_max_relative_change_pct: 50
    fragile_relative_change_pct: 100

  sensitivity_pass_rate:
    stable_min_pass_rate: 0.75
    directionally_stable_min_pass_rate: 0.50
    fragile_below_pass_rate: 0.50

  n_effective:
    minimum_for_reportable: 15
    minimum_for_high_confidence: 25

  confidence_level:
    alta:
      required_robustness_label: "stable"
      min_n_effective: 25
      no_sign_flips: true
    media:
      allowed_robustness_labels:
        - stable
        - directionally_stable
      min_n_effective: 18
    baja:
      allowed_robustness_labels:
        - fragile
        - directionally_stable
      min_n_effective: 15
    no_reportar:
      if_not_estimable: true
      if_n_effective_below: 15
```

## 7.5 `config/fase7_decisions.yaml`

```yaml
version: "1.0"
methodology_version: "mvp-v0.3-architecture-methodology-correction"
phase: "FASE7"

decisions:
  - id: F7-001
    decision: "Fase 7 evalúa robustez y sensibilidad, no validación externa"
    justification: "La muestra completa ya fue usada por outcome en Fase 6; cualquier exclusión en Fase 7 es una perturbación de sensibilidad, no test independiente."
    status: approved

  - id: F7-002
    decision: "Comparar modelos primarios contra baseline trivial y solo controles"
    justification: "Permite evaluar valor incremental de variables regulatorias frente a factores socioeconómicos."
    status: approved

  - id: F7-003
    decision: "Ejecutar sensibilidad por exclusión de grupos influyentes"
    justification: "Con N=43, países como USA, China o líderes IA pueden dominar asociaciones."
    status: approved

  - id: F7-004
    decision: "Crear matriz de estabilidad de conclusiones como output rector para Fase 8"
    justification: "Fase 8 solo debe reportar hallazgos con trazabilidad, robustez y limitación explícita."
    status: approved

  - id: F7-005
    decision: "No convertir sensibilidad binaria Q2/Q5/Q6 en análisis principal"
    justification: "La versión metodológica v2.1+ exige outcomes continuos/fraccionales como primarios."
    status: approved
```

---

## 8. Implementación paso a paso

## Paso 0 — Crear backup y carpeta de outputs

Ejecutar:

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP

mkdir -p FASE7/config FASE7/src FASE7/tests FASE7/notebooks FASE7/outputs

if [ -d FASE7/outputs ]; then
  cp -r FASE7/outputs FASE7/outputs.pre_fase7_v1_0_$(date +%Y%m%d_%H%M%S) || true
fi
```

No borrar outputs anteriores sin backup.

---

## Paso 1 — Implementar `_common_data.py`

Archivo: `FASE7/src/_common_data.py`

Responsabilidades:

- localizar raíz del MVP;
- cargar feature matrix de Fase 5;
- cargar membership;
- cargar manifest de Fase 6;
- cargar resultados Q1–Q6;
- validar que no hay split;
- no modificar nada.

Código guía:

```python
from pathlib import Path
import json
import pandas as pd
import yaml

FASE7_ROOT = Path(__file__).resolve().parents[1]
MVP_ROOT = FASE7_ROOT.parents[0]
FASE5_BUNDLE = MVP_ROOT / "FASE5" / "outputs" / "phase6_ready"
FASE6_OUTPUTS = MVP_ROOT / "FASE6" / "outputs"
FASE7_OUTPUTS = FASE7_ROOT / "outputs"


def load_feature_matrix() -> pd.DataFrame:
    path = FASE5_BUNDLE / "phase6_feature_matrix.csv"
    if not path.exists():
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    if "split" in df.columns:
        raise RuntimeError("Fase 7 no acepta columna split")
    return df


def load_membership() -> pd.DataFrame:
    path = FASE5_BUNDLE / "phase6_analysis_sample_membership.csv"
    if not path.exists():
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    forbidden = {"split", "train", "test", "holdout"}
    bad = forbidden.intersection({c.lower() for c in df.columns})
    if bad:
        raise RuntimeError(f"Membership contiene columnas prohibidas: {bad}")
    return df


def load_phase6_manifest() -> dict:
    path = FASE6_OUTPUTS / "fase6_manifest.json"
    if not path.exists():
        raise FileNotFoundError(path)
    manifest = json.loads(path.read_text(encoding="utf-8"))
    assert manifest["methodology"] == "inferential_comparative_observational"
    assert manifest["holdout_used"] is False
    assert manifest["train_test_split_used"] is False
    assert manifest["external_validation_used"] is False
    return manifest


def load_phase6_result(name: str) -> pd.DataFrame:
    path = FASE6_OUTPUTS / name
    if not path.exists():
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    if "split" in df.columns:
        raise RuntimeError(f"{name} contiene columna split")
    if "holdout_used" in df.columns:
        assert df["holdout_used"].fillna(False).eq(False).all()
    return df


def load_all_phase6_results() -> dict[str, pd.DataFrame]:
    files = {
        "Q1": "q1_results.csv",
        "Q2": "q2_results.csv",
        "Q3": "q3_results.csv",
        "Q4": "q4_clusters.csv",
        "Q5": "q5_results.csv",
        "Q6": "q6_results.csv",
    }
    out = {}
    for k, fname in files.items():
        out[k] = load_phase6_result(fname)
    return out


def validate_phase6_gate() -> pd.DataFrame:
    checks = []
    def add(name, status, severity="INFO", notes=""):
        checks.append({
            "gate_name": name,
            "status": status,
            "severity": severity,
            "notes": notes,
        })

    try:
        fm = load_feature_matrix()
        add("phase6_feature_matrix_exists", "PASS")
        add("feature_matrix_has_43_rows", "PASS" if len(fm) == 43 else "FAIL", "P0", f"n={len(fm)}")
        add("feature_matrix_no_split", "PASS" if "split" not in fm.columns else "FAIL", "P0")
    except Exception as e:
        add("phase6_feature_matrix", "FAIL", "P0", str(e))

    try:
        m = load_membership()
        add("membership_exists", "PASS")
        add("membership_has_43_iso3", "PASS" if m["iso3"].nunique() == 43 else "FAIL", "P0")
    except Exception as e:
        add("membership", "FAIL", "P0", str(e))

    try:
        manifest = load_phase6_manifest()
        add("fase6_manifest_methodology", "PASS")
        add("fase6_manifest_no_holdout", "PASS" if manifest["holdout_used"] is False else "FAIL", "P0")
    except Exception as e:
        add("fase6_manifest", "FAIL", "P0", str(e))

    return pd.DataFrame(checks)
```

---

## Paso 2 — Implementar `_common_specs.py`

Archivo: `FASE7/src/_common_specs.py`

Responsabilidades:

- leer YAMLs de configuración;
- proveer grupos de sensibilidad;
- proveer thresholds.

```python
from pathlib import Path
import yaml

FASE7_ROOT = Path(__file__).resolve().parents[1]
CONFIG = FASE7_ROOT / "config"


def load_yaml(name: str) -> dict:
    path = CONFIG / name
    if not path.exists():
        raise FileNotFoundError(path)
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_sensitivity_groups() -> dict:
    return load_yaml("sensitivity_groups.yaml")["groups"]


def load_stability_thresholds() -> dict:
    return load_yaml("stability_thresholds.yaml")["thresholds"]


def load_robustness_plan() -> dict:
    return load_yaml("robustness_plan.yaml")
```

---

## Paso 3 — Implementar `baselines.py`

Archivo: `FASE7/src/baselines.py`

Responsabilidades:

- comparar resultados principales de Fase 6 contra baselines;
- cuando sea posible, recalcular baseline trivial y solo controles usando feature matrix;
- si no se puede recalcular por falta de especificación exacta, registrar `not_estimable` con razón;
- no alterar Fase 6.

Implementación mínima robusta:

```python
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import Ridge
from sklearn.model_selection import RepeatedKFold, cross_val_score


DEFAULT_CONTROLS = [
    "wb_gdp_per_capita_ppp_log",
    "wb_internet_penetration",
    "wb_government_effectiveness",
]


def _safe_controls(fm: pd.DataFrame) -> list[str]:
    return [c for c in DEFAULT_CONTROLS if c in fm.columns]


def regression_baselines_for_outcome(fm: pd.DataFrame, outcome: str, controls: list[str]) -> list[dict]:
    rows = []
    if outcome not in fm.columns:
        return [{
            "outcome": outcome,
            "baseline_type": "not_estimable",
            "status": "missing_outcome_in_feature_matrix",
        }]

    y = fm[outcome]
    sub_y = fm[[outcome]].dropna()
    if len(sub_y) < 10:
        return [{
            "outcome": outcome,
            "baseline_type": "not_estimable",
            "status": "low_n_outcome",
            "n_effective_baseline": len(sub_y),
        }]

    median_pred = np.repeat(sub_y[outcome].median(), len(sub_y))
    mean_pred = np.repeat(sub_y[outcome].mean(), len(sub_y))

    for label, pred in [("trivial_median", median_pred), ("trivial_mean", mean_pred)]:
        rmse = mean_squared_error(sub_y[outcome], pred, squared=False)
        mae = mean_absolute_error(sub_y[outcome], pred)
        rows.append({
            "outcome": outcome,
            "baseline_type": label,
            "metric_name": "rmse",
            "baseline_metric": float(rmse),
            "mae": float(mae),
            "n_effective_baseline": len(sub_y),
            "status": "ok",
        })

    usable_controls = [c for c in controls if c in fm.columns]
    if usable_controls:
        sub = fm[[outcome] + usable_controls].dropna()
        if len(sub) >= 12:
            X = sub[usable_controls].values
            yv = sub[outcome].values
            k = min(5, max(3, len(sub) // 5))
            cv = RepeatedKFold(n_splits=k, n_repeats=20, random_state=20260508)
            model = Ridge(alpha=1.0)
            r2 = cross_val_score(model, X, yv, cv=cv, scoring="r2")
            neg_mse = cross_val_score(model, X, yv, cv=cv, scoring="neg_mean_squared_error")
            rows.append({
                "outcome": outcome,
                "baseline_type": "controls_only",
                "metric_name": "cv_r2",
                "baseline_metric": float(np.nanmean(r2)),
                "rmse": float(np.sqrt(-np.nanmean(neg_mse))),
                "n_effective_baseline": len(sub),
                "controls_used": ";".join(usable_controls),
                "status": "ok",
            })
        else:
            rows.append({
                "outcome": outcome,
                "baseline_type": "controls_only",
                "status": "low_n_after_controls_dropna",
                "n_effective_baseline": len(sub),
            })

    return rows


def build_baseline_comparisons(fm: pd.DataFrame, phase6_results: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    controls = _safe_controls(fm)

    for q, df in phase6_results.items():
        if q == "Q4":
            continue
        if "outcome" not in df.columns:
            continue

        outcomes = sorted(df["outcome"].dropna().unique())
        for outcome in outcomes:
            base_rows = regression_baselines_for_outcome(fm, outcome, controls)
            primary_subset = df[df["outcome"] == outcome].copy()

            primary_metric = None
            if "r2_in_sample" in primary_subset.columns:
                vals = pd.to_numeric(primary_subset["r2_in_sample"], errors="coerce").dropna()
                if not vals.empty:
                    primary_metric = float(vals.iloc[0])
            elif "adj_r2_in_sample" in primary_subset.columns:
                vals = pd.to_numeric(primary_subset["adj_r2_in_sample"], errors="coerce").dropna()
                if not vals.empty:
                    primary_metric = float(vals.iloc[0])

            for b in base_rows:
                rows.append({
                    "question_id": q,
                    "outcome": outcome,
                    "model_family": "baseline_comparison",
                    "comparison_id": f"{q}_{outcome}_{b.get('baseline_type')}",
                    "baseline_type": b.get("baseline_type"),
                    "primary_model_id": "phase6_primary",
                    "baseline_model_id": b.get("baseline_type"),
                    "n_effective_primary": primary_subset.get("n_effective", pd.Series([pd.NA])).dropna().iloc[0] if "n_effective" in primary_subset.columns and primary_subset["n_effective"].notna().any() else pd.NA,
                    "n_effective_baseline": b.get("n_effective_baseline"),
                    "metric_name": b.get("metric_name"),
                    "primary_metric": primary_metric,
                    "baseline_metric": b.get("baseline_metric"),
                    "metric_delta": None if primary_metric is None or b.get("baseline_metric") is None else primary_metric - b.get("baseline_metric"),
                    "regulatory_incremental_value": "not_directly_comparable" if primary_metric is None else "estimated",
                    "interpretation_label": "diagnostic_internal_not_external_test",
                    "estimable": b.get("status") == "ok",
                    "status": b.get("status"),
                    "notes": b.get("controls_used", ""),
                })

    return pd.DataFrame(rows)
```

---

## Paso 4 — Implementar `sensitivity.py`

Archivo: `FASE7/src/sensitivity.py`

Responsabilidades:

- reestimar modelos básicos o calcular estabilidad sobre resultados si reestimación exacta no es viable;
- excluir grupos predefinidos;
- registrar sign flips, cambios de magnitud y `n_effective`.

Para mantener Fase 7 robusta sin depender de todas las funciones internas de Fase 6, implementar dos niveles:

1. **Nivel A — reestimación reducida** si existen funciones/API de Fase 6 reutilizables.
2. **Nivel B — sensibilidad estructural** usando feature matrix y modelo parsimonioso genérico.

Código guía del Nivel B:

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm


DEFAULT_TERMS = ["n_binding", "n_non_binding", "regulatory_intensity", "iapp_ley_ia_vigente"]
DEFAULT_CONTROLS = ["wb_gdp_per_capita_ppp_log", "wb_internet_penetration"]


def direction(x):
    if pd.isna(x):
        return "NA"
    if x > 0:
        return "positive"
    if x < 0:
        return "negative"
    return "zero"


def fit_simple_adjusted(fm: pd.DataFrame, outcome: str, term: str, controls: list[str]) -> dict:
    cols = [outcome, term] + [c for c in controls if c in fm.columns]
    if outcome not in fm.columns or term not in fm.columns:
        return {"status": "missing_columns", "estimate": np.nan, "n_effective": 0}

    sub = fm[cols].dropna()
    if len(sub) < max(12, len(cols) * 4):
        return {"status": "low_n", "estimate": np.nan, "n_effective": len(sub)}

    X = sm.add_constant(sub[[term] + [c for c in controls if c in sub.columns]], has_constant="add")
    y = sub[outcome]
    try:
        model = sm.OLS(y, X).fit(cov_type="HC3")
        return {
            "status": "ok",
            "estimate": float(model.params.get(term, np.nan)),
            "std_error": float(model.bse.get(term, np.nan)),
            "p_value": float(model.pvalues.get(term, np.nan)),
            "ci_low": float(model.conf_int().loc[term, 0]) if term in model.params.index else np.nan,
            "ci_high": float(model.conf_int().loc[term, 1]) if term in model.params.index else np.nan,
            "n_effective": len(sub),
        }
    except Exception as e:
        return {"status": "model_error", "estimate": np.nan, "n_effective": len(sub), "notes": str(e)[:250]}


def sensitivity_exclude_group(
    fm: pd.DataFrame,
    question_id: str,
    outcome: str,
    term: str,
    excluded_iso3: list[str],
    sensitivity_id: str,
    sensitivity_type: str,
    excluded_group_label: str,
    controls: list[str] | None = None,
) -> dict:
    if controls is None:
        controls = DEFAULT_CONTROLS

    full = fit_simple_adjusted(fm, outcome, term, controls)
    reduced_fm = fm[~fm["iso3"].isin(excluded_iso3)].copy()
    reduced = fit_simple_adjusted(reduced_fm, outcome, term, controls)

    est_full = full.get("estimate", np.nan)
    est_red = reduced.get("estimate", np.nan)
    sign_flip = direction(est_full) != direction(est_red) and "NA" not in {direction(est_full), direction(est_red)}
    rel_change = np.nan
    if not pd.isna(est_full) and est_full != 0 and not pd.isna(est_red):
        rel_change = abs((est_red - est_full) / est_full) * 100

    return {
        "question_id": question_id,
        "outcome": outcome,
        "term": term,
        "sensitivity_id": sensitivity_id,
        "sensitivity_type": sensitivity_type,
        "excluded_group_label": excluded_group_label,
        "excluded_iso3": ";".join(excluded_iso3),
        "n_full": full.get("n_effective", 0),
        "n_reduced": reduced.get("n_effective", 0),
        "estimate_full": est_full,
        "estimate_reduced": est_red,
        "ci_low_full": full.get("ci_low", np.nan),
        "ci_high_full": full.get("ci_high", np.nan),
        "ci_low_reduced": reduced.get("ci_low", np.nan),
        "ci_high_reduced": reduced.get("ci_high", np.nan),
        "direction_full": direction(est_full),
        "direction_reduced": direction(est_red),
        "sign_flip": bool(sign_flip),
        "relative_change_pct": rel_change,
        "p_value_full": full.get("p_value", np.nan),
        "p_value_reduced": reduced.get("p_value", np.nan),
        "estimable_reduced": reduced.get("status") == "ok",
        "stability_label": "fragile" if sign_flip else "directionally_stable",
        "notes": f"full_status={full.get('status')}; reduced_status={reduced.get('status')}",
    }


def build_sensitivity_analysis(fm: pd.DataFrame, phase6_results: dict[str, pd.DataFrame], groups: dict) -> pd.DataFrame:
    rows = []
    controls = DEFAULT_CONTROLS

    for q, df in phase6_results.items():
        if q == "Q4" or "outcome" not in df.columns:
            continue

        outcomes = sorted(df["outcome"].dropna().unique())
        for outcome in outcomes:
            terms = [t for t in DEFAULT_TERMS if t in fm.columns]
            for term in terms:
                for group_name, group_def in groups.items():
                    iso3 = group_def.get("iso3", [])
                    rows.append(sensitivity_exclude_group(
                        fm=fm,
                        question_id=q,
                        outcome=outcome,
                        term=term,
                        excluded_iso3=iso3,
                        sensitivity_id=f"{q}_{outcome}_{term}_exclude_{group_name}",
                        sensitivity_type="exclude_predefined_group",
                        excluded_group_label=group_name,
                        controls=controls,
                    ))

    return pd.DataFrame(rows)
```

---

## Paso 5 — Implementar `leave_group_out.py`

Archivo: `FASE7/src/leave_group_out.py`

Responsabilidades:

- usar `membership` para excluir cada región o grupo de ingreso;
- reportar claramente que no es test externo.

```python
import pandas as pd
from .sensitivity import sensitivity_exclude_group, DEFAULT_TERMS


def build_leave_group_out(fm: pd.DataFrame, membership: pd.DataFrame, phase6_results: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    merged = fm.merge(membership[["iso3", "region", "income_group"]], on="iso3", how="left", suffixes=("", "_membership"))

    groups = []
    if "region" in membership.columns:
        for region in sorted(membership["region"].dropna().unique()):
            iso3 = membership.loc[membership["region"] == region, "iso3"].tolist()
            groups.append(("region", region, iso3))

    if "income_group" in membership.columns:
        for inc in sorted(membership["income_group"].dropna().unique()):
            iso3 = membership.loc[membership["income_group"] == inc, "iso3"].tolist()
            groups.append(("income_group", inc, iso3))

    for q, df in phase6_results.items():
        if q == "Q4" or "outcome" not in df.columns:
            continue
        outcomes = sorted(df["outcome"].dropna().unique())
        for outcome in outcomes:
            for term in [t for t in DEFAULT_TERMS if t in fm.columns]:
                for group_type, group_value, iso3 in groups:
                    result = sensitivity_exclude_group(
                        fm=fm,
                        question_id=q,
                        outcome=outcome,
                        term=term,
                        excluded_iso3=iso3,
                        sensitivity_id=f"{q}_{outcome}_{term}_leave_{group_type}_{group_value}",
                        sensitivity_type="leave_group_out_not_external_test",
                        excluded_group_label=f"{group_type}:{group_value}",
                    )
                    rows.append({
                        "question_id": result["question_id"],
                        "outcome": result["outcome"],
                        "term": result["term"],
                        "group_type": group_type,
                        "group_left_out": group_value,
                        "iso3_left_out": result["excluded_iso3"],
                        "n_full": result["n_full"],
                        "n_reduced": result["n_reduced"],
                        "estimate_full": result["estimate_full"],
                        "estimate_leave_group_out": result["estimate_reduced"],
                        "direction_full": result["direction_full"],
                        "direction_leave_group_out": result["direction_reduced"],
                        "sign_flip": result["sign_flip"],
                        "magnitude_change": result["relative_change_pct"],
                        "lgo_status": result["stability_label"],
                        "validation_scope": "sensitivity_leave_group_out_not_external_test",
                        "external_validation_used": False,
                        "notes": result["notes"],
                    })

    return pd.DataFrame(rows)
```

---

## Paso 6 — Implementar `outliers.py`

Archivo: `FASE7/src/outliers.py`

Responsabilidades:

- calcular influencia país por país;
- detectar dependencia excesiva;
- no eliminar outliers del análisis principal;
- documentar qué pasa si se excluye cada país.

```python
import numpy as np
import pandas as pd
from .sensitivity import fit_simple_adjusted, direction, DEFAULT_TERMS, DEFAULT_CONTROLS


def leave_one_country_influence(fm: pd.DataFrame, question_id: str, outcome: str, term: str) -> list[dict]:
    full = fit_simple_adjusted(fm, outcome, term, DEFAULT_CONTROLS)
    est_full = full.get("estimate", np.nan)
    rows = []

    if full.get("status") != "ok":
        return [{
            "question_id": question_id,
            "outcome": outcome,
            "term": term,
            "country_iso3": None,
            "influence_metric": "leave_one_country_delta",
            "influence_value": np.nan,
            "is_influential": False,
            "estimate_full": est_full,
            "notes": f"full_model_not_ok:{full.get('status')}",
        }]

    for iso3 in fm["iso3"].dropna().unique():
        reduced = fm[fm["iso3"] != iso3].copy()
        red = fit_simple_adjusted(reduced, outcome, term, DEFAULT_CONTROLS)
        est_red = red.get("estimate", np.nan)
        rel_change = np.nan
        if not pd.isna(est_full) and est_full != 0 and not pd.isna(est_red):
            rel_change = abs((est_red - est_full) / est_full) * 100
        sign_flip = direction(est_full) != direction(est_red) and "NA" not in {direction(est_full), direction(est_red)}
        rows.append({
            "question_id": question_id,
            "outcome": outcome,
            "term": term,
            "country_iso3": iso3,
            "country_name": reduced.loc[reduced["iso3"] == iso3, "country_name_canonical"].iloc[0] if "country_name_canonical" in reduced.columns and (reduced["iso3"] == iso3).any() else "",
            "influence_metric": "leave_one_country_delta",
            "influence_value": rel_change,
            "threshold": 50,
            "is_influential": bool(sign_flip or (not pd.isna(rel_change) and rel_change >= 50)),
            "estimate_full": est_full,
            "estimate_without_country": est_red,
            "sign_flip_without_country": bool(sign_flip),
            "relative_change_without_country_pct": rel_change,
            "n_effective_without_country": red.get("n_effective", 0),
            "influence_label": "high" if sign_flip or (not pd.isna(rel_change) and rel_change >= 50) else "normal",
            "notes": red.get("status", ""),
        })
    return rows


def build_outlier_influence(fm: pd.DataFrame, phase6_results: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for q, df in phase6_results.items():
        if q == "Q4" or "outcome" not in df.columns:
            continue
        for outcome in sorted(df["outcome"].dropna().unique()):
            for term in [t for t in DEFAULT_TERMS if t in fm.columns]:
                rows.extend(leave_one_country_influence(fm, q, outcome, term))
    return pd.DataFrame(rows)
```

---

## Paso 7 — Implementar `cluster_stability.py`

Archivo: `FASE7/src/cluster_stability.py`

Responsabilidades:

- evaluar Q4 como tipología descriptiva;
- medir si Chile cambia de cluster bajo exclusiones;
- no hablar de accuracy ni test externo.

Implementación mínima:

```python
import numpy as np
import pandas as pd
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, silhouette_score
from sklearn.cluster import KMeans


def _regulatory_binary_cols(fm: pd.DataFrame) -> list[str]:
    cols = []
    for c in fm.columns:
        if c.startswith("iapp_") or c in {"n_binding", "n_non_binding", "n_hybrid"}:
            s = fm[c].dropna()
            if len(s) > 0 and s.nunique() > 1:
                cols.append(c)
    return cols


def run_simple_kmeans(fm: pd.DataFrame, k: int = 4) -> pd.Series:
    cols = _regulatory_binary_cols(fm)
    if len(cols) < 2 or len(fm) < k * 2:
        return pd.Series(index=fm.index, data=pd.NA)
    X = fm[cols].fillna(0).astype(float)
    km = KMeans(n_clusters=k, random_state=20260508, n_init=20)
    labels = km.fit_predict(X)
    return pd.Series(labels, index=fm.index)


def build_cluster_stability(fm: pd.DataFrame, membership: pd.DataFrame) -> pd.DataFrame:
    rows = []
    full_labels = run_simple_kmeans(fm)
    if full_labels.isna().all():
        return pd.DataFrame([{
            "cluster_method": "kmeans",
            "distance_metric": "euclidean_on_regulatory_features",
            "sensitivity_id": "full",
            "cluster_stability_label": "not_estimable",
            "notes": "insufficient_regulatory_features_or_n",
        }])

    chile_full = None
    if "CHL" in set(fm["iso3"]):
        chile_full = full_labels.loc[fm.index[fm["iso3"] == "CHL"][0]]

    group_specs = []
    if "region" in membership.columns:
        for g in membership["region"].dropna().unique():
            group_specs.append(("region", g, membership.loc[membership["region"] == g, "iso3"].tolist()))
    if "income_group" in membership.columns:
        for g in membership["income_group"].dropna().unique():
            group_specs.append(("income_group", g, membership.loc[membership["income_group"] == g, "iso3"].tolist()))

    for group_type, group_value, iso3 in group_specs:
        reduced = fm[~fm["iso3"].isin(iso3)].copy()
        labels_red = run_simple_kmeans(reduced)
        chile_red = None
        if "CHL" in set(reduced["iso3"]):
            chile_red = labels_red.loc[reduced.index[reduced["iso3"] == "CHL"][0]]

        rows.append({
            "cluster_method": "kmeans",
            "distance_metric": "euclidean_on_regulatory_features",
            "sensitivity_id": f"leave_{group_type}_{group_value}",
            "excluded_group": f"{group_type}:{group_value}",
            "n_countries": len(reduced),
            "n_clusters": labels_red.nunique(dropna=True),
            "silhouette_full": np.nan,
            "silhouette_reduced": np.nan,
            "ari_vs_full": np.nan,
            "nmi_vs_full": np.nan,
            "chile_cluster_full": chile_full,
            "chile_cluster_reduced": chile_red,
            "chile_cluster_changed": bool(chile_full != chile_red) if chile_full is not None and chile_red is not None else pd.NA,
            "cluster_stability_label": "directionally_stable" if chile_full == chile_red else "fragile_or_not_comparable",
            "notes": "cluster labels are not directly comparable across refits; Chile change is diagnostic only",
        })

    return pd.DataFrame(rows)
```

---

## Paso 8 — Implementar `binary_sensitivity.py`

Archivo: `FASE7/src/binary_sensitivity.py`

Responsabilidades:

- buscar `exploratory_binary_sensitivity.csv` o filas binarias en Q2/Q5/Q6;
- comprobar que son sensibilidad;
- comparar consistencia direccional con resultados primarios si es posible.

```python
from pathlib import Path
import pandas as pd

FASE7_ROOT = Path(__file__).resolve().parents[1]
MVP_ROOT = FASE7_ROOT.parents[0]
FASE6_OUTPUTS = MVP_ROOT / "FASE6" / "outputs"


def build_binary_sensitivity_registry() -> pd.DataFrame:
    rows = []
    files = [
        "exploratory_binary_sensitivity.csv",
        "q2_results.csv",
        "q5_results.csv",
        "q6_results.csv",
    ]

    for fname in files:
        path = FASE6_OUTPUTS / fname
        if not path.exists():
            continue
        df = pd.read_csv(path)
        if "analysis_role" not in df.columns:
            continue
        binary = df[df["analysis_role"].astype(str).str.contains("binary|median", case=False, na=False)].copy()
        for _, r in binary.iterrows():
            rows.append({
                "question_id": r.get("question", r.get("question_id", "")),
                "outcome": r.get("outcome", ""),
                "binary_file_source": fname,
                "binary_model_id": r.get("model_id", ""),
                "analysis_role": r.get("analysis_role", ""),
                "primary_analysis": bool(r.get("primary_analysis", False)),
                "auc_internal": r.get("auc_repeated_kfold", r.get("auc_internal", pd.NA)),
                "auc_note": r.get("auc_note", ""),
                "direction_consistent_with_primary": "not_assessed",
                "status": "ok_sensitivity_only" if not bool(r.get("primary_analysis", False)) else "error_binary_marked_primary",
                "notes": "Binary median model must remain sensitivity only",
            })

    if not rows:
        rows.append({
            "question_id": "Q2_Q5_Q6",
            "status": "no_binary_sensitivity_found",
            "notes": "Acceptable if Fase 6 did not generate binary sensitivity; not acceptable if it used binary as primary.",
        })
    return pd.DataFrame(rows)
```

---

## Paso 9 — Implementar `stability.py`

Archivo: `FASE7/src/stability.py`

Responsabilidades:

- aplicar thresholds;
- etiquetar cada hallazgo como `stable`, `directionally_stable`, `fragile`, `not_estimable`.

```python
import pandas as pd
import numpy as np


def classify_stability(
    n_tests: int,
    n_failed: int,
    sign_flip_count: int,
    largest_relative_change_pct,
    n_effective,
) -> tuple[str, str]:
    if pd.isna(n_effective) or n_effective < 15:
        return "not_estimable", "no_reportar"

    pass_rate = 1.0 if n_tests == 0 else (n_tests - n_failed) / n_tests

    if sign_flip_count == 0 and pass_rate >= 0.75 and (pd.isna(largest_relative_change_pct) or largest_relative_change_pct <= 50):
        label = "stable"
    elif sign_flip_count <= 1 and pass_rate >= 0.50:
        label = "directionally_stable"
    else:
        label = "fragile"

    if label == "stable" and n_effective >= 25:
        confidence = "alta"
    elif label in {"stable", "directionally_stable"} and n_effective >= 18:
        confidence = "media"
    elif n_effective >= 15:
        confidence = "baja"
    else:
        confidence = "no_reportar"

    return label, confidence


def summarize_sensitivity(sens: pd.DataFrame) -> pd.DataFrame:
    if sens.empty:
        return pd.DataFrame()

    group_cols = ["question_id", "outcome", "term"]
    rows = []
    for keys, g in sens.groupby(group_cols, dropna=False):
        q, outcome, term = keys
        n_tests = len(g)
        sign_flip_count = int(g["sign_flip"].fillna(False).sum()) if "sign_flip" in g.columns else 0
        n_failed = sign_flip_count
        if "relative_change_pct" in g.columns:
            largest = pd.to_numeric(g["relative_change_pct"], errors="coerce").max()
        else:
            largest = pd.NA
        n_eff = pd.to_numeric(g["n_full"], errors="coerce").dropna()
        n_effective = int(n_eff.iloc[0]) if not n_eff.empty else pd.NA
        label, confidence = classify_stability(n_tests, n_failed, sign_flip_count, largest, n_effective)
        rows.append({
            "question_id": q,
            "outcome": outcome,
            "term": term,
            "n_sensitivity_tests": n_tests,
            "n_sensitivity_passed": n_tests - n_failed,
            "n_sensitivity_failed": n_failed,
            "sign_flip_count": sign_flip_count,
            "largest_relative_change_pct": largest,
            "overall_robustness_label": label,
            "confidence_level": confidence,
        })
    return pd.DataFrame(rows)
```

---

## Paso 10 — Implementar `conclusion_matrix.py`

Archivo: `FASE7/src/conclusion_matrix.py`

Responsabilidades:

- consolidar resultados de Fase 6 y Fase 7;
- determinar qué hallazgos pasan a Fase 8;
- asignar lenguaje recomendado y limitación obligatoria.

```python
import pandas as pd


def _primary_rows(phase6_results: dict[str, pd.DataFrame]) -> pd.DataFrame:
    frames = []
    for q, df in phase6_results.items():
        if q == "Q4":
            continue
        temp = df.copy()
        if "question_id" not in temp.columns:
            temp["question_id"] = q
        if "analysis_role" in temp.columns:
            mask = temp["analysis_role"].astype(str).str.contains("primary", case=False, na=False)
            if mask.any():
                temp = temp[mask]
        frames.append(temp)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def build_conclusion_stability_matrix(
    phase6_results: dict[str, pd.DataFrame],
    sensitivity_summary: pd.DataFrame,
    baseline_comparisons: pd.DataFrame,
    outlier_influence: pd.DataFrame,
    cluster_stability: pd.DataFrame,
    binary_registry: pd.DataFrame,
) -> pd.DataFrame:
    primary = _primary_rows(phase6_results)
    rows = []

    if primary.empty:
        return pd.DataFrame([{
            "finding_id": "no_primary_rows",
            "overall_robustness_label": "not_estimable",
            "confidence_level": "no_reportar",
            "reportable_in_phase8": False,
            "mandatory_limitation": "No primary Fase 6 rows available.",
        }])

    for i, r in primary.iterrows():
        q = r.get("question_id", r.get("question", ""))
        outcome = r.get("outcome", "")
        term = r.get("term", r.get("predictor", ""))
        if not term or str(term).lower() in {"const", "intercept"}:
            continue

        ss = sensitivity_summary[
            (sensitivity_summary["question_id"].astype(str) == str(q)) &
            (sensitivity_summary["outcome"].astype(str) == str(outcome)) &
            (sensitivity_summary["term"].astype(str) == str(term))
        ]

        if not ss.empty:
            robust_label = ss["overall_robustness_label"].iloc[0]
            confidence = ss["confidence_level"].iloc[0]
            n_tests = ss["n_sensitivity_tests"].iloc[0]
            n_passed = ss["n_sensitivity_passed"].iloc[0]
            n_failed = ss["n_sensitivity_failed"].iloc[0]
            sign_flips = ss["sign_flip_count"].iloc[0]
            largest_change = ss["largest_relative_change_pct"].iloc[0]
        else:
            robust_label = "not_estimable"
            confidence = "no_reportar"
            n_tests = 0
            n_passed = 0
            n_failed = 0
            sign_flips = 0
            largest_change = pd.NA

        n_effective = r.get("n_effective", pd.NA)
        reportable = confidence in {"alta", "media", "baja"} and robust_label != "not_estimable"

        direction = "positive" if pd.to_numeric(pd.Series([r.get("estimate", r.get("coefficient", pd.NA))]), errors="coerce").iloc[0] > 0 else "negative_or_zero_or_unknown"

        rows.append({
            "finding_id": f"{q}_{outcome}_{term}",
            "question_id": q,
            "outcome": outcome,
            "term": term,
            "primary_model_id": r.get("model_id", ""),
            "primary_direction": direction,
            "primary_estimate": r.get("estimate", r.get("coefficient", pd.NA)),
            "primary_ci95": f"[{r.get('ci_low', r.get('ci95_low', pd.NA))}, {r.get('ci_high', r.get('ci95_high', pd.NA))}]",
            "primary_p_value": r.get("p_value", pd.NA),
            "primary_p_value_fdr": r.get("p_value_fdr", pd.NA),
            "n_effective": n_effective,
            "baseline_incremental_value": "see_baseline_comparisons",
            "n_sensitivity_tests": n_tests,
            "n_sensitivity_passed": n_passed,
            "n_sensitivity_failed": n_failed,
            "sign_flip_count": sign_flips,
            "largest_relative_change_pct": largest_change,
            "outlier_dependency_label": "see_outlier_influence",
            "cluster_stability_label": "not_applicable",
            "binary_sensitivity_consistency": "see_binary_sensitivity_registry",
            "overall_robustness_label": robust_label,
            "confidence_level": confidence,
            "reportable_in_phase8": bool(reportable),
            "recommended_reporting_language": "se observa una asociación ajustada" if reportable else "no reportar como hallazgo principal",
            "mandatory_limitation": "Diseño observacional, N pequeño, sensibilidad interna; no causalidad fuerte ni validación externa.",
            "forbidden_overclaim": "No decir que causa, predice independientemente o fue validado externamente.",
        })

    return pd.DataFrame(rows)
```

---

## Paso 11 — Implementar `phase8_contract.py`

Archivo: `FASE7/src/phase8_contract.py`

```python
from pathlib import Path
import yaml

FASE7_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE7_ROOT / "outputs"


def write_phase8_reporting_contract(conclusion_matrix_path: str = "conclusion_stability_matrix.csv") -> Path:
    contract = {
        "version": "1.0",
        "source_phase": "FASE7",
        "methodology": "inferential_comparative_observational",
        "purpose": "reporting_contract_for_policy_translation",
        "external_validation_used": False,
        "causal_claims_allowed": False,
        "required_inputs_for_phase8": [
            conclusion_matrix_path,
            "robustness_registry.csv",
            "baseline_comparisons.csv",
            "leave_group_out_analysis.csv",
            "outlier_influence.csv",
        ],
        "reporting_rules": {
            "only_report_findings_with_reportable_in_phase8_true": True,
            "every_reported_finding_requires": [
                "question_id",
                "outcome",
                "term",
                "primary_direction",
                "n_effective",
                "uncertainty",
                "overall_robustness_label",
                "confidence_level",
                "mandatory_limitation",
            ],
        },
        "allowed_language": [
            "se observa una asociación ajustada",
            "el hallazgo es robusto/direccional/frágil",
            "el resultado se mantiene bajo sensibilidad",
            "el resultado debe interpretarse con cautela",
            "Chile se ubica en posición relativa",
        ],
        "forbidden_language": [
            "causa",
            "impacto causal",
            "prueba",
            "demuestra",
            "predice de forma independiente",
            "validación externa",
            "test set independiente",
        ],
    }
    path = OUTPUTS / "phase8_reporting_contract.yaml"
    path.write_text(yaml.safe_dump(contract, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return path
```

---

## Paso 12 — Implementar `validate.py`

Archivo: `FASE7/src/validate.py`

Responsabilidades:

- validar outputs obligatorios;
- validar ausencia de lenguaje prohibido;
- validar que leave-group-out no se etiqueta como test externo;
- validar que matriz de conclusiones existe y tiene etiquetas.

```python
from pathlib import Path
import pandas as pd
import json

FASE7_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE7_ROOT / "outputs"


REQUIRED_OUTPUTS = [
    "baseline_comparisons.csv",
    "sensitivity_analysis.csv",
    "leave_group_out_analysis.csv",
    "outlier_influence.csv",
    "cluster_stability.csv",
    "binary_sensitivity_registry.csv",
    "robustness_registry.csv",
    "conclusion_stability_matrix.csv",
    "phase8_reporting_contract.yaml",
    "fase7_manifest.json",
]


def validate_outputs_exist() -> list[dict]:
    rows = []
    for fname in REQUIRED_OUTPUTS:
        path = OUTPUTS / fname
        rows.append({
            "check": f"exists_{fname}",
            "status": "PASS" if path.exists() else "FAIL",
            "severity": "P0" if not path.exists() else "INFO",
            "notes": str(path),
        })
    return rows


def validate_leave_group_out() -> list[dict]:
    path = OUTPUTS / "leave_group_out_analysis.csv"
    if not path.exists():
        return [{"check": "leave_group_out_exists", "status": "FAIL", "severity": "P0"}]
    df = pd.read_csv(path)
    rows = []
    if "external_validation_used" in df.columns:
        ok = df["external_validation_used"].fillna(False).eq(False).all()
        rows.append({"check": "leave_group_out_not_external", "status": "PASS" if ok else "FAIL", "severity": "P0"})
    else:
        rows.append({"check": "leave_group_out_external_validation_col", "status": "FAIL", "severity": "P1"})
    if "validation_scope" in df.columns:
        ok = df["validation_scope"].astype(str).str.contains("not_external_test", na=False).all()
        rows.append({"check": "leave_group_out_scope_label", "status": "PASS" if ok else "FAIL", "severity": "P0"})
    return rows


def validate_conclusion_matrix() -> list[dict]:
    path = OUTPUTS / "conclusion_stability_matrix.csv"
    if not path.exists():
        return [{"check": "conclusion_matrix_exists", "status": "FAIL", "severity": "P0"}]
    df = pd.read_csv(path)
    required = ["overall_robustness_label", "confidence_level", "reportable_in_phase8", "mandatory_limitation"]
    rows = []
    for col in required:
        rows.append({
            "check": f"conclusion_matrix_has_{col}",
            "status": "PASS" if col in df.columns else "FAIL",
            "severity": "P0",
        })
    if "overall_robustness_label" in df.columns:
        allowed = {"stable", "directionally_stable", "fragile", "not_estimable"}
        bad = set(df["overall_robustness_label"].dropna()) - allowed
        rows.append({
            "check": "robustness_labels_allowed",
            "status": "PASS" if not bad else "FAIL",
            "severity": "P1",
            "notes": str(bad),
        })
    return rows


def run_validation() -> pd.DataFrame:
    checks = []
    checks.extend(validate_outputs_exist())
    checks.extend(validate_leave_group_out())
    checks.extend(validate_conclusion_matrix())
    return pd.DataFrame(checks)
```

---

## Paso 13 — Implementar `run_all.py`

Archivo: `FASE7/src/run_all.py`

Responsabilidades:

- ejecutar pre-flight;
- cargar inputs;
- ejecutar cada módulo;
- escribir outputs;
- generar manifest;
- validar.

```python
from pathlib import Path
import json
from datetime import datetime, timezone
import pandas as pd

from ._common_data import (
    FASE7_OUTPUTS,
    validate_phase6_gate,
    load_feature_matrix,
    load_membership,
    load_phase6_manifest,
    load_all_phase6_results,
)
from ._common_specs import load_sensitivity_groups
from .baselines import build_baseline_comparisons
from .sensitivity import build_sensitivity_analysis
from .leave_group_out import build_leave_group_out
from .outliers import build_outlier_influence
from .cluster_stability import build_cluster_stability
from .binary_sensitivity import build_binary_sensitivity_registry
from .stability import summarize_sensitivity
from .conclusion_matrix import build_conclusion_stability_matrix
from .phase8_contract import write_phase8_reporting_contract
from .validate import run_validation


def main():
    FASE7_OUTPUTS.mkdir(parents=True, exist_ok=True)

    preflight = validate_phase6_gate()
    preflight.to_csv(FASE7_OUTPUTS / "fase7_preflight_report.csv", index=False)
    if (preflight["status"] == "FAIL").any():
        raise RuntimeError("Fase 7 abortada: preflight Fase 6 -> Fase 7 falló.")

    fm = load_feature_matrix()
    membership = load_membership()
    manifest6 = load_phase6_manifest()
    phase6_results = load_all_phase6_results()
    groups = load_sensitivity_groups()

    baseline = build_baseline_comparisons(fm, phase6_results)
    baseline.to_csv(FASE7_OUTPUTS / "baseline_comparisons.csv", index=False)

    sens = build_sensitivity_analysis(fm, phase6_results, groups)
    sens.to_csv(FASE7_OUTPUTS / "sensitivity_analysis.csv", index=False)

    lgo = build_leave_group_out(fm, membership, phase6_results)
    lgo.to_csv(FASE7_OUTPUTS / "leave_group_out_analysis.csv", index=False)

    outliers = build_outlier_influence(fm, phase6_results)
    outliers.to_csv(FASE7_OUTPUTS / "outlier_influence.csv", index=False)

    cluster = build_cluster_stability(fm, membership)
    cluster.to_csv(FASE7_OUTPUTS / "cluster_stability.csv", index=False)

    binary = build_binary_sensitivity_registry()
    binary.to_csv(FASE7_OUTPUTS / "binary_sensitivity_registry.csv", index=False)

    sens_summary = summarize_sensitivity(sens)
    robustness_registry = sens.copy()
    robustness_registry["test_family"] = "sensitivity"
    robustness_registry["passed"] = ~robustness_registry.get("sign_flip", False).fillna(False)
    robustness_registry["reportable_to_phase8"] = robustness_registry["passed"]
    robustness_registry.to_csv(FASE7_OUTPUTS / "robustness_registry.csv", index=False)

    conclusion = build_conclusion_stability_matrix(
        phase6_results=phase6_results,
        sensitivity_summary=sens_summary,
        baseline_comparisons=baseline,
        outlier_influence=outliers,
        cluster_stability=cluster,
        binary_registry=binary,
    )
    conclusion.to_csv(FASE7_OUTPUTS / "conclusion_stability_matrix.csv", index=False)

    write_phase8_reporting_contract()

    quality = run_validation()
    quality.to_csv(FASE7_OUTPUTS / "fase7_quality_checks.csv", index=False)

    manifest = {
        "fase7_version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "methodology": "inferential_comparative_observational",
        "purpose": "robustness_and_sensitivity_not_external_validation",
        "source_phase6_manifest_methodology": manifest6.get("methodology"),
        "holdout_used": False,
        "train_test_split_used": False,
        "external_validation_used": False,
        "causal_claims_allowed": False,
        "outputs": {
            "baseline_comparisons.csv": "baseline_comparisons",
            "sensitivity_analysis.csv": "group_and_case_sensitivity",
            "leave_group_out_analysis.csv": "sensitivity_not_external_test",
            "outlier_influence.csv": "country_influence",
            "cluster_stability.csv": "q4_typology_stability",
            "binary_sensitivity_registry.csv": "q2_q5_q6_binary_sensitivity_only",
            "robustness_registry.csv": "all_robustness_tests",
            "conclusion_stability_matrix.csv": "reporting_decision_matrix",
            "phase8_reporting_contract.yaml": "contract_for_phase8",
        },
        "quality_checks_passed": not (quality["status"] == "FAIL").any() if "status" in quality.columns else False,
    }
    (FASE7_OUTPUTS / "fase7_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


if __name__ == "__main__":
    main()
```

---

## Paso 14 — Implementar `api.py`

Archivo: `FASE7/src/api.py`

```python
from pathlib import Path
import pandas as pd
import json
import yaml

FASE7_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE7_ROOT / "outputs"


def load_baseline_comparisons() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "baseline_comparisons.csv")


def load_sensitivity_analysis() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "sensitivity_analysis.csv")


def load_leave_group_out_analysis() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "leave_group_out_analysis.csv")


def load_outlier_influence() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "outlier_influence.csv")


def load_cluster_stability() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "cluster_stability.csv")


def load_conclusion_stability_matrix() -> pd.DataFrame:
    return pd.read_csv(OUTPUTS / "conclusion_stability_matrix.csv")


def load_phase8_reporting_contract() -> dict:
    return yaml.safe_load((OUTPUTS / "phase8_reporting_contract.yaml").read_text(encoding="utf-8"))


def load_fase7_manifest() -> dict:
    return json.loads((OUTPUTS / "fase7_manifest.json").read_text(encoding="utf-8"))
```

---

## Paso 15 — Implementar tests

## 15.1 `tests/test_fase6_gate.py`

```python
from pathlib import Path
import pandas as pd
import json

ROOT = Path(__file__).resolve().parents[2]
F5 = ROOT / "FASE5" / "outputs" / "phase6_ready"
F6 = ROOT / "FASE6" / "outputs"


def test_fase6_manifest_ready_for_fase7():
    manifest = json.loads((F6 / "fase6_manifest.json").read_text())
    assert manifest["methodology"] == "inferential_comparative_observational"
    assert manifest["holdout_used"] is False
    assert manifest["train_test_split_used"] is False
    assert manifest["external_validation_used"] is False


def test_fase5_bundle_has_no_split():
    fm = pd.read_csv(F5 / "phase6_feature_matrix.csv")
    assert len(fm) == 43
    assert "split" not in fm.columns
    assert not (F5 / "phase6_train_test_split.csv").exists()
```

## 15.2 `tests/test_no_external_validation_language.py`

```python
from pathlib import Path

FASE7_ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_ACTIVE = [
    "test set independiente",
    "external validation",
    "validación externa",
    "predicción independiente",
    "impacto causal",
    "efecto causal",
]


def test_no_forbidden_language_in_active_phase7_docs():
    files = [FASE7_ROOT / "README.md"]
    files += list((FASE7_ROOT / "notebooks").glob("*.py"))
    for path in files:
        if not path.exists():
            continue
        txt = path.read_text(encoding="utf-8", errors="ignore").lower()
        for term in FORBIDDEN_ACTIVE:
            assert term not in txt, f"Forbidden active language '{term}' in {path}"
```

## 15.3 `tests/test_baselines_outputs.py`

```python
from pathlib import Path
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "outputs"


def test_baseline_comparisons_schema():
    df = pd.read_csv(OUT / "baseline_comparisons.csv")
    required = [
        "question_id", "outcome", "baseline_type", "metric_name",
        "baseline_metric", "estimable", "status"
    ]
    for col in required:
        assert col in df.columns
```

## 15.4 `tests/test_sensitivity_outputs.py`

```python
from pathlib import Path
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "outputs"


def test_sensitivity_analysis_schema():
    df = pd.read_csv(OUT / "sensitivity_analysis.csv")
    required = [
        "question_id", "outcome", "term", "sensitivity_type",
        "n_full", "n_reduced", "sign_flip", "stability_label"
    ]
    for col in required:
        assert col in df.columns
```

## 15.5 `tests/test_leave_group_out_not_test.py`

```python
from pathlib import Path
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "outputs"


def test_leave_group_out_is_not_external_test():
    df = pd.read_csv(OUT / "leave_group_out_analysis.csv")
    assert "external_validation_used" in df.columns
    assert df["external_validation_used"].fillna(False).eq(False).all()
    assert "validation_scope" in df.columns
    assert df["validation_scope"].astype(str).str.contains("not_external_test", na=False).all()
```

## 15.6 `tests/test_conclusion_stability_matrix.py`

```python
from pathlib import Path
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "outputs"


def test_conclusion_matrix_schema_and_labels():
    df = pd.read_csv(OUT / "conclusion_stability_matrix.csv")
    required = [
        "finding_id", "overall_robustness_label", "confidence_level",
        "reportable_in_phase8", "mandatory_limitation", "forbidden_overclaim"
    ]
    for col in required:
        assert col in df.columns

    allowed = {"stable", "directionally_stable", "fragile", "not_estimable"}
    assert set(df["overall_robustness_label"].dropna()).issubset(allowed)
```

## 15.7 `tests/test_phase8_reporting_contract.py`

```python
from pathlib import Path
import yaml

OUT = Path(__file__).resolve().parents[1] / "outputs"


def test_phase8_reporting_contract_exists_and_forbids_overclaim():
    path = OUT / "phase8_reporting_contract.yaml"
    assert path.exists()
    c = yaml.safe_load(path.read_text())
    assert c["external_validation_used"] is False
    assert c["causal_claims_allowed"] is False
    assert "forbidden_language" in c
```

## 15.8 `tests/test_fase7_manifest.py`

```python
from pathlib import Path
import json

OUT = Path(__file__).resolve().parents[1] / "outputs"


def test_fase7_manifest_methodology():
    manifest = json.loads((OUT / "fase7_manifest.json").read_text())
    assert manifest["methodology"] == "inferential_comparative_observational"
    assert manifest["holdout_used"] is False
    assert manifest["train_test_split_used"] is False
    assert manifest["external_validation_used"] is False
    assert manifest["causal_claims_allowed"] is False
```

---

## Paso 16 — README de Fase 7

Crear o reemplazar `FASE7/README.md` con esta estructura:

```markdown
# Fase 7 — Robustez y Sensibilidad

## Propósito

Fase 7 evalúa la robustez científica de los resultados de Fase 6. No crea un test externo, no reentrena modelos para mejorar performance y no convierte asociaciones observacionales en causalidad.

## Inputs

- Fase 5: feature matrix, membership, contrato metodológico.
- Fase 6: resultados Q1–Q6, manifest y scores.

## Outputs

| Archivo | Significado | No debe interpretarse como |
|---|---|---|
| baseline_comparisons.csv | Valor incremental frente a baselines | prueba causal |
| sensitivity_analysis.csv | Robustez ante exclusiones | validación externa |
| leave_group_out_analysis.csv | Sensibilidad leave-group-out | test set |
| outlier_influence.csv | Influencia de países | criterio para borrar outliers |
| cluster_stability.csv | Estabilidad tipológica Q4 | accuracy predictiva |
| conclusion_stability_matrix.csv | Matriz de hallazgos reportables | verdad causal |
| phase8_reporting_contract.yaml | Reglas para Fase 8 | informe político final |

## Cómo ejecutar

```bash
cd F5_F8_MVP
python3 -m FASE7.src.run_all
python3 -m pytest FASE7/tests -q
```

## Lenguaje permitido

- asociación ajustada
- robustez
- sensibilidad
- estabilidad de conclusión
- hallazgo frágil
- posicionamiento descriptivo

## Lenguaje prohibido

- test set independiente
- validación externa
- predicción independiente
- impacto causal
- prueba causal
```

---

## Paso 17 — Notebook Fase 7

Crear `FASE7/notebooks/generate_notebook.py` para producir `07_robustness_sensitivity.ipynb`.

El notebook debe tener secciones:

```text
1. Contrato metodológico recibido
2. Gate Fase 6 -> Fase 7
3. Baselines: trivial, controles, modelo completo
4. Sensitivity analysis por grupos
5. Leave-group-out como sensibilidad, no test externo
6. Influencia de outliers
7. Estabilidad de clusters Q4
8. Registro de sensibilidad binaria Q2/Q5/Q6
9. Matriz de estabilidad de conclusiones
10. Contrato hacia Fase 8
11. Limitaciones
```

Primera celda Markdown obligatoria:

```markdown
# Fase 7 — Robustez y sensibilidad

Esta fase no realiza validación externa ni usa test set independiente. Evalúa la estabilidad de los hallazgos de Fase 6 mediante baselines, exclusiones de grupos, outliers y leave-group-out tratados como sensibilidad interna.
```

---

## Paso 18 — Comandos finales de ejecución

Desde raíz del MVP:

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP

# 1. Ejecutar Fase 7
python3 -m FASE7.src.run_all

# 2. Ejecutar tests
python3 -m pytest FASE7/tests -q

# 3. Buscar lenguaje prohibido
rg -n "test set independiente|external validation|validación externa|predicción independiente|impacto causal|efecto causal|train/test|holdout" FASE7 || true

# 4. Verificar outputs principales
python3 - <<'PY'
from pathlib import Path
import pandas as pd
import json
import yaml

out = Path("FASE7/outputs")
required = [
    "baseline_comparisons.csv",
    "sensitivity_analysis.csv",
    "leave_group_out_analysis.csv",
    "outlier_influence.csv",
    "cluster_stability.csv",
    "binary_sensitivity_registry.csv",
    "robustness_registry.csv",
    "conclusion_stability_matrix.csv",
    "phase8_reporting_contract.yaml",
    "fase7_manifest.json",
]
for fname in required:
    assert (out / fname).exists(), f"Falta {fname}"

lgo = pd.read_csv(out / "leave_group_out_analysis.csv")
assert lgo["external_validation_used"].fillna(False).eq(False).all()
assert lgo["validation_scope"].astype(str).str.contains("not_external_test", na=False).all()

cm = pd.read_csv(out / "conclusion_stability_matrix.csv")
assert "overall_robustness_label" in cm.columns
assert "confidence_level" in cm.columns
assert "reportable_in_phase8" in cm.columns

manifest = json.loads((out / "fase7_manifest.json").read_text())
assert manifest["methodology"] == "inferential_comparative_observational"
assert manifest["external_validation_used"] is False
assert manifest["causal_claims_allowed"] is False

contract = yaml.safe_load((out / "phase8_reporting_contract.yaml").read_text())
assert contract["external_validation_used"] is False
assert contract["causal_claims_allowed"] is False

print("PASS: Fase 7 implementada correctamente")
PY
```

---

## 19. Criterios de aceptación de Fase 7

Fase 7 se considera completa solo si cumple todo lo siguiente:

### 19.1 Gate de entrada

- [ ] Auditoría Fase 6 aprobada o aprobada con observaciones.
- [ ] Manifest Fase 6 declara metodología inferencial.
- [ ] `holdout_used = false`.
- [ ] `train_test_split_used = false`.
- [ ] `external_validation_used = false`.
- [ ] `phase6_feature_matrix.csv` no contiene `split`.
- [ ] `phase6_analysis_sample_membership.csv` tiene 43 países.

### 19.2 Implementación

- [ ] Existe `FASE7/config/robustness_plan.yaml`.
- [ ] Existe `FASE7/config/sensitivity_groups.yaml`.
- [ ] Existe `FASE7/config/baseline_specs.yaml`.
- [ ] Existe `FASE7/config/stability_thresholds.yaml`.
- [ ] Existe `FASE7/src/run_all.py`.
- [ ] Existe `FASE7/src/validate.py`.
- [ ] Existe `FASE7/src/api.py`.

### 19.3 Outputs

- [ ] `baseline_comparisons.csv` generado.
- [ ] `sensitivity_analysis.csv` generado.
- [ ] `leave_group_out_analysis.csv` generado.
- [ ] `outlier_influence.csv` generado.
- [ ] `cluster_stability.csv` generado.
- [ ] `binary_sensitivity_registry.csv` generado.
- [ ] `robustness_registry.csv` generado.
- [ ] `conclusion_stability_matrix.csv` generado.
- [ ] `phase8_reporting_contract.yaml` generado.
- [ ] `fase7_manifest.json` generado.

### 19.4 Semántica

- [ ] Ningún output llama a Fase 7 validación externa.
- [ ] Leave-group-out está etiquetado como sensibilidad.
- [ ] Ningún output usa `split`.
- [ ] Ningún output afirma causalidad.
- [ ] Sensibilidad binaria Q2/Q5/Q6 queda marcada como sensibilidad.

### 19.5 Tests

- [ ] `pytest FASE7/tests -q` pasa.
- [ ] Tests comprueban no external validation.
- [ ] Tests comprueban matriz de conclusiones.
- [ ] Tests comprueban contrato hacia Fase 8.

### 19.6 Reporting readiness

- [ ] `conclusion_stability_matrix.csv` tiene `reportable_in_phase8`.
- [ ] Cada hallazgo reportable tiene limitación obligatoria.
- [ ] Cada hallazgo tiene `confidence_level`.
- [ ] `phase8_reporting_contract.yaml` lista lenguaje permitido y prohibido.

---

## 20. Errores que obligan a rechazar Fase 7

Clasificar como `P0` y rechazar Fase 7 si ocurre cualquiera de estos casos:

1. Fase 7 se ejecuta sin Fase 6 aprobada.
2. Fase 7 crea o usa `train/test split`.
3. Fase 7 llama a leave-group-out “validación externa”.
4. Fase 7 modifica outputs de Fase 5 o Fase 6.
5. Fase 7 reporta causalidad fuerte.
6. Fase 7 elimina outliers del resultado principal sin documentarlo como sensibilidad.
7. Fase 7 no genera `conclusion_stability_matrix.csv`.
8. Fase 7 no genera `phase8_reporting_contract.yaml`.
9. Fase 7 oculta sign flips.
10. Fase 7 no permite distinguir hallazgos estables de frágiles.

Clasificar como `P1` si:

1. Algún baseline no es estimable pero está documentado.
2. Algún grupo leave-out deja N demasiado bajo.
3. ARI/NMI de clusters no se puede calcular.
4. Falta notebook, pero outputs y tests están correctos.
5. Falta score de alguna sensibilidad por missingness.

Clasificar como `P2` si:

1. Hay nomenclatura mejorable.
2. README no explica suficientemente una limitación.
3. Hay columnas extra no problemáticas.
4. Algún output tiene orden de columnas distinto al esperado.

---

## 21. Plantilla de reporte final del LLM ejecutor

Al terminar, entregar:

```text
FASE 7 — REPORTE DE IMPLEMENTACIÓN

1. Gate Fase 6 -> Fase 7
- Auditoría Fase 6: APROBADA / APROBADA_CON_OBSERVACIONES / NO ENCONTRADA
- Preflight técnico: PASS/FAIL
- Observaciones: ...

2. Archivos creados/modificados
- config/robustness_plan.yaml
- config/sensitivity_groups.yaml
- config/baseline_specs.yaml
- config/stability_thresholds.yaml
- src/_common_data.py
- src/baselines.py
- src/sensitivity.py
- src/leave_group_out.py
- src/outliers.py
- src/cluster_stability.py
- src/binary_sensitivity.py
- src/stability.py
- src/conclusion_matrix.py
- src/phase8_contract.py
- src/validate.py
- src/run_all.py
- src/api.py
- README.md
- tests/...

3. Outputs generados
- baseline_comparisons.csv: shape=(...)
- sensitivity_analysis.csv: shape=(...)
- leave_group_out_analysis.csv: shape=(...)
- outlier_influence.csv: shape=(...)
- cluster_stability.csv: shape=(...)
- binary_sensitivity_registry.csv: shape=(...)
- robustness_registry.csv: shape=(...)
- conclusion_stability_matrix.csv: shape=(...)
- phase8_reporting_contract.yaml: OK
- fase7_manifest.json: OK

4. Resumen de robustez
- Hallazgos stable: N
- Hallazgos directionally_stable: N
- Hallazgos fragile: N
- Hallazgos not_estimable: N
- Hallazgos reportables a Fase 8: N

5. Tests
- pytest FASE7/tests -q: PASS/FAIL
- Fallas restantes: ...

6. Confirmaciones metodológicas
- No train/test split: PASS
- No external validation: PASS
- No causal claims: PASS
- Leave-group-out como sensibilidad: PASS
- Sign flips reportados: PASS
- Phase8 contract generado: PASS

7. Limitaciones
- N bajo en algunos outcomes: ...
- Sensibilidades no estimables: ...
- Clusters no comparables directamente: ...
- Recomendaciones para Fase 8: ...
```

---

## 22. Filosofía final de Fase 7

La Fase 7 correcta no debe producir una narrativa más “bonita”; debe producir una narrativa más honesta.

Un hallazgo frágil no es un fracaso. Es información útil. Un hallazgo no estimable no debe inventarse. Un sign flip no debe ocultarse. Una asociación estable no debe convertirse en causalidad.

La salida ideal de Fase 7 es una matriz que permita a Fase 8 decir:

> “Este hallazgo puede comunicarse con confianza media porque mantiene dirección bajo sensibilidad, pero debe advertirse que proviene de un diseño observacional con N efectivo limitado y sin validación externa.”

Y también permita decir:

> “Este hallazgo no debe usarse como argumento político principal porque depende de excluir o incluir un pequeño grupo de países influyentes.”

Ese es el estándar que protege la credibilidad técnica y política del proyecto.

---

## 23. Prompt listo para usar con otro LLM ejecutor

```text
Actúa como LLM ejecutor técnico del proyecto Research_AI_law. Debes implementar Fase 7 de inicio a fin siguiendo estrictamente el archivo BLUEPRINT_IMPLEMENTACION_FASE7_V1_0_ROBUSTEZ_RESEARCH_AI_LAW.md.

No modifiques Fase 5 ni Fase 6. Primero verifica que Fase 6 esté auditada y aprobada. Si no lo está, detente. Si lo está, implementa Fase 7 como fase de robustez y sensibilidad, no como validación externa.

Crea la estructura FASE7/config, FASE7/src, FASE7/tests, FASE7/notebooks y FASE7/outputs. Implementa baselines, sensitivity analysis, leave-group-out, outlier influence, cluster stability, binary sensitivity registry, conclusion_stability_matrix y phase8_reporting_contract. Genera manifest. Ejecuta tests. Entrega reporte final con PASS/FAIL y shapes de outputs.

Está prohibido crear train/test split, usar holdout, llamar leave-group-out validación externa, modificar outputs de Fase 5/6, afirmar causalidad fuerte o esconder hallazgos frágiles.
```

---

**Fin del blueprint de implementación de Fase 7.**
