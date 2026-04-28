# Jordania (JOR) - Dossier consolidado Legal-IA

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
- Intensidad regulatoria: 2
- Enforcement: low
- Cobertura tematica: 3
- Grupo regulatorio: strategy_only
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.0086 (ref. 2024.0)
- Startups IA acumuladas: 2.0 (ref. 2024.0)
- Patentes IA por 100k: 0.01748372 (ref. 2023.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 27.0 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 56.07 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 29.6936103734472 (ref. 2025.0)
- Region: Northern Africa and Western Asia

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 10821.4909765317 (ref. 2024.0)
- Penetracion internet: 92.5344 (ref. 2023.0)
- Educacion terciaria: 35.9184001120427 (ref. 2024.0)
- Exportaciones ICT: 0.509793399517038 (ref. 2024.0)
- Exportaciones high-tech: 2.08415985427159 (ref. 2023.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: 0.217705458402634 (ref. 2023.0)
- Rule of law: 0.257768124341965 (ref. 2023.0)
- Government effectiveness: 0.386213511228561 (ref. 2023.0)
- Control of corruption: 0.0886586904525757 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2023
- Tiene DPA: 0
- Enforcement activo DP: 0

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 33 (ref. 2025)
- FH status: NF
- Nivel democracia FH: 0

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: French
- Common law: 0

## 4. Perfil cuantitativo del pais
- Region: Northern Africa and Western Asia
- OECD member: No
- Legal origin: French
- Common law: No
- Poblacion: 11552876.0
- GDP actual USD: 53352289577.4648
- AI readiness: 56.07 (ref. 2025)
- Adopcion IA: 27.0% (ref. H2_2025)
- Inversion IA acumulada: 0.0086 (ref. 2024.0)
- Startups IA acumuladas: 2.0 (ref. 2024.0)
- Patentes IA por 100k: 0.0175 (ref. 2023.0)
- GDP per capita PPP: 10821.491 (ref. 2024.0)
- GII score: 29.6936 (ref. 2025.0)
- Internet penetration: 92.5344% (ref. 2023.0)
- R&D expenditure: N/A
- Tertiary education: 35.9184 (ref. 2024.0)
- Regulatory quality: 0.2177 (ref. 2023.0)
- Rule of law: 0.2578 (ref. 2023.0)
- Freedom House: 33 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: strategy_only
- Tiene ley IA: No
- Enfoque: strategy_led
- Intensidad: 2 (ref. 0-10)
- Enforcement: low
- Cobertura tematica: 3 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 2
- Tiene DPA: No

## 6. Inventario de documentos legales
No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.

## 7. Analisis cualitativo disponible
- meta_analysis chars: 721
- SOURCES chars: 0
- CANDIDATES chars: 0
- FINDINGS chars: 0
- Preview meta analisis: # JOR — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** strategy_only - **Intensidad:** 2/10 - **Enfoque:** strategy_led - **Enforcement:** low - **Cobertura temática:** 3/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 56.07/100 - **Adopción:** 27.0% - **Inversión:** USD 0.0086B - **Startups:** 2.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** 0.2177 - **Rule of Law:** 0.2578 - **Freedom House:** 33/100 (NF)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
