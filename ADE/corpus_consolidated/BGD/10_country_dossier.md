# Banglades (BGD) - Dossier consolidado Legal-IA

## 1. Proposito analitico
Existe una asociacion estadisticamente significativa entre las caracteristicas de la regulacion de inteligencia artificial de un pais y el desarrollo de su ecosistema de IA, despues de controlar por factores socioeconomicos e institucionales.

El estudio busca informar la discusion chilena sobre Ley Marco de IA (Boletin 16821-19) con evidencia comparativa internacional.

- Diseno del estudio: Cross-section comparativo 2025 con 86 paises y una submuestra ADE de 73.
- Dataset base: data/interim/sample_ready_cross_section.csv
- Tier recomendada: complete_confounded

## 2. Estado del pais dentro del estudio
- Grupo regulatorio: strategy_only
- Tiene corpus legal manual: Si
- Documentos legales identificados: 4
- Paginas totales del corpus legal: 55
- complete_principal: Si
- complete_confounded: Si
- complete_digital: No
- complete_regime: Si
- complete_legal_tradition: Si

## 3. Datos recopilados por fuente y proposito
### IAPP + OECD (X1 regulatorio)
- Proposito: Caracterizar el marco regulatorio de IA del pais.
- Tiene ley IA: 0
- Enfoque regulatorio: strategy_led
- Intensidad regulatoria: 2
- Enforcement: low
- Cobertura tematica: 4
- Grupo regulatorio: strategy_only
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.0022 (ref. 2024.0)
- Startups IA acumuladas: 1.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 7.1 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 48.37 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 20.951047653279 (ref. 2025.0)
- Region: Central and Southern Asia

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 9646.76984383255 (ref. 2024.0)
- Penetracion internet: 53.42171316 (ref. 2024.0)
- Educacion terciaria: 23.7295608009814 (ref. 2024.0)
- Exportaciones ICT: 9.51203440588108 (ref. 2024.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: -0.9009111 (ref. 2023.0)
- Rule of law: -0.9020256 (ref. 2023.0)
- Government effectiveness: -0.5574534 (ref. 2023.0)
- Control of corruption: -1.1987203 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2023
- Tiene DPA: 0
- Enforcement activo DP: 0

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 40 (ref. 2025)
- FH status: PF
- Nivel democracia FH: 1

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: English
- Common law: 1

### Corpus legal manual por pais
- Proposito: Aportar evidencia documental, citas, inventario y hallazgos diferenciales del caso nacional.
- 05_sources.md: disponible
- 06_candidates.md: disponible
- 07_findings.md: disponible

## 4. Perfil cuantitativo del pais
- Region: Central and Southern Asia
- OECD member: No
- Legal origin: English
- Common law: Si
- Poblacion: 173562364.0
- GDP actual USD: 450119432068.852
- AI readiness: 48.37 (ref. 2025)
- Adopcion IA: 7.1% (ref. H2_2025)
- Inversion IA acumulada: 0.0022 (ref. 2024.0)
- Startups IA acumuladas: 1.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 9646.7698 (ref. 2024.0)
- GII score: 20.951 (ref. 2025.0)
- Internet penetration: 53.4217% (ref. 2024.0)
- R&D expenditure: N/A
- Tertiary education: 23.7296 (ref. 2024.0)
- Regulatory quality: -0.9009 (ref. 2023.0)
- Rule of law: -0.902 (ref. 2023.0)
- Freedom House: 40 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: strategy_only
- Tiene ley IA: No
- Enfoque: strategy_led
- Intensidad: 2 (ref. 0-10)
- Enforcement: low
- Cobertura tematica: 4 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 2
- Tiene DPA: No

## 6. Inventario de documentos legales
El corpus legal del pais contiene 4 documentos identificados.
- Doc 1: National Strategy for Artificial Intelligence — Bangladesh | tipo=strategy | fecha=2020-03 | paginas=55
- Doc 2: National AI Policy Bangladesh 2026-2030 (DRAFT V1.1) | tipo=policy_draft | fecha=2026-01 | paginas=
- Doc 3: Bangladesh National AI Policy 2026-2030 (Draft v2) | tipo=policy_draft | fecha=2026-02-09 | paginas=
- Doc 4: Bangladesh Artificial Intelligence Readiness Assessment Report | tipo=readiness_assessment | fecha=2025-11 | paginas=

## 7. Analisis cualitativo disponible
- meta_analysis chars: 3107
- SOURCES chars: 7053
- CANDIDATES chars: 16337
- FINDINGS chars: 5668
- Preview hallazgo diferencial: # BGD — Hallazgo Diferencial  ## 1. Tesis del hallazgo diferencial  **Bangladesh transita de `strategy_only` a `soft_framework` mediante el National AI Policy 2026-2030 (Draft V2.0): marco risk-based completo (4 niveles: prohibited/high/limited/low), AIAs mandatorios, strict liability para high-risk, prohibiciones explícitas (social scoring, mass surveillance), y pathway declarado a AI Act para 2028. Es el caso de "emerging soft_framework con trajectory legislativa formal" en el corpus — comparable a GHA y MNG en el mismo cluster, pero con marco más denso y fecha de AI Act comprometidas.**  ---  ## 2. Evidencia cuantitativa — densidad del corpus  | Métrica | Valor | Cálculo | |---|---|---| | # documentos totales | 5 | count(manifest.csv) | | # binding (ley IA) | 0 | Sin ley vigente | | # p

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
