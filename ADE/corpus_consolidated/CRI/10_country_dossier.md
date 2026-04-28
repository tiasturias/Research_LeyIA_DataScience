# Costa Rica (CRI) - Dossier consolidado Legal-IA

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
- Cobertura tematica: 4
- Grupo regulatorio: strategy_only
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.005932492 (ref. 2024.0)
- Startups IA acumuladas: 2.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 26.5 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 45.92 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 28.3589014854175 (ref. 2025.0)
- Region: Latin America and the Caribbean

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 31106.7643556729 (ref. 2024.0)
- Penetracion internet: 85.3951 (ref. 2023.0)
- Gasto I+D: 0.33789 (ref. 2022.0)
- Educacion terciaria: 55.0202903747559 (ref. 2019.0)
- Exportaciones ICT: 14.2776211889662 (ref. 2024.0)
- Exportaciones high-tech: 22.8587994049653 (ref. 2024.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: 0.543547570705414 (ref. 2023.0)
- Rule of law: 0.389316648244858 (ref. 2023.0)
- Government effectiveness: 0.260196477174759 (ref. 2023.0)
- Control of corruption: 0.653749406337738 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2011
- Tiene DPA: 1
- Enforcement activo DP: 1

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 91 (ref. 2025)
- FH status: F
- Nivel democracia FH: 2

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: French
- Common law: 0

### OECD robustez
- Proposito: Variables adicionales de sensibilidad y robustez.
- Publicaciones IA: 16.48861738 (ref. 2023.0)

## 4. Perfil cuantitativo del pais
- Region: Latin America and the Caribbean
- OECD member: Si
- Legal origin: French
- Common law: No
- Poblacion: 5129910.0
- GDP actual USD: 95350423176.5962
- AI readiness: 45.92 (ref. 2025)
- Adopcion IA: 26.5% (ref. H2_2025)
- Inversion IA acumulada: 0.0059 (ref. 2024.0)
- Startups IA acumuladas: 2.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 31106.7644 (ref. 2024.0)
- GII score: 28.3589 (ref. 2025.0)
- Internet penetration: 85.3951% (ref. 2023.0)
- R&D expenditure: 0.3379 (ref. 2022.0)
- Tertiary education: 55.0203 (ref. 2019.0)
- Regulatory quality: 0.5435 (ref. 2023.0)
- Rule of law: 0.3893 (ref. 2023.0)
- Freedom House: 91 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: strategy_only
- Tiene ley IA: No
- Enfoque: strategy_led
- Intensidad: 2 (ref. 0-10)
- Enforcement: low
- Cobertura tematica: 4 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 2
- Tiene DPA: Si

## 6. Inventario de documentos legales
No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.

## 7. Analisis cualitativo disponible
- meta_analysis chars: 720
- SOURCES chars: 0
- CANDIDATES chars: 0
- FINDINGS chars: 0
- Preview meta analisis: # CRI — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** strategy_only - **Intensidad:** 2/10 - **Enfoque:** strategy_led - **Enforcement:** low - **Cobertura temática:** 4/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 45.92/100 - **Adopción:** 26.5% - **Inversión:** USD 0.0059B - **Startups:** 2.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** 0.5435 - **Rule of Law:** 0.3893 - **Freedom House:** 91/100 (F)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
