# Plan de Consolidación — Corpus Legal-IA por País (v2)

> **Versión 2 — actualizada al 2026-04-28** tras avance del corpus a 38/86 países y generación de `x1_master_v2.csv`. Incorpora datos del pipeline completo, alinea con la skill `corpus-legal-ia` y el nuevo notebook ADE v2.

## Objetivo

Consolidar toda la información recopilada de los **86 países de la muestra** en una estructura única, lista para ingestión en el sistema RAG (`legal-rag`) y usable como entrada del ADE y del modelamiento.

---

## 1. Estado actual del corpus (2026-04-28)

| Categoría | Cuenta |
|---|---|
| Total muestra del estudio | **86** |
| **Procesados (DONE)** en muestra | **38** ⬆ (era 23 en v1) |
| Procesados fuera de muestra (referencia) | 1 (QAT) |
| Pendientes en muestra | 48 |
| Países con bloqueos documentados | 5 (CMR, KAZ, LBN, BHR, ARM) |

### 1.1 Países con corpus completo (38 + 1 QAT externo + 1 KAZ pendiente firma)

`AUS, AUT, ARE, ARM, BEL, BGD, BGR, BHR, BLR, CAN, CHE, CMR, CRI, CZE, DEU, DNK, ESP, FIN, FRA, GBR, GHA, HUN, IND, IRL, ISR, ITA, JOR, JPN, KAZ, KOR, LBN, MNG, NLD, NOR, NZL, POL, SGP, SWE, TWN, USA` + `QAT` (referencia externa).

### 1.2 Países pendientes (48)

P2-IAPP-LOW pendientes (16): `ECU, ISL, LKA, MAR, MEX, MYS, PAK, PAN, PHL, RUS, SRB, SYC, THA, TUN, UGA, UKR, URY`.

P3-SAMPLE pendientes (29): `ARG, BRA, CHN, COL, CYP, EGY, EST, GRC, HRV, IDN, KEN, LTU, LUX, LVA, MLT, MUS, NGA, PER, PRT, ROU, SAU, SVK, SVN, TUR, VNM, ZAF`.

FOCAL (1): `CHL` — **PENDING**, se procesará después del Top 30.

---

## 2. Estructura de información por país

### 2.1 Fuentes de datos (3 capas)

| Fuente | Ubicación | Contenido | Países |
|--------|-----------|-----------|--------|
| **embedded_rag** | `ADE/embedded_rag/{ISO3}/` | Perfil + chunks ricos para RAG | 75 países |
| **legal_corpus** | `data/raw/legal_corpus/{ISO3}/` | PDFs originales + 4 entregables (skill output) | **38** países (era 23) |
| **info_data** | `info_data/` | Metodologías y diccionarios de variables | Global |

### 2.2 Archivos por país en `embedded_rag/`

```
{ISO3}/
├── country_profile.json          # población, GDP, AI readiness
├── regulatory_framework.json     # grupo regulatorio, enfoque, intensidad
├── documents_index.json          # lista de documentos legales
├── embedding_chunks.json         # chunks básicos
├── embedding_chunks_rich.json    # chunks ricos (8-11 por país)
├── full_corpus_text.json         # texto completo
├── legal_corpus.json             # resumen
├── legal_corpus_full.json        # SOURCES + CANDIDATES + FINDINGS
├── meta_chunks.md                # análisis diferencial
└── documentos.json               # metadata
```

### 2.3 Archivos por país en `legal_corpus/` (38 países)

Generados por la skill `corpus-legal-ia` siguiendo R1-R5:

```
{ISO3}/
├── manifest.csv                  # trazabilidad PDFs (URL, SHA-256, páginas)
├── SOURCES.md                    # citas APA 7 + provenance
├── CANDIDATES.md                 # inventario + recodificación X1 propuesta
├── FINDINGS.md                   # hallazgo diferencial completo
└── *.pdf                         # documentos legales descargados
```

---

## 3. Datos consolidados producidos (NUEVO v2)

Los siguientes archivos son **outputs del pipeline ETL** alimentados por el corpus:

| Archivo | Filas | Columnas | Descripción |
|---|---|---|---|
| `data/interim/sample_ready_cross_section.csv` | 86 | 105 | Dataset principal (Y, X1 IAPP, X2) |
| `data/interim/x1_master.csv` | 86 | 11 | X1 IAPP base |
| **`data/interim/x1_master_v2.csv`** ⬆ NUEVO | **41** | **23** | **X1 IAPP + propuestas skill (38 muestra + 3 ext)** |
| `data/interim/x2_*_master.csv` | 86 | varios | Componentes de X2 (legal_origin, GDPR, FH, WB, WIPO) |
| `data/interim/y_*_master.csv` | 86 | varios | Componentes de Y (Stanford, Microsoft, Oxford) |
| `data/interim/proxy_infra_pilots.csv` | 6 | 35 | **Sub-estudio**: proxies infraestructura 6 pilotos |
| `data/interim/proxy_infra_universal.csv` | 35 | 7 | **Sub-estudio**: water stress, B-READY, electricity universales |

### 3.1 Variables nuevas en `x1_master_v2.csv`

| Variable | Origen | Cobertura |
|---|---|---|
| `has_ai_law_proposed` | Diff summary CANDIDATES.md §6 | 38 |
| `regulatory_intensity_proposed` | Diff summary CANDIDATES.md §6 | 20 |
| `thematic_coverage_proposed` | Diff summary CANDIDATES.md §6 | 20 |
| `regulatory_regime_group_proposed` | CANDIDATES.md §Status propuesto | 32 |
| `enforcement_level_proposed` | Diff summary | 19 |
| `regulatory_approach_proposed` | Diff summary | varias |
| `confidence_iapp` / `confidence_proposed` | CANDIDATES.md §Confidence | 25 |
| **`has_dedicated_ai_authority`** | Heurística sobre texto FINDINGS | 41 |
| **`ai_law_pathway_declared`** | Heurística sobre bills/drafts | 41 |
| `ai_corpus_n_documents` | Conteo PDFs en carpeta | 41 |
| `ai_corpus_total_pages` | Suma `pages` en manifest.csv | 38 |
| `ai_corpus_first_doc_year` / `ai_corpus_last_doc_year` / `ai_corpus_years_span` | Manifest publication_date | 38 |

---

## 4. Estructura propuesta para consolidación final (`corpus_consolidated/`)

### 4.1 Carpeta destino

```
ADE/corpus_consolidated/{ISO3}/
```

### 4.2 Archivos por país

```
{ISO3}/
├── 01_profile.json              # country_profile.json original
├── 02_regulatory.json           # regulatory_framework.json original
├── 03_documents_index.json      # lista de documentos legales
├── 04_meta_analysis.md          # meta_chunks.md
├── 05_sources.md                # SOURCES.md (skill output)
├── 06_candidates.md             # CANDIDATES.md (skill output)
├── 07_findings.md               # FINDINGS.md (skill output)
├── 08_full_analysis.json        # legal_corpus_full.json
└── embedding_chunks.json        # embedding_chunks_rich.json
```

### 4.3 Archivo maestro de países

`ADE/corpus_consolidated/master_index.json` con:

- `iso3`, `country_name`, `region`
- `regulatory_group_iapp`, `regulatory_regime_group_proposed`
- `has_corpus` (true/false)
- `n_documents`, `n_pages`, `years_span`
- `has_dedicated_ai_authority`, `ai_law_pathway_declared`
- `metrics`: AI readiness, adoption rate, investment, startups
- `priority_tier`: P1-TOP30 / P2-IAPP-LOW / P3-SAMPLE / FOCAL

---

## 5. Variables disponibles del pipeline ETL

### 5.1 Variables Y (Resultado — Ecosistema IA)

| Variable | Fuente | Cobertura (de 86) |
|---|---|---|
| `ai_readiness_score` | Oxford Insights | 86/86 (100%) |
| `ai_adoption_rate` | Microsoft AI Diffusion | 86/86 |
| `ai_investment_usd_bn_cumulative` | Microsoft / Stanford | 86/86 |
| `ai_startups_cumulative` | Microsoft | 86/86 |
| `ai_patents_per100k` | OECD / Stanford | 49/72 (en muestra principal) |
| `ai_publications_frac` | UNESCO / Scopus | 70/72 |

### 5.2 Variables X1 (Tratamiento — Regulación IA)

#### IAPP base
- `has_ai_law`, `regulatory_approach`, `regulatory_intensity`, `enforcement_level`, `thematic_coverage`, `regulatory_status_group`

#### Propuestas skill `corpus-legal-ia` (NUEVO v2 — 38 países)
- `regulatory_intensity_proposed`, `thematic_coverage_proposed`, `regulatory_regime_group_proposed`, `enforcement_level_proposed`, `has_ai_law_proposed`

#### Variables nuevas derivadas del corpus (NUEVO v2)
- `has_dedicated_ai_authority` (0/1)
- `ai_law_pathway_declared` (0/1)
- `ai_corpus_n_documents`, `ai_corpus_total_pages`, `ai_corpus_years_span`

### 5.3 Variables X2 (Controles)

- `gdp_per_capita_ppp`, `internet_penetration`, `gii_score`, `rd_expenditure`, `tertiary_education`
- `regulatory_quality`, `rule_of_law` (World Bank WGI)
- `has_gdpr_like_law`, `gdpr_similarity_level`
- `fh_total_score`, `legal_origin`, `is_common_law`

---

## 6. Proceso de consolidación a `legal-rag`

### Paso 1 — Consolidar estructura unificada

Script Python que:

1. Lee cada país de `embedded_rag/`.
2. Si existe en `legal_corpus/`, agrega SOURCES, CANDIDATES, FINDINGS.
3. Si está en `x1_master_v2.csv`, anexa propuestas + flags nuevas (autoridad / pathway).
4. Crea estructura unificada en `corpus_consolidated/`.

### Paso 2 — Copiar a legal-rag

```bash
cp -r ADE/corpus_consolidated /home/pablo/legal-rag/data/ai_regulation_v2/
```

### Paso 3 — Script de ingestión optimizado

- 1 documento por país con metadata rico (incluye `has_dedicated_ai_authority`, `regulatory_regime_group_proposed`).
- Múltiples chunks (meta-chunking):
  - Chunk 1: Perfil + ecosistema (resumen)
  - Chunk 2: Marco regulatorio (detalle, IAPP + propuesta)
  - Chunk 3: Documentos legales (lista del manifest)
  - Chunk 4: SOURCES completo
  - Chunk 5: CANDIDATES completo
  - Chunk 6: FINDINGS completo
- Embeddings con Ollama (modelo a definir según `legal-rag/`).

### Paso 4 — Verificación post-ingestión

```sql
-- Contar documentos por país
SELECT metadata->>'country_name', COUNT(*)
FROM documents WHERE source LIKE 'ai-regulation-v2:%'
GROUP BY 1;

-- Ver chunks por documento
SELECT d.id, d.metadata->>'country_name', COUNT(c.id)
FROM documents d
LEFT JOIN chunks c ON d.id = c.document_id
WHERE d.source LIKE 'ai-regulation-v2:%'
GROUP BY 1, 2;

-- Verificar embeddings
SELECT d.id, d.metadata->>'country_name', c.embedding IS NOT NULL
FROM documents d
JOIN chunks c ON d.id = c.document_id
WHERE d.source LIKE 'ai-regulation-v2:%';
```

---

## 7. Documentación de metodología (`info_data/`)

| Archivo | Descripción |
|---------|-------------|
| `METODOLOGIA_FREEDOM_HOUSE.md` | Codificación Freedom House |
| `METODOLOGIA_GDPR_CODING.md` | Similitud GDPR |
| `METODOLOGIA_LEGAL_ORIGIN.md` | Clasificación origen legal |
| `VARIABLES_IAPP.md` | Variables IAPP Tracker |
| `VARIABLES_MICROSOFT.md` | Microsoft AI Index |
| `VARIABLES_OECD.md` | OECD AI |
| `VARIABLES_OXFORD_INSIGHTS.md` | Oxford AI Readiness |
| `VARIABLES_STANFORD_IA_INDEX.md` | Stanford AI Index |
| `VARIABLES_WIPO_GII.md` | WIPO GII |
| `VARIABLES_WORLD_BANK_WDI.md` | World Bank WDI |
| `TRAZABILIDAD_FUENTES_BIBLIOGRAFICAS.md` | Citas |

---

## 8. Conexión con sub-estudios paralelos

> Estos sub-estudios usan los mismos datos consolidados pero NO se reportan en este plan.

### 8.1 MVP Top 30 (en desarrollo)

- 29 P1-TOP30 todos DONE (corpus completo)
- + CHL focal (PENDING)
- Análisis SCM contrafactual + OLS/CEM/IV/Bayesian
- Plan: `../ARCHIVOS_MD_CONTEXTO/PLAN_MVP_TOP30_PAISES.md`

### 8.2 Proxies de infraestructura (en desarrollo)

- 6 pilotos (SGP, JPN, FRA, IRL, GBR, ESP) × 33 variables
- Datos: `data/raw/proxies/`
- Inventario fuentes: `data/raw/proxies/SOURCES_INVENTORY.md`

---

## 9. Cronograma actualizado

- [x] **Paso 0:** Generar `x1_master_v2.csv` con propuestas + variables nuevas (DONE 2026-04-28)
- [ ] Paso 1: Consolidar estructura `corpus_consolidated/` (incorporando v2 + autoridad/pathway)
- [ ] Paso 2: Copiar a `legal-rag/data/ai_regulation_v2`
- [ ] Paso 3: Script de ingestión optimizado con metadata rico
- [ ] Paso 4: Ejecutar ingestión
- [ ] Paso 5: Verificar embeddings y chunks
- [ ] Paso 6: Probar consultas RAG (smoke tests con 5 países)
- [ ] Paso 7: Procesar 48 países pendientes con la skill (asíncrono)

---

## 10. Próximos pasos críticos

1. **Procesar P2-IAPP-LOW pendientes** (16 países): aplicar skill `corpus-legal-ia` siguiendo orden de `sample.md`.
2. **Procesar P3-SAMPLE pendientes** (29 países): cuando P2 esté completo.
3. **Procesar CHL focal** (1): después del Top 30, con análisis especial para SCM.
4. **Resolver bloqueos automáticos** documentados en `data/raw/legal_corpus/BLOQUEOS_AUTOMATICOS.md`: CMR, KAZ, LBN, BHR, ARM.
5. **Re-generar x1_master_v2.csv** tras cada lote de países nuevos procesados.

---

*Generado: 2026-04-28 (v2)*
*Versión anterior: 2026-04-22 (v1, basada en 23 países)*
*Proyecto: LeyIA DataScience — "¿Regular o no regular?"*
*Referencia operativa de avance: `.claude/skills/corpus-legal-ia/sample.md`*
