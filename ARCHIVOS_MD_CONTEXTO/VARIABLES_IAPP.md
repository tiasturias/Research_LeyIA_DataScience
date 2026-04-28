# Variables IAPP — Global AI Law and Policy Tracker

## Proposito

Este documento resume las variables X1 de regulacion IA extraidas y codificadas a partir del **IAPP Global AI Law and Policy Tracker** (Feb 2026). IAPP complementa y valida las variables X1 previamente construidas desde la EC-OECD AI Policy Database, cerrando la brecha de cobertura de 68/86 a **86/86 paises del estudio**.

Su objetivo es servir como referencia rapida para:
- conocer la fuente primaria (IAPP tracker PDF) y su alcance;
- documentar la rubrica de codificacion manual aplicada;
- detallar la reconciliacion OECD vs IAPP y las reglas de consolidacion;
- servir como trazabilidad para auditoria academica.

## Fuente

| atributo | valor |
|---|---|
| Nombre | IAPP Global AI Law and Policy Tracker |
| Organizacion | International Association of Privacy Professionals (IAPP) |
| URL tracker | `https://iapp.org/resources/article/global-ai-legislation-tracker/` |
| URL PDF | `https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt34a8e3844fb44942/global_ai_law_policy_tracker.pdf` |
| Fecha datos | Febrero 2026 |
| Formato | PDF (41 paginas), tablas con 5 columnas |
| Jurisdicciones directas | 29 (28 paises + EU como bloque) |
| Metodo extraccion | pdfplumber (Python), con decodificacion de texto espejo |

## Conclusion Ejecutiva

IAPP aporta **6 variables X1 core** de regulacion IA para los 86 paises del estudio:
- **29 jurisdicciones** codificadas directamente desde el PDF (28 paises + EU → 27 miembros en estudio = 54 paises)
- **32 paises adicionales** codificados con evidencia de fuentes complementarias (UNESCO, OECD AI Observatory, Stanford HAI, fuentes oficiales)
- **Reconciliacion con OECD**: 14 AGREE, 22 PARTIAL_AGREE, 32 DIVERGE, 18 IAPP_FILL_GAP
- **Resultado**: X1 consolidado con 86/86 paises cubiertos (100%)

**Hallazgo critico**: 32 divergencias OECD↔IAPP se explican principalmente por:
1. EU AI Act (Regulation 2024/1689, vigente desde Ago 2024) — no capturado en OECD data corte 2024
2. KOR AI Basic Act (Ene 2025), JPN AI Promotion Act (May 2025) — posteriores a OECD
3. Definicion mas estricta de "ley AI vinculante" en IAPP vs OECD

## Archivos Generados

| archivo | contenido | filas | columnas |
|---|---|---|---|
| `data/raw/IAPP/iapp_tracker_structured_raw.csv` | Tabla raw estructurada del tracker con 29 jurisdicciones directas, 4 campos de texto y trazabilidad por paginas | 29 | 11 |
| `data/raw/IAPP/iapp_all_coded.csv` | Todas las jurisdicciones codificadas (incl. HKG) | 87 | 11 |
| `data/raw/IAPP/iapp_x1_core.csv` | Solo 86 paises del estudio, codificacion directa IAPP | 86 | 11 |
| `data/raw/iapp_regulatory.csv` | Archivo plano X1 (formato flat, solicitado por metodologia) | 86 | 9 |
| `data/raw/IAPP/download_manifest.csv` | Inventario de activos IAPP descargados | 3 | 10 |
| `data/raw/iapp_tracker_raw_extracted.json` | Extraccion raw del PDF (29 jurisdicciones, texto completo) | 29 | 5 columnas texto |
| `src/iapp_coding.py` | Modulo Python con rubrica y codificacion | - | - |

> **NOTA ETL**: Los archivos de reconciliacion OECD vs IAPP (`iapp_oecd_reconciliation.csv`, `iapp_x1_consolidated.csv`, `iapp_x1_snapshot_2026.csv`) son artefactos **Transform**, NO Extract. Pertenecen a `data/interim/` y se generaran en `02_limpieza.ipynb`. No deben existir en `data/raw/`.

## Estructura del PDF

El PDF IAPP contiene una tabla por jurisdiccion con 5 columnas:

| columna | contenido |
|---|---|
| Country | Nombre del pais (texto espejo/invertido en PDF) |
| Specific AI governance law/policy | Leyes y politicas AI-especificas vigentes |
| Relevant authorities | Autoridades regulatorias competentes |
| Other relevant laws/policies | Leyes conexas (proteccion de datos, derechos digitales, etc.) |
| Wider AI context | Contexto amplio (estrategias, planes nacionales, iniciativas) |

**Nota tecnica**: Los nombres de paises en el PDF estan codificados en texto espejo (e.g., "ANITNEGRA" → "Argentina"). Se utilizo un diccionario de decodificacion (COUNTRY_DECODE) para resolver los 29 nombres.

Ademas del JSON raw, la extraccion conserva una version tabular reusable en `data/raw/IAPP/iapp_tracker_structured_raw.csv` con:
- `jurisdiction_iapp`
- `policy_text`
- `authorities_text`
- `other_laws_text`
- `context_text`
- `pages`, `page_count`, `page_start`, `page_end`
- `source`, `source_date`

## Rubrica de Codificacion X1

### Variables Core (6)

| variable | tipo | definicion | valores | criterio |
|---|---|---|---|---|
| has_ai_law | binaria (0/1) | Existe ≥1 ley vinculante AI-especifica EN VIGOR | 0, 1 | Solo leyes promulgadas y vigentes; no proyectos de ley ni propuestas |
| regulatory_approach | categorica ordinal | Enfoque regulatorio predominante del pais | none, light_touch, strategy_led, regulation_focused, comprehensive | Basado en combinacion de estrategia + ley vinculante + enforcement |
| regulatory_intensity | numerica (0-10) | Score compuesto de profundidad regulatoria | 0-10 | Pondera: existencia ley, enforcement, alcance, autoridad, sanciones |
| year_enacted | numerica | Año de primera regulacion IA vinculante vigente | 2017-2025 o NaN | NaN si no hay ley vinculante |
| enforcement_level | ordinal | Nivel de enforcement efectivo | none, low, medium, high | Basado en: autoridad designada, mecanismos sancion, historial enforcement |
| thematic_coverage | numerica (0-15) | Conteo de temas cubiertos por politicas IA | 0-15 | 15 temas: transparency, fairness, privacy, safety, liability, discrimination, IP, sector_specific, data_governance, explainability, human_oversight, sandboxes, public_sector, international_cooperation, employment_impact |

### Escala regulatory_approach

| valor | definicion | n_paises |
|---|---|---|
| none | Sin iniciativas de politica IA identificadas | 5 |
| light_touch | Directrices no vinculantes, principios eticos, marcos voluntarios | 10 |
| strategy_led | Estrategia nacional de IA publicada, pero sin legislacion AI-especifica vinculante | 39 |
| regulation_focused | Regulacion AI-especifica vinculante sin estrategia nacional integral | 0 |
| comprehensive | Ley AI-especifica vinculante + estrategia nacional + enforcement activo | 32 |

### Escala enforcement_level

| valor | definicion |
|---|---|
| none | Sin mecanismo de enforcement identificado |
| low | Autoridad designada pero mecanismos limitados |
| medium | Autoridad con mandato claro, sanciones posibles |
| high | Autoridad activa con historial de enforcement, sanciones significativas |

## Reconciliacion OECD vs IAPP

### Politica de Consolidacion

- **Fuente primaria**: OECD (datos estructurados, API, panel temporal 2013-2024)
- **Fuente validacion/complemento**: IAPP (mas reciente Feb 2026, codificacion rigurosa)
- **Regla AGREE/PARTIAL_AGREE**: Se toma max(OECD, IAPP) para intensidad/cobertura; IAPP para approach si difiere
- **Regla DIVERGE**: Se usa IAPP override (mas reciente), confidence = medium_needs_review
- **Regla FILL_GAP**: Se usa IAPP (unica fuente disponible), confidence variable

### Distribucion Reconciliacion

| status | n_paises | descripcion |
|---|---|---|
| AGREE | 14 | OECD e IAPP coinciden en has_ai_law y regulatory_approach |
| PARTIAL_AGREE | 22 | Coinciden en has_ai_law pero difieren en approach |
| DIVERGE | 32 | Difieren en has_ai_law (principal diferencia) |
| IAPP_FILL_GAP | 18 | Sin datos OECD; IAPP provee cobertura unica |

### Principales Divergencias

Las 32 divergencias se explican por:
1. **EU AI Act (27 paises)**: Regulation 2024/1689 entro en vigor Ago 2024. OECD data (corte 2024) no captura este cambio; IAPP (Feb 2026) si.
2. **KOR**: AI Basic Act aprobado Ene 2025 (posterior a OECD).
3. **JPN**: AI Promotion Act aprobado May 2025 (posterior a OECD).
4. **Definicion**: IAPP aplica definicion mas estricta de "ley AI vinculante", reclasificando paises con regulacion indirecta (AUS, GBR, BRA, CHL, EGY) de regulation_focused a strategy_led.

## Cobertura Final Consolidada

| metrica | valor |
|---|---|
| Paises con has_ai_law = 1 | 32 (37%) |
| Paises con has_ai_law = 0 | 54 (63%) |
| Paises comprehensive | 32 |
| Paises strategy_led | 39 |
| Paises light_touch | 10 |
| Paises none | 5 |
| mean(regulatory_intensity) | 5.3 |
| mean(thematic_coverage) | 8.3 |
| Confidence high | 36 |
| Confidence medium_needs_review | 32 |
| Confidence medium | 3 |
| Confidence low | 15 |

## Paises con Ley AI Vinculante (32)

| iso3 | jurisdiccion | year_enacted | approach | enforcement |
|---|---|---|---|---|
| RUS | Russia | 2020 | comprehensive | high |
| CHN | China | 2021 | comprehensive | high |
| PER | Peru | 2023 | comprehensive | medium |
| AUT-SWE | 27 EU Member States | 2024 | comprehensive | high |
| JPN | Japan | 2025 | comprehensive | high |
| KOR | South Korea | 2025 | comprehensive | high |

## 18 Paises IAPP Fill-Gap (sin datos OECD)

| iso3 | pais | has_ai_law | approach | confidence |
|---|---|---|---|---|
| BGD | Bangladesh | 0 | strategy_led | low |
| BHR | Bahrain | 0 | strategy_led | low |
| BLR | Belarus | 0 | light_touch | low |
| BLZ | Belize | 0 | none | low |
| BRB | Barbados | 0 | none | low |
| CHN | China | 1 | comprehensive | medium |
| CMR | Cameroon | 0 | none | low |
| GHA | Ghana | 0 | strategy_led | low |
| JOR | Jordan | 0 | strategy_led | low |
| LBN | Lebanon | 0 | none | low |
| LKA | Sri Lanka | 0 | light_touch | low |
| MNG | Mongolia | 0 | light_touch | low |
| PAK | Pakistan | 0 | strategy_led | low |
| PAN | Panama | 0 | strategy_led | low |
| PHL | Philippines | 0 | strategy_led | low |
| RUS | Russia | 1 | comprehensive | medium |
| SYC | Seychelles | 0 | none | low |
| TWN | Taiwan | 0 | strategy_led | low |

## Limitaciones

1. **Datos PDF**: La extraccion depende de la estructura del PDF; cambios de formato futuro requeririan actualizacion del parser.
2. **Texto espejo**: Los nombres de paises estan codificados en texto invertido — se resolvio con diccionario manual pero podria fallar con nuevas jurisdicciones.
3. **Codificacion manual**: Los 32 paises adicionales (no cubiertos por IAPP) se codificaron con evidencia publica — confidence = low para la mayoria.
4. **Definicion divergente**: IAPP y OECD usan definiciones diferentes de "regulacion AI vinculante", generando 32 divergencias. Se documento la justificacion de cada override.
5. **Corte temporal**: IAPP Feb 2026 es snapshot; la regulacion AI evoluciona rapidamente.
6. **EU AI Act**: Se propago a 27 miembros EU en el estudio, pero la implementacion nacional varia — aplicacion completa prevista para Ago 2026.

## Notebook de Referencia

Seccion 8 de `notebooks/01_recoleccion.ipynb`:
- Cell 8.1: Setup, rutas, discovery de activos
- Cell 8.2: Extraccion PDF con pdfplumber
- Cell 8.3: Codificacion X1 (importa `src/iapp_coding.py`) → produce `iapp_study_df` (fuente IAPP pura)
- Cell 8.4: Nota ETL — reconciliacion OECD vs IAPP **diferida** a `02_limpieza.ipynb` (no es Extract)
- Cell 8.5: Guardado de archivos raw IAPP puros + QA sobre `iapp_study_df`

> **Principio ETL**: `01_recoleccion.ipynb` = Extract puro. Cada fuente se guarda en `data/raw/` de forma independiente. La consolidacion OECD+IAPP se realizara en `02_limpieza.ipynb` → `data/interim/`.

Modulo: `src/iapp_coding.py` — contiene IAPP_CODING (29 jurisdicciones), build_iapp_x1(), build_additional_countries(), study_iso3.
