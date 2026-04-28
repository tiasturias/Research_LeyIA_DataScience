# Uruguay (URY) - Dossier consolidado Legal-IA

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
- Cobertura tematica: 5
- Grupo regulatorio: strategy_only
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.01975 (ref. 2024.0)
- Startups IA acumuladas: 2.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 22.5 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 58.47 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 28.837903949844 (ref. 2025.0)
- Region: Latin America and the Caribbean

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 36417.874162496 (ref. 2024.0)
- Penetracion internet: 91.9911 (ref. 2024.0)
- Gasto I+D: 0.62592 (ref. 2022.0)
- Educacion terciaria: 79.9536903496537 (ref. 2023.0)
- Exportaciones ICT: 20.9358087447164 (ref. 2024.0)
- Exportaciones high-tech: 9.84178975855216 (ref. 2024.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: 0.675111055374146 (ref. 2023.0)
- Rule of law: 0.717662572860718 (ref. 2023.0)
- Government effectiveness: 0.850249707698822 (ref. 2023.0)
- Control of corruption: 1.57394731044769 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 3
- Ano ley DP: 2008
- Tiene DPA: 1
- Status UE/adequacy: adequacy
- Enforcement activo DP: 1

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 97 (ref. 2025)
- FH status: F
- Nivel democracia FH: 2

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: French
- Common law: 0

## 4. Perfil cuantitativo del pais
- Region: Latin America and the Caribbean
- OECD member: No
- Legal origin: French
- Common law: No
- Poblacion: 3386588.0
- GDP actual USD: 80961511073.5797
- AI readiness: 58.47 (ref. 2025)
- Adopcion IA: 22.5% (ref. H2_2025)
- Inversion IA acumulada: 0.0198 (ref. 2024.0)
- Startups IA acumuladas: 2.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 36417.8742 (ref. 2024.0)
- GII score: 28.8379 (ref. 2025.0)
- Internet penetration: 91.9911% (ref. 2024.0)
- R&D expenditure: 0.6259 (ref. 2022.0)
- Tertiary education: 79.9537 (ref. 2023.0)
- Regulatory quality: 0.6751 (ref. 2023.0)
- Rule of law: 0.7177 (ref. 2023.0)
- Freedom House: 97 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: strategy_only
- Tiene ley IA: No
- Enfoque: strategy_led
- Intensidad: 3 (ref. 0-10)
- Enforcement: low
- Cobertura tematica: 5 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 3
- Tiene DPA: Si

## 6. Inventario de documentos legales
No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.

## 7. Analisis cualitativo disponible
- meta_analysis chars: 720
- SOURCES chars: 0
- CANDIDATES chars: 0
- FINDINGS chars: 0
- Preview meta analisis: # URY — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** strategy_only - **Intensidad:** 3/10 - **Enfoque:** strategy_led - **Enforcement:** low - **Cobertura temática:** 5/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 58.47/100 - **Adopción:** 22.5% - **Inversión:** USD 0.0198B - **Startups:** 2.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** 0.6751 - **Rule of Law:** 0.7177 - **Freedom House:** 97/100 (F)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
