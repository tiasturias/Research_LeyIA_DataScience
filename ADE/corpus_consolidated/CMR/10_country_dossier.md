# Camerun (CMR) - Dossier consolidado Legal-IA

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
- Cobertura tematica: 0
- Grupo regulatorio: no_framework
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.005 (ref. 2024.0)
- Startups IA acumuladas: 1.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 7.8 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 34.91 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 18.1843870946301 (ref. 2025.0)
- Region: Sub-Saharan Africa

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 5588.98645861945 (ref. 2024.0)
- Penetracion internet: 41.9088 (ref. 2023.0)
- Educacion terciaria: 16.6614294830602 (ref. 2024.0)
- Exportaciones ICT: 10.479456496953 (ref. 2024.0)
- Exportaciones high-tech: 2.10363029161033 (ref. 2023.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: -0.913473010063171 (ref. 2023.0)
- Rule of law: -1.03819787502289 (ref. 2023.0)
- Government effectiveness: -0.906262576580048 (ref. 2023.0)
- Control of corruption: -1.16255974769592 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 0
- Nivel de similitud GDPR: 1
- Ano ley DP: 2010
- Tiene DPA: 0
- Enforcement activo DP: 0

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 14 (ref. 2025)
- FH status: NF
- Nivel democracia FH: 0

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: French
- Common law: 0

## 4. Perfil cuantitativo del pais
- Region: Sub-Saharan Africa
- OECD member: No
- Legal origin: French
- Common law: No
- Poblacion: 29123744.0
- GDP actual USD: 53296694320.2057
- AI readiness: 34.91 (ref. 2025)
- Adopcion IA: 7.8% (ref. H2_2025)
- Inversion IA acumulada: 0.005 (ref. 2024.0)
- Startups IA acumuladas: 1.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 5588.9865 (ref. 2024.0)
- GII score: 18.1844 (ref. 2025.0)
- Internet penetration: 41.9088% (ref. 2023.0)
- R&D expenditure: N/A
- Tertiary education: 16.6614 (ref. 2024.0)
- Regulatory quality: -0.9135 (ref. 2023.0)
- Rule of law: -1.0382 (ref. 2023.0)
- Freedom House: 14 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: no_framework
- Tiene ley IA: No
- Enfoque: N/A
- Intensidad: 0 (ref. 0-10)
- Enforcement: N/A
- Cobertura tematica: 0 (ref. 15)
- GDPR-like law: No
- GDPR similarity level: 1
- Tiene DPA: No

## 6. Inventario de documentos legales
No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.

## 7. Analisis cualitativo disponible
- meta_analysis chars: 713
- SOURCES chars: 0
- CANDIDATES chars: 0
- FINDINGS chars: 0
- Preview meta analisis: # CMR — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** no_framework - **Intensidad:** 0/10 - **Enfoque:** none - **Enforcement:** none - **Cobertura temática:** 0/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 34.91/100 - **Adopción:** 7.8% - **Inversión:** USD 0.005B - **Startups:** 1.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** -0.9135 - **Rule of Law:** -1.0382 - **Freedom House:** 14/100 (NF)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
