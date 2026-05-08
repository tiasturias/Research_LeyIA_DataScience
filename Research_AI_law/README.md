# Research_AI_law — Estudio Observacional Comparativo sobre Regulación de IA

**Boletín 16821-19 — Ley Marco de Inteligencia Artificial de Chile**

[![Estado](https://img.shields.io/badge/Fase-6%20v2.2%20completada-brightgreen)](#)
[![Metodología](https://img.shields.io/badge/Metodolog%C3%ADa-Inferencial%20Comparativa%20Observacional-blue)](#)
[![Muestra](https://img.shields.io/badge/Muestra-43%20pa%C3%ADses-orange)](#)
[![Fuentes](https://img.shields.io/badge/Fuentes-8%20internacionales-purple)](#)

---

## Resumen

Este repositorio investiga la relación entre las características regulatorias de inteligencia artificial (IA) de los países y el desarrollo de sus ecosistemas de IA, usando una muestra preregistrada de **43 países** y datos de **8 fuentes internacionales** (Oxford Insights, WIPO, OECD, Banco Mundial, IAPP, Microsoft, Anthropic, Stanford HAI). El caso focal es **Chile**, donde el Boletín 16821-19 propone una Ley Marco de IA actualmente en trámite legislativo.

**Pregunta principal:** *¿Existe una asociación estadísticamente significativa entre las características de la regulación de IA de un país y el desarrollo de su ecosistema de IA, después de controlar por factores socioeconómicos e institucionales?*

**Estado actual:** Fases 1-6 completadas. Fases 7 (Robustez) y 8 (Narrativa/Política Pública) pendientes.

---

## Arquitectura del Repositorio

```
Research_AI_law/
├── README.md                          ← Este archivo
├── pyproject.toml                     # Configuración Python del proyecto
│
├── CONTEXTOS/                         # 📚 Documentación y planificación central
├── FASE3/                             # 🗄️ Matriz Madre (base de datos unificada)
├── FASE4/                             # 📊 Análisis Exploratorio de Datos (EDA)
├── F5_F8_MVP/                         # 🚀 Pipeline MVP: Fases 5-8
│   ├── _common/                       # Código compartido entre fases
│   ├── FASE5/                         # Preparación de datos (Feature Engineering)
│   ├── FASE6/                         # ★ Modelado Inferencial (FASE ACTUAL)
│   │   ├── src/                       # Módulos Q1-Q6 + Country Intelligence
│   │   ├── notebooks/                 # Notebook didáctico de auditoría
│   │   ├── outputs/                   # Resultados, perfiles país, figuras
│   │   └── config/                    # Contratos y planes de análisis
│   ├── FASE7/                         # 🔜 Robustez y Sensibilidad (pendiente)
│   ├── FASE8/                         # 🔜 Narrativa y Política Pública (pendiente)
│   └── auditoria_fase5_v2_1_plus/    # Registro de auditoría Fase 5
│
├── FUENTES/                           # 📥 Datos crudos de las 8 fuentes
├── notebooks/                         # 📓 Notebooks exploratorios (Fase 1-2)
├── NUEVA_METODOLOGIA_08/             # 🔧 Blueprints de reestructuración (v0.3)
└── .claude/                           # ⚙️ Skills y configuración Claude
```

---

## 📂 Descripción de cada carpeta

### `CONTEXTOS/` — Documentación Central del Proyecto

El **centro de conocimiento** del proyecto. Aquí están todos los planes, blueprints, justificaciones metodológicas y la arquitectura completa. Si quieres entender el proyecto de principio a fin, empieza aquí.

| Archivo | Contenido |
|---|---|
| `6.ARQUITECTURA_COMPLETA_PROYECTO.md` ★ | **Documento maestro** (862 líneas). Cubre Fases 1-8: problema de investigación, 8 fuentes con todas las variables explicadas, muestra de 43 países, las 6 preguntas (Q1-Q6), pipeline end-to-end, Fase 4 EDA con PCA/clustering/taxonomía, Fase 6 con justificación detallada de cada modelo, hallazgos, Chile en contexto. |
| `7.PLAN_FASES_7_8_Y_CORRECCION_IAPP.md` ★ | Plan de abordaje para Fases 7-8, diagnóstico del cuello de botella IAPP (solo 18 países), solución via Techieray Global AI Regulation Tracker, lecciones aprendidas desde Fase 1. |
| `5.PLAN_FASE_MVP_END_TO_END.md` | Plan original del MVP (Fases 5-8). Decisión de eliminar train/test split. Contrato metodológico v0.2. Arquitectura de directorios, especificaciones de código. |
| `pipeline_datascience.md` | Guía CRISP-DM adaptada a este proyecto. Marco de referencia para las 8 fases. |
| `1.PLAN_EDA_PRELIMINAR_RAW.md` | Plan de exploración inicial de datos crudos (Fase 1-2). |
| `3.PLAN_FASE3_MATRIZ_MADRE.md` | Plan de construcción de la matriz madre (Fase 3). |
| `4.PLAN_FASE4_EDA.md` | Plan del EDA principal (Fase 4). |
| `FASE6_EXPLICACION.md` | Explicación didáctica de la Fase 6 para todo público. |
| `arquitectura_ciencia_datos_didactico.pdf` | PDF didáctico sobre arquitectura de ciencia de datos. |

### `FASE3/` — Matriz Madre (Base de Datos Unificada) ✅

La **fuente de verdad** de todos los datos del proyecto. Integra 8 fuentes internacionales en una matriz unificada.

**Entregable principal:** `Matriz_Madre_Fase3.xlsx` — 199 países × 1,203 columnas.

| Subcarpeta/Archivo | Contenido |
|---|---|
| `outputs/` | Matriz madre (wide, panel, snapshot), diccionario de 397 variables, trazabilidad, crosswalk geográfico, reportes de calidad |
| `src/fase3/api.py` | API estable: `load_wide()`, `load_dictionary()`, `get_block()`, `get_chile_snapshot()` |

**Regla de oro:** Fase 3 es inmutable. Las fases posteriores solo leen, nunca modifican.

### `FASE4/` — Análisis Exploratorio de Datos (EDA) ✅

El **diagnóstico exhaustivo** de los datos antes del modelado. Aplica estadística robusta (mediana, IQR, Spearman) y técnicas multivariadas.

**Técnicas aplicadas:** PCA (global y por bloque), clustering exploratorio de países, correlaciones Spearman/Kendall/Pearson, correlaciones parciales con corrección FDR, taxonomía regulatoria binding/non-binding/hybrid.

**Entregable vinculante:** `eda_decisions_for_fase5.yaml` — todas las decisiones preregistradas que Fase 5 debe ejecutar.

| Subcarpeta/Archivo | Contenido |
|---|---|
| `outputs/eda_principal/` | ~30 archivos CSV: correlaciones, PCA loadings, clustering, perfiles país, binding taxonomy, candidatos para feature engineering |
| `config/fase4/binding_taxonomy.yaml` | Clasificación de variables IAPP en binding/non-binding/hybrid |

### `F5_F8_MVP/` — Pipeline MVP (Fases 5-8)

El **corazón ejecutable** del proyecto. Cada fase vive en su propia carpeta autocontenida con `src/`, `config/`, `tests/`, `notebooks/`, `outputs/`.

#### `F5_F8_MVP/FASE5/` — Preparación de Datos ✅

Transforma la matriz madre en una **feature matrix** lista para modelado.

**Pipeline:** filtrar 43 países → filtrar 46 variables → log-transform → z-score robusto (mediana/MAD) → variables agregadas (`n_binding`, `n_non_binding`) → contrato metodológico (sin train/test split).

**Entregable principal:** `phase6_ready/phase6_feature_matrix.csv` (43 filas × n columnas).

#### `F5_F8_MVP/FASE6/` — Modelado Inferencial ★ FASE ACTUAL

La fase más extensa. Se divide en dos sub-capas:

**Fase 6.1 — Modelado Inferencial Base**
6 módulos de modelado con justificación detallada de cada elección:

| Módulo | Q | Método | Justificación clave |
|---|---|---|---|
| `q1_investment.py` | Q1 | OLS HC3 + Bootstrap BCa | Interpretabilidad, robustez a heterocedasticidad, IC sin supuestos asintóticos |
| `q2_adoption.py` | Q2 | Fractional Logit + Sensibilidad binaria | Outcomes acotados [0,1]; OLS violaría supuestos; binario solo como auxiliar |
| `q3_innovation.py` | Q3 | OLS HC3 + Bootstrap | Ídem Q1 |
| `q4_clustering.py` | Q4 | HCA + Jaccard + KMeans | Variables binarias → Jaccard; HCA no requiere k a priori; KMeans como sensibilidad |
| `q5_population_usage.py` | Q5 | Fractional Logit + Sensibilidad | Ídem Q2 |
| `q6_public_sector.py` | Q6 | Fractional Logit + Sensibilidad | Ídem Q2 |

**Fase 6.2 — Country Intelligence Layer**
Traduce resultados de modelos en **perfiles país por país**:

| Output | Descripción |
|---|---|
| `country_q_profile_long.csv` ★ | Archivo central: 903 filas (país × Q × outcome) con percentiles, rankings, etiquetas |
| `country_rankings_by_group.csv` | 3,297 filas: rankings por 16 grupos (región, ingreso, custom) |
| `country_headline_flags.csv` | Pioneros y rezagados consistentes (6 + 3) |
| `country_learning_patterns.csv` | Lecciones de pioneros/rezagados para Chile |
| `figures/` | **40 archivos gráficos** (20 PNG + 20 SVG) en 8 subcarpetas, cada uno con su `.md` descriptivo didáctico |
| `country_cards_data/` | 11 fichas CSV consolidadas (CHL, SGP, EST, IRL, ARE, KOR, JPN, USA, CHN, BRA, URY) |

**Documentos clave en FASE6/outputs/:**
- `INDICE_ARQUITECTONICO_OUTPUTS.md` — Catálogo completo de los 28 outputs de Fase 6
- `fase6_manifest.json` — Contrato metodológico (sin holdout, sin causalidad, sin split)
- `q*_results.csv` — Resultados de modelos (12 a 36 filas por Q)

#### `F5_F8_MVP/FASE7/` — Robustez y Sensibilidad 🔜

**Pendiente.** Evaluará estabilidad de hallazgos de Fase 6 mediante: baselines, leave-group-out, influencia de outliers, estabilidad de clusters. El blueprint técnico completo está en `nueva_metodologia/FASE7_PLAN.md`.

#### `F5_F8_MVP/FASE8/` — Narrativa y Política Pública 🔜

**Pendiente.** Producirá el notebook maestro, informe ejecutivo (8-12 páginas) y recomendaciones para el Boletín 16821-19.

### `FUENTES/` — Datos Crudos

Archivos originales descargados de las 8 fuentes internacionales, organizados por fuente:

| Carpeta | Fuente | ¿Qué contiene? |
|---|---|---|
| `Oxford Insights/` | Government AI Readiness Index 2024 | 39 indicadores en 3 pilares (gobierno, sector tech, datos) |
| `WIPO Global Innovation Index/` | Global Innovation Index 2024 | Input/output de innovación, deals de VC |
| `OECD/` | Digital Government + ICT Stats | INDIGO, adopción empresarial de IA, gobierno digital |
| `World Bank WDI/` | World Development Indicators + WGI | PIB, educación, I+D, infraestructura, gobernanza |
| `IAPP/` | AI Legislation Tracker | Leyes y proyectos de ley de IA por país |
| `MICROSOFT/` | AI Diffusion Index 2025 | Difusión poblacional de IA |
| `ANTROPHIC/` | Usage Data 2024 | Uso de Claude por país |
| `STANFORD AI INDEX 26/` | AI Index Report | Publicaciones y patentes de IA |

### `notebooks/` — Exploración Inicial

Notebooks de las Fases 1-2 (exploración preliminar de datos crudos, antes de la construcción de la matriz madre).

### `NUEVA_METODOLOGIA_08/` — Blueprints de Reestructuración

Documentos técnicos que guiaron la corrección metodológica del pipeline. Contiene el blueprint maestro de reestructuración arquitectónica F5-F8 (v0.3) y especificaciones detalladas de implementación.

---

## 🧪 Las 6 Preguntas de Investigación

| Q | Título | Pregunta | Modelo |
|---|---|---|---|
| **Q1** | Inversión | ¿Países con más regulación IA muestran mejor inversión, VC, unicornios? | OLS + HC3 + Bootstrap |
| **Q2** | Adopción | ¿Países con más regulación IA muestran mayor adopción empresarial? | Fractional Logit |
| **Q3** | Innovación | ¿Países con más regulación IA muestran mejor innovación/preparación? | OLS + HC3 + Bootstrap |
| **Q4** | Perfil Regulatorio | ¿Qué perfiles regulatorios tienen los países? ¿Con quién se parece Chile? | HCA + Jaccard |
| **Q5** | Uso Poblacional | ¿Países con más regulación IA muestran mayor uso social de IA? | Fractional Logit |
| **Q6** | Sector Público | ¿Países con más regulación IA muestran mayor capacidad pública digital? | Fractional Logit |

---

## 🌍 La Muestra: 43 Países

| Región | Países |
|---|---|
| **Europa y Asia Central** (22) | DEU, FRA, GBR, NLD, EST, IRL, DNK, FIN, SWE, NOR, CHE, AUT, BEL, ESP, ITA, CZE, POL, HUN, BGR, ROU, HRV, GRC |
| **Asia Oriental y Pacífico** (8) | SGP, KOR, JPN, CHN, AUS, NZL, TWN, IND |
| **Latinoamérica y Caribe** (8) | **CHL**, ARG, BRA, COL, MEX, PER, URY, CRI |
| **Medio Oriente y Norte de África** (3) | ARE, ISR, QAT |
| **Norteamérica** (2) | USA, CAN |

---

## 📊 Fuentes de Datos y Variables

| Fuente | Variables en el estudio | Rol principal |
|---|---|---|
| **Oxford Insights** | 10 (preparación país, inversión, adopción, e-gov, gobernanza) | Outcomes (Y) |
| **WIPO** | 2 (output innovación, deals VC) | Outcomes (Y) |
| **OECD** | 3 (adopción empresarial, INDIGO, gobierno digital) | Outcomes (Y) |
| **Banco Mundial** | 11 (PIB, internet, gobernanza, I+D, educación, infraestructura) | Controles (C) |
| **IAPP** | 4 (ley vigente, proyecto, n_binding, n_non_binding) | Predictores (X1) |
| **Microsoft** | 1 (difusión poblacional IA) | Outcome (Y) |
| **Anthropic** | 2 (uso Claude, colaboración humano-IA) | Outcomes (Y) |
| **Stanford HAI** | 2 (publicaciones, patentes — pendientes) | Outcomes (Y) |

---

## 🔑 Principios Metodológicos

1. **Estudio observacional comparativo**, no predictivo. No existe train/test split.
2. **Cero imputación**: si un dato falta, se documenta como missing.
3. **Cero causalidad**: el lenguaje permitido es "asociación ajustada", no "efecto causal".
4. **Submuestra preregistrada**: los 43 países se fijaron antes de ejecutar modelos.
5. **Fase 7 es robustez**, no validación externa.
6. **Fases 3 y 4 son inmutables**: el pipeline solo lee de ellas.
7. **Bootstrap BCa** (2000 iteraciones) para intervalos de confianza en muestras pequeñas.
8. **Validación interna** por CV repetida como diagnóstico auxiliar.

---

## 🚀 ¿Por dónde empiezo?

| Si quieres... | Lee... |
|---|---|
| Entender el proyecto completo de una sentada | `CONTEXTOS/6.ARQUITECTURA_COMPLETA_PROYECTO.md` |
| Ver el plan para las fases que faltan | `CONTEXTOS/7.PLAN_FASES_7_8_Y_CORRECCION_IAPP.md` |
| Ver los resultados país por país | `F5_F8_MVP/FASE6/outputs/country_intelligence/country_q_profile_wide.csv` |
| Ver gráficos y sus explicaciones | `F5_F8_MVP/FASE6/outputs/country_intelligence/figures/` (cada PNG tiene su `.md`) |
| Ver el catálogo completo de outputs | `F5_F8_MVP/FASE6/outputs/INDICE_ARQUITECTONICO_OUTPUTS.md` |
| Entender la elección de modelos | `CONTEXTOS/6.ARQUITECTURA_COMPLETA_PROYECTO.md` §6.5.1.1 |
| Ver el notebook didáctico | `F5_F8_MVP/FASE6/notebooks/06_modeling_AUDITORIA_HUMANA_FASE6_V2_2_VISUAL_DIDACTICO.ipynb` |
| Ver los datos crudos | `FASE3/outputs/Matriz_Madre_Fase3.xlsx` |
| Ejecutar Fase 6 | `cd F5_F8_MVP/FASE6 && python -m src.run_all` |
| Ver el plan original del MVP | `CONTEXTOS/5.PLAN_FASE_MVP_END_TO_END.md` |

---

## ⚙️ Requisitos Técnicos

- **Python** ≥ 3.10
- **Dependencias:** pandas, numpy, scipy, scikit-learn, statsmodels, matplotlib, seaborn, pyyaml, openpyxl
- Instalar: `pip install -e F5_F8_MVP/`

---

## 📈 Estado del Proyecto

| Fase | Estado | Entregable principal |
|---|---|---|
| Fase 1-2: Definición y comprensión | ✅ | Plan de investigación, hipótesis, Q1-Q6 |
| Fase 3: Matriz Madre | ✅ | 199 países × 1,203 columnas, API estable |
| Fase 4: EDA Principal | ✅ | PCA, clustering, taxonomía, decisiones preregistradas |
| Fase 5: Feature Engineering | ✅ | Feature matrix 43 países × 46 vars, contrato metodológico |
| Fase 6.1: Modelado Inferencial | ✅ | 6 modelos (Q1-Q6), bootstrap, resultados |
| Fase 6.2: Country Intelligence | ✅ | 903 perfiles, 38 figuras, 11 country cards, 20 .md descriptivos |
| Fase 7: Robustez | 🔜 | Sensibilidad, baselines, leave-group-out, estabilidad |
| Fase 8: Narrativa | 🔜 | Notebook maestro, informe ejecutivo, recomendaciones |

---

## 📄 Licencia y Citación

Proyecto de investigación académica. Los datos provienen de fuentes públicas internacionales (Oxford Insights, WIPO, OECD, Banco Mundial, IAPP, Microsoft, Anthropic, Stanford HAI).

---

*Última actualización: 2026-05-08 · Fase 6 v2.2 completada*
