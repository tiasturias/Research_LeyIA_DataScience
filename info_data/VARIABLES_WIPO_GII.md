# Variables WIPO GII (Global Innovation Index)

## Proposito

Este documento deja trazabilidad operativa y audit-ready de la integracion inicial de WIPO Global Innovation Index (GII) al estudio.

Su objetivo es documentar:
- que parte de la fuente oficial WIPO ya fue explotada con exito;
- que variables utiles aporta al estudio como controles X2;
- que outputs fueron generados;
- cual es la cobertura real en la muestra del estudio.

## Resumen Ejecutivo

WIPO GII entra al estudio como fuente **X2** para `gii_score` y como fuente ampliada de indicadores de innovacion comparables a nivel pais.

La integracion cubre **6 ediciones (2020–2025)** con los siguientes resultados:

**2024–2025 (XLSX oficial):**
- `gii_score` y `gii_rank` recuperados para 133 economias (2024) y 139 (2025);
- 118 indicadores unicos preservados en la union 2024-2025;
- cobertura de la muestra: **83/86** paises en 2024 y **84/86** en 2025;
- outputs raw, study, long, wide y snapshot generados en `data/raw/WIPO Global Innovation Index/`.

**2020–2023 (PDF oficial, extraccion pdfplumber):**
- PDFs descargados manualmente y procesados mediante `pdfplumber`;
- `gii_score` y `gii_rank` extraidos; 131–132 economias por anio;
- cobertura de la muestra: **81–82/86** paises en 2020–2023;
- panel historico completo guardado en `wipo_gii_overall_panel.csv` (799 filas, 2020–2025);
- validacion top-3 OK para todos los anos.

## Fuente Y Proveniencia

| campo | detalle |
|---|---|
| emisor | World Intellectual Property Organization (WIPO) |
| producto | Global Innovation Index (GII) |
| fuente principal | `https://www.wipo.int/en/web/global-innovation-index` |
| carpeta local | `data/raw/WIPO Global Innovation Index/` |
| notebook de implementacion | `notebooks/01_recoleccion.ipynb` |
| rol metodologico | X2 high (`gii_score`) |
| granularidad | pais-anio |
| periodos operativos integrados | 2020, 2021, 2022, 2023, 2024, 2025 |
| fecha de extraccion inicial | 2026-04-08 |
| manifiesto | `data/raw/WIPO Global Innovation Index/download_manifest.csv` |

## Activos Inventariados

| anio | activo | estado | observacion |
|---|---|---|---|
| 2025 | `wipo-pub-2000-2025-tech1.xlsx` | valido | dataset estructurado oficial con 139 economias |
| 2025 | `global-innovation-index-2025-en.pdf` | invalido/bloqueado | la URL oficial respondio, pero el archivo descargado por terminal fue HTML y no PDF binario |
| 2024 | `wipo-pub-2000-2024-tech1.xlsx` | valido | dataset estructurado oficial con 133 economias |
| 2024 | `wipo-pub-2000-2024-en-global-innovation-index-2024.pdf` | valido | reporte PDF oficial archivado localmente |
| 2023 | `wipo-pub-2000-2023-...-16th-edition.pdf` | valido | descargado manualmente; 132 economias extraidas con pdfplumber |
| 2022 | `wipo-pub-2000-2022-...-15th-edition.pdf` | valido | descargado manualmente; 132 economias extraidas con pdfplumber |
| 2021 | `wipo_pub_gii_2021.pdf` | valido | descargado manualmente; 132 economias extraidas con pdfplumber |
| 2020 | `wipo_pub_gii_2020.pdf` | valido | descargado manualmente; 131 economias extraidas con pdfplumber |
| 2019 | `wipo_pub_gii_2019_keyfindings.pdf` | valido parcial | solo Key Findings (20 paginas); sin tabla completa de ranking — excluido del ETL |

## Alcance De Extraccion Actual

### Datasets estructurados efectivamente integrados

Los XLSX oficiales 2024 y 2025 contienen 4 hojas:
- `Index Structure`
- `Economies`
- `Data`
- `Metadata`

La hoja `Data` fue usada como base del ETL. Cada fila representa una economia x indicador con:
- nombre del indicador;
- score;
- rank;
- flags de screening;
- year original del dato cuando aplica.

La hoja `Economies` se uso para enriquecer con:
- `ISO3`
- `ECONOMY_NAME`
- `INCOME`
- `REG_UN`
- `REG_UN_CODE`
- `POP`
- `PPPGDP`
- `PPPPC`

La hoja `Index Structure` se uso para preservar metadata de indicador:
- `NUM`
- `NAME`
- `LEVEL`
- `TYPE`
- `PROFILE`
- `DESCRIPTION`
- `SOURCE`
- `WEBSITE`

### Variables operativas extraidas

| variable | rol | estado | detalle |
|---|---|---|---|
| `gii_score` | X2 high | extraida | row `Global Innovation Index` del sheet `Data` |
| `gii_rank` | X2 complementaria | extraida | ranking oficial por economia |
| subindices/pilares GII | X2 extra | extraidos | preservados en raw/long/wide |
| metadata de economia | metadata | extraida | ingreso, region UN, poblacion, PPP GDP, PPP per capita |
| metadata de indicador | metadata | extraida | nivel, tipo, descripcion, fuente WIPO y website |

## Diccionario Operativo Resumido

| campo final | origen | descripcion |
|---|---|---|
| `iso3` | sheet `Economies` | ISO3 oficial provisto por WIPO |
| `country_name_std` | sheet `Economies` | nombre de economia normalizado desde WIPO |
| `year` | nombre del archivo | edicion GII integrada |
| `indicator` | derivado | slug en snake_case del nombre del indicador |
| `indicator_code` | sheet `Data` / `Index Structure` | codigo del indicador |
| `indicator_name_wipo` | sheet `Data` | nombre original del indicador |
| `value` | sheet `Data` (`SCORE`) | score del indicador |
| `rank_reported` | sheet `Data` (`RANK`) | rank reportado |
| `gii_score` | derivado | score overall del GII |
| `gii_rank` | derivado | rank overall del GII |
| `income_group_wipo` | sheet `Economies` | grupo de ingreso |
| `region_un` | sheet `Economies` | region ONU |
| `source_tier` | derivado | `official_primary` para XLSX validos |
| `methodology_regime` | derivado | etiqueta por edicion: `gii_YYYY_official_release_109_indicators` |
| `comparability_group` | derivado | `review_pending_cross_year` |

## Archivos Generados

| archivo | descripcion | filas | columnas |
|---|---|---|---|
| `wipo_gii_all_raw.csv` | union raw 2024-2025 con todos los indicadores y metadata | 29648 | 40 |
| `wipo_gii_study.csv` | subconjunto de la muestra del estudio | 18203 | 40 |
| `wipo_gii_long.csv` | capa long operativa | 29648 | 40 |
| `wipo_gii_wide.csv` | capa wide por `iso3 x year` con indicadores pivotados | 267 | 128 |
| `wipo_gii_snapshot_latest.csv` | snapshot overall latest year (2025) | 139 | 40 |
| `wipo_gii_overall_panel.csv` | **panel historico GII score+rank 2020-2025** | 799 | 40 |
| `download_manifest.csv` | manifiesto de activos y estado de descarga | 11 | 12 |

## Cobertura Final

### Cobertura global (`gii_score`)

| anio | economias | fuente | notas |
|---|---|---|---|
| 2020 | 131 | PDF (pdfplumber) | extraccion completa |
| 2021 | 132 | PDF (pdfplumber) | extraccion completa |
| 2022 | 132 | PDF (pdfplumber) | extraccion completa |
| 2023 | 132 | PDF (pdfplumber) | extraccion completa |
| 2024 | 133 | XLSX oficial | dataset estructurado |
| 2025 | 139 | XLSX oficial | dataset estructurado |

### Cobertura en la muestra del estudio (`gii_score`)

| anio | paises muestra | ACTIVOS (63) | faltantes principales |
|---|---|---|---|
| 2020 | 82 | 63 | `BLZ`, `BRB`, `SYC`, `TWN` |
| 2021 | 82 | 63 | `BLZ`, `BRB`, `SYC`, `TWN` |
| 2022 | 81 | 63 | `BLZ`, `BRB`, `LBN`, `SYC`, `TWN` |
| 2023 | 82 | 63 | `BLZ`, `BRB`, `SYC`, `TWN` |
| 2024 | 83 | 63 | `BLZ`, `SYC`, `TWN` |
| 2025 | 84 | 63 | `BLZ`, `TWN` |

Nota: `BLZ` (Belize), `TWN` (Taiwan) y `SYC` (Seychelles) no son cubiertos por WIPO en ningun anio. `BRB` (Barbados) y `LBN` (Libano) tienen cobertura variable por edicion.

## Controles De Calidad Ejecutados

### Controles estructurales

| control | resultado |
|---|---|
| datasets estructurados XLSX validos | 2024, 2025 |
| PDFs extraidos con pdfplumber | 2020, 2021, 2022, 2023 |
| firmas PDF validadas como PDF binario | 2020 ✓, 2021 ✓, 2022 ✓, 2023 ✓, 2024 ✓, 2025 ✓ (IAPP1) |
| duplicados `year + iso3` en panel historico | 0 |
| ISO3 faltantes en XLSX 2024-2025 | 0 |
| indicadores unicos preservados (XLSX) | 118 |
| validacion top-3 por anio | PASS 2020–2025 |

### Validacion de ranking oficial

El top 10 del `gii_score` recuperado coincide con el orden oficial visible en las paginas WIPO:

**2024**
1. CHE
2. SWE
3. USA
4. SGP
5. GBR
6. KOR
7. FIN
8. NLD
9. DEU
10. DNK

**2025**
1. CHE
2. SWE
3. USA
4. KOR
5. SGP
6. GBR
7. FIN
8. NLD
9. DNK
10. CHN

## Limitaciones Y Notas Metodologicas

1. Para 2020-2023 solo se extrajo `gii_score` y `gii_rank` (no los 109 sub-indicadores); estos anos carecen de columnas de metadata enriquecida (income_group, region_un, PPP, etc.).
2. `comparability_group` queda provisionalmente como `review_pending_cross_year` para los datos XLSX (2024-2025) y como `gii_historical_pdf_only` para los datos PDF (2020-2023).
3. `BLZ`, `TWN` y `SYC` son ausencias estructurales permanentes de WIPO; no se recuperaran con mas ediciones.
4. La comparabilidad entre ediciones debe verificarse antes de usar la serie temporal en regresiones ponderadas; el GII introdujo cambios de metodologia en varias ediciones.
5. El PDF 2019 disponible es solo Key Findings (20 paginas); la tabla de 130 economias no esta disponible. Si se requiere cobertura 2019, habria que buscar el PDF completo del informe principal.

## Estado Operativo Recomendado

- `gii_score` puede usarse como X2 para el panel **2020–2025** (6 anos).
- Los subindices y pilares WIPO quedan disponibles como variables auxiliares para los anos 2024-2025.
- El archivo clave para analisis de serie temporal es `wipo_gii_overall_panel.csv`.
- La proxima tarea metodologica es verificar la comparabilidad entre ediciones antes de usar el panel en regresiones longitudinales.
- Si se requiere cobertura 2019, habria que obtener el PDF completo del informe 2019 (no el Key Findings).