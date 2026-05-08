# Blueprint de auditoría meticulosa de Fase 5 v2.1+ — Research_AI_law

**Proyecto:** Research_AI_law — Boletín 16821-19 Ley Marco de IA Chile  
**Documento:** Guía de auditoría para comprobar que Fase 5 fue actualizada correctamente  
**Versión auditada esperada:** `fase5-v2.1-methodology-correction-plus`  
**Versión metodológica global esperada:** `mvp-v0.3-inferential-comparative-observational`  
**Tipo de documento:** Protocolo de verificación para LLM auditor / agente técnico / revisor metodológico  
**Fecha de emisión:** 2026-05-08  
**Modo de uso:** Solo lectura, auditoría forense, sin modificar archivos  
**Nivel de obligatoriedad:** Normativo para aceptar o rechazar el cierre de Fase 5  

---

## 0. Instrucción principal para el LLM auditor

Tu tarea es auditar la carpeta `F5_F8_MVP/FASE5/` y todos sus outputs para determinar si Fase 5 fue realmente actualizada según la nueva metodología del proyecto.

No debes implementar cambios. No debes corregir código. No debes regenerar outputs. Debes inspeccionar, ejecutar checks de lectura, revisar contratos, revisar Excel, revisar manifests, revisar tests y emitir un dictamen técnico.

La pregunta de auditoría es:

> ¿La Fase 5 quedó convertida en una fase de preparación auditable, contractual e inferencial, sin artefactos de `train/test split`, lista para entregar a Fase 6 una matriz y un contrato coherentes con un estudio observacional de asociaciones ajustadas?

La respuesta final debe ser una de estas tres:

| Dictamen | Significado |
|---|---|
| `APROBADA` | Fase 5 cumple todos los criterios bloqueantes y no contiene deuda metodológica crítica. |
| `APROBADA_CON_OBSERVACIONES` | Fase 5 cumple lo esencial, pero existen mejoras documentales o no bloqueantes. |
| `RECHAZADA` | Fase 5 conserva errores incompatibles con la nueva metodología o no puede ser auditada con evidencia suficiente. |

La auditoría debe ser meticulosa. Cada afirmación debe estar respaldada por evidencia verificable: ruta de archivo, comando ejecutado, conteo, hash, columna, hoja de Excel, bloque YAML, test o fragmento de código.

---

## 1. Principio rector de la auditoría

La Fase 5 correcta no es una etapa de modelado predictivo. Es una etapa de preparación y contrato analítico.

Por tanto, el auditor debe verificar que Fase 5:

1. congela una muestra primaria de 43 países;
2. preserva el contrato real de 46 variables observadas;
3. no crea ni exporta `train/test split`;
4. no contiene columna `split` en matrices canónicas;
5. crea `analysis_sample_membership.csv`;
6. exporta un bundle `phase6_ready` sin holdout;
7. declara explícitamente `use_holdout_test_set: false`;
8. preserva missingness y no imputa;
9. documenta cobertura, transformaciones y transformaciones no estimables;
10. evita que datos regulatorios ausentes sean convertidos silenciosamente en ceros;
11. mantiene Fase 3 y Fase 4 en modo solo lectura;
12. deja manifests y tests que impiden la regresión metodológica;
13. limpia la narrativa del Excel, README y cierre técnico;
14. entrega a Fase 6 un contrato coherente con asociaciones ajustadas y `n_effective` por outcome.

Si cualquiera de los puntos 3, 4, 5, 6, 7, 8 o 10 falla, la auditoría debe marcar `RECHAZADA`, salvo que exista justificación explícita, documentada y metodológicamente aceptable.

---

## 2. Alcance exacto de la auditoría

### 2.1 Elementos que deben auditarse

Auditar como mínimo:

```text
F5_F8_MVP/FASE5/
├── README.md
├── config/
│   ├── mvp_sample.yaml
│   ├── mvp_variables.yaml
│   ├── mvp_pipeline.yaml
│   └── mvp_decisions.yaml
├── src/
│   ├── build.py
│   ├── sample.py
│   ├── variables.py
│   ├── transform.py
│   ├── engineer.py
│   ├── phase6_bundle.py
│   ├── api.py
│   ├── validate.py
│   └── audit_excel.py
├── tests/
├── notebooks/
│   └── 05_data_preparation.ipynb
└── outputs/
    ├── feature_matrix_mvp.csv
    ├── coverage_report_mvp.csv
    ├── mvp_countries.csv
    ├── mvp_variables_catalog.csv
    ├── mvp_transform_params.csv
    ├── analysis_sample_membership.csv
    ├── MVP_AUDITABLE.xlsx
    ├── fase5_manifest.json
    ├── FASE5_CIERRE_TECNICO.md
    └── phase6_ready/
```

Auditar además el contrato global si existe:

```text
F5_F8_MVP/manifest_mvp.json
F5_F8_MVP/README.md
```

### 2.2 Elementos que NO deben modificarse

El auditor debe comprobar que Fase 5 no haya modificado:

```text
FASE3/
FASE4/
```

Si existen hashes previos o manifests, deben compararse. Si no existen, debe reportarse como observación metodológica: `hashes_previos_no_disponibles`.

### 2.3 Evidencia mínima de auditoría

El auditor debe producir una carpeta o archivo de evidencia con al menos:

```text
auditoria_fase5_v2_1_plus/
├── audit_report.md
├── audit_findings.csv
├── audit_summary.json
├── file_inventory.csv
├── forbidden_terms_scan.txt
├── output_schema_checks.json
├── excel_sheet_audit.csv
├── contract_audit.yaml
├── tests_audit.txt
└── hash_manifest_audit.json
```

Si el usuario no pidió generar archivos, al menos debe entregar esos contenidos en el informe final.

---

## 3. Severidad de hallazgos

Clasifica cada hallazgo con esta escala:

| Severidad | Nombre | Efecto en dictamen | Ejemplos |
|---|---|---|---|
| `P0` | Bloqueante metodológico | Rechaza Fase 5 | Existe columna `split`; existe `phase6_train_test_split.csv`; contrato dice `use_holdout_test_set: true`; se imputa missingness. |
| `P1` | Crítico corregible | Rechaza salvo corrección explícita | `analysis_sample_membership.csv` incompleto; faltan variables Q5/Q6; Excel contradice metodología. |
| `P2` | Mayor no bloqueante | Aprueba con observaciones | README usa lenguaje ambiguo; falta nota sobre 40 vs 46 variables; manifest incompleto. |
| `P3` | Menor | Aprueba con observaciones leves | Naming legacy sin impacto; comentarios antiguos no ejecutables. |
| `INFO` | Informativo | No afecta | Recomendaciones de mejora futura. |

Regla: un solo `P0` implica `RECHAZADA`.

---

## 4. Pre-flight de auditoría

### 4.1 Identificar raíz del proyecto

Ejecutar:

```bash
pwd
ls -la
find . -maxdepth 3 -type d | sort | sed -n '1,120p'
```

Verificar que exista:

```text
F5_F8_MVP/FASE5/
```

Si no existe, buscar rutas alternativas:

```bash
find . -type d -name FASE5 | sort
find . -type f -name 'feature_matrix_mvp.csv' | sort
```

### 4.2 Crear inventario de archivos sin modificar nada

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law || exit 1
find F5_F8_MVP/FASE5 -type f | sort > /tmp/fase5_file_inventory.txt
wc -l /tmp/fase5_file_inventory.txt
sed -n '1,200p' /tmp/fase5_file_inventory.txt
```

Criterio:

- Si faltan carpetas `config`, `src`, `tests` u `outputs`, marcar `P1`.
- Si falta `outputs/phase6_ready`, marcar `P0`.

---

## 5. Auditoría de ausencia total de `train/test split`

Esta es la auditoría más importante. Debe hacerse en código, outputs, contratos, Excel, README y notebooks.

### 5.1 Buscar artefactos prohibidos en nombres de archivo

Ejecutar:

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law || exit 1
find F5_F8_MVP/FASE5 -iname '*split*' -o -iname '*train*' -o -iname '*test*' -o -iname '*holdout*' | sort
```

Evaluación:

| Resultado | Dictamen |
|---|---|
| No aparecen archivos prohibidos | OK |
| Aparece `test_*.py` en carpeta tests | Revisar contenido; no es automáticamente error |
| Aparece `mvp_train_test_split.csv` | `P0` |
| Aparece `phase6_train_test_split.csv` | `P0` |
| Aparece archivo de documentación con `train/test` histórico | `P2` o `P1` según si induce a error |

### 5.2 Buscar términos prohibidos en código y documentación

Ejecutar:

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law || exit 1
rg -n --hidden --glob '!*.pyc' --glob '!__pycache__' \
  'train_test_split|phase6_train_test_split|mvp_train_test_split|split_col|\bsplit\b|\btrain\b|\btest\b|holdout|external validation|test set independiente|predicción independiente|independent prediction' \
  F5_F8_MVP/FASE5 || true
```

Interpretación estricta:

- `train_test_split` importado desde sklearn = `P0`.
- función `_build_split()` activa = `P0`.
- escritura de `mvp_train_test_split.csv` = `P0`.
- escritura de `phase6_train_test_split.csv` = `P0`.
- columna `split` en matriz o schema = `P0`.
- mención histórica en un changelog que dice “se eliminó split” = OK si no induce a error.
- tests que verifican ausencia de split = OK.
- palabra `test` en nombres de tests unitarios = OK.

### 5.3 Verificar que matrices canónicas no tengan columna `split`

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

paths = [
    Path('F5_F8_MVP/FASE5/outputs/feature_matrix_mvp.csv'),
    Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_feature_matrix.csv'),
    Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_schema.csv'),
]
for p in paths:
    if not p.exists():
        print('[MISSING]', p)
        continue
    df = pd.read_csv(p)
    bad_cols = [c for c in df.columns if c.lower() in {'split','train','test','holdout'}]
    print(p, 'shape=', df.shape, 'bad_cols=', bad_cols)
    if bad_cols:
        raise SystemExit(f'P0: columnas prohibidas en {p}: {bad_cols}')
print('OK: no hay columnas split/train/test/holdout en matrices canónicas')
PY
```

Criterio:

- Si falla, `RECHAZADA`.

---

## 6. Auditoría de muestra primaria de 43 países

### 6.1 Verificar `feature_matrix_mvp.csv`

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

p = Path('F5_F8_MVP/FASE5/outputs/feature_matrix_mvp.csv')
assert p.exists(), f'No existe {p}'
df = pd.read_csv(p)
print('shape:', df.shape)
print('columns_first_20:', list(df.columns[:20]))
assert len(df) == 43, f'P0: feature_matrix_mvp debe tener 43 filas, tiene {len(df)}'
assert 'iso3' in df.columns, 'P0: falta columna iso3'
assert df['iso3'].is_unique, 'P0: iso3 duplicados'
assert 'CHL' in set(df['iso3']), 'P0: Chile no está presente'
print('OK: matriz principal tiene 43 países únicos e incluye CHL')
PY
```

### 6.2 Verificar composición esperada de 43 países

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

expected = {
    'ARE','SGP','NOR','IRL','FRA','ESP','NZL','NLD','GBR','QAT',
    'AUS','ISR','BEL','CAN','CHE','SWE','AUT','KOR','HUN','DNK',
    'DEU','POL','TWN','CZE','ITA','BGR','FIN','CRI',
    'CHL','USA','CHN','IND','JPN','EST',
    'ARG','BRA','COL','MEX','PER','URY',
    'GRC','ROU','HRV'
}
actual = set(pd.read_csv('F5_F8_MVP/FASE5/outputs/feature_matrix_mvp.csv')['iso3'])
print('expected_n:', len(expected), 'actual_n:', len(actual))
print('missing:', sorted(expected - actual))
print('extra:', sorted(actual - expected))
assert actual == expected, 'P0: la muestra no coincide exactamente con los 43 países preregistrados'
print('OK: muestra coincide exactamente')
PY
```

Si el proyecto usa una lista actualizada y firmada distinta a esta, el auditor debe exigir que esté registrada en `mvp_sample.yaml` y `mvp_decisions.yaml`. Si no está firmada, `P1`.

### 6.3 Verificar `analysis_sample_membership.csv`

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

p = Path('F5_F8_MVP/FASE5/outputs/analysis_sample_membership.csv')
assert p.exists(), 'P0: falta analysis_sample_membership.csv'
df = pd.read_csv(p)
print('shape:', df.shape)
print('columns:', list(df.columns))
assert len(df) == 43, f'P0: membership debe tener 43 filas, tiene {len(df)}'
assert 'iso3' in df.columns, 'P0: membership sin iso3'
assert df['iso3'].is_unique, 'P0: iso3 duplicados en membership'
assert 'is_primary_analysis_sample' in df.columns, 'P0: falta is_primary_analysis_sample'
assert df['is_primary_analysis_sample'].astype(str).str.lower().isin(['true','1']).all(), 'P0: no todos están marcados como muestra primaria'
for bad in ['split','train','test','holdout']:
    assert bad not in [c.lower() for c in df.columns], f'P0: columna prohibida en membership: {bad}'
required_flags = [
    'is_chile_focal',
    'is_ai_leader_sensitivity',
    'is_large_ai_power_sensitivity',
    'is_latam_peer_sensitivity',
    'leave_group_region',
    'leave_group_income',
]
missing = [c for c in required_flags if c not in df.columns]
print('missing_required_flags:', missing)
assert not missing, f'P1: faltan flags de sensibilidad: {missing}'
assert df.loc[df['iso3'].eq('CHL'), 'is_chile_focal'].astype(str).str.lower().isin(['true','1']).any(), 'P0: CHL no está marcado como foco'
print('OK: membership válido')
PY
```

Criterio:

- Sin `analysis_sample_membership.csv`: `P0`.
- Menos o más de 43 filas: `P0`.
- Faltan flags de sensibilidad: `P1`.
- CHL no marcado: `P0`.

---

## 7. Auditoría de contrato Fase 5 → Fase 6

### 7.1 Existencia del contrato

Debe existir:

```text
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_modeling_contract.yaml
```

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import yaml

p = Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_modeling_contract.yaml')
assert p.exists(), 'P0: falta phase6_modeling_contract.yaml'
contract = yaml.safe_load(p.read_text())
print(contract)
PY
```

### 7.2 Campos obligatorios

El contrato debe contener, como mínimo:

```yaml
version: "0.3"
fase5_version: "2.1"
methodology: "inferential_comparative_observational"
primary_estimand: "adjusted_association"
grain: "country_iso3"
primary_key: "iso3"
sample_policy:
  n_primary_sample: 43
  use_holdout_test_set: false
  train_test_split_created: false
  split_column_present: false
  effective_n_rule: "listwise_deletion_per_model_on_required_y_x"
  primary_analysis_scope: "full_preregistered_sample_available_by_outcome"
validation_policy:
  primary_uncertainty: "bootstrap_confidence_intervals"
  internal_validation:
    - repeated_kfold_cv
  robustness_phase: "FASE7"
  external_validation_available: false
  leave_group_out_is_external_test: false
language_policy:
  allowed: [...]
  forbidden_without_extra_design: [...]
contract:
  n_rows: 43
  n_observed_core_variables: 46
  no_imputation: true
  missing_values_preserved: true
  outliers_preserved: true
  phase6_should_not_recompute_phase5: true
```

### 7.3 Validación automática del contrato

```bash
python3 - <<'PY'
from pathlib import Path
import yaml

p = Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_modeling_contract.yaml')
contract = yaml.safe_load(p.read_text())

errors = []
def check(cond, msg):
    if not cond:
        errors.append(msg)

check(contract.get('methodology') == 'inferential_comparative_observational', 'methodology incorrecta')
check(contract.get('primary_estimand') == 'adjusted_association', 'primary_estimand incorrecto')
sp = contract.get('sample_policy', {})
check(sp.get('n_primary_sample') == 43, 'n_primary_sample debe ser 43')
check(sp.get('use_holdout_test_set') is False, 'use_holdout_test_set debe ser false')
check(sp.get('train_test_split_created') is False, 'train_test_split_created debe ser false')
check(sp.get('split_column_present') is False, 'split_column_present debe ser false')
check(sp.get('effective_n_rule') == 'listwise_deletion_per_model_on_required_y_x', 'effective_n_rule incorrecta')
vp = contract.get('validation_policy', {})
check(vp.get('external_validation_available') is False, 'external_validation_available debe ser false')
check(vp.get('leave_group_out_is_external_test') is False, 'leave_group_out_is_external_test debe ser false')
ct = contract.get('contract', {})
check(ct.get('n_rows') == 43, 'contract.n_rows debe ser 43')
check(ct.get('n_observed_core_variables') == 46, 'contract.n_observed_core_variables debe ser 46')
check(ct.get('no_imputation') is True, 'no_imputation debe ser true')
check(ct.get('missing_values_preserved') is True, 'missing_values_preserved debe ser true')
check(ct.get('outliers_preserved') is True, 'outliers_preserved debe ser true')

if errors:
    print('P0/P1 contract errors:')
    for e in errors:
        print('-', e)
    raise SystemExit(1)
print('OK: contrato Fase 5 -> Fase 6 cumple metodología')
PY
```

Criterio:

- `use_holdout_test_set` distinto de `false`: `P0`.
- `split_column_present` distinto de `false`: `P0`.
- `n_observed_core_variables` no especificado o distinto de 46: `P1`.

---

## 8. Auditoría de outputs prohibidos y outputs obligatorios

### 8.1 Outputs prohibidos

No deben existir:

```text
F5_F8_MVP/FASE5/outputs/mvp_train_test_split.csv
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_train_test_split.csv
```

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
forbidden = [
    Path('F5_F8_MVP/FASE5/outputs/mvp_train_test_split.csv'),
    Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_train_test_split.csv'),
]
for p in forbidden:
    print(p, 'exists=', p.exists())
    assert not p.exists(), f'P0: archivo prohibido existe: {p}'
print('OK: no existen outputs prohibidos de split')
PY
```

### 8.2 Outputs obligatorios

Deben existir:

```text
F5_F8_MVP/FASE5/outputs/feature_matrix_mvp.csv
F5_F8_MVP/FASE5/outputs/coverage_report_mvp.csv
F5_F8_MVP/FASE5/outputs/mvp_countries.csv
F5_F8_MVP/FASE5/outputs/mvp_variables_catalog.csv
F5_F8_MVP/FASE5/outputs/mvp_transform_params.csv
F5_F8_MVP/FASE5/outputs/analysis_sample_membership.csv
F5_F8_MVP/FASE5/outputs/MVP_AUDITABLE.xlsx
F5_F8_MVP/FASE5/outputs/fase5_manifest.json
F5_F8_MVP/FASE5/outputs/FASE5_CIERRE_TECNICO.md
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_feature_matrix.csv
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_schema.csv
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_schema.json
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_variables_catalog.csv
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_transform_params.csv
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_column_groups.yaml
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_missingness_by_column.csv
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_missingness_by_country.csv
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_llm_context.json
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_modeling_contract.yaml
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_analysis_sample_membership.csv
F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_ready_manifest.json
```

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
required = [
'F5_F8_MVP/FASE5/outputs/feature_matrix_mvp.csv',
'F5_F8_MVP/FASE5/outputs/coverage_report_mvp.csv',
'F5_F8_MVP/FASE5/outputs/mvp_countries.csv',
'F5_F8_MVP/FASE5/outputs/mvp_variables_catalog.csv',
'F5_F8_MVP/FASE5/outputs/mvp_transform_params.csv',
'F5_F8_MVP/FASE5/outputs/analysis_sample_membership.csv',
'F5_F8_MVP/FASE5/outputs/MVP_AUDITABLE.xlsx',
'F5_F8_MVP/FASE5/outputs/fase5_manifest.json',
'F5_F8_MVP/FASE5/outputs/FASE5_CIERRE_TECNICO.md',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_feature_matrix.csv',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_schema.csv',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_schema.json',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_variables_catalog.csv',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_transform_params.csv',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_column_groups.yaml',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_missingness_by_column.csv',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_missingness_by_country.csv',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_llm_context.json',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_modeling_contract.yaml',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_analysis_sample_membership.csv',
'F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_ready_manifest.json',
]
missing = [p for p in required if not Path(p).exists()]
print('missing:', missing)
if missing:
    raise SystemExit('P1/P0: faltan outputs obligatorios')
print('OK: todos los outputs obligatorios existen')
PY
```

Criterio:

- Falta `phase6_feature_matrix.csv`: `P0`.
- Falta `phase6_modeling_contract.yaml`: `P0`.
- Falta `phase6_analysis_sample_membership.csv`: `P0`.
- Falta manifest: `P1`.
- Falta cierre técnico: `P2` si todo lo demás está correcto.

---

## 9. Auditoría de 46 variables observadas y nomenclatura 40/46

### 9.1 Verificar catálogo de variables

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

paths = [
    Path('F5_F8_MVP/FASE5/outputs/mvp_variables_catalog.csv'),
    Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_variables_catalog.csv'),
]
for p in paths:
    assert p.exists(), f'Falta {p}'
    df = pd.read_csv(p)
    print('\n', p, df.shape)
    print(df.columns.tolist())
    var_col = 'variable_matriz' if 'variable_matriz' in df.columns else 'variable'
    n = df[var_col].nunique()
    print('n_variables:', n)
    assert n == 46, f'P1: catálogo debe registrar 46 variables observadas, registra {n}'
print('OK: catálogos registran 46 variables observadas')
PY
```

### 9.2 Verificar que Q5/Q6 están preservadas

El auditor debe confirmar que las variables Q5/Q6 no desaparecieron por aplicar una versión antigua del plan.

Variables mínimas esperadas:

```text
anthropic_usage_pct
anthropic_collaboration_pct
oxford_ind_adoption_emerging_tech
oxford_public_sector_adoption
oxford_e_government_delivery
oxford_government_digital_policy
oxford_ind_data_governance
oxford_governance_ethics
oecd_2_indigo_oecd_indigo_score
oecd_4_digital_gov_oecd_digital_gov_overall
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
from pathlib import Path

expected = {
'anthropic_usage_pct',
'anthropic_collaboration_pct',
'oxford_ind_adoption_emerging_tech',
'oxford_public_sector_adoption',
'oxford_e_government_delivery',
'oxford_government_digital_policy',
'oxford_ind_data_governance',
'oxford_governance_ethics',
'oecd_2_indigo_oecd_indigo_score',
'oecd_4_digital_gov_oecd_digital_gov_overall',
}
fm = pd.read_csv('F5_F8_MVP/FASE5/outputs/feature_matrix_mvp.csv')
cols = set(fm.columns)
missing = sorted(expected - cols)
print('missing_q5_q6:', missing)
assert not missing, f'P1: faltan variables Q5/Q6 esperadas: {missing}'
print('OK: Q5/Q6 preservadas')
PY
```

### 9.3 Auditar nombres legacy “40”

Buscar:

```bash
rg -n 'Variables_40|Matriz_40|40 variables|TOTAL = 40|46 variables|46 variables observadas' F5_F8_MVP/FASE5 || true
```

Criterio:

- Si aparecen nombres legacy como `Variables_40` pero están documentados como “nombre heredado; contenido real = 46 variables observadas”: `P3`.
- Si el README o cierre técnico afirma que el contrato final tiene 40 variables y omite Q5/Q6: `P1`.
- Si el contrato declara `n_observed_core_variables: 46`: OK.

---

## 10. Auditoría de missingness, cero imputación y transformaciones

### 10.1 Verificar que no se imputan valores faltantes

Buscar patrones peligrosos:

```bash
rg -n 'fillna\(|SimpleImputer|KNNImputer|IterativeImputer|interpolate\(|bfill\(|ffill\(|replace\(.*nan|dropna\(.*inplace' F5_F8_MVP/FASE5/src F5_F8_MVP/FASE5/config || true
```

Interpretación:

- `fillna(0)` sobre variables raw sin justificación: `P0`.
- `fillna(0)` solo para cálculo de flags derivados con columna de cobertura/missingness explícita: revisar; puede ser OK con justificación.
- `dropna()` en Fase 5 para eliminar países o variables: `P0` salvo validación no destructiva.
- `dropna()` solo para calcular estadísticas auxiliares: OK si no altera outputs.

### 10.2 Comparar missingness entre matriz principal y bundle

```bash
python3 - <<'PY'
import pandas as pd
from pathlib import Path

fm = pd.read_csv('F5_F8_MVP/FASE5/outputs/feature_matrix_mvp.csv')
bundle = pd.read_csv('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_feature_matrix.csv')
common = [c for c in fm.columns if c in bundle.columns]
problems = []
for c in common:
    if fm[c].isna().sum() != bundle[c].isna().sum():
        problems.append((c, int(fm[c].isna().sum()), int(bundle[c].isna().sum())))
print('missingness_differences:', problems[:30], 'n=', len(problems))
assert not problems, 'P1/P0: missingness cambió entre feature_matrix y phase6_feature_matrix'
print('OK: missingness preservado entre matriz principal y bundle')
PY
```

### 10.3 Verificar reporte de missingness por columna y país

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

col = Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_missingness_by_column.csv')
cty = Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_missingness_by_country.csv')
assert col.exists(), 'P1: falta phase6_missingness_by_column.csv'
assert cty.exists(), 'P1: falta phase6_missingness_by_country.csv'
col_df = pd.read_csv(col)
cty_df = pd.read_csv(cty)
print('column_missingness shape:', col_df.shape)
print('country_missingness shape:', cty_df.shape)
for required in ['column','n_missing','pct_missing']:
    assert required in col_df.columns, f'P1: falta {required} en missingness_by_column'
for required in ['iso3','n_missing','pct_missing']:
    assert required in cty_df.columns, f'P1: falta {required} en missingness_by_country'
print('OK: reportes de missingness existen y tienen schema básico')
PY
```

### 10.4 Auditar transformaciones no estimables

Debe existir una política explícita para casos como MAD=0 o derivadas degeneradas.

Buscar:

```bash
rg -n 'zero_mad|MAD|mad|not_estimable|degenerate|no_estimable|transform.*estimable|exclude_from_primary_modeling' F5_F8_MVP/FASE5 || true
```

Verificar `mvp_transform_params.csv`:

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

p = Path('F5_F8_MVP/FASE5/outputs/mvp_transform_params.csv')
assert p.exists(), 'P1: falta mvp_transform_params.csv'
df = pd.read_csv(p)
print(df.shape)
print(df.columns.tolist())
expected_cols = {'variable','transform','status'}
missing = expected_cols - set(df.columns)
assert not missing, f'P1: mvp_transform_params.csv debe incluir {missing}'
status_values = set(df['status'].astype(str).str.lower())
print('status_values:', sorted(status_values))
allowed = {'ok','not_estimable','zero_mad_or_not_estimable','skipped','not_applicable'}
assert status_values & allowed, 'P2: no se observa política explícita de estado de transformaciones'
print('OK: transformaciones documentan status')
PY
```

Criterio:

- Si una transformación no estimable se rellena con 0 y queda en grupos de modelado sin flag: `P1`.
- Si se marca como `zero_mad_or_not_estimable` y se excluye de modelado primario: OK.

---

## 11. Auditoría especial de agregados regulatorios y `fillna(0)`

Esta auditoría es crítica porque la investigación detectó el riesgo de convertir ausencia de datos regulatorios en ceros interpretables como ausencia de regulación.

### 11.1 Principio correcto

No todo missing regulatorio significa `0`.

Debe distinguirse entre:

| Caso | Tratamiento correcto |
|---|---|
| Fuente confirma ausencia de regulación | Puede codificarse como `0`. |
| Fuente no tiene dato / no observado / no disponible | Debe mantenerse como `NaN` o marcarse en `n_missing_regulatory_inputs`. |
| Variable binaria observada con 0/1 completo | Puede sumarse directamente. |
| Variable binaria incompleta | Debe calcularse agregado con denominador observado y flag de cobertura. |

### 11.2 Buscar uso de `fillna(0)` en ingeniería regulatoria

```bash
rg -n 'fillna\(0\)|fillna\(0\.0\)|fillna\(False\)' F5_F8_MVP/FASE5/src/engineer.py F5_F8_MVP/FASE5/src/transform.py F5_F8_MVP/FASE5/src/build.py F5_F8_MVP/FASE5/src/phase6_bundle.py || true
```

Evaluación:

- Si aparece `fillna(0)` en cálculo de `n_binding`, `n_non_binding`, `n_hybrid` sin columnas auxiliares de cobertura, marcar `P0/P1` según impacto.
- Si aparece con comentario explícito y columnas `n_regulatory_inputs_observed`, `n_regulatory_inputs_missing`, `regulatory_coverage_ratio`, puede ser OK.

### 11.3 Verificar columnas de cobertura regulatoria

Deben existir, idealmente:

```text
n_regulatory_inputs_observed
n_regulatory_inputs_missing
regulatory_coverage_ratio
n_binding_observed
n_non_binding_observed
n_hybrid_observed
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
fm = pd.read_csv('F5_F8_MVP/FASE5/outputs/feature_matrix_mvp.csv')
recommended = [
'n_regulatory_inputs_observed',
'n_regulatory_inputs_missing',
'regulatory_coverage_ratio',
'n_binding_observed',
'n_non_binding_observed',
'n_hybrid_observed',
]
missing = [c for c in recommended if c not in fm.columns]
print('missing_regulatory_coverage_columns:', missing)
if missing:
    raise SystemExit('P1: faltan columnas recomendadas para evitar interpretar missing regulatorio como cero')
print('OK: agregados regulatorios incluyen cobertura/missingness')
PY
```

Si el diseño final opta por no crear esas columnas, debe existir explicación en `FASE5_CIERRE_TECNICO.md` y `phase6_modeling_contract.yaml`. Sin explicación, `P1`.

### 11.4 Chequeo de países con datos regulatorios ausentes

```bash
python3 - <<'PY'
import pandas as pd
fm = pd.read_csv('F5_F8_MVP/FASE5/outputs/feature_matrix_mvp.csv')
if 'n_regulatory_inputs_missing' in fm.columns:
    flagged = fm[fm['n_regulatory_inputs_missing'] > 0][['iso3','n_regulatory_inputs_missing']]
    print('countries_with_missing_regulatory_inputs:', flagged.to_dict('records'))
else:
    print('WARNING: no existe n_regulatory_inputs_missing')
PY
```

Criterio:

- Si hay países con missing regulatorio y sus agregados quedan en cero sin flag: `P0` si afecta columnas de modelado; `P1` si solo afecta documentación.

---

## 12. Auditoría del bundle `phase6_ready`

### 12.1 Verificar consistencia entre outputs de Fase 5 y bundle

```bash
python3 - <<'PY'
import pandas as pd

fm = pd.read_csv('F5_F8_MVP/FASE5/outputs/feature_matrix_mvp.csv')
p6 = pd.read_csv('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_feature_matrix.csv')
print('feature_matrix:', fm.shape)
print('phase6_feature_matrix:', p6.shape)
assert len(p6) == 43, 'P0: phase6_feature_matrix debe tener 43 filas'
assert set(p6['iso3']) == set(fm['iso3']), 'P0: países difieren entre matriz Fase 5 y bundle'
assert 'split' not in p6.columns, 'P0: split en phase6_feature_matrix'
print('OK: phase6_feature_matrix consistente')
PY
```

### 12.2 Verificar schema y column groups

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd, yaml, json

schema_csv = Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_schema.csv')
schema_json = Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_schema.json')
groups_yaml = Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_column_groups.yaml')
for p in [schema_csv, schema_json, groups_yaml]:
    assert p.exists(), f'P1: falta {p}'

schema = pd.read_csv(schema_csv)
print('schema cols:', schema.columns.tolist())
assert 'column' in schema.columns, 'P1: schema debe tener columna column'
assert not schema['column'].astype(str).str.lower().isin(['split','train','test','holdout']).any(), 'P0: schema contiene columna prohibida'

groups = yaml.safe_load(groups_yaml.read_text())
print('groups keys:', list(groups.keys()))
for key in ['X1_regulatory','X2_controls','Y_Q1_investment','Y_Q2_adoption','Y_Q3_innovation']:
    assert key in groups, f'P1: falta grupo {key}'
for key, cols in groups.items():
    if isinstance(cols, list):
        bad = [c for c in cols if str(c).lower() in {'split','train','test','holdout'}]
        assert not bad, f'P0: grupos contienen columnas prohibidas {bad}'
print('OK: schema y column_groups válidos')
PY
```

### 12.3 Verificar contexto LLM

`phase6_llm_context.json` debe decir explícitamente que Fase 6 no recibe holdout.

```bash
python3 - <<'PY'
from pathlib import Path
import json
p = Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_llm_context.json')
assert p.exists(), 'P1: falta phase6_llm_context.json'
data = json.loads(p.read_text())
text = json.dumps(data, ensure_ascii=False).lower()
required = ['inferential', 'observational', 'no holdout', 'use_holdout_test_set']
print('contains:', {r: r in text for r in required})
assert 'train/test split' not in text or 'no train/test split' in text, 'P1: contexto LLM puede inducir a split'
print('OK: contexto LLM no induce holdout')
PY
```

---

## 13. Auditoría de API de Fase 5

### 13.1 Funciones obligatorias

`FASE5/src/api.py` debe exponer funciones de lectura limpias para fases posteriores:

```python
load_feature_matrix_mvp()
load_analysis_sample_membership()
load_phase6_feature_matrix()
load_phase6_schema()
load_phase6_column_groups()
load_phase6_modeling_contract()
load_phase6_ready_manifest()
load_phase6_llm_context()
load_phase6_analysis_sample_membership()
```

### 13.2 Funciones prohibidas

No debe existir función pública activa:

```python
load_train_test_split()
load_phase6_train_test_split()
get_train_test_split()
```

Buscar:

```bash
rg -n 'def load_train_test_split|def load_phase6_train_test_split|def get_train_test_split|train_test_split' F5_F8_MVP/FASE5/src/api.py F5_F8_MVP/FASE5/src || true
```

Criterio:

- Función activa que carga split: `P0`.
- Función legacy que lanza `DeprecationError` y explica migración: `P2`, aceptable temporalmente.

### 13.3 Prueba de carga vía API

```bash
python3 - <<'PY'
import sys
from pathlib import Path
root = Path('F5_F8_MVP').resolve()
sys.path.insert(0, str(root))
try:
    from FASE5.src import api
    fm = api.load_phase6_feature_matrix()
    membership = api.load_phase6_analysis_sample_membership()
    contract = api.load_phase6_modeling_contract()
    print('fm:', fm.shape)
    print('membership:', membership.shape)
    print('methodology:', contract.get('methodology'))
    assert len(fm) == 43
    assert len(membership) == 43
    assert contract.get('methodology') == 'inferential_comparative_observational'
except Exception as e:
    raise SystemExit(f'P1: API Fase 5 no permite cargar bundle limpiamente: {e}')
print('OK: API Fase 5 funcional')
PY
```

---

## 14. Auditoría del Excel `MVP_AUDITABLE.xlsx`

El Excel debe ser coherente con la nueva metodología. No basta con que los CSV estén bien; el workbook también debe dejar de hablar de `split` como modelado.

### 14.1 Listar hojas

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd
p = Path('F5_F8_MVP/FASE5/outputs/MVP_AUDITABLE.xlsx')
assert p.exists(), 'P1: falta MVP_AUDITABLE.xlsx'
xl = pd.ExcelFile(p)
print('sheets:', xl.sheet_names)
PY
```

Hojas esperadas, con nombres flexibles:

```text
0_Leer_Primero o README
3_Paises_43 o Paises
5_Variables_40 / Variables_46 / Variables
6_Matriz_40_Humana / Matriz_Humana
10_Cobertura
11_Features_Fase6 / Feature_Matrix
12_Diccionario_Cols
13_Trazabilidad
14_Transformaciones
15_Membership / Analysis_Sample_Membership
```

Criterio:

- Falta hoja de membresía analítica: `P1`.
- El Excel sigue mostrando hoja `split` o narrativa de `train/test`: `P1` o `P0` si contradice contrato.

### 14.2 Buscar columnas prohibidas en todas las hojas

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd
p = Path('F5_F8_MVP/FASE5/outputs/MVP_AUDITABLE.xlsx')
xl = pd.ExcelFile(p)
violations = []
for sheet in xl.sheet_names:
    df = xl.parse(sheet, nrows=2000)
    bad_cols = [c for c in df.columns if str(c).lower() in {'split','train','test','holdout'}]
    if bad_cols:
        violations.append((sheet, bad_cols))
print('column_violations:', violations)
if violations:
    raise SystemExit('P1/P0: Excel contiene columnas prohibidas')
print('OK: Excel no contiene columnas split/train/test/holdout')
PY
```

### 14.3 Buscar texto prohibido dentro del Excel

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd
p = Path('F5_F8_MVP/FASE5/outputs/MVP_AUDITABLE.xlsx')
xl = pd.ExcelFile(p)
terms = ['train/test', 'test set', 'holdout', 'split para modelado', 'test independiente', 'predicción independiente']
hits = []
for sheet in xl.sheet_names:
    df = xl.parse(sheet, dtype=str).fillna('')
    for term in terms:
        mask = df.apply(lambda col: col.str.lower().str.contains(term, regex=False, na=False)).any(axis=1)
        if mask.any():
            hits.append((sheet, term, int(mask.sum())))
print('text_hits:', hits)
if hits:
    raise SystemExit('P1: Excel contiene narrativa prohibida o legacy no corregida')
print('OK: Excel sin narrativa prohibida')
PY
```

### 14.4 Verificar hoja de transformaciones

```bash
python3 - <<'PY'
import pandas as pd
from pathlib import Path
p = Path('F5_F8_MVP/FASE5/outputs/MVP_AUDITABLE.xlsx')
xl = pd.ExcelFile(p)
transform_sheets = [s for s in xl.sheet_names if 'Transform' in s or 'transform' in s]
print('transform_sheets:', transform_sheets)
assert transform_sheets, 'P1: Excel debe tener hoja de transformaciones'
for s in transform_sheets:
    df = xl.parse(s)
    print(s, df.shape, df.columns.tolist())
    cols_lower = [str(c).lower() for c in df.columns]
    assert any('status' in c or 'estado' in c for c in cols_lower), 'P2: hoja transformaciones debe incluir estado/status'
print('OK: Excel documenta transformaciones')
PY
```

---

## 15. Auditoría de manifests y hashes

### 15.1 `fase5_manifest.json`

Debe contener:

```json
{
  "fase5_version": "2.1",
  "methodology": "inferential_comparative_observational",
  "primary_estimand": "adjusted_association",
  "holdout_used": false,
  "train_test_split_created": false,
  "split_column_present": false,
  "n_primary_sample": 43,
  "n_observed_core_variables": 46,
  "no_imputation": true,
  "missing_values_preserved": true,
  "outputs": {...},
  "hashes": {...}
}
```

Validar:

```bash
python3 - <<'PY'
from pathlib import Path
import json
p = Path('F5_F8_MVP/FASE5/outputs/fase5_manifest.json')
assert p.exists(), 'P1: falta fase5_manifest.json'
data = json.loads(p.read_text())
checks = {
    'methodology': data.get('methodology') == 'inferential_comparative_observational',
    'holdout_used_false': data.get('holdout_used') is False,
    'train_test_split_created_false': data.get('train_test_split_created') is False,
    'split_column_present_false': data.get('split_column_present') is False,
    'n_primary_sample_43': data.get('n_primary_sample') == 43,
    'n_observed_core_variables_46': data.get('n_observed_core_variables') == 46,
    'no_imputation_true': data.get('no_imputation') is True,
}
print(checks)
failed = [k for k,v in checks.items() if not v]
assert not failed, f'P1/P0: manifest falla checks: {failed}'
print('OK: manifest coherente')
PY
```

### 15.2 `phase6_ready_manifest.json`

Validar que liste todos los archivos del bundle y sus hashes.

```bash
python3 - <<'PY'
from pathlib import Path
import json
p = Path('F5_F8_MVP/FASE5/outputs/phase6_ready/phase6_ready_manifest.json')
assert p.exists(), 'P1: falta phase6_ready_manifest.json'
data = json.loads(p.read_text())
text = json.dumps(data).lower()
assert 'phase6_train_test_split' not in text, 'P0: manifest menciona phase6_train_test_split'
assert 'phase6_analysis_sample_membership' in text, 'P0: manifest no registra membership'
assert 'phase6_modeling_contract' in text, 'P0: manifest no registra contrato'
print('OK: manifest phase6_ready correcto')
PY
```

---

## 16. Auditoría de tests automáticos

### 16.1 Tests que deben existir

Como mínimo:

```text
FASE5/tests/test_no_train_test_split.py
FASE5/tests/test_phase6_contract.py
FASE5/tests/test_analysis_sample_membership.py
FASE5/tests/test_no_imputation.py
FASE5/tests/test_sample_integrity.py
FASE5/tests/test_variables_catalog_46.py
FASE5/tests/test_phase6_bundle_integrity.py
FASE5/tests/test_excel_methodology_clean.py
FASE5/tests/test_regulatory_missingness_policy.py
```

Ejecutar:

```bash
find F5_F8_MVP/FASE5/tests -maxdepth 1 -type f -name 'test_*.py' -printf '%f\n' | sort
```

Si falta un test, no necesariamente rechaza, pero debe evaluarse si otra prueba cubre el mismo riesgo.

### 16.2 Tests prohibidos o legacy

No debe existir un test que exija 34/9 train/test.

Buscar:

```bash
rg -n '34|9|train|test|split|phase6_train_test_split|mvp_train_test_split' F5_F8_MVP/FASE5/tests || true
```

Interpretación:

- Si el test verifica ausencia de esos términos: OK.
- Si el test espera `34 train / 9 test`: `P0`.

### 16.3 Ejecutar tests

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP/FASE5 || exit 1
python3 -m pytest tests/ -q
```

Criterio:

- Si falla un test anti-split, `P0`.
- Si falla un test de documentación, `P2` o `P1` según contenido.
- Si no hay tests, `P1` mínimo; `P0` si no hay evidencia alternativa suficiente.

---

## 17. Auditoría de documentación y narrativa

### 17.1 README de Fase 5

Debe decir explícitamente:

- Fase 5 es preparación auditable y contractual.
- No hay `train/test split`.
- La muestra primaria es N=43.
- El contrato real es 46 variables observadas.
- Fase 6 usa muestra completa disponible por outcome.
- Fase 7 hace sensibilidad, no validación externa.
- No hay causalidad fuerte.

Buscar:

```bash
rg -n 'preparación auditable|contractual|inferential|observational|observacional|43|46|no train|sin train|sin holdout|analysis_sample_membership|asociación ajustada|n_effective' F5_F8_MVP/FASE5/README.md || true
```

### 17.2 Cierre técnico de Fase 5

`FASE5_CIERRE_TECNICO.md` debe incluir:

1. resumen de cambios v2.1+;
2. lista de outputs generados;
3. confirmación de ausencia de split;
4. confirmación de N=43;
5. confirmación de 46 variables observadas;
6. política de missingness;
7. política de transformaciones no estimables;
8. política de agregados regulatorios y missingness;
9. hash de outputs;
10. instrucciones para Fase 6;
11. limitaciones conocidas.

Validar:

```bash
rg -n 'N=43|43 países|46 variables|sin split|no split|analysis_sample_membership|missingness|zero_mad|not_estimable|regulatory|hash|Fase 6' F5_F8_MVP/FASE5/outputs/FASE5_CIERRE_TECNICO.md || true
```

Criterio:

- Falta cierre técnico: `P2` si todo lo demás OK; `P1` si además hay dudas.
- Cierre técnico contradice contrato: `P1` o `P0`.

---

## 18. Auditoría de notebook `05_data_preparation.ipynb`

El notebook debe ser de verificación visual, no de modelado.

### 18.1 Buscar términos prohibidos en notebook

```bash
python3 - <<'PY'
from pathlib import Path
import json
p = Path('F5_F8_MVP/FASE5/notebooks/05_data_preparation.ipynb')
if not p.exists():
    raise SystemExit('P2: falta notebook 05_data_preparation.ipynb')
nb = json.loads(p.read_text())
text = '\n'.join(''.join(cell.get('source', [])) for cell in nb.get('cells', []))
terms = ['train_test_split', 'mvp_train_test_split', 'phase6_train_test_split', 'test set independiente', 'holdout externo']
hits = {t: text.lower().count(t.lower()) for t in terms}
print(hits)
if any(v > 0 for v in hits.values()):
    raise SystemExit('P1: notebook contiene términos prohibidos')
print('OK: notebook sin narrativa prohibida')
PY
```

### 18.2 Verificar contenido mínimo

Debe tener secciones sobre:

- muestra 43 países;
- variables 46;
- cobertura;
- missingness;
- transformaciones;
- membership;
- contrato Fase 6;
- confirmación no split.

Buscar encabezados:

```bash
python3 - <<'PY'
import json
from pathlib import Path
p = Path('F5_F8_MVP/FASE5/notebooks/05_data_preparation.ipynb')
if not p.exists():
    raise SystemExit('P2: falta notebook')
nb = json.loads(p.read_text())
text = '\n'.join(''.join(cell.get('source', [])) for cell in nb.get('cells', [])).lower()
required = ['43', '46', 'cobertura', 'missing', 'transform', 'membership', 'contract', 'split']
print({r: r in text for r in required})
PY
```

La palabra `split` puede aparecer solo para decir que no existe.

---

## 19. Auditoría de compatibilidad con Fase 6

La Fase 5 se aprueba solo si Fase 6 puede consumirla sin reinterpretar la muestra.

### 19.1 Simular carga mínima de Fase 6

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd, yaml, json

bundle = Path('F5_F8_MVP/FASE5/outputs/phase6_ready')
fm = pd.read_csv(bundle / 'phase6_feature_matrix.csv')
membership = pd.read_csv(bundle / 'phase6_analysis_sample_membership.csv')
contract = yaml.safe_load((bundle / 'phase6_modeling_contract.yaml').read_text())
groups = yaml.safe_load((bundle / 'phase6_column_groups.yaml').read_text())

assert len(fm) == 43
assert len(membership) == 43
assert set(fm['iso3']) == set(membership['iso3'])
assert contract['sample_policy']['use_holdout_test_set'] is False
assert 'split' not in fm.columns

for group_name, cols in groups.items():
    if isinstance(cols, list):
        missing = [c for c in cols if c not in fm.columns]
        if missing:
            print('group_missing_columns', group_name, missing)
            raise SystemExit(f'P1: column_groups referencia columnas ausentes en {group_name}')
print('OK: Fase 6 puede cargar bundle sin split')
PY
```

### 19.2 Verificar `n_effective` posible por outcome

Fase 5 no estima modelos, pero debe permitir que Fase 6 calcule `n_effective`.

```bash
python3 - <<'PY'
import pandas as pd, yaml
from pathlib import Path
bundle = Path('F5_F8_MVP/FASE5/outputs/phase6_ready')
fm = pd.read_csv(bundle / 'phase6_feature_matrix.csv')
groups = yaml.safe_load((bundle / 'phase6_column_groups.yaml').read_text())

for y_group in ['Y_Q1_investment','Y_Q2_adoption','Y_Q3_innovation','Y_Q5_population_usage','Y_Q6_public_sector']:
    if y_group not in groups:
        print('WARNING missing group', y_group)
        continue
    for y in groups[y_group]:
        if y in fm.columns:
            n = fm[y].notna().sum()
            print(y_group, y, 'n_non_missing=', int(n))
        else:
            print('MISSING_COLUMN', y_group, y)
PY
```

Criterio:

- Si grupos Q5/Q6 faltan sin justificación: `P1`.
- Si todos los outcomes clave tienen N extremadamente bajo y no está documentado: `P1`.

---

## 20. Auditoría de decisiones metodológicas

### 20.1 `mvp_decisions.yaml`

Debe registrar decisiones explícitas:

```yaml
F5-V2.1-001: eliminar train/test split
F5-V2.1-002: reemplazar split por analysis_sample_membership.csv
F5-V2.1-003: contrato declara use_holdout_test_set=false
F5-V2.1-004: mantener 43 países y 46 variables observadas
F5-V2.1-005: preservar missingness y cero imputación
F5-V2.1-006: documentar transformaciones no estimables
F5-V2.1-007: no interpretar missing regulatorio como cero sin evidencia
```

Validar:

```bash
rg -n 'F5-V2.1|train/test|analysis_sample_membership|use_holdout_test_set|43|46|missing|imput|zero_mad|regulatorio|regulatory' F5_F8_MVP/FASE5/config/mvp_decisions.yaml || true
```

Criterio:

- Falta decisión anti-split: `P1`.
- Falta decisión de missing regulatorio: `P1`.
- Decisión dice “train/test aceptado”: `P0`.

---

## 21. Auditoría de inmutabilidad de Fase 3 y Fase 4

### 21.1 Revisar código por escrituras fuera de Fase 5

Buscar:

```bash
rg -n 'to_csv\(|to_excel\(|open\(.*w|write_text\(|mkdir\(|unlink\(|remove\(|rmtree\(' F5_F8_MVP/FASE5/src || true
```

El auditor debe revisar si alguna escritura apunta a:

```text
FASE3/
FASE4/
```

Criterio:

- Escritura en Fase 3 o Fase 4: `P0`.
- Lectura desde Fase 3/Fase 4 vía API: OK.

### 21.2 Verificar manifiestos de hashes

Si existen manifests con hashes previos:

```bash
find FASE3 FASE4 -maxdepth 3 -iname '*manifest*' -o -iname '*hash*' | sort
```

Comparar con `fase5_manifest.json` o `manifest_mvp.json`.

Si no hay hashes, registrar:

```text
OBSERVACION: no fue posible verificar inmutabilidad por hash porque no existe manifest previo accesible.
```

No rechazar automáticamente, salvo que haya evidencia de escritura.

---

## 22. Matriz de criterios de aceptación

### 22.1 Criterios bloqueantes P0

Fase 5 se rechaza si ocurre cualquiera:

- Existe `mvp_train_test_split.csv`.
- Existe `phase6_train_test_split.csv`.
- Existe columna `split` en `feature_matrix_mvp.csv`.
- Existe columna `split` en `phase6_feature_matrix.csv`.
- El contrato declara `use_holdout_test_set: true`.
- El contrato declara `train_test_split_created: true`.
- La muestra no tiene 43 países.
- Chile no está en la muestra.
- Falta `analysis_sample_membership.csv`.
- Falta `phase6_modeling_contract.yaml`.
- Se imputan missing values en variables originales.
- Se convierten datos regulatorios ausentes a cero sin bandera/documentación.
- Fase 5 escribe en Fase 3 o Fase 4.
- Fase 5 entrega a Fase 6 un bundle que no puede cargarse.

### 22.2 Criterios críticos P1

Fase 5 debe corregirse antes de cierre formal si:

- Falta hoja de membership en Excel.
- Faltan Q5/Q6 en catálogo o contrato.
- El catálogo declara 40 variables como contrato final y omite 46.
- Faltan reportes de missingness.
- Falta política de transformaciones no estimables.
- Faltan tests anti-regresión.
- README o cierre técnico contradicen el contrato.
- `phase6_column_groups.yaml` referencia columnas inexistentes.
- No hay manifest del bundle.

### 22.3 Criterios P2/P3

Puede aprobarse con observaciones si:

- Hay nombres legacy pero explicados.
- Falta una mejora menor de formato en Excel.
- El README es breve pero no erróneo.
- El notebook no tiene todas las visualizaciones pero sí verifica lo esencial.

---

## 23. Plantilla de informe final del LLM auditor

El LLM auditor debe entregar el informe en este formato:

```markdown
# Informe de auditoría Fase 5 v2.1+ — Research_AI_law

## 1. Dictamen

**Dictamen:** APROBADA / APROBADA_CON_OBSERVACIONES / RECHAZADA  
**Fecha de auditoría:** YYYY-MM-DD  
**Ruta auditada:** ...  
**Commit / git sha:** ...  
**Resumen ejecutivo:** ...

## 2. Evidencia revisada

| Categoría | Evidencia | Estado |
|---|---|---|
| Código | `FASE5/src/...` | OK / Hallazgos |
| Config | `FASE5/config/...` | OK / Hallazgos |
| Outputs | `FASE5/outputs/...` | OK / Hallazgos |
| Bundle Fase 6 | `phase6_ready/...` | OK / Hallazgos |
| Excel | `MVP_AUDITABLE.xlsx` | OK / Hallazgos |
| Tests | `pytest FASE5/tests/` | OK / Fallas |
| Manifests | `fase5_manifest.json` | OK / Hallazgos |

## 3. Resultado por gate

| Gate | Resultado | Evidencia |
|---|---|---|
| No split | PASS/FAIL | ... |
| Muestra 43 | PASS/FAIL | ... |
| Membership | PASS/FAIL | ... |
| Contrato Fase 6 | PASS/FAIL | ... |
| 46 variables | PASS/FAIL | ... |
| Missingness | PASS/FAIL | ... |
| Agregados regulatorios | PASS/FAIL | ... |
| Excel limpio | PASS/FAIL | ... |
| Tests | PASS/FAIL | ... |
| Manifest | PASS/FAIL | ... |

## 4. Hallazgos

| ID | Severidad | Archivo | Descripción | Evidencia | Recomendación |
|---|---|---|---|---|---|
| F5-AUD-001 | P0/P1/P2/P3 | ... | ... | ... | ... |

## 5. Conclusión

La Fase 5 queda / no queda apta para ser consumida por Fase 6 bajo la metodología inferencial-comparativa observacional.

## 6. Próximas acciones

- Acción 1
- Acción 2
```

---

## 24. Plantilla JSON de salida para automatización

Además del informe narrativo, generar un resumen JSON:

```json
{
  "audit_name": "fase5_v2_1_plus_methodology_audit",
  "project": "Research_AI_law",
  "phase": "FASE5",
  "verdict": "APROBADA_CON_OBSERVACIONES",
  "audited_at": "2026-05-08T00:00:00Z",
  "root_path": "/home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP/FASE5",
  "gates": {
    "no_split_artifacts": "PASS",
    "sample_43_chile_present": "PASS",
    "analysis_sample_membership": "PASS",
    "phase6_contract": "PASS",
    "variables_46_preserved": "PASS",
    "missingness_preserved": "PASS",
    "regulatory_missingness_policy": "PASS",
    "excel_methodology_clean": "PASS",
    "tests_pass": "PASS",
    "manifest_complete": "PASS"
  },
  "findings": [
    {
      "id": "F5-AUD-001",
      "severity": "P2",
      "file": "FASE5/README.md",
      "description": "README no menciona explícitamente STROBE o reporte observacional.",
      "recommendation": "Agregar una frase de alineación con estudio observacional comparativo."
    }
  ],
  "blockers_count": 0,
  "critical_count": 0,
  "approved_for_phase6": true
}
```

---

## 25. Prompt listo para usar por un LLM auditor

Copia y pega este prompt cuando quieras ejecutar la auditoría:

```text
Eres un auditor metodológico y técnico del proyecto Research_AI_law. Debes auditar SOLO la Fase 5 ubicada en F5_F8_MVP/FASE5/. No implementes cambios. No edites archivos. Tu tarea es verificar si Fase 5 fue actualizada correctamente a la metodología v2.1+ inferencial-comparativa observacional.

Debes comprobar meticulosamente:
1. que no exista ningún artefacto train/test/split/holdout;
2. que la muestra primaria tenga exactamente 43 países e incluya CHL;
3. que exista analysis_sample_membership.csv con flags de sensibilidad;
4. que phase6_ready contenga un contrato inferencial válido;
5. que use_holdout_test_set=false, train_test_split_created=false y split_column_present=false;
6. que se preserven 46 variables observadas reales, incluidas Q5/Q6;
7. que no haya imputación de missing values;
8. que los agregados regulatorios no conviertan missing regulatorio en cero sin bandera y documentación;
9. que las transformaciones no estimables estén documentadas y excluidas de modelado primario;
10. que el Excel MVP_AUDITABLE.xlsx no contenga narrativa o columnas de split;
11. que tests, README, manifests y cierre técnico estén alineados con la nueva metodología;
12. que Fase 5 no escriba ni modifique Fase 3 o Fase 4.

Entrega un informe con dictamen APROBADA, APROBADA_CON_OBSERVACIONES o RECHAZADA. Clasifica hallazgos como P0, P1, P2, P3 o INFO. Cada hallazgo debe incluir archivo, evidencia y recomendación. Si encuentras un P0, el dictamen final debe ser RECHAZADA.
```

---

## 26. Conclusión normativa

La Fase 5 solo puede considerarse actualizada si la auditoría demuestra que ya no existe ninguna frontera predictiva artificial entre países de entrenamiento y prueba, y que el nuevo contrato de datos habilita a Fase 6 a trabajar correctamente como una fase de estimación de asociaciones ajustadas.

La señal de éxito no es que “corra el pipeline”. La señal de éxito es que un tercero pueda abrir la carpeta `FASE5/`, leer sus contratos, inspeccionar el Excel, revisar los manifests, ejecutar los tests y concluir sin ambigüedad:

> Esta Fase 5 prepara una muestra completa, auditable y preregistrada para un estudio observacional comparativo; no contiene holdout ficticio, no imputa datos, no oculta missingness y no sobrepromete predicción ni causalidad.

Fin del blueprint de auditoría.
