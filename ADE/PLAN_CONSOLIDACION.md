# Plan de Consolidación - Corpus Legal-IA por País

## Objetivo
Consolidar toda la información recopilada de los 73 países en una estructura única, luego copiar a legal-rag y realizar la ingestión óptima.

---

## 1. Estructura de Información por País

### 1.1 Fuentes de Datos

| Fuente | Ubicación | Contenido | Países |
|--------|-----------|-----------|--------|
| **embedded_rag** | `/home/pablo/Research_LeyIA_DataScience/ADE/embedded_rag/{ISO3}/` | Perfil, regulación, chunks ricos | 75 países |
| **legal_corpus** | `/home/pablo/Research_LeyIA_DataScience/data/raw/legal_corpus/{ISO3}/` | PDF + análisis (SOURCES, CANDIDATES, FINDINGS) | 23 países |
| **info_data** | `/home/pablo/Research_LeyIA_DataScience/info_data/` | Metodologías y variables de estudios | Global |

### 1.2 Archivos por País en embedded_rag/

```
{ISO3}/
├── country_profile.json          # Métricas: población, GDP, AI readiness, etc.
├── regulatory_framework.json     # Grupo regulatorio, enfoque, intensidad
├── documents_index.json          # Lista de documentos legales (tipo, fecha, páginas)
├── embedding_chunks.json         # Chunks básicos
├── embedding_chunks_rich.json    # Chunks ricos (8-11 por país con análisis completo)
├── full_corpus_text.json         # Texto completo del corpus
├── legal_corpus.json             # Resumen del corpus legal
├── legal_corpus_full.json        # Corpus completo (SOURCES, CANDIDATES, FINDINGS)
├── meta_chunks.md                # Análisis diferencial (hallazgo)
└── documentos.json               # metadata de documentos
```

### 1.3 Archivos por País en legal_corpus/ (solo 23 países)

```
{ISO3}/
├── manifest.csv                  # Trazabilidad de PDFs (URL, hash, páginas)
├── SOURCES.md                    # Citas bibliográficas APA 7
├── CANDIDATES.md                 # Inventario + recodificación propuesta
├── FINDINGS.md                   # Hallazgo diferencial completo
└── *.pdf                         # Documentos legales descargados (NO incluir en ingestión)
```

---

## 2. Países por Tipo de Corpus

### 2.1 Países CON corpus legal completo (23)

Estos tienen PDFs + análisis SOURCES/CANDIDATES/FINDINGS:

`AUS, AUT, ARE, BEL, CAN, DEU, DNK, ESP, FRA, GBR, GHA, HUN, IRL, ISR, MNG, NLD, NOR, NZL, SGP, SWE, TWN, QAT (QAT no está en 73), CHL (solo perfil)`

### 2.2 Países SIN corpus legal (50)

Estos tienen solo perfil + marco regulatorio:

`ARG, ARM, BGD, BGR, BLR, BRA, CHE, CHL, CHN, CMR, COL, CRI, CZE, ECU, EGY, FIN, HRV, IDN, IND, ITA, JOR, JPN, KAZ, KEN, KOR, LBN, LKA, LTU, MEX, MYS, NGA, PAN, PER, PHL, POL, PRT, ROU, RUS, SAU, SRB, SVK, SVN, THA, TUN, TUR, UKR, URY, USA, VNM, ZAF`

### 2.3 Países de la muestra ADE (73)

Lista completa en master_index.json de embedded_rag/

---

## 3. Estructura Propuesta para Consolidation

### 3.1 Carpeta destino

```
/home/pablo/Research_LeyIA_DataScience/ADE/corpus_consolidated/{ISO3}/
```

### 3.2 Archivos a crear por país

```
{ISO3}/
├── 01_profile.json              # country_profile.json original
├── 02_regulatory.json           # regulatory_framework.json original
├── 03_documents_index.json      # Lista de documentos legales
├── 04_meta_analysis.md          # meta_chunks.md original
├── 05_sources.md                # SOURCES.md (si existe en legal_corpus)
├── 06_candidates.md             # CANDIDATES.md (si existe en legal_corpus)
├── 07_findings.md               # FINDINGS.md (si existe en legal_corpus)
├── 08_full_analysis.json        # legal_corpus_full.json (SOURCES+CANDIDATES+FINDINGS)
└── embedding_chunks.json        # embedding_chunks_rich.json
```

### 3.3 Archivo maestro de países

`master_index.json` con:
- ISO3, nombre país, región
- regulatory_group (binding_regulation, strategy_only, soft_framework, no_framework)
- has_corpus (true/false)
- n_documents, n_pages
- metrics (AI readiness, inversión, etc.)

---

## 4. Proceso de Ejecución

### Paso 1: Consolidar estructura (Script Python)
- Leer cada país de embedded_rag/
- Si existe en legal_corpus/, agregar SOURCES, CANDIDATES, FINDINGS
- Crear estructura unificada en corpus_consolidated/

### Paso 2: Copiar a legal-rag
```bash
cp -r /home/pablo/Research_LeyIA_DataScience/ADE/corpus_consolidated \
      /home/pablo/legal-rag/data/ai_regulation_v2/
```

### Paso 3: Script de ingestión optimizado
- 1 documento por país con metadata rico
- Múltiples chunks (meta-chunking):
  - Chunk 1: Perfil + ecosistema (resumen)
  - Chunk 2: Marco regulatorio (detalle)
  - Chunk 3: Documentos legales (lista)
  - Chunk 4: SOURCES completo
  - Chunk 5: CANDIDATES completo
  - Chunk 6: FINDINGS completo
- Embeddings con Ollama

---

## 5. Métricas y Variables Disponibles

### 5.1 Desde country_profile.json

| Variable | Descripción | Fuente |
|----------|-------------|--------|
| region | Región geográfica | IAPP |
| oecd_member | Miembro OECD | IAPP |
| legal_origin | Origen legal (English, French, etc.) | Legal Origin |
| is_common_law | Sistema common law | Legal Origin |
| population | Población | World Bank |
| gdp_current_usd | GDP nominal | World Bank |

### 5.2 Ecosystem IA

| Variable | Descripción | Fuente |
|----------|-------------|--------|
| ai_readiness_score | Score 0-100 | Oxford Insights |
| ai_adoption_rate | % adopción | Microsoft |
| ai_investment_usd_bn | Inversión acumulada | Microsoft |
| ai_startups | Número startups | Microsoft |
| ai_patents_per100k | Patentes per cápita | WIPO |

### 5.3 Controles

| Variable | Descripción | Fuente |
|----------|-------------|--------|
| gdp_per_capita_ppp | GDP per cápita PPP | World Bank |
| gii_score | Global Innovation Index | WIPO |
| internet_penetration | % penetración internet | World Bank |
| rd_expenditure | % PIB en I+D | World Bank |
| tertiary_education | % educación terciaria | World Bank |

### 5.4 Gobernanza

| Variable | Descripción | Fuente |
|----------|-------------|--------|
| regulatory_quality | Calidad regulatoria | World Bank |
| rule_of_law | Estado de derecho | World Bank |
| fh_total_score | Freedom House score | Freedom House |

### 5.5 Marco Regulatorio

| Variable | Descripción | Fuente |
|----------|-------------|--------|
| regulatory_group | Grupo (binding/strategy/soft/no) | IAPP + análisis |
| has_ai_law | Tiene ley IA específica | IAPP |
| regulatory_approach | Enfoque (proactive/reactive/etc.) | IAPP |
| regulatory_intensity | Intensidad 0-10 | GDPR coding |
| enforcement_level | Nivel enforcement | GDPR coding |
| thematic_coverage | Cobertura temática 0-15 | GDPR coding |
| gdpr_similarity | Similitud con GDPR | GDPR coding |

---

## 6. Documentación de Metodología (info_data/)

| Archivo | Descripción |
|---------|-------------|
| METODOLOGIA_FREEDOM_HOUSE.md | Cómo se codifica Freedom House |
| METODOLOGIA_GDPR_CODING.md | Cómo se mide similitud GDPR |
| METODOLOGIA_LEGAL_ORIGIN.md | Clasificación de origen legal |
| VARIABLES_IAPP.md | Variables del tracker IAPP |
| VARIABLES_MICROSOFT.md | Variables Microsoft AI Index |
| VARIABLES_OECD.md | Indicadores OECD |
| VARIABLES_OXFORD_INSIGHTS.md | Oxford AI Readiness |
| VARIABLES_STANFORD_IA_INDEX.md | Stanford AI Index |
| VARIABLES_WIPO_GII.md | WIPO Global Innovation Index |
| VARIABLES_WORLD_BANK_WDI.md | World Bank WDI |
| TRAZABILIDAD_FUENTES_BIBLIOGRAFICAS.md | Citas y fuentes |

---

## 7. Verificación Post-Ingestión

Consultas de verificación:

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

## 8. Cronograma

- [ ] Paso 1: Consolidar estructura de archivos por país
- [ ] Paso 2: Copiar a legal-rag/data/ai_regulation_v2
- [ ] Paso 3: Crear script de ingestión optimizado
- [ ] Paso 4: Ejecutar ingestión
- [ ] Paso 5: Verificar embeddings y chunks
- [ ] Paso 6: Probar consultas RAG

---

*Generado: 2026-04-22*
*Proyecto: LeyIA DataScience - Regular o No Regular?*