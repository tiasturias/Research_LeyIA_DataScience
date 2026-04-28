# Plan MVP — Estudio cuantitativo Top 30 países + Chile focal

**Proyecto:** Research_LeyIA_DataScience — "¿Regular o no regular? Impacto de la regulación de IA en los ecosistemas nacionales"
**Curso:** IMT3860 — Introducción a Data Science (PUC, abril 2026)
**Audiencia primaria:** legisladores chilenos + Comisión de Ciencia del Senado + Ministerio de Ciencia, Tecnología, Conocimiento e Innovación
**Caso focal:** Boletín 16821-19 (Ley Marco de IA chilena, en trámite)
**Fecha plan:** 2026-04-27
**Versión:** 1.0
**Estado:** Aprobado por usuario (2026-04-27)

---

## 0. Índice

1. [Contexto y motivación](#1-contexto-y-motivación)
2. [Objetivo del MVP](#2-objetivo-del-mvp)
3. [Alcance: muestra N=30](#3-alcance-muestra-n30)
4. [Estado de los datos: gap analysis completo](#4-estado-de-los-datos-gap-analysis-completo)
5. [Plan de ejecución por fases](#5-plan-de-ejecución-por-fases)
6. [Arquitectura de archivos](#6-arquitectura-de-archivos)
7. [Decisiones metodológicas](#7-decisiones-metodológicas)
8. [Métodos cuantitativos: correlación + causalidad](#8-métodos-cuantitativos-correlación--causalidad)
9. [Verification end-to-end](#9-verification-end-to-end)
10. [Limitaciones explícitas](#10-limitaciones-explícitas)
11. [Estimación de tiempo](#11-estimación-de-tiempo)
12. [Criterios de éxito y go/no-go para extender a 86 países](#12-criterios-de-éxito-y-gono-go-para-extender-a-86-países)

---

## 1. Contexto y motivación

### 1.1 ¿Por qué un MVP?

El proyecto LeyIA tiene una muestra original de **86 países × ~70 variables**. Procesar el corpus legal-IA de los 86 países requiere ~50 horas de trabajo activo del LLM distribuido en 12-17 sesiones. Antes de invertir ese esfuerzo total, el usuario decidió validar la **viabilidad metodológica** del estudio con una submuestra controlada.

### 1.2 ¿Por qué Top 30 + Chile?

Tres razones convergentes:

1. **Top 30 Microsoft AI Diffusion 2025** es el sample más documentado y trazable disponible. Sus 30 países cubren el grueso del ecosistema mundial de IA y todos están en P1 de prioridad.
2. **29 de los 30 ya tienen corpus legal procesado** (DONE) en `data/raw/legal_corpus/{ISO3}/`. Solo CHL queda PENDING (focal, se procesa al final por diseño).
3. **Chile (CHL)** es el caso focal del estudio para el Boletín 16821-19. Incluirlo en N=30 permite el análisis narrativo central (Synthetic Control Method).

### 1.3 ¿Por qué este plan ahora?

El usuario expresó dos requerimientos explícitos en 2026-04-27:

> "Quiero comenzar a hacer el EDA, entrenamiento, etc solo con estos top 30, talvez hacer una submuestra para hacer un MVP de este estudio en todas sus fases, EDA, features, label, target, entrenamiento, y todo... luego de que tengamos resultados con el top 30 (y comprobamos que este estudio es viable) seguimos extrayendo corpus de los top 30 países."

> "[Quiero] la información más completa posible para lograr tener un estudio completo de esta submuestra de 30 países, que se convierta en un proyecto capaz de lograr encontrar la correlación y causalidad de [lo] que busca entre X1, X2 e Y."

Este plan responde a ambos requerimientos.

---

## 2. Objetivo del MVP

### 2.1 Objetivo central

Entregar **evidencia empírica preliminar** de la relación entre régimen regulatorio IA (X1) y ecosistema/desempeño IA (Y), controlando por instituciones y economía (X2), con máxima riqueza de variables disponibles para la submuestra N=30.

### 2.2 Sub-objetivos

| # | Sub-objetivo | Output verificable |
|---|---|---|
| 1 | Maximizar completitud de variables Y, X1, X2 para los 30 países | `top30_master.csv` con ≤2% missing |
| 2 | Integrar mejores recodificaciones X1 de la skill `corpus-legal-ia` | `x1_master_v2.csv` con `*_proposed` paralelo a IAPP |
| 3 | Extraer variables nuevas mencionadas en AI Index 2026 (Stanford) | 5+ variables nuevas integradas |
| 4 | Realizar EDA descriptivo riguroso del subset 30 | notebook `03a_eda_top30_mvp.ipynb` con 15+ figuras |
| 5 | Construir features y targets reproducibles | matrices `X_top30.csv`, `Y_top30.csv` |
| 6 | Estimar correlación Y ~ X1 condicional a X2 | tabla coeficientes con CIs bootstrap |
| 7 | Estimar efectos causales con limitaciones explícitas (SCM CHL, matching, IV) | reportes específicos por método |
| 8 | Documentar limitaciones y criterios de robustez | sección dedicada en `MVP_TOP30_RESULTS.md` |
| 9 | Decidir go/no-go para extender a 86 países | recomendación final con criterios |

### 2.3 Lo que NO es objetivo del MVP

- **NO** es objetivo replicar resultados con 86 países (eso es la fase post-MVP).
- **NO** es objetivo procesar el corpus legal de CHL (se procesa después del MVP).
- **NO** es objetivo entrenar modelos ML pesados (RF, XGBoost, NN) — N=30 hace que sobreajusten.
- **NO** es objetivo el análisis NLP del corpus (notebook 05_nlp.ipynb queda fuera del MVP).
- **NO** es objetivo aprobar las 16 recodificaciones X1 pendientes — se difiere hasta post-MVP.

---

## 3. Alcance: muestra N=30

### 3.1 Lista exacta de los 30 países

| # | ISO3 | País | Región | EU AI Act | Régimen propuesto | Aprobado | Status corpus |
|---|---|---|---|---|---|---|---|
| 1 | ARE | United Arab Emirates | MENA | No | soft_framework | Sí | DONE (5 PDFs) |
| 2 | AUS | Australia | Oceania | No | soft_framework | Sí | DONE (7 PDFs) |
| 3 | AUT | Austria | EU | Sí | binding_regulation | Sí | DONE (6 PDFs) |
| 4 | BEL | Belgium | EU | Sí | binding_regulation | Sí | DONE (5 PDFs) |
| 5 | BGR | Bulgaria | EU | Sí | binding_regulation | Pendiente | DONE (5 PDFs) |
| 6 | CAN | Canada | North America | No | soft_framework | Pendiente | DONE (6 PDFs) |
| 7 | CHE | Switzerland | Europe-Other | No | soft_framework | Pendiente | DONE (6 PDFs) |
| 8 | CHL | Chile | LATAM | No | (a determinar) | — | **PENDING** (focal) |
| 9 | CRI | Costa Rica | LATAM | No | soft_framework | Pendiente | DONE (5 PDFs) |
| 10 | CZE | Czechia | EU | Sí | binding_regulation | Sí | DONE (5 PDFs) |
| 11 | DEU | Germany | EU | Sí | binding_regulation | Pendiente | DONE (5 PDFs) |
| 12 | DNK | Denmark | EU | Sí | binding_regulation | Pendiente | DONE (5 PDFs) |
| 13 | ESP | Spain | EU | Sí | binding_regulation | Pendiente | DONE (6 PDFs) |
| 14 | FIN | Finland | EU | Sí | binding_regulation | Pendiente | DONE (8 PDFs) |
| 15 | FRA | France | EU | Sí | binding_regulation | Pendiente | DONE (6 PDFs) |
| 16 | GBR | United Kingdom | Europe-Other | No | soft_framework | Pendiente | DONE (6 PDFs) |
| 17 | HUN | Hungary | EU | Sí | binding_regulation | Sí | DONE (5 PDFs) |
| 18 | IRL | Ireland | EU | Sí | binding_regulation | Pendiente | DONE (6 PDFs) |
| 19 | ISR | Israel | MENA | No | soft_framework | Pendiente | DONE (5 PDFs) |
| 20 | ITA | Italy | EU | Sí | binding_regulation | Sí | DONE (7 PDFs) |
| 21 | JOR | Jordan | MENA | No | soft_framework | Pendiente | DONE (5 PDFs) |
| 22 | KOR | South Korea | East Asia | No | binding_regulation | Sí | DONE (5 PDFs) |
| 23 | NLD | Netherlands | EU | Sí | binding_regulation | Sí | DONE (5 PDFs) |
| 24 | NOR | Norway | Europe-Other | No | soft_framework | Pendiente | DONE (5 PDFs) |
| 25 | NZL | New Zealand | Oceania | No | soft_framework | Sí | DONE (5 PDFs) |
| 26 | POL | Poland | EU | Sí | binding_regulation | Pendiente | DONE (5 PDFs) |
| 27 | SGP | Singapore | Southeast Asia | No | soft_framework | Sí | DONE (7 PDFs) |
| 28 | SWE | Sweden | EU | Sí | binding_regulation | Sí | DONE (5 PDFs) |
| 29 | TWN | Taiwan | East Asia | No | binding_regulation | Sí | DONE (5 PDFs) |
| 30 | USA | United States | North America | No | soft_framework | Pendiente | DONE (6 PDFs) |

### 3.2 Distribución por bucket regulatorio

| Bucket | N | Países |
|---|---|---|
| `binding_regulation` | 14 | AUT, BEL, BGR, CZE, DEU, DNK, ESP, FIN, FRA, HUN, IRL, ITA, KOR, NLD, POL, SWE, TWN |
| `soft_framework` | 14 | ARE, AUS, CAN, CHE, CRI, GBR, ISR, JOR, NOR, NZL, SGP, USA |
| `strategy_only` | 0 | (ninguno en P1-TOP30) |
| `no_framework` | 0 | (ninguno en P1-TOP30) |
| `(a determinar)` | 1 | CHL (focal) |

> Conteo final: 14 binding + 14 soft + 1 + 1 mismo bucket per CHL = N=30. Después de procesar CHL, su régimen entrará en una de las categorías existentes (preliminarmente `strategy_only` con intensity 4-5).

### 3.3 Distribución por región

| Región | N | Países |
|---|---|---|
| EU | 14 | AUT, BEL, BGR, CZE, DEU, DNK, ESP, FIN, FRA, HUN, IRL, ITA, NLD, POL, SWE |
| Europe-Other | 3 | CHE, GBR, NOR |
| North America | 2 | CAN, USA |
| Oceania | 2 | AUS, NZL |
| East Asia | 2 | KOR, TWN |
| Southeast Asia | 1 | SGP |
| MENA | 3 | ARE, ISR, JOR |
| LATAM | 2 | CRI, CHL |

### 3.4 Distribución por EU AI Act

- **Sí, EU member (aplica directamente):** 15 (AUT, BEL, BGR, CZE, DEU, DNK, ESP, FIN, FRA, HUN, IRL, ITA, NLD, POL, SWE)
- **No (no EU member):** 15 (ARE, AUS, CAN, CHE, CHL, CRI, GBR, ISR, JOR, KOR, NOR, NZL, SGP, TWN, USA)

> **Balance perfecto 15/15** entre tratamiento (EU AI Act aplicable) y control (no EU AI Act). Esto permite usar `eu_status` como **instrumento natural** y/o variable de comparación principal.

---

## 4. Estado de los datos: gap analysis completo

### 4.1 GAP A — Missing en variables existentes (acción P0)

Variables que YA están en `data/interim/sample_ready_cross_section.csv` pero tienen valores faltantes para algunos países del subset 30.

| Variable | N missing / 30 | ISO3 afectados | Fuente sugerida para imputación |
|---|---|---|---|
| `ai_patents_per100k` | 3 | ARE, CRI, TWN | OECD AI Patent Database 2025 (https://stats.oecd.org) o Stanford AI Index 2026 Cap. 1 (versión actualizada vs 2025) |
| `ai_publications_frac` | 2 | JOR, TWN | UNESCO Science Report 2024 / Scopus AI subset (Elsevier) / OpenAlex AI tag |
| `ai_investment_vc_proxy` | 7 | ARE, CRI, JOR, KOR, NZL, SGP, TWN | Crunchbase Pro / Stanford AI Index 2026 Cap. 4 / OECD AI Going Digital 2025 / CB Insights State of AI |
| `tertiary_education` | 2 (parciales) | TWN, BGR | Eurostat (BGR) / ROC Ministry of Education (TWN) |
| `rd_expenditure` | 3 | TWN, ARE, JOR | UNESCO UIS / ROC NSC / OECD MSTI |
| `ict_service_exports_pct` | 2 | TWN, JOR | UN Trade Statistics / WTO ITSS |
| `high_tech_exports_pct` | 2 | TWN, JOR | UN Trade Statistics / OECD STAN |
| `gii_score` | 1 | TWN | WIPO (no publica TWN) → marcar como NA estructural o usar proxy alternative |
| `regulatory_quality`, `rule_of_law`, `government_effectiveness`, `control_of_corruption` | 1 cada | TWN | World Bank no publica TWN → NA estructural o proxy desde V-Dem / EIU |

**Total estimado**: ~25 imputaciones individuales. Para TWN, se documentan como NA estructural (Banco Mundial no publica datos de Taiwán por cuestiones políticas).

### 4.2 GAP B — Variables X1 propuestas por la skill (acción P1)

Las 29 P1-TOP30 procesadas tienen `CANDIDATES.md` con propuestas de recodificación que NO están propagadas a `x1_master.csv`. Para el MVP construimos `x1_master_v2.csv` paralelo.

| Variable nueva en v2 | Origen | Tipo | Cobertura potencial |
|---|---|---|---|
| `regulatory_intensity_proposed` | CANDIDATES.md §5/§6 | int 0-10 | 29/29 P1-TOP30 |
| `thematic_coverage_proposed` | CANDIDATES.md §5/§6 | int 0-15 | 29/29 |
| `regulatory_regime_group_proposed` | CANDIDATES.md §6 | categórico 4-niveles | 29/29 |
| `enforcement_level_proposed` | CANDIDATES.md §5 | "none\|low\|medium\|high" | 29/29 |
| `has_dedicated_ai_authority` | CANDIDATES.md §4 (autoridades) | bool 0/1 | 29/29 |
| `enforcement_governance_model` | CANDIDATES.md §4 | "centralized\|delegated\|coordinator-only\|hybrid" | 29/29 |
| `eu_ai_act_implementation_date` | CANDIDATES.md §3 (EU members) | date | 14/29 (UE/EEA) |
| `ai_law_pathway_declared` | FINDINGS.md (banderas) | bool 0/1 | 29/29 |
| `ai_law_pathway_target_date` | FINDINGS.md | date | subset of 29 |
| `confidence_iapp_to_skill` | CANDIDATES.md §6 | "low\|medium\|medium-high\|high" | 29/29 |
| `regime_change_iapp_vs_skill` | CANDIDATES.md §7 | "confirmed\|upgrade\|downgrade\|reclassified" | 29/29 |
| `ai_corpus_n_documents` | manifest.csv count | int | 29/29 |
| `ai_corpus_total_pages` | sum(manifest.pages) | int | 29/29 |
| `ai_corpus_first_doc_year` | min(manifest.publication_date) | int | 29/29 |
| `ai_corpus_last_doc_year` | max(manifest.publication_date) | int | 29/29 |
| `ai_corpus_years_span` | max-min | float | 29/29 |

### 4.3 GAP C — Variables nuevas del AI Index 2026 (acción P2)

Mencionadas explícitamente en `docs/ai_index_report_2026.pdf` (423 pp). Útiles como features adicionales o proxy de Y.

| Variable | Fuente primaria | Tabla/Figura AI Index 2026 | Disponibilidad |
|---|---|---|---|
| `microsoft_diffusion_capital_score` | Microsoft AI Diffusion 2025 | (subscore composite) | Reporte original Microsoft |
| `microsoft_diffusion_skills_score` | Microsoft AI Diffusion 2025 | (subscore) | Ídem |
| `microsoft_diffusion_infra_score` | Microsoft AI Diffusion 2025 | (subscore) | Ídem |
| `microsoft_diffusion_innovation_score` | Microsoft AI Diffusion 2025 | (subscore) | Ídem |
| `genai_adoption_pct` | Microsoft AI Economy Institute 2025 | Fig 4.3.10 | Citado, fuente Microsoft directo |
| `ai_job_posting_share_pct` (2025) | Lightcast 2025 | Fig 4.4.1 / 4.4.2 | Lightcast tiene API + reportes públicos |
| `state_backed_supercomputers_count` | Epoch AI | Fig 8.3.1 | Epoch dataset abierto (epoch.ai) |
| `data_localization_measures_count` | Ferracane et al. 2026 | Fig 8.3.3 | Replication data Ferracane |
| `nvidia_partnership` | Stanford HAI 2026 | Fig 8.3.2 | Binario derivable |
| `openai_stargate_partnership` | Stanford HAI 2026 | Fig 8.3.2 | Binario derivable |
| `ai_publications_per_capita` | Stanford AI Index 2026 Cap. 1 | (R&D landscape) | Derivable |
| `ai_patents_per_capita_v2` | Stanford AI Index 2026 Cap. 1 | (versión actualizada) | Derivable |
| `talent_flow_index_zeki` | Zeki/Brookings 2025 | Cap. 1 | Brookings data tools |
| `public_trust_ai_government_pct` | Stanford 2026 Cap. 9 | Public Opinion | Survey data citada |
| `ai_engineering_skills_growth_rate` | Stanford 2026 Take-away #13 | Lightcast subset | Derivable |
| `ai_safety_incident_count` | Stanford 2026 Cap. 3 (RAI) | RAI incidents | OECD AI Incident Tracker |
| `legislative_records_ai_count` | Stanford 2026 Cap. 8.4 | Global Legislative Records | Citado de Digital Policy Alert |

**Priorización P2:**
- **Must-have** (alto valor + alta disponibilidad): Microsoft subscores (4), Lightcast jobs, Epoch supercomputers, Ferracane localization → 7 variables
- **Nice-to-have**: Talent flow Zeki, Stanford patents/publications v2, public trust → 4 variables
- **Optional**: Nvidia/OpenAI partnerships (binarios derivables), AI safety incidents → 3 variables

### 4.4 GAP D — Targets Y para robustness multi-medida

Una sola Y es frágil. Para causalidad robusta usaremos múltiples Y de fuentes independientes:

| Y | Fuente | Status | Uso en MVP |
|---|---|---|---|
| `ai_adoption_rate` | Microsoft AI Diffusion 2025 | ✅ presente | Y primario |
| `ai_readiness_score` | Oxford Insights 2024 | ✅ presente | Y secundario (robustness) |
| `ai_publications_frac` | Stanford AI Index 2025 | ⚠ 2 missing → imputar | Y de R&D |
| `ai_patents_per100k` | Stanford AI Index 2025 | ⚠ 3 missing → imputar | Y de innovación |
| `ai_investment_per_capita` | derivar de cumulative ÷ pop | construir | Y económica |
| `ai_startups_per_capita` | derivar de cumulative ÷ pop | construir | Y emprendimiento |
| `genai_adoption_pct` | Microsoft AI Economy Institute 2025 | extraer (Fig 4.3.10) | Y de difusión consumer |
| `ai_job_posting_share_pct` | Lightcast 2025 | extraer | Y de demanda laboral |

**Total Y disponibles:** **8 variables Y multi-fuente**. El modelo estimará cada Y por separado (por método) y comparará coeficientes para evaluar consistencia.

### 4.5 Tabla síntesis de gaps

| Gap | Categoría | Acción | Esfuerzo | Bloquea MVP? |
|---|---|---|---|---|
| A | Missing en vars existentes | Imputar 25 valores | 1 sesión (~3h) | No (pero los modelos pierden poder) |
| B | X1 propuestas en CANDIDATES.md | Construir x1_master_v2.csv | 0.5 sesión (~2h) | No (pero pierdes mejoras de la skill) |
| C | Vars nuevas AI Index 2026 | Extraer 7-14 variables | 1.5 sesiones (~5h) | No (enriquecimiento) |
| D | Targets Y robustness | Construir 8 Y multi-fuente | 0.5 sesión (~2h) | No |

**Total esfuerzo extracción**: ~3.5 sesiones / 12h. **Crítica**: ninguno bloquea, todos enriquecen.

---

## 5. Plan de ejecución por fases

### Fase 0 — Extracción y enriquecimiento de datos (≈12h)

#### 0.A. Imputación P0 de Y missing (Gap A)

**Script:** `src/impute_missing_y_p0.py`

**Tareas:**
1. Cargar `sample_ready_cross_section.csv`.
2. Identificar las 12 celdas missing en `ai_patents_per100k`, `ai_publications_frac`, `ai_investment_vc_proxy`.
3. Para cada celda missing:
   - Buscar valor en fuente sugerida (OECD, UNESCO, Crunchbase, Stanford 2026).
   - Si valor encontrado: imputar + registrar fuente en columna `*_source` paralela.
   - Si no encontrado: marcar como NA estructural + documentar razón.
4. Output: `data/interim/sample_ready_imputed_p0.csv`.

**Decisión:** para TWN, imputar desde ROC NSC + Scopus directo (no World Bank). Documentar limitación.

#### 0.B. Extracción Microsoft Diffusion subscores (Gap C)

**Script:** `src/extract_top30_subscores_microsoft.py`

**Tareas:**
1. Buscar reporte original Microsoft AI Diffusion 2025 en `docs/` o descargarlo.
2. Extraer subscores `capital`, `skills`, `infra`, `innovation` para los 30 ISO3.
3. Output: `data/raw/microsoft/microsoft_diffusion_subscores_2025.csv` con columnas `iso3`, `capital_score`, `skills_score`, `infra_score`, `innovation_score`.

**Fallback:** si reporte original no es accesible, usar Stanford AI Index 2026 Fig 4.3.10 + texto Cap. 8 (que cita Microsoft) como mejor proxy disponible.

#### 0.C. Extracción Lightcast AI job postings (Gap C)

**Script:** `src/extract_lightcast_jobpostings.py`

**Tareas:**
1. Parsear AI Index 2026 PDF con `pdfplumber` para extraer Fig 4.4.1 + 4.4.2 (datos por país 2014-2025).
2. Si los datos están solo en gráfico (no tabla): extraer manualmente los 22 países visualizados.
3. Para los 30 del subset, asignar valor 2025 (% de job postings que requieren AI skills).
4. Output: `data/raw/lightcast/lightcast_ai_jobshare_2025.csv`.

#### 0.D. Extracción Epoch supercomputers (Gap C)

**Script:** `src/extract_epoch_supercomputers.py`

**Tareas:**
1. Visitar epoch.ai dataset abierto.
2. Filtrar AI supercomputers state-backed o public-private por país.
3. Para los 30 del subset, contar # clusters al 2025.
4. Output: `data/raw/epoch/epoch_supercomputers_2025.csv`.

#### 0.E. Extracción Ferracane data localization (Gap C)

**Script:** `src/extract_ferracane_localization.py`

**Tareas:**
1. Buscar Ferracane et al. (2026) replication data.
2. Para los 30, contar # data localization measures al 2024.
3. Output: `data/raw/ferracane/ferracane_localization_2024.csv`.

#### 0.F. Extracción otras variables AI Index 2026 (Gap C)

**Script:** `src/extract_aiindex_2026_misc.py`

**Tareas:**
1. Parsear AI Index 2026 PDF para variables adicionales:
   - `genai_adoption_pct` (Fig 4.3.10)
   - `nvidia_partnership`, `openai_stargate_partnership` (Fig 8.3.2)
   - `legislative_records_ai_count` (Cap. 8.4 Digital Policy Alert)
2. Output: `data/raw/aiindex_2026/aiindex_misc_2025.csv`.

#### 0.G. Construcción de Y derivadas (Gap D)

**Script:** `src/build_derived_y.py`

**Tareas:**
1. Cargar `sample_ready_imputed_p0.csv` + `population` (de WDI) + `gdp_current_usd`.
2. Construir:
   - `ai_investment_per_capita` = `ai_investment_usd_bn_cumulative` × 1e9 / `population`
   - `ai_startups_per_capita` = `ai_startups_cumulative` / `population` × 1e6
   - `ai_publications_per_capita` = `ai_publications_frac` × `total_publications_proxy` / `population` (si disponible)
3. Output: agrega columnas a `sample_ready_imputed_p0.csv`.

### Fase 1 — Consolidación dataset MVP (≈2h)

#### 1.A. Construcción `x1_master_v2.csv` (Gap B)

**Script:** `src/consolidate_x1_v2.py`

**Tareas:**
1. Para cada uno de los 29 P1-TOP30 procesados:
   - Leer `data/raw/legal_corpus/{ISO3}/CANDIDATES.md`.
   - Parsear sección §5 (recodificación propuesta) + §6 (diff summary) + §4 (autoridades).
   - Extraer:
     - `regulatory_intensity_proposed`
     - `thematic_coverage_proposed`
     - `regulatory_regime_group_proposed`
     - `enforcement_level_proposed`
     - `has_dedicated_ai_authority` (de §4)
     - `enforcement_governance_model` (de §4)
     - `eu_ai_act_implementation_date` (de §3 si EU member)
     - `ai_law_pathway_declared` (de FINDINGS.md banderas)
     - `confidence_iapp_to_skill`
     - `regime_change_iapp_vs_skill`
     - Métricas corpus: `ai_corpus_n_documents`, `ai_corpus_total_pages`, `ai_corpus_first_doc_year`, `ai_corpus_last_doc_year`, `ai_corpus_years_span`
2. Para CHL: dejar valores `_proposed` como NA (corpus pendiente).
3. Output: `data/interim/x1_master_v2.csv` (30 filas × ~16 columnas adicionales a `x1_master.csv`).

#### 1.B. Construcción `top30_master.csv`

**Script:** `src/build_top30_master.py`

**Tareas:**
1. Cargar `data/interim/sample_ready_imputed_p0.csv`.
2. Filtrar a los 30 ISO3.
3. JOIN con `x1_master_v2.csv` por `iso3`.
4. JOIN con datasets nuevos AI Index 2026:
   - `data/raw/microsoft/microsoft_diffusion_subscores_2025.csv`
   - `data/raw/lightcast/lightcast_ai_jobshare_2025.csv`
   - `data/raw/epoch/epoch_supercomputers_2025.csv`
   - `data/raw/ferracane/ferracane_localization_2024.csv`
   - `data/raw/aiindex_2026/aiindex_misc_2025.csv`
5. Agregar Y derivadas (`ai_investment_per_capita`, etc.).
6. Output: `data/interim/top30_master.csv` (30 filas × ~95 columnas).

**Verificación intermedia:**
```bash
python -c "
import pandas as pd
df = pd.read_csv('data/interim/top30_master.csv')
assert len(df) == 30
print(f'Shape: {df.shape}')
print(f'Missing %: {df.isna().mean().mean()*100:.1f}')
print(f'Países: {df.iso3.tolist()}')
"
```

### Fase 2 — EDA descriptivo (≈3h)

**Notebook:** `notebooks/03a_eda_top30_mvp.ipynb`

**Estructura por secciones:**

#### 2.1. Setup
- Imports (pandas, numpy, matplotlib, seaborn, scipy, statsmodels).
- Carga `top30_master.csv`.
- Functions auxiliares (boxplot por categoría, scatter con regression line, heatmap).

#### 2.2. Sanity check + completeness
- `df.shape`, `df.dtypes`, `df.iso3.nunique()`.
- Heatmap de missing values (filas = 30 países, cols = 95 vars).
- Tabla de top-10 columnas con más missing.

#### 2.3. Distribuciones univariadas
- **Y primario**: histograma + KDE de `ai_adoption_rate`, anotar mean/median/std.
- **Y secundario**: ídem `ai_readiness_score`, `ai_publications_frac`, `ai_patents_per100k`, `ai_investment_per_capita`.
- **X1 IAPP**: bar chart de `regulatory_regime_group` (counts), violin de `regulatory_intensity` por bucket, histograma de `thematic_coverage`.
- **X1 propuesta**: lo mismo con `*_proposed` para comparar.
- **X2 económica**: histograma log-scale de `gdp_per_capita_ppp`, `gdp_current_usd`, `population`.
- **X2 institucional**: bar de `legal_origin`, `is_common_law`, `eu_status`.

#### 2.4. Comparación X1 IAPP vs X1 propuesta (diff plots)
- Tabla 30 países × cambios en `intensity`, `coverage`, `regime_group`.
- Scatter `intensity_iapp` vs `intensity_proposed` con diagonal y=x.
- Bar chart de `regime_change_iapp_vs_skill` por país.

#### 2.5. Bivariadas Y ~ X1
- **Boxplot Y por `regulatory_regime_group`** (4 categorías): `ai_adoption_rate`, `ai_readiness_score`, etc.
  - Mostrar n por categoría.
  - ANOVA y Kruskal-Wallis con p-value.
- **Scatter Y vs `regulatory_intensity`** con regresión lineal:
  - Spearman ρ + p-value en título.
  - Pearson r como comparación (más sensible a outliers).
- **Scatter Y vs `thematic_coverage`** (X1 secundaria).

#### 2.6. Correlaciones
- Matriz Spearman de Y (8) × X1 (8) × X2 selectivos (10) = ~26 vars.
- Heatmap con mask para diagonal.
- Tabla top-15 correlaciones absolutas.

#### 2.7. Clustering exploratorio
- K-means k=4 sobre features X1+X2 normalizadas (StandardScaler).
- PCA 2D para visualizar clusters.
- Anotar cada punto con ISO3.
- Tabla cluster vs `regulatory_regime_group` (esperamos correspondencia parcial).

#### 2.8. Country profiling
- Para cada uno de los 30, ficha de 1 línea:
  - `iso3 | regime | intensity | adoption_rate | readiness | gdp | eu_member | legal_origin`
- Tabla ordenable.

#### 2.9. Hallazgos preliminares
- Lista de 5-10 observaciones del EDA.
- Hipótesis tentativas a testear en Fase 4.

**Reusables:**
- Patrones de [notebooks/03_eda.ipynb](../notebooks/03_eda.ipynb) — base EDA general.
- Patrones de [ADE/01_ADE_Analisis_Exploratorio.ipynb](../ADE/01_ADE_Analisis_Exploratorio.ipynb) — boxplots por grupo regulatorio.

### Fase 3 — Feature engineering (≈2h)

**Notebook:** `notebooks/04a_features_top30_mvp.ipynb`

**Tareas:**

#### 3.1. Preprocesamiento
- Imputación de NA estructurales (TWN) con flag `_imputed`.
- Outlier detection (IQR) en variables continuas.

#### 3.2. Codificación categóricas
- One-hot `regulatory_regime_group` (4 niveles → 3 dummies con drop_first).
- One-hot `legal_origin` (4-5 niveles → drop_first).
- One-hot `enforcement_level` (4 niveles → drop_first).
- One-hot `enforcement_governance_model` (4 niveles → drop_first, X1 v2).

#### 3.3. Escalado
- StandardScaler (z-score) para `regulatory_intensity`, `thematic_coverage`, scores 0-100, scores 0-10.
- MinMaxScaler para variables proporcionales (`internet_penetration`, `tertiary_education`).

#### 3.4. Transformaciones logarítmicas
- `log_gdp` = log(gdp_current_usd)
- `log_population` = log(population)
- `log_ai_investment_per_capita` = log(ai_investment_per_capita + 1)
- `log_ai_startups_per_capita` = log(ai_startups_per_capita + 1)

#### 3.5. Interacciones
- `regime × eu_status` (especialmente para identificar efecto AI Act).
- `intensity × log_gdp` (efecto regulación moderado por riqueza).
- `intensity × is_common_law` (efecto regulación moderado por tradición legal).

#### 3.6. Output
- `data/interim/X_top30.csv` — matriz features (30 × ~50).
- `data/interim/Y_top30.csv` — matriz targets (30 × 8).
- `data/interim/feature_dictionary.csv` — diccionario de variables con descripciones.

### Fase 4 — Modelado correlación + causalidad (≈5h)

**Notebook:** `notebooks/04b_modeling_top30_mvp.ipynb`

> **Honestidad metodológica:** Con N=30 cross-section, "causalidad" es un **claim limitado**. El MVP entrega evidencia **observacional + robustness multi-método**, no causal estricto. Las limitaciones se discuten explícitamente.

#### 4.1. Modelos correlacionales (descriptivos)

**M1 — OLS multivariado para cada Y:**
```python
import statsmodels.api as sm

for Y_var in ['ai_adoption_rate', 'ai_readiness_score', ...]:
    X = features[['regime_binding', 'regime_soft', 'intensity_z',
                  'log_gdp', 'gii_score', 'internet_penetration']]
    model = sm.OLS(df[Y_var], sm.add_constant(X)).fit(cov_type='HC3')
    print(model.summary())
```
- Robust SE (HC3).
- Reportar: coef, SE, t, p, R² adj, AIC.
- N=30 ⇒ máx 5-6 covariables (regla de oro: 5 obs/var).

**M2 — Regresión logística multinomial inversa (predictivo):**
```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(multi_class='multinomial', max_iter=1000)
clf.fit(X_features, df['regulatory_regime_group'])
print(clf.score(X_features, df['regulatory_regime_group']))
```
- ¿Cuál es la accuracy de "predecir" régimen desde Y + X2?
- Si alta → señal de endogeneidad (los países regulan según su Y).
- Si baja → menos endogeneidad.

**M3 — Correlación parcial (Spearman):**
- `Y ~ regime` controlando por `gdp` y `gii`.
- Para cada Y individual.

#### 4.2. Modelos causales (limitados, multi-método)

**M4 — Synthetic Control Method (SCM) para CHL:**
```python
from synthcontrol import SyntheticControl
# CHL es treated; usar los otros 29 como donor pool
sc = SyntheticControl(
    treatment_country='CHL',
    donor_countries=[...29 ISO3...],
    pre_treatment_features=['gdp_per_capita_ppp', 'gii_score', 'internet_penetration'],
    treatment_year=2025  # cuando hipotéticamente entra Boletín 16821-19
)
sc.fit()
sc.plot_counterfactual('ai_adoption_rate')
```
- Construir CHL "sintético" como combinación de países similares.
- Visualizar trayectoria contrafactual.
- **Limitación importante:** SCM requiere panel data; con cross-section solo es ilustrativo.

**M5 — Coarsened Exact Matching (CEM):**
```python
from cem import CEM
matched = CEM.match(
    df,
    treatment='regime_binding',
    covariates=['gdp_quartile', 'region', 'eu_status', 'common_law']
)
ate = matched.compute_ate('ai_adoption_rate')
```
- Parejar países `binding_regulation` con `soft_framework` por GDP-quartile + region + EU + common_law.
- Estimar Average Treatment Effect (ATE) sobre Y.
- **Limitación:** N=30 hace que muchos matches no existan; reducir CEM bins.

**M6 — Instrumental Variables (IV):**
```python
from linearmodels.iv import IV2SLS
# Instrumento: legal_origin (Common law tiende a regulación blanda)
ivmodel = IV2SLS.from_formula(
    'ai_adoption_rate ~ 1 + log_gdp + [regulatory_intensity ~ legal_origin]',
    df
).fit()
```
- `legal_origin` como instrumento exógeno para `regulatory_intensity` (variación en regulación independiente de Y por razones históricas).
- **Limitación:** validez del instrumento depende de exogeneidad de legal_origin sobre Y, debatible.

**M7 — Bayesian regression con priors informados:**
```python
import bambi as bmb
model = bmb.Model(
    'ai_adoption_rate ~ regime + intensity_z + log_gdp + gii_score',
    data=df,
    priors={
        'regime[binding_regulation]': bmb.Prior('Normal', mu=0, sigma=10),
        # priors weakly informative dados N=30
    }
)
fit = model.fit(draws=4000, chains=4, target_accept=0.95)
print(fit.summary())
```
- Priors weakly informative dado N pequeño.
- HDI 95% en lugar de CIs frequentista.
- Posterior predictive checks.

**M8 — Bootstrap percentile CIs para todos los modelos:**
- 10,000 resamples para cada estimador (OLS, IV, matching).
- CIs percentile 2.5% / 97.5%.
- Permutation tests (shuffle treatment) para p-values robustos.

#### 4.3. Análisis de sensibilidad

**S1 — IAPP vs proposed:**
- Re-correr M1, M3, M4, M5, M7 con `regulatory_intensity_proposed` en lugar de IAPP.
- Comparar coeficientes lado a lado.
- Si signo y magnitud consistentes ⇒ resultado robusto a recodificación.

**S2 — Excluir TWN, EU bloque, USA outlier:**
- Re-correr M1 con (a) sin TWN (datos limitados), (b) sin EU members (homogeneidad regulatoria), (c) sin USA (peso desproporcionado en ai_investment).
- Reportar cambios en coef principales.

**S3 — Multiple Y consistency check:**
- ¿Los coef de `regime_binding` tienen mismo signo en las 8 Y?
- Tabla wide: Y rows × modelo columns × coef cells.

**S4 — Subset binary EU vs no-EU:**
- N=15 EU (todos `binding_regulation`).
- N=15 no-EU (mezcla buckets).
- Comparar Y mean entre grupos como naive baseline.

#### 4.4. Outputs de la Fase 4

- `data/processed/coefficients_top30.csv` — tabla completa de todos los coeficientes con CIs.
- `data/processed/sensitivity_analysis_top30.csv` — variations across robustness checks.
- 5-8 figuras: SCM CHL, OLS coefs forest plot, Bayesian posterior, sensitivity heatmap.

### Fase 5 — Reporte MVP (≈2h)

**Notebook:** `notebooks/05a_results_top30_mvp.ipynb`
**Documento:** `docs/MVP_TOP30_RESULTS.md`

**Estructura:**

1. **Resumen ejecutivo** (1 página):
   - Hallazgo #1: dirección Y ~ régimen (signo + magnitud)
   - Hallazgo #2: confounding por GDP/EU
   - Hallazgo #3: SCM CHL (interpretación cualitativa)
   - Decisión go/no-go para 86 países

2. **Hallazgos por hipótesis** (3-4 páginas):
   - H1: ¿Países con `binding_regulation` tienen menor `ai_adoption_rate`? (efecto pessimista)
   - H2: ¿Países con regulación más intensa tienen mayor `ai_readiness_score`? (efecto institucional)
   - H3: ¿La regulación afecta diferencialmente a Y de innovación (patentes, publicaciones) vs Y de adopción (uso)?
   - H4: ¿Es CHL `strategy_only` actual mejor o peor que su contrafactual (otros LATAM, otros strategy_only)?

3. **Tablas de resultados** (2 páginas):
   - Tabla coef principales (M1 OLS, todas las Y).
   - Tabla sensitivity (IAPP vs proposed).
   - Tabla SCM CHL.

4. **Figuras** (5-7):
   - Boxplot Y por bucket regulatorio.
   - Forest plot OLS coefs con CIs bootstrap.
   - SCM CHL.
   - Posterior Bayesian.
   - Sensitivity heatmap.

5. **Limitaciones** (1 página):
   - N=30 cross-section.
   - Causalidad limitada.
   - Selección de muestra (Top 30 = high-income skew).
   - Endogeneidad.

6. **Recomendación final**:
   - **GO** (extender a 86 países): si coef principales son robustos a sensibilidad y consistentes en al menos 5/8 Y.
   - **PIVOT**: si resultados son débiles pero metodología necesita ajustes (ej. más IV, panel data).
   - **NO-GO**: si N=30 ya muestra ruido sin señal, aumentar N no solucionaría sin diseño distinto.

---

## 6. Arquitectura de archivos

### 6.1 Archivos a crear (nuevos)

#### Scripts en `src/`
- `extract_top30_subscores_microsoft.py`
- `extract_lightcast_jobpostings.py`
- `extract_epoch_supercomputers.py`
- `extract_ferracane_localization.py`
- `extract_aiindex_2026_misc.py`
- `impute_missing_y_p0.py`
- `build_derived_y.py`
- `consolidate_x1_v2.py`
- `build_top30_master.py`

#### Datos en `data/raw/`
- `data/raw/microsoft/microsoft_diffusion_subscores_2025.csv`
- `data/raw/lightcast/lightcast_ai_jobshare_2025.csv`
- `data/raw/epoch/epoch_supercomputers_2025.csv`
- `data/raw/ferracane/ferracane_localization_2024.csv`
- `data/raw/aiindex_2026/aiindex_misc_2025.csv`

#### Datos en `data/interim/`
- `data/interim/sample_ready_imputed_p0.csv`
- `data/interim/x1_master_v2.csv`
- `data/interim/top30_master.csv`
- `data/interim/X_top30.csv`
- `data/interim/Y_top30.csv`
- `data/interim/feature_dictionary.csv`

#### Datos en `data/processed/`
- `data/processed/coefficients_top30.csv`
- `data/processed/sensitivity_analysis_top30.csv`

#### Notebooks
- `notebooks/03a_eda_top30_mvp.ipynb`
- `notebooks/04a_features_top30_mvp.ipynb`
- `notebooks/04b_modeling_top30_mvp.ipynb`
- `notebooks/05a_results_top30_mvp.ipynb`

#### Documentación
- `docs/MVP_TOP30_RESULTS.md` — reporte final
- `ARCHIVOS_MD_CONTEXTO/PLAN_MVP_TOP30_PAISES.md` — este archivo
- `ARCHIVOS_MD_CONTEXTO/ACLARACION_ESTADO_TOP30_PAISES.md` — aclaración estados

### 6.2 Archivos a modificar (mínimamente)

- `.claude/skills/corpus-legal-ia/sample.md` — verificar/sincronizar columna "Aprobado".
- `docs/HALLAZGOS_DIFERENCIALES.md` — link a MVP results al final.

### 6.3 Reusables existentes (NO duplicar)

Ya existen en el proyecto:
- [src/build_sample_ready.py](../src/build_sample_ready.py) — patrón de joining datasets.
- [src/consolidate_x1.py](../src/consolidate_x1.py) — patrón consolidación X1.
- [src/audit_completeness.py](../src/audit_completeness.py) — patrón de completeness reporting.
- [src/build_derived_controls.py](../src/build_derived_controls.py) — patrón derivación controles.
- [notebooks/01_recoleccion.ipynb](../notebooks/01_recoleccion.ipynb) — patrón scraping/extracción.
- [notebooks/02_limpieza.ipynb](../notebooks/02_limpieza.ipynb) — patrón limpieza.
- [notebooks/03_eda.ipynb](../notebooks/03_eda.ipynb) — base EDA general.
- [ADE/01_ADE_Analisis_Exploratorio.ipynb](../ADE/01_ADE_Analisis_Exploratorio.ipynb) — boxplots por grupo regulatorio.
- [data/interim/sample_ready_cross_section.csv](../data/interim/sample_ready_cross_section.csv) — base de partida.

### 6.4 Diagrama de flujo

```
sample_ready_cross_section.csv (86 × 70)
         │
         ▼
  impute_missing_y_p0.py
         │
         ▼
sample_ready_imputed_p0.csv (86 × 70 + sources)
         │
         │  ┌─────────────────────────────┐
         │  │ extract_*.py (P2 enrichment)│
         │  └──────────────┬──────────────┘
         │                 │
         │                 ▼
         │        microsoft/lightcast/epoch/...
         │        ferracane/aiindex_misc.csv
         │                 │
         │     ┌───────────┘
         │     │
         │     │  ┌──────────────────────┐
         │     │  │ consolidate_x1_v2.py │
         │     │  └──────────┬───────────┘
         │     │             │
         │     │             ▼
         │     │    x1_master_v2.csv (29 × ~16)
         │     │             │
         │     │             │
         ▼     ▼             ▼
         build_top30_master.py
                  │
                  ▼
       top30_master.csv (30 × ~95)
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
  03a_eda    04a_feat    04b_model
                              │
                              ▼
                   coefficients_top30.csv
                   sensitivity_analysis_top30.csv
                              │
                              ▼
                   MVP_TOP30_RESULTS.md
```

---

## 7. Decisiones metodológicas

### 7.1 Diseño cross-section vs panel

**Decisión:** cross-section 2025.

**Rationale:**
- Los datos disponibles son anuales 2024-2025; la regulación IA es muy reciente (post-2023).
- Panel pre/post AI Act sería ideal pero no factible con datos actuales.
- Workaround: SCM CHL provee mini-panel ilustrativo.

### 7.2 Y primario vs múltiple

**Decisión:** Y primario = `ai_adoption_rate` (Microsoft) + 7 Y secundarias.

**Rationale:**
- `ai_adoption_rate` es coherente narrativamente con la fuente de la muestra (Top 30 Microsoft).
- 8 Y permiten consistency check robusto a una mala medida.
- Stanford `ai_readiness_score` es Y secundaria por validez convergente.

### 7.3 X1 IAPP vs proposed

**Decisión:** ambas en paralelo, columnas separadas.

**Rationale:**
- Las 13 propuestas "Sí" ya están aprobadas → idénticas.
- Las 16 "Pendiente" tienen propuestas que mejoran calidad (skill leyó docs primarios, IAPP es heurística).
- Análisis de sensibilidad (S1) compara ambos lados.

### 7.4 Inclusión CHL

**Decisión:** incluir CHL en N=30 sin esperar corpus legal.

**Rationale:**
- Datos cuantitativos CHL ya disponibles desde IAPP/Microsoft/Oxford.
- CHL es caso focal narrativo (Boletín 16821-19).
- SCM CHL requiere CHL en sample.
- Procesar corpus CHL después del MVP es decisión separada.

### 7.5 Tratamiento TWN

**Decisión:** mantener TWN con NA estructurales documentados.

**Rationale:**
- World Bank no publica TWN por razones políticas.
- TWN es Top 22 Microsoft y debe estar.
- Imputar desde ROC NSC + Scopus + IMF para vars críticas; otras quedan NA.
- En sensibilidad S2, re-correr modelos sin TWN.

### 7.6 Dummies regionales

**Decisión:** usar `region` como FE solo en sensibilidad, NO en M1 principal.

**Rationale:**
- N=30 con 8 regiones = 22 grados libertad efectivos. Demasiado para OLS.
- En cambio, usar `eu_status` (binario) + `is_common_law` como proxies regionales.

### 7.7 Outlier handling

**Decisión:** WinsorizeR al 5%/95% solo en Y económicas (ai_investment*); robustness HC3 en SE.

**Rationale:**
- USA es outlier extremo en ai_investment (~$285B vs media ~$10B).
- Winsorizar mantiene a USA pero comprime cola.
- HC3 SE robust a heterocedasticidad.

---

## 8. Métodos cuantitativos: correlación + causalidad

### 8.1 Diferencia conceptual

| Aspecto | Correlación | Causalidad |
|---|---|---|
| Pregunta | "¿Y se asocia con X?" | "¿Cambiar X cambia Y?" |
| Diseño | Cualquier observacional | Experimental o cuasi-experimental |
| Confianza con N=30 | Alta (con bootstrap) | Limitada (sin variación temporal) |
| Métodos del MVP | M1, M3 | M4, M5, M6, M7 |

### 8.2 Cuándo "causalidad" es defendible con N=30

- **SCM:** si hay tratamiento dicotómico claro y donor pool válido. CHL único treated; resto donor.
- **CEM:** si los matches existen (overlap entre treated y control en X2).
- **IV:** si instrumento es exógeno y relevante. `legal_origin` razonable pero debatible.
- **Bayesian:** si priors son defendibles, posterior se puede interpretar como creencia actualizada.

### 8.3 Cuándo "causalidad" NO es defendible

- N=30 es chico para Frequentist nominal coverage.
- Sin variación temporal pre/post.
- Sin RCT (obviamente).
- Endogeneidad regulación↔Y bidireccional.

### 8.4 Recomendación operativa

**No reclamar "causalidad estricta" en `MVP_TOP30_RESULTS.md`.** Reclamar:
- "Asociación condicional robusta a múltiples especificaciones" (M1+sensitivity)
- "Evidencia tentativa cuasi-experimental" (SCM CHL)
- "Estimación bayesiana con priors weakly informative" (M7)
- "Direcciones consistentes con literatura" (si aplica)

Reservar el lenguaje "efecto causal" SOLO si IV pasa los Sargan/F-stat tests (improbable con N=30).

---

## 9. Verification end-to-end

### 9.1 Tests de smoke

```bash
# Test 1 — Dataset MVP existe y tiene 30 filas
python -c "
import pandas as pd
df = pd.read_csv('data/interim/top30_master.csv')
assert len(df) == 30, f'Expected 30 rows, got {len(df)}'
assert df.iso3.nunique() == 30
print('OK — top30_master.csv has 30 países')
"

# Test 2 — X1 v2 tiene los 29 países procesados con propuestas
python -c "
import pandas as pd
df = pd.read_csv('data/interim/x1_master_v2.csv')
done = df.regulatory_intensity_proposed.notna().sum()
assert done >= 29, f'Expected ≥29 with proposed, got {done}'
print(f'OK — x1_master_v2.csv has {done}/30 with _proposed')
"

# Test 3 — Y missing imputados
python -c "
import pandas as pd
df = pd.read_csv('data/interim/top30_master.csv')
critical = ['ai_patents_per100k', 'ai_publications_frac', 'ai_investment_vc_proxy']
miss = df[critical].isna().sum()
print(f'Missing post-imputation:')
print(miss)
# Aceptamos máx 5 missing total tras imputación
assert miss.sum() <= 5, f'Too many missing: {miss.sum()}'
print('OK — imputation P0 successful')
"

# Test 4 — Notebooks ejecutan sin error
jupyter nbconvert --to notebook --execute notebooks/03a_eda_top30_mvp.ipynb --output 03a_executed.ipynb
jupyter nbconvert --to notebook --execute notebooks/04a_features_top30_mvp.ipynb --output 04a_executed.ipynb
jupyter nbconvert --to notebook --execute notebooks/04b_modeling_top30_mvp.ipynb --output 04b_executed.ipynb

# Test 5 — Outputs de modelado existen
test -f data/processed/coefficients_top30.csv
test -f data/processed/sensitivity_analysis_top30.csv

# Test 6 — Reporte final existe
test -f docs/MVP_TOP30_RESULTS.md
test $(wc -l < docs/MVP_TOP30_RESULTS.md) -ge 200  # mínimo 200 líneas
```

### 9.2 Tests metodológicos

```bash
# Test M1 OLS no rompe
python -c "
import statsmodels.api as sm
import pandas as pd
df = pd.read_csv('data/interim/top30_master.csv').dropna(subset=['ai_adoption_rate'])
y = df['ai_adoption_rate']
X = sm.add_constant(df[['regulatory_intensity', 'gdp_per_capita_ppp']].dropna())
y_aligned = y.loc[X.index]
m = sm.OLS(y_aligned, X).fit(cov_type='HC3')
assert m.rsquared >= 0  # tautológico pero detecta NaN
print(f'M1 R² adj: {m.rsquared_adj:.3f}')
"

# Test M4 SCM CHL produce contrafactual válido
# (test específico depende de implementación SCM)
```

### 9.3 Sanity checks de resultados

- ¿Coef de `regulatory_intensity` cambia signo entre M1 y M3? Si sí, marcar como NO-robusto.
- ¿R² ajustado de M1 es > 0.30? Si no, modelos pobres explicativamente.
- ¿SCM CHL converge (suma de pesos donor = 1, RMSPE pre-treatment razonable)?
- ¿Bayesian posterior tiene Rhat < 1.05 y ESS > 400?

---

## 10. Limitaciones explícitas

### 10.1 Limitaciones inherentes a N=30

1. **Poder estadístico bajo.** Detectar efectos pequeños requiere N grande. Con N=30, solo efectos medianos-grandes son detectables al 5%.
2. **Errores estándar amplios.** CIs van a ser anchos. Intervalos puede contener 0 incluso para efectos reales.
3. **Sensibilidad a outliers.** Cada país pesa 3.3% del análisis. USA o TWN solo pueden mover coef.
4. **Multicolinearidad probable.** EU member fuertemente correlacionado con `binding_regulation`, `regulatory_intensity`, `gdp_per_capita_ppp` alto. Difícil separar contribuciones.
5. **Curse of dimensionality.** No factible incluir muchas covariables; trade-off entre confounding control y df.

### 10.2 Limitaciones del diseño cross-section

1. **Sin variación temporal.** No DiD, no event study. SCM CHL es ilustrativo, no inferencial estricto.
2. **Endogeneidad regulación↔adopción.** Países con más IA regulan más; países que regulan retroactivamente reflejan adopción ya alta. IV partial workaround.
3. **Selección no aleatoria de la muestra.** Top 30 Microsoft es muestra propositiva (high-income skew). Generalización a 86 países pendiente del MVP.
4. **Brussels Effect confounding.** EU members convergen regulatoriamente por AI Act, dificultando aislar efecto AI Act específico de cultura regulatoria europea.

### 10.3 Limitaciones de las medidas

1. **Microsoft AI Diffusion 2025 es propietario.** Subscores específicos pueden no estar accesibles públicamente; mejor effort de extracción.
2. **IAPP X1 base es heurística.** La skill mejora muchos casos pero IAPP queda como "ground truth" oficial.
3. **Recodificación skill no aprobada en 16/29.** Sensibilidad S1 es crítica.
4. **TWN datos limitados.** 7 missing en X2; resultados sin TWN deben compararse.
5. **Stanford AI Index 2026 cita Microsoft 2025 como fuente de adopción.** Riesgo de circularidad si ambas se usan como Y/X.

### 10.4 Cómo mitigar (parcialmente)

| Limitación | Mitigación implementada |
|---|---|
| N=30 chico | Bootstrap percentile CIs (10k resamples), Bayesian con priors weakly informative |
| Sin variación temporal | SCM CHL como mini-panel ilustrativo, IV con `legal_origin` |
| Selección muestra | Sensitivity S2 (excluir EU bloque, USA) |
| Brussels Effect | Modelo separado solo no-EU (N=15) como check |
| Recodificación pendiente | Sensitivity S1 (IAPP vs proposed) |
| TWN missings | Imputar desde alternative sources + sensitivity sin TWN |

### 10.5 Lo que el MVP NO puede entregar

- **Causalidad fuerte.** Para eso necesitas RCT o cuasi-experimento natural con variación exógena clara (no disponible aquí).
- **Generalización a países low-income.** Top 30 está sesgado a high/upper-middle income.
- **Efectos heterogéneos por sector.** Y agregadas país-nivel no permiten cortes sector × régimen.
- **Predicción year-on-year.** Sin panel, no proyección temporal.

---

## 11. Estimación de tiempo

| Fase | Tareas | Esfuerzo | Output |
|---|---|---|---|
| 0.A | Imputación P0 Y missing | 1-2h | sample_ready_imputed_p0.csv |
| 0.B | Microsoft subscores | 1h | microsoft_diffusion_subscores_2025.csv |
| 0.C | Lightcast jobs | 2h | lightcast_ai_jobshare_2025.csv |
| 0.D | Epoch supercomputers | 1h | epoch_supercomputers_2025.csv |
| 0.E | Ferracane localization | 1h | ferracane_localization_2024.csv |
| 0.F | Otras AI Index 2026 | 2h | aiindex_misc_2025.csv |
| 0.G | Y derivadas | 1h | (agregadas a interim) |
| **Subtotal Fase 0** | | **~9h** | 5+ CSVs nuevos |
| 1.A | x1_master_v2.csv | 2h | x1_master_v2.csv |
| 1.B | top30_master.csv | 1h | top30_master.csv |
| **Subtotal Fase 1** | | **~3h** | 2 CSVs |
| 2 | Notebook 03a EDA | 3h | 15+ figuras |
| 3 | Notebook 04a Features | 2h | X/Y matrices |
| 4 | Notebook 04b Modeling | 5h | 8 modelos + sensitivity |
| 5 | Notebook 05a + RESULTS.md | 2h | reporte final |
| **TOTAL MVP** | | **~24h** | dataset + 4 notebooks + 2 docs |

Distribuido en **5-7 sesiones** de trabajo activo. Sesiones recomendadas:

| Sesión | Tareas | Duración |
|---|---|---|
| S1 | Fase 0.A (imputación P0) + 0.G (derivadas) | 3h |
| S2 | Fase 0.B-0.F (extracción AI Index) | 5h |
| S3 | Fase 1.A-1.B (consolidación) | 3h |
| S4 | Fase 2 (EDA notebook) | 3h |
| S5 | Fase 3 (features) + Fase 4.1 (correlacionales) | 4h |
| S6 | Fase 4.2 (causales) + 4.3 (sensibilidad) | 4h |
| S7 | Fase 5 (reporte + decisión final) | 2h |

---

## 12. Criterios de éxito y go/no-go para extender a 86 países

### 12.1 Criterios cuantitativos

**GO (proceder con corpus 56 países restantes):** se cumplen al menos 5 de 7:

- [ ] Coef de `regulatory_intensity` significativo al 10% en M1 OLS para Y primario.
- [ ] Signo del coef consistente entre M1 IAPP y M1 proposed.
- [ ] Signo consistente en al menos 5/8 Y secundarias.
- [ ] CIs bootstrap NO contienen 0 para Y primario.
- [ ] R² ajustado M1 ≥ 0.40.
- [ ] SCM CHL converge con RMSPE pre-treatment ≤ 1.0× std de Y donor pool.
- [ ] Bayesian posterior 95% HDI excluye 0.

### 12.2 Criterios cualitativos

**GO** si además:
- Hallazgos consistentes con literatura (ej: Korinek, Acemoglu).
- Hallazgos útiles para Boletín 16821-19 (narrativa para legislativo chileno).
- Limitaciones documentadas no debilitan conclusiones core.

### 12.3 Criterios de PIVOT (no-GO con ajustes)

Si los criterios anteriores fallan PERO:
- Hay patrones interesantes solo en submuestras (ej: solo no-EU).
- Hay interacciones no exploradas (régimen × sector económico).
- Variables nuevas AI Index 2026 muestran señal donde IAPP no.

→ Ajustar diseño antes de extender a 86. Posibles ajustes:
- Cambiar Y primario.
- Agregar más X2.
- Re-codificar X1 (post aprobación humana de los 16 pendientes).
- Diseñar panel pseudo-temporal con Stanford 2025 + 2026.

### 12.4 Criterios de NO-GO definitivo

Si:
- Coef cero o erráticos en todos los modelos.
- Sin hallazgos defendibles para Boletín 16821-19.
- Diseño cross-section es insuficiente y no hay forma de salvarlo con 86 países.

→ Reformular pregunta de investigación o cambiar fuente de variación principal.

### 12.5 Decisión final en `MVP_TOP30_RESULTS.md`

El documento final tendrá una sección **§Decisión** con:
1. Veredicto: GO / PIVOT / NO-GO.
2. Justificación cuantitativa.
3. Recomendación operativa para Fase 2 del proyecto (post-MVP).

---

## 13. Riesgos identificados y mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Microsoft Diffusion subscores no accesibles públicamente | Alta | Medio | Usar Stanford 2026 como proxy; documentar limitación |
| Lightcast PDF data extraction fails | Media | Bajo | Manual transcription como fallback (22 países) |
| Epoch dataset cambió formato | Baja | Bajo | Versión cached vs latest |
| TWN datos imposibles de imputar | Media | Bajo | Documentar NA estructural; sensitivity sin TWN |
| Modelos no convergen | Baja | Alto | Bayesian con priors tighter; reducir features |
| SCM CHL no encuentra donors válidos | Media | Medio | Relax matching; usar variable Y proxy |
| IV `legal_origin` falla F-stat | Alta | Bajo | NO reportar como causal; downgrade a sensitivity |
| Coef consistentes pero no significativos (Type II) | Alta | Medio | Reportar magnitud + dirección + power analysis |

---

## 14. Apéndices

### A. Glosario de variables MVP

(Ver sección 4 del documento + `data/interim/feature_dictionary.csv` post-implementación)

### B. Referencias bibliográficas clave

- IAPP. (2025). *Global AI Law and Policy Tracker*.
- Microsoft. (2025). *AI Diffusion Report*.
- Oxford Insights. (2024). *Government AI Readiness Index*.
- Stanford HAI. (2026). *AI Index Report 2026*. [docs/ai_index_report_2026.pdf]
- WIPO. (2024). *Global Innovation Index*.
- Ferracane, M. F., et al. (2026). Data localization measures dataset.
- Epoch AI. (2025). State-backed AI supercomputers dataset.

### C. Comandos clave de inicio

```bash
# Verificar estado actual
ls /home/pablo/Research_LeyIA_DataScience/data/interim/
cat /home/pablo/Research_LeyIA_DataScience/.claude/skills/corpus-legal-ia/sample.md | grep "P1-TOP30"

# Arrancar Fase 0
python /home/pablo/Research_LeyIA_DataScience/src/impute_missing_y_p0.py

# Verificar tras Fase 0
python -c "import pandas as pd; print(pd.read_csv('data/interim/sample_ready_imputed_p0.csv').isna().sum())"

# Arrancar Fase 1
python /home/pablo/Research_LeyIA_DataScience/src/consolidate_x1_v2.py
python /home/pablo/Research_LeyIA_DataScience/src/build_top30_master.py

# Arrancar Fase 2
jupyter notebook notebooks/03a_eda_top30_mvp.ipynb
```

### D. Contactos y dependencias externas

- **Crunchbase Pro:** acceso para imputar `ai_investment_vc_proxy`.
- **Lightcast:** datos pueden requerir API key.
- **OECD:** datasets públicos AI Patent + AI Going Digital.
- **UNESCO UIS:** rd_expenditure para JOR, ARE.
- **ROC NSC:** para imputar TWN R&D.

---

**Fin del Plan MVP — Top 30 países + Chile.**

Este documento es la **fuente de verdad** del MVP. Cualquier desviación debe documentarse como PR a este archivo. Las fases pueden ejecutarse en paralelo dentro de una sesión cuando son independientes (ej: 0.B, 0.D, 0.E).

**Próxima acción tras aprobar este plan:** ejecutar Sesión S1 (Fase 0.A imputación + 0.G derivadas) → genera `sample_ready_imputed_p0.csv`.
