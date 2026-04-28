# GBR - Embedding Data Complet

## 1. Metadata
- **ISO3:** GBR
- **Región:** Europe
- **OECD:** True
- **Legal Origin:** English

## 2. Regulatory Framework
- **Grupo:** strategy_only
- **Intensidad:** 6/10
- **Enfoque:** strategy_led
- **Enforcement:** high
- **Cover:** 13/15
- **GDPR-like:** True, similarity 3

## 3. Ecosystem IA
- **AI Readiness:** 77.75/100
- **Adopción:** 38.9%
- **Inversión:** $28.1703B
- **Startups:** 885.0
- **Patentes/100k:** 0.5179

## 4. Controls
- **GDP per capita:** $62009.4908
- **GII:** 59.1154
- **Internet:** 96.2988%
- **R&D:** 2.8971%

## 5. Governance
- **Regulatory Quality:** 1.5366
- **Rule of Law:** 1.3984
- **Freedom House:** 91/100 (F)

## 6. Documentos Legales (6)
| Título | Tipo | Fecha | Pág |
|---|---|---|---|
| National AI Strategy | policy_strategy | 2021-09-22 | 66 |
| A Pro-Innovation Approach to AI Regulati | soft_framework | 2024-02-06 | 98 |
| AI Opportunities Action Plan (CP 1241) | policy_strategy | 2025-01-13 | 26 |
| Introducing the AI Safety Institute | soft_framework | 2023-11-02 | 18 |
| Data Protection Act 2018 (c. 12) | binding_law | 2018-05-23 | 354 |
| Online Safety Act 2023 (c. 50) | binding_law | 2023-10-26 | 303 |

## 7. Análisis Diferencial
# GBR — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Reino Unido presenta la paradoja regulatoria más notable del corpus: el país con mayor liderazgo global en seguridad IA (AISI — primer instituto estatal de seguridad IA del mundo, lanzado en Bletchley Park noviembre 2023) ha adoptado deliberadamente el enfoque regulatorio más ligero de Europa mediante su "sector-specific, context-based approach" articulado en la Government Response 2024, que explícitamente rechaza una ley IA horizontal al estilo UE y opta por cinco principios transversales aplicados por reguladores sectoriales existentes — una teoría regulatoria alternativa que exporta a USA, JPN y KOR, pero que lo clasifica como soft_framework en lugar de binding_regulation.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 6 | count(manifest.csv) |
| # binding (law + sectoral) | 2 | DPA 2018 + OSA 2023 |
| # soft/policy/strategy | 4 | AI Strategy + White Paper Response + Action Plan + AISI |
| Páginas totales corpus | 865 | sum(pages) |
| Páginas binding / soft | 657 / 208 | 3.16:1 |
| Primer documento (fecha) | 2018-05 | Data Protection Act |
| Último documento (fecha) | 2025-01 | AI Opportunities Action Plan |
| Años cubiertos | 6.5 | (2025-01 - 2018-05) |
| Gap con fecha corpus | ~3 meses | 2026-04-21 - 2025-01 |
| # docs superseded | 1 | National AI Strategy 2021 (superseded por Action Plan 2025) |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2018-05-23 | Data Protection Act | Ley de protección de datos post-Brexit. Art. 22 sobre automated decisions. ICO enforcement. |
| 2021-09-22 | National AI Strategy | Estrategia IA nacional. Tres pilares: ecosistema, economía, gobernanza. |
| 2023-03 | AI White Paper | CP 815 — consulta pública sobre enfoque regulatorio IA. |
| 2023-10-26 | Online Safety Act | Royal Assent. Primera ley británica con provisiones explícitas...