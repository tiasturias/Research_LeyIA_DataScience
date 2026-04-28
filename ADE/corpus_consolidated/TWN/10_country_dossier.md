# Taiwan (TWN) - Dossier consolidado Legal-IA

## 1. Proposito analitico
Existe una asociacion estadisticamente significativa entre las caracteristicas de la regulacion de inteligencia artificial de un pais y el desarrollo de su ecosistema de IA, despues de controlar por factores socioeconomicos e institucionales.

El estudio busca informar la discusion chilena sobre Ley Marco de IA (Boletin 16821-19) con evidencia comparativa internacional.

- Diseno del estudio: Cross-section comparativo 2025 con 86 paises y una submuestra ADE de 73.
- Dataset base: data/interim/sample_ready_cross_section.csv
- Tier recomendada: complete_confounded

## 2. Estado del pais dentro del estudio
- Grupo regulatorio: strategy_only
- Tiene corpus legal manual: Si
- Documentos legales identificados: 7
- Paginas totales del corpus legal: 30
- complete_principal: No
- complete_confounded: No
- complete_digital: No
- complete_regime: No
- complete_legal_tradition: No

## 3. Datos recopilados por fuente y proposito
### IAPP + OECD (X1 regulatorio)
- Proposito: Caracterizar el marco regulatorio de IA del pais.
- Tiene ley IA: 0
- Enfoque regulatorio: strategy_led
- Intensidad regulatoria: 5
- Enforcement: medium
- Cobertura tematica: 9
- Grupo regulatorio: strategy_only
- Fuente X1 consolidada: IAPP

### Stanford AI Index
- Proposito: Medir inversion, startups y patentes del ecosistema IA.
- Inversion IA acumulada (USD bn): 0.971927833 (ref. 2024.0)
- Startups IA acumuladas: 42.0 (ref. 2024.0)

### Microsoft AI Diffusion Report
- Proposito: Capturar adopcion efectiva de IA generativa.
- Adopcion IA: 28.4 (ref. H2_2025)

### Oxford Insights
- Proposito: Medir readiness gubernamental para IA.
- AI readiness score: 64.81 (ref. 2025)

### WIPO Global Innovation Index
- Proposito: Controlar capacidad general de innovacion y region.
- Region: South East Asia, East Asia, and Oceania

### GDPR / proteccion de datos
- Proposito: Capturar tradicion regulatoria digital preexistente.
- Tiene ley GDPR-like: 1
- Nivel de similitud GDPR: 2
- Ano ley DP: 2023
- Tiene DPA: 1
- Enforcement activo DP: 1

### Freedom House
- Proposito: Controlar tipo de regimen politico y libertades.
- Freedom House total: 94 (ref. 2025)
- FH status: F
- Nivel democracia FH: 2

### Legal Origin
- Proposito: Capturar tradicion juridica como confounder institucional.
- Legal origin: German
- Common law: 0

### Corpus legal manual por pais
- Proposito: Aportar evidencia documental, citas, inventario y hallazgos diferenciales del caso nacional.
- 05_sources.md: disponible
- 06_candidates.md: disponible
- 07_findings.md: disponible

## 4. Perfil cuantitativo del pais
- Region: South East Asia, East Asia, and Oceania
- OECD member: No
- Legal origin: German
- Common law: No
- Poblacion: N/A
- GDP actual USD: N/A
- AI readiness: 64.81 (ref. 2025)
- Adopcion IA: 28.4% (ref. H2_2025)
- Inversion IA acumulada: 0.9719 (ref. 2024.0)
- Startups IA acumuladas: 42.0 (ref. 2024.0)
- Patentes IA por 100k: N/A
- GDP per capita PPP: N/A
- GII score: N/A
- Internet penetration: N/A
- R&D expenditure: N/A
- Tertiary education: N/A
- Regulatory quality: N/A
- Rule of law: N/A
- Freedom House: 94 (ref. 2025)

## 5. Marco regulatorio y confounders
- Grupo: strategy_only
- Tiene ley IA: No
- Enfoque: strategy_led
- Intensidad: 5 (ref. 0-10)
- Enforcement: medium
- Cobertura tematica: 9 (ref. 15)
- GDPR-like law: Si
- GDPR similarity level: 2
- Tiene DPA: Si

## 6. Inventario de documentos legales
El corpus legal del pais contiene 7 documentos identificados.
- Doc 1: Artificial Intelligence Basic Act (Taiwan, 2026) | tipo=binding_law_ai | fecha=2026-01-14 | paginas=3
- Doc 2: 人工智慧基本法 (Artificial Intelligence Basic Act, ZH) | tipo=binding_law_ai | fecha=2026-01-14 | paginas=3
- Doc 3: Personal Data Protection Act (Taiwan) | tipo=binding_law_sectoral | fecha=2025-11-11 | paginas=8
- Doc 4: Cyber Security Management Act (Taiwan) | tipo=binding_law_sectoral | fecha=2018-06-06 | paginas=7
- Doc 5: AI Taiwan Action Plan 2.0 (2023-2026) | tipo=policy_strategy | fecha=2023-04 | paginas=
- Doc 6: Reference Guidelines for the Use of Generative AI by the Executive Yuan and Subordinate Agencies (Draft, approved by 3869th session) | tipo=guidelines | fecha=2023-08-31 | paginas=5
- Doc 7: Reference Guidelines for AI Applications in National Critical Infrastructure (國家關鍵基礎設施應用人工智慧參考指引) | tipo=guidelines | fecha=2025-10-08 | paginas=4

## 7. Analisis cualitativo disponible
- meta_analysis chars: 3354
- SOURCES chars: 10761
- CANDIDATES chars: 18903
- FINDINGS chars: 6290
- Preview hallazgo diferencial: # TWN — Hallazgo Diferencial  ## 1. Tesis del hallazgo diferencial  **Taiwán promulgó el AI Basic Act (人工智慧基本法) el 14 de enero de 2026, transicionando de `soft_framework` a `binding_regulation` — primer caso del corpus piloto con ley IA horizontal vigente. Este caso constituye el contrafactual natural de Singapur: ambos países con ecosistemas IA densos (tier equivalente en cobertura), pero decisiones regulatorias opuestas: SGP rechaza ley horizontal por política explícita; TWN la promulga. La arquitectura taiwanesa es delegada: NSTC como autoridad competente + MODA implementa risk taxonomy (Art. 16) + enforcement sectorial vía PDPA/CSMA.**  ---  ## 2. Evidencia cuantitativa — densidad del corpus  | Métrica | Valor | Cálculo | |---|---|---| | # documentos totales | 7 | count(manifest.csv) |

## 8. Nota de uso para ingesta
La estrategia objetivo es 1 documento por pais con multiples metachunks: contexto del estudio, perfil cuantitativo, marco regulatorio, inventario documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista.
