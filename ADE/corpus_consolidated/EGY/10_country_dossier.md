# Egipto (EGY) - Dossier consolidado Legal-IA

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
- Cobertura tematica: 6
- Grupo regulatorio: strategy_only
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.0971 (ref. 2024.0)
- Startups IA acumuladas: 14.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 13.4 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 59.1 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 24.7122281668271 (ref. 2025.0)
- Region: Northern Africa and Western Asia

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 19094.1449444111 (ref. 2024.0)
- Penetracion internet: 72.6899 (ref. 2023.0)
- Gasto I+D: 1.03356 (ref. 2023.0)
- Educacion terciaria: 37.5781274463676 (ref. 2024.0)
- Exportaciones ICT: 5.76658761386299 (ref. 2024.0)
- Exportaciones high-tech: 3.81290087814207 (ref. 2024.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: -0.665456295013428 (ref. 2023.0)
- Rule of law: -0.184178426861763 (ref. 2023.0)
- Government effectiveness: -0.239516973495483 (ref. 2023.0)
- Control of corruption: -0.747790396213531 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2020
- Tiene DPA: 0
- Enforcement activo DP: 0

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 18 (ref. 2025)
- FH status: NF
- Nivel democracia FH: 0

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: French
- Common law: 0

### OECD robustez
- Proposito: Variables adicionales de sensibilidad y robustez.
- Publicaciones IA: 1313.851307 (ref. 2023.0)

## 4. Perfil cuantitativo del pais
- Region: Northern Africa and Western Asia
- OECD member: No
- Legal origin: French
- Common law: No
- Poblacion: 116538258.0
- GDP actual USD: 389059911003.566
- AI readiness: 59.1 (ref. 2025)
- Adopcion IA: 13.4% (ref. H2_2025)
- Inversion IA acumulada: 0.0971 (ref. 2024.0)
- Startups IA acumuladas: 14.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 19094.1449 (ref. 2024.0)
- GII score: 24.7122 (ref. 2025.0)
- Internet penetration: 72.6899% (ref. 2023.0)
- R&D expenditure: 1.0336 (ref. 2023.0)
- Tertiary education: 37.5781 (ref. 2024.0)
- Regulatory quality: -0.6655 (ref. 2023.0)
- Rule of law: -0.1842 (ref. 2023.0)
- Freedom House: 18 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: strategy_only
- Tiene ley IA: No
- Enfoque: strategy_led
- Intensidad: 3 (ref. 0-10)
- Enforcement: low
- Cobertura tematica: 6 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 2
- Tiene DPA: No

## 6. Inventario de documentos legales
No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.

## 7. Analisis cualitativo disponible
- meta_analysis chars: 723
- SOURCES chars: 0
- CANDIDATES chars: 0
- FINDINGS chars: 0
- Preview meta analisis: # EGY — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** strategy_only - **Intensidad:** 3/10 - **Enfoque:** strategy_led - **Enforcement:** low - **Cobertura temática:** 6/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 59.1/100 - **Adopción:** 13.4% - **Inversión:** USD 0.0971B - **Startups:** 14.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** -0.6655 - **Rule of Law:** -0.1842 - **Freedom House:** 18/100 (NF)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
