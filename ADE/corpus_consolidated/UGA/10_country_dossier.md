# Uganda (UGA) - Dossier consolidado Legal-IA

## 1. Proposito analitico
Existe una asociacion estadisticamente significativa entre las caracteristicas de la regulacion de inteligencia artificial de un pais y el desarrollo de su ecosistema de IA, despues de controlar por factores socioeconomicos e institucionales.

El estudio busca informar la discusion chilena sobre Ley Marco de IA (Boletin 16821-19) con evidencia comparativa internacional.

- Diseno del estudio: Cross-section comparativo 2025 con 86 paises y una submuestra ADE de 73.
- Dataset base: data/interim/sample_ready_cross_section.csv
- Tier recomendada: complete_confounded

## 2. Estado del pais dentro del estudio
- Grupo regulatorio: soft_framework
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
- Enfoque regulatorio: light_touch
- Intensidad regulatoria: 1
- Cobertura tematica: 1
- Grupo regulatorio: soft_framework
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.0094 (ref. 2024.0)
- Startups IA acumuladas: 3.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 6.8 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 35.76 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 17.0672701323701 (ref. 2025.0)
- Region: Sub-Saharan Africa

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 3273.2671741364 (ref. 2024.0)
- Penetracion internet: 8.949831061 (ref. 2024.0)
- Gasto I+D: 0.4383 (ref. 2023.0)
- Exportaciones ICT: 1.89162479943853 (ref. 2024.0)
- Exportaciones high-tech: 1.91593833437355 (ref. 2024.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: -0.500208099999999 (ref. 2023.0)
- Rule of law: -0.752792999999999 (ref. 2023.0)
- Government effectiveness: -0.4315787 (ref. 2023.0)
- Control of corruption: -0.996690299999999 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2019
- Tiene DPA: 1
- Enforcement activo DP: 1

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 35 (ref. 2025)
- FH status: NF
- Nivel democracia FH: 0

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: English
- Common law: 1

## 4. Perfil cuantitativo del pais
- Region: Sub-Saharan Africa
- OECD member: No
- Legal origin: English
- Common law: Si
- Poblacion: 50015092.0
- GDP actual USD: 53911907086.1525
- AI readiness: 35.76 (ref. 2025)
- Adopcion IA: 6.8% (ref. H2_2025)
- Inversion IA acumulada: 0.0094 (ref. 2024.0)
- Startups IA acumuladas: 3.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 3273.2672 (ref. 2024.0)
- GII score: 17.0673 (ref. 2025.0)
- Internet penetration: 8.9498% (ref. 2024.0)
- R&D expenditure: 0.4383 (ref. 2023.0)
- Tertiary education: N/A
- Regulatory quality: -0.5002 (ref. 2023.0)
- Rule of law: -0.7528 (ref. 2023.0)
- Freedom House: 35 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: soft_framework
- Tiene ley IA: No
- Enfoque: light_touch
- Intensidad: 1 (ref. 0-10)
- Enforcement: N/A
- Cobertura tematica: 1 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 2
- Tiene DPA: Si

## 6. Inventario de documentos legales
No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.

## 7. Analisis cualitativo disponible
- meta_analysis chars: 723
- SOURCES chars: 0
- CANDIDATES chars: 0
- FINDINGS chars: 0
- Preview meta analisis: # UGA — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** soft_framework - **Intensidad:** 1/10 - **Enfoque:** light_touch - **Enforcement:** none - **Cobertura temática:** 1/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 35.76/100 - **Adopción:** 6.8% - **Inversión:** USD 0.0094B - **Startups:** 3.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** -0.5002 - **Rule of Law:** -0.7528 - **Freedom House:** 35/100 (NF)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
