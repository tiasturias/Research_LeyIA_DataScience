# Anthropic Economic Index — Unified Dataset

## Descripción

Dataset unificado del repositorio [Anthropic/EconomicIndex](https://huggingface.co/datasets/Anthropic/EconomicIndex) (Hugging Face, MIT license). Contiene **~344 MB de datos originales** distribuidos en **80+ archivos** de 6 releases, consolidados en un solo dataset SQLite + Excel con trazabilidad completa.

**Tamaño total unificado:** 640 MB SQLite / 7.2 MB Excel  
**Filas totales:** ~1,474,000  
**Tablas:** 21 (1 central long, 2 wide, 4 dimensiones, 11 hechos, 3 metadata)

---

## Tabla de Contenido

1. [¿Qué es el Anthropic Economic Index?](#1-qué-es-el-anthropic-economic-index)
2. [Arquitectura del Dataset](#2-arquitectura-del-dataset)
3. [Esquema de Tablas](#3-esquema-de-tablas)
4. [Guía de Uso — SQLite](#4-guía-de-uso--sqlite)
5. [Guía de Uso — Excel](#5-guía-de-uso--excel)
6. [Cómo Unir con Otras Fuentes](#6-cómo-unir-con-otras-fuentes)
7. [Auditoría y Verificación](#7-auditoría-y-verificación)
8. [Proceso de Unificación](#8-proceso-de-unificación)
9. [Contexto para LLM](#9-contexto-para-llm)
10. [Limitaciones](#10-limitaciones)

---

## 1. ¿Qué es el Anthropic Economic Index?

El **Anthropic Economic Index (AEI)** es un índice económico que mide cómo se utiliza la IA (específicamente Claude) en actividades económicas reales. Está basado en conversaciones anónimas de Claude.ai y la API de Anthropic, categorizadas por:

- **Tipo de interacción:** directiva, feedback loop, task iteration, validation, learning
- **Tarea O*NET:** clasificación ocupacional estándar de EE.UU.
- **Cluster de tareas:** 3 niveles jerárquicos de categorización
- **Geografía:** global, país, estado de EE.UU.
- **Plataforma:** 1P API, Claude AI (Free + Pro)
- **Período:** agosto 2025, noviembre 2025, febrero 2026 (3 ventanas)

**Paper de referencia:** [arxiv: 2503.04761](https://arxiv.org/abs/2503.04761)

---

## 2. Arquitectura del Dataset

```
Source Files (80 archivos, ~344 MB)
│
├── labor_market_impacts/          (2 CSVs)
├── release_2025_02_10/            (7 CSVs + plots)
├── release_2025_03_27/            (13 CSVs + 1 TSV)
├── release_2025_09_15/            (24 CSVs + 2 JSON + código)
├── release_2026_01_15/            (2 CSVs + PDF)
├── release_2026_03_24/            (2 CSVs)
│
└── build_unified_dataset.py
        │
        ▼
┌─────────────────────────────────────────────────────┐
│             UNIFIED DATASET (Star Schema)            │
├─────────────────────────────────────────────────────┤
│                                                      │
│  CENTRAL FACT (LONG)                                 │
│  ┌─────────────────────────────────────────────┐    │
│  │  aei_metrics_long       ~1,400,819 rows     │    │
│  │  geo_id × date × platform × variable × val  │    │
│  └─────────────────────────────────────────────┘    │
│           │ pivot                       │           │
│           ▼                            ▼            │
│  ┌──────────────────┐  ┌────────────────────────┐   │
│  │ aei_metrics_wide │  │ aei_metrics_wide_by_cl │   │
│  │ 2,927 rows × 179 │  │ 2,104 rows × 19 cols   │   │
│  └──────────────────┘  └────────────────────────┘   │
│                                                      │
│  DIMENSIONS           │   FACTS (aux)               │
│  ┌──────────────┐     │   ┌──────────────────┐      │
│  │ dim_occupation│     │   │fact_auto_tasks   │      │
│  │ 1,596 rows    │     │   │3,364 rows        │      │
│  ├──────────────┤     │   ├──────────────────┤      │
│  │ dim_onet_task │     │   │fact_penetration  │      │
│  │ 19,530 rows   │     │   │17,998 rows       │      │
│  ├──────────────┤     │   ├──────────────────┤      │
│  │ dim_geography │     │   │fact_labor_market │      │
│  │ 304 rows      │     │   │1,868 rows        │      │
│  ├──────────────┤     │   ├──────────────────┤      │
│  │ dim_cluster   │     │   │fact_cluster_prof │      │
│  │ 970 rows      │     │   │630 rows          │      │
│  └──────────────┘     │   ├──────────────────┤      │
│                        │   │fact_gdp_economic │      │
│  METADATA              │   │194 rows          │      │
│  ┌─────────────────┐   │   ├──────────────────┤      │
│  │ data_lineage    │   │   │fact_demographics │      │
│  │ 18 entries      │   │   │13,572 rows       │      │
│  ├─────────────────┤   │   └──────────────────┘      │
│  │ column_descriptions│                              │
│  │ 361 rows          │                               │
│  ├─────────────────┤                                  │
│  │ source_manifest │                                  │
│  │ 80 files        │                                  │
│  └─────────────────┘                                  │
└─────────────────────────────────────────────────────┘
```

---

## 3. Esquema de Tablas

### 3.1 Tabla Central — `aei_metrics_long` (~1.4M rows)

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `geo_id` | text | Código geográfico (ISO-3, "GLOBAL", "US-AL") |
| `geography` | text | Tipo: global, country, state_us |
| `date_start` | text | Inicio del período |
| `date_end` | text | Fin del período |
| `platform_and_product` | text | "1P API" o "Claude AI (Free and Pro)" |
| `facet` | text | Dimensión: collaboration, onet_task, request |
| `level` | int | Nivel jerárquico (0, 1, 2) |
| `variable` | text | Métrica: collaboration_count, collaboration_pct, etc. |
| `cluster_name` | text | Nombre del cluster de tareas |
| `value` | float | Valor numérico |
| `_source_release` | text | Release de origen |
| `_origin_file` | text | **Archivo exacto de origen** |
| `_origin_line` | int | **Línea exacta en el archivo origen** |
| `geo_name` | text | Nombre geográfico legible |

### 3.2 Tabla Wide Agregada — `aei_metrics_wide` (2,927 rows × 179 cols)

Una fila por combinación `geo_id × date_start × date_end × platform_and_product`. Las variables están pivoteadas a columnas. Para counts se suman a través de clusters, para pcts se promedian.

### 3.3 Tabla Wide por Cluster — `aei_metrics_wide_by_cluster` (2,104 rows)

Una fila por combinación geografía × fecha × plataforma, con columnas para `cluster_{nombre}_{variable}`. Solo incluye `collaboration` level 0.

### 3.4 Dimensiones

| Tabla | Filas | Propósito |
|-------|-------|-----------|
| `dim_occupation` | 1,596 | Taxonomía SOC (Major → Minor → Broad → Detailed → O*NET-SOC) |
| `dim_onet_task` | 19,530 | Catálogo completo de tareas O*NET con descripciones |
| `dim_geography` | 304 | Códigos ISO (252 países) + estados US + global |
| `dim_cluster_hierarchy` | 970 | Jerarquía 3 niveles de clusters desde JSON trees |

### 3.5 Tablas de Hechos Auxiliares

| Tabla | Filas | Origen | Columnas clave |
|-------|-------|--------|----------------|
| `fact_automation_tasks` | 3,364 | `automation_vs_augmentation_by_task.csv` | task_name, directive, feedback_loop, task_iteration, validation, learning, filtered |
| `fact_task_penetration` | 17,998 | `task_penetration.csv` | task, penetration (0.0 a 1.0) |
| `fact_labor_market` | 1,868 | `job_exposure.csv` + `wage_data.csv` + `bls_employment.csv` | occ_code, observed_exposure, median_salary, wage_group, job_forecast |
| `fact_cluster_profiles` | 630 | `cluster_level_dataset.tsv` | cluster_name, percent_records, percent_users, onet_task, collaboration_ratios, has_thinking_ratio |
| `fact_gdp_economic` | 194 | `gdp_2024_country.csv` + `working_age_pop.csv` | iso_alpha_3, gdp_total, year, working_age_pop |
| `fact_gdp_us_state` | 105 | `bea_us_state_gdp_2024.csv` + `working_age_pop_us.csv` | state_code, state_name, gdp_total, working_age_pop |
| `fact_task_percentages` | 4,098 | `task_pct_v1.csv` + `v2.csv` + `thinking_fractions.csv` | task_name, pct_v1, pct_v2, thinking_fraction |
| `fact_demographics_us` | 13,572 | `sc-est2024-agesex-civ.csv` | Census 2024: población US por edad/sexo/estado |
| `fact_onet_task_mappings_aggregated` | 3,514 | `onet_task_mappings.csv` | task_name, pct |
| `fact_automation_vs_augmentation_summary` | 6 | `automation_vs_augmentation*.csv` | interaction_type (directive, feedback loop, etc.), pct, version |
| `fact_workforce_demographics` | 266 | `working_age_pop_raw.csv` | World Bank: población en edad de trabajar por país |

### 3.6 Tablas de Metadata

| Tabla | Filas | Propósito |
|-------|-------|-----------|
| `data_lineage` | 18 | Mapea cada tabla de salida a sus archivos fuente (con SHA256) |
| `metadata_column_descriptions` | 361 | Diccionario: cada columna de cada tabla con tipo de dato, % no nulo, valores de ejemplo |
| `metadata_row_counts` | 36 | Log de conteo de filas originales vs destino |

---

## 4. Guía de Uso — SQLite

### Conexión

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("antrophic_economic_index.db")
```

### Consultas de ejemplo

```sql
-- Top 10 clusters por uso global (colaboración)
SELECT cluster_name, SUM(value) as total
FROM aei_metrics_long
WHERE geography = 'global'
  AND variable = 'collaboration_count'
  AND facet = 'collaboration'
GROUP BY cluster_name
ORDER BY total DESC
LIMIT 10;
```

```sql
-- Exposición laboral a IA por ocupación (top 20)
SELECT o.title, o.major_group, je.observed_exposure
FROM fact_labor_market je
JOIN dim_occupation o ON je.occ_code = o.detailed_occupation
WHERE je.observed_exposure IS NOT NULL
ORDER BY je.observed_exposure DESC
LIMIT 20;
```

```sql
-- ¿Qué países tienen más adopción de IA? (colaboración total por país)
SELECT geo_name, date_start, SUM(value) as total_collaborations
FROM aei_metrics_long
WHERE geography = 'country'
  AND variable = 'collaboration_count'
  AND platform_and_product = 'Claude AI (Free and Pro)'
GROUP BY geo_id, date_start
ORDER BY total_collaborations DESC
LIMIT 20;
```

```sql
-- Verificar un valor específico contra su origen
SELECT cluster_name, value, _origin_file, _origin_line
FROM aei_metrics_long
WHERE variable = 'collaboration_count'
  AND geo_id = 'CHL'
  AND platform_and_product = 'Claude AI (Free and Pro)'
LIMIT 5;
```

### Verificación de proveniencia

```python
# Para AUDITAR cualquier valor:
valor = conn.execute("""
    SELECT value, _origin_file, _origin_line
    FROM aei_metrics_long
    WHERE geo_id = 'CHL' AND variable = 'collaboration_count'
    LIMIT 1
""").fetchone()

print(f"Valor: {valor[0]}")
print(f"Origen: {valor[1]}, línea {valor[2]}")
# → Abrir EconomicIndex/{origen} en línea {línea} para verificar
```

---

## 5. Guía de Uso — Excel

### Hojas disponibles

| Hoja | Filas | Columnas | Qué contiene |
|------|-------|----------|-------------|
| `README` | — | 1 | Esta documentación |
| `aei_metrics_wide` | 2,927 | 179 | AEI agregado por geo × fecha × plataforma |
| `aei_metrics_wide_by_cluster` | 2,104 | 19 | AEI por cluster individual |
| `dim_occupation` | 1,596 | 8 | Taxonomía SOC completa |
| `dim_onet_task` | 19,530 | 10 | Catálogo O*NET |
| `dim_geography` | 304 | 9 | Códigos ISO + estados |
| `dim_cluster_hierarchy` | 970 | 9 | Jerarquía de clusters |
| `data_lineage` | 18 | 5 | Linaje de datos |
| `fact_automation_tasks` | 3,364 | 9 | Scores de automatización |
| `fact_task_penetration` | 17,998 | 4 | Penetración por tarea |
| `fact_labor_market` | 1,868 | 17 | Exposición + salarios |
| `fact_cluster_profiles` | 630 | 18 | Perfiles de clusters |
| `fact_gdp_economic` | 194 | 11 | GDP por país |
| `fact_gdp_us_state` | 105 | 8 | GDP por estado |
| `fact_task_percentages` | 4,098 | 10 | % de tareas v1+v2+thinking |
| `fact_demographics_us` | 13,572 | 15 | Demografía US 2024 |
| `fact_onet_task_mappings_aggrega` | 3,514 | 4 | Mappings tarea→% |
| `fact_automation_vs_augmentation` | 6 | 5 | Resumen global auto |
| `fact_workforce_demographics` | 266 | 12 | World Bank raw |
| `metadata_column_descriptions` | 361 | 7 | Diccionario de columnas |
| `metadata_row_counts` | 36 | 3 | Log de verificación |

**Nota:** `aei_metrics_long` (~1.4M rows) solo está en SQLite por límite de tamaño de Excel.

---

## 6. Cómo Unir con Otras Fuentes

Para integrar datos externos (ej: IAPP AI Law Tracker, Oxford Insights, Banco Mundial):

### Por país (ISO-3)

```python
# Tu fuente externa tiene columna 'iso3'
# El campo de unión es dim_geography.iso_alpha_3

import pandas as pd
import sqlite3

conn = sqlite3.connect("antrophic_economic_index.db")
dim_geo = pd.read_sql("SELECT * FROM dim_geography", conn)
aei = pd.read_sql("""
    SELECT * FROM aei_metrics_long 
    WHERE geography = 'country'
""", conn)

# Unir con tu dataset externo
# merged = pd.merge(tu_data, aei, left_on='iso3', right_on='geo_id')
```

### Por ocupación (SOC)

```python
# Unir fact_labor_market con dim_occupation por detailed_occupation
# O fact_automation_tasks con dim_onet_task por task_name
```

### Estrategia general

1. Identificar la granularidad común (país, ocupación, tarea, año)
2. Usar la columna `geo_id` (para países son códigos ISO-3166 alpha-3)
3. Para países, `dim_geography` tiene `iso_alpha_2`, `iso_alpha_3`, y `country_name`

---

## 7. Auditoría y Verificación

### Para auditar CUALQUIER valor del dataset:

```
1. Localiza el valor en la tabla deseada
2. Lee las columnas _origin_file y _origin_line
3. Abre EconomicIndex/{_origin_file}
4. Ve a la línea _origin_line (línea 1 = header)
5. El valor DEBE coincidir exactamente
6. Calcula SHA256 del archivo:
   shasum -a 256 EconomicIndex/{_origin_file}
7. Compara con source_files_manifest.csv
```

### Garantías:

- **CERO datos sintéticos**: cada valor proviene de su archivo original
- **CERO imputación**: los valores nulos son nulos originales
- **CERO estimación**: no se infirió ningún valor faltante
- **TRAZABILIDAD TOTAL**: cada celda tiene `_origin_file` + `_origin_line`
- **VERIFICABLE**: el manifiesto SHA256 prueba que los archivos fuente no han sido alterados

---

## 8. Proceso de Unificación

### Paso a paso

1. **Lectura**: los 80+ archivos se leen con `pandas.read_csv()`, preservando números de línea originales
2. **Normalización**: nombres de columnas a lowercase_underscore
3. **Unificación AEI**: los 6 archivos AEI raw (3 períodos × 2 plataformas) se concatenan en `aei_metrics_long`
4. **Enriquecimiento**: `geo_name` se agrega desde el archivo enriched
5. **Pivoteo**: `aei_metrics_wide` agrega por variable (sum para counts, mean para pcts); `aei_metrics_wide_by_cluster` mantiene granularidad por cluster
6. **Dimensiones**: se construyen desde archivos separados (SOC, O*NET, ISO, JSON trees)
7. **Hechos**: tablas auxiliares se construyen desde sus archivos fuente
8. **Metadata**: `data_lineage` documenta qué archivos originaron cada tabla; `metadata_column_descriptions` documenta cada columna
9. **SHA256**: todos los archivos fuente se hashean en `source_files_manifest.csv`
10. **Escritura**: SQLite + Excel

### Lo que NO se hizo

- ❌ No se generaron datos sintéticos
- ❌ No se imputaron valores faltantes
- ❌ No se estimaron/infirieron datos
- ❌ No se modificaron valores originales
- ❌ No se eliminaron filas (excepto duplicados exactos en dim_onet_task)
- ✅ Se preservaron todos los datos originales

---

## 9. Contexto para LLM

> **Instrucciones para asistentes LLM que trabajen con este dataset:**
>
> Este dataset contiene el Anthropic Economic Index unificado. Está compuesto por 21 tablas en SQLite (~640 MB) con ~1.47 millones de filas de datos reales, todos provenientes del repositorio Hugging Face Anthropic/EconomicIndex.
>
> **Estructura clave:**
> - `aei_metrics_long` es la tabla central: formato largo (tidy), cada fila = 1 medición de uso de IA para una combinación de geografía, fecha, plataforma, variable y cluster de tarea
> - La columna `variable` contiene métricas como collaboration_count, collaboration_pct, request_count, completion_tokens_count, etc.
> - La columna `cluster_name` contiene ~1,400 nombres descriptivos de clusters de tareas (ej: "Write and debug code", "Analyze documents", "Create marketing content")
> - Disponible para 3 períodos: ago2025, nov2025, feb2026
> - 2 plataformas: 1P API (uso programático) y Claude AI (uso directo)
> - 4 niveles geográficos: global, país (252), estado US (50+DC)
>
> **Para unir con datos externos:**
> - Por país: usar `geo_id` = ISO 3166-1 alpha-3
> - Por ocupación: `dim_occupation.detailed_occupation` es código SOC
> - Por tarea: `dim_onet_task.onet_soc_code` y `task` (descripción)
>
> **Auditoría:** toda tabla de datos tiene `_origin_file` y `_origin_line` para verificar cada valor en su archivo original. El `source_files_manifest.csv` contiene SHA256 de cada archivo fuente.
>
> **Limitaciones:** solo 3 períodos de 1 semana cada uno; ~73% de países tienen datos de Claude AI; los países con 0 uso tienen `value = 0.0` (no null).
>
> **Sin datos sintéticos.** Todo valor es real y trazable.

---

## 10. Limitaciones

1. **Cobertura temporal**: solo 3 ventanas de 1 semana (ago2025, nov2025, feb2026). No es una serie de tiempo continua.
2. **Cobertura geográfica**: los datos de Claude AI cubren ~73% de países. Países sin datos tienen valor 0.0.
3. **Sesgo de plataforma**: 1P API representa uso programático; Claude AI representa uso directo. No son directamente comparables sin normalización.
4. **Agregación**: `aei_metrics_wide` suma counts y promedia pcts a través de clusters. Para granularidad por cluster, usar `aei_metrics_long` o `aei_metrics_wide_by_cluster`.
5. **Nulos en merged tables**: tablas como `fact_gdp_economic` tienen nulos cuando un país tiene GDP pero no working_age_pop (o viceversa). Son nulos originales.
6. **Causalidad**: el AEI mide correlación, no causalidad. No se pueden inferir relaciones causales entre uso de IA y variables económicas.
7. **Tamaño**: `aei_metrics_long` (~1.4M rows) no cabe en Excel. Usar SQLite para consultas completas.

---

## Licencia

MIT (misma que el dataset fuente [Anthropic/EconomicIndex](https://huggingface.co/datasets/Anthropic/EconomicIndex))

## Créditos

- **Anthropic** — Economic Index dataset y paper
- **Hugging Face** — Plataforma de hosting del dataset

---

*Generado el 2026-05-04 por el script `build_unified_dataset.py`*
