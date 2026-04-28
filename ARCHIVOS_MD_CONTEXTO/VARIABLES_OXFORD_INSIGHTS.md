# Variables Oxford Insights - Government AI Readiness Index

## Proposito

Este documento consolida, con criterio de auditoria, la trazabilidad completa de la fuente Oxford Insights usada para construir la variable `ai_readiness_score` del estudio.

Su objetivo es dejar documentado de forma profesional:
- que se extrajo exactamente;
- desde que URLs y activos oficiales se obtuvo;
- como se transformo cada edicion en tablas comparables;
- que archivos finales se generaron;
- que controles de calidad se ejecutaron;
- que limitaciones metodologicas siguen vigentes.

## Resumen Ejecutivo

Oxford Insights aporta la variable target de preparacion gubernamental `ai_readiness_score`, definida como el score global reportado por el Government AI Readiness Index.

La fuente fue explotada al maximo disponible en formato estructurado oficial:
- se identificaron activos oficiales via landing pages y WordPress media API publica;
- se descargaron y archivaron datasets XLSX para 2019, 2020, 2021, 2022, 2023 y 2025;
- se archivaron los reportes PDF oficiales 2019-2025 y el methodology report 2025;
- se normalizaron 1,095 registros pais-anio con 100.0% de mapeo ISO3;
- se construyeron 7 tablas operativas para auditoria, panel, muestra, snapshot y vistas long;
- se documento explicitamente el gap 2024: PDF oficial disponible, pero sin XLSX/CSV publico discoverable al 2026-04-08;
- se detecto y resolvio un problema de versionado en 2025: el adjunto oficial `data.xlsx` quedo archivado porque no coincidia con el dashboard publico, y el output final usa el adjunto oficial mas reciente `data-1.xlsx`.

En la muestra del estudio, la cobertura final es:
- 86 de 86 paises en 2019, 2021, 2022, 2023 y 2025;
- 85 de 86 paises en 2020, con unica ausencia de Taiwan (`TWN`).

## Fuente Y Proveniencia

| campo | detalle |
|---|---|
| emisor | Oxford Insights |
| producto | Government AI Readiness Index |
| familia fuente | AI Readiness |
| landing principal | `https://oxfordinsights.com/ai-readiness/government-ai-readiness-index/` |
| landing 2025 verificada | `https://oxfordinsights.com/ai-readiness/government-ai-readiness-index-2025/` |
| discovery estructurado | `https://oxfordinsights.com/wp-json/wp/v2/media?search=Government%20AI%20Readiness&per_page=100` |
| discovery complementario | `https://oxfordinsights.com/wp-json/wp/v2/media?search=public%20data&per_page=100` |
| tipo de acceso | landing publica + WordPress media API publica |
| API publica tabular | No hay API de datos dedicada; se uso media API para descubrir activos oficiales |
| formatos explotados | XLSX, PDF, HTML, JSON |
| anios estructurados integrados | 2019, 2020, 2021, 2022, 2023, 2025 |
| gap estructurado | 2024 |
| fecha de extraccion | 2026-04-08 |
| notebook de extraccion | `notebooks/01_recoleccion.ipynb` |
| carpeta de salida | `data/raw/Oxford Insights/` |

## Activos Oficiales Inventariados

El manifiesto final `download_manifest.csv` contiene 19 entradas:
- 18 activos publicamente accesibles descargados y archivados;
- 1 marcador explicito de gap estructurado para 2024.

### Activos estructurados y documentales por anio

| anio | dataset estructurado | reporte PDF | metodologia | observacion |
|---|---|---|---|---|
| 2019 | `2019_government_ai_readiness_index_dataset.xlsx` | si | no separado | Estructura antigua, score original 0-10 |
| 2020 | `2020_government_ai_readiness_index_public_dataset.xlsx` | si | no separado | 3 pilares, 9 dimensiones |
| 2021 | `2021_government_ai_readiness_index_public_dataset.xlsx` | si | no separado | 3 pilares, 9 dimensiones |
| 2022 | `2022_government_ai_readiness_index_public_data.xlsx` | si | no separado | 3 pilares, 9 dimensiones |
| 2023 | `2023_government_ai_readiness_index_public_dataset.xlsx` | si | no separado | 3 pilares, 9 dimensiones |
| 2024 | **ninguno** — Oxford no publico XLSX/CSV para esta edicion | si — `2024_government_ai_readiness_index.pdf` archivado en `reports/` | no separado | **Gap estructurado resuelto por extraccion PDF**: el PDF contiene tablas structuradas en paginas 43-50. Datos extraidos con `pdfplumber` el 2026-04-08: 188 paises, score + 3 pilares. Sin dimensiones (no publicadas en PDF). Ver seccion "Gap 2024" en Limitaciones. `source_tier=official_pdf_extracted`. |
| 2025 | `2025_government_ai_readiness_index_data.xlsx` | si | `2025_methodology_report.pdf` | Canonico final alimentado por el adjunto oficial `data-1.xlsx` |

### Caso especial 2025: adjunto inicial vs adjunto vigente

Se identificaron dos adjuntos oficiales distintos para 2025:

| activo | rol | URL oficial | estado en el repositorio |
|---|---|---|---|
| `2025-Government-AI-Readiness-Index-data.xlsx` | adjunto publico inicial | `https://oxfordinsights.com/wp-content/uploads/2026/01/2025-Government-AI-Readiness-Index-data.xlsx` | archivado como `2025_government_ai_readiness_index_data_initial.xlsx` |
| `2025-Government-AI-Readiness-Index-data-1.xlsx` | adjunto oficial mas reciente | `https://oxfordinsights.com/wp-content/uploads/2026/01/2025-Government-AI-Readiness-Index-data-1.xlsx` | canonico final usado en outputs |

Motivo de la decision:
- el adjunto inicial no replicaba los valores publicados en el dashboard 2025;
- el adjunto `data-1.xlsx` si reproduce exactamente los spot-checks oficiales validados para USA, CAN, FRA, GBR y SAU;
- por auditoria, el adjunto inicial se conserva como archivo historico y el canonico queda alineado con el dashboard publico.

## Variable Canonica Y Campos Auxiliares

### Variable canonica del estudio

| campo | detalle |
|---|---|
| canonical_name | `ai_readiness_score` |
| nombre funcional en la fuente | Government AI Readiness overall score |
| definicion operativa | score global de preparacion gubernamental para adopcion y gobernanza de IA |
| rol metodologico | Y complementaria / target institucional |
| unidad canonica | indice 0-100 |
| cobertura temporal | 2019, 2020, 2021, 2022, 2023, 2024, 2025 |
| granularidad | pais |

### Campos auxiliares relevantes conservados

| campo | descripcion |
|---|---|
| `ai_readiness_score_original` | score tal como viene en la edicion original de Oxford |
| `score_scale_original` | escala original reportada (`0_to_10` o `0_to_100`) |
| `oxford_rank_reported` | ranking oficial reportado por Oxford |
| `iso3` | codigo ISO 3166-1 alpha-3 normalizado |
| `country_name_oxford` | nombre del pais tal como aparece en Oxford |
| `country_name_std` | nombre estandarizado |
| `methodology_regime` | version metodologica aplicada a esa edicion |
| `comparability_group` | bandera de comparabilidad interanual |
| `report_url` | URL exacta del reporte PDF oficial |
| `data_asset_url` | URL exacta del XLSX oficial efectivamente usado |
| `methodology_url` | URL del methodology report cuando existe |

## Regimenes Metodologicos Y Comparabilidad

| periodo | regime | estructura | escala | tratamiento ETL |
|---|---|---|---|---|
| 2019 | `v1_2019_4_clusters_12_indicators_scale_0_to_10` | 4 clusters, 12 indicadores | 0-10 | se preserva `ai_readiness_score_original` y se armoniza `ai_readiness_score = original * 10` |
| 2020-2023 | `v2_2020_2023_3_pillars_9_dimensions_scale_0_to_100` | 3 pilares, 9 dimensiones | 0-100 | comparable de forma moderada dentro del bloque 2020-2023 |
| 2025 | `v3_2025_6_pillars_14_dimensions_scale_0_to_100` | 6 pilares, 14 dimensiones | 0-100 | se conserva en el panel con flag de cambio metodologico fuerte |

Interpretacion recomendada:
- 2019 sirve como baseline historico, pero su comparabilidad con 2020+ es baja;
- 2020-2023 forman el bloque mas estable para comparaciones temporales;
- 2025 no debe interpretarse como continuidad estricta de 2023 por el rediseño metodologico.

## Inventario De Tablas Generadas

| archivo | nivel | descripcion | filas | llave principal |
|---|---|---|---|---|
| `download_manifest.csv` | metadata | inventario de activos, estados y URLs | 19 | `year`, `asset_kind`, `relative_path` |
| `oxford_ai_readiness_all_raw.csv` | raw global | tabla audit-rich con metadata completa y todas las columnas recuperadas | 1095 | `year`, `iso3` |
| `oxford_ai_readiness_wide.csv` | wide | export limpio para modelado y joins | 1095 | `year`, `iso3` |
| `oxford_ai_readiness_study.csv` | raw muestra | subconjunto de la muestra de 86 paises | 515 | `year`, `iso3` |
| `oxford_ai_readiness_long.csv` | long | tabla larga multi-indicador | 20108 | `year`, `iso3`, `indicator` |
| `oxford_ai_readiness_snapshot_latest.csv` | snapshot | ultimo anio disponible (2025) | 195 | `iso3` |
| `oxford_ai_readiness_pillars_long.csv` | long pilares | solo pilares para 2020-2023 y 2025 | 3288 | `year`, `iso3`, `indicator` |
| `oxford_ai_readiness_dimensions_long.csv` | long dimensiones | solo dimensiones para 2020-2023 y 2025 | 9777 | `year`, `iso3`, `indicator` |

## Diccionario Operativo De Columnas

### Metadata comun en outputs wide/raw

| columna | descripcion |
|---|---|
| `year` | anio de la edicion integrada |
| `iso3` | ISO3 normalizado |
| `country_name_std` | nombre estandarizado del pais |
| `country_name_oxford` | nombre original Oxford |
| `source_name` | identificador fijo de la fuente |
| `source_dataset` | nombre del archivo XLSX de origen |
| `report_edition` | etiqueta anual de la edicion |
| `report_url` | PDF oficial asociado |
| `data_asset_url` | XLSX oficial exacto usado |
| `methodology_url` | PDF metodologico si aplica |
| `source_tier` | `official_primary` o `official_archive` |
| `coverage_level` | nivel de observacion, fijado en `country` |
| `methodology_regime` | version metodologica |
| `comparability_group` | nivel de comparabilidad sugerido |

### Campos canonicos y de auditoria

| columna | descripcion |
|---|---|
| `ai_readiness_score` | score armonizado a 0-100 usado como variable canonica |
| `ai_readiness_score_original` | score reportado originalmente |
| `score_scale_original` | escala original del score |
| `oxford_rank_reported` | ranking reportado por Oxford |

### Bloques de indicadores recuperados

| bloque | columnas principales |
|---|---|
| 2019 clusters e indicadores | `cluster_avg_*`, `indicator_*`, `normalized_*` |
| 2020-2023 pilares | `pillar_government`, `pillar_technology_sector`, `pillar_data_and_infrastructure` |
| 2020-2023 dimensiones | `dimension_vision`, `dimension_governance_and_ethics`, `dimension_digital_capacity`, `dimension_adaptability`, `dimension_size`, `dimension_innovation_capacity`, `dimension_human_capital`, `dimension_infrastructure`, `dimension_data_availability`, `dimension_data_representativeness`, `dimension_maturity` |
| 2025 pilares | `pillar_policy_capacity`, `pillar_ai_infrastructure`, `pillar_governance`, `pillar_public_sector_adoption`, `pillar_development_and_diffusion`, `pillar_resilience` |
| 2025 dimensiones | `dimension_policy_vision`, `dimension_policy_commitment`, `dimension_compute_capacity`, `dimension_enabling_technical_infrastructure`, `dimension_data_quality`, `dimension_governance_principles`, `dimension_regulatory_compliance`, `dimension_government_digital_policy`, `dimension_e_government_delivery`, `dimension_ai_sector_maturity`, `dimension_ai_technology_diffusion`, `dimension_societal_transition`, `dimension_safety_and_security` |

### Estructura del long master

`oxford_ai_readiness_long.csv` conserva 21 columnas con esta logica:
- identificacion: `iso3`, `country_name_std`, `country_name_oxford`, `year`;
- metadata de fuente: `source_name`, `source_dataset`, `report_url`, `data_asset_url`, `methodology_url`, `source_tier`, `coverage_level`, `report_edition`, `methodology_regime`, `comparability_group`, `score_scale_original`;
- observacion: `indicator`, `value`, `source_variable_original`, `indicator_group`, `unit_original`.

## Metodologia De Extraccion Y Transformacion

### Flujo aplicado

1. Se inspeccionaron las landings oficiales de Oxford Insights y se confirmo que el sitio usa WordPress.
2. Se consulto la media API publica para descubrir los `source_url` oficiales de datasets, reportes y metodologia.
3. Se creo un manifiesto auditable con cada activo, URL, tamano, estado y fecha UTC de descarga.
4. Se descargo cada XLSX y PDF oficial a `data/raw/Oxford Insights/`.
5. Se inspecciono la estructura de hojas por anio y se construyeron parsers separados para 2019 y para 2020+.
6. Se mapearon nombres de pais a ISO3 con diccionario Oxford especifico mas `pycountry` como fallback.
7. Se harmonizo el score 2019 de 0-10 a 0-100, preservando la escala original para auditoria.
8. Se consolidaron outputs wide, long, study, snapshot y vistas de pilares/dimensiones.
9. Se aplico hotfix explicito para 2025 usando el adjunto oficial `data-1.xlsx`, conservando el adjunto previo como archivo historico.

### Decisiones de estandarizacion

| decision | implementacion |
|---|---|
| variable canonica | `ai_readiness_score` en escala 0-100 |
| preservacion del original | `ai_readiness_score_original` y `score_scale_original` |
| comparabilidad interanual | via `methodology_regime` y `comparability_group` |
| criterio de llave | unicidad obligatoria en `year + iso3` |
| cobertura de muestra | filtro contra los 86 paises del estudio |
| metadata 2025 | `data_asset_url` alineado al adjunto oficial `data-1.xlsx` |

## Cobertura Final

### Cobertura global por anio

| anio | paises | min_score | max_score | mean_score |
|---|---|---|---|---|
| 2019 | 194 | 1.68 | 91.86 | 40.32 |
| 2020 | 172 | 19.07 | 85.48 | 44.23 |
| 2021 | 160 | 17.93 | 88.16 | 47.42 |
| 2022 | 181 | 13.46 | 85.72 | 44.61 |
| 2023 | 193 | 9.20 | 84.80 | 44.94 |
| 2024 | 188 | 14.62 | 87.03 | 47.59 | _(extraido del PDF oficial — sin XLSX)_ |
| 2025 | 195 | 12.12 | 88.36 | 42.52 |

### Cobertura en la muestra del estudio

| anio | paises muestra con Oxford | ACTIVOS | SOLO Y | faltantes |
|---|---|---|---|---|
| 2019 | 86 | 63 | 23 | 0 |
| 2020 | 85 | 63 | 22 | 1 (`TWN`) |
| 2021 | 86 | 63 | 23 | 0 |
| 2022 | 86 | 63 | 23 | 0 |
| 2023 | 86 | 63 | 23 | 0 |
| 2024 | 86 | 63 | 23 | 0 | _(pilares disponibles; dimensiones NaN)_ |
| 2025 | 86 | 63 | 23 | 0 |

## Controles De Calidad Aplicados

### Controles estructurales

| control | resultado |
|---|---|
| filas wide/globales | 1283 |
| filas long | 21048 |
| filas snapshot 2025 | 195 |
| filas study | 601 |
| filas pillars_long | 3852 |
| filas dimensions_long | 9777 |
| ISO3 no nulos en raw | 1283/1283 |
| ISO3 unicos globales | 195 |
| duplicados `year + iso3` | 0 |
| anios integrados | 7 (2019-2025 continuo) |

### Controles de valores 2025

Valores contrastados contra el dashboard publico y el reporte oficial:

| iso3 | pais | esperado 2025 | obtenido | resultado |
|---|---|---|---|---|
| USA | United States | 88.36 | 88.36 | ok |
| CAN | Canada | 74.66 | 74.66 | ok |
| FRA | France | 80.81 | 80.81 | ok |
| GBR | United Kingdom | 77.75 | 77.75 | ok |
| SAU | Saudi Arabia | 71.57 | 71.57 | ok |

### Top 15 latest year (2025)

| rank | iso3 | pais | ai_readiness_score |
|---|---|---|---|
| 1 | USA | United States | 88.36 |
| 2 | FRA | France | 80.81 |
| 3 | GBR | United Kingdom | 77.75 |
| 4 | NLD | Netherlands | 77.18 |
| 5 | KOR | Korea, Republic of | 76.89 |
| 6 | DEU | Germany | 76.78 |
| 7 | SGP | Singapore | 76.42 |
| 8 | CHN | China | 76.27 |
| 9 | AUS | Australia | 75.73 |
| 10 | NOR | Norway | 74.84 |
| 11 | DNK | Denmark | 74.75 |
| 12 | CAN | Canada | 74.66 |
| 13 | ESP | Spain | 74.22 |
| 14 | JPN | Japan | 72.24 |
| 15 | SAU | Saudi Arabia | 71.57 |

## Limitaciones Y Notas Metodologicas

### Gap 2024 — Analisis exhaustivo y resolucion por extraccion PDF

> **Estado actualizado (2026-04-08):** El gap fue **RESUELTO**. El PDF oficial contiene tablas estructuradas en las paginas 43-50. Se extrajeron 188 paises con `pdfplumber`. Cobertura de la muestra: **86/86**. Los datos estan integrados en el panel con `source_tier=official_pdf_extracted`. Ver PLAN_RECUPERACION_OXFORD_2024.md para el proceso completo.

**Conclusion original:** La edicion 2024 del Government AI Readiness Index no tiene dataset estructurado publico (XLSX/CSV). El gap de datos tabulares es oficial y verificado. Sin embargo, el PDF contiene tablas parseables que permiten recuperar `ai_readiness_score` y los 3 pilares. Los datos de 9 dimensiones NO estan presentes en el PDF.

#### Que publico Oxford Insights para 2024

Oxford Insights publico el reporte PDF narrativo de 2024 con normalidad:

| activo | URL oficial | estado |
|---|---|---|
| Reporte PDF 2024 | `https://oxfordinsights.com/wp-content/uploads/2024/12/2024-Government-AI-Readiness-Index-1.pdf` | descargado → `reports/2024_government_ai_readiness_index.pdf` |

El PDF contiene rankings narrativos, analisis de paises y discusion metodologica. Las **paginas 43-50 contienen tablas estructuradas** con columnas `Country | Total | Government | Technology Sector | Data and Infrastructure`, que permiten extraer datos con `pdfplumber`. La extraccion se ejecuto exitosamente el 2026-04-08 obteniendo 188 paises con 0 errores de mapeo.

#### Que NO publico Oxford Insights para 2024

No existe ningun adjunto XLSX, CSV, ni ningun otro formato tabular de datos para la edicion 2024. Esto se confirmo con tres metodos independientes ejecutados el 2026-04-08:

**Metodo 1 — WordPress Media API (busqueda directa por año)**

```
GET https://oxfordinsights.com/wp-json/wp/v2/media
    ?search=2024%20Government%20AI%20Readiness%20Index%20data
    &per_page=50
```

Resultado: la API devolvio 0 adjuntos con la palabra `2024` y tipo de archivo tabular. La huella de la busqueda esta archivada en `metadata/wp_media_search_government_ai_readiness.json` y `metadata/wp_media_search_public_data.json`.

**Metodo 2 — WordPress Media API (busqueda amplia «public data»)**

```
GET https://oxfordinsights.com/wp-json/wp/v2/media
    ?search=public%20data
    &per_page=100
```

Resultado: devolvio datasets para 2019, 2020, 2021, 2022, 2023 y 2025. Ningun adjunto de datos para 2024 aparecio en los resultados de ninguna de las dos busquedas.

**Metodo 3 — Prueba de URLs canonicas por convencion de nombre**

Se probaron URLs construidas siguiendo el patron de nomenclatura de otros anios:

| URL candidata | HTTP response |
|---|---|
| `.../uploads/2024/12/2024-Government-AI-Readiness-Index-data.xlsx` | 404 |
| `.../uploads/2024/12/2024-AI-Readiness-Index-public-dataset.xlsx` | 404 |
| `.../uploads/2025/01/2024-Government-AI-Readiness-Index-data.xlsx` | 404 |
| `.../uploads/2024/01/2024-Government-AI-Readiness-Index-data.xlsx` | 404 |

Ninguna URL candidata resolvio con exito.

#### Contexto de por que ocurrio este gap

El gap 2024 se enmarca en el periodo de transicion metodologica de Oxford Insights:

- Ediciones 2020-2023 usaban el regimen `v2` (3 pilares, 9 dimensiones, escala 0-100).
- La edicion 2025 introdujo el regimen `v3` (6 pilares, 14 dimensiones, rediseno sustancial).
- La edicion 2024 fue la ultima bajo el regimen anterior y coincide con el periodo en que Oxford estaba rediseñando el indice. Es posible que Oxford optara por no publicar datos estructurados para 2024 precisamente porque el marco metodologico estaba en transicion y los datos no serian comparables con el nuevo esquema.
- No hay declaracion publica explicita de Oxford sobre por que 2024 no tiene datos estructurados, pero el patron editorial es consistente con un año de transicion sin publicacion de datos.

#### Implicaciones para el estudio

- El panel de datos Oxford integra **7 ediciones: 2019, 2020, 2021, 2022, 2023, 2024 y 2025** — serie temporal continua.
- Para 2024, `dimension_*` son `NaN` (solo pilares+score disponibles). Los modelos deben manejar `NaN` en columnas de dimension para ese año.
- La comparabilidad 2024 con 2020-2023 es `moderate_comparability_2020_2023` (misma metodologia `v2`, mismo regimen de 3 pilares).
- El salto metodologico relevante es **2023→2025** (`v2` a `v3`), no 2023→2024.
- `source_tier=official_pdf_extracted` permite filtrar 2024 si se requiere solo datos de fuente primaria estructurada.

#### Evidencia archivada

| archivo | contenido |
|---|---|
| `data/raw/Oxford Insights/reports/2024_government_ai_readiness_index.pdf` | Reporte PDF oficial 2024 descargado |
| `data/raw/Oxford Insights/metadata/wp_media_search_government_ai_readiness.json` | Respuesta completa de la API WordPress — confirma ausencia de datos 2024 |
| `data/raw/Oxford Insights/metadata/wp_media_search_public_data.json` | Segunda busqueda API — confirma ausencia de datos 2024 |
| `data/raw/Oxford Insights/download_manifest.csv` | Entrada `year=2024, asset_kind=data_pdf_extracted, status=extracted_from_pdf` |
| `data/raw/Oxford Insights/oxford_ai_readiness_all_raw.csv` | Incluye 188 filas de 2024 con `source_tier=official_pdf_extracted` |
| `info_data/PLAN_RECUPERACION_OXFORD_2024.md` | Plan completo de recuperacion — todos los hitos cumplidos |

---

1. **Gap 2024 (resumen):** la edicion 2024 fue publicada solo como PDF narrativo. Oxford Insights no publico dataset XLSX/CSV para ese año. Investigacion exhaustiva ejecutada el 2026-04-08 via WordPress Media API y prueba de URLs candidatas confirmo la ausencia. Ver seccion completa arriba.
2. 2019 no es estrictamente comparable con 2020+ porque cambia la escala y la arquitectura del indice.
3. 2025 tampoco es estrictamente comparable con 2020-2023 por el cambio a 6 pilares y 14 dimensiones.
4. El panel conserva las distintas generaciones metodologicas en una sola tabla, pero siempre con banderas explicitas para evitar comparaciones ingenuas.
5. `oxford_ai_readiness_pillars_long.csv` y `oxford_ai_readiness_dimensions_long.csv` no incluyen 2019 porque esa edicion no publica la misma estructura de pilares/dimensiones moderna.

## Archivos Relevantes Del Repositorio

| ruta | funcion |
|---|---|
| `notebooks/01_recoleccion.ipynb` | descarga, parsing, armonizacion y verificacion Oxford |
| `data/raw/Oxford Insights/download_manifest.csv` | inventario auditable de activos |
| `data/raw/Oxford Insights/datasets/` | XLSX oficiales descargados |
| `data/raw/Oxford Insights/reports/` | PDFs oficiales |
| `data/raw/Oxford Insights/metadata/` | huellas HTML/JSON del discovery oficial |
