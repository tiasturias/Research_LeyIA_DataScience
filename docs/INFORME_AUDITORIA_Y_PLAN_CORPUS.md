# Informe de Auditoría Científica y Plan de Corpus Legal

**Proyecto:** LeyIA DataScience — ¿Regular o no regular? Impacto de marcos regulatorios de IA en ecosistemas nacionales de IA
**Fecha auditoría:** 2026-04-14
**Fecha informe consolidado:** 2026-04-15
**Estado proyecto:** Fase 1 (recolección) cerrada para variables numéricas · Corpus legal pendiente
**Nivel de riesgo político:** **ALTO** — informa el Proyecto de Ley Marco IA Chile (16821-19)

---

## Índice

1. [Valoración global](#1-valoración-global)
2. [Problemas críticos (bloqueantes para inferencia causal)](#2-problemas-críticos)
3. [Problemas moderados](#3-problemas-moderados)
4. [Fortalezas reconocidas](#4-fortalezas-reconocidas)
5. [Estado post-Tarea A (abril 2026)](#5-estado-post-tarea-a)
6. [Plan detallado Tarea B — recodificación low-confidence](#6-plan-detallado-tarea-b)
7. [Plan detallado Tarea C — extracción corpus legal](#7-plan-detallado-tarea-c)
8. [Human-in-the-loop: qué hace el investigador, qué hace el sistema](#8-human-in-the-loop)
9. [Roadmap priorizado](#9-roadmap-priorizado)
10. [Clasificación problemas × fase](#10-clasificación-problemas--fase)
11. [Opinión franca](#11-opinión-franca)

---

## 1. Valoración global

El proyecto tiene una **calidad infraestructural de nivel top-tier académico** (mejor que el 80% de los papers de política pública revisados). La trazabilidad documental (`DATA_DECISIONS_LOG.md` con 17 decisiones numeradas, `ETL_RUNBOOK.md`, 7 archivos `VARIABLES_*.md`, `SEGUIMIENTO_PAISES_MUESTRA.md`) es de calidad publicable en *Policy Sciences* o *Regulation & Governance*.

**PERO** existen **8 problemas metodológicos críticos** que, si no se resuelven antes de que este estudio informe la ley chilena, pueden producir **conclusiones causales inválidas** que el gobierno usaría para legislar mal.

---

## 2. Problemas críticos

### 🔴 PROBLEMA #1 — Endogeneidad / causalidad inversa *(el más grave)*

**Diagnóstico:** El diseño es *cross-section* 2025 con regulación y outcomes medidos contemporáneamente. Esto hace que la **dirección causal sea irresoluble estadísticamente**.

- Pregunta política: *"¿la regulación causa menor/mayor inversión, adopción e innovación?"*
- Pero el dataset también puede responder: *"los países con ecosistemas IA maduros desarrollan regulación (porque tienen algo que regular)"*
- **Ejemplo concreto**: la EU AI Act (2024) no causó la concentración de inversión IA en Alemania/Francia — Alemania/Francia **ya tenían** esa inversión y por eso la UE legisló. Confundir las dos historias es un error de primer año de econometría.

**Fix obligatorio (orden de preferencia):**

1. **Lag estructural** — Medir Y en 2025 pero X1 en 2022-2023 (año de promulgación, no vigencia). El campo `year_enacted` lo permite, pero no se está usando así.
2. **Difference-in-differences** con el panel `x1_consolidated.csv` (2013-2025, 902 rows) que ya existe. Este dataset es oro y se está ignorando en el análisis principal.
3. **Instrumental Variable** — Usar `oecd_member` o `region` como instrumento de `regulatory_intensity` (válido si la región determina adopción regulatoria por presión de pares, no por capacidad técnica).

**Declaración honesta:** Sin alguno de los 3 fixes, el paper solo puede hablar de **asociación**, no de **efecto**. Esto es **no negociable** para un policy paper.

**Recomendación para Chile:** No permitir que el gobierno cite este estudio como *"la regulación causa X"* sin uno de los 3 fixes. Un paper mal interpretado puede causar una mala ley.

---

### 🔴 PROBLEMA #2 — Tamaño muestral insuficiente para los grupos que más importan

Tabla `SEGUIMIENTO_PAISES_MUESTRA.md`:

| Grupo regulatorio | N en muestra principal |
|---|---|
| binding_regulation | 27 |
| strategy_only | 34 |
| soft_framework | 9 |
| no_framework | **2** |

Con **N=2 en `no_framework`** NO se puede hacer inferencia estadística comparativa. Un ANOVA o regresión con dummies tendrá ese grupo con varianza cero y errores estándar gigantes. Un referee rechazaría el paper en la primera ronda.

**Irónicamente, el contraste que más le interesa a Chile sí es defendible:** `strategy_only` (donde Chile está hoy, N=34) vs `binding_regulation` (a donde iría con la ley, N=27).

**Fixes:**
1. Colapsar a 3 grupos: `{no_framework + soft_framework}` vs `strategy_only` vs `binding_regulation` → (11, 34, 27).
2. Reportar *power analysis* explícito con `statsmodels.stats.power` para cada contraste.
3. Usar *bootstrap* / permutation tests en vez de t-tests paramétricos para grupos pequeños.

---

### 🔴 PROBLEMA #3 — El "EU AI Act block" contamina el análisis

En la codificación IAPP (`VARIABLES_IAPP.md:159`), los 27 miembros de la UE quedan codificados como `comprehensive` con `year_enacted=2024`. Tres problemas:

1. **No son observaciones independientes.** Alemania y Bulgaria "adoptaron" la misma regulación el mismo día. OLS trata esto como 27 puntos de datos cuando en realidad es **1 decisión política replicada 27 veces**.
2. **Rompe la varianza intra-grupo.** `binding_regulation` tiene 27 observaciones pero ~0 de variabilidad regulatoria dentro del bloque EU.
3. **Confunde regulación con "ser miembro UE"**, correlacionada con GDP, GII, readiness. Básicamente mide *"efecto UE"*, no *"efecto de regular IA"*.

**Fixes (usar al menos 2):**
- *Cluster-robust standard errors* agrupados por `eu_bloc` (27 países UE + resto como singletons).
- Efecto fijo EU: agregar dummy `is_eu_member` → absorbe el shock común.
- Análisis dual: modelos con/sin UE, mostrando que los resultados sobreviven sin ella.
- Submuestra "tratamiento temprano": CHN (2021), RUS (2020), PER (2023), KOR/JPN (2025) — países que regularon antes o fuera del bloque EU. Son el verdadero grupo de tratamiento natural.

---

### 🔴 PROBLEMA #4 — Confianza de codificación baja en 16 países

`VARIABLES_IAPP.md:147-150`:
> Confidence high: 36 · medium_needs_review: 32 · medium: 3 · **low: 16**

Los 16 `IAPP_FILL_GAP` con `confidence=low`: **BGD, BHR, BLR, BLZ, BRB, CMR, GHA, JOR, LBN, LKA, MNG, PAK, PAN, PHL, SYC, TWN**.

Esto significa que **~19% de la codificación regulatoria es débil**. Un referee pedirá:
1. *Inter-rater reliability* (Cohen's κ) — ¿un segundo codificador llega a las mismas categorías?
2. Análisis de sensibilidad excluyendo los 16 `low confidence`.
3. Validación externa contra ≥1 tercera fuente (FLI AI Policy Tracker, GPAI).

**Plan:** Ver Sección 6 (Plan detallado Tarea B).

---

### 🔴 PROBLEMA #5 — La Y principal está dominada por un outlier

`ai_investment_usd_bn_cumulative` (Stanford fig_4.3.9):
- USA acumula **~60-70%** del total mundial 2013-2024
- China **~15%**
- Los 82 países restantes se reparten el resto

Si se corre OLS sin transformar, **USA y CHN determinan todos los coeficientes**. El resto del modelo es ruido.

**Fixes obligatorios:**
1. `log(1 + ai_investment)` — verificar que `02_limpieza.ipynb` lo aplique sistemáticamente.
2. Per-capita o per-GDP: `ai_investment / gdp` es más interpretable y reduce el outlier effect.
3. Winsorizing al percentil 95/5 como análisis de sensibilidad.
4. Reportar resultados con y sin USA/CHN. Si los coeficientes cambian de signo, **la historia cambia**.

Lo mismo vale para `ai_startups_cumulative` (USA=6,000+, mediana global=15) y `ai_patents_per100k`.

---

### 🔴 PROBLEMA #6 — Confounders estructurales no controlados

Los controles X2 originales (`gdp_per_capita_ppp`, `internet_penetration`, `gii_score`, `oecd_member`, `region`) estaban bien pero faltaba un confounder crítico: **naturaleza del sistema legal y tradición regulatoria general**.

Un país *common-law* (EE.UU., UK) regula menos cualquier tecnología que un país *civil-law* (Alemania, Chile). Un país con alto `regulatory_quality` del WB regula IA no por IA, sino por **hábito institucional**.

**Estado actualizado 2026-04 (ver Sección 5):** Los 7 confounders prioritarios **ya fueron incorporados** en Tarea A:

| Variable | Fuente | Status |
|---|---|---|
| `regulatory_quality` | WGI | ✅ 85/86 |
| `rule_of_law` | WGI | ✅ 85/86 |
| `has_gdpr_like_law` | DLA Piper 2025 | ✅ 86/86 |
| `gdpr_similarity_level` | DLA Piper + EU adequacy | ✅ 86/86 |
| `fh_total_score` + `fh_democracy_level` | Freedom House FITW 2025 | ✅ 86/86 |
| `legal_origin` + `is_common_law` | La Porta 2008 | ✅ 86/86 |
| `ict_service_exports_pct` + `high_tech_exports_pct` | WDI | ✅ 83/86 |

---

### 🔴 PROBLEMA #7 — Fase NLP subdimensionada

La pregunta Q4 (*"¿qué temas dominan el contenido regulatorio?"*) requiere un corpus robusto. Pero en `GUIA_VARIABLES_ESTUDIO_ETL.md` se definían solo 15-20 documentos legales. Con ese tamaño:
- **LDA no converge** bien (necesita ≥50-100 documentos para tópicos estables)
- **TF-IDF funciona** pero es susceptible al idioma (corpus es multilingüe: español, inglés, chino, coreano, japonés, ruso...)
- **Embeddings + clustering** funcionan mejor con pocos docs, pero **requieren documentos de verdad**, no codificación agregada

**Problema más profundo detectado 2026-04-15:** el proyecto **no tiene ningún documento legal descargado** en `data/raw/` por país. Solo reportes agregados (Stanford, Oxford PDFs). **X1 existe como metadatos (CSV) pero sin corpus textual subyacente.**

**Plan:** Ver Sección 7 (Plan detallado Tarea C).

---

### 🔴 PROBLEMA #8 — Chile no está tratado metodológicamente como "caso focal"

El proyecto se presenta como informante de la ley chilena, pero Chile aparece como **una más de las 72 observaciones** sin tratamiento especial. Para un policy brief gubernamental, esto es **insuficiente**.

**Fix:** incorporar análisis contrafactual específico de Chile:

1. **Synthetic Control Method** — construir un "Chile sintético" combinando países similares (Argentina, Uruguay, Costa Rica, Colombia) para simular qué pasa si Chile adopta `binding_regulation` vs queda en `strategy_only`.
2. **Matching** (propensity score o Mahalanobis) — identificar los 3-5 países más similares a Chile que sí legislaron, medir su trayectoria.
3. **Análisis de escenarios** — usar los coeficientes del modelo principal para predecir ΔY para Chile bajo 3 escenarios regulatorios.

Sin esto, el gobierno chileno solo obtiene *"hay una correlación global"* — no obtiene *"qué pasaría si Chile toma el camino X"*, que es la única pregunta que les importa realmente.

---

## 3. Problemas moderados

### 🟡 #9 — Ventana temporal de controles inconsistente
`DATA_DECISIONS_LOG.md D-003` dice *"2019-2024 más reciente"*. Pero un país tiene `internet_penetration=2019` y otro =2024. En *cross-section*, esto introduce ruido no aleatorio (países pobres tienen datos más antiguos).

**Fix:** forzar año específico (2022 o 2023) con imputación explícita para los 5-10 países faltantes usando regresión lineal de la serie país-específica.

### 🟡 #10 — `regulatory_intensity` como variable ordinal con escala arbitraria
La escala 0-10 es construcción propia (no estándar internacional). Reportar:
- Matriz de ítems y pesos explícita (ya parcial en `VARIABLES_IAPP.md`).
- Sensibilidad al esquema de ponderación.
- Correlación con escalas externas (GPAI, OECD AIM, Stanford FMTI).

### 🟡 #11 — Falta imputación principled
11 países sin `ai_adoption_rate` (estructural en Microsoft). En vez de excluirlos:
- **MICE** (Multiple Imputation by Chained Equations) usando `gii_score + gdp + internet + readiness`
- Esto da **N=83** principal en vez de N=72. Gran aumento de poder estadístico.
- Reportar con y sin imputación es el **estándar oro**.

### 🟡 #12 — No hay preregistro
Para un paper que informa legislación, el estándar post-reproducibility crisis:
- Preregistrar en OSF.io las 4 hipótesis específicas antes de correr el modelo final.
- Separar exploratorio (EDA libre) de confirmatorio (tests con Bonferroni o FDR).
- Sin esto: acusación de *p-hacking* en peer review. 30 min de trabajo, defensa impecable.

### 🟡 #13 — Falta análisis de heterogeneidad
- Regresión por grupos: modelo separado para LATAM, EU, Asia-Pacífico, África.
- Interacciones: `regulatory_intensity × gdp_per_capita` — ¿la regulación afecta diferente a países ricos vs pobres?
- Le da AL GOBIERNO CHILENO una respuesta específica: *"en países del tamaño de Chile, la regulación X se asocia con Y"*.

---

## 4. Fortalezas reconocidas

- **Documentación reproducible:** `DATA_DECISIONS_LOG` con 17 decisiones numeradas es mejor que la mayoría de papers publicados en *Nature Policy*.
- **Trazabilidad raw → interim → master → sample-ready:** arquitectura ETL limpia, auditable por cualquier tercero.
- **Sistema de muestras jerárquicas** (PRINCIPAL / CONFOUNDED / DIGITAL / REGIME / LEGAL_TRADITION / EXTENDED / STRICT) con flags binarios: exactamente lo que pide un revisor de JPART o Policy Sciences.
- Manejo honesto de Taiwan (D-004) y casos excepcionales.
- Reconciliación OECD vs IAPP con 4 status (AGREE / PARTIAL / DIVERGE / FILL_GAP): nivel de auditoría forense.
- Recuperación del gap Oxford 2024 via `pdfplumber`: solución ingeniosa y documentada.

---

## 5. Estado post-Tarea A (abril 2026)

**Tarea A completada** — 7 confounders institucionales incorporados al pipeline ETL. Snapshot actualizado:

| Tier | N | Variables |
|---|---|---|
| PRINCIPAL (4Y + 5X1 + 5X2 core) | **72/86** | baseline |
| CONFOUNDED (+WGI_RQ + WGI_RL + GDPR-like) **[recomendada]** | **72/86** | separa calidad institucional + tradición digital pre-existente |
| DIGITAL (+ICT + high_tech exports) | 69/86 | robustness economía digital |
| REGIME (+FH score + democracy level) | 72/86 | robustness régimen político |
| LEGAL_TRADITION (+legal_origin La Porta) | 72/86 | robustness tradición jurídica |
| EXTENDED (+R&D + tertiary educ) | 62/86 | robustness capacidad absortiva |
| STRICT (+patents + gov_effectiveness) | 47/86 | robustness innovación + institucional |

**Dataset definitivo:** `data/interim/sample_ready_cross_section.csv` (86 × 105 columnas).

**Decisiones formalizadas D-012 a D-017** (ver `info_data/DATA_DECISIONS_LOG.md`):
- D-012: WGI confounders
- D-013: WGI expansion via DataBank db=3
- D-014: GDPR-like manual coding
- D-015: Digital economy proxies
- D-016: Freedom House regime
- D-017: Legal origin La Porta

**Lo que aún bloquea cierre de Fase 1:**
1. Recodificar los 16 `confidence=low` de IAPP → **Tarea B** (Sección 6)
2. Extraer corpus legal textual por país → **Tarea C** (Sección 7)

---

## 6. Plan detallado Tarea B — recodificación low-confidence

### 6.1 Motivación

Los 16 países con `confidence=low` representan **~19% de la muestra principal** y su codificación actual está basada en **una sola fuente secundaria** (notas de prensa, noticias, wiki-entries). Esto genera:

- **Sesgo sistemático en X1.** El coeficiente de `regulatory_intensity` en OLS tiene ruido no aleatorio concentrado en países de renta baja/media.
- **Falta de evidencia textual verificable.** Un referee no puede inspeccionar la fuente.
- **Imposibilidad de análisis de sensibilidad.** No hay métrica de confianza para reportar.

### 6.2 Países objetivo (16)

| ISO3 | País | has_ai_law actual | approach actual | evidencia original |
|---|---|---|---|---|
| BGD | Bangladesh | 0 | strategy_led | nota de prensa |
| BHR | Bahrain | 0 | strategy_led | wiki + prensa |
| BLR | Belarus | 0 | light_touch | wiki |
| BLZ | Belize | 0 | none | sin evidencia positiva |
| BRB | Barbados | 0 | none | sin evidencia positiva |
| CMR | Cameroon | 0 | none | sin evidencia positiva |
| GHA | Ghana | 0 | strategy_led | nota de prensa |
| JOR | Jordan | 0 | strategy_led | comunicado oficial |
| LBN | Lebanon | 0 | none | sin evidencia positiva |
| LKA | Sri Lanka | 0 | light_touch | comunicado oficial |
| MNG | Mongolia | 0 | light_touch | wiki |
| PAK | Pakistan | 0 | strategy_led | comunicado oficial |
| PAN | Panama | 0 | strategy_led | comunicado oficial |
| PHL | Philippines | 0 | strategy_led | comunicado oficial |
| SYC | Seychelles | 0 | none | sin evidencia positiva |
| TWN | Taiwan | 0 | strategy_led | comunicado oficial |

### 6.3 Decisión metodológica clave (2026-04-15)

**Tarea B y Tarea C se fusionan parcialmente.** No tiene sentido "recodificar con alta confianza" sin leer el documento fuente. Por tanto, la ejecución real será:

1. Para cada uno de los 16 países, **localizar y descargar el documento oficial** (ley, estrategia, lineamiento vigente) desde el sitio del gobierno.
2. Si el documento existe → descargar, leer, **recodificar con evidencia textual citada**.
3. Si no se encuentra → `has_ai_law=0` con `confidence=high`, justificación: "búsqueda exhaustiva sin resultados".
4. Guardar documento + metadata en `data/raw/legal_corpus/{ISO3}/` (ver esquema Sección 7.4).

Esto convierte Tarea B en **el piloto de Tarea C**: deja el terreno preparado para hacer la extracción completa con los ~70 países restantes.

### 6.4 Rúbrica de codificación formal

Para cada variable, criterio explícito:

#### `has_ai_law` (0/1)
- **1** ↔ existe instrumento legal vinculante específico para IA (ley, decreto con fuerza de ley, reglamento con sanciones). **NO** cuenta: estrategia nacional, lineamientos voluntarios, marco ético no-vinculante.
- **0** ↔ no existe instrumento vinculante al 2025-Q4.
- Regulación sectorial (solo fintech, solo salud) → `has_ai_law=0`, se captura en `regulatory_approach=light_touch`.
- Regulación de datos personales que menciona IA → `has_ai_law=0` (ya capturado por `gdpr_similarity_level`).

#### `regulatory_approach` (categorical)
- `none` — no hay ley, estrategia ni lineamientos formales.
- `light_touch` — solo lineamientos no-vinculantes o regulación sectorial parcial.
- `strategy_led` — estrategia nacional formal publicada por gobierno, sin ley vinculante.
- `regulation_focused` — ley vinculante parcial (solo ciertos sectores o ciertas obligaciones).
- `comprehensive` — ley horizontal comprehensiva (EU AI Act, Colorado AI Act, CAC regulations).

#### `regulatory_intensity` (0-10)
Suma ponderada de:
- Existencia de ley (0-3): 0=no, 1=draft, 2=sectorial, 3=horizontal
- Obligaciones concretas (0-3): 0=ninguna, 1=transparencia, 2=+evaluación, 3=+restricciones
- Sanciones (0-2): 0=sin sanciones, 1=administrativas, 2=penales/multas materiales
- Autoridad competente (0-2): 0=sin autoridad, 1=órgano existente adaptado, 2=autoridad ad-hoc

#### `enforcement_level` (ordinal: none/low/medium/high)
- `none` — sin autoridad competente
- `low` — autoridad existe pero sin sanciones registradas públicamente
- `medium` — ≥1 caso de enforcement público
- `high` — múltiples casos + multas materiales

#### `thematic_coverage` (0-15)
Conteo de tópicos cubiertos por el instrumento: {transparency, bias/discrimination, privacy, safety, accountability, human_oversight, risk_assessment, sectoral_carveouts, high_risk_systems, foundation_models, copyright_AI, deepfakes, labor_AI, public_procurement, sandboxes}.

### 6.5 Jerarquía de fuentes (niveles 1-7)

| Nivel | Fuente | Ejemplos |
|---|---|---|
| 1 (máxima) | Sitio oficial del gobierno | `.gov.xx`, `.gouv.xx`, portal parlamentario, diario oficial |
| 2 | OECD AI Policy Observatory | `oecd.ai/countries` |
| 3 | Global Partnership on AI (GPAI) | `gpai.ai` country reports |
| 4 | FLI AI Policy Tracker | `futureoflife.org/ai-policy` |
| 5 | UNESCO AI Ethics Observatory | `unesco.org/ethics-ai` |
| 6 | Stanford HAI country profiles | `aiindex.stanford.edu` |
| 7 | Prensa especializada | MIT Tech Review, Reuters, Bloomberg |

**Regla de confianza:**
- `high` → ≥2 fuentes de nivel 1-3 concuerdan + documento primario guardado
- `medium` → 1 fuente nivel 1-3 + 1 nivel 4-6 concuerdan
- `low` → solo nivel 4-7 o fuentes que se contradicen

### 6.6 Output esperado

Archivo `data/raw/IAPP/manual_coding/recoding_v2.csv` con columnas:

| Columna | Tipo | Descripción |
|---|---|---|
| iso3 | string | — |
| has_ai_law_v2 | 0/1 | codificación re-verificada |
| regulatory_approach_v2 | categorical | — |
| regulatory_intensity_v2 | 0-10 | — |
| enforcement_level_v2 | ordinal | — |
| thematic_coverage_v2 | 0-15 | — |
| year_enacted_v2 | int | año del instrumento principal (NULL si has_ai_law_v2=0) |
| confidence_v2 | high/medium/low | según regla Sección 6.5 |
| source_primary_url | string | URL documento primario |
| source_primary_title | string | — |
| source_primary_type | L/S/G/D/none | Ley, Strategy, Guideline, Draft, none |
| source_secondary_urls | list[string] | URLs adicionales de validación |
| evidence_quote | text | cita textual (≤200 chars) |
| recoding_date | date | — |
| recoding_changed | bool | flag si cambia vs IAPP original |
| change_justification | text | si `recoding_changed=true` |

### 6.7 Flujo de trabajo (human-in-the-loop)

1. **Sistema (Claude):** preparar rúbrica formal → `info_data/METODOLOGIA_RECODIFICACION_IAPP.md`
2. **Humano:** aprobar rúbrica + criterios de borde de Sección 6.4
3. **Sistema:** para cada país, ejecutar búsqueda sistemática vía WebFetch/WebSearch en la jerarquía de fuentes. Descargar documento primario si existe. Rellenar fila en `recoding_v2.csv`.
4. **Sistema:** generar tabla de propuestas de cambio (países donde `recoding_changed=true`).
5. **Humano:** revisar caso por caso. Para cada propuesta de cambio:
   - Aceptar (la nueva evidencia es superior)
   - Rechazar (la original era correcta, rechazar nueva evidencia)
   - Pedir más evidencia (sistema hace búsqueda adicional)
6. **Sistema:** aplicar cambios aprobados, actualizar `x1_master.csv`, regenerar `sample_ready_cross_section.csv`, documentar en `D-018`.
7. **Sistema:** análisis de sensibilidad: correr modelo principal con y sin los 16 países, reportar estabilidad de coeficientes.

**Tiempo estimado:**
- Sistema: 4-6h (búsqueda + descarga + codificación)
- Humano: 40-60 min (revisión de propuestas)

---

## 7. Plan detallado Tarea C — extracción corpus legal

### 7.1 Motivación y alcance

**Objetivo:** construir un corpus legal textual **por país** que permita:
1. Análisis NLP (LDA / embeddings / TF-IDF) de contenido regulatorio (pregunta Q4)
2. Validación textual de la codificación X1 (backing para Tarea B)
3. Comparación temática cross-país
4. Publicación reproducible (otros investigadores pueden verificar el texto que codificamos)

**Restricción explícita del usuario:** *incluir solo leyes y estrategias vigentes*. Excluir borradores no aprobados, documentos obsoletos, versiones derogadas.

### 7.2 Universo del corpus

Para los 86 países + 1 bloque EU:

| Tipo | Código | Ejemplo | Criterio |
|---|---|---|---|
| Ley vinculante | L | EU AI Act, Colorado AI Act, CAC Generative AI Regulation | Vigente al 2025-Q4 |
| Estrategia nacional | S | Chile "Política Nacional de IA" 2021 | Oficialmente publicada por gobierno |
| Reglamento derivado | R | EU AI Act Implementing Regulations | Vigente |
| Lineamiento formal | G | NIST AI RMF 1.0 (EE.UU.) | Emitido por autoridad pública |
| **Excluidos** | — | drafts, borradores, propuestas, whitepapers académicos | — |

**Meta cuantitativa:** 80-150 documentos totales. Un país puede tener 0 (ej: no_framework), 1 (ley o estrategia), o múltiples (EU = 1 AI Act + 27 estrategias nacionales).

### 7.3 Jerarquía de capas (3-layer source hierarchy)

**Capa 1 — Índice** (descubrir qué documentos existen):
- OECD.AI Policy Observatory — lista oficial de instrumentos por país
- IAPP Global AI Law & Policy Tracker (PDF Feb 2026)
- GPAI country reports

**Capa 2 — Verificación** (confirmar que el documento existe y está vigente):
- EUR-Lex (para EU AI Act y derivados)
- Bases de datos legales nacionales (Biblioteca del Congreso Chile, LexisNexis, national gazettes)
- Archivos parlamentarios

**Capa 3 — Descarga** (obtener el documento primario):
- **Sitio oficial del gobierno** (requisito hard — sin excepciones)
- Formato preferido: PDF oficial > HTML gubernamental > texto en gazette oficial

**Principio rector:** *trust but verify*. Capa 1 dice "Bangladesh tiene estrategia X". Capa 2 confirma vigencia. Capa 3 baja el PDF desde el sitio del Ministerio de Ciencia de Bangladesh (no desde un aggregator).

### 7.4 Estructura de almacenamiento

```
data/raw/legal_corpus/
├── manifest.csv                    # índice maestro de todos los documentos
├── EU/
│   ├── EU_L_001_ai_act_2024.pdf
│   ├── EU_L_001_ai_act_2024.meta.json
│   └── EU_L_001_ai_act_2024.txt    # texto extraído (OCR si necesario)
├── CHL/
│   ├── CHL_S_001_politica_nacional_ia_2021.pdf
│   ├── CHL_S_001_politica_nacional_ia_2021.meta.json
│   └── CHL_S_001_politica_nacional_ia_2021.txt
├── USA/
│   ├── USA_G_001_nist_ai_rmf_2023.pdf
│   ├── USA_L_001_colorado_ai_act_2024.pdf
│   └── ...
├── CHN/
│   ├── CHN_L_001_cac_gen_ai_2023.pdf
│   ├── CHN_L_002_cac_algorithmic_recs_2022.pdf
│   └── CHN_L_003_cac_deep_synthesis_2023.pdf
└── ...
```

**Esquema `manifest.csv`:**

| Columna | Tipo | Descripción |
|---|---|---|
| doc_id | string | `{ISO3}_{TYPE}_{NNN}` ej: `CHL_S_001` |
| iso3 | string | país o `EU` |
| jurisdiction_name | string | — |
| doc_type | L/S/R/G | ley / estrategia / reglamento / lineamiento |
| doc_title_original | string | título oficial en idioma original |
| doc_title_english | string | título traducido |
| year_enacted | int | año de promulgación |
| year_last_amended | int | última modificación vigente |
| still_in_force | bool | validado por humano |
| language_original | string | ISO 639-1 |
| source_url_official | string | URL sitio gobierno |
| source_url_mirror | string | URL secundaria (EUR-Lex, OECD.AI) |
| download_date | date | — |
| file_format | string | pdf/html/docx/txt |
| file_size_bytes | int | — |
| file_sha256 | string | hash para deduplicación |
| pages | int | — |
| word_count_original | int | — |
| word_count_english | int | — |
| extraction_method | string | pdfplumber / OCR / html_parser |
| human_verified | bool | flag human-in-the-loop |
| human_verifier_date | date | — |
| human_verifier_notes | text | — |
| corpus_tier | core/extended | core = usa para análisis principal |

**Esquema `{doc_id}.meta.json`:** copia estructurada de la fila manifest + resumen + TOC extraído.

### 7.5 Pipeline de extracción

Tres scripts nuevos en `src/`:

#### `src/fetch_ai_corpus.py` (descarga)
- Input: registro por país con URLs candidatas
- Acciones: descarga respetando `robots.txt`, calcula SHA-256, guarda raw + metadata preliminar
- Output: archivos en `data/raw/legal_corpus/{ISO3}/`
- **Human-in-the-loop:** antes de descargar, presenta al humano la lista de URLs candidatas y pide confirmación (checkbox UI simple) → evita descargar drafts, versiones obsoletas, documentos erróneos

#### `src/parse_ai_corpus.py` (extracción de texto)
- Input: archivos raw en `data/raw/legal_corpus/`
- Acciones: `pdfplumber` para PDFs, `BeautifulSoup` para HTML, OCR con Tesseract para PDFs escaneados
- Output: archivo `.txt` paralelo por cada documento
- Validación: word count > umbral mínimo (descarta extracciones fallidas)

#### `src/translate_ai_corpus.py` (traducción unificada)
- Input: `.txt` en idioma original
- Acciones: traducción a inglés vía **DeepL API** (costo estimado ~$70 one-time para corpus completo)
- Output: `.en.txt` paralelo
- Cache por SHA-256 para no traducir el mismo documento dos veces

### 7.6 Quality Gates (8 verificaciones)

| Gate | Verificación | Umbral |
|---|---|---|
| G1 | SHA-256 único por documento | 100% |
| G2 | `source_url_official` apunta a dominio gubernamental autoritativo | 100% |
| G3 | `still_in_force=true` verificado manualmente por humano | 100% |
| G4 | `word_count_original` ≥ 500 palabras (filtra PDFs vacíos o scans fallidos) | ≥95% |
| G5 | `language_original` detectado vía `langdetect` coincide con país esperado | ≥95% |
| G6 | Traducción al inglés no corrupta (word_count_english > 0.5× word_count_original) | ≥95% |
| G7 | Cobertura: cada país con `has_ai_law=1` OR `regulatory_approach=strategy_led` tiene ≥1 documento | 100% |
| G8 | `human_verified=true` en todos los documentos del corpus core | 100% |

### 7.7 Casos especiales

**EU (27 países + EUU):**
- 1 entrada `EU_L_001_ai_act_2024` (nivel bloque)
- 27 entradas `{ISO3}_S_001_national_strategy` (estrategias nacionales individuales)
- En el análisis: los 27 países comparten `has_ai_law=1` vía EU AI Act, pero su estrategia nacional es independiente

**USA:**
- 1 entrada `USA_G_001_nist_ai_rmf_2023` (federal, no vinculante)
- 1 entrada `USA_L_001_colorado_ai_act_2024` (estadual vinculante)
- 1 entrada `USA_S_001_national_ai_rd_plan_2023`
- `has_ai_law=0` a nivel federal, pero se documenta la fragmentación

**China:**
- 3 entradas separadas por CAC (Cyberspace Administration of China):
  - `CHN_L_001_cac_generative_ai_2023`
  - `CHN_L_002_cac_algorithmic_recommendations_2022`
  - `CHN_L_003_cac_deep_synthesis_2023`
- Tratadas como 3 instrumentos → `has_ai_law=1`, `regulatory_approach=comprehensive`

**Países sin documento:**
- No hay fila en manifest
- `has_ai_law=0` con `confidence=high` justificado por "búsqueda exhaustiva sin resultados en Capa 1 y 3"

### 7.8 Human-in-the-loop explícito

Este punto es **no negociable** por decisión del usuario: *"esta extracción no sería 100% automática, tiene que haber intervención humana para evitar descargar archivos incorrectos, antiguos o que ya no están en vigencia"*.

**Puntos de intervención humana obligatoria:**

| Paso | Acción del humano | Tiempo estimado |
|---|---|---|
| **Antes de descarga** | Revisar lista de URLs candidatas por país y confirmar/rechazar cada una | 30-60 min por país × 86 = 40-80h (puede distribuirse) |
| **Post-descarga** | Abrir el documento y verificar: (a) está vigente, (b) es el documento que el sistema cree que es, (c) no es un borrador | 10-15 min por documento × ~100 = 15-25h |
| **Post-traducción** | Spot-check de 10-15% de traducciones (~10-15 documentos) | 3-5h |
| **Pre-análisis NLP** | Validar que el corpus final cumple los 8 Quality Gates | 2-3h |
| **Total humano** | | **60-110h** (fase distribuida en 4-6 semanas) |

**Por qué la intervención humana es crítica:**
- **Vigencia:** un LLM puede bajar un borrador 2022 creyéndolo ley 2024. Solo un humano verifica la fecha de entrada en vigor contra el diario oficial.
- **Autenticidad:** sitios espejo pueden publicar versiones con texto alterado. Solo el humano valida que el PDF es el oficial.
- **Contexto político:** Chile 2021 tiene "Política Nacional de IA" pero también un proyecto de ley 2024 (16821-19). Solo el humano decide qué cuenta como "instrumento vigente" para el corpus.
- **Traducciones sensibles:** términos legales en chino/ruso/árabe pueden tener múltiples traducciones. Humano spot-check en los casos ambiguos.

### 7.9 Análisis NLP posterior (fase posterior al corpus)

Una vez corpus cerrado y validado:

1. **Preprocessing:** tokenización, lematización, stopwords legales (en inglés post-traducción)
2. **TF-IDF** para términos distintivos por país y por grupo regulatorio
3. **Embeddings** multilingües vía Sentence-BERT `paraphrase-multilingual-mpnet-base-v2` (alternativa: `Legal-BERT`, `E5-multilingual`)
4. **Clustering temático** (K-Means sobre embeddings) → valida taxonomía de `thematic_coverage`
5. **LDA** (Latent Dirichlet Allocation) — solo si N ≥ 80 (necesita tamaño mínimo para convergencia)
6. **Validación humana de tópicos:** top 20 términos por tópico → experto legal los nombra

### 7.10 Timeline Tarea C

| Semana | Actividad | Sistema | Humano |
|---|---|---|---|
| 1 | Construir `manifest.csv` preliminar con URLs candidatas por país (Capa 1) | 6h | 0h |
| 2 | Revisión humana de URLs candidatas | 0h | 15-20h |
| 3 | Descarga masiva post-aprobación | 4h | 5h (spot-checks) |
| 4 | Extracción de texto + traducción DeepL | 3h | 10h (verificación) |
| 5 | Quality Gates + validación humana final | 2h | 5h |
| 6 | Análisis NLP preliminar + validación tópicos | 8h | 5h |
| **Total** | | **~23h** | **~40-50h** |

---

## 8. Human-in-the-loop

Esta sección consolida **qué tiene que hacer el usuario** vs **qué hace el sistema** a lo largo de B y C.

### 8.1 Roles

**Sistema (Claude):**
- Buscar fuentes vía WebFetch/WebSearch
- Descargar documentos (con confirmación previa)
- Extraer texto (pdfplumber / OCR / HTML parsing)
- Traducir (DeepL API)
- Codificar variables X1 siguiendo rúbrica
- Calcular SHA-256, metadata técnica, Quality Gates
- Generar tabla de propuestas de cambio
- Correr análisis de sensibilidad
- Ejecutar NLP final

**Humano (investigador):**
- Aprobar rúbrica y criterios de borde antes de empezar
- Revisar URLs candidatas por país (confirmar cuáles son oficiales vs descartar)
- Verificar vigencia de cada documento descargado (fecha entrada en vigor, versión actual, no es borrador)
- Decidir casos ambiguos (Chile: estrategia 2021 + proyecto ley 2024 → ¿qué entra al corpus?)
- Spot-check traducciones
- Validar los 8 Quality Gates finales
- Nombrar tópicos LDA/embedding post-análisis
- Aprobar/rechazar propuestas de cambio de codificación

### 8.2 Qué NO debe subir el usuario al repo

**Nada físicamente.** El sistema tiene capacidad para:
- Buscar fuentes en internet (WebSearch)
- Descargar documentos (WebFetch)
- Leer PDFs (pdfplumber / OCR)
- Traducir (llamando DeepL API)

El usuario **no necesita descargar manualmente** ni un solo PDF. Su rol es de **validador y decisor**, no de recolector.

### 8.3 Qué SÍ tiene que proveer el usuario

| Input | Quién lo da | Cuándo |
|---|---|---|
| Key DeepL API | Usuario (~$70 one-time) | Antes de Tarea C Semana 4 |
| Aprobación de rúbrica B | Usuario | Antes de Tarea B ejecución |
| Aprobación de jerarquía de fuentes | Usuario | Antes de Tarea B ejecución |
| Confirmación de URLs candidatas | Usuario | Tarea C Semana 2 (iterativo por país) |
| Verificación de vigencia | Usuario | Tarea C Semana 3 (iterativo por documento) |
| Revisión de propuestas de cambio | Usuario | Tarea B cierre |
| Nombres de tópicos NLP | Usuario | Tarea C Semana 6 |

### 8.4 Interfaz de revisión humana propuesta

Para hacer el trabajo del humano **tractable**, el sistema generará archivos de decisión con checkbox en formato `.md` o CSV:

```markdown
# Revisión URLs candidatas — BGD (Bangladesh)

## Candidata 1
- URL: https://ict.gov.bd/policies/national-ai-strategy-2024
- Título: Bangladesh National AI Strategy (2024-2030)
- Nivel fuente: 1 (sitio oficial Ministry of ICT)
- Fecha documento: 2024-07-15
- Decisión: [ ] Aprobar · [ ] Rechazar · [ ] Más evidencia
- Notas: ___________

## Candidata 2
- URL: https://oecd.ai/en/dashboards/countries/Bangladesh
- Título: OECD AI country profile — Bangladesh
- Nivel fuente: 2
- Fecha documento: 2025-01
- Decisión: [x] Aprobar (como validación secundaria) · [ ] Rechazar
- Notas: Confirma que estrategia nacional existe y está vigente
```

El usuario revisa, marca, y el sistema procesa en batch.

---

## 9. Roadmap priorizado

### Fase 1 (recolección) — restante

**Semana en curso (2026-04-15 — 2026-04-22):**
- ✅ Tarea A (7 confounders) — **COMPLETADA**
- ⏳ Tarea B (recodificar 16 low-confidence) + descarga inicial para esos 16 países
- ⏳ Tarea C Semana 1: construir manifest preliminar

**Semanas 2-3 (2026-04-22 — 2026-05-06):**
- ⏳ Tarea C Semanas 2-3: revisión humana + descarga masiva

**Semana 4 (2026-05-06 — 2026-05-13):**
- ⏳ Tarea C Semana 4: extracción texto + traducción

**Semana 5 (2026-05-13 — 2026-05-20):**
- ⏳ Tarea C Semanas 5-6: QG + NLP preliminar

### Fase 2 (limpieza) — post-Fase 1

- Aplicar `log(1 + ai_investment)` sistemáticamente (#5)
- Normalización per-capita / per-GDP (#5)
- Winsorizing p95/p5 (#5)
- Forzar ventana temporal 2022-2023 con imputación explícita (#9)
- Imputación MICE para 11 países sin `ai_adoption_rate` (#11)
- Análisis de sensibilidad al esquema de ponderación (#10)

### Fase 3 (EDA confirmatorio)

- Preregistro OSF con 4 hipótesis específicas (#12)
- Separación exploratorio vs confirmatorio

### Fase 4 (modelamiento)

- OLS con lags temporales (#1, fix principal endogeneidad)
- Difference-in-differences con `x1_consolidated.csv` panel (#1)
- Instrumental Variables (#1)
- Cluster-robust SE por `eu_bloc` (#3)
- Dummy `is_eu_member` (#3)
- Análisis con/sin UE, con/sin USA+CHN (#3, #5)
- Power analysis por contraste (#2)
- Synthetic Control Method para Chile (#8)
- Matching / Mahalanobis para Chile (#8)
- Análisis de heterogeneidad regional e interacciones (#13)

### Fase 5 (entregable)

- Paper para Research Policy / Policy Sciences / Regulation & Governance
- Policy brief específico para Chile (5-10 páginas, no técnico)

---

## 10. Clasificación problemas × fase

| # | Problema | Severidad | Fase resolución | ¿Requiere más recolección? | Estado |
|---|---|---|---|---|---|
| #1 | Endogeneidad | 🔴 | Fase 4 | ❌ usa `x1_consolidated.csv` panel existente | Pendiente |
| #2 | N por grupo | 🔴 | Fase 4 + reclasificar | 🟡 parcial | Pendiente |
| #3 | Bloque EU | 🔴 | Fase 4 | ❌ | Pendiente |
| #4 | confidence=low | 🔴 | **Fase 1** | ✅ Tarea B | **En curso** |
| #5 | Outliers USA/CHN | 🔴 | Fase 2 | ❌ | Pendiente |
| #6 | Confounders faltantes | 🔴 | **Fase 1** | ✅ Tarea A | **✅ COMPLETADA** |
| #7 | Corpus NLP | 🔴 | **Fase 1** | ✅ Tarea C | **Planificada** |
| #8 | Chile caso focal | 🔴 | Fase 4 | ❌ | Pendiente |
| #9 | Ventana temporal | 🟡 | Fase 2 | ❌ | Pendiente |
| #10 | Escala `regulatory_intensity` | 🟡 | Fase 2 + 4 | ❌ | Pendiente |
| #11 | Imputación MICE | 🟡 | Fase 2 | ❌ | Pendiente |
| #12 | Preregistro | 🟡 | Fase 3 | ❌ | Pendiente |
| #13 | Heterogeneidad | 🟡 | Fase 4 | ❌ | Pendiente |

**Conclusión:** Solo 3 de los 13 problemas son realmente de Fase 1 — #4 (en curso), #6 (completado), #7 (planificado). Los demás se abordan en fases posteriores.

---

## 11. Opinión franca

Este proyecto va en buen camino pero **NO está listo**. La infraestructura de datos es de élite, pero la arquitectura de inferencia causal es débil. Un *cross-section* con N=72 contaminado por el bloque UE no puede responder *"¿Chile debe regular?"* con rigor científico.

**Si se publica el paper como está hoy:**
- Probable rechazo en revistas Q1 (Research Policy, Policy Sciences).
- El gobierno chileno podría usarlo mal, exagerando asociaciones como si fueran efectos causales.

**Si se implementan los 8 problemas críticos:**
- El paper puede ser publicable en Research Policy, Policy Sciences o Regulation & Governance.
- El proyecto puede fundamentar la ley 16821-19 con solidez científica defensible.

**Prioridades inmediatas (próximas 4 semanas):**
1. **Endogeneidad (#1)** — fix no requiere recolección adicional, sí requiere diseño de modelo. Crítico para Fase 4.
2. **Corpus legal (#7, #4 fusionados)** — única brecha real de Fase 1 que queda abierta. Sin corpus, el paper es "descriptivo con evidencia agregada"; con corpus es "estudio reproducible con evidencia primaria".
3. **Chile como caso focal (#8)** — diferencia entre "paper académico sobre 86 países" y "paper que informa una ley específica". Es la única razón por la que este proyecto tiene riesgo político alto.

**Si algo tuviera que priorizarse por encima del resto:** cerrar Tarea B+C (corpus legal con validación humana). Es lo único que:
- Todavía es parte de Fase 1 (no se puede posponer)
- No puede ejecutarse sin el usuario (human-in-the-loop obligatorio)
- Da evidencia primaria verificable por cualquier tercero

Todo lo demás (modelamiento, Synthetic Control, preregistro) puede esperar hasta tener corpus cerrado.

---

## Historial del informe

| Fecha | Acción |
|---|---|
| 2026-04-14 | Auditoría científica original (13 problemas identificados) |
| 2026-04-15 | Tarea A cerrada (problema #6 resuelto: 7 confounders incorporados) |
| 2026-04-15 | Plan B+C consolidado con human-in-the-loop explícito (este informe) |
