# Recopilación de Datos: Impacto de la Regulación de IA en los Ecosistemas de Inteligencia Artificial

## Introducción: ¿Por qué esta recopilación de datos?

### El problema legislativo que origina este estudio

Chile se encuentra en un momento decisivo respecto a la regulación de la inteligencia artificial. La Cámara de Diputados aprobó el proyecto de **Ley Marco de Inteligencia Artificial** (Boletín 16821-19), que actualmente se tramita en la **Comisión de Ciencia, Tecnología e Innovación del Senado**. Esta decisión legislativa tendrá consecuencias directas sobre la capacidad de Chile para atraer inversión, fomentar la adopción de IA en los sectores público y privado, y posicionarse competitivamente en América Latina.

El debate global presenta dos visiones contrapuestas: la regulación como **mecanismo de protección ciudadana** frente a riesgos de la IA (sesgo, privacidad, transparencia), y la regulación como **potencial barrera para la innovación**, la inversión y la adopción tecnológica. La Unión Europea optó por un enfoque basado en riesgos con el EU AI Act (2024), Estados Unidos prefirió un enfoque sectorial y de mercado, y China implementó regulaciones específicas por aplicación. Cada enfoque tiene implicancias distintas en los indicadores de desarrollo del ecosistema de IA — pero **¿cuáles implicancias exactamente, y de qué magnitud?** Esa es la pregunta que este estudio busca responder con evidencia empírica.

### Pregunta principal de investigación

> *¿Existe una asociación estadísticamente significativa entre las características de la regulación de inteligencia artificial de un país y el desarrollo de su ecosistema de IA, después de controlar por factores socioeconómicos e institucionales?*

Esta pregunta se descompone en **cuatro sub-preguntas** que guían directamente la selección de variables y fuentes de datos:

1. **Inversión:** ¿Los países con marcos regulatorios más restrictivos muestran menores niveles de inversión privada en IA?
2. **Adopción:** ¿Qué tipo de enfoque regulatorio (basado en riesgos, sectorial, principios, sin regulación) se asocia con mayores tasas de adopción de IA?
3. **Innovación:** ¿Existe relación entre la presencia y tipo de regulación de IA y los indicadores de innovación (patentes, startups)?
4. **Contenido regulatorio (NLP):** ¿Qué temas dominan en los textos legales de IA a nivel global, y cómo se agrupan temáticamente los países?

### ¿Por qué estas variables? Justificación de cada medición

La recopilación de datos no fue un ejercicio genérico de "juntar datos de IA". Cada variable fue seleccionada porque responde a una necesidad específica del diseño de investigación. A continuación se justifica por qué se recopila cada una:

#### Variables de resultado (Y) — ¿Qué miden y por qué?

| Variable | ¿Qué mide? | ¿Por qué se necesita? |
|---|---|---|
| `ai_readiness_score` | Preparación gubernamental y de infraestructura para la IA (Oxford Insights, 195 países) | Captura la **capacidad integral** de un país para aprovechar la IA. Es la variable Y más comprehensiva y con mayor cobertura geográfica (86/86 países). Permite responder: ¿los países más regulados están más "preparados"? |
| `ai_adoption_rate` | Porcentaje de adopción de IA en la población (Microsoft AI Diffusion Index) | Mide el **uso real de IA** por personas y empresas, no solo la capacidad. Responde directamente la sub-pregunta 2: ¿la regulación afecta cuánta gente adopta IA? |
| `ai_investment_usd_bn_cumulative` | Inversión acumulada en IA por capital de riesgo (Stanford HAI, 2013-2024) | Mide el **flujo de capital privado** hacia el sector de IA. Responde la sub-pregunta 1: ¿la regulación ahuyenta o atrae inversión? La medida acumulada captura la trayectoria histórica de compromiso financiero. |
| `ai_startups_cumulative` | Número acumulado de startups de IA fundadas (Stanford HAI) | Mide la **actividad emprendedora** en IA. Responde la sub-pregunta 3: ¿la regulación inhibe la creación de empresas de IA? Complementa la inversión al capturar el dinamismo del ecosistema innovador. |
| `ai_patents_per100k` | Patentes de IA por cada 100.000 habitantes (Stanford HAI) | Mide la **producción de propiedad intelectual** en IA, normalizada por población. Responde la sub-pregunta 3. Asignada a robustez (N=54) porque su cobertura limitada excluiría 32 países emergentes si fuera principal. |

#### Variables regulatorias (X1) — ¿Qué capturan y por qué?

| Variable | ¿Qué captura? | ¿Por qué se necesita? |
|---|---|---|
| `has_ai_law` | Presencia/ausencia de legislación específica de IA (dummy 0/1) | El predictor más básico: ¿tener una ley de IA hace alguna diferencia medible? Permite la comparación más directa entre países con y sin legislación. |
| `regulatory_approach` | Tipo de enfoque regulatorio (comprehensive, strategy_led, light_touch, none) | Captura la **naturaleza cualitativa** de la regulación. No es lo mismo tener una ley vinculante comprehensiva (EU AI Act) que una estrategia no vinculante. Permite comparar los 4 arquetipos regulatorios globales. |
| `regulatory_intensity` | Escala ordinal 0-5 de intensidad regulatoria | Transforma el enfoque cualitativo en una **escala cuantitativa ordenada**, necesaria para modelos de regresión. Permite estimar si "más regulación" se asocia linealmente con mejores o peores resultados. |
| `year_enacted` | Año de promulgación del primer marco regulatorio | Captura la **antigüedad regulatoria**. Permite controlar si los efectos dependen de cuánto tiempo lleva vigente la regulación (madurez del marco). |
| `enforcement_level` | Nivel de enforcement (autoridad supervisora, sanciones) | Distingue entre **regulación en papel** y **regulación con dientes**. Un país puede tener ley de IA pero sin autoridad que la haga cumplir — esta variable captura esa diferencia crítica. |
| `thematic_coverage` | Número de temas regulatorios cubiertos (privacidad, sesgo, transparencia, etc.) | Mide la **amplitud temática** de la regulación. Permite evaluar si las regulaciones más comprehensivas (que cubren más temas) se asocian con diferentes resultados que las regulaciones enfocadas. |

#### Variables de control (X2) — ¿Por qué son imprescindibles?

Sin controles socioeconómicos, cualquier correlación entre regulación y ecosistema de IA sería espuria. Un país puede tener mejor ecosistema de IA simplemente porque es más rico, más innovador, o tiene mejor infraestructura digital — **no porque regule más o mejor**. Las variables de control permiten aislar el efecto de la regulación:

| Variable | ¿Qué controla? | ¿Por qué es necesaria? |
|---|---|---|
| `gdp_per_capita_ppp` | Nivel de desarrollo económico | Los países ricos invierten más en IA independientemente de su regulación. Sin este control, el efecto de la regulación estaría confundido con el de la riqueza. |
| `internet_penetration` | Infraestructura digital básica | La adopción de IA requiere conectividad. Un país con 20% de penetración de internet no puede tener alta adopción de IA aunque tenga la mejor ley del mundo. |
| `gii_score` | Capacidad de innovación general (WIPO) | Captura el ecosistema de innovación más allá de la IA: calidad de universidades, infraestructura de I+D, sofisticación empresarial. Controla por la "base innovadora" del país. |
| `rd_expenditure` | Inversión pública/privada en I+D (%PIB) | Los países que gastan más en investigación tienen ecosistemas de IA más fuertes por razones estructurales, no regulatorias. |
| `tertiary_education` | Capital humano disponible | La IA requiere talento altamente calificado. La tasa de educación terciaria proxy la disponibilidad de programadores, investigadores, y profesionales técnicos. |
| `government_effectiveness` | Calidad institucional general | Un gobierno que ejecuta bien cualquier política también implementará mejor su regulación de IA. Controla por capacidad estatal (asignada a robustez por cobertura parcial: 63/86). |
| `oecd_member` | Membresía OECD (dummy) | Controla el sesgo estructural de que los países OECD tienden a regular más Y tener mejores ecosistemas simultáneamente. |
| `region` | Región geográfica | Controla por patrones regionales no observados (cultura regulatoria, integración económica, proximidad a hubs tecnológicos). |

### Diseño de la recopilación

La recopilación se diseñó como un **pipeline reproducible** en 3 etapas: (1) extracción de datos crudos desde 7 fuentes internacionales, (2) construcción de 7 masters estandarizados al universo de 86 países, y (3) ensamblaje en un dataset definitivo con jerarquía explícita de variables (principal → extended → robustez). Este diseño garantiza **trazabilidad total** — cada valor en el dataset final puede rastrearse al archivo raw original, script de extracción, y decisión metodológica que lo justifica.

---

## Resumen Ejecutivo

Este documento presenta la sección de recopilación de datos del estudio sobre el impacto de la regulación de inteligencia artificial en los ecosistemas nacionales de IA. Se construyó un dataset transversal (cross-section 2025) de **86 países** a partir de **7 fuentes internacionales independientes**, cubriendo **4 variables de resultado (Y)**, **5 variables regulatorias (X1)** y **10 variables de control y robustez (X2)**. El dataset definitivo contiene **66 columnas** por país, con una **muestra principal de 72 países** que disponen de todas las variables necesarias para el modelo de estimación central, y representación de los **4 grupos regulatorios** definidos en la taxonomía del estudio.

---

## 1. Diseño Muestral

### 1.1 Universo y Criterio de Inclusión

El universo del estudio comprende los **86 países** identificados en el IAPP Global AI Law & Policy Tracker como jurisdicciones con actividad regulatoria documentada en materia de inteligencia artificial, o ausencia documentada de la misma. Este universo fue seleccionado por cumplir un criterio fundamental: incluir **todo el espectro regulatorio observable**, desde países sin ningún marco regulatorio (`no_framework`) hasta aquellos con legislación vinculante comprehensiva (`binding_regulation`).

La decisión de incluir todo el espectro —y no limitarse a países con ley de IA vigente— es metodológicamente necesaria: la pregunta de investigación ("¿existe asociación entre las características de la regulación de IA y el desarrollo del ecosistema de IA?") requiere varianza en la variable de tratamiento. Excluir países sin regulación eliminaría la comparación contrafactual.

### 1.2 Unidad de Análisis

- **Unidad:** País (identificado por código ISO 3166-1 alpha-3)
- **Diseño temporal:** Corte transversal principal (2025), con variables Y referidas a 2024-2025 según la fuente, y controles socioeconómicos dentro de la ventana [2019-2024]
- **No se estima un panel:** La cobertura y comparabilidad temporal entre fuentes no es simétrica para todas las variables Y

### 1.3 Taxonomía Regulatoria

Se definieron **4 grupos regulatorios** a partir de la variable `regulatory_approach` (derivada de la codificación IAPP + EC-OECD):

| Grupo regulatorio | Approches incluidos | N (86 países) | N (muestra principal, 72) |
|---|---|---|---|
| `no_framework` | Países sin marco regulatorio de IA | 5 | 2 |
| `soft_framework` | Enfoque light-touch (principios, guías no vinculantes) | 10 | 9 |
| `strategy_only` | Estrategia nacional sin legislación vinculante | 39 | 34 |
| `binding_regulation` | Legislación vinculante (regulation_focused + comprehensive) | 32 | 27 |

---

## 2. Fuentes de Datos

### 2.1 Inventario de Fuentes

Se integraron 7 fuentes de datos internacionales, cada una cubriendo una dimensión específica del estudio:

| # | Fuente | Institución | Tipo de datos | Variables principales | Archivos raw |
|---|---|---|---|---|---|
| 1 | Stanford AI Index Report 2025 | Stanford HAI | Indicadores cuantitativos de ecosistema IA | Inversión IA, startups IA, patentes IA | 306 archivos CSV |
| 2 | Microsoft AI Economy Institute — AI Diffusion Report | Microsoft Research | Encuesta de adopción GenAI | Tasa de adopción de IA | 4 archivos CSV |
| 3 | Government AI Readiness Index 2025 | Oxford Insights | Índice compuesto de preparación gubernamental | Score de AI Readiness | 15 archivos (CSV + PDF) |
| 4 | WIPO Global Innovation Index 2025 | WIPO | Índice compuesto de innovación | GII Score, región UN | 9 archivos (CSV + XLSX) |
| 5 | World Development Indicators / Worldwide Governance Indicators | World Bank | Indicadores socioeconómicos e institucionales | PIB, internet, I+D, educación, gobernanza | 8 archivos CSV |
| 6 | OECD STI Scoreboard + MSTI | OECD | Indicadores de ciencia, tecnología e innovación | VC proxy, publicaciones IA | 11 archivos CSV |
| 7 | IAPP Global AI Law & Policy Tracker + EC-OECD AI Policy Database | IAPP / OECD | Codificación regulatoria | has_ai_law, regulatory_approach, year_enacted | 4 archivos CSV |

**Tamaño total de datos crudos:** ~107 MB en `data/raw/` distribuidos en 7 directorios.

### 2.2 Detalle por Fuente

#### Fuente 1: Stanford AI Index 2025 (Variables Y)

**Institución:** Stanford Institute for Human-Centered Artificial Intelligence (HAI)  
**Edición:** AI Index Report 2025 (publicado abril 2025)  
**Método de obtención:** Descarga directa de Google Drive público con archivo CSV por figura

Variables extraídas:

| Variable | Figura fuente | Año de referencia | Cobertura | Rol en el estudio |
|---|---|---|---|---|
| `ai_investment_usd_bn_cumulative` | fig_4.3.9 | Acumulado 2013-2024 | 84/86 | Y principal |
| `ai_investment_usd_bn_2024` | fig_4.3.8 | 2024 | 62/86 | Y robustez |
| `ai_startups_cumulative` | fig_4.3.9 | Acumulado hasta 2024 | 84/86 | Y principal |
| `ai_startups_2024` | fig_4.3.8 | 2024 | 57/86 | Y robustez |
| `ai_patents_per100k` | fig_1.2.4 | 2023 | 54/86 | Y robustez |

**Decisiones metodológicas:**
- Se utilizan las figuras 4.3.8 y 4.3.9 como fuentes primarias de inversión por país. La figura 4.3.10, que solo reporta USA, China y EU como agregado, fue descartada (Decision D-002).
- `ai_patents_per100k` fue reclasificada como variable de robustez (no principal) porque solo cubre 54/86 países. Incluirla como Y principal reduciría la muestra en 32 países, mayoritariamente economías emergentes (Decision D-006).
- La variable `ai_vibrancy_score` fue excluida del estudio: la fuente oficial (Stanford HAI Global AI Vibrancy Tool) fue descomisionada y no existe fuente pública reproducible (Decision D-001).

#### Fuente 2: Microsoft AI Economy Institute — AI Diffusion Report (Variable Y)

**Institución:** Microsoft Research, AI Economy Institute (AIEI)  
**Edición:** AI Diffusion Report, datos H1 y H2 2025  
**Método de obtención:** HTML scraping de la página oficial AIEI  
**Universo del reporte:** 147 países a nivel global

| Variable | Período | Cobertura estudio | Rol |
|---|---|---|---|
| `ai_adoption_rate` | H2 2025 (canónico), H1 2025 (fallback) | 75/86 | Y principal |

**Decisiones metodológicas:**
- Se usa H2 2025 como período canónico por ser el más reciente y contemporáneo con el corte transversal 2025 (Decision D-007).
- 11 países del estudio no aparecen en el reporte Microsoft de 147 países: BHR, BLZ, BRB, CYP, EST, ISL, LUX, LVA, MLT, MUS, SYC. Se trata de ausencias estructurales de la fuente, no de errores de extracción.

#### Fuente 3: Oxford Insights — Government AI Readiness Index 2025 (Variable Y)

**Institución:** Oxford Insights  
**Edición:** Government AI Readiness Index 2025 (con panel histórico 2019-2025)  
**Método de obtención:** Descarga directa del archivo oficial + extracción de ediciones históricas en PDF

| Variable | Año | Cobertura | Rol |
|---|---|---|---|
| `ai_readiness_score` | 2025 (canónico), 2024 (fallback) | 86/86 | Y principal |

**Nota:** Es la única variable Y con cobertura completa (86/86). El score se construye sobre pilares de gobierno, tecnología, datos y ética, en escala 0-100.

#### Fuente 4: WIPO Global Innovation Index 2025 (Variable X2)

**Institución:** World Intellectual Property Organization (WIPO)  
**Edición:** GII 2025 (con panel histórico 2020-2025)  
**Método de obtención:** Descarga del XLSX oficial (`tech1.xlsx`)

| Variable | Año | Cobertura | Rol |
|---|---|---|---|
| `gii_score` | 2025 (canónico), 2024 (fallback) | 84/86 | X2 core |
| `region` | 2025 | 86/86 (derivado) | X2 core |

**Ausencias (2/86):** BLZ y TWN no figuran en el ranking WIPO por criterios de cobertura de la propia organización.

#### Fuente 5: World Bank — WDI y WGI (Variables X2)

**Institución:** Banco Mundial  
**Método de obtención:** API oficial World Bank (v2) + archivos de descarga masiva  
**Ventana temporal:** [2019-2024], tomando el valor más reciente disponible por país y variable

| Variable | Indicador WB | Cobertura | Años disponibles | Rol |
|---|---|---|---|---|
| `gdp_per_capita_ppp` | NY.GDP.PCAP.PP.CD | 85/86 | 2023-2024 | X2 core |
| `internet_penetration` | IT.NET.USER.ZS | 85/86 | 2022-2024 | X2 core |
| `rd_expenditure` | GB.XPD.RSDV.GD.ZS | 74/86 | 2019-2024 | X2 extended |
| `tertiary_education` | SE.TER.ENRR | 82/86 | 2019-2024 | X2 extended |
| `government_effectiveness` | GE.EST | 63/86 | 2023 | X2 robustez |

**Decisiones metodológicas:**
- Política temporal: para cada combinación variable × país, se toma el valor más reciente dentro de [2019, 2024]. Valores anteriores a 2019 serían demasiado distantes para un cross-section de regulación vigente (Decision D-003).
- `government_effectiveness` fue reclasificada como variable de robustez (no core) porque solo cubre 63/86 países. Incluirla como core reduciría la muestra principal de 72 a ~48 (Decision D-005).
- TWN: excluido de la API del Banco Mundial por su estatus político. Se mantiene en la muestra con valores NaN documentados para gdp_per_capita_ppp, internet_penetration y gii_score (Decision D-004).

#### Fuente 6: OECD — STI Scoreboard y MSTI (Variables de robustez)

**Institución:** OECD  
**Método de obtención:** API oficial OECD + archivos CSV del STI Scoreboard  
**Alcance:** Países miembros y asociados OECD

| Variable | Descripción | Cobertura | Rol |
|---|---|---|---|
| `ai_investment_vc_proxy` | VC total como % del PIB (proxy de inversión) | 32/86 | X2 robustez |
| `ai_publications_frac` | Fracción de publicaciones IA mundiales | 60/86 | Y robustez |

**Decisiones metodológicas:**
- `ai_investment_vc_proxy` se clasifica como robustez: solo cubre 32 países, mide VC general (no IA-específico), y Stanford fig_4.3.8/9 ya provee inversión IA directa para 84/86 (Decision D-008).

#### Fuente 7: IAPP + EC-OECD AI Policy Database (Variables X1)

**Institución:** International Association of Privacy Professionals (IAPP) + EC-OECD  
**Método de obtención:** Codificación manual a partir del IAPP Tracker + API EC-OECD (case-api.buddyweb.fr)  
**Alcance:** 86 países del estudio (universo completo)

| Variable | Tipo | Cobertura | Rol |
|---|---|---|---|
| `has_ai_law` | Binaria (0/1) | 86/86 | X1 principal |
| `regulatory_approach` | Categórica (5 niveles) | 86/86 | X1 principal |
| `regulatory_intensity` | Ordinal (0-4) | 86/86 | X1 principal |
| `enforcement_level` | Categórica | 86/86 | X1 principal |
| `thematic_coverage` | Numérica (0-7) | 86/86 | X1 principal |
| `year_enacted` | Numérica (año) | 32/86 | Condicional (solo si has_ai_law=1) |
| `regulatory_status_group` | Categórica (4 niveles) | 86/86 | Derivada |

**Cobertura total X1:** Todas las 5 variables X1 principales están disponibles para los 86 países (cobertura 100%). La variable `year_enacted` solo aplica a los 32 países con legislación vinculante.

---

## 3. Pipeline ETL

### 3.1 Arquitectura del Pipeline

El pipeline sigue una arquitectura de **3 pasos** que transforma datos crudos (`data/raw/`) en un dataset analítico único (`data/interim/sample_ready_cross_section.csv`):

```
data/raw/           →  Paso 0: ETL por fuente  →  data/interim/*_individual.csv
                    →  Paso 1: Source Masters   →  data/interim/*_master.csv (7 masters)
                    →  Paso 2: Sample-Ready     →  data/interim/sample_ready_cross_section.csv
```

### 3.2 Paso 0 — ETL por Fuente (raw → interim individuales)

Cada fuente tiene un script dedicado que transforma los archivos crudos en un archivo interim estandarizado con clave `iso3`. Estos scripts realizan limpieza de nombres, mapeo a ISO3, selección temporal y validación básica.

| Script | Fuente | Output | Descripción |
|---|---|---|---|
| `src/consolidate_x1.py` | OECD + IAPP | `x1_consolidated.csv` (902 filas panel) | Reconcilia las dos fuentes X1 en un panel país-año 2013-2025 |
| `src/build_stanford_y.py` | Stanford AI Index | `stanford_ai_patents.csv`, `stanford_ai_investment.csv`, `stanford_ai_startups.csv` | Extrae y estandariza 3 figuras del reporte Stanford |
| `src/expand_wdi.py` | World Bank API | `wdi_all_86.csv` | Descarga indicadores WDI/WGI para los 86 países |
| `src/build_derived_controls.py` | IAPP + WIPO | `derived_controls.csv` | Construye variables derivadas (oecd_member, region, regulatory_status_group) |
| `src/build_vc_proxy.py` | OECD | `ai_investment_vc_proxy.csv` | Construye proxy de inversión VC como % del PIB |

### 3.3 Paso 1 — Source Masters (interim → 7 masters consolidados)

El script `src/build_source_masters.py` genera **7 archivos master**, uno por fuente, cada uno con exactamente **86 filas** (un registro por país del estudio) y metadatos temporales explícitos.

| Master | Variables | Política temporal | Cobertura |
|---|---|---|---|
| `y_stanford_master.csv` | ai_patents_per100k, ai_investment_usd_bn_cumulative, ai_investment_usd_bn_2024, ai_startups_cumulative, ai_startups_2024 | Patentes: 2023; Inversión/Startups: acumulado hasta 2024 | 54-84/86 |
| `y_microsoft_master.csv` | ai_adoption_rate, adoption_period | H2 2025 canónico, H1 2025 fallback | 75/86 |
| `y_oxford_master.csv` | ai_readiness_score | 2025 canónico, 2024 fallback | 86/86 |
| `x2_wipo_master.csv` | gii_score, region_un | 2025 canónico, 2024 fallback | 84/86 |
| `x2_wb_master.csv` | gdp_per_capita_ppp, rd_expenditure, internet_penetration, tertiary_education, government_effectiveness, population, gdp_current_usd | Más reciente en ventana [2019-2024] | 63-85/86 |
| `x1_master.csv` | has_ai_law, regulatory_approach, regulatory_intensity, enforcement_level, thematic_coverage, year_enacted, regulatory_status_group | Snapshot 2025 | 86/86 |
| `oecd_robustness_master.csv` | ai_investment_vc_proxy, ai_publications_frac | Más reciente en ventana [2019-2024] | 32-60/86 |

### 3.4 Paso 2 — Ensamblaje del Dataset Definitivo

El script `src/build_sample_ready.py` fusiona los 7 masters en un único dataset transversal siguiendo una jerarquía formal de variables:

**Modelo PRINCIPAL (N=72):**
- Y: `ai_readiness_score`, `ai_adoption_rate`, `ai_investment_usd_bn_cumulative`, `ai_startups_cumulative`
- X1: `has_ai_law`, `regulatory_approach`, `regulatory_intensity`, `enforcement_level`, `thematic_coverage`
- X2: `gdp_per_capita_ppp`, `internet_penetration`, `gii_score`, `oecd_member`, `region`

**Modelo EXTENDIDO (N=62):**
- Todas las variables del modelo principal + `rd_expenditure`, `tertiary_education`

**Submodelos de ROBUSTEZ (N variable):**
- `ai_patents_per100k` (N≈54), `government_effectiveness` (N≈63), `ai_investment_vc_proxy` (N≈32)
- Estos no se mezclan con el modelo principal; se estiman por separado como análisis de sensibilidad

El script genera flags de completitud (`complete_principal`, `complete_extended`, `complete_strict`) y una matriz de cobertura variable × país para auditoría.

### 3.5 Reproducibilidad

El pipeline completo se ejecuta con:

```bash
source .venv/bin/activate

# Paso 0: ETL por fuente
python src/consolidate_x1.py
python src/build_stanford_y.py
python src/build_derived_controls.py
python src/build_vc_proxy.py

# Paso 1: Source masters
python src/build_source_masters.py

# Paso 2: Sample-ready
python src/build_sample_ready.py
```

**Requisitos:** Python 3.9+, pandas, numpy. Datos raw presentes en `data/raw/`.

---

## 4. Cobertura y Completitud del Dataset

### 4.1 Cobertura por Variable

| Variable | N disponibles | % (de 86) | Tipo | Rol | Fuente |
|---|---|---|---|---|---|
| `ai_readiness_score` | 86 | 100.0% | Numérica continua | Y principal | Oxford Insights 2025 |
| `has_ai_law` | 86 | 100.0% | Binaria | X1 principal | IAPP |
| `regulatory_approach` | 86 | 100.0% | Categórica | X1 principal | IAPP |
| `regulatory_intensity` | 86 | 100.0% | Ordinal (0-4) | X1 principal | IAPP |
| `enforcement_level` | 86 | 100.0% | Categórica | X1 principal | IAPP |
| `thematic_coverage` | 86 | 100.0% | Numérica (0-7) | X1 principal | IAPP |
| `oecd_member` | 86 | 100.0% | Binaria | X2 core | Derivada |
| `region` | 86 | 100.0% | Categórica (7 regiones) | X2 core | WIPO/Derivada |
| `gdp_per_capita_ppp` | 85 | 98.8% | Numérica continua | X2 core | World Bank WDI |
| `internet_penetration` | 85 | 98.8% | Numérica continua | X2 core | World Bank WDI |
| `ai_investment_usd_bn_cumulative` | 84 | 97.7% | Numérica continua | Y principal | Stanford fig_4.3.9 |
| `ai_startups_cumulative` | 84 | 97.7% | Numérica continua | Y principal | Stanford fig_4.3.9 |
| `gii_score` | 84 | 97.7% | Numérica continua | X2 core | WIPO GII 2025 |
| `tertiary_education` | 82 | 95.3% | Numérica continua | X2 extended | World Bank WDI |
| `ai_adoption_rate` | 75 | 87.2% | Numérica continua | Y principal | Microsoft AIEI H2 2025 |
| `rd_expenditure` | 74 | 86.0% | Numérica continua | X2 extended | World Bank WDI |
| `government_effectiveness` | 63 | 73.3% | Numérica continua | X2 robustez | World Bank WGI |
| `ai_publications_frac` | 60 | 69.8% | Numérica continua | Y robustez | OECD STI |
| `ai_patents_per100k` | 54 | 62.8% | Numérica continua | Y robustez | Stanford fig_1.2.4 |
| `ai_investment_vc_proxy` | 32 | 37.2% | Numérica continua | X2 robustez | OECD MSTI |

### 4.2 Muestras por Nivel de Completitud

| Nivel | Definición | N países | % del universo |
|---|---|---|---|
| **PRINCIPAL** | Todas las Y principales + X1 + X2 core sin valores faltantes | **72** | 83.7% |
| **EXTENDED** | PRINCIPAL + rd_expenditure + tertiary_education | **62** | 72.1% |
| **STRICT** | EXTENDED + todas las variables de robustez | **46** | 53.5% |
| Países con las 19 variables clave completas | Incluye todas las de STRICT más vc_proxy | **27** | 31.4% |

### 4.3 Representación Regulatoria por Nivel de Muestra

| Grupo regulatorio | Universo (86) | PRINCIPAL (72) | EXTENDED (62) | STRICT (46) |
|---|---|---|---|---|
| `binding_regulation` | 32 | 27 | 26 | 24 |
| `strategy_only` | 39 | 34 | 29 | 19 |
| `soft_framework` | 10 | 9 | 7 | 3 |
| `no_framework` | 5 | 2 | 0 | 0 |

**Nota crítica:** La muestra PRINCIPAL mantiene representación de los 4 grupos regulatorios, lo cual es condición necesaria para estimar comparaciones between-group. Las muestras EXTENDED y STRICT pierden el grupo `no_framework`, por lo que los análisis en esas muestras deben limitarse a 3 grupos.

### 4.4 Distribución Geográfica

| Región | Universo (86) | PRINCIPAL (72) | % retenido |
|---|---|---|---|
| Europa | 34 | 29 | 85.3% |
| Sudeste Asiático, Asia Oriental y Oceanía | 13 | 12 | 92.3% |
| América Latina y el Caribe | 12 | 10 | 83.3% |
| Norte de África y Asia Occidental | 12 | 9 | 75.0% |
| África Subsahariana | 8 | 6 | 75.0% |
| Asia Central y del Sur | 5 | 4 | 80.0% |
| América del Norte | 2 | 2 | 100.0% |

**Membresía OECD:**
- Universo (86): 38 OECD, 48 no-OECD
- Muestra PRINCIPAL (72): 34 OECD, 38 no-OECD (proporción preservada)

### 4.5 Estadísticos Descriptivos de Variables Y

| Variable | N | Mín | Máx | Media | Mediana | Desv. Est. |
|---|---|---|---|---|---|---|
| `ai_readiness_score` | 86 | 22.68 | 88.36 | 59.27 | 60.50 | 13.50 |
| `ai_adoption_rate` (%) | 75 | 6.60 | 64.00 | 23.56 | 22.40 | 12.20 |
| `ai_investment_usd_bn_cumulative` | 84 | 0.00 | 470.92 | 8.98 | 0.22 | 52.78 |
| `ai_startups_cumulative` | 84 | 1.00 | 6,956.00 | 171.63 | 13.00 | 781.81 |

**Observación:** Las variables de inversión y startups presentan distribuciones altamente asimétricas (sesgo positivo), con concentración en un grupo reducido de países (USA, CHN, GBR). Se anticipa la necesidad de transformaciones logarítmicas en la fase de modelamiento.

---

## 5. Inventario Completo de Países

### 5.1 Tabla de 86 Países con Variables Disponibles

La siguiente tabla detalla cada país del estudio con su clasificación regulatoria, nivel de completitud alcanzado, número de variables disponibles (de 19 variables clave) y las variables faltantes específicas.

| ISO3 | País | Grupo regulatorio | Nivel alcanzado | Variables (de 19) | Variables faltantes |
|---|---|---|---|---|---|
| ARE | Emiratos Árabes Unidos | strategy_only | EXTENDED | 17 | ai_patents_per100k, ai_investment_vc_proxy |
| ARG | Argentina | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| ARM | Armenia | soft_framework | EXTENDED | 16 | ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| AUS | Australia | strategy_only | STRICT | 19 | NINGUNA |
| AUT | Austria | binding_regulation | STRICT | 19 | NINGUNA |
| BEL | Bélgica | binding_regulation | STRICT | 19 | NINGUNA |
| BGD | Bangladesh | strategy_only | PRINCIPAL | 15 | rd_expenditure, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| BGR | Bulgaria | binding_regulation | STRICT | 19 | NINGUNA |
| BHR | Bahréin | strategy_only | PARCIAL | 15 | ai_adoption_rate, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| BLR | Bielorrusia | soft_framework | EXTENDED | 16 | ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| BLZ | Belice | no_framework | PARCIAL | 13 | ai_adoption_rate, gii_score, rd_expenditure, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| BRA | Brasil | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| BRB | Barbados | no_framework | PARCIAL | 14 | ai_adoption_rate, rd_expenditure, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| CAN | Canadá | strategy_only | STRICT | 19 | NINGUNA |
| CHE | Suiza | soft_framework | STRICT | 19 | NINGUNA |
| CHL | Chile | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| CHN | China | binding_regulation | STRICT | 18 | ai_investment_vc_proxy |
| CMR | Camerún | no_framework | PRINCIPAL | 16 | rd_expenditure, ai_patents_per100k, ai_investment_vc_proxy |
| COL | Colombia | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| CRI | Costa Rica | strategy_only | EXTENDED | 17 | ai_patents_per100k, ai_investment_vc_proxy |
| CYP | Chipre | binding_regulation | PARCIAL | 16 | ai_adoption_rate, ai_patents_per100k, ai_investment_vc_proxy |
| CZE | Chequia | binding_regulation | STRICT | 19 | NINGUNA |
| DEU | Alemania | binding_regulation | STRICT | 19 | NINGUNA |
| DNK | Dinamarca | binding_regulation | STRICT | 19 | NINGUNA |
| ECU | Ecuador | soft_framework | PRINCIPAL | 15 | rd_expenditure, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| EGY | Egipto | strategy_only | EXTENDED | 17 | ai_patents_per100k, ai_investment_vc_proxy |
| ESP | España | binding_regulation | STRICT | 19 | NINGUNA |
| EST | Estonia | binding_regulation | PARCIAL | 18 | ai_adoption_rate |
| FIN | Finlandia | binding_regulation | STRICT | 19 | NINGUNA |
| FRA | Francia | binding_regulation | STRICT | 19 | NINGUNA |
| GBR | Reino Unido | strategy_only | STRICT | 19 | NINGUNA |
| GHA | Ghana | strategy_only | PRINCIPAL | 15 | rd_expenditure, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| GRC | Grecia | binding_regulation | STRICT | 19 | NINGUNA |
| HRV | Croacia | binding_regulation | EXTENDED | 18 | ai_patents_per100k |
| HUN | Hungría | binding_regulation | STRICT | 19 | NINGUNA |
| IDN | Indonesia | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| IND | India | soft_framework | STRICT | 18 | ai_investment_vc_proxy |
| IRL | Irlanda | binding_regulation | STRICT | 19 | NINGUNA |
| ISL | Islandia | soft_framework | PARCIAL | 16 | ai_adoption_rate, ai_patents_per100k, ai_investment_vc_proxy |
| ISR | Israel | soft_framework | STRICT | 19 | NINGUNA |
| ITA | Italia | binding_regulation | STRICT | 19 | NINGUNA |
| JOR | Jordania | strategy_only | PRINCIPAL | 17 | rd_expenditure, ai_investment_vc_proxy |
| JPN | Japón | binding_regulation | STRICT | 18 | ai_investment_vc_proxy |
| KAZ | Kazajistán | strategy_only | EXTENDED | 17 | ai_patents_per100k, ai_investment_vc_proxy |
| KEN | Kenia | strategy_only | EXTENDED | 16 | ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| KOR | Corea del Sur | binding_regulation | STRICT | 18 | ai_investment_vc_proxy |
| LBN | Líbano | no_framework | PRINCIPAL | 15 | rd_expenditure, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| LKA | Sri Lanka | soft_framework | EXTENDED | 16 | ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| LTU | Lituania | binding_regulation | STRICT | 19 | NINGUNA |
| LUX | Luxemburgo | binding_regulation | PARCIAL | 18 | ai_adoption_rate |
| LVA | Letonia | binding_regulation | PARCIAL | 18 | ai_adoption_rate |
| MAR | Marruecos | strategy_only | PARCIAL | 14 | ai_investment_usd_bn_cumulative, ai_startups_cumulative, rd_expenditure, government_effectiveness, ai_investment_vc_proxy |
| MEX | México | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| MLT | Malta | binding_regulation | PARCIAL | 15 | ai_adoption_rate, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| MNG | Mongolia | soft_framework | EXTENDED | 16 | ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| MUS | Mauricio | strategy_only | PARCIAL | 15 | ai_adoption_rate, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| MYS | Malasia | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| NGA | Nigeria | strategy_only | PRINCIPAL | 16 | tertiary_education, ai_patents_per100k, ai_investment_vc_proxy |
| NLD | Países Bajos | binding_regulation | STRICT | 19 | NINGUNA |
| NOR | Noruega | strategy_only | STRICT | 19 | NINGUNA |
| NZL | Nueva Zelanda | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| PAK | Pakistán | strategy_only | PARCIAL | 15 | ai_investment_usd_bn_cumulative, ai_startups_cumulative, government_effectiveness, ai_investment_vc_proxy |
| PAN | Panamá | strategy_only | EXTENDED | 16 | ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| PER | Perú | binding_regulation | PRINCIPAL | 16 | tertiary_education, ai_patents_per100k, ai_investment_vc_proxy |
| PHL | Filipinas | strategy_only | PRINCIPAL | 17 | rd_expenditure, ai_investment_vc_proxy |
| POL | Polonia | binding_regulation | STRICT | 19 | NINGUNA |
| PRT | Portugal | binding_regulation | STRICT | 19 | NINGUNA |
| ROU | Rumania | binding_regulation | STRICT | 19 | NINGUNA |
| RUS | Rusia | binding_regulation | STRICT | 18 | ai_investment_vc_proxy |
| SAU | Arabia Saudita | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| SGP | Singapur | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| SRB | Serbia | strategy_only | EXTENDED | 16 | ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| SVK | Eslovaquia | binding_regulation | EXTENDED | 18 | government_effectiveness |
| SVN | Eslovenia | binding_regulation | STRICT | 19 | NINGUNA |
| SWE | Suecia | binding_regulation | STRICT | 19 | NINGUNA |
| SYC | Seychelles | no_framework | PARCIAL | 14 | ai_adoption_rate, rd_expenditure, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| THA | Tailandia | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| TUN | Túnez | strategy_only | EXTENDED | 17 | ai_patents_per100k, ai_investment_vc_proxy |
| TUR | Turquía | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| TWN | Taiwán | strategy_only | PARCIAL | 11 | gdp_per_capita_ppp, internet_penetration, gii_score, rd_expenditure, tertiary_education, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| UGA | Uganda | soft_framework | PRINCIPAL | 15 | tertiary_education, ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| UKR | Ucrania | strategy_only | EXTENDED | 16 | ai_patents_per100k, government_effectiveness, ai_investment_vc_proxy |
| URY | Uruguay | strategy_only | EXTENDED | 17 | ai_patents_per100k, ai_investment_vc_proxy |
| USA | Estados Unidos | strategy_only | STRICT | 19 | NINGUNA |
| VNM | Vietnam | strategy_only | STRICT | 18 | ai_investment_vc_proxy |
| ZAF | Sudáfrica | strategy_only | STRICT | 18 | ai_investment_vc_proxy |

### 5.2 Países con Cobertura Completa (27 países — todas las 19 variables clave)

Los siguientes 27 países disponen de las 19 variables clave sin ningún valor faltante, incluyendo las variables de robustez:

| ISO3 | País | Grupo regulatorio |
|---|---|---|
| AUS | Australia | strategy_only |
| AUT | Austria | binding_regulation |
| BEL | Bélgica | binding_regulation |
| BGR | Bulgaria | binding_regulation |
| CAN | Canadá | strategy_only |
| CHE | Suiza | soft_framework |
| CZE | Chequia | binding_regulation |
| DEU | Alemania | binding_regulation |
| DNK | Dinamarca | binding_regulation |
| ESP | España | binding_regulation |
| FIN | Finlandia | binding_regulation |
| FRA | Francia | binding_regulation |
| GBR | Reino Unido | strategy_only |
| GRC | Grecia | binding_regulation |
| HUN | Hungría | binding_regulation |
| IRL | Irlanda | binding_regulation |
| ISR | Israel | soft_framework |
| ITA | Italia | binding_regulation |
| LTU | Lituania | binding_regulation |
| NLD | Países Bajos | binding_regulation |
| NOR | Noruega | strategy_only |
| POL | Polonia | binding_regulation |
| PRT | Portugal | binding_regulation |
| ROU | Rumania | binding_regulation |
| SVN | Eslovenia | binding_regulation |
| SWE | Suecia | binding_regulation |
| USA | Estados Unidos | strategy_only |

### 5.3 Países Parciales (14 países — excluidos de la muestra principal)

Los siguientes 14 países no alcanzan el nivel PRINCIPAL por presentar al menos una variable Y principal o X2 core faltante:

| ISO3 | País | Grupo | Variable(s) Y faltante(s) | Variable(s) X2 faltante(s) | Causa |
|---|---|---|---|---|---|
| BHR | Bahréin | strategy_only | ai_adoption_rate | — | Ausencia estructural Microsoft AIEI |
| BLZ | Belice | no_framework | ai_adoption_rate | gii_score | Ausencia estructural Microsoft + WIPO |
| BRB | Barbados | no_framework | ai_adoption_rate | — | Ausencia estructural Microsoft AIEI |
| CYP | Chipre | binding_regulation | ai_adoption_rate | — | Ausencia estructural Microsoft AIEI |
| EST | Estonia | binding_regulation | ai_adoption_rate | — | Ausencia estructural Microsoft AIEI |
| ISL | Islandia | soft_framework | ai_adoption_rate | — | Ausencia estructural Microsoft AIEI |
| LUX | Luxemburgo | binding_regulation | ai_adoption_rate | — | Ausencia estructural Microsoft AIEI |
| LVA | Letonia | binding_regulation | ai_adoption_rate | — | Ausencia estructural Microsoft AIEI |
| MAR | Marruecos | strategy_only | ai_investment, ai_startups | — | Ausencia en Stanford fig_4.3.8/9 |
| MLT | Malta | binding_regulation | ai_adoption_rate | — | Ausencia estructural Microsoft AIEI |
| MUS | Mauricio | strategy_only | ai_adoption_rate | — | Ausencia estructural Microsoft AIEI |
| PAK | Pakistán | strategy_only | ai_investment, ai_startups | — | Ausencia en Stanford fig_4.3.8/9 |
| SYC | Seychelles | no_framework | ai_adoption_rate | — | Ausencia estructural Microsoft AIEI |
| TWN | Taiwán | strategy_only | — | gdp_per_capita_ppp, internet_penetration, gii_score | Exclusión World Bank/WIPO por estatus político |

**Patrones de ausencia:**
- **11 países** faltan por `ai_adoption_rate`: son los 11 países del estudio no cubiertos por el reporte Microsoft AIEI de 147 países. Esta es una limitación estructural de la fuente.
- **2 países** (MAR, PAK) faltan por inversión/startups: no figuran en las figuras Stanford 4.3.8/9.
- **1 país** (TWN) falta por controles socioeconómicos: excluido sistemáticamente de World Bank y WIPO por su estatus político.

---

## 6. Metadatos Temporales

Cada variable del dataset tiene un año de referencia trazable:

| Variable | Fuente | Rango de años en el dataset | Política |
|---|---|---|---|
| `ai_readiness_score` | Oxford Insights | 2025 (uniforme) | Edición 2025 |
| `ai_adoption_rate` | Microsoft AIEI | H2 2025 (uniforme) | H2 canónico, H1 fallback |
| `ai_investment_usd_bn_cumulative` | Stanford | 2024 (uniforme) | Acumulado 2013-2024 |
| `ai_startups_cumulative` | Stanford | 2024 (uniforme) | Acumulado hasta 2024 |
| `ai_patents_per100k` | Stanford | 2023 (uniforme) | Edición 2023 del reporte |
| `gii_score` | WIPO GII | 2025 (uniforme) | Edición 2025 |
| `gdp_per_capita_ppp` | World Bank WDI | 2023-2024 | Más reciente en [2019-2024] |
| `rd_expenditure` | World Bank WDI | 2019-2024 | Más reciente en [2019-2024] |
| `internet_penetration` | World Bank WDI | 2022-2024 | Más reciente en [2019-2024] |
| `tertiary_education` | World Bank WDI | 2019-2024 | Más reciente en [2019-2024] |
| `government_effectiveness` | World Bank WGI | 2023 (uniforme) | Más reciente en [2019-2024] |
| `ai_investment_vc_proxy` | OECD MSTI | 2019-2024 | Más reciente en [2019-2024] |
| `ai_publications_frac` | OECD STI | 2023 (uniforme) | Más reciente disponible |

---

## 7. Decisiones Metodológicas Formales

Las siguientes decisiones fueron tomadas durante la recopilación y están documentadas en el registro formal `DATA_DECISIONS_LOG.md`:

| Código | Decisión | Justificación | Impacto |
|---|---|---|---|
| D-001 | Exclusión de `ai_vibrancy_score` | Fuente oficial descomisionada; alternativa tras paywall | Compensado por outcomes observables directos |
| D-002 | Stanford fig_4.3.8/9 como fuente primaria de inversión | fig_4.3.10 solo reporta USA/CHN/EU agregado | Cobertura de 84/86 países |
| D-003 | Ventana temporal [2019-2024] para controles WDI | Coherencia con cross-section 2025 | Reduce ligeramente cobertura de rd_expenditure |
| D-004 | TWN con excepciones documentadas | Relevante para análisis regulatorio pese a exclusión de WB/WIPO | Queda como observación incompleta |
| D-005 | `government_effectiveness` → robustez | Solo 63/86; incluirla como core reduciría muestra a ~48 | Modelo principal no controla por gobernanza |
| D-006 | `ai_patents_per100k` → robustez | Solo 54/86; eliminaría 32 países emergentes | Innovación se mide con startups como Y principal |
| D-007 | Microsoft H2 2025 canónico | Más reciente y contemporáneo | 75/86 con dato canónico |
| D-008 | `ai_investment_vc_proxy` → robustez | 32/86, mide VC general (no IA-específico) | Stanford ya provee inversión IA directa |
| D-009 | Muestra principal como cross-section 2025 | Cobertura temporal no simétrica entre fuentes Y | Panel disponible solo como extensión |
| D-010 | Taxonomía regulatoria de 4 niveles | Tamaños de grupo suficientes para inferencia | Colapsa 5 niveles IAPP/OECD en 4 |
| D-011 | Inclusión de todo el espectro regulatorio | Necesario para varianza en variable de tratamiento | Permite comparación between-group |

---

## 8. Archivos del Dataset

### 8.1 Estructura de Directorios

```
data/
├── raw/                              ← Datos crudos originales (no modificados)
│   ├── IAPP/                         (4 archivos, 120 KB)
│   ├── Microsoft/                    (4 archivos, 44 KB)
│   ├── OECD/                         (11 archivos, 3,864 KB)
│   ├── Oxford Insights/              (15 archivos, 21,041 KB)
│   ├── STANFORD AI INDEX 25/         (306 archivos, 22,366 KB)
│   ├── WIPO Global Innovation Index/ (9 archivos, 57,823 KB)
│   └── World Bank WDI/              (8 archivos, 2,491 KB)
│
├── interim/                          ← Archivos procesados por el pipeline
│   ├── x1_consolidated.csv           (panel 2013-2025, 902 filas)
│   ├── y_stanford_master.csv         (86 filas)
│   ├── y_microsoft_master.csv        (86 filas)
│   ├── y_oxford_master.csv           (86 filas)
│   ├── x2_wipo_master.csv            (86 filas)
│   ├── x2_wb_master.csv              (86 filas)
│   ├── x1_master.csv                 (86 filas)
│   ├── oecd_robustness_master.csv    (86 filas)
│   ├── sample_ready_cross_section.csv ← DATASET DEFINITIVO (86 × 66)
│   └── coverage_matrix.csv           (matriz de auditoría)
│
└── processed/                        ← (Reservado para fase de limpieza)
```

### 8.2 Dataset Definitivo

**Archivo:** `data/interim/sample_ready_cross_section.csv`  
**Dimensiones:** 86 filas × 66 columnas  
**Clave primaria:** `iso3` (ISO 3166-1 alpha-3, sin duplicados)

Estructura de columnas:
- **Identificación:** iso3
- **Variables regulatorias (X1):** has_ai_law, regulatory_approach, regulatory_intensity, year_enacted, enforcement_level, thematic_coverage, regulatory_status_group, x1_source
- **Variables de ecosistema IA (Y):** ai_readiness_score, ai_adoption_rate, ai_investment_usd_bn_cumulative, ai_investment_usd_bn_2024, ai_startups_cumulative, ai_startups_2024, ai_patents_per100k, ai_publications_frac, ai_investment_vc_proxy
- **Variables de control (X2):** gdp_per_capita_ppp, internet_penetration, gii_score, oecd_member, region, rd_expenditure, tertiary_education, government_effectiveness, population, gdp_current_usd
- **Metadatos temporales:** *_year para cada variable con ventana temporal
- **Flags de completitud:** complete_principal, complete_extended, complete_strict
- **Indicadores de disponibilidad:** has_* (binarios por variable para auditoría)

---

## 9. Validación y Calidad

### 9.1 Verificaciones Realizadas

1. **Unicidad:** 86 países únicos sin duplicados en `iso3`
2. **Integridad referencial:** Todos los 86 ISO3 provienen del IAPP Tracker verificado
3. **Completitud declarada:** Los flags `complete_principal/extended/strict` coinciden con la presencia efectiva de valores no nulos en las variables correspondientes
4. **Representación regulatoria:** Los 4 grupos regulatorios están presentes en la muestra principal (binding=27, strategy=34, soft=9, no_framework=2)
5. **Coherencia temporal:** Todas las variables respetan la ventana [2019-2025] declarada en las decisiones metodológicas
6. **Spot-checks de ancla:** Validaciones manuales de valores conocidos (e.g., USA ai_readiness_score top tier, CHN con binding_regulation, BLZ sin marco regulatorio)
7. **No hay valores negativos** en variables que no los admiten (inversión, startups, readiness)
8. **Reproducibilidad:** El pipeline completo genera outputs idénticos desde los archivos raw

### 9.2 Limitaciones Conocidas

1. **Sesgo de disponibilidad:** Las variables de robustez (patentes, VC proxy, gobernanza) tienen cobertura parcial sesgada hacia países OECD y economías avanzadas. Esto implica que los análisis de robustez se basan en muestras con menor representación de economías emergentes.

2. **Asimetría temporal entre fuentes Y:** `ai_readiness_score` (2025), `ai_adoption_rate` (H2 2025), `ai_investment` (acumulado hasta 2024), `ai_patents` (2023). No todas miden el mismo punto temporal exacto.

3. **TWN como caso especial:** Taiwán tiene datos regulatorios y de adopción/readiness, pero carece de controles socioeconómicos por exclusión sistemática de organismos internacionales. Se mantiene en el universo (86) pero no en la muestra principal (72).

4. **Concentración en `ai_investment`:** El 73.2% de la inversión acumulada global en IA se concentra en 3 países (USA, CHN, GBR), lo que genera una distribución altamente asimétrica.

5. **X1 basado en fuente única:** Todas las variables regulatorias provienen de la codificación IAPP (fuente autoritativa pero sin triangulación con otra fuente independiente comparable).

---

## 10. Conclusión: ¿Está lista la fase de recopilación?

### 10.1 Evaluación cuantitativa de la recopilación

La fase de recopilación produjo un dataset transversal de **86 países × 66 columnas** a partir de **7 fuentes internacionales independientes**. Los siguientes indicadores cuantitativos permiten evaluar objetivamente si el dataset es suficiente para iniciar la fase de limpieza y modelamiento:

**Cobertura del dataset:**

| Nivel de completitud | N países | % del universo (86) | Criterio |
|---|---|---|---|
| Universo total | 86 | 100% | Todos los países con actividad regulatoria documentada (IAPP) |
| **Muestra principal** | **72** | **83.7%** | Todas las Y principales + X2 core completas |
| Muestra extended | 62 | 72.1% | Principal + rd_expenditure |
| Muestra strict | 46 | 53.5% | Extended + government_effectiveness |

**Cobertura por variable Y en la muestra principal (N=72):**

| Variable Y | Cobertura principal | Cobertura total (86) | Rol |
|---|---|---|---|
| `ai_readiness_score` | 72/72 (100%) | 86/86 (100%) | Y principal — preparación IA |
| `ai_adoption_rate` | 72/72 (100%) | 75/86 (87.2%) | Y principal — uso real |
| `ai_investment_usd_bn_cumulative` | 72/72 (100%) | 84/86 (97.7%) | Y principal — capital privado |
| `ai_startups_cumulative` | 72/72 (100%) | 84/86 (97.7%) | Y principal — emprendimiento IA |
| `ai_patents_per100k` | 49/72 (68.1%) | 54/86 (62.8%) | Robustez — propiedad intelectual |

**Cobertura por variable X2 de control:**

| Variable X2 | Cobertura (86) | Rol |
|---|---|---|
| `gdp_per_capita_ppp` | 85/86 (98.8%) | Core — desarrollo económico |
| `internet_penetration` | 85/86 (98.8%) | Core — infraestructura digital |
| `gii_score` | 84/86 (97.7%) | Core — capacidad de innovación |
| `oecd_member` | 86/86 (100%) | Core — membresía OECD |
| `region` | 86/86 (100%) | Core — control geográfico |
| `tertiary_education` | 82/86 (95.3%) | Extended — capital humano |
| `rd_expenditure` | 74/86 (86.0%) | Extended — inversión I+D |
| `government_effectiveness` | 63/86 (73.3%) | Robustez — calidad institucional |

**Representación de los 4 grupos regulatorios (muestra principal, N=72):**

| Grupo regulatorio | N | % de la muestra principal |
|---|---|---|
| `strategy_led` | 34 | 47.2% |
| `comprehensive` (binding) | 27 | 37.5% |
| `light_touch` (soft) | 9 | 12.5% |
| `none` (no_framework) | 2 | 2.8% |

Los 4 grupos están representados. El grupo `none` tiene N=2 en la muestra principal, lo que es un mínimo aceptable como referencia contrafactual en modelos con variable dummy, aunque limita la inferencia específica sobre este grupo.

**Distribución geográfica (muestra principal, N=72):**

| Región | N |
|---|---|
| Europa | 29 |
| SE Asia, E Asia y Oceanía | 12 |
| América Latina y el Caribe | 10 |
| Norte de África y Asia Occidental | 9 |
| África Subsahariana | 6 |
| Asia Central y del Sur | 4 |
| Norteamérica | 2 |

Las 7 regiones están representadas, con presencia significativa tanto de economías avanzadas como de países en desarrollo.

### 10.2 Estadísticas descriptivas de las variables Y (muestra principal)

| Variable | N | Media | Mediana | Mín | Máx | Observación |
|---|---|---|---|---|---|---|
| `ai_readiness_score` | 72 | 60.89 | 60.90 | 32.47 | 88.36 | Distribución simétrica, rango amplio |
| `ai_adoption_rate` (%) | 72 | 23.86 | 22.45 | 6.60 | 64.00 | Varianza suficiente para regresión |
| `ai_investment_usd_bn` | 72 | 10.45 | 0.33 | 0.00 | 470.92 | Altamente asimétrica — requiere log-transform |
| `ai_startups_cumulative` | 72 | 198.75 | 15.00 | 1.00 | 6956.00 | Altamente asimétrica — requiere log-transform |
| `ai_patents_per100k` | 49 | 0.85 | 0.08 | 0.00 | 17.27 | Solo robustez (N=49 en principal) |

Todas las variables Y presentan **varianza suficiente** para estimar modelos de regresión. Las variables de inversión y startups requieren transformación logarítmica por su alta asimetría, lo cual se abordará en la fase de limpieza.

### 10.3 Enlace con las preguntas de investigación

La pregunta principal del estudio es: *¿Existe una asociación estadísticamente significativa entre las características de la regulación de IA de un país y el desarrollo de su ecosistema de IA, después de controlar por factores socioeconómicos e institucionales?*

A continuación se evalúa la disponibilidad de datos para cada sub-pregunta:

**Sub-pregunta 1 — Inversión:** *¿Los marcos regulatorios más restrictivos se asocian con menores niveles de inversión privada en IA?*
- **Variable Y disponible:** `ai_investment_usd_bn_cumulative` — 72/72 en muestra principal (100%)
- **Variables X1:** `regulatory_approach`, `regulatory_intensity` — 72/72 (100%)
- **Controles X2:** GDP, internet, GII — todos >97% cobertura
- **Veredicto:** ✅ Datos suficientes para estimar modelo de inversión

**Sub-pregunta 2 — Adopción:** *¿Qué enfoque regulatorio se asocia con mayores tasas de adopción de IA?*
- **Variable Y disponible:** `ai_adoption_rate` — 72/72 en muestra principal (100%)
- **Variables X1:** `regulatory_approach` con 4 niveles representados
- **Controles X2:** Completos
- **Veredicto:** ✅ Datos suficientes para comparar adopción entre grupos regulatorios

**Sub-pregunta 3 — Innovación:** *¿Existe relación entre regulación de IA e indicadores de innovación?*
- **Variables Y disponibles:** `ai_startups_cumulative` (72/72, 100%), `ai_patents_per100k` (49/72, robustez)
- **Estrategia:** Startups como Y principal; patentes como análisis de robustez
- **Veredicto:** ✅ Datos suficientes con startups como indicador principal de innovación

**Sub-pregunta 4 — Contenido regulatorio (NLP):** *¿Qué temas dominan en los textos legales de IA?*
- **Datos requeridos:** Textos completos de leyes de IA para 15-20 países
- **Estado:** Pendiente — esta sub-pregunta se aborda en una rama separada del pipeline (fase NLP, notebook `05_nlp.ipynb`)
- **Veredicto:** ⏳ No aplica a esta fase de recopilación cuantitativa

### 10.4 Chile en el dataset

Chile (`CHL`) está presente en el dataset con el siguiente perfil:

| Indicador | Valor | Contexto |
|---|---|---|
| `regulatory_approach` | strategy_led | Estrategia nacional, Boletín 16821-19 en trámite |
| `regulatory_intensity` | 4 | Nivel de intensidad regulatoria medio-alto |
| `ai_readiness_score` | 59.30 | Cercano a la mediana global (60.90) |
| `ai_adoption_rate` | 20.8% | Ligeramente por debajo de la mediana (22.45%) |
| `ai_investment_usd_bn` | 0.68 | Por encima de la mediana (0.33) |
| `ai_startups_cumulative` | 17 | Cercano a la mediana (15) |
| `complete_principal` | ✅ | Incluido en la muestra principal |
| `complete_strict` | ✅ | Incluido incluso en la muestra más restrictiva |

Chile dispone de **todas las variables** necesarias para el análisis (18/19, faltando únicamente `ai_investment_vc_proxy`, variable de robustez OECD). Esto significa que el dataset permite posicionar a Chile dentro de los modelos estimados y generar inferencias directamente aplicables a la decisión legislativa sobre el Boletín 16821-19.

### 10.5 Fortalezas del dataset

1. **Cobertura geográfica amplia:** 7 regiones, 72 países principales, equilibrio entre economías OECD (34 en universo) y no-OECD (38 en universo)
2. **Espectro regulatorio completo:** Los 4 arquetipos regulatorios globales representados — desde ausencia de marco hasta legislación comprehensiva
3. **Múltiples dimensiones de resultado:** 4 variables Y principales que cubren preparación, adopción, inversión y emprendimiento en IA
4. **Trazabilidad total:** Cada variable tiene fuente documentada, año de referencia, script de extracción y decisión metodológica formal en `DATA_DECISIONS_LOG.md`
5. **Jerarquía explícita de variables:** Clasificación principal/extended/robustez con N y representación calculados para cada nivel
6. **Reproducibilidad:** Pipeline de 3 etapas (8 scripts) ejecutable desde archivos raw, con outputs idénticos

### 10.6 Limitaciones y riesgos para las fases siguientes

1. **Grupo `none` con N=2:** El grupo sin marco regulatorio tiene solo 2 países en la muestra principal (Belice fue excluido por variables faltantes). Esto limita la inferencia estadística sobre este grupo específico, aunque permite mantenerlo como referencia categórica.
2. **Asimetría en inversión y startups:** Las distribuciones altamente concentradas (USA concentra ~62% de la inversión global en la muestra) requieren transformación logarítmica y posiblemente modelos robustos a outliers.
3. **Variables de robustez con cobertura parcial:** `ai_patents_per100k` (54/86), `government_effectiveness` (63/86), `ai_investment_vc_proxy` (32/86) — los análisis de robustez operan con muestras más pequeñas y sesgadas hacia economías avanzadas.
4. **Asimetría temporal entre fuentes Y:** Las variables Y no miden exactamente el mismo punto temporal (readiness 2025, adopción H2 2025, inversión 2024, patentes 2023). Esta limitación es inherente a un diseño cross-section con fuentes heterogéneas.
5. **Corpus NLP pendiente:** La sub-pregunta 4 requiere recopilación de textos legales, que es una fase independiente.

### 10.7 Veredicto final

| Criterio | Estado | Evidencia |
|---|---|---|
| ¿Dataset con dimensiones suficientes? | ✅ | 86 × 66 (72 principales) |
| ¿4 grupos regulatorios representados? | ✅ | comprehensive=27, strategy=34, light_touch=9, none=2 |
| ¿7 regiones representadas? | ✅ | Todas con N ≥ 2 |
| ¿Variables Y principales completas en muestra principal? | ✅ | 4/4 variables con 72/72 |
| ¿Controles X2 core completos? | ✅ | GDP, internet, GII, OECD, region ≥97% |
| ¿Chile incluido con datos completos? | ✅ | 18/19 variables, complete_strict=True |
| ¿Varianza suficiente en todas las Y? | ✅ | Rango amplio en todas las variables |
| ¿Pipeline reproducible? | ✅ | 8 scripts, 3 etapas, desde raw hasta sample_ready |
| ¿Decisiones metodológicas documentadas? | ✅ | 11 decisiones en DATA_DECISIONS_LOG.md |

**La fase de recopilación de datos está completa.** El dataset `sample_ready_cross_section.csv` contiene los datos necesarios y suficientes para iniciar la fase de limpieza (notebook `02_limpieza.ipynb`) y, posteriormente, el análisis exploratorio y modelamiento estadístico que responderán las preguntas de investigación. La muestra principal de **72 países** proporciona suficiente poder estadístico para estimar modelos de regresión multivariada con controles socioeconómicos y comparaciones entre los 4 grupos regulatorios, cumpliendo los requisitos metodológicos para un estudio de recomendación de política pública orientado a informar la decisión legislativa chilena sobre el Boletín 16821-19.

---

## 11. Recomendaciones para Pasos Siguientes

Esta sección tiene un propósito concreto: **aclarar cómo se conectan los datos recopilados con las respuestas que busca la investigación**, y definir el camino exacto desde el dataset crudo hasta las conclusiones de política pública. Se organiza en tres bloques: (1) qué nos dice cada dato, (2) cómo limpiar y preparar los datos, y (3) cómo usarlos para responder las hipótesis.

---

### 11.1 ¿Qué nos dice cada variable? Mapa de lectura del dataset

Antes de tocar una sola línea de código, es fundamental entender **qué historia cuenta cada columna** del dataset. Cada variable fue recopilada con un propósito preciso dentro de la lógica de investigación: medir el ecosistema de IA (Y), caracterizar la regulación (X1), o controlar por factores que podrían confundir la relación entre ambas (X2).

#### Las variables Y — "¿Cómo le va al ecosistema de IA de cada país?"

Cada variable Y captura una **dimensión diferente** del desarrollo del ecosistema de IA. No existe un indicador único que capture todo, por eso se recopilaron cuatro complementarias:

| Variable | Lo que nos dice en una frase | Ejemplo concreto | Skewness |
|---|---|---|---|
| `ai_readiness_score` | Qué tan preparado está un país para aprovechar la IA (gobierno, infraestructura, sociedad) | USA=88.36 (más preparado), Chile=59.30 (mediana global), SEN=32.47 (menos preparado) | −0.40 (simétrica) |
| `ai_adoption_rate` | Qué porcentaje de la población y empresas usan IA activamente | CHN=64.0% (mayor adopción), Chile=20.8%, NGA=6.6% (menor) | 0.91 (leve asimetría) |
| `ai_investment_usd_bn_cumulative` | Cuánto capital de riesgo ha fluido hacia startups de IA en ese país desde 2013 | USA=470.9 bn (domina), CHN=103.3 bn, Chile=0.68 bn, mediana=0.33 bn | 7.76 (extrema — requiere log) |
| `ai_startups_cumulative` | Cuántas empresas de IA se han creado en ese país | USA=6,956, GBR=1,948, Chile=17, mediana=15 | 7.55 (extrema — requiere log) |

**Lectura práctica:** Si un país tiene alto readiness pero baja inversión, significa que tiene condiciones favorables pero el capital privado no está llegando. Si tiene alta adopción pero pocas startups, probablemente está **consumiendo** IA importada en lugar de **producirla**. Estas diferencias entre dimensiones Y son las que hacen interesante el análisis multidimensional.

**Decisión crítica sobre `ai_patents_per100k` (variable de robustez):** Con skewness=5.10 y solo 49/72 observaciones en la muestra principal, las patentes se usan únicamente como **análisis de robustez** — es decir, para verificar si los resultados principales se sostienen con un indicador alternativo de innovación, no como variable central del modelo.

#### Las variables X1 — "¿Cómo regula cada país la IA?"

Las variables X1 son el corazón de la pregunta de investigación. Son las variables **explicativas** — el "tratamiento" cuyo efecto queremos medir:

| Variable | Lo que nos dice | Cómo se usa en el modelo | Valores observados |
|---|---|---|---|
| `has_ai_law` | ¿Tiene el país algún marco regulatorio de IA? (sí/no) | **Modelo básico:** Comparar Y entre países con y sin marco. Es el test más simple: ¿importa tener regulación? | 81 sí / 5 no |
| `regulatory_approach` | ¿Qué tipo de enfoque adoptó? | **Modelo con dummies:** Crear 3 dummies (comprehensive, strategy_led, light_touch) con none como referencia. Permite comparar cada tipo de regulación contra la ausencia | comprehensive=32, strategy=39, light_touch=10, none=5 |
| `regulatory_intensity` | ¿Qué tan intensa es la regulación? (escala 0-5) | **Modelo lineal ordinal:** Estimar si más intensidad = más/menos ecosistema. Correlación cruda con readiness: r=0.598, con adopción: r=0.451 — pero **sin controlar por GDP/GII** | 0 a 5, media~3.2 |
| `enforcement_level` | ¿Tiene autoridad supervisora y sanciones? | **Interacción/moderación:** Una ley sin enforcement puede ser diferente de una con cumplimiento activo | high=31, low=30, medium=14, none=11 |
| `thematic_coverage` | ¿Cuántos temas cubre la regulación? (privacidad, sesgo, IA generativa, etc.) | **Proxy de comprehensividad:** Más temas → regulación más amplia | 0 a 14 temas |
| `year_enacted` | ¿Cuándo se promulgó el marco regulatorio? | **Control temporal:** Permite evaluar si el efecto de regular depende de cuántos años lleva vigente | 54 países sin dato (no tienen año), los demás entre 2017-2025 |

**Alerta sobre correlaciones crudas vs. controladas:** Los datos crudos muestran que `regulatory_intensity` correlaciona con readiness (r=0.598) y adopción (r=0.451), pero **también** lo hacen GDP per cápita (r=0.674 y 0.807) y GII (r=0.835 y 0.706). Esto significa que la correlación regulación-ecosistema podría ser espuria — los países ricos regulan más Y tienen mejor ecosistema de IA, no necesariamente **porque** regulan. Aislar el efecto causal de la regulación requiere el modelo multivariado con controles X2. **Esta es la razón fundamental por la que los controles existen.**

#### Las variables X2 — "¿Qué otros factores explican el ecosistema de IA?"

Sin controles, la investigación sería inútil. Las variables X2 absorben la varianza que no corresponde a la regulación:

| Variable | Efecto confundente que controla |
|---|---|
| `gdp_per_capita_ppp` | Los países ricos invierten más en todo, incluida IA. Sin este control, confundiríamos "efecto de ser rico" con "efecto de regular". Correlación con readiness: r=0.674 |
| `internet_penetration` | La adopción de IA es imposible sin infraestructura digital. Un país con 20% de internet no adoptará IA al 50% por más que tenga la mejor ley |
| `gii_score` | La innovación general (universidades, I+D, patentes en todos los campos) determina la base sobre la que opera el ecosistema de IA. Correlación con readiness: r=0.835 — el control más fuerte |
| `oecd_member` | Ser OECD implica más recursos, más presión regulatoria y más datos disponibles. Controla el sesgo estructural OECD/no-OECD |
| `region` | Absorbe patrones regionales no observados: proximidad a Silicon Valley, integración en mercado digital europeo, hubs asiáticos, etc. |
| `rd_expenditure` | El gasto en I+D es causa directa de innovación, no consecuencia de la regulación de IA. Sin este control, una regulación en un país que gasta 3% del PIB en I+D parecería "mejor" que la de un país que gasta 0.3% |
| `tertiary_education` | La IA requiere talento calificado. La disponibilidad de profesionales técnicos es un factor estructural previo a cualquier regulación |
| `government_effectiveness` | Un gobierno que ejecuta bien sus políticas también implementará mejor su regulación de IA. Asignada a robustez (63/86) para no reducir la muestra principal |

---

### 11.2 Proceso de limpieza de datos: paso a paso

La limpieza es la fase que transforma el dataset de recopilación (`sample_ready_cross_section.csv`) en un dataset analítico listo para modelamiento. Debe ejecutarse en el notebook `02_limpieza.ipynb` siguiendo este orden lógico:

#### Paso 1 — Carga y validación inicial

- Cargar `data/interim/sample_ready_cross_section.csv` (86 × 66)
- Verificar que `iso3` es clave primaria sin duplicados (86 únicos)
- Verificar tipos de datos: numéricas como float64, categóricas como object
- Confirmar los flags de completitud: `complete_principal` (72), `complete_extended` (62), `complete_strict` (46)

#### Paso 2 — Definir el scope de análisis

- **Muestra de trabajo:** Filtrar a los 72 países con `complete_principal == True`
- **Justificación:** Estos 72 países tienen las 4 variables Y principales y los 3 controles X2 core completos. Trabajar con la muestra principal garantiza que ningún modelo sufra pérdida de observaciones por missingness en variables centrales
- **Conservar los 86 para referencia:** No eliminar los 14 países parciales del archivo, solo marcarlos

#### Paso 3 — Tratamiento de valores nulos en la muestra principal

Los 72 países principales tienen cero nulos en Y principales y X2 core, pero pueden tener nulos en variables extended y robustez:

| Variable | Nulls en principal (72) | Tratamiento recomendado |
|---|---|---|
| `ai_patents_per100k` | 23 | Variable de robustez — usar solo en modelos de sensibilidad con submuestreo (N=49) |
| `rd_expenditure` | 10 | Variable extended — imputar con mediana regional o usar submuestreo (N=62) |
| `tertiary_education` | ~3 | Imputar con mediana regional; baja proporción de missingness |
| `government_effectiveness` | ~9 | Variable de robustez — usar con submuestreo (N=63 en universo) |
| `ai_investment_vc_proxy` | ~40 | Robustez OECD — solo para OECD countries, no imputar |
| `ai_publications_frac` | ~15 | Robustez OECD — mismas condiciones |
| `year_enacted` | ~40 | Los nulos son legítimos: países sin marco regulatorio no tienen año. Codificar como `NaN` intencional o 0 según el modelo |

**Regla de oro:** No imputar variables de robustez. Usar submuestreo explícito con N reportado.

#### Paso 4 — Transformaciones de distribución

Las estadísticas de skewness revelan qué transformaciones son necesarias:

| Variable | Skewness | Transformación recomendada | Justificación |
|---|---|---|---|
| `ai_readiness_score` | −0.40 | Ninguna | Distribución aproximadamente simétrica |
| `ai_adoption_rate` | 0.91 | Evaluar log o dejar sin transformar | Leve asimetría, probablemente tolerable para OLS |
| `ai_investment_usd_bn_cumulative` | **7.76** | **log(x + 1)** obligatoria | Distribución extremadamente concentrada (USA=471, mediana=0.33). Sin transformación, OLS estará dominado por 2-3 outliers |
| `ai_startups_cumulative` | **7.55** | **log(x + 1)** obligatoria | Mismo patrón: USA=6,956, mediana=15. La transformación log lineariza la relación |
| `ai_patents_per100k` | 5.10 | log(x + 1) si se usa | Solo en análisis de robustez |
| `gdp_per_capita_ppp` | Moderada | log(x) recomendada | Estándar en econometría: log-GDP captura rendimientos decrecientes |

**Nota práctica:** Usar `log(x + 1)` en lugar de `log(x)` cuando la variable puede tomar valor 0 (e.g., inversión=0 para algunos países). En Python: `np.log1p(x)`.

#### Paso 5 — Codificación de variables categóricas

| Variable | Tipo actual | Codificación necesaria | Para el modelo |
|---|---|---|---|
| `regulatory_approach` | Categórica (4 niveles) | One-hot encoding → 3 dummies (referencia: `none`) | OLS con dummies de grupo regulatorio |
| `enforcement_level` | Categórica (4 niveles) | One-hot o codificación ordinal (none=0, low=1, medium=2, high=3) | Depende si se trata como ordinal o nominal |
| `region` | Categórica (7 niveles) | One-hot encoding → 6 dummies (referencia: a elegir) | Fixed effects regionales |
| `oecd_member` | Binaria (0/1) | Ya codificada | Dummy directa |
| `has_ai_law` | Binaria (0/1) | Ya codificada | Dummy directa |

#### Paso 6 — Detección de outliers

Las principales variables con outliers identificados:

- **`ai_investment_usd_bn_cumulative`:** USA (470.9) y CHN (103.3) son outliers extremos. La transformación log mitiga esto, pero verificar que los resultados son robustos excluyendo USA y CHN (análisis de sensibilidad)
- **`ai_startups_cumulative`:** USA (6,956) y GBR (1,948) son outliers. Mismo tratamiento con log
- **Verificar Cook's distance** en los modelos OLS para identificar observaciones influyentes

#### Paso 7 — Multicolinealidad

Verificar con VIF (Variance Inflation Factor) antes de modelar:

- `gdp_per_capita_ppp` y `gii_score` correlacionan fuertemente con readiness (r=0.674 y r=0.835). Podrían generar multicolinealidad entre controles
- `internet_penetration` correlaciona con GDP (países ricos tienen más internet)
- **Acción recomendada:** Calcular VIF para todos los regresores. Si VIF > 10, evaluar eliminar un control redundante o usar PCA para reducir los controles a componentes

#### Paso 8 — Exportar dataset limpio

- Guardar en `data/processed/` como `analytical_dataset.csv` (o nombre equivalente)
- Incluir tanto las variables originales como las transformadas (log_investment, log_startups, log_gdp)
- Documentar cada transformación en el notebook `02_limpieza.ipynb`

---

### 11.3 ¿Cómo usar los datos para responder las hipótesis?

Esta es la pregunta central: tenemos 72 países con datos completos — **¿cómo pasamos de tablas de números a respuestas sobre política pública?** A continuación se describe la estrategia analítica para cada fase posterior a la limpieza.

#### Fase 1: Análisis Exploratorio (EDA) — notebook `03_eda.ipynb`

El EDA tiene un objetivo concreto: **descubrir patrones visuales** antes de modelar, y verificar que los supuestos estadísticos se cumplen. No es una exploración genérica — cada visualización responde una pregunta específica:

| Visualización | Pregunta que responde | Variables |
|---|---|---|
| Boxplots de Y por `regulatory_approach` | ¿Se observan diferencias visibles en el ecosistema de IA entre los 4 grupos regulatorios? | Y × regulatory_approach |
| Scatter: `regulatory_intensity` vs. cada Y | ¿Existe una relación visual entre intensidad regulatoria y ecosistema? ¿Es lineal? | regulatory_intensity × Y |
| Heatmap de correlaciones | ¿Qué variables correlacionan entre sí? ¿Hay multicolinealidad? ¿Los controles X2 dominan sobre X1? | Todas las numéricas |
| Mapa coropleth de readiness/adoption | ¿Hay patrones geográficos visibles? | Y × iso3 |
| Distribuciones de Y (histogramas, Q-Q plots) | ¿Las transformaciones log normalizaron las distribuciones? | Y originales y log-transformadas |
| Scatter matrix: Y vs. controles X2 | ¿Cuánta varianza en Y ya explican los controles? (Si es >80%, el espacio para que X1 aporte es pequeño) | Y × X2 |

**Lo que se busca en el EDA respecto a la hipótesis:** Si los boxplots muestran diferencias claras entre grupos regulatorios **pero** el scatter GDP vs. readiness muestra una relación aún más fuerte, eso anticipa que la regulación podría no ser significativa después de controlar por GDP. El EDA prepara mentalmente para los resultados del modelo.

#### Fase 2: Modelamiento Estadístico — notebook `04_modelamiento.ipynb`

El diseño de modelos sigue una progresión lógica:

**Modelo 1 — OLS bivariado (baseline):**

```
Y_i = β₀ + β₁ · regulatory_intensity_i + ε_i
```

Sin controles. Compara directamente regulación con ecosistema. Las correlaciones crudas anticipan: β₁ positivo para readiness (r=0.598) y adopción (r=0.451), pero cercano a cero para inversión (r=0.065) y startups (r=0.083). **Pero este modelo es inútil para inferencia causal** — solo describe la correlación bruta.

**Modelo 2 — OLS multivariado con controles (modelo central):**

```
Y_i = β₀ + β₁ · regulatory_intensity_i + β₂ · log(GDP_i) + β₃ · internet_i + β₄ · GII_i + β₅ · OECD_i + β₆₋₁₁ · region_dummies_i + ε_i
```

Este es **el modelo que responde la pregunta principal.** Se estima para cada variable Y separadamente. Si β₁ es estadísticamente significativo después de controlar por GDP, internet, GII, OECD y región, entonces hay evidencia de asociación entre regulación y ecosistema **que no se explica por factores socioeconómicos**.

**Modelo 3 — OLS con dummies de grupo regulatorio:**

```
Y_i = β₀ + β₁ · comprehensive_i + β₂ · strategy_led_i + β₃ · light_touch_i + controles_i + ε_i
```

Con `none` como grupo de referencia. Permite comparar cada tipo de regulación contra la ausencia. ¿comprehensive supera a strategy_led? ¿light_touch es diferente de no regular? Aquí se responde qué **tipo** de enfoque se asocia con mejores resultados.

**Modelo 4 — Análisis de robustez:**
- Reestimar Modelos 2-3 con `ai_patents_per100k` como Y (N=49)
- Reestimar con `government_effectiveness` y `rd_expenditure` como controles adicionales (N=62 y 46)
- Reestimar excluyendo USA y CHN (test de sensibilidad a outliers)
- Si los resultados son consistentes entre modelos, la conclusión es robusta

**Modelo 5 — Clustering (K-Means):**

Agrupación no supervisada de los 72 países según su perfil combinado de regulación + ecosistema + controles. Permite identificar **arquetipos de países** (e.g., "alta regulación, alto ecosistema", "baja regulación, bajo ecosistema", "alta regulación, bajo ecosistema"). ¿Dónde cae Chile? ¿Con quiénes comparte cluster?

**Modelo 6 — PCA:**

Reducción de dimensionalidad para visualizar en 2D la relación entre las múltiples variables. Útil para comunicar resultados de manera visual y detectar estructuras latentes en los datos.

#### Fase 3: NLP de textos legales — notebook `05_nlp.ipynb`

Para la sub-pregunta 4 (contenido regulatorio), se requiere una rama paralela:

1. **Recopilar** textos completos de leyes de IA para 15-20 países representativos de cada grupo regulatorio
2. **Preprocesar:** Tokenización, eliminación de stopwords, lematización con spaCy
3. **TF-IDF:** Identificar términos diferenciadores entre jurisdicciones
4. **Topic Modeling (LDA):** Extraer temas latentes (riesgo, transparencia, innovación, sanciones, datos personales)
5. **Similaridad coseno:** Identificar clusters de países con regulaciones similares
6. **Integrar** los resultados temáticos con el dataset cuantitativo

---

### 11.4 De los datos a la recomendación para Chile

El flujo completo de la investigación, desde los datos hasta la recomendación legislativa, es:

```
DATOS (86 × 66)
    │
    ▼
LIMPIEZA (72 × ~30 variables analíticas)
    │
    ▼
EDA (patrones visuales, verificación de supuestos)
    │
    ▼
MODELOS OLS (β₁ significativo → regulación importa)
    │                           (β₁ no significativo → regulación no importa después de controlar)
    ▼
ROBUSTEZ (¿se sostiene con otros Y, otros controles, sin outliers?)
    │
    ▼
CLUSTERING (¿con quiénes se agrupa Chile?)
    │
    ▼
NLP (¿qué temas regulatorios se asocian con mejores resultados?)
    │
    ▼
RECOMENDACIÓN PARA CHILE:
    - ¿Debe aprobar el Boletín 16821-19?
    - Si sí, ¿qué tipo de enfoque (comprehensive vs strategy_led)?
    - ¿Qué temas regulatorios priorizar?
    - ¿Qué nivel de enforcement implementar?
```

**Lo que el dataset puede y no puede responder:**

| Pregunta | ¿El dataset puede responderla? | Cómo |
|---|---|---|
| ¿Tener regulación de IA importa para el ecosistema? | ✅ | OLS: β₁ de `has_ai_law` o `regulatory_intensity` controlando por X2 |
| ¿Qué tipo de regulación es mejor? | ✅ | OLS con dummies: comparar β de comprehensive, strategy_led, light_touch |
| ¿Más enforcement = mejor resultado? | ✅ | OLS con `enforcement_level` como regresor adicional |
| ¿La regulación causa mejor ecosistema? | ⚠️ Parcialmente | Cross-section no permite causalidad estricta — solo asociación después de controlar por confounders. Para causalidad se necesitaría panel o instrumento |
| ¿Chile debería copiar el EU AI Act? | ✅ | Comparar el cluster de Chile con los de comprehensive countries. Si países similares a Chile con comprehensive tienen mejor ecosistema, hay evidencia favorable |
| ¿Qué temas regulatorios priorizar? | ✅ (con NLP) | Cruzar clusters temáticos del NLP con valores Y de cada cluster |

---

### 11.5 Checklist de entrega para la fase de limpieza

Antes de dar por completada la fase de limpieza (`02_limpieza.ipynb`), verificar:

- [ ] Dataset filtrado a muestra principal (72 países)
- [ ] Transformaciones log aplicadas a inversión, startups (y GDP si procede)
- [ ] Variables categóricas codificadas (dummies para regulatory_approach, region)
- [ ] VIF calculado — multicolinealidad diagnosticada
- [ ] Outliers identificados y documentados (no eliminados, pero flaggeados)
- [ ] Nulos en variables extended/robustez documentados con estrategia explícita
- [ ] Dataset limpio exportado a `data/processed/`
- [ ] Todas las transformaciones reproducibles desde el notebook
