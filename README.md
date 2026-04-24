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
| **Variables** | 66 columnas por país |
| **Fuentes** | 7 fuentes internacionales independientes |
| **Archivo definitivo** | `data/interim/sample_ready_cross_section.csv` |

Las variables se organizan en tres roles:

| Rol | Qué mide | Ejemplos |
|---|---|---|
| **Y** (resultado) | Ecosistema de IA del país | `ai_readiness_score`, `ai_adoption_rate`, `ai_investment_usd_bn_cumulative`, `ai_startups_cumulative` |
| **X1** (regulación) | Cómo regula cada país la IA | `has_ai_law`, `regulatory_approach`, `regulatory_intensity`, `enforcement_level` |
| **X2** (controles) | Factores que confunden la relación Y↔X1 | `gdp_per_capita_ppp`, `internet_penetration`, `gii_score`, `region` |

---

## Fuentes de Datos

| # | Fuente | Institución | Variables | Cobertura |
|---|---|---|---|---|
| 1 | Stanford AI Index 2025 | Stanford HAI | Inversión, startups, patentes IA | 54–84/86 |
| 2 | Microsoft AI Diffusion Report | Microsoft Research | Tasa de adopción de IA | 75/86 |
| 3 | Government AI Readiness Index 2025 | Oxford Insights | Score de preparación gubernamental | 86/86 |
| 4 | Global Innovation Index 2025 | WIPO (ONU) | Capacidad de innovación, región | 84/86 |
| 5 | World Development / Governance Indicators | World Bank | GDP, internet, educación, I+D, gobernanza | 63–85/86 |
| 6 | STI Scoreboard + MSTI | OECD | VC proxy, publicaciones IA | 32–60/86 |
| 7 | IAPP + EC-OECD AI Policy Database | IAPP / OECD | Regulación: leyes, enfoque, intensidad, enforcement | 86/86 |

---

## Arquitectura del Pipeline ETL

Los datos crudos de las 7 fuentes se transforman en un dataset analítico único a través de 3 etapas:

```
 data/raw/  (7 directorios, ~107 MB — nunca se modifican)
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
 │  Genera 7 masters estandarizados, 86 filas c/u     │
 └────────────────────────────────────────────────────┘
      │
      ▼
 data/interim/*_master.csv  (7 masters: y_stanford, y_microsoft, y_oxford,
                              x2_wipo, x2_wb, x1_master, oecd_robustness)
      │
      ▼
 ┌─ Paso 2: Ensamblaje ─────────────────────────────┐
 │  src/build_sample_ready.py                         │
 │  Fusiona 7 masters → 1 dataset definitivo          │
 │  Genera flags de completitud y matriz de cobertura │
 └────────────────────────────────────────────────────┘
      │
      ▼
 data/interim/sample_ready_cross_section.csv  (86 × 66 — DATASET DEFINITIVO)
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
│   │   └── World Bank WDI/           #   → GDP, internet, educación, I+D
│   ├── interim/                      # Archivos procesados por el pipeline
│   │   ├── *_master.csv              #   7 masters (86 filas c/u)
│   │   ├── sample_ready_cross_section.csv  #   DATASET DEFINITIVO (86 × 66)
│   │   └── coverage_matrix.csv       #   Matriz de auditoría variable × país
│   └── processed/                    # (Reservado para fase de limpieza)
│
├── src/                              # Scripts ETL del pipeline
│   ├── consolidate_x1.py            #   Reconcilia IAPP + OECD → panel X1
│   ├── build_stanford_y.py          #   Extrae figuras Stanford → Y
│   ├── expand_wdi.py                #   Descarga World Bank API → X2
│   ├── build_derived_controls.py    #   Construye oecd_member, region, status_group
│   ├── build_vc_proxy.py            #   OECD VC como % PIB → robustez
│   ├── iapp_coding.py               #   Codificación regulatoria IAPP
│   ├── build_source_masters.py      #   [Paso 1] Genera 7 masters
│   ├── build_sample_ready.py        #   [Paso 2] Ensambla dataset definitivo
│   ├── audit_sources.py             #   Auditoría de fuentes
│   ├── audit_completeness.py        #   Auditoría de completitud
│   └── download_public_drive_folder.py  #   Descarga Drive público de Stanford
│
├── notebooks/                        # Análisis secuencial
│   ├── 01_recoleccion.ipynb         #   Documentación del proceso de recolección
│   ├── 02_limpieza.ipynb            #   Limpieza, transformaciones, codificación
│   ├── 03_eda.ipynb                 #   Análisis exploratorio y visualizaciones
│   ├── 04_modelamiento.ipynb        #   Regresiones OLS, clustering, PCA
│   └── 05_nlp.ipynb                 #   Topic modeling de textos legales
│
├── docs/                             # Documentación formal del proyecto
│   ├── RECOPILACION_DATOS_PAPER.md  #   Sección de recopilación (1089 líneas)
│   ├── RECOPILACION_DATOS_PAPER.pdf #   Versión PDF profesional (35 páginas)
│   └── FUENTES_DATOS.docx           #   Detalle de las 7 fuentes de datos
│
├── info_data/                        # Documentación técnica del dataset
│   ├── ETL_RUNBOOK.md               #   Manual de ejecución del pipeline
│   ├── DATA_DECISIONS_LOG.md        #   Registro de 11 decisiones metodológicas
│   ├── GUIA_VARIABLES_ESTUDIO_ETL.md  #   Guía de variables y ETL
│   ├── TRAZABILIDAD_FUENTES_BIBLIOGRAFICAS.md
│   └── VARIABLES_*.md               #   Diccionarios por fuente (7 archivos)
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

El pipeline completo se ejecuta secuencialmente:

```bash
source .venv/bin/activate

# ── Paso 0: ETL por fuente (raw → interim individuales) ──
python src/consolidate_x1.py          # IAPP+OECD → x1_consolidated.csv
python src/build_stanford_y.py        # Stanford   → stanford_ai_*.csv
python src/expand_wdi.py              # World Bank → wdi_all_86.csv
python src/build_derived_controls.py  # Derivadas  → derived_controls.csv
python src/build_vc_proxy.py          # OECD       → ai_investment_vc_proxy.csv

# ── Paso 1: Source Masters (interim → 7 masters) ──
python src/build_source_masters.py    # → *_master.csv (7 archivos, 86 filas c/u)

# ── Paso 2: Ensamblaje (7 masters → dataset definitivo) ──
python src/build_sample_ready.py      # → sample_ready_cross_section.csv (86 × 66)
```

**Requisitos:** Python 3.9+ con pandas y numpy. Datos raw presentes en `data/raw/`.

---

## Muestras por Nivel de Completitud

No todos los 86 países tienen todas las variables. Según cuántas variables estén completas, existen 3 niveles de muestra:

| Nivel | Definición | N países | Para qué se usa |
|---|---|---|---|
| **Principal** | Y principales + X1 + X2 core completos | **72** | Modelo central de regresión |
| **Extended** | Principal + `rd_expenditure` + `tertiary_education` | **62** | Modelo ampliado con más controles |
| **Strict** | Extended + variables de robustez | **46** | Análisis de sensibilidad |

Los **14 países excluidos** de la muestra principal carecen de variables Y (principalmente `ai_adoption_rate` no reportada por Microsoft) o X2 (`gdp_per_capita_ppp` no disponible para Taiwán en World Bank). **Todas las variables X1 están completas para los 86 países.**

---

## Fases del Proyecto

| Fase | Notebook | Estado | Descripción |
|---|---|---|---|
| **1. Recopilación** | `01_recoleccion.ipynb` | ✅ Completa | Pipeline ETL de 8 scripts, 7 fuentes → dataset 86 × 66 |
| **2. Limpieza** | `02_limpieza.ipynb` | ⏳ Siguiente | Filtrar a 72, log-transforms, codificación, VIF, outliers |
| **3. EDA** | `03_eda.ipynb` | ⏳ Pendiente | Boxplots por grupo regulatorio, heatmaps, mapas |
| **4. Modelamiento** | `04_modelamiento.ipynb` | ⏳ Pendiente | OLS bivariado → multivariado → dummies → robustez → K-Means → PCA |
| **5. NLP** | `05_nlp.ipynb` | ⏳ Pendiente | TF-IDF, topic modeling (LDA), similaridad coseno de textos legales |

---

## Taxonomía Regulatoria

Los 86 países se clasifican en 4 grupos regulatorios:

| Grupo | Descripción | Ejemplos | N (principal) |
|---|---|---|---|
| `binding_regulation` | Legislación vinculante comprehensiva | UE (AI Act), China, Corea del Sur | 27 |
| `strategy_only` | Estrategia nacional sin ley vinculante | Chile, USA, UK, Australia | 34 |
| `soft_framework` | Principios o guías no vinculantes | India, Israel, Suiza | 9 |
| `no_framework` | Sin marco regulatorio de IA | Camerún, Líbano | 2 |

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

---

## Instalación

```bash
# Clonar y configurar entorno
cd research
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Ejecutar pipeline completo (requiere datos en data/raw/)
python src/consolidate_x1.py
python src/build_stanford_y.py
python src/expand_wdi.py
python src/build_derived_controls.py
python src/build_vc_proxy.py
python src/build_source_masters.py
python src/build_sample_ready.py
```

---

## Documentación Clave

| Documento | Ubicación | Descripción |
|---|---|---|
| Sección de recopilación | `docs/RECOPILACION_DATOS_PAPER.pdf` | Documento técnico completo (35 págs) |
| Detalle de fuentes | `docs/FUENTES_DATOS.docx` | Las 7 fuentes con justificación |
| Decisiones metodológicas | `info_data/DATA_DECISIONS_LOG.md` | 11 decisiones formales (D-001 a D-011) |
| Manual del pipeline | `info_data/ETL_RUNBOOK.md` | Instrucciones de reproducción |
| Guía de variables | `info_data/GUIA_VARIABLES_ESTUDIO_ETL.md` | Diccionario completo del dataset |
