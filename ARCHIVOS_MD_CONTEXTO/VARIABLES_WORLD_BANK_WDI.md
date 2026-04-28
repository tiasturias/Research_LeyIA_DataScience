# Variables World Bank WDI (World Development Indicators)

## Proposito

Este documento resume, en una version operativa, que variables del estudio fueron extraidas desde la fuente World Bank WDI via la API `wbgapi`.

Su objetivo es servir como referencia rapida para:
- saber que variables de la metodologia si estan en World Bank WDI;
- identificar el codigo de indicador exacto usado;
- conocer la cobertura real (paises, anios, missingness);
- distinguir entre variables core, complementarias y no disponibles;
- preparar la extraccion hacia tablas intermedias antes de limpieza.

## Fuente

- Fuente base: World Bank - World Development Indicators (WDI) + World Governance Indicators (WGI)
- API: `wbgapi` (wrapper oficial Python de la API del World Bank)
- Ubicacion local: `/Users/francoia/Documents/MIA/Proyecto Data-Science/research/data/raw/World Bank WDI/`
- Periodo extraido: 2013-2024
- Paises extraidos: 63 (seleccionados por tener cobertura en al menos 2 datasets de Stanford AI Index)

## Conclusion Ejecutiva

World Bank WDI aporta las **variables de control X2** del estudio: factores socioeconomicos e institucionales que permiten aislar el efecto de la regulacion de IA sobre el ecosistema.

Se extrajeron **20 indicadores analiticos** organizados en 4 bloques, mas **12 indicadores de metadata WGI**:
1. **Core X2** (4 variables): las variables de control obligatorias de la guia metodologica.
2. **Gobernanza WGI** (6 variables): indicadores de calidad institucional y gobernanza.
3. **Estructura economica** (7 variables): tamano, apertura y dinamica macroeconomica.
4. **Capital humano e infraestructura** (3 variables): educacion, conectividad y capacidad inventiva.
5. **Metadata WGI** (12 indicadores): errores estandar y numero de fuentes para auditar precision de los 6 estimadores WGI.

No aporta variables Y (targets de ecosistema IA) ni variables X1 (regulacion de IA).

## Variables Operativas Extraidas

### 1. Core X2 - Controles Obligatorios (Guia Metodologica)

| canonical_name | wb_indicator | tipo_metodologico | estado | descripcion_wb | paises | periodo | missingness_wide | archivo_tematico | observacion_metodologica |
|---|---|---|---|---|---|---|---|---|---|
| gdp_per_capita_ppp | NY.GDP.PCAP.PP.CD | X2 core | Disponible directo | GDP per capita, PPP (current international $) | 63 | 2013-2024 | 0.0% | wdi_core_controls.csv | Variable de control principal. Comparable internacionalmente. Sin datos faltantes. |
| rd_expenditure | GB.XPD.RSDV.GD.ZS | X2 core | Disponible directo | Research and development expenditure (% of GDP) | 62 | 2013-2023 | 27.6% | wdi_core_controls.csv | Missingness significativo. No todos los paises reportan I+D. Considerar imputacion en limpieza. |
| internet_penetration | IT.NET.USER.ZS | X2 core | Disponible directo | Individuals using the Internet (% of population) | 63 | 2013-2024 | 3.7% | wdi_core_controls.csv | Buena cobertura. Missingness minimo. |
| tertiary_education | SE.TER.ENRR | X2 core | Disponible directo | School enrollment, tertiary (% gross) | 62 | 2013-2024 | 13.6% | wdi_core_controls.csv | Missingness moderado. Algunos paises no reportan todos los anios. |

### 2. Gobernanza - World Governance Indicators (WGI)

| canonical_name | wb_indicator | tipo_metodologico | estado | descripcion_wb | paises | periodo | missingness_wide | archivo_tematico | observacion_metodologica |
|---|---|---|---|---|---|---|---|---|---|
| government_effectiveness | GE.EST | X2 high | Disponible directo | Government Effectiveness: Estimate | 63 | 2013-2023 | 8.3% | wdi_governance.csv | Variable de control prioritaria en la guia. Missingness solo por 2024 (WGI se publica con rezago). |
| regulatory_quality | RQ.EST | X2 complementario | Disponible directo | Regulatory Quality: Estimate | 63 | 2013-2023 | 8.3% | wdi_governance.csv | Mide calidad regulatoria general, no especifica de IA. Util para controlar capacidad institucional. |
| rule_of_law | RL.EST | X2 complementario | Disponible directo | Rule of Law: Estimate | 63 | 2013-2023 | 8.3% | wdi_governance.csv | Estado de derecho general. Relevante para enforcement regulatorio. |
| control_of_corruption | CC.EST | X2 complementario | Disponible directo | Control of Corruption: Estimate | 63 | 2013-2023 | 8.3% | wdi_governance.csv | Complemento de gobernanza. Puede correlacionar con enforcement de regulacion IA. |
| voice_accountability | VA.EST | X2 complementario | Disponible directo | Voice and Accountability: Estimate | 63 | 2013-2023 | 8.3% | wdi_governance.csv | Proxy de calidad democratica. Relevante para modelo regulatorio adoptado. |
| political_stability | PV.EST | X2 complementario | Disponible directo | Political Stability and Absence of Violence/Terrorism: Estimate | 63 | 2013-2023 | 8.3% | wdi_governance.csv | Estabilidad politica como condicion de base para regulacion e inversion en IA. |

### 3. Estructura Economica

| canonical_name | wb_indicator | tipo_metodologico | estado | descripcion_wb | paises | periodo | missingness_wide | archivo_tematico | observacion_metodologica |
|---|---|---|---|---|---|---|---|---|---|
| gdp_current_usd | NY.GDP.MKTP.CD | X2 complementario | Disponible directo | GDP (current US$) | 63 | 2013-2024 | 0.0% | wdi_economic_structure.csv | Tamano absoluto de la economia. Util para normalizar variables absolutas (inversion, patentes). |
| population | SP.POP.TOTL | X2 complementario | Disponible directo | Population, total | 63 | 2013-2024 | 0.0% | wdi_economic_structure.csv | Para normalizar per capita. Cobertura completa. |
| labor_force | SL.TLF.TOTL.IN | X2 complementario | Disponible directo | Labor force, total | 63 | 2013-2024 | 0.0% | wdi_economic_structure.csv | Tamano del mercado laboral. Relevante para talento IA disponible. |
| fdi_net_inflows | BX.KLT.DINV.CD.WD | X2 complementario | Disponible directo | Foreign direct investment, net inflows (BoP, current US$) | 63 | 2013-2024 | 0.0% | wdi_economic_structure.csv | Proxy de atractivo para inversion extranjera. Puede relacionarse con inversion en IA. |
| exports_pct_gdp | NE.EXP.GNFS.ZS | X2 complementario | Disponible directo | Exports of goods and services (% of GDP) | 62 | 2013-2024 | 1.7% | wdi_economic_structure.csv | Apertura comercial. Paises mas abiertos pueden tener mayor difusion tecnologica. |
| inflation_consumer_prices | FP.CPI.TOTL.ZG | X2 complementario | Disponible directo | Inflation, consumer prices (annual %) | 63 | 2013-2024 | 0.7% | wdi_economic_structure.csv | Estabilidad macroeconomica. Missingness minimo. |
| unemployment_rate | SL.UEM.TOTL.ZS | X2 complementario | Disponible directo | Unemployment, total (% of total labor force) (modeled ILO estimate) | 63 | 2013-2024 | 0.0% | wdi_economic_structure.csv | Condicion del mercado laboral. Cobertura completa. |

### 4. Capital Humano e Infraestructura

| canonical_name | wb_indicator | tipo_metodologico | estado | descripcion_wb | paises | periodo | missingness_wide | archivo_tematico | observacion_metodologica |
|---|---|---|---|---|---|---|---|---|---|
| education_expenditure_pct_gdp | SE.XPD.TOTL.GD.ZS | X2 complementario | Disponible directo | Government expenditure on education, total (% of GDP) | 62 | 2013-2024 | 24.9% | wdi_human_capital_infra.csv | Missingness alto. Muchos paises no reportan este indicador anualmente. Considerar imputacion. |
| mobile_subscriptions_per100 | IT.CEL.SETS.P2 | X2 complementario | Disponible directo | Mobile cellular subscriptions (per 100 people) | 63 | 2013-2023 | 8.5% | wdi_human_capital_infra.csv | Complemento de infraestructura digital junto a internet_penetration. |
| patent_applications_residents | IP.PAT.RESD | X2 complementario | Disponible directo | Patent applications, residents | 62 | 2013-2021 | 29.4% | wdi_human_capital_infra.csv | Missingness alto. Serie corta (hasta 2021). Proxy de capacidad inventiva general, no especifica de IA. |

### 5. Metadata WGI — Calidad De Medicion

Estos indicadores **no son variables analiticas X2**. Son metadata que mide la precision y robustez de los 6 estimadores WGI. Se guardan en `wdi_governance_metadata.csv` (separado de los outputs analiticos).

| canonical_name | wb_indicator | tipo_metodologico | estado | descripcion_wb | paises | periodo | archivo_tematico | observacion_metodologica |
|---|---|---|---|---|---|---|---|---|
| government_effectiveness_se | GE.STD.ERR | Metadata | Disponible directo | Government Effectiveness: Standard Error | 63 | 2013-2023 | wdi_governance_metadata.csv | Error estandar del estimador compuesto. Mide precision. |
| regulatory_quality_se | RQ.STD.ERR | Metadata | Disponible directo | Regulatory Quality: Standard Error | 63 | 2013-2023 | wdi_governance_metadata.csv | Error estandar del estimador compuesto. |
| rule_of_law_se | RL.STD.ERR | Metadata | Disponible directo | Rule of Law: Standard Error | 63 | 2013-2023 | wdi_governance_metadata.csv | Error estandar del estimador compuesto. |
| control_of_corruption_se | CC.STD.ERR | Metadata | Disponible directo | Control of Corruption: Standard Error | 63 | 2013-2023 | wdi_governance_metadata.csv | Error estandar del estimador compuesto. |
| voice_accountability_se | VA.STD.ERR | Metadata | Disponible directo | Voice and Accountability: Standard Error | 63 | 2013-2023 | wdi_governance_metadata.csv | Error estandar del estimador compuesto. |
| political_stability_se | PV.STD.ERR | Metadata | Disponible directo | Political Stability: Standard Error | 63 | 2013-2023 | wdi_governance_metadata.csv | Error estandar del estimador compuesto. |
| government_effectiveness_nsrc | GE.NO.SRC | Metadata | Disponible directo | Government Effectiveness: Number of Sources | 63 | 2013-2023 | wdi_governance_metadata.csv | Cantidad de fuentes subyacentes. Mide robustez del compuesto. |
| regulatory_quality_nsrc | RQ.NO.SRC | Metadata | Disponible directo | Regulatory Quality: Number of Sources | 63 | 2013-2023 | wdi_governance_metadata.csv | Cantidad de fuentes subyacentes. |
| rule_of_law_nsrc | RL.NO.SRC | Metadata | Disponible directo | Rule of Law: Number of Sources | 63 | 2013-2023 | wdi_governance_metadata.csv | Cantidad de fuentes subyacentes. |
| control_of_corruption_nsrc | CC.NO.SRC | Metadata | Disponible directo | Control of Corruption: Number of Sources | 63 | 2013-2023 | wdi_governance_metadata.csv | Cantidad de fuentes subyacentes. |
| voice_accountability_nsrc | VA.NO.SRC | Metadata | Disponible directo | Voice and Accountability: Number of Sources | 63 | 2013-2023 | wdi_governance_metadata.csv | Cantidad de fuentes subyacentes. |
| political_stability_nsrc | PV.NO.SRC | Metadata | Disponible directo | Political Stability: Number of Sources | 63 | 2013-2023 | wdi_governance_metadata.csv | Cantidad de fuentes subyacentes. |

### Indicadores WGI Evaluados Y Excluidos

| wb_indicator | descripcion | razon_exclusion |
|---|---|---|
| `*.PER.RNK` | Percentile Rank (0-100) | Transformacion monotona de `.EST`. Introduce redundancia perfecta (multicolinealidad = 1). |
| `*.PER.RNK.LOWER` | Lower Bound 90% CI | Derivado de `.STD.ERR`. Redundante si ya se tiene el error estandar. |
| `*.PER.RNK.UPPER` | Upper Bound 90% CI | Derivado de `.STD.ERR`. Redundante si ya se tiene el error estandar. |

## Variables De La Guia No Disponibles En World Bank WDI

| variable_estudio | tipo_metodologico | fuente_esperada | observacion |
|---|---|---|---|
| ai_vibrancy_score | Y target | Stanford HAI Global AI Vibrancy Tool | WDI no contiene variables de ecosistema IA. |
| ai_investment_vc | Y target | Stanford HAI | WDI no contiene variables de ecosistema IA. |
| ai_adoption_rate | Y target | Microsoft AI Diffusion | WDI no contiene variables de ecosistema IA. |
| ai_patents | Y target | Stanford HAI | WDI tiene patentes generales (IP.PAT.RESD), no especificas de IA. |
| ai_startups | Y target | Stanford HAI | WDI no contiene variables de ecosistema IA. |
| ai_readiness_score | Y target | Oxford Insights | WDI no contiene variables de ecosistema IA. |
| has_ai_law | X1 feature | OECD / IAPP | WDI no contiene regulacion de IA. |
| regulatory_approach | X1 feature | OECD / IAPP | WDI no contiene regulacion de IA. |
| regulatory_intensity | X1 feature | Codificacion manual | WDI no contiene regulacion de IA. |
| year_enacted | X1 feature | OECD / IAPP | WDI no contiene regulacion de IA. |
| enforcement_level | X1 feature | Codificacion manual | WDI no contiene regulacion de IA. |
| thematic_coverage | X1 feature | Codificacion manual | WDI no contiene regulacion de IA. |
| gii_score | X2 high | WIPO | Indicador compuesto de innovacion. No disponible en WDI. |
| oecd_member | X2 high | OECD / Manual | No es un indicador WDI. Debe construirse aparte. |
| region | X2 high | Manual / WB classification | No extraido como indicador. Puede derivarse de la clasificacion WB. |

## Archivos Generados

| archivo | contenido | formato | filas | columnas |
|---|---|---|---|---|
| `wdi_all_indicators_long.csv` | Todos los indicadores en formato long | iso3, year, country_name, value, wb_indicator, canonical_name | ~12,000 | 6 |
| `wdi_all_indicators_wide.csv` | Todos los indicadores en formato wide | iso3, country_name, year + 20 columnas de indicadores | 756 | 23 |
| `wdi_core_controls.csv` | 4 variables core X2 | long | ~2,700 | 6 |
| `wdi_governance.csv` | 6 indicadores WGI (estimadores) | long | ~4,200 | 6 |
| `wdi_governance_metadata.csv` | 12 indicadores WGI metadata (SE + NSRC) | long | ~8,300 | 6 |
| `wdi_economic_structure.csv` | 7 indicadores macro | long | ~5,300 | 6 |
| `wdi_human_capital_infra.csv` | 3 indicadores capital humano | long | ~1,800 | 6 |

## Paises Cubiertos (63)

Los paises fueron seleccionados por tener cobertura en al menos 2 datasets de Stanford AI Index (variables Y), garantizando que ningun pais quede sin target.

| iso3 | pais |
|---|---|
| ARE | United Arab Emirates |
| ARG | Argentina |
| AUS | Australia |
| AUT | Austria |
| BEL | Belgium |
| BGR | Bulgaria |
| BRA | Brazil |
| CAN | Canada |
| CHE | Switzerland |
| CHL | Chile |
| CHN | China |
| CMR | Cameroon |
| COL | Colombia |
| CRI | Costa Rica |
| CYP | Cyprus |
| CZE | Czechia |
| DEU | Germany |
| DNK | Denmark |
| EGY | Egypt |
| ESP | Spain |
| EST | Estonia |
| FIN | Finland |
| FRA | France |
| GBR | United Kingdom |
| GRC | Greece |
| HRV | Croatia |
| HUN | Hungary |
| IDN | Indonesia |
| IND | India |
| IRL | Ireland |
| ISL | Iceland |
| ISR | Israel |
| ITA | Italy |
| JOR | Jordan |
| JPN | Japan |
| KAZ | Kazakhstan |
| KOR | South Korea |
| LTU | Lithuania |
| LUX | Luxembourg |
| LVA | Latvia |
| MEX | Mexico |
| MYS | Malaysia |
| NGA | Nigeria |
| NLD | Netherlands |
| NOR | Norway |
| NZL | New Zealand |
| PER | Peru |
| PHL | Philippines |
| POL | Poland |
| PRT | Portugal |
| ROU | Romania |
| RUS | Russia |
| SAU | Saudi Arabia |
| SGP | Singapore |
| SVN | Slovenia |
| SWE | Sweden |
| THA | Thailand |
| TUN | Tunisia |
| TUR | Turkey |
| URY | Uruguay |
| USA | United States |
| VNM | Vietnam |
| ZAF | South Africa |

## Alertas De Calidad Para La Fase De Limpieza

1. **rd_expenditure** (27.6% missing): no todos los paises reportan gasto en I+D anualmente. Considerar imputacion por interpolacion temporal o last-observation-carried-forward.
2. **patent_applications_residents** (29.4% missing): serie corta (hasta 2021) y cobertura parcial. Evaluar si vale la pena mantenerla o si ai_patents de Stanford la reemplaza mejor.
3. **education_expenditure_pct_gdp** (24.9% missing): reportado irregularmente. Evaluar imputacion o exclusion si no agrega valor al modelo.
4. **Indicadores WGI** (8.3% missing cada uno): el missingness se debe a que WGI 2024 aun no estaba publicado al momento de la extraccion. No es un problema real de cobertura.
5. **Taiwan (TWN)**: excluido del dataset final porque World Bank no reporta datos para Taiwan. Si Taiwan es importante para el estudio, habra que buscar datos de fuentes alternativas (IMF, CIA Factbook).

## Recomendacion Operativa Para Este Estudio

Para el dataset maestro, la prioridad de uso de estas variables es:

1. **Core X2 obligatorios**: `gdp_per_capita_ppp`, `rd_expenditure`, `internet_penetration`, `tertiary_education` — deben estar en el modelo final.
2. **Gobernanza clave**: `government_effectiveness` — requerido por la guia metodologica. Los otros 5 indicadores WGI son complementarios para robustez.
3. **Estructura economica de soporte**: `gdp_current_usd`, `population` — para normalizar variables absolutas.
4. **Complementarios para robustez**: el resto segun necesidad del modelo y diagnostico de multicolinealidad.

## Regla De Uso

- Usar `data/raw/World Bank WDI/` solo como fuente cruda.
- No modificar estos archivos.
- Cuando se extraigan variables concretas hacia el dataset maestro, guardar el resultado en `data/interim/`.
- Las decisiones de imputacion, normalizacion o exclusion de variables deben documentarse en `notebooks/02_limpieza.ipynb`.
