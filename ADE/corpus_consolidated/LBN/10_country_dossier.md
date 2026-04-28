# Libano (LBN) - Dossier consolidado Legal-IA

## 1. Proposito analitico
Existe una asociacion estadisticamente significativa entre las caracteristicas de la regulacion de inteligencia artificial de un pais y el desarrollo de su ecosistema de IA, despues de controlar por factores socioeconomicos e institucionales.

El estudio busca informar la discusion chilena sobre Ley Marco de IA (Boletin 16821-19) con evidencia comparativa internacional.

- Diseno del estudio: Cross-section comparativo 2025 con 86 paises y una submuestra ADE de 73.
- Dataset base: data/interim/sample_ready_cross_section.csv
- Tier recomendada: complete_confounded

## 2. Estado del pais dentro del estudio
- Grupo regulatorio: no_framework
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
- Intensidad regulatoria: 0
- Cobertura tematica: 1
- Grupo regulatorio: no_framework
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.0138 (ref. 2024.0)
- Startups IA acumuladas: 1.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 25.7 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 34.26 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 23.6120255291244 (ref. 2025.0)
- Region: Northern Africa and Western Asia

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 12574.8329116403 (ref. 2023.0)
- Penetracion internet: 80.63400269 (ref. 2024.0)
- Educacion terciaria: 54.4012561547071 (ref. 2023.0)
- Exportaciones ICT: 1.77653813888075 (ref. 2023.0)
- Exportaciones high-tech: 2.89591276881506 (ref. 2024.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: -0.912561 (ref. 2023.0)
- Rule of law: -1.0665045 (ref. 2023.0)
- Government effectiveness: -1.16583329999999 (ref. 2023.0)
- Control of corruption: -1.2554109 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2018
- Tiene DPA: 0
- Enforcement activo DP: 0

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 42 (ref. 2025)
- FH status: PF
- Nivel democracia FH: 1

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: French
- Common law: 0

## 4. Perfil cuantitativo del pais
- Region: Northern Africa and Western Asia
- OECD member: No
- Legal origin: French
- Common law: No
- Poblacion: 5805962.0
- GDP actual USD: 20078620356.9931
- AI readiness: 34.26 (ref. 2025)
- Adopcion IA: 25.7% (ref. H2_2025)
- Inversion IA acumulada: 0.0138 (ref. 2024.0)
- Startups IA acumuladas: 1.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 12574.8329 (ref. 2023.0)
- GII score: 23.612 (ref. 2025.0)
- Internet penetration: 80.634% (ref. 2024.0)
- R&D expenditure: N/A
- Tertiary education: 54.4013 (ref. 2023.0)
- Regulatory quality: -0.9126 (ref. 2023.0)
- Rule of law: -1.0665 (ref. 2023.0)
- Freedom House: 42 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: no_framework
- Tiene ley IA: No
- Enfoque: N/A
- Intensidad: 0 (ref. 0-10)
- Enforcement: N/A
- Cobertura tematica: 1 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 2
- Tiene DPA: No

## 6. Inventario de documentos legales
No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.

## 7. Analisis cualitativo disponible
- meta_analysis chars: 715
- SOURCES chars: 0
- CANDIDATES chars: 0
- FINDINGS chars: 0
- Preview meta analisis: # LBN — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** no_framework - **Intensidad:** 0/10 - **Enfoque:** none - **Enforcement:** none - **Cobertura temática:** 1/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 34.26/100 - **Adopción:** 25.7% - **Inversión:** USD 0.0138B - **Startups:** 1.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** -0.9126 - **Rule of Law:** -1.0665 - **Freedom House:** 42/100 (PF)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
