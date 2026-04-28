# CAN - Embedding Data Complet

## 1. Metadata
- **ISO3:** CAN
- **Región:** Northern America
- **OECD:** True
- **Legal Origin:** English

## 2. Regulatory Framework
- **Grupo:** strategy_only
- **Intensidad:** 5/10
- **Enfoque:** strategy_led
- **Enforcement:** medium
- **Cover:** 11/15
- **GDPR-like:** True, similarity 3

## 3. Ecosystem IA
- **AI Readiness:** 74.66/100
- **Adopción:** 35.0%
- **Inversión:** $15.306B
- **Startups:** 481.0
- **Patentes/100k:** 0.1746

## 4. Controls
- **GDP per capita:** $64610.3795
- **GII:** 51.0644
- **Internet:** 93.9564%
- **R&D:** 1.7013%

## 5. Governance
- **Regulatory Quality:** 1.6447
- **Rule of Law:** 1.473
- **Freedom House:** 97/100 (F)

## 6. Documentos Legales (7)
| Título | Tipo | Fecha | Pág |
|---|---|---|---|
| Personal Information Protection and Elec | binding_law_sectoral | 2000-04-13 | 66 |
| Pan-Canadian Artificial Intelligence Str | policy_strategy | 2022-06-22 | 6 |
| The Artificial Intelligence and Data Act | bill_pending | 2023-03-13 | 8 |
| Directive on Automated Decision-Making | binding_law_sectoral | 2019-04-01 | 8 |
| Voluntary Code of Conduct on the Respons | soft_framework | 2023-09-27 | 8 |
| Guide on the Use of Generative AI | guidelines | 2024-02-12 | 8 |
| Engagements on Canada's Next AI Strategy | policy_draft | 2026-02-02 | 19 |

## 7. Análisis Diferencial
# CAN — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Canadá es el único país del corpus cuyo proyecto de ley IA comprehensiva (AIDA/Bill C-27) murió formalmente por prorogación parlamentaria, marking a deliberate legislative retreat that distinguishes it from peers like AUS (mandatory guardrails abortado) and GBR (AI Bill abandonado).** Este caso proporciona un "negative control" natural en el estudio: un ecosistema IA maduro (Top 13 Microsoft) con estrategia, frameworks y Directive ADM binding, pero sin legislación IA vinculante por decisión política explícita. La muerte del AIDA no fue por falta de iniciativa sino por timing político (snap election).

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 7 | count(manifest.csv) |
| # binding (law + sectoral) | 2 | PIPEDA + Directive ADM |
| # soft/policy/strategy | 5 | Strategy + AIDA (dead) + VolCode + Guide + Consultation |
| Páginas totales corpus | 123 | sum(pages) |
| Páginas binding / soft | 74/49 | 1.51:1 |
| Primer documento (fecha) | 2000-04-13 | min(publication_date) |
| Último documento (fecha) | 2026-02-02 | max(publication_date) |
| Años cubiertos | 26 | (2026-02-02 - 2000-04-13).years |
| Gap con fecha corpus | 2.6 meses | 2026-04-21 - 2026-02-02 |
| # docs superseded | 1 | AIDA Companion Document (died_prorogation) |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2000-04-13 | PIPEDA Royal Assent | Ley federal de protección de datos, aplica a automated processing |
| 2019-04-01 | Directive on ADM | Vigente desde 2019, AIA mandatorio para sistemas ADM federales |
| 2022-06-22 | Pan-Canadian AI Strategy Phase 2 | Anuncio oficial, CAD 443M/10 años |
| 2023-03-13 | AIDA Companion Document | Publicación explicativa del Bill C-27 |
| 2023-09-27 | Voluntary Code of Conduct GenAI | Lanzado por Min. Champagne, 6 outcomes (FASTER) |
| 2024-02-12 | Guide on Generative AI ...