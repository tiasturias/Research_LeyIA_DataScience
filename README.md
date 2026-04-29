# ¿Regular o no regular? Impacto de la regulación de IA en los ecosistemas nacionales

> **Análisis comparativo del impacto de marcos regulatorios de inteligencia artificial en el desarrollo de ecosistemas de IA a nivel global**  
> IMT3860 — Introducción a Data Science · Abril 2026

---

## Descripción del Proyecto

Este proyecto investiga si existe una **asociación estadísticamente significativa** entre las características de la regulación de inteligencia artificial de un país y el desarrollo de su ecosistema de IA, después de controlar por factores socioeconómicos e institucionales.

El contexto es la decisión legislativa de Chile sobre el **Boletín 16821-19** (Ley Marco de IA), actualmente en trámite en el Senado. El estudio busca proveer evidencia empírica para informar esta decisión, comparando 86 países con distintos enfoques regulatorios.

### Sub-preguntas de investigación

1. **Inversión:** ¿Los marcos regulatorios más restrictivos se asocian con menores niveles de inversión privada en IA?
2. **Adopción:** ¿Qué tipo de enfoque regulatorio se asocia con mayores tasas de adopción de IA?
3. **Innovación:** ¿Existe relación entre regulación de IA e indicadores de innovación (startups, patentes)?
4. **Contenido regulatorio (NLP):** ¿Qué temas dominan en los textos legales de IA y cómo se agrupan los países?

---

## Dataset

| Dimensión | Valor |
|---|---|
| **Países** | 86 (universo) · 72 (muestra principal) |
| **Variables** | 105+ columnas por país (66 base + controles institucionales + corpus / propuestas) |
| **Fuentes** | 10 fuentes independientes + corpus legal-IA (skill) |
| **Archivo definitivo** | `data/interim/sample_ready_cross_section.csv` (86 × 105+) |
| **Corpus legal-IA** | 43/86 países procesados (skill `corpus-legal-ia`) · 75/86 en `embedded_rag` |

Las variables se organizan en tres roles:

| Rol | Qué mide | Ejemplos |
|---|---|---|
| **Y** (resultado) | Ecosistema de IA del país | `ai_readiness_score`, `ai_adoption_rate`, `ai_investment_usd_bn_cumulative`, `ai_startups_cumulative` |
| **X1** (regulación) | Cómo regula cada país la IA | `has_ai_law`, `regulatory_approach`, `regulatory_intensity`, `enforcement_level`, `has_dedicated_ai_authority`, `ai_law_pathway_declared` |
| **X2** (controles) | Factores que confunden la relación Y↔X1 | `gdp_per_capita_ppp`, `internet_penetration`, `gii_score`, `regulatory_quality`, `rule_of_law`, `fh_total_score`, `legal_origin`, `has_gdpr_like_law`, `region` |

---

## Fuentes de Datos

| # | Fuente | Institución | Variables | Cobertura |
|---|---|---|---|---|
| 1 | Stanford AI Index 2025 | Stanford HAI | Inversión, startups, patentes IA | 54–84/86 |
| 2 | Microsoft AI Diffusion Report | Microsoft Research | Tasa de adopción de IA | 75/86 |
| 3 | Government AI Readiness Index 2025 | Oxford Insights | Score de preparación gubernamental | 86/86 |
| 4 | Global Innovation Index 2025 | WIPO (ONU) | Capacidad de innovación, región | 84/86 |
| 5 | World Development / Governance Indicators | World Bank | GDP, internet, educación, I+D, gobernanza (WGI) | 63–85/86 |
| 6 | STI Scoreboard + MSTI | OECD | VC proxy, publicaciones IA | 32–60/86 |
| 7 | IAPP + EC-OECD AI Policy Database | IAPP / OECD | Regulación: leyes, enfoque, intensidad, enforcement | 86/86 |
| 8 | DLA Piper 2025 + UNCTAD (codificación manual) | DLA Piper / UNCTAD | Leyes de protección de datos tipo GDPR, DPA, nivel de similitud | 86/86 |
| 9 | Freedom in the World 2025 (codificación manual) | Freedom House | Score de democracia, derechos políticos y libertades civiles | 86/86 |
| 10 | La Porta et al. 2008 (codificación manual) | Literatura académica | Tradición legal (common law / civil law) | 86/86 |

---

## Arquitectura del Pipeline ETL

Los datos crudos de las fuentes se transforman en un dataset analítico único a través de 3 etapas:

```
 data/raw/  (10+ directorios — nunca se modifican)
      │
      ▼
 ┌─ Paso 0: ETL por fuente ──────────────────────────┐
 │  Cada fuente tiene su script dedicado en src/      │
 │  Normaliza nombres, mapea a ISO3, selecciona año   │
 └────────────────────────────────────────────────────┘
      │
      ▼
 data/interim/*_individual.csv  (archivos intermedios por fuente)
      │
      ▼
 ┌─ Paso 1: Source Masters ──────────────────────────┐
 │  src/build_source_masters.py                       │
 │  Genera masters estandarizados, 86 filas c/u       │
 └────────────────────────────────────────────────────┘
      │
      ▼
 data/interim/*_master.csv  (masters: y_stanford, y_microsoft, y_oxford,
                              x2_wipo, x2_wb, x2_fh, x2_gdpr, x2_legal_origin,
                              x1_master, x1_master_v2, oecd_robustness)
      │
      ▼
 ┌─ Paso 2: Ensamblaje ─────────────────────────────┐
 │  src/build_sample_ready.py                         │
 │  Fusiona masters → 1 dataset definitivo            │
 │  Genera flags de completitud y matriz de cobertura │
 └────────────────────────────────────────────────────┘
      │
      ▼
 data/interim/sample_ready_cross_section.csv  (86 × 105+ — DATASET DEFINITIVO)
      │
      ▼
 ┌─ Fase ADE v2 ────────────────────────────────────┐
 │  ADE/01_ADE_Analisis_Exploratorio.ipynb            │
 │  Análisis descriptivo exploratorio con corpus v2  │
 └────────────────────────────────────────────────────┘
      │
      ▼
 ┌─ Fase siguiente ─────────────────────────────────┐
 │  notebooks/02_limpieza.ipynb                       │
 │  Limpia, transforma y exporta a data/processed/   │
 └────────────────────────────────────────────────────┘
```

---

## Estructura del Proyecto

```
research/
├── data/
│   ├── raw/                          # Datos crudos originales (NUNCA se modifican)
│   │   ├── IAPP/                     #   → Regulación: IAPP Global AI Law Tracker
│   │   ├── Microsoft/                #   → Adopción: AI Diffusion Report
│   │   ├── OECD/                     #   → Robustez: STI Scoreboard, MSTI
│   │   ├── Oxford Insights/          #   → Readiness: AI Readiness Index 2025
│   │   ├── STANFORD AI INDEX 25/     #   → Inversión, startups, patentes
│   │   ├── WIPO Global Innovation Index/  #   → GII score, región
│   │   ├── World Bank WDI/           #   → GDP, internet, educación, I+D, WGI
│   │   ├── FreedomHouse/             #   → Democracia: Freedom in the World 2025
│   │   ├── GDPR_coding/              #   → Leyes de protección de datos (manual)
│   │   ├── LegalOrigin/              #   → Tradición legal La Porta (manual)
│   │   ├── proxies/                  #   → Proxies infraestructura DC / energía
│   │   └── legal_corpus/             #   → Corpus legal-IA por país (skill output)
│   │       └── {ISO3}/               #     manifest.csv · SOURCES.md · CANDIDATES.md · FINDINGS.md
│   ├── interim/                      # Archivos procesados por el pipeline
│   │   ├── *_master.csv              #   Masters por fuente (86 filas c/u)
│   │   ├── sample_ready_cross_section.csv  #   DATASET DEFINITIVO (86 × 105+)
│   │   └── coverage_matrix.csv       #   Matriz de auditoría variable × país
│   └── processed/                    # (Reservado para fase de limpieza)
│
├── data_v2/                          # Análisis EDA legal-IA matricial (paralelo)
│   ├── {ISO3}/                       #   Perfiles por país
│   └── 2_EDA/                        #   Matrices consolidadas, clusters, regresiones
│
├── src/                              # Scripts ETL del pipeline
│   ├── consolidate_x1.py            #   Reconcilia IAPP + OECD → panel X1
│   ├── consolidate_x1_v2.py         #   X1 v2 con variables de propuesta
│   ├── build_stanford_y.py          #   Extrae figuras Stanford → Y
│   ├── expand_wdi.py                #   Descarga World Bank WDI API → X2
│   ├── expand_wgi.py                #   Descarga World Bank WGI → regulatory_quality, rule_of_law
│   ├── expand_digital_economy.py    #   ICT exports, high-tech exports → X2 digital
│   ├── build_derived_controls.py    #   Construye oecd_member, region, status_group
│   ├── build_vc_proxy.py            #   OECD VC como % PIB → robustez
│   ├── build_proxy_pilots_master.py #   Proxies infraestructura DC (scraping)
│   ├── iapp_coding.py               #   Codificación regulatoria IAPP
│   ├── build_source_masters.py      #   [Paso 1] Genera masters por fuente
│   ├── build_sample_ready.py        #   [Paso 2] Ensambla dataset definitivo
│   ├── audit_sources.py             #   Auditoría de fuentes
│   ├── audit_completeness.py        #   Auditoría de completitud
│   ├── scrape_country_dc_policies.py#   Scraper: políticas DC por país
│   ├── scrape_eu_eed_registry.py    #   Scraper: registro EED (UE)
│   ├── scrape_eurostat_electricity.py#  Scraper: precio electricidad Eurostat
│   ├── scrape_jll_dc_outlook.py     #   Scraper: JLL Data Center Outlook
│   ├── scrape_worldbank_bready.py   #   Scraper: World Bank B-Ready
│   ├── scrape_wri_aqueduct.py       #   Scraper: WRI Aqueduct (agua)
│   └── download_public_drive_folder.py  #   Descarga Drive público de Stanford
│
├── tools/                            # Herramientas de scraping avanzadas
│   └── scraper/                      #   Browser, cloudflare bypass, downloader, law_extractor
│
├── ADE/                              # Análisis Descriptivo Exploratorio v2
│   ├── 01_ADE_Analisis_Exploratorio.ipynb  # Notebook ADE principal (corpus v2) ✅
│   ├── outputs/                      #   Visualizaciones y tablas exportadas
│   ├── corpus_consolidated/          #   Corpus consolidado por país
│   ├── embedded_rag/                 #   Perfiles + chunks para RAG (75 países)
│   ├── scripts/                      #   Scripts auxiliares de consolidación
│   ├── PLAN_CONSOLIDACION.md        #   Plan de consolidación a legal-rag
│   └── README.md                     #   Documentación del ADE
│
├── notebooks/                        # Análisis secuencial
│   ├── 01_recoleccion.ipynb         #   Documentación del proceso de recolección ✅
│   ├── 02_limpieza.ipynb            #   Limpieza, transformaciones, codificación ⏳
│   ├── 03_eda.ipynb                 #   Análisis exploratorio y visualizaciones ⏳
│   ├── 04_modelamiento.ipynb        #   Regresiones OLS, clustering, PCA ⏳
│   └── 05_nlp.ipynb                 #   Topic modeling de textos legales ⏳
│
├── docs/                             # Documentación formal del proyecto
│   ├── RECOPILACION_DATOS_PAPER.md  #   Sección de recopilación (1089 líneas)
│   ├── RECOPILACION_DATOS_PAPER.pdf #   Versión PDF profesional (35 páginas)
│   ├── HALLAZGOS_DIFERENCIALES.md   #   Tesis diferenciales del corpus legal-IA
│   ├── INFORME_AUDITORIA_Y_PLAN_CORPUS.md  #   Auditoría y plan corpus legal-IA
│   ├── INFORME_EJECUTIVO_ADE_EDA.pdf #  Informe ejecutivo del ADE
│   ├── INFORME_EJECUTIVO_CORPUS_LEGAL_SENADO.md  #  Informe para el Senado
│   ├── PIPELINE_BUSQUEDA_CORPUS_LEGAL_IA.md  #  Guía de búsqueda del corpus
│   ├── PLAN_CORPUS_NLP_TAREA_C.md   #   Plan NLP tarea C
│   └── FUENTES_DATOS.docx           #   Detalle de las 10 fuentes de datos
│
├── ARCHIVOS_MD_CONTEXTO/             # Contexto para LLMs y seguimiento
│   ├── SEGUIMIENTO_PAISES_MUESTRA.md #  Estado de cobertura de los 86 países
│   └── ...                           #  Otros archivos de contexto
│
├── context_llm/                      # Contexto para asistentes LLM
│   ├── PROYECTO DATASCIENCE .md     #   Descripción general del proyecto
│   ├── guia_metodologia.md          #   Metodología del estudio
│   └── stanford_ai_index_resume.md  #   Resumen del Stanford AI Index
│
├── outputs/                          # (Reservado para gráficos y tablas)
├── requirements.txt                  # Dependencias de Python
└── README.md                         # ← Este archivo
```

---

## Scripts ETL — Orden de Ejecución

```bash
source .venv_linux/bin/activate

# ── Paso 0: ETL por fuente (raw → interim individuales) ──
python src/consolidate_x1.py          # IAPP+OECD → x1_consolidated.csv
python src/build_stanford_y.py        # Stanford   → stanford_ai_*.csv
python src/expand_wdi.py              # World Bank → wdi_all_86.csv
python src/expand_wgi.py              # World Bank WGI → regulatory_quality, rule_of_law
python src/expand_digital_economy.py  # ICT + high-tech exports → digital controls
python src/build_derived_controls.py  # Derivadas  → derived_controls.csv
python src/build_vc_proxy.py          # OECD       → ai_investment_vc_proxy.csv

# ── Paso 1: Source Masters (interim → masters) ──
python src/build_source_masters.py    # → *_master.csv (86 filas c/u)

# ── Paso 2: Ensamblaje (masters → dataset definitivo) ──
python src/build_sample_ready.py      # → sample_ready_cross_section.csv (86 × 105+)

# ── Paso 3: Corpus legal-IA (skill corpus-legal-ia) ──
# Ejecutar skill por país → data/raw/legal_corpus/{ISO3}/
# Genera: x1_master_v2.csv con propuestas + variables derivadas
```

**Requisitos:** Python 3.9+ con pandas y numpy. Datos raw presentes en `data/raw/`.

---

## Muestras por Nivel de Completitud

| Nivel | Definición | N países | Para qué se usa |
|---|---|---|---|
| **Principal** | Y principales + X1 + X2 core completos | **72** | Modelo base de regresión |
| **Confounded** ★ | Principal + WGI (reg. quality, rule of law) + GDPR-like | **72** | **Modelo recomendado** |
| **Regime** | Principal + Freedom House (democracia) | **72** | Análisis por tipo de régimen político |
| **Legal Tradition** | Principal + legal origin (La Porta) | **72** | Análisis por familia legal |
| **Digital** | Principal + ICT exports + high-tech exports | **69** | Análisis de economía digital |
| **Extended** | Confounded + R&D + educación terciaria | **62** | Modelo ampliado con más controles |
| **Strict** | Extended + patentes + gov_effectiveness | **47** | Análisis de sensibilidad |

Los **14 países excluidos** de la muestra principal carecen de variables Y (principalmente `ai_adoption_rate`) o X2 (`gdp_per_capita_ppp`). **Todas las variables X1 están completas para los 86 países.**

---

## Fases del Proyecto

| Fase | Notebook | Estado | Descripción |
|---|---|---|---|
| **1. Recopilación** | `01_recoleccion.ipynb` | ✅ Completa | Pipeline ETL, 10 fuentes → dataset 86 × 105+ |
| **2. Limpieza** | `02_limpieza.ipynb` | ⏳ Siguiente | Filtrar a 72, log-transforms, codificación, VIF, outliers |
| **3. EDA** | `ADE/01_ADE_Analisis_Exploratorio.ipynb` | ✅ Completa v2 | ADE con corpus 43/86, comparación IAPP vs propuesta, nuevas variables |
| **3b. EDA (legacy)** | `03_eda.ipynb` | ⏳ Pendiente | Versión legacy en notebooks/ (será consolidada) |
| **4. Modelamiento** | `04_modelamiento.ipynb` | ⏳ Pendiente | OLS bivariado → multivariado → dummies → robustez → K-Means → PCA |
| **5. NLP** | `05_nlp.ipynb` | ⏳ Pendiente | TF-IDF, topic modeling (LDA), similaridad coseno de textos legales |

---

## Taxonomía Regulatoria

Los 86 países se clasifican en 4 grupos regulatorios:

| Grupo | Descripción | Ejemplos | N total (86) | N muestra principal (72) |
|---|---|---|---|---|
| `binding_regulation` | Legislación vinculante comprehensiva | UE (AI Act), China, Corea del Sur | 32 | 27 |
| `strategy_only` | Estrategia nacional sin ley vinculante | Chile, USA, UK, Australia | 39 | 34 |
| `soft_framework` | Principios o guías no vinculantes | India, Israel, Suiza | 10 | 9 |
| `no_framework` | Sin marco regulatorio de IA | Camerún, Líbano | 5 | 2 |

---

## Chile en el Dataset

| Indicador | Valor | Contexto |
|---|---|---|
| Enfoque regulatorio | `strategy_only` | Boletín 16821-19 en trámite en el Senado |
| Intensidad regulatoria | 4 de 5 | Medio-alto |
| AI Readiness Score | 59.30 | Cercano a la mediana global (60.90) |
| Adopción de IA | 20.8% | Ligeramente bajo la mediana (22.45%) |
| Inversión IA acumulada | USD 0.68 bn | Sobre la mediana (0.33) |
| Startups IA | 17 | Cercano a la mediana (15) |
| Muestra principal | ✅ | 18/19 variables disponibles |
| Corpus legal-IA | ✅ DONE | Procesado (en cola focal, posterior al Top 30) |

---

## Instalación

```bash
# Clonar y configurar entorno
cd research
python3 -m venv .venv_linux
source .venv_linux/bin/activate
pip install pandas numpy matplotlib seaborn scipy ipykernel nbconvert

# Registrar kernel de Jupyter (opcional, para notebooks)
python -m ipykernel install --user --name=.venv_linux --display-name="Python (.venv_linux)"

# Ejecutar pipeline completo (requiere datos en data/raw/)
python src/consolidate_x1.py
python src/build_stanford_y.py
python src/expand_wdi.py
python src/expand_wgi.py
python src/expand_digital_economy.py
python src/build_derived_controls.py
python src/build_vc_proxy.py
python src/build_source_masters.py
python src/build_sample_ready.py

# Ejecutar ADE v2
jupyter nbconvert --to notebook --execute ADE/01_ADE_Analisis_Exploratorio.ipynb --output ADE/01_ADE_Analisis_Exploratorio.ipynb
```

---

## Documentación Clave

| Documento | Ubicación | Descripción |
|---|---|---|
| Sección de recopilación | `docs/RECOPILACION_DATOS_PAPER.pdf` | Documento técnico completo (35 págs) |
| Detalle de fuentes | `docs/FUENTES_DATOS.docx` | Las 10 fuentes con justificación |
| Hallazgos diferenciales | `docs/HALLAZGOS_DIFERENCIALES.md` | Tesis diferenciales del corpus por país |
| Informe ejecutivo ADE | `docs/INFORME_EJECUTIVO_ADE_EDA.pdf` | Síntesis del ADE v2 |
| Informe corpus Senado | `docs/INFORME_EJECUTIVO_CORPUS_LEGAL_SENADO.md` | Síntesis regulatoria para política pública |
| Seguimiento de países | `ARCHIVOS_MD_CONTEXTO/SEGUIMIENTO_PAISES_MUESTRA.md` | Estado de cobertura de los 86 países |
| Plan consolidación corpus | `ADE/PLAN_CONSOLIDACION.md` | Estado v2 del corpus legal-IA (43/86 países) |
| ADE v2 | `ADE/README.md` | Documentación del Análisis Descriptivo Exploratorio v2 |
