# Peru (PER) - Dossier consolidado Legal-IA

## 1. Proposito analitico
Existe una asociacion estadisticamente significativa entre las caracteristicas de la regulacion de inteligencia artificial de un pais y el desarrollo de su ecosistema de IA, despues de controlar por factores socioeconomicos e institucionales.

El estudio busca informar la discusion chilena sobre Ley Marco de IA (Boletin 16821-19) con evidencia comparativa internacional.

- Diseno del estudio: Cross-section comparativo 2025 con 86 paises y una submuestra ADE de 73.
- Dataset base: data/interim/sample_ready_cross_section.csv
- Tier recomendada: complete_confounded

## 2. Estado del pais dentro del estudio
- Grupo regulatorio: binding_regulation
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
- Tiene ley IA: 1
- Enfoque regulatorio: comprehensive
- Intensidad regulatoria: 6
- Ano promulgacion: 2023.0
- Enforcement: medium
- Cobertura tematica: 9
- Grupo regulatorio: binding_regulation
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.002 (ref. 2024.0)
- Startups IA acumuladas: 1.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 14.7 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 56.52 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- GII score: 26.4660453517052 (ref. 2025.0)
- Region: Latin America and the Caribbean

### World Bank WDI
- Proposito: Agregar controles socioeconomicos y de economia digital.
- PIB per capita PPP: 17802.4182498972 (ref. 2024.0)
- Penetracion internet: 81.9571 (ref. 2024.0)
- Gasto I+D: 0.16178 (ref. 2022.0)
- Exportaciones ICT: 2.15949973332149 (ref. 2024.0)
- Exportaciones high-tech: 5.21372377596414 (ref. 2024.0)

### World Bank WGI
- Proposito: Controlar calidad institucional y gobernanza.
- Regulatory quality: 0.292205184698105 (ref. 2023.0)
- Rule of law: -0.538132667541504 (ref. 2023.0)
- Government effectiveness: -0.491872787475586 (ref. 2023.0)
- Control of corruption: -0.721040904521942 (ref. 2023.0)

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2011
- Tiene DPA: 1
- Enforcement activo DP: 1

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 66 (ref. 2025)
- FH status: PF
- Nivel democracia FH: 1

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: French
- Common law: 0

### OECD robustez
- Proposito: Variables adicionales de sensibilidad y robustez.
- Publicaciones IA: 291.8083533 (ref. 2023.0)

## 4. Perfil cuantitativo del pais
- Region: Latin America and the Caribbean
- OECD member: No
- Legal origin: French
- Common law: No
- Poblacion: 34217848.0
- GDP actual USD: 289221969062.941
- AI readiness: 56.52 (ref. 2025)
- Adopcion IA: 14.7% (ref. H2_2025)
- Inversion IA acumulada: 0.002 (ref. 2024.0)
- Startups IA acumuladas: 1.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: 17802.4182 (ref. 2024.0)
- GII score: 26.466 (ref. 2025.0)
- Internet penetration: 81.9571% (ref. 2024.0)
- R&D expenditure: 0.1618 (ref. 2022.0)
- Tertiary education: N/A
- Regulatory quality: 0.2922 (ref. 2023.0)
- Rule of law: -0.5381 (ref. 2023.0)
- Freedom House: 66 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: binding_regulation
- Tiene ley IA: Si
- Enfoque: comprehensive
- Intensidad: 6 (ref. 0-10)
- Enforcement: medium
- Cobertura tematica: 9 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 2
- Tiene DPA: Si

## 6. Inventario de documentos legales
No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.

## 7. Analisis cualitativo disponible
- meta_analysis chars: 730
- SOURCES chars: 0
- CANDIDATES chars: 0
- FINDINGS chars: 0
- Preview meta analisis: # PER — Meta Chunks para Embedding  ## chunk_01: regulatory_framework  **Tema:** Marco regulatorio de IA **Tipo:** regulatory_framework **Relevancia:** 0.85  - **Grupo:** binding_regulation - **Intensidad:** 6/10 - **Enfoque:** comprehensive - **Enforcement:** medium - **Cobertura temática:** 9/15  ## chunk_02: ecosystem_metrics  **Tema:** Métricas ecosistema IA **Tipo:** ecosystem_ia **Relevancia:** 0.80  - **AI Readiness:** 56.52/100 - **Adopción:** 14.7% - **Inversión:** USD 0.002B - **Startups:** 1.0  ## chunk_03: governance  **Tema:** Gobernanza **Tipo:** governance **Relevancia:** 0.75  - **Regulatory Quality:** 0.2922 - **Rule of Law:** -0.5381 - **Freedom House:** 66/100 (PF)  *Nota: Sin corpus legal descargado* 

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
