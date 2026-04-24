# Variables OECD — STI Scoreboard, MSTI & OECD.AI

## Proposito

Este documento resume las variables extraidas desde cuatro subfuentes OECD:
1. **STI Scoreboard** (GitHub SDMX XML) — indicadores de publicaciones IA, patentes IA, venture capital e investigadores.
2. **MSTI** (SDMX API) — indicadores macro de I+D (GERD, BERD, HERD, GOVERD).
3. **OECD.AI Visualizations** (WordPress REST API) — catalogo de 191 visualizaciones del portal OECD.AI (sin datos tabulares, solo metadata).
4. **EC-OECD AI Policy Database** (API buddyweb) — 2,218 iniciativas de politica de IA de 73+ paises. Fuente para las 6 variables X1 del estudio.

Su objetivo es servir como referencia rapida para:
- saber que variables del estudio fueron extraidas desde OECD;
- conocer la cobertura real (paises, anios, missingness);
- distinguir roles (Y, Y_proxy, X2, extra);
- preparar la integracion con Stanford y WDI en fases posteriores.

## Fuentes

| subfuente | metodo | endpoint | ubicacion_local |
|---|---|---|---|
| STI Scoreboard | GitHub raw files (SDMX XML) | `raw.githubusercontent.com/STIScoreboard/STI.Scoreboard/main/` | `data/raw/OECD/oecd_sti_scoreboard.csv` |
| MSTI | OECD SDMX API (CSV) | `sdmx.oecd.org/public/rest/data/OECD.STI.STP,DSD_MSTI@DF_MSTI/` | `data/raw/OECD/oecd_msti.csv` |
| OECD.AI Visualizations | WordPress REST API | `wp.oecd.ai/wp-json/wp/v2/visualizations` | `data/raw/OECD/oecd_ai_visualizations_catalog.csv` |
| EC-OECD AI Policy DB | JSON REST API (paginada) | `oecd-ai.case-api.buddyweb.fr/policy-initiatives` | `data/raw/OECD/oecd_ai_policy_initiatives_all.csv` |

## Conclusion Ejecutiva

OECD aporta **16 indicadores cuantitativos** + **6 variables X1 de regulacion** + **7 variables complementarias** para el estudio:
- **8 variables Y / Y_proxy** directas de ecosistema IA (publicaciones, patentes, venture capital)
- **5 variables X2** de capacidad cientifica e innovacion (GERD, BERD, HERD, GOVERD, investigadores)
- **6 variables X1** de regulacion IA derivadas de la EC-OECD AI Policy Database (has_ai_law, regulatory_approach, year_enacted, regulatory_intensity, enforcement_level, thematic_coverage)
- **7 variables X1 complementarias** (n_total_initiatives, n_binding, n_nonbinding, n_strategies, n_regulations, n_sectors_covered, n_policy_instruments)
- **3 variables extra** de calidad y colaboracion (top 10%, colab. internacional, PhD ingenieria)

**Cobertura**: 107 paises cuantitativos + 73 paises policy = 80 de los 86 paises del estudio. Periodo 2009-2024 (cuantitativos) y 2013-2024 panel (policy/X1).

**Hallazgo critico (resuelto)**: Las variables X1 de regulacion IA fueron exitosamente extraidas de la API oculta `case-api.buddyweb.fr` del portal EC-OECD. Se descargaron 2,218 iniciativas de politica de IA y se construyeron las 6 variables X1 en formato panel pais-año. **La brecha X1 del estudio esta cubierta** para 68 de los 86 paises.

## Archivos Generados

| archivo | contenido | filas | columnas | tamano |
|---|---|---|---|---|
| `oecd_all_indicators_long.csv` | Todos los indicadores en formato long | 12,700 | 5 (iso3, year, indicator, value, source) | 772 KB |
| `oecd_all_indicators_wide.csv` | Todos los indicadores en formato wide | 1,515 | 18 (iso3, year, + 16 indicadores) | 170 KB |
| `oecd_sti_scoreboard.csv` | Solo indicadores STI Scoreboard (wide) | - | 14 | 140 KB |
| `oecd_msti.csv` | Solo indicadores MSTI (wide) | - | 6 | 31 KB |
| `oecd_ai_visualizations_catalog.csv` | Catalogo metadata de visualizaciones | 191 | 6 | 27 KB |
| `oecd_ai_policy_initiatives_all.csv` | Todas las iniciativas de politica IA (73 paises) | 2,535 | 19 | 1,365 KB |
| `oecd_ai_policy_initiatives_study.csv` | Iniciativas filtradas a 86 paises del estudio | 2,402 | 19 | 1,285 KB |
| `oecd_x1_policy_variables.csv` | Panel X1 completo pais-año (13 variables) | 816 | 15 | 40 KB |
| `oecd_x1_core.csv` | Solo 6 variables X1 core pais-año | 816 | 8 | 28 KB |
| `oecd_x1_snapshot_2024.csv` | Snapshot X1 para 2024 (1 fila por pais) | 68 | 15 | 4 KB |
| `oecd_ai_country_profiles.csv` | Perfiles resumen de paises (limitado) | 10 | 6 | 0.6 KB |

## Variables Operativas Extraidas

### 1. Y / Y_proxy — Ecosistema IA (STI Scoreboard)

| canonical_name | archivo_github | role | descripcion | paises | periodo | n_obs | observacion_metodologica |
|---|---|---|---|---|---|---|---|
| ai_publications_frac | AIPUBS_NBFRAC_V8.txt | Y_proxy | Total AI scientific publications (fractional count) | 63 | 2009-2023 | 945 | Complementa ai_patents de Stanford. Conteo fraccionario evita doble conteo por coautoria. |
| ai_publications_top10_frac | TOP10_AI_NBFRAC_V8.txt | Y_proxy | Top 10% cited AI scientific publications (fractional count) | 63 | 2009-2023 | 941 | Mide calidad de la produccion cientifica en IA, no solo volumen. |
| ai_publications_scopus_frac | FPUBS_1702_NBFRAC_V8.txt | Y_proxy | AI publications in Scopus field 1702 (fractional count) | 62 | 2009-2023 | 930 | Restringido a Scopus campo 1702. Subset mas selectivo. |
| ai_patents_pct | PCTAI_NB_V8.txt | Y | AI-related patent families filed under PCT | 104 | 2009-2020 | 1,248 | Complementa ai_patents de Stanford con serie temporal mas larga y mas paises. |
| ai_patents_ip5 | IP5AI_NB_V8.txt | Y | AI-related patent families filed at IP5 offices | 104 | 2009-2020 | 1,248 | Patentes IA ante las 5 oficinas principales (USPTO, EPO, JPO, KIPO, CNIPA). |
| vc_seed_pct_gdp | VCSEED_XGDP_V8.txt | Y_proxy | Venture capital — seed stage as % of GDP | 33 | 2009-2024 | 511 | Solo 33 paises con datos. Complementa ai_investment de Stanford. |
| vc_startup_pct_gdp | VCSTART_XGDP_V8.txt | Y_proxy | Venture capital — start-up stage as % of GDP | 33 | 2009-2024 | 511 | Desglose por etapa. Solo paises OECD con datos de VC. |
| vc_later_pct_gdp | VCLATE_XGDP_V8.txt | Y_proxy | Venture capital — later stage as % of GDP | 33 | 2009-2024 | 511 | Etapas tardias de VC. Mismo subset de 33 paises. |

### 2. X2 — Variables de Control (MSTI SDMX + STI Scoreboard)

| canonical_name | fuente | measure_code | role | descripcion | paises | periodo | n_obs | observacion_metodologica |
|---|---|---|---|---|---|---|---|---|
| gerd_pct_gdp | MSTI SDMX | G (PT_B1GQ) | X2 | Gross domestic expenditure on R&D as % of GDP | 49 | 2013-2024 | 546 | Complementa/reemplaza rd_expenditure de WDI. Fuente oficial OECD, mas actualizada. |
| berd_pct_gdp | MSTI SDMX | B (PT_B1GQ) | X2 | Business enterprise R&D expenditure as % of GDP | 49 | 2013-2024 | 550 | Desglose no disponible en WDI. I+D del sector privado, relevante para ecosistema IA. |
| herd_pct_gdp | MSTI SDMX | H (PT_B1GQ) | X2 | Higher education R&D expenditure as % of GDP | 49 | 2013-2024 | 553 | I+D universitario. Relevante para publicaciones y talento IA. |
| goverd_pct_gdp | MSTI SDMX | GV (PT_B1GQ) | X2 | Government R&D expenditure as % of GDP | 49 | 2013-2024 | 553 | I+D gubernamental. Complementa gerd_pct_gdp. |
| researchers_per_1000_employed | STI Scoreboard | TP_RSXEM_V8.txt | X2 | Total researchers (FTE) per 1000 total employment | 47 | 2009-2023 | 648 | Capital humano cientifico. Denominador = empleo total. |

### 3. Variables Extra (STI Scoreboard)

| canonical_name | archivo_github | role | descripcion | paises | periodo | n_obs | observacion_metodologica |
|---|---|---|---|---|---|---|---|
| ai_publications_top10_pct | TOP10_AI_X_V8.txt | extra | % of AI publications among world's 10% top-cited | 63 | 2009-2023 | 941 | Calidad relativa. Podria servir como Y alternativa en modelos de robustez. |
| ai_publications_intl_collab_pct | AI_INTL_X_V8.txt | extra | % of AI publications with international collaboration | 63 | 2009-2023 | 941 | Proxy de apertura cientifica. Podria ser X2 o control en analisis. |
| phd_enrolment_engineering_pct | PHDENR_ENG_XT_V8.txt | extra | PhD enrolment in engineering as % of all PhD | 45 | 2013-2023 | 1,123 | Proxy de pipeline de talento STEM/IA. Missingness alto (67% en wide para muestra). |

## Cobertura — Cruce Con Muestra Del Estudio

| metrica | valor |
|---|---|
| Paises en datos OECD (cuantitativos) | 107 |
| Paises en datos OECD (policy) | 73 |
| Paises en muestra del estudio | 86 |
| Interseccion cuantitativos | 77 |
| Interseccion policy (X1) | 68 |
| Con al menos 1 dato OECD | 80 |
| Sin datos OECD de ningun tipo | 6 |

### Paises de la muestra SIN ningun dato OECD (6)

| iso3 | pais | estado_actual |
|---|---|---|
| BGD | Bangladesh | SOLO Y |
| BHR | Bahrain | SOLO Y |
| BLZ | Belize | SOLO Y |
| BRB | Barbados | SOLO Y |
| CMR | Cameroon | ACTIVO |
| GHA | Ghana | SOLO Y |

**Nota**: 5 de los 6 son paises "SOLO Y". Solo CMR (Cameroon) es ACTIVO. MUS, SRB y UGA ahora tienen datos X1 via la API de politicas.

## Missingness por Indicador (solo paises del estudio, formato wide)

| indicador | pct_missing |
|---|---|
| phd_enrolment_engineering_pct | 67.0% |
| vc_seed_pct_gdp | 55.4% |
| vc_startup_pct_gdp | 55.4% |
| vc_later_pct_gdp | 55.4% |
| gerd_pct_gdp | 54.4% |
| berd_pct_gdp | 54.1% |
| goverd_pct_gdp | 53.8% |
| herd_pct_gdp | 53.8% |
| researchers_per_1000_employed | 45.9% |
| ai_publications_intl_collab_pct | 21.7% |
| ai_publications_top10_frac | 21.7% |
| ai_publications_top10_pct | 21.7% |
| ai_publications_frac | 21.4% |
| ai_publications_scopus_frac | 21.4% |
| ai_patents_ip5 | 20.3% |
| ai_patents_pct | 20.3% |

**Interpretacion**: Las publicaciones y patentes IA tienen missingness ~20% (buena cobertura). Los indicadores MSTI (~54%) y VC (~55%) tienen missingness alto porque solo cubren paises OECD e invitados. PhD enrolment (67%) tiene la peor cobertura.

### 4. X1 — Variables de Regulacion IA (EC-OECD AI Policy Database)

**Fuente**: API `https://oecd-ai.case-api.buddyweb.fr/policy-initiatives`
**Metodo**: API REST paginada (JSON), 20 items/pagina, 111 paginas.
**Total extraido**: 2,218 iniciativas de 73 paises + 8 organizaciones internacionales.
**Cobertura estudio**: 68 de 86 paises del estudio tienen datos de politica.

#### Variables X1 Core (por pais-año, acumulativas)

| canonical_name | tipo | derivacion | descripcion | valores_ejemplo |
|---|---|---|---|---|
| has_ai_law | X1 (binaria) | count(Binding vigentes) > 0 | Indicador si el pais tiene al menos 1 regulacion IA vinculante vigente | 0, 1 |
| regulatory_approach | X1 (categorica) | Clasificacion de initiativeType + category | Enfoque regulatorio del pais | none, light_touch, strategy_led, regulation_focused, comprehensive |
| year_enacted | X1 (numerica) | min(startYear) de iniciativas Binding | Año de la primera regulacion IA vinculante | 1999-2024 o NaN |
| regulatory_intensity | X1 (numerica) | n_binding + n_initiative_types distintos | Intensidad regulatoria compuesta | 0-31 |
| enforcement_level | X1 (ordinal) | Presencia governance_bodies + count binding | Nivel de enforcement regulatorio | none, low, medium, high |
| thematic_coverage | X1 (numerica) | count(tags distintos) de iniciativas vigentes | Amplitud tematica de las politicas IA | 0-28 |

#### Variables X1 Complementarias

| canonical_name | tipo | descripcion |
|---|---|---|
| n_total_initiatives | complementaria | Total iniciativas de politica IA vigentes |
| n_binding | complementaria | Numero de iniciativas vinculantes vigentes |
| n_nonbinding | complementaria | Numero de iniciativas no vinculantes vigentes |
| n_strategies | complementaria | Numero de estrategias nacionales vigentes |
| n_regulations | complementaria | Numero de regulaciones/estandares vigentes |
| n_sectors_covered | complementaria | Numero de sectores cubiertos por las politicas |
| n_policy_instruments | complementaria | Numero de instrumentos de politica distintos |

#### Distribucion regulatory_approach (2024, 68 paises)

| enfoque | n_paises | descripcion |
|---|---|---|
| light_touch | 24 | Sin regulacion binding ni estrategia explicita |
| strategy_led | 17 | Tiene estrategia nacional pero sin regulacion binding |
| regulation_focused | 16 | Tiene regulacion binding sin estrategia explicita |
| comprehensive | 9 | Tiene regulacion binding + estrategia nacional |
| none | 2 | Sin iniciativas vigentes |

#### Paises del estudio SIN datos policy (18)

BGD, BHR, BLR, BLZ, BRB, CMR, GHA, JOR, LBN, LKA, MNG, PAK, PAN, PHL, RUS, SYC, TWN, UGA

## Variables De La Guia Restantes No Disponibles En OECD

| variable_estudio | tipo_metodologico | fuente_esperada | observacion |
|---|---|---|---|
| ai_vibrancy_score | Y target | Stanford HAI | No disponible en OECD. |
| ai_talent | Y | Stanford HAI | OECD tiene datos de talento IA en visualizaciones (OECD.AI), pero no como datos tabulares exportables. |
| ai_investment | Y | Stanford HAI | OECD.AI tiene 30 visualizaciones de inversion, pero datos detras de las viz no son accesibles (Flourish). |

## Catalogo OECD.AI Visualizations (referencia)

Se extrajo el catalogo completo de 191 visualizaciones del portal OECD.AI. Estas no aportan datos tabulares directamente (estan alojadas en Flourish con acceso restringido), pero sirven como:
- Referencia de que indicadores publica la OECD sobre IA.
- Posible fuente manual para datos puntuales.
- Traza documental de la exploracion.

| categoria | n_visualizaciones |
|---|---|
| OTHER | 58 |
| AI_RESEARCH_MODELS | 53 |
| AI_TALENT | 44 |
| AI_INVESTMENT | 30 |
| AI_INFRA | 4 |
| AI_POLICY | 2 |

## Nota Tecnica

### Codigos de pais
OECD usa codigos ISO 3166-1 alpha-3 para la mayoria de indicadores. Algunas excepciones (e.g., "OECD", "EU27", "EA20") son agregaciones regionales que fueron incluidas en la extraccion pero se eliminaran en la limpieza. No se requirio mapeo de codigos — la interseccion directa con la muestra ISO3 del estudio funciono correctamente.

### Dimension SDMX para MSTI
- Dataflow: `OECD.STI.STP,DSD_MSTI@DF_MSTI/1.3`
- Dimensiones: `REF_AREA.FREQ.MEASURE.UNIT_MEASURE.PRICE_BASE.TRANSFORMATION`
- Codigos de medida verificados: G (GERD), B (BERD), H (HERD), GV (GOVERD)
- Unidad: PT_B1GQ (porcentaje del PIB)
