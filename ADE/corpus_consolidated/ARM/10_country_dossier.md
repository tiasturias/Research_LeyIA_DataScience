# Armenia (ARM) - Dossier consolidado Legal-IA

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
- Cobertura tematica: 2
- Grupo regulatorio: soft_framework
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.00443894 (ref. 2024.0)
- Startups IA acumuladas: 1.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 6.6 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 38.95 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 30.448190677743 (ref. 2025.0)
- Region: Northern Africa and Western Asia

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 22823.1795255693 (ref. 2024.0)
- Penetracion internet: 81.33930206 (ref. 2024.0)
- Gasto I+D: 0.2861 (ref. 2024.0)
- Educacion terciaria: 52.7748065090859 (ref. 2024.0)
- Exportaciones ICT: 20.1631222184293 (ref. 2024.0)
- Exportaciones high-tech: 23.6403270515259 (ref. 2024.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: 0.0964411 (ref. 2023.0)
- Rule of law: -0.2107914 (ref. 2023.0)
- Government effectiveness: -0.163441 (ref. 2023.0)
- Control of corruption: 0.1046118 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2015
- Tiene DPA: 1
- Enforcement activo DP: 1

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 54 (ref. 2025)
- FH status: PF
- Nivel democracia FH: 1

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: Socialist
- Common law: 0

## 4. Perfil cuantitativo del pais
- Region: Northern Africa and Western Asia
- OECD member: No
- Legal origin: Socialist
- Common law: No
- Poblacion: 3033500.0
- GDP actual USD: 25955275380.0321
- AI readiness: 38.95 (ref. 2025)
- Adopcion IA: 6.6% (ref. H2_2025)
- Inversion IA acumulada: 0.0044 (ref. 2024.0)
- Startups IA acumuladas: 1.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 22823.1795 (ref. 2024.0)
- GII score: 30.4482 (ref. 2025.0)
- Internet penetration: 81.3393% (ref. 2024.0)
- R&D expenditure: 0.2861 (ref. 2024.0)
- Tertiary education: 52.7748 (ref. 2024.0)
- Regulatory quality: 0.0964 (ref. 2023.0)
- Rule of law: -0.2108 (ref. 2023.0)
- Freedom House: 54 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: soft_framework
- Tiene ley IA: No
- Enfoque: light_touch
- Intensidad: 1 (ref. 0-10)
- Enforcement: N/A
- Cobertura tematica: 2 (ref. 15)
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
- Preview meta analisis: # ARM — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** soft_framework - **Intensidad:** 1/10 - **Enfoque:** light_touch - **Enforcement:** none - **Cobertura temática:** 2/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 38.95/100 - **Adopción:** 6.6% - **Inversión:** USD 0.0044B - **Startups:** 1.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** 0.0964 - **Rule of Law:** -0.2108 - **Freedom House:** 54/100 (PF)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
