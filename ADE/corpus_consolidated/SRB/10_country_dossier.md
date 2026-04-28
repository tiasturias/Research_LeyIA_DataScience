# Serbia (SRB) - Dossier consolidado Legal-IA

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
- Cobertura tematica: 3
- Grupo regulatorio: strategy_only
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.010291385 (ref. 2024.0)
- Startups IA acumuladas: 2.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 21.5 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 60.96 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 31.7434550377633 (ref. 2025.0)
- Region: Europe

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 32832.1763221005 (ref. 2024.0)
- Penetracion internet: 87.69071294 (ref. 2024.0)
- Gasto I+D: 0.93978 (ref. 2024.0)
- Educacion terciaria: 70.582649230957 (ref. 2024.0)
- Exportaciones ICT: 28.5641919197406 (ref. 2024.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: 0.0850626999999999 (ref. 2023.0)
- Rule of law: -0.1840377 (ref. 2023.0)
- Government effectiveness: 0.1035439 (ref. 2023.0)
- Control of corruption: -0.501692 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2018
- Tiene DPA: 1
- Enforcement activo DP: 1

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 57 (ref. 2025)
- FH status: PF
- Nivel democracia FH: 1

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: Socialist
- Common law: 0

## 4. Perfil cuantitativo del pais
- Region: Europe
- OECD member: No
- Legal origin: Socialist
- Common law: No
- Poblacion: 6586476.0
- GDP actual USD: 90097765959.1114
- AI readiness: 60.96 (ref. 2025)
- Adopcion IA: 21.5% (ref. H2_2025)
- Inversion IA acumulada: 0.0103 (ref. 2024.0)
- Startups IA acumuladas: 2.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 32832.1763 (ref. 2024.0)
- GII score: 31.7435 (ref. 2025.0)
- Internet penetration: 87.6907% (ref. 2024.0)
- R&D expenditure: 0.9398 (ref. 2024.0)
- Tertiary education: 70.5826 (ref. 2024.0)
- Regulatory quality: 0.0851 (ref. 2023.0)
- Rule of law: -0.184 (ref. 2023.0)
- Freedom House: 57 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: strategy_only
- Tiene ley IA: No
- Enfoque: strategy_led
- Intensidad: 2 (ref. 0-10)
- Enforcement: low
- Cobertura tematica: 3 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 2
- Tiene DPA: Si

## 6. Inventario de documentos legales
No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.

## 7. Analisis cualitativo disponible
- meta_analysis chars: 721
- SOURCES chars: 0
- CANDIDATES chars: 0
- FINDINGS chars: 0
- Preview meta analisis: # SRB — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** strategy_only - **Intensidad:** 2/10 - **Enfoque:** strategy_led - **Enforcement:** low - **Cobertura temática:** 3/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 60.96/100 - **Adopción:** 21.5% - **Inversión:** USD 0.0103B - **Startups:** 2.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** 0.0851 - **Rule of Law:** -0.184 - **Freedom House:** 57/100 (PF)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
