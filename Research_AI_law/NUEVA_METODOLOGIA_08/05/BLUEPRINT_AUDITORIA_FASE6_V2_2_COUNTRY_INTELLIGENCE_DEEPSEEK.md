# BLUEPRINT DE AUDITORÍA METICULOSA — Fase 6 v2.2 Country Intelligence Layer

**Proyecto:** Research_AI_law — Boletín 16821-19 Ley Marco de IA Chile  
**Documento:** Actualización del blueprint `FASE6V2.1-AUDITORIA.md` para auditar Fase 6.2  
**Versión auditada esperada:** `fase6-v2.2-country-intelligence-layer`  
**Base anterior:** `FASE6V2.1-AUDITORIA.md`  
**Extensión auditada:** `FASE6/outputs/country_intelligence/`  
**Modelo auditor recomendado:** DeepSeek V4 Pro  
**Tipo:** Protocolo de auditoría forense, metodológica, técnica, documental y visual para LLM auditor  
**Modo de uso:** Solo lectura, no implementación  
**Estado:** Listo para ejecutar después de implementar Fase 6.2  

---

## 0. Instrucción principal para DeepSeek V4 Pro

Actúa como **auditor técnico-metodológico senior** del proyecto `Research_AI_law`.

Tu tarea no es corregir, implementar ni regenerar Fase 6. Tu tarea es **auditar en modo solo lectura** si la actualización **Fase 6.2 Country Intelligence Layer** quedó correctamente implementada sobre la Fase 6 v2.1+ existente.

Debes auditar dos niveles:

1. **Fase 6 v2.1+ base**  
   Verificar que los resultados originales siguen correctos: sin split, sin holdout, sin validación externa falsa, sin causalidad fuerte, con Q2/Q5/Q6 continuos/fraccionales como análisis principal y scores por país como posicionamiento descriptivo in-sample.

2. **Fase 6.2 Country Intelligence Layer**  
   Verificar que se agregó correctamente una capa país-por-país con perfiles Q1–Q6, rankings globales, rankings por grupo, mejores/peores por Q, drivers descriptivos, residuales/gaps, country cards, gráficos profesionales, manifest, tests y semántica no causal.

Para cada criterio auditado debes indicar:

```text
archivo/comando revisado
evidencia observada
resultado: PASS / FAIL / WARNING / NO_VERIFICADO
severidad: P0 / P1 / P2 / P3
impacto
action recommended / acción recomendada
```

**Regla de oro:** Fase 6.2 solo puede aprobarse si conserva íntegra la metodología de Fase 6 v2.1+ y agrega inteligencia país-por-país sin convertirla en causalidad, predicción independiente o ranking normativo no justificado.

---

## 1. Cómo debe razonar DeepSeek V4 Pro

DeepSeek V4 Pro debe usar este documento como **norma de auditoría**, no como sugerencia.

### 1.1 No hacer

No debes:

```text
editar archivos
recalcular modelos
regenerar outputs
ejecutar run_all.py
ejecutar notebooks
borrar archivos
renombrar archivos
optimizar código
```

salvo autorización explícita del investigador.

### 1.2 Sí puedes hacer

Puedes ejecutar comandos de inspección:

```bash
pwd
ls
find
rg
cat
sed
head
tail
python3 - <<'PY'
# scripts de lectura/verificación
PY
pytest --collect-only
pytest tests/ -q
```

Puedes ejecutar tests si estos no modifican outputs.

### 1.3 Manejo de contexto para DeepSeek

No cargues todo el repositorio en memoria. Trabaja por capas:

```text
1. Leer manifests.
2. Verificar inventario.
3. Auditar Fase 6 base.
4. Auditar Fase 6.2 outputs.
5. Auditar country profiles.
6. Auditar rankings.
7. Auditar gráficos.
8. Auditar tests.
9. Emitir dictamen.
```

Si una salida de terminal es muy larga, usa inspecciones focalizadas:

```bash
head
tail
sed -n
python scripts cortos
```

No inventes resultados si no alcanzas a verificar. Usa `NO_VERIFICADO`.

---

## 2. Base normativa de la auditoría

Esta auditoría se basa en tres documentos normativos:

```text
FASE6V2.1-AUDITORIA.md
BLUEPRINT_ACTUALIZACION_FASE6_2_COUNTRY_INTELLIGENCE_RESEARCH_AI_LAW.md
BLUEPRINT_ARQUITECTURA_F5_F8_V0_3_RESEARCH_AI_LAW.md
```

La auditoría anterior `FASE6V2.1-AUDITORIA.md` ya establecía que Fase 6 solo puede aprobarse si:

- no usa `train/test split`;
- no usa holdout;
- no afirma validación externa;
- no afirma causalidad fuerte;
- valida el contrato inferencial de Fase 5;
- usa muestra disponible por outcome;
- reporta `n_effective`;
- trata Q2/Q5/Q6 como continuos/fraccionales en análisis principal;
- limita la binarización por mediana a sensibilidad;
- rotula scores por país como `in_sample_descriptive_positioning`;
- produce manifest y tests coherentes.

La nueva Fase 6.2 agrega una obligación adicional:

> Fase 6 debe producir una capa país-por-país que permita entender cómo se comporta cada uno de los países de la muestra en Q1–Q6, quiénes son pioneros, quiénes son rezagados, qué explica descriptivamente esas posiciones, qué puede aprender Chile y qué errores conviene evitar, sin afirmar causalidad ni predicción externa.

---

## 3. Resultado esperado de Fase 6 v2.2

La Fase 6 v2.2 correcta debe estar compuesta por:

```text
FASE6 v2.1+ base
   +
FASE6.2 Country Intelligence Layer
```

### 3.1 Fase 6 v2.1+ debe conservarse

Los 11 outputs originales deben seguir existiendo:

```text
FASE6/outputs/fase6_manifest.json
FASE6/outputs/q1_results.csv
FASE6/outputs/q2_results.csv
FASE6/outputs/q2_scores_per_country.csv
FASE6/outputs/q3_results.csv
FASE6/outputs/q4_clusters.csv
FASE6/outputs/q4_distance_matrix.csv
FASE6/outputs/q5_results.csv
FASE6/outputs/q5_scores_per_country.csv
FASE6/outputs/q6_results.csv
FASE6/outputs/q6_scores_per_country.csv
```

Ninguno debe haber sido eliminado, reemplazado con semántica distinta o convertido en predicción externa.

### 3.2 Fase 6.2 debe agregarse

Debe existir:

```text
FASE6/outputs/country_intelligence/
```

Con outputs tabulares, gráficos, country cards, manifest, quality checks y README.

### 3.3 Frase metodológica esperada

Debe aparecer en README, manifest, notebook o documento equivalente:

> Los rankings, scores y perfiles país-por-país son posicionamientos descriptivos in-sample dentro de la muestra preregistrada. No son predicciones independientes ni estimaciones causales. Su robustez debe evaluarse en Fase 7 antes de convertirse en recomendación política.

---

## 4. Clasificación de severidad

### P0 — Crítico bloqueante

Rechaza Fase 6.2 automáticamente.

Ejemplos:

- Se borró alguno de los 11 outputs originales de Fase 6.
- Existe o se usa `train/test split`.
- Existe columna `split` en outputs principales o country intelligence.
- `holdout_used = true`.
- `external_validation_used = true`.
- `independent_prediction = true`.
- `causal_claim = true`.
- Country Intelligence afirma causalidad país-por-país.
- Singapur no aparece en perfiles.
- Chile no aparece en perfiles.
- No existe `country_q_profile_wide.csv`.
- No existe `country_q_profile_long.csv`.
- No existe `phase6_2_country_intelligence_manifest.json`.
- No se puede distinguir ranking descriptivo de predicción.

### P1 — Alto

Debe corregirse antes de considerar Fase 6.2 cerrada.

Ejemplos:

- Faltan rankings por grupo.
- Falta `country_best_worst_by_q.csv`.
- Falta `country_headline_flags.csv`.
- Falta `country_learning_patterns.csv`.
- Faltan gráficos clave.
- Q4 se presenta como ranking normativo de mejor/peor regulación sin cautela.
- Drivers descriptivos se interpretan como causalidad implícita.
- No se documenta missingness.
- No hay tests para Fase 6.2.
- No hay README de `country_intelligence`.

### P2 — Medio

Permite aprobación con observaciones si no afecta la metodología central.

Ejemplos:

- Algunos gráficos no están en SVG pero sí en PNG.
- Faltan country cards de países secundarios.
- Alguna submuestra no tiene suficientes países y no se generó ranking.
- Nombres de columnas mejorables.
- Falta algún residual plot no central.

### P3 — Bajo

Mejoras de estilo o documentación.

Ejemplos:

- Gráficos podrían ser más profesionales.
- Títulos podrían ser más ejecutivos.
- Falta una tabla resumen de lectura rápida.
- README podría ser más claro.

---

## 5. Dictamen final posible

El auditor debe emitir uno de estos dictámenes:

```text
APROBADA
APROBADA_CON_OBSERVACIONES
APROBADA_CONDICIONAL
RECHAZADA
```

### 5.1 APROBADA

No hay P0 ni P1. Puede haber P2/P3 menores.

### 5.2 APROBADA_CON_OBSERVACIONES

No hay P0. Puede haber P1 menor si está mitigado y no bloquea Fase 7.

### 5.3 APROBADA_CONDICIONAL

No hay P0, pero hay P1 relevantes que deben corregirse antes de usar Fase 6.2 para Fase 7/Fase 8.

### 5.4 RECHAZADA

Existe al menos un P0 o múltiples P1 que impiden confiar en la capa país-por-país.

---

## 6. Inventario mínimo esperado

Desde la raíz esperada:

```text
/home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP
```

Debe existir:

```text
FASE6/
├── outputs/
│   ├── fase6_manifest.json
│   ├── q1_results.csv
│   ├── q2_results.csv
│   ├── q2_scores_per_country.csv
│   ├── q3_results.csv
│   ├── q4_clusters.csv
│   ├── q4_distance_matrix.csv
│   ├── q5_results.csv
│   ├── q5_scores_per_country.csv
│   ├── q6_results.csv
│   ├── q6_scores_per_country.csv
│   └── country_intelligence/
│       ├── country_q_profile_long.csv
│       ├── country_q_profile_wide.csv
│       ├── country_rankings_by_outcome.csv
│       ├── country_rankings_by_group.csv
│       ├── country_best_worst_by_q.csv
│       ├── country_model_contributions.csv
│       ├── country_residuals_and_gaps.csv
│       ├── country_cluster_profile.csv
│       ├── country_headline_flags.csv
│       ├── country_comparison_pairs.csv
│       ├── country_learning_patterns.csv
│       ├── country_graphics_catalog.csv
│       ├── phase6_2_country_intelligence_manifest.json
│       ├── phase6_2_quality_checks.csv
│       ├── README.md
│       ├── country_cards_data/
│       └── figures/
├── src/
│   └── country_intelligence/
└── tests/
    └── test_phase6_2_country_intelligence.py
```

---

## 7. Auditoría 0 — pre-flight general

Ejecutar desde raíz `F5_F8_MVP`:

```bash
pwd
ls -la
ls -la FASE6/outputs
ls -la FASE6/outputs/country_intelligence || true
```

Registrar:

```text
ruta auditada
fecha/hora
rama git si existe
commit si existe
archivos presentes
```

Si no existe `FASE6/outputs/country_intelligence`, la auditoría Fase 6.2 falla como P0.

---

## 8. Auditoría 1 — preservación de Fase 6 v2.1+

### 8.1 Verificar que los 11 outputs originales siguen presentes

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path

out = Path("FASE6/outputs")
required = [
    "fase6_manifest.json",
    "q1_results.csv",
    "q2_results.csv",
    "q2_scores_per_country.csv",
    "q3_results.csv",
    "q4_clusters.csv",
    "q4_distance_matrix.csv",
    "q5_results.csv",
    "q5_scores_per_country.csv",
    "q6_results.csv",
    "q6_scores_per_country.csv",
]
for fname in required:
    print(fname, (out / fname).exists(), (out / fname).stat().st_size if (out / fname).exists() else None)
PY
```

### PASS

Todos existen y no tienen tamaño cero.

### FAIL

- Falta cualquiera: P0.
- Existe con tamaño 0: P0/P1 según archivo.

### 8.2 Verificar manifest base

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import json

p = Path("FASE6/outputs/fase6_manifest.json")
print("exists", p.exists())
if p.exists():
    m = json.loads(p.read_text())
    keys = [
        "fase6_version",
        "methodology",
        "primary_estimand",
        "analysis_scope",
        "validation_scope",
        "analysis_sample_n",
        "holdout_used",
        "train_test_split_used",
        "external_validation_used",
        "split_column_present",
        "phase6_train_test_split_present",
        "q2_q5_q6_primary_model_policy",
    ]
    for k in keys:
        print(k, m.get(k, "<MISSING>"))
PY
```

### PASS esperado

```json
{
  "fase6_version": "2.1+",
  "methodology": "inferential_comparative_observational",
  "primary_estimand": "adjusted_association",
  "analysis_sample_n": 43,
  "holdout_used": false,
  "train_test_split_used": false,
  "external_validation_used": false,
  "split_column_present": false,
  "phase6_train_test_split_present": false
}
```

### Red flags P0

```text
holdout_used = true
train_test_split_used = true
external_validation_used = true
split_column_present = true
phase6_train_test_split_present = true
```

---

## 9. Auditoría 2 — ausencia de split, holdout, external validation y causalidad

Ejecutar:

```bash
rg -n "phase6_train_test_split|mvp_train_test_split|get_train_test_split|train/test|holdout|test set independiente|external validation|validación externa|predicción independiente|independent prediction|impacto causal|efecto causal|causal effect|la regulación causa|la regulacion causa|\\bsplit\\b" FASE6 || true
```

### Clasificación

Permitido solo si aparece en:

- listas de términos prohibidos;
- tests anti-regresión;
- documentación que dice explícitamente que está prohibido;
- auditoría histórica.

No permitido si aparece en:

- código activo;
- outputs como afirmación;
- README como metodología activa;
- gráficos;
- notebooks;
- country profiles;
- manifest con valor `true`.

### Red flags P0

```text
fm[fm['split'] == 'train']
fm[fm['split'] == 'test']
phase6_train_test_split.csv usado
external_validation_used = true
independent_prediction = true
causal_claim = true
```

---

## 10. Auditoría 3 — inventario Fase 6.2

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path

ci = Path("FASE6/outputs/country_intelligence")
required = [
    "country_q_profile_long.csv",
    "country_q_profile_wide.csv",
    "country_rankings_by_outcome.csv",
    "country_rankings_by_group.csv",
    "country_best_worst_by_q.csv",
    "country_model_contributions.csv",
    "country_residuals_and_gaps.csv",
    "country_cluster_profile.csv",
    "country_headline_flags.csv",
    "country_comparison_pairs.csv",
    "country_learning_patterns.csv",
    "country_graphics_catalog.csv",
    "phase6_2_country_intelligence_manifest.json",
    "phase6_2_quality_checks.csv",
    "README.md",
]
print("country_intelligence_exists", ci.exists())
for fname in required:
    path = ci / fname
    print(fname, path.exists(), path.stat().st_size if path.exists() else None)
print("country_cards_data_exists", (ci / "country_cards_data").exists())
print("figures_exists", (ci / "figures").exists())
PY
```

### PASS

Todos los archivos principales existen y no están vacíos.

### Severidades si falla

| Archivo faltante | Severidad |
|---|---|
| `country_q_profile_long.csv` | P0 |
| `country_q_profile_wide.csv` | P0 |
| manifest 6.2 | P0 |
| rankings by outcome | P1 |
| rankings by group | P1 |
| best/worst | P1 |
| contributions | P1 |
| residuals/gaps | P1/P2 |
| headline flags | P1 |
| learning patterns | P1 |
| graphics catalog | P1 |
| README | P1 |
| country cards | P1/P2 |
| figures | P1 |

---

## 11. Auditoría 4 — manifest de Fase 6.2

Archivo:

```text
FASE6/outputs/country_intelligence/phase6_2_country_intelligence_manifest.json
```

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import json

p = Path("FASE6/outputs/country_intelligence/phase6_2_country_intelligence_manifest.json")
print("exists", p.exists())
if p.exists():
    m = json.loads(p.read_text())
    keys = [
        "fase6_2_version",
        "module",
        "methodology",
        "scope",
        "holdout_used",
        "train_test_split_used",
        "external_validation_used",
        "independent_prediction",
        "causal_claim",
        "preserved_existing_fase6_outputs",
        "n_countries_profiled",
        "n_figures",
    ]
    for k in keys:
        print(k, m.get(k, "<MISSING>"))
    print("outputs_keys", list(m.get("outputs", {}).keys()))
PY
```

### PASS esperado

```json
{
  "fase6_2_version": "2.2",
  "module": "country_intelligence_layer",
  "methodology": "inferential_comparative_observational",
  "scope": "descriptive_country_level_positioning",
  "holdout_used": false,
  "train_test_split_used": false,
  "external_validation_used": false,
  "independent_prediction": false,
  "causal_claim": false,
  "preserved_existing_fase6_outputs": true
}
```

### FAIL P0

- `independent_prediction = true`.
- `causal_claim = true`.
- `external_validation_used = true`.
- `preserved_existing_fase6_outputs = false`.
- `n_countries_profiled = 0`.

---

## 12. Auditoría 5 — quality checks de Fase 6.2

Archivo:

```text
phase6_2_quality_checks.csv
```

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

p = Path("FASE6/outputs/country_intelligence/phase6_2_quality_checks.csv")
print("exists", p.exists())
if p.exists():
    df = pd.read_csv(p)
    print("shape", df.shape)
    print(df.head(30).to_string())
    print("columns", df.columns.tolist())
    if "status" in df.columns:
        print("status_counts", df["status"].value_counts(dropna=False).to_dict())
    if "severity" in df.columns:
        print("severity_counts", df["severity"].value_counts(dropna=False).to_dict())
PY
```

### PASS

- Existe.
- Registra pre-flight.
- No tiene `FAIL` con severidad `P0`.
- Si hay warnings, están explicados.

### FAIL

- No existe: P1.
- Tiene P0 no resuelto: P0.

---

## 13. Auditoría 6 — country profile long

Archivo:

```text
country_q_profile_long.csv
```

### 13.1 Verificar schema

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

p = Path("FASE6/outputs/country_intelligence/country_q_profile_long.csv")
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
required = [
    "iso3",
    "country_name",
    "question_id",
    "question_label",
    "outcome",
    "observed_value",
    "score_value",
    "rank_global",
    "percentile_global",
    "n_comparable_countries",
    "interpretation_label",
    "strength_weakness_label",
    "score_scope",
    "independent_prediction",
    "causal_claim",
]
for col in required:
    print(col, col in df.columns)
print("question_ids", sorted(df["question_id"].dropna().unique()) if "question_id" in df.columns else None)
print("n_iso3", df["iso3"].nunique() if "iso3" in df.columns else None)
print("CHL_present", "CHL" in set(df["iso3"]) if "iso3" in df.columns else None)
print("SGP_present", "SGP" in set(df["iso3"]) if "iso3" in df.columns else None)
if "score_scope" in df.columns:
    print("score_scope_unique", df["score_scope"].dropna().unique())
if "independent_prediction" in df.columns:
    print("independent_prediction_unique", df["independent_prediction"].dropna().unique())
if "causal_claim" in df.columns:
    print("causal_claim_unique", df["causal_claim"].dropna().unique())
PY
```

### PASS

Debe cumplir:

- Tiene filas para Q1, Q2, Q3, Q5 y Q6.
- Q4 puede estar en archivo aparte si está justificado.
- Chile (`CHL`) está presente.
- Singapur (`SGP`) está presente.
- `score_scope = in_sample_descriptive_positioning` o equivalente descriptivo.
- `independent_prediction = false`.
- `causal_claim = false`.
- Tiene percentiles/rankings.
- No tiene columna `split`.

### FAIL P0

- Falta Chile.
- Falta Singapur.
- `independent_prediction = true`.
- `causal_claim = true`.
- No existen Q profiles.

### 13.2 Verificar cobertura por pregunta

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
df = pd.read_csv("FASE6/outputs/country_intelligence/country_q_profile_long.csv")
print(df.groupby("question_id")["iso3"].nunique())
print(df.groupby("question_id")["outcome"].nunique())
PY
```

### PASS

Debe haber cobertura razonable:

```text
Q1 > 0 países y outcomes
Q2 > 0 países y outcomes
Q3 > 0 países y outcomes
Q5 > 0 países y outcomes
Q6 > 0 países y outcomes
```

Si alguna Q no existe, debe estar justificado en quality checks.

---

## 14. Auditoría 7 — country profile wide

Archivo:

```text
country_q_profile_wide.csv
```

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

p = Path("FASE6/outputs/country_intelligence/country_q_profile_wide.csv")
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
print("n_iso3", df["iso3"].nunique() if "iso3" in df.columns else None)
print("CHL_present", "CHL" in set(df["iso3"]) if "iso3" in df.columns else None)
print("SGP_present", "SGP" in set(df["iso3"]) if "iso3" in df.columns else None)

expected_partial = [
    "Q1_percentile",
    "Q2_percentile",
    "Q3_percentile",
    "Q5_percentile",
    "Q6_percentile",
    "overall_country_profile_score",
    "overall_country_profile_rank",
    "overall_country_profile_label",
    "main_strengths",
    "main_weaknesses",
    "recommended_use_in_phase8",
]
for col in expected_partial:
    print(col, col in df.columns)

if "overall_country_profile_score" in df.columns:
    cols = [c for c in ["iso3","country_name","overall_country_profile_score","overall_country_profile_rank","overall_country_profile_label"] if c in df.columns]
    print(df[cols].head(15).to_string(index=False))
PY
```

### PASS

- Una fila por país perfilado.
- Idealmente 43 países, salvo missingness documentada.
- Chile y Singapur presentes.
- Q1, Q2, Q3, Q5, Q6 percentiles o equivalentes.
- Score general descriptivo.
- Rank general.
- Strengths/weaknesses.
- Recomendación de uso en Fase 8.
- Debe indicar que el score es descriptivo, no causal.

### FAIL P0

- Falta `country_q_profile_wide.csv`.
- Falta Chile o Singapur.
- Score general se presenta como índice causal o predictivo.

---

## 15. Auditoría 8 — rankings por outcome

Archivo:

```text
country_rankings_by_outcome.csv
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
p = "FASE6/outputs/country_intelligence/country_rankings_by_outcome.csv"
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
required = [
    "question_id",
    "outcome",
    "iso3",
    "country_name",
    "value_used_for_ranking",
    "rank_desc",
    "rank_asc",
    "percentile",
    "n_ranked",
    "is_top_5_global",
    "is_bottom_5_global",
    "interpretation_label",
    "why_high_or_low_short",
    "missingness_flag",
]
for col in required:
    print(col, col in df.columns)
print("questions", sorted(df["question_id"].dropna().unique()))
print("outcomes_by_q")
print(df.groupby("question_id")["outcome"].nunique())
print("top examples")
cols = [c for c in ["question_id","outcome","iso3","country_name","rank_desc","percentile"] if c in df.columns]
print(df.sort_values(["question_id","rank_desc"]).groupby("question_id").head(3)[cols].to_string(index=False))
PY
```

### PASS

- Rankings existen para Q1, Q2, Q3, Q5, Q6.
- Ranking descendente y ascendente.
- Top/bottom flags.
- Interpretación.
- Missingness flag.

### FAIL P1

- No hay rankings por Q.
- No hay ranking para varias preguntas.
- No se puede identificar mejores/peores.

---

## 16. Auditoría 9 — rankings por grupo/submuestra

Archivo:

```text
country_rankings_by_group.csv
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
p = "FASE6/outputs/country_intelligence/country_rankings_by_group.csv"
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
required = [
    "group_name",
    "group_type",
    "question_id",
    "outcome",
    "iso3",
    "country_name",
    "rank_within_group",
    "percentile_within_group",
    "n_group_ranked",
    "is_best_in_group",
    "is_worst_in_group",
    "distance_to_group_best",
    "distance_to_group_median",
    "distance_to_chile",
    "why_best_or_worst",
]
for col in required:
    print(col, col in df.columns)
print("groups", sorted(map(str, df["group_name"].dropna().unique()))[:50] if "group_name" in df.columns else None)
print("CHL groups", sorted(df.loc[df["iso3"].eq("CHL"), "group_name"].dropna().unique()) if "iso3" in df.columns and "group_name" in df.columns else None)
print("SGP groups", sorted(df.loc[df["iso3"].eq("SGP"), "group_name"].dropna().unique()) if "iso3" in df.columns and "group_name" in df.columns else None)
PY
```

### PASS

Debe permitir responder:

```text
¿Quién es el mejor de LATAM en Q2?
¿Quién es el mejor entre benchmarks de Chile?
¿Quién es el peor dentro de un grupo?
¿Dónde está Chile dentro de su grupo?
¿Dónde está Singapur dentro de pioneros?
```

### Grupos esperados

Al menos algunos de:

```text
global_43
latam_peers
chile_priority_benchmarks
ai_pioneers
large_ai_powers
eu_laggards
region groups
income groups
```

### FAIL P1

- No hay rankings por grupo.
- No se puede comparar Chile con submuestras.
- No se puede identificar best/worst de grupos.

---

## 17. Auditoría 10 — mejores y peores por Q

Archivo:

```text
country_best_worst_by_q.csv
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
p = "FASE6/outputs/country_intelligence/country_best_worst_by_q.csv"
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
required = [
    "question_id",
    "question_label",
    "group_name",
    "rank_type",
    "iso3",
    "country_name",
    "rank",
    "percentile",
    "value_summary",
    "why_this_country_is_best_or_worst",
    "lesson_for_chile",
    "caution_note",
]
for col in required:
    print(col, col in df.columns)
print("rank_types", sorted(df["rank_type"].dropna().unique()) if "rank_type" in df.columns else None)
print(df.head(20).to_string(index=False))
PY
```

### PASS

Debe tener al menos:

```text
best_global
worst_global
```

Idealmente también:

```text
best_group
worst_group
best_latam
worst_latam
best_benchmark
worst_benchmark
```

### FAIL P1

- No existe top/bottom por Q.
- No hay lección para Chile.
- No hay cautela metodológica.

---

## 18. Auditoría 11 — drivers/contribuciones descriptivas

Archivo:

```text
country_model_contributions.csv
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
p = "FASE6/outputs/country_intelligence/country_model_contributions.csv"
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
required = [
    "iso3",
    "country_name",
    "question_id",
    "outcome",
    "model_id",
    "term",
    "term_value",
    "term_percentile",
    "coefficient_or_weight",
    "standardized_contribution",
    "contribution_direction",
    "contribution_label",
    "driver_type",
    "interpretation",
    "causal_claim",
]
for col in required:
    print(col, col in df.columns)
if "causal_claim" in df.columns:
    print("causal_claim_unique", df["causal_claim"].dropna().unique())
if "contribution_label" in df.columns:
    print("contribution_labels", df["contribution_label"].dropna().unique()[:20])
print("SGP sample")
print(df[df["iso3"].eq("SGP")].head(20).to_string(index=False) if "iso3" in df.columns else "NO_ISO3")
PY
```

### PASS

- Incluye Chile y Singapur.
- Tiene contribuciones por término/modelo.
- `causal_claim = false`.
- Interpretaciones dicen `descriptive_driver_not_causal` o equivalente.

### FAIL P0/P1

- Contribuciones se presentan como causalidad.
- No hay drivers para países clave.
- No hay advertencia de no causalidad.

---

## 19. Auditoría 12 — residuals and gaps

Archivo:

```text
country_residuals_and_gaps.csv
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
p = "FASE6/outputs/country_intelligence/country_residuals_and_gaps.csv"
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
required = [
    "iso3",
    "country_name",
    "question_id",
    "outcome",
    "model_id",
    "observed_value",
    "fitted_value",
    "residual",
    "absolute_residual",
    "overperformer_underperformer",
    "gap_vs_best",
    "gap_vs_chile",
    "gap_vs_singapore",
    "interpretation",
]
for col in required:
    print(col, col in df.columns)
if "overperformer_underperformer" in df.columns:
    print("labels", df["overperformer_underperformer"].dropna().unique())
print("SGP residuals")
print(df[df["iso3"].eq("SGP")].head(10).to_string(index=False) if "iso3" in df.columns else "NO_ISO3")
PY
```

### PASS

- Permite identificar overperformers/underperformers.
- Tiene gaps vs Chile y Singapur.
- Interpretación no causal.

### WARNING/P2

- No existe por falta de fitted values, pero hay justificación.
- Solo algunas Q tienen residuals.

---

## 20. Auditoría 13 — Q4 cluster profile

Archivo:

```text
country_cluster_profile.csv
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
p = "FASE6/outputs/country_intelligence/country_cluster_profile.csv"
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
print("CHL_present", "CHL" in set(df["iso3"]) if "iso3" in df.columns else None)
print("SGP_present", "SGP" in set(df["iso3"]) if "iso3" in df.columns else None)
for col in ["cluster_id","cluster_label","cluster_method","score_scope","independent_prediction","causal_claim"]:
    print(col, col in df.columns)
if "causal_claim" in df.columns:
    print("causal_claim_unique", df["causal_claim"].dropna().unique())
PY
```

### PASS

- Q4 se presenta como tipología descriptiva.
- No se presenta como ranking normativo de mejor/peor.
- Chile y Singapur presentes o missingness documentada.
- `independent_prediction = false`.
- `causal_claim = false`.

### FAIL P1/P0

- Q4 dice que un cluster “causa” mejores resultados.
- Q4 rankea regulación mejor/peor sin outcome ni cautela.
- Q4 usa test/accuracy.

---

## 21. Auditoría 14 — headline flags

Archivo:

```text
country_headline_flags.csv
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
p = "FASE6/outputs/country_intelligence/country_headline_flags.csv"
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
required = [
    "iso3",
    "country_name",
    "is_consistent_pioneer",
    "is_consistent_laggard",
    "is_chile_benchmark",
    "headline_candidate",
    "suggested_headline",
    "caution_note",
]
for col in required:
    print(col, col in df.columns)
print("headline candidates")
if "headline_candidate" in df.columns:
    print(df[df["headline_candidate"].fillna(False)].head(20).to_string(index=False))
PY
```

### PASS

- Identifica pioneros/rezagados.
- Identifica benchmarks para Chile.
- Incluye cautela metodológica.

### FAIL P1

- No hay flags narrativos.
- No hay cautela.

---

## 22. Auditoría 15 — learning patterns

Archivo:

```text
country_learning_patterns.csv
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
p = "FASE6/outputs/country_intelligence/country_learning_patterns.csv"
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
required = [
    "pattern_id",
    "question_id",
    "group_name",
    "pattern_type",
    "countries_in_pattern",
    "shared_strengths",
    "shared_weaknesses",
    "lesson_for_chile",
    "risk_of_overinterpretation",
    "evidence_strength",
    "recommended_phase8_use",
]
for col in required:
    print(col, col in df.columns)
print(df.head(20).to_string(index=False))
PY
```

### PASS

Debe permitir aprender:

```text
qué comparten los pioneros
qué errores comparten los rezagados
qué puede aprender Chile
qué no se debe sobreinterpretar
```

### FAIL P1

- No existe.
- No hay `lesson_for_chile`.
- No hay `risk_of_overinterpretation`.

---

## 23. Auditoría 16 — comparación Chile vs benchmarks

Archivo:

```text
country_comparison_pairs.csv
```

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
p = "FASE6/outputs/country_intelligence/country_comparison_pairs.csv"
df = pd.read_csv(p)
print("shape", df.shape)
print("columns", df.columns.tolist())
required = [
    "country_a",
    "country_b",
    "dimension",
    "country_a_percentile",
    "country_b_percentile",
    "gap_b_minus_a",
    "interpretation",
]
for col in required:
    print(col, col in df.columns)
print("comparisons")
print(df.head(50).to_string(index=False))
print("has_CHL_SGP", ((df.get("country_a") == "CHL") & (df.get("country_b") == "SGP")).any() if "country_a" in df.columns and "country_b" in df.columns else None)
PY
```

### PASS

Debe incluir:

```text
CHL vs SGP
CHL vs EST
CHL vs IRL
CHL vs ARE
CHL vs KOR
CHL vs URY/BRA si existen
```

Al menos `CHL vs SGP` debe estar.

### FAIL P1

- No hay comparación Chile vs Singapur.
- No hay gaps interpretables.

---

## 24. Auditoría 17 — country cards data

Carpeta:

```text
country_cards_data/
```

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

card_dir = Path("FASE6/outputs/country_intelligence/country_cards_data")
print("exists", card_dir.exists())
if card_dir.exists():
    files = sorted(card_dir.glob("*_country_card_data.csv"))
    print("n_files", len(files))
    print([f.name for f in files])
    for iso in ["CHL", "SGP", "EST", "IRL", "ARE", "KOR", "USA", "CHN", "BRA", "URY"]:
        matches = list(card_dir.glob(f"{iso}_country_card_data.csv"))
        print(iso, bool(matches), matches[0].stat().st_size if matches else None)
        if matches:
            df = pd.read_csv(matches[0])
            print(iso, "shape", df.shape, "sections", df["section"].dropna().unique()[:10] if "section" in df.columns else "NO_SECTION")
PY
```

### PASS

Country cards para al menos:

```text
CHL
SGP
```

Idealmente también:

```text
EST, IRL, ARE, KOR, USA, CHN, BRA, URY
```

### P0/P1

- Falta CHL: P0.
- Falta SGP: P0.
- Faltan varios benchmarks: P1/P2.

---

## 25. Auditoría 18 — gráficos

Carpeta:

```text
figures/
```

Archivo catálogo:

```text
country_graphics_catalog.csv
```

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

ci = Path("FASE6/outputs/country_intelligence")
fig = ci / "figures"
cat = ci / "country_graphics_catalog.csv"
print("figures_exists", fig.exists())
print("catalog_exists", cat.exists())

if fig.exists():
    pngs = sorted(fig.rglob("*.png"))
    svgs = sorted(fig.rglob("*.svg"))
    print("n_png", len(pngs))
    print("n_svg", len(svgs))
    print("first_pngs", [str(p) for p in pngs[:20]])

expected = [
    "q_heatmaps/heatmap_country_by_q_percentiles.png",
    "q_rankings/q1_ranking.png",
    "q_rankings/q2_ranking.png",
    "q_rankings/q3_ranking.png",
    "q_rankings/q5_ranking.png",
    "q_rankings/q6_ranking.png",
    "country_cards/SGP_country_card_radar.png",
    "country_cards/CHL_country_card_radar.png",
    "chile_vs_benchmarks/chile_vs_singapore_q_profile.png",
]
for e in expected:
    p = fig / e
    print(e, p.exists(), p.stat().st_size if p.exists() else None)

if cat.exists():
    df = pd.read_csv(cat)
    print("catalog_shape", df.shape)
    print(df.head(20).to_string(index=False))
PY
```

### PASS

Debe existir al menos:

```text
heatmap país × Q
ranking Q1
ranking Q2
ranking Q3
ranking Q5
ranking Q6
radar Singapur
radar Chile
Chile vs Singapur
catálogo de figuras
```

### P1

- Falta heatmap país × Q.
- Falta gráfico Chile vs Singapur.
- Falta radar Singapur o Chile.
- No hay catálogo.

### P2

- Faltan SVG pero hay PNG.
- Gráficos existen pero tienen títulos débiles.

---

## 26. Auditoría 19 — calidad visual mínima

El auditor no debe limitarse a verificar existencia de PNG. Debe revisar, al menos con metadata y opcionalmente apertura visual, que las figuras no están vacías.

### 26.1 Verificar tamaño de archivos

```bash
find FASE6/outputs/country_intelligence/figures -name "*.png" -exec ls -lh {} \;
```

Red flags:

```text
archivos < 5 KB
figuras vacías
solo ejes sin datos
```

### 26.2 Verificar dimensiones

```bash
python3 - <<'PY'
from pathlib import Path
from PIL import Image

fig = Path("FASE6/outputs/country_intelligence/figures")
for p in sorted(fig.rglob("*.png"))[:50]:
    try:
        im = Image.open(p)
        print(p, im.size)
    except Exception as e:
        print("ERROR", p, e)
PY
```

### PASS

- Figuras tienen dimensiones razonables.
- No parecen archivos vacíos.
- Si se puede revisar visualmente, deben mostrar datos, títulos y nota metodológica.

---

## 27. Auditoría 20 — README de country intelligence

Archivo:

```text
FASE6/outputs/country_intelligence/README.md
```

Ejecutar:

```bash
rg -n "Country Intelligence|pais|país|Q1|Q2|Q3|Q4|Q5|Q6|ranking|in-sample|descriptivo|causal|predic" FASE6/outputs/country_intelligence/README.md || true
```

### PASS

Debe explicar:

- qué contiene;
- que no contiene causalidad;
- que no contiene predicción independiente;
- que Fase 7 debe validar robustez;
- cómo interpretar rankings y scores.

### FAIL P1

- No existe.
- Presenta rankings como verdad causal.
- No advierte limitaciones.

---

## 28. Auditoría 21 — código fuente Fase 6.2

Carpeta esperada:

```text
FASE6/src/country_intelligence/
```

Ejecutar:

```bash
find FASE6/src/country_intelligence -maxdepth 2 -type f -print 2>/dev/null || true
```

Archivos esperados:

```text
__init__.py
_paths.py
_load.py
_scoring.py
_rankings.py
_profiles.py
_contributions.py
_residuals.py
_groups.py
_learning_patterns.py
_graphics.py
_country_cards.py
_validate.py
run_country_intelligence.py
```

No todos son obligatorios si existe funcionalidad equivalente, pero debe haber un orquestador claro.

### 28.1 Buscar semántica prohibida en código

```bash
rg -n "causal_claim.*True|independent_prediction.*True|external_validation.*True|holdout_used.*True|split|train_test|test set|causal effect|impacto causal|predicción independiente" FASE6/src/country_intelligence || true
```

### 28.2 Verificar orquestador

```bash
rg -n "validate_preflight|country_q_profile|country_rankings|country_cards|graphics|manifest|causal_claim|independent_prediction|score_scope" FASE6/src/country_intelligence/run_country_intelligence.py
```

### PASS

- Orquestador valida preflight.
- Genera outputs principales.
- Escribe manifest.
- No toca outputs originales.
- Escribe `causal_claim = false`.
- Escribe `independent_prediction = false`.

---

## 29. Auditoría 22 — tests Fase 6.2

Archivo esperado:

```text
FASE6/tests/test_phase6_2_country_intelligence.py
```

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path("FASE6/tests/test_phase6_2_country_intelligence.py")
print("exists", p.exists())
if p.exists():
    txt = p.read_text()
    required = [
        "country_q_profile_long",
        "country_q_profile_wide",
        "CHL",
        "SGP",
        "independent_prediction",
        "causal_claim",
        "score_scope",
        "country_graphics_catalog",
        "manifest",
    ]
    for r in required:
        print(r, r in txt)
PY
```

Si se puede ejecutar:

```bash
python3 -m pytest FASE6/tests/test_phase6_2_country_intelligence.py -q
```

### PASS

- Test existe.
- Verifica outputs.
- Verifica Chile y Singapur.
- Verifica semántica no causal/no predictiva.
- Verifica catálogo gráfico.
- Test pasa.

### P1

- No existe test.
- No verifica semántica.
- No verifica Chile/Singapur.

---

## 30. Auditoría 23 — integración con Fase 7

Fase 6.2 debe producir outputs consumibles por Fase 7.

Verificar que existen:

```text
country_q_profile_long.csv
country_q_profile_wide.csv
country_rankings_by_outcome.csv
country_rankings_by_group.csv
country_best_worst_by_q.csv
country_model_contributions.csv
country_residuals_and_gaps.csv
country_headline_flags.csv
country_learning_patterns.csv
```

Y que contienen:

```text
iso3
question_id
outcome o dimension
ranking/percentile
interpretación
cautela metodológica
```

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

ci = Path("FASE6/outputs/country_intelligence")
files = [
    "country_q_profile_long.csv",
    "country_q_profile_wide.csv",
    "country_rankings_by_outcome.csv",
    "country_rankings_by_group.csv",
    "country_best_worst_by_q.csv",
    "country_model_contributions.csv",
    "country_residuals_and_gaps.csv",
    "country_headline_flags.csv",
    "country_learning_patterns.csv",
]
for fname in files:
    p = ci / fname
    if not p.exists():
        print(fname, "MISSING")
        continue
    df = pd.read_csv(p)
    print(fname, df.shape, df.columns.tolist()[:15])
PY
```

### PASS

Fase 7 puede auditar robustez país-por-país y patrones de pioneros/rezagados.

---

## 31. Auditoría 24 — integración con Fase 8

Fase 6.2 debe permitir crear narrativa ejecutiva, pero no debe hacer Fase 8 por sí sola.

Verificar:

- `country_cards_data/` existe.
- gráficos existen.
- `country_learning_patterns.csv` existe.
- `country_headline_flags.csv` existe.
- `country_comparison_pairs.csv` existe.
- no hay `EXECUTIVE_SUMMARY.md` dentro de Fase 6.2 salvo que esté claramente marcado como preliminar.

Ejecutar:

```bash
find FASE6/outputs/country_intelligence -maxdepth 2 -type f | sort
rg -n "recomendación final|recomendacion final|conclusión política definitiva|conclusion politica definitiva|se debe aprobar|causa|prueba que" FASE6/outputs/country_intelligence || true
```

### PASS

Fase 6.2 prepara insumos para Fase 8, pero no emite conclusiones políticas definitivas.

### FAIL P1/P0

- Fase 6.2 produce recomendaciones finales como si fueran Fase 8.
- Fase 6.2 convierte ranking descriptivo en mandato político.
- Fase 6.2 dice que un país prueba causalidad.

---

## 32. Auditoría 25 — caso Singapur

El usuario necesita poder responder:

> ¿Cómo Singapur es el mejor o uno de los pioneros en IA?  
> ¿Cómo se comporta Singapur en cada Q?

La auditoría debe verificar si Fase 6.2 permite responderlo.

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
from pathlib import Path

ci = Path("FASE6/outputs/country_intelligence")

wide = pd.read_csv(ci / "country_q_profile_wide.csv")
long = pd.read_csv(ci / "country_q_profile_long.csv")
rankings = pd.read_csv(ci / "country_rankings_by_outcome.csv")
flags = pd.read_csv(ci / "country_headline_flags.csv")

print("SGP wide")
print(wide[wide["iso3"].eq("SGP")].to_string(index=False))

print("\nSGP long by Q")
print(long[long["iso3"].eq("SGP")].sort_values(["question_id","outcome"]).head(100).to_string(index=False))

print("\nSGP rankings")
print(rankings[rankings["iso3"].eq("SGP")].sort_values(["question_id","rank_desc"]).head(100).to_string(index=False))

print("\nSGP flags")
print(flags[flags["iso3"].eq("SGP")].to_string(index=False))
PY
```

### PASS

Debe poder verse:

- percentiles de SGP por Q;
- rankings de SGP por outcomes;
- fortalezas/debilidades;
- si es pionero consistente;
- cautelas;
- no causalidad.

### FAIL P0/P1

- Singapur no aparece.
- Aparece pero sin Q breakdown.
- Aparece solo como ranking global sin explicación.
- Se dice que su regulación causa liderazgo.

---

## 33. Auditoría 26 — caso Chile

Debe poder responder:

> ¿Dónde está Chile frente a pioneros y pares?  
> ¿Qué brechas tiene?  
> ¿Qué puede aprender?

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
from pathlib import Path

ci = Path("FASE6/outputs/country_intelligence")

wide = pd.read_csv(ci / "country_q_profile_wide.csv")
pairs = pd.read_csv(ci / "country_comparison_pairs.csv")
group = pd.read_csv(ci / "country_rankings_by_group.csv")
learn = pd.read_csv(ci / "country_learning_patterns.csv")

print("CHL wide")
print(wide[wide["iso3"].eq("CHL")].to_string(index=False))

print("\nCHL comparison pairs")
print(pairs[pairs["country_a"].eq("CHL")].head(100).to_string(index=False))

print("\nCHL group rankings")
print(group[group["iso3"].eq("CHL")].head(100).to_string(index=False))

print("\nLearning patterns")
print(learn.head(50).to_string(index=False))
PY
```

### PASS

Debe permitir:

- ubicar Chile por Q;
- comparar Chile vs SGP;
- comparar Chile vs benchmarks;
- ver brechas;
- obtener lecciones preliminares.

### FAIL P0/P1

- Chile falta.
- No hay comparación Chile vs Singapur.
- No hay brechas.
- No hay lecciones para Chile.

---

## 34. Auditoría 27 — mejores y peores por Q

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
df = pd.read_csv("FASE6/outputs/country_intelligence/country_best_worst_by_q.csv")
for q in sorted(df["question_id"].dropna().unique()):
    print("\n###", q)
    sub = df[df["question_id"].eq(q)]
    cols = [c for c in ["rank_type","iso3","country_name","rank","percentile","why_this_country_is_best_or_worst","lesson_for_chile","caution_note"] if c in sub.columns]
    print(sub[cols].head(20).to_string(index=False))
PY
```

### PASS

Para cada Q debe identificar:

- mejores;
- peores;
- razón descriptiva;
- lección para Chile;
- cautela.

### FAIL P1

- Solo ranking sin interpretación.
- No hay bottom/worst.
- No hay lección para Chile.
- No hay cautela.

---

## 35. Auditoría 28 — missingness y países ausentes

Fase 6.2 debe documentar si no puede rankear a los 43 países.

Ejecutar:

```bash
python3 - <<'PY'
import pandas as pd
from pathlib import Path

ci = Path("FASE6/outputs/country_intelligence")
wide = pd.read_csv(ci / "country_q_profile_wide.csv")
long = pd.read_csv(ci / "country_q_profile_long.csv")
print("wide_n_iso3", wide["iso3"].nunique())
print("long_n_iso3", long["iso3"].nunique())

expected = set(pd.read_csv("FASE5/outputs/phase6_ready/phase6_analysis_sample_membership.csv")["iso3"])
wide_iso = set(wide["iso3"])
long_iso = set(long["iso3"])
print("missing_from_wide", sorted(expected - wide_iso))
print("missing_from_long", sorted(expected - long_iso))

if "missingness_warnings" in wide.columns:
    print(wide[["iso3","country_name","missingness_warnings"]].head(50).to_string(index=False))
PY
```

### PASS

- Idealmente 43 países.
- Si hay menos, missingness está documentado.
- Países faltantes no desaparecen silenciosamente.

### P1

- Faltan países sin explicación.
- Taiwan u otros desaparecen sin warning.

---

## 36. Auditoría 29 — lenguaje prohibido en outputs de Fase 6.2

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path

forbidden = [
    "causa",
    "causal effect",
    "impacto causal",
    "efecto causal",
    "prueba que",
    "demuestra que",
    "predicción independiente",
    "prediccion independiente",
    "external validation",
    "validación externa",
    "validacion externa",
    "test set independiente",
    "holdout",
    "train/test",
]

root = Path("FASE6/outputs/country_intelligence")
for p in root.rglob("*"):
    if p.is_file() and p.suffix.lower() in {".csv", ".md", ".json", ".yaml", ".txt"}:
        txt = p.read_text(encoding="utf-8", errors="ignore").lower()
        hits = [t for t in forbidden if t in txt]
        if hits:
            print(p, hits)
PY
```

### Interpretación

- Permitido si aparece para negar explícitamente causalidad/predicción.
- No permitido si se usa como afirmación activa.

### P0

- “Singapur lidera porque X causa Y”.
- “El modelo predice independientemente...”.
- “Validación externa demuestra...”.

---

## 37. Auditoría 30 — consistencia de semántica en CSVs

Ejecutar:

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd

ci = Path("FASE6/outputs/country_intelligence")
for p in ci.glob("*.csv"):
    df = pd.read_csv(p)
    print("\nFILE", p.name, df.shape)
    for col in ["score_scope", "independent_prediction", "causal_claim", "external_validation_used", "holdout_used"]:
        if col in df.columns:
            print(col, df[col].dropna().unique()[:10])
PY
```

### PASS

Si existen estas columnas, deben tener:

```text
score_scope = in_sample_descriptive_positioning / descriptive_regulatory_typology
independent_prediction = false
causal_claim = false
external_validation_used = false
holdout_used = false
```

### FAIL P0

Cualquier `true` en causalidad, predicción independiente, holdout o validación externa.

---

## 38. Script automático consolidado

DeepSeek puede ejecutar este script de auditoría rápida desde `F5_F8_MVP`:

```bash
python3 - <<'PY'
from pathlib import Path
import pandas as pd
import json

findings = []

def add(check, status, severity, evidence):
    findings.append({
        "check": check,
        "status": status,
        "severity": severity,
        "evidence": evidence,
    })

root = Path(".")
f6 = root / "FASE6"
out = f6 / "outputs"
ci = out / "country_intelligence"

# Original outputs
original = [
    "fase6_manifest.json",
    "q1_results.csv",
    "q2_results.csv",
    "q2_scores_per_country.csv",
    "q3_results.csv",
    "q4_clusters.csv",
    "q4_distance_matrix.csv",
    "q5_results.csv",
    "q5_scores_per_country.csv",
    "q6_results.csv",
    "q6_scores_per_country.csv",
]
for fname in original:
    p = out / fname
    add(f"original_output_exists_{fname}", "PASS" if p.exists() and p.stat().st_size > 0 else "FAIL", "P0", str(p))

# Base manifest
mp = out / "fase6_manifest.json"
if mp.exists():
    m = json.loads(mp.read_text())
    for k, expected in [
        ("methodology", "inferential_comparative_observational"),
        ("holdout_used", False),
        ("train_test_split_used", False),
        ("external_validation_used", False),
    ]:
        add(f"base_manifest_{k}", "PASS" if m.get(k) == expected else "FAIL", "P0", f"{m.get(k)}")
else:
    add("base_manifest_exists", "FAIL", "P0", "missing")

# Country intelligence exists
add("country_intelligence_dir_exists", "PASS" if ci.exists() else "FAIL", "P0", str(ci))

required_ci = [
    "country_q_profile_long.csv",
    "country_q_profile_wide.csv",
    "country_rankings_by_outcome.csv",
    "country_rankings_by_group.csv",
    "country_best_worst_by_q.csv",
    "country_model_contributions.csv",
    "country_residuals_and_gaps.csv",
    "country_cluster_profile.csv",
    "country_headline_flags.csv",
    "country_comparison_pairs.csv",
    "country_learning_patterns.csv",
    "country_graphics_catalog.csv",
    "phase6_2_country_intelligence_manifest.json",
    "phase6_2_quality_checks.csv",
    "README.md",
]
for fname in required_ci:
    p = ci / fname
    severity = "P0" if fname in ["country_q_profile_long.csv", "country_q_profile_wide.csv", "phase6_2_country_intelligence_manifest.json"] else "P1"
    add(f"ci_output_exists_{fname}", "PASS" if p.exists() and p.stat().st_size > 0 else "FAIL", severity, str(p))

# CI manifest
cip = ci / "phase6_2_country_intelligence_manifest.json"
if cip.exists():
    m = json.loads(cip.read_text())
    for k, expected in [
        ("methodology", "inferential_comparative_observational"),
        ("holdout_used", False),
        ("train_test_split_used", False),
        ("external_validation_used", False),
        ("independent_prediction", False),
        ("causal_claim", False),
        ("preserved_existing_fase6_outputs", True),
    ]:
        add(f"ci_manifest_{k}", "PASS" if m.get(k) == expected else "FAIL", "P0", f"{m.get(k)}")

# Profiles
for fname in ["country_q_profile_long.csv", "country_q_profile_wide.csv"]:
    p = ci / fname
    if not p.exists():
        continue
    df = pd.read_csv(p)
    add(f"{fname}_has_CHL", "PASS" if "CHL" in set(df.get("iso3", [])) else "FAIL", "P0", f"n_iso3={df.get('iso3', pd.Series()).nunique() if 'iso3' in df else 'NO_ISO3'}")
    add(f"{fname}_has_SGP", "PASS" if "SGP" in set(df.get("iso3", [])) else "FAIL", "P0", f"n_iso3={df.get('iso3', pd.Series()).nunique() if 'iso3' in df else 'NO_ISO3'}")
    if "independent_prediction" in df.columns:
        ok = df["independent_prediction"].fillna(False).eq(False).all()
        add(f"{fname}_independent_prediction_false", "PASS" if ok else "FAIL", "P0", str(df["independent_prediction"].dropna().unique()))
    if "causal_claim" in df.columns:
        ok = df["causal_claim"].fillna(False).eq(False).all()
        add(f"{fname}_causal_claim_false", "PASS" if ok else "FAIL", "P0", str(df["causal_claim"].dropna().unique()))
    if "score_scope" in df.columns:
        ok = df["score_scope"].astype(str).str.contains("in_sample|descriptive", case=False, na=False).all()
        add(f"{fname}_score_scope_descriptive", "PASS" if ok else "FAIL", "P0", str(df["score_scope"].dropna().unique()))

# Rankings
rp = ci / "country_rankings_by_outcome.csv"
if rp.exists():
    df = pd.read_csv(rp)
    qs = set(df.get("question_id", []))
    required_q = {"Q1", "Q2", "Q3", "Q5", "Q6"}
    add("rankings_cover_Q1_Q2_Q3_Q5_Q6", "PASS" if required_q.issubset(qs) else "FAIL", "P1", str(qs))

gp = ci / "country_rankings_by_group.csv"
if gp.exists():
    df = pd.read_csv(gp)
    add("group_rankings_has_group_name", "PASS" if "group_name" in df.columns else "FAIL", "P1", str(df.columns.tolist()))
    add("group_rankings_has_rank_within_group", "PASS" if "rank_within_group" in df.columns else "FAIL", "P1", str(df.columns.tolist()))

# Figures
fig = ci / "figures"
add("figures_dir_exists", "PASS" if fig.exists() else "FAIL", "P1", str(fig))
if fig.exists():
    pngs = list(fig.rglob("*.png"))
    add("figures_png_count_positive", "PASS" if len(pngs) > 0 else "FAIL", "P1", f"n_png={len(pngs)}")
    for rel in [
        "q_heatmaps/heatmap_country_by_q_percentiles.png",
        "country_cards/SGP_country_card_radar.png",
        "country_cards/CHL_country_card_radar.png",
        "chile_vs_benchmarks/chile_vs_singapore_q_profile.png",
    ]:
        add(f"figure_exists_{rel}", "PASS" if (fig / rel).exists() else "FAIL", "P1", str(fig / rel))

print(json.dumps(findings, indent=2, ensure_ascii=False))
PY
```

---

## 39. Matriz de criterios de aceptación

| Área | Criterio | Evidencia mínima | Severidad si falla |
|---|---|---|---|
| Preservación | 11 outputs originales existen | `ls`, script | P0 |
| Manifest base | No holdout/no split/no external validation | JSON | P0 |
| CI dir | `country_intelligence/` existe | `ls` | P0 |
| CI manifest | v2.2, no causal, no prediction | JSON | P0 |
| Profiles long | existe y tiene CHL/SGP | CSV | P0 |
| Profiles wide | existe y tiene CHL/SGP | CSV | P0 |
| Semántica | `independent_prediction=false` | CSV/JSON | P0 |
| Semántica | `causal_claim=false` | CSV/JSON | P0 |
| Rankings outcome | Q1/Q2/Q3/Q5/Q6 | CSV | P1 |
| Rankings group | rankings por submuestra | CSV | P1 |
| Best/worst | mejores y peores por Q | CSV | P1 |
| Drivers | contribuciones descriptivas | CSV | P1 |
| Residuals/gaps | observed vs fitted/gaps | CSV | P1/P2 |
| Q4 | tipología, no ranking normativo | CSV/README | P1 |
| Chile vs SGP | comparación explícita | CSV/figura | P1 |
| Gráficos | heatmap, rankings Q, radar CHL/SGP | PNG/SVG/catalog | P1 |
| Tests | test Fase 6.2 existe y pasa | pytest | P1 |
| README | cautela metodológica | README | P1 |
| Lenguaje | no causalidad activa | `rg` | P0/P1 |
| Fase 7 readiness | outputs consumibles por Fase 7 | CSVs | P1 |

---

## 40. Plantilla de informe final para DeepSeek V4 Pro

DeepSeek debe entregar un informe en Markdown con esta estructura:

```markdown
# Auditoría Fase 6 v2.2 Country Intelligence Layer — Research_AI_law

## 1. Dictamen ejecutivo
- Dictamen: APROBADA / APROBADA_CON_OBSERVACIONES / APROBADA_CONDICIONAL / RECHAZADA
- ¿Fase 6 v2.1+ base se preserva?: SÍ/NO
- ¿Fase 6.2 está implementada?: SÍ/NO
- ¿Puede pasar a Fase 7?: SÍ/NO
- ¿Puede alimentar Fase 8?: SÍ/NO, con/sin cautela
- Hallazgos P0/P1/P2/P3

## 2. Alcance auditado
- Ruta del repositorio
- Fecha/hora
- Archivos normativos usados
- Outputs revisados
- Comandos principales ejecutados

## 3. Verificación Fase 6 base
| Criterio | Resultado | Evidencia | Severidad |
|---|---|---|---|
| 11 outputs preservados | PASS/FAIL | ... | P0 |
| no holdout | PASS/FAIL | ... | P0 |
| no train/test | PASS/FAIL | ... | P0 |
| no external validation | PASS/FAIL | ... | P0 |

## 4. Verificación Fase 6.2
| Output | Existe | Shape | Observación | Severidad |
|---|---:|---:|---|---|
| country_q_profile_long.csv | ... | ... | ... | ... |
| country_q_profile_wide.csv | ... | ... | ... | ... |
| country_rankings_by_outcome.csv | ... | ... | ... | ... |
| country_rankings_by_group.csv | ... | ... | ... | ... |
| country_best_worst_by_q.csv | ... | ... | ... | ... |
| country_model_contributions.csv | ... | ... | ... | ... |
| country_residuals_and_gaps.csv | ... | ... | ... | ... |
| country_headline_flags.csv | ... | ... | ... | ... |
| country_learning_patterns.csv | ... | ... | ... | ... |
| graphics catalog | ... | ... | ... | ... |

## 5. Auditoría de países clave
### Chile
- Presente: SÍ/NO
- Perfil Q1-Q6: ...
- Comparaciones disponibles: ...
- Gaps principales: ...
- Observaciones:

### Singapur
- Presente: SÍ/NO
- Perfil Q1-Q6: ...
- ¿Permite explicar por qué es pionero descriptivo?: SÍ/NO
- Gráficos disponibles:
- Observaciones:

## 6. Auditoría de rankings y submuestras
- Rankings globales:
- Rankings LATAM:
- Rankings benchmarks Chile:
- Rankings pioneros:
- Mejores/peores por Q:
- Limitaciones:

## 7. Auditoría de gráficos
- Heatmap país × Q:
- Rankings Q1-Q6:
- Radar CHL:
- Radar SGP:
- Chile vs Singapur:
- Calidad visual:
- Observaciones:

## 8. Auditoría semántica
- independent_prediction=false:
- causal_claim=false:
- score_scope correcto:
- lenguaje prohibido:
- Q4 no normativo:
- Observaciones:

## 9. Tests
- Tests encontrados:
- Tests ejecutados:
- Resultado:
- Fallas:

## 10. Hallazgos detallados
### H-001
- Severidad:
- Criterio:
- Archivo/comando:
- Evidencia:
- Impacto:
- Acción recomendada:

## 11. Recomendaciones priorizadas
1. Corregir P0...
2. Corregir P1...
3. Mejoras P2/P3...

## 12. Conclusión final
Texto claro indicando si Fase 6.2 está lista para alimentar Fase 7 y Fase 8.
```

---

## 41. Plantilla JSON de dictamen

DeepSeek debe producir, si se solicita, un JSON con este formato:

```json
{
  "audit_name": "Fase 6 v2.2 Country Intelligence Layer Research_AI_law",
  "verdict": "APROBADA|APROBADA_CON_OBSERVACIONES|APROBADA_CONDICIONAL|RECHAZADA",
  "phase6_base_preserved": true,
  "country_intelligence_layer_present": true,
  "ready_for_phase7": true,
  "ready_for_phase8_inputs": true,
  "methodology_expected": "inferential_comparative_observational",
  "critical_checks": {
    "original_11_outputs_present": "PASS|FAIL|NO_VERIFICADO",
    "no_train_test_split": "PASS|FAIL|NO_VERIFICADO",
    "no_holdout": "PASS|FAIL|NO_VERIFICADO",
    "no_external_validation": "PASS|FAIL|NO_VERIFICADO",
    "country_intelligence_manifest_correct": "PASS|FAIL|NO_VERIFICADO",
    "country_q_profile_long_exists": "PASS|FAIL|NO_VERIFICADO",
    "country_q_profile_wide_exists": "PASS|FAIL|NO_VERIFICADO",
    "chile_present": "PASS|FAIL|NO_VERIFICADO",
    "singapore_present": "PASS|FAIL|NO_VERIFICADO",
    "rankings_by_outcome_exist": "PASS|FAIL|NO_VERIFICADO",
    "rankings_by_group_exist": "PASS|FAIL|NO_VERIFICADO",
    "best_worst_by_q_exist": "PASS|FAIL|NO_VERIFICADO",
    "graphics_exist": "PASS|FAIL|NO_VERIFICADO",
    "scores_are_in_sample_descriptive": "PASS|FAIL|NO_VERIFICADO",
    "no_independent_prediction_claims": "PASS|FAIL|NO_VERIFICADO",
    "no_causal_claims": "PASS|FAIL|NO_VERIFICADO",
    "phase6_2_tests_pass": "PASS|FAIL|NO_VERIFICADO"
  },
  "findings_count": {
    "P0": 0,
    "P1": 0,
    "P2": 0,
    "P3": 0
  },
  "blocking_findings": [],
  "recommended_actions": []
}
```

---

## 42. Prompt listo para DeepSeek V4 Pro

Usar este prompt junto con este blueprint:

```text
Actúa como auditor técnico-metodológico senior del proyecto Research_AI_law.

Debes auditar en modo solo lectura la actualización Fase 6 v2.2 Country Intelligence Layer, usando como norma el archivo BLUEPRINT_AUDITORIA_FASE6_V2_2_COUNTRY_INTELLIGENCE_DEEPSEEK.md y la auditoría previa FASE6V2.1-AUDITORIA.md.

No implementes, no corrijas y no regeneres outputs. Solo inspecciona archivos, comandos, CSVs, manifests, README, tests y gráficos.

Debes verificar dos cosas:

1. Que Fase 6 v2.1+ base se preservó: los 11 outputs originales existen, no hay split, no hay holdout, no hay validación externa, Q2/Q5/Q6 siguen con análisis primario continuo/fraccional, scores por país siguen siendo in-sample/descriptivos.

2. Que Fase 6.2 agregó correctamente Country Intelligence Layer: perfiles país-por-país Q1-Q6, rankings globales, rankings por grupo, mejores/peores por Q, drivers descriptivos, residuals/gaps, headline flags, learning patterns, comparación Chile vs Singapur, country cards, gráficos profesionales, manifest, tests y README.

Debes emitir dictamen APROBADA, APROBADA_CON_OBSERVACIONES, APROBADA_CONDICIONAL o RECHAZADA. Para cada hallazgo indica archivo/comando, evidencia observada, severidad P0-P3, impacto y acción recomendada.

Está prohibido afirmar que algo está correcto sin evidencia. Si no puedes verificar algo, marca NO_VERIFICADO.
```

---

## 43. Criterio final de cierre

Fase 6 v2.2 solo puede considerarse correctamente actualizada si el auditor puede afirmar todo lo siguiente:

```text
1. Los 11 outputs originales de Fase 6 v2.1+ siguen presentes.
2. El manifest base mantiene no split, no holdout, no external validation.
3. Existe FASE6/outputs/country_intelligence/.
4. Existe manifest Fase 6.2 y declara no causalidad/no predicción independiente.
5. Existen perfiles long y wide país-por-país.
6. Chile aparece en perfiles.
7. Singapur aparece en perfiles.
8. Hay rankings por outcome para Q1/Q2/Q3/Q5/Q6.
9. Hay rankings por grupo/submuestra.
10. Hay mejores y peores por Q.
11. Hay drivers descriptivos o justificación si no son estimables.
12. Hay residuals/gaps o justificación si no son estimables.
13. Hay comparación Chile vs Singapur.
14. Hay country cards data para Chile y Singapur.
15. Hay gráficos mínimos: heatmap, rankings Q, radar CHL, radar SGP, Chile vs Singapur.
16. Todos los scores/perfiles son in_sample_descriptive_positioning.
17. No hay independent_prediction=true.
18. No hay causal_claim=true.
19. Q4 se trata como tipología descriptiva, no ranking normativo causal.
20. Existen tests de Fase 6.2 y pasan o se documenta por qué no pudieron ejecutarse.
21. La capa está lista para que Fase 7 valide robustez y Fase 8 construya narrativa ejecutiva.
```

Si cualquiera de los puntos 1, 2, 4, 5, 6, 7, 16, 17 o 18 falla, el dictamen debe ser `RECHAZADA`.

---

## 44. Frase esperada del auditor si todo está correcto

> Fase 6 v2.2 queda aprobada como extensión país-por-país de Fase 6 v2.1+. La fase base conserva la metodología inferencial-comparativa sin split, sin holdout y sin validación externa. La nueva Country Intelligence Layer agrega perfiles Q1-Q6, rankings globales y por grupo, mejores/peores por pregunta, drivers descriptivos, brechas, country cards y gráficos, preservando la semántica de posicionamiento descriptivo in-sample. Chile y Singapur están presentes y comparables. La capa no afirma causalidad ni predicción independiente y queda lista para ser validada por Fase 7 antes de alimentar Fase 8.

---

**Fin del blueprint de auditoría Fase 6 v2.2 Country Intelligence Layer para DeepSeek V4 Pro.**
