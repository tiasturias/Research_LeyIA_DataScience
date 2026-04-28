# Nigeria (NGA) - Dossier consolidado Legal-IA

## 1. Proposito analitico
Existe una asociacion estadisticamente significativa entre las caracteristicas de la regulacion de inteligencia artificial de un pais y el desarrollo de su ecosistema de IA, despues de controlar por factores socioeconomicos e institucionales.

El estudio busca informar la discusion chilena sobre Ley Marco de IA (Boletin 16821-19) con evidencia comparativa internacional.

- Diseno del estudio: Cross-section comparativo 2025 con 86 paises y una submuestra ADE de 73.
- Dataset base: data/interim/sample_ready_cross_section.csv
- Tier recomendada: complete_confounded

## 2. Estado del pais dentro del estudio
- Grupo regulatorio: strategy_only
- Tiene corpus legal manual: Si
- Documentos legales identificados: 0
- Paginas totales del corpus legal: 0
- complete_principal: Si
- complete_confounded: Si
- complete_digital: Si
- complete_regime: Si
- complete_legal_tradition: Si

## 3. Datos recopilados por fuente y proposito
### IAPP + OECD (X1 regulatorio)
- Proposito: Caracterizar el marco regulatorio de IA del pais.
- Tiene ley IA: 0
- Enfoque regulatorio: strategy_led
- Intensidad regulatoria: 3
- Enforcement: low
- Cobertura tematica: 7
- Grupo regulatorio: strategy_only
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.127722651 (ref. 2024.0)
- Startups IA acumuladas: 8.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 9.3 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 50.79 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 21.0815209410651 (ref. 2025.0)
- Region: Sub-Saharan Africa

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 9086.87550609627 (ref. 2024.0)
- Penetracion internet: 39.2136 (ref. 2023.0)
- Gasto I+D: 0.28444 (ref. 2019.0)
- Exportaciones ICT: 4.03817725408016 (ref. 2024.0)
- Exportaciones high-tech: 2.71167186435579 (ref. 2024.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: -0.936865150928497 (ref. 2023.0)
- Rule of law: -0.887689292430878 (ref. 2023.0)
- Government effectiveness: -0.847906708717346 (ref. 2023.0)
- Control of corruption: -1.04097437858582 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2023
- Tiene DPA: 1
- Enforcement activo DP: 1

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 43 (ref. 2025)
- FH status: PF
- Nivel democracia FH: 1

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: English
- Common law: 1

## 4. Perfil cuantitativo del pais
- Region: Sub-Saharan Africa
- OECD member: No
- Legal origin: English
- Common law: Si
- Poblacion: 232679478.0
- GDP actual USD: 252261880141.151
- AI readiness: 50.79 (ref. 2025)
- Adopcion IA: 9.3% (ref. H2_2025)
- Inversion IA acumulada: 0.1277 (ref. 2024.0)
- Startups IA acumuladas: 8.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 9086.8755 (ref. 2024.0)
- GII score: 21.0815 (ref. 2025.0)
- Internet penetration: 39.2136% (ref. 2023.0)
- R&D expenditure: 0.2844 (ref. 2019.0)
- Tertiary education: N/A
- Regulatory quality: -0.9369 (ref. 2023.0)
- Rule of law: -0.8877 (ref. 2023.0)
- Freedom House: 43 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: strategy_only
- Tiene ley IA: No
- Enfoque: strategy_led
- Intensidad: 3 (ref. 0-10)
- Enforcement: low
- Cobertura tematica: 7 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 2
- Tiene DPA: Si

## 6. Inventario de documentos legales
No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.

## 7. Analisis cualitativo disponible
- meta_analysis chars: 722
- SOURCES chars: 0
- CANDIDATES chars: 0
- FINDINGS chars: 0
- Preview meta analisis: # NGA — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** strategy_only - **Intensidad:** 3/10 - **Enfoque:** strategy_led - **Enforcement:** low - **Cobertura temática:** 7/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 50.79/100 - **Adopción:** 9.3% - **Inversión:** USD 0.1277B - **Startups:** 8.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** -0.9369 - **Rule of Law:** -0.8877 - **Freedom House:** 43/100 (PF)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
