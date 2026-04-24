# Guia Maestra De Variables Para ETL Del Estudio

## Proposito

Este documento define la lista canonica de variables que deben buscarse, evaluarse y mapearse cuando se importe cualquier nueva fuente de datos al proyecto.

Su uso esperado es el siguiente:
1. Primero se descarga o importa la fuente completa a `data/raw/`.
2. Luego se inspecciona el dataset completo.
3. Despues se compara ese dataset contra esta guia.
4. Solo entonces se decide que columnas extraer a `data/interim/`.

Este archivo esta escrito para que un LLM pueda usarlo como referencia operativa al revisar datasets nuevos.

## Definicion De Complete-Case (Actualizada 2025-04)

### Regla de inclusion muestral

La muestra incluye paises a lo largo de **todo el espectro regulatorio** (none, light_touch, strategy_led, regulation_focused, comprehensive). `has_ai_law` es una variable explicativa, **no** un filtro de inclusion.

### Tratamiento de year_enacted

`year_enacted` es obligatorio **solo** cuando `has_ai_law = 1`. Cuando `has_ai_law = 0`, `year_enacted` es ausencia estructural (no aplicable), no un dato faltante.

### Taxonomia regulatoria derivada

Variable `regulatory_status_group` con 4 niveles para analisis comparativo:
- `no_framework` ← regulatory_approach = none
- `soft_framework` ← regulatory_approach = light_touch
- `strategy_only` ← regulatory_approach = strategy_led
- `binding_regulation` ← regulatory_approach = regulation_focused | comprehensive

### Variables obligatorias para complete-case

**Y (4 targets operativos):** ai_readiness_score, ai_adoption_rate, ai_investment (Stanford), ai_startups (Stanford)

**X1 (5 regulatorias):** has_ai_law, regulatory_approach, regulatory_intensity, enforcement_level, thematic_coverage + year_enacted (condicional)

**X2 core (5 controles):** gdp_per_capita_ppp, internet_penetration, gii_score, oecd_member, region

**X2 confounders institucionales (2 — agregados 2026-04 post-auditoria Tarea A, ver D-012):**
regulatory_quality, rule_of_law

**X2 confounders legal-regulatorios (2 — agregados 2026-04 post-auditoria Tarea A sub-tarea A.4, ver D-014):**
has_gdpr_like_law, gdpr_similarity_level

**X2 economia digital (2 — agregados 2026-04 post-auditoria Tarea A sub-tarea A.5, ver D-015):**
ict_service_exports_pct, high_tech_exports_pct (proxies de produccion/exportacion digital via WDI)

**X2 regimen politico (2 — agregados 2026-04 post-auditoria Tarea A sub-tarea A.6, ver D-016):**
fh_total_score, fh_democracy_level (Freedom in the World 2025, captura dimension democratica no-redundante con WGI)

**X2 tradicion juridica (2 — agregados 2026-04 post-auditoria Tarea A sub-tarea A.3-bis, ver D-017):**
legal_origin, is_common_law (La Porta 2008, cinco familias legales; gradiente 13.3x en proporcion binding_regulation; r=-0.22 con regulatory_intensity, no redundante con WGI r=0.10)

**X2 extended (2 adicionales):** rd_expenditure, tertiary_education

### Variables de robustez (no bloquean complete-case)

- ai_patents_per100k: disponible para 54/86 paises — robustez para subpregunta de innovacion (ver DATA_DECISIONS_LOG D-006)
- government_effectiveness: disponible para **85/86** paises tras expansion WGI 2026-04 — robustez institucional (ver DATA_DECISIONS_LOG D-005, D-012)
- control_of_corruption: disponible para 85/86 paises (agregado 2026-04) — robustez institucional adicional (ver D-012)
- ai_investment_vc_proxy: disponible para 32/86 paises (OECD VC general) — robustez financiera (ver DATA_DECISIONS_LOG D-008)
- ai_vibrancy_score: **EXCLUIDA** — fuente no disponible (Stanford Vibrancy Tool descomisionado) (ver DATA_DECISIONS_LOG D-001)

### Resultados de la auditoria (actualizados 2026-04)

| Definicion | Paises completos | Variables |
|---|---|---|
| **PRINCIPAL** (4Y + 5X1 + 5X2) | **72/86** | ai_readiness_score, ai_adoption_rate, ai_investment_cumul, ai_startups_cumul + 5 X1 + gdp, internet, gii, oecd, region |
| **CONFOUNDED** (+WGI + GDPR-like confounders) **[recomendado]** | **72/86** | Principal + regulatory_quality + rule_of_law + has_gdpr_like_law + gdpr_similarity_level |
| DIGITAL (+economia digital) | 69/86 | Confounded + ict_service_exports_pct + high_tech_exports_pct (robustness) |
| REGIME (+Freedom House) | 72/86 | Confounded + fh_total_score + fh_democracy_level (robustness politica) |
| **LEGAL_TRADITION (+La Porta)** | **72/86** | **Confounded + legal_origin + is_common_law (robustness tradicion juridica)** |
| EXTENDED (+R&D+educ) | 62/86 | Principal + rd_expenditure + tertiary_education |
| STRICT (+patents+GE) | 47/86 | Extended + ai_patents_per100k + government_effectiveness |

**Nota metodologica:** La tier CONFOUNDED tiene el mismo N que PRINCIPAL (72) porque los confounders tienen cobertura alta: WGI 85/86 y GDPR-like 86/86. Esta es la tier **recomendada** para el modelo principal post-auditoria 2026-04, ya que separa el efecto de la regulacion AI-especifica de: (a) la calidad institucional general (WGI), y (b) la tradicion regulatoria digital preexistente GDPR-like. Ver D-012 (WGI) y D-014 (GDPR-like) en DATA_DECISIONS_LOG.

Representacion por grupo regulatorio (PRINCIPAL, N=72):
- binding_regulation: 27
- strategy_only: 34
- soft_framework: 9
- no_framework: 2

### Paquete de datos oficial para limpieza

La recoleccion se considera cerrada. El dataset definitivo es:

- **`data/interim/sample_ready_cross_section.csv`** — 86 paises × todas las variables + flags de completitud
- **`data/interim/coverage_matrix.csv`** — auditoria de cobertura variable × pais
- Source masters: `y_stanford_master.csv`, `y_microsoft_master.csv`, `y_oxford_master.csv`, `x2_wipo_master.csv`, `x2_wb_master.csv`, `x1_master.csv`, `oecd_robustness_master.csv`, `x2_gdpr_master.csv`, `x2_fh_master.csv`, `x2_legal_origin_master.csv`
- Pipeline: `src/build_source_masters.py` → `src/build_sample_ready.py`
- Decisiones: `info_data/DATA_DECISIONS_LOG.md`
- Ejecucion: `info_data/ETL_RUNBOOK.md`

## Instrucciones Operativas Para Un LLM

Cuando analices una fuente nueva para este proyecto, sigue estas reglas:

1. No inventes variables nuevas si no estan alineadas con la pregunta de investigacion.
2. Prioriza variables a nivel pais o pais-anio.
3. Prioriza observaciones comparables internacionalmente.
4. Si una variable no existe exactamente, busca una proxy defendible y dejala marcada como `proxy`.
5. No mezcles regiones con paises en la misma variable final sin documentarlo.
6. No mezcles anios distintos sin dejar una columna `year` clara.
7. Si el dataset tiene nombres de paises no estandarizados, normalizalos luego en limpieza, no en `data/raw/`.
8. Si una columna parece util pero no responde la pregunta principal, clasificala como `opcional` en vez de `core`.
9. Toda variable extraida debe poder mapearse a un nombre canonico definido aqui.
10. Si una fuente solo cubre parte del constructo, conserva el archivo y marca la variable como `proxy parcial`.

## Pregunta De Investigacion Que Debe Guiar El ETL

Pregunta central:

`Existe una asociacion estadisticamente significativa entre las caracteristicas de la regulacion de inteligencia artificial de un pais y el desarrollo de su ecosistema de IA, despues de controlar por factores socioeconomicos e institucionales?`

## Unidad Analitica Objetivo

### Tabla cuantitativa principal

- Grano preferido: `pais-anio`
- Llave ideal: `iso3 + year`
- Si una fuente solo entrega corte transversal, usar `iso3` y documentar el anio de referencia.

### Tabla NLP legal

- Grano preferido: `jurisdiccion-documento`
- Llave ideal: `jurisdiction_id + law_id`

## Variables Obligatorias De Identificacion Y Trazabilidad

Estas no son targets ni features analiticos, pero son obligatorias para un ETL profesional.

| canonical_name | rol | prioridad | tipo | descripcion | regla |
|---|---|---|---|---|---|
| iso3 | identificador | core | string | Codigo ISO 3166-1 alpha-3 | Obligatorio en la tabla maestra final |
| country_name_std | identificador | core | string | Nombre de pais estandarizado | Debe coexistir con `iso3` |
| year | identificador temporal | core | integer | Anio de referencia de la observacion | Si no existe, inferir y documentar |
| source_name | metadata | core | string | Fuente original del dato | Ej. Stanford, OECD, World Bank |
| source_dataset | metadata | core | string | Nombre del archivo, tabla o endpoint | Mantener traza a la fuente |
| source_variable_original | metadata | high | string | Nombre original de la columna o indicador | Muy util para auditoria |
| coverage_level | metadata | high | string | Nivel de agregacion | `country`, `region`, `global`, `jurisdiction` |
| unit_original | metadata | high | string | Unidad original reportada por la fuente | No perder unidades |
| notes_mapping | metadata | high | string | Nota breve de decisiones de mapeo | Usar cuando haya proxies o ambiguedad |

## Catalogo Canonico De Variables Del Estudio

### 1. Targets Y - Desarrollo Del Ecosistema De IA

| canonical_name | rol | prioridad | tipo esperado | grano esperado | definicion | fuente preferida | fuentes alternativas | alias de busqueda en datasets | proxy permitida |
|---|---|---|---|---|---|---|---|---|---|
| ai_vibrancy_score | target | **excluida** | float | pais-anio o pais | Score compuesto de vitalidad del ecosistema de IA | ~~Stanford HAI Global AI Vibrancy Tool~~ (descomisionado) | ~~Tortoise Global AI Index~~ (paywall) | vibrancy, ai vibrancy, global ai vibrancy, vibrancy score | no |
| ai_investment_vc | target | core | float | pais-anio o pais | Inversion privada o VC en IA en USD | **Stanford HAI fig_4.3.8/4.3.9 (84/86 paises)** | OECD VC proxy (33 paises) | ai investment, private investment, venture capital, vc investment, total investment in ai | si |
| ai_adoption_rate | target | core | float | pais-anio o pais | Tasa de adopcion de IA en poblacion, empresas o sector publico | Microsoft AI Diffusion | Oxford, Tortoise | adoption, ai adoption, enterprise adoption, business adoption, public sector adoption | si |
| ai_patents | target | core | float | pais-anio o pais | Volumen de patentes de IA | Stanford HAI | WIPO, OECD | ai patents, granted ai patents, patents per 100000, patents share | si |
| ai_startups | target | core | float | pais-anio o pais | Numero de startups o empresas de IA activas o financiadas | Stanford HAI | Crunchbase si fuera necesario | ai startups, newly funded ai companies, ai companies, funded ai companies | si |
| ai_readiness_score | target | core | float | pais-anio o pais | Capacidad gubernamental e infraestructura para IA | Oxford Insights Government AI Readiness Index | Tortoise | readiness, ai readiness, government ai readiness | no |

### 2. Features X1 - Regulacion De IA

> **Estado Extract**: ✅ **86/86 paises cubiertos** — fuentes raw listas y consolidadas.
> - OECD raw: `data/raw/OECD/oecd_x1_core.csv` (68 paises, panel 2013-2024)
> - IAPP raw: `data/raw/IAPP/iapp_x1_core.csv` (86 paises, codificacion directa)
> - **Consolidacion OECD+IAPP COMPLETADA**: `src/consolidate_x1.py` → `data/interim/x1_consolidated.csv` (86 paises, 902 rows, panel 2013-2025)
> - **Master oficial**: `data/interim/x1_master.csv` (86 paises, cross-section 2025)
> Documentacion detallada: `info_data/VARIABLES_IAPP.md`.

| canonical_name | rol | prioridad | tipo esperado | grano esperado | definicion | fuente preferida | fuentes alternativas | alias de busqueda en datasets | proxy permitida |
|---|---|---|---|---|---|---|---|---|---|
| has_ai_law | feature | core | binary | pais-anio o pais | 1 si existe ley especifica de IA, 0 si no | **OECD + IAPP (consolidado)** | Legislaturas nacionales | ai law, ai act, ai legislation, law enacted, specific ai law | no |
| regulatory_approach | feature | core | categorical | pais-anio o pais | Enfoque regulatorio dominante | **OECD + IAPP (consolidado)** | Codificacion manual | risk-based, sectoral, principles, horizontal, application-specific | no |
| regulatory_intensity | feature | core | ordinal | pais-anio o pais | Intensidad regulatoria 0-10 | **OECD + IAPP (consolidado)** | Legislacion nacional | restrictions, obligations, sanctions, comprehensive law | no |
| year_enacted | feature | core | integer | pais | Anio de promulgacion de la regulacion principal | **OECD + IAPP (consolidado)** | Manual | enacted, adopted, promulgated, entered into force | no |
| enforcement_level | feature | high | ordinal | pais | Nivel de enforcement institucional y sancionatorio | **OECD + IAPP (consolidado)** | Legislaturas nacionales | authority, supervisory authority, penalties, sanctions | no |
| thematic_coverage | feature | high | integer | pais | Numero de temas cubiertos por la norma (0-15) | **OECD + IAPP (consolidado)** | Textos legales | privacy, bias, transparency, safety, accountability, copyright | no |

### 3. Controls X2 - Factores Socioeconomicos E Institucionales

| canonical_name | rol | prioridad | tipo esperado | grano esperado | definicion | fuente preferida | fuentes alternativas | alias de busqueda en datasets | proxy permitida |
|---|---|---|---|---|---|---|---|---|---|
| gdp_per_capita_ppp | control | core | float | pais-anio | PIB per capita PPP | World Bank WDI | IMF, OECD | gdp per capita ppp, ny.gdp.pcap.pp.cd | no |
| rd_expenditure | control | core | float | pais-anio | Gasto en I+D como porcentaje del PIB | World Bank WDI | UNESCO, OECD | r&d expenditure, research and development expenditure, gb.xpd.rsdv.gd.zs | no |
| internet_penetration | control | core | float | pais-anio | Porcentaje de poblacion con acceso a internet | World Bank WDI | ITU | internet users, internet penetration, it.net.user.zs | no |
| tertiary_education | control | core | float | pais-anio | Matricula en educacion terciaria | World Bank WDI | UNESCO | tertiary education, tertiary enrollment, se.ter.enrr | no |
| gii_score | control | high | float | pais-anio o pais | Global Innovation Index | WIPO | Tortoise si no hay mejor opcion | innovation index, gii score | no |
| regulatory_quality | control | **core (confounder)** | float | pais-anio | Calidad regulatoria general (WGI estimate, -2.5 a +2.5) | World Bank WGI (db=3, GOV_WGI_RQ.EST) | ninguno | regulatory quality, regulation quality | no |
| rule_of_law | control | **core (confounder)** | float | pais-anio | Estado de derecho (WGI estimate, -2.5 a +2.5) | World Bank WGI (db=3, GOV_WGI_RL.EST) | ninguno | rule of law, rol | no |
| has_gdpr_like_law | control | **core (confounder)** | binary | pais | Pais tiene ley nacional comprehensiva de proteccion de datos | Codificacion manual (DLA Piper 2025) | UNCTAD DP Tracker | gdpr-like law, data protection law, dp law | no |
| gdpr_similarity_level | control | **core (confounder)** | ordinal (0-3) | pais | Nivel de alineacion con GDPR: 1=sectoral, 2=comprehensive, 3=EU/EEA/adequacy | Codificacion manual (DLA Piper 2025) + EU adequacy decisions list | UNCTAD DP Tracker | gdpr similarity, gdpr alignment | no |
| ict_service_exports_pct | control | robustness (digital economy) | float | pais-anio | Exportaciones de servicios ICT (% de exportaciones de servicios). Proxy de produccion/exportacion digital | World Bank WDI (BX.GSR.CCIS.ZS) | UNCTAD (no country-level) | ict services exports, bx.gsr.ccis.zs | no |
| high_tech_exports_pct | control | robustness (digital economy) | float | pais-anio | Exportaciones de alta tecnologia (% de manufactureras). Proxy de manufactura tech-avanzada | World Bank WDI (TX.VAL.TECH.MF.ZS) | OECD STI | high tech exports, tx.val.tech.mf.zs | no |
| fh_total_score | control | robustness (regimen politico) | int (0-100) | pais | Freedom in the World total (Political Rights + Civil Liberties) | Freedom House FITW 2025 (manual) | V-Dem, Polity5 | freedom house, fh score, fitw | no |
| fh_democracy_level | control | robustness (regimen politico) | ordinal (0-2) | pais | Categorical regime level: 0=NF, 1=PF, 2=F | Freedom House FITW 2025 (manual) | V-Dem | fh status, democracy level | no |
| legal_origin | control | robustness (tradicion juridica) | categorical (5) | pais | Familia legal La Porta 2008: English, French, German, Scandinavian, Socialist | La Porta-LS 2008 Appendix (manual, CBR Leximetric para ambiguos) | Djankov 2003 | legal origin, legal family, common law, civil law | no |
| is_common_law | control | robustness (tradicion juridica) | binary | pais | 1 si legal_origin == English, 0 si no | Derivado de legal_origin | ninguno | common law binary | no |
| government_effectiveness | control | robustness | float | pais-anio | Efectividad gubernamental (WGI estimate) | World Bank WGI (db=3, GOV_WGI_GE.EST) | ninguno preferente | government effectiveness | no |
| control_of_corruption | control | robustness | float | pais-anio | Control de corrupcion (WGI estimate) | World Bank WGI (db=3, GOV_WGI_CC.EST) | ninguno | control of corruption, cc | no |
| oecd_member | control | high | binary | pais | Pertenencia a la OECD | OECD | Manual | oecd member | no |
| region | control | high | categorical | pais | Region geografica normalizada | Manual | World Bank region, UN region | region, subregion, geographic area | no |

## Variables Profesionales Opcionales Recomendadas

Estas variables no son obligatorias para responder la pregunta central, pero pueden elevar la calidad del estudio y mejorar robustez, clusters o EDA.

| canonical_name | rol | prioridad | definicion | fuentes posibles | alias de busqueda |
|---|---|---|---|---|---|
| ai_talent_concentration | extra | medium | Concentracion de talento IA en la fuerza laboral | Stanford HAI, LinkedIn | ai talent concentration |
| ai_skill_penetration | extra | medium | Penetracion de habilidades IA | Stanford HAI, LinkedIn | ai skill penetration |
| ai_job_postings_share | extra | medium | Participacion de empleos IA en avisos laborales | Stanford HAI | ai job postings |
| notable_ml_models | extra | low | Numero de modelos ML notables por pais | Stanford HAI | notable machine learning models |
| public_ai_procurement | extra | medium | Gasto publico o contratos publicos en IA | Stanford, OECD | ai contracts, ai procurement |
| ai_legislative_activity | extra | low | Numero de bills o menciones legislativas sobre IA | Stanford, OECD | ai bills, legislative mentions |

## Variables Para La Capa NLP Legal

| canonical_name | rol | prioridad | tipo | definicion | fuente esperada |
|---|---|---|---|---|---|
| jurisdiction_name | identificador | core | string | Nombre de pais o jurisdiccion | Textos legales |
| jurisdiction_iso3 | identificador | core | string | ISO3 si aplica | Textos legales |
| law_id | identificador | core | string | ID interno del documento legal | Textos legales |
| law_title | metadata | core | string | Titulo oficial de la norma | Textos legales |
| law_year | metadata | core | integer | Anio de promulgacion | Textos legales |
| law_text_raw | feature_nlp | core | text | Texto crudo de la ley | Textos legales |
| law_language | metadata | core | string | Idioma del documento | Textos legales |
| law_type | metadata | high | string | Ley, reglamento, decreto, estrategia, guidance | Textos legales |
| law_url_source | metadata | high | string | URL de procedencia | Textos legales |
| nlp_topic_risk | derived | high | float | Intensidad del topico riesgo | Derivada |
| nlp_topic_transparency | derived | high | float | Intensidad del topico transparencia | Derivada |
| nlp_topic_innovation | derived | high | float | Intensidad del topico innovacion | Derivada |
| nlp_topic_sanctions | derived | high | float | Intensidad del topico sanciones | Derivada |

## Mapa De Fuentes Esperadas Contra Variables

| fuente | variables core esperadas | variables opcionales esperadas |
|---|---|---|
| Stanford HAI / AI Index / Vibrancy Tool | ai_vibrancy_score, ai_investment_vc, ai_patents, ai_startups | ai_talent_concentration, ai_skill_penetration, ai_job_postings_share, notable_ml_models |
| Microsoft AI Diffusion | ai_adoption_rate | proxies de adopcion sectorial |
| Oxford Insights AI Readiness | ai_readiness_score | subcomponentes de readiness |
| OECD AI Policy Observatory | has_ai_law, regulatory_approach, year_enacted | ai_legislative_activity, estrategia nacional, procurement |
| IAPP Global AI Law Tracker | has_ai_law, regulatory_approach, year_enacted | enforcement_level, intensidad regulatoria |
| World Bank WDI + WGI | gdp_per_capita_ppp, rd_expenditure, internet_penetration, tertiary_education, government_effectiveness + 5 WGI | metadata WGI (SE, NSRC); otras covariables macro si se justifican |
| WIPO / GII | gii_score | subcomponentes de innovacion |
| Textos legales | thematic_coverage, enforcement_level, variables NLP | topicos latentes, embeddings, similitud documental |

## Protocolo De Decision Cuando Se Revise Un Dataset Nuevo

Para cada dataset importado, seguir esta secuencia exacta:

1. Identificar su grano real.
2. Identificar si trae pais, region o global.
3. Detectar si tiene anio explicito.
4. Buscar coincidencias con los `canonical_name` de esta guia.
5. Marcar cada coincidencia como una de estas categorias:
   - `exacta`
   - `proxy fuerte`
   - `proxy parcial`
   - `no util`
6. Registrar las columnas candidatas con su nombre original.
7. No transformar el raw original.
8. Extraer solo las columnas utiles a `data/interim/`.
9. Documentar la decision de mapeo en el notebook de recoleccion.

## Regla De Priorizacion Para Construir El Dataset Maestro

### Nota metodologica sobre fuentes multiarchivo

No todas las fuentes admiten un unico conteo simple de `paises raw` o `paises estudio`.

- Stanford AI Index es el caso principal: entra al proyecto como multiples archivos de figuras con coberturas distintas por variable.
- En esa situacion, cualquier tabla resumen debe evitar usar `-` como si significara `sin datos`.
- La forma correcta de resumir estas fuentes es una de estas dos:
   - `cobertura por variable`, o
   - `cobertura en la union de archivos auditados`.

Para Stanford, la referencia documental vigente es:
- 7 archivos Y principales auditados
- 96 labels geograficos raw
- 88 ISO3 mapeables
- 86/86 paises del estudio cubiertos en la union de variables

Si dos variables compiten para representar el mismo constructo, priorizar en este orden:

1. Variable exacta definida por la metodologia.
2. Serie pais-anio comparable internacionalmente.
3. Corte transversal pais con anio claro.
4. Proxy fuerte internacionalmente comparable.
5. Proxy parcial solo si no existe nada mejor.

## Convencion De Nombres Para Variables Finales

Usar siempre nombres en `snake_case` y evitar nombres ambiguos.

Ejemplos correctos:
- `ai_investment_vc`
- `ai_patents_per_100k`
- `regulatory_intensity`
- `government_effectiveness`

Ejemplos incorrectos:
- `investment`
- `score_final`
- `law_data`
- `variable1`

## Regla De Oro

Cada columna final del dataset maestro debe responder al menos una de estas preguntas:

1. Mide desarrollo del ecosistema de IA?
2. Mide regulacion de IA?
3. Controla un factor estructural relevante?
4. Mejora la interpretacion politica del estudio sin distorsionar la pregunta central?

Si la respuesta es no, no debe entrar al dataset maestro.
