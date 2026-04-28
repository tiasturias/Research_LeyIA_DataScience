# GBR — Candidates para corpus legal-IA

**País:** United Kingdom (ISO3: GBR)
**Región:** Europe-Other
**Fecha:** 2026-04-20
**Codificador:** Claude Sonnet 4.6 (asistido)
**Status propuesto:** soft_framework ↑ (desde IAPP strategy_led)

---

## 1. Inventario de documentos

| # | Archivo | Tipo | Emisor | Fecha | Estado | Páginas | Capa |
|---|---|---|---|---|---|---|---|
| 1 | GBR_NationalAIStrategy_2021.pdf | policy_strategy | DCMS | 2021-09-22 | superseded | 66 | 3 |
| 2 | GBR_AIWhitePaperResponse_2024.pdf | soft_framework | DSIT | 2024-02-06 | in_use | 98 | 4 |
| 3 | GBR_AIOpportunitiesActionPlan_2025.pdf | policy_strategy | DSIT | 2025-01-13 | in_use | 26 | 3 |
| 4 | GBR_AISI_Intro_2023.pdf | soft_framework | AISI/DSIT | 2023-11-02 | in_use | 18 | 4 |
| 5 | GBR_DataProtectionAct_2018.pdf | binding_law | Parliament UK | 2018-05-23 | in_use | 354 | 2 |
| 6 | GBR_OnlineSafetyAct_2023.pdf | binding_law | Parliament UK | 2023-10-26 | in_use | 303 | 2 |

---

## 2. Citas textuales clave

### Doc 1 — National AI Strategy 2021

> "The UK aims to be a global AI superpower. We will build on our existing AI strengths [...] by investing in research and development, growing AI talent, and removing barriers to adoption — while building public trust and ensuring our approach supports our values."

> "We have a unique opportunity to show the world that it is possible to be both a leading AI nation and a world leader in safe, ethical and trustworthy AI."

### Doc 2 — AI White Paper Response 2024

> "We are not creating a new overarching AI regulator or passing a new law at this stage. Instead, we are asking existing regulators — who already have expertise in their sectors — to issue guidance, drive adoption of good practices, and use their existing enforcement powers."

> "The five cross-cutting principles are: (1) Safety, security and robustness; (2) Appropriate transparency and explainability; (3) Fairness; (4) Accountability and governance; (5) Contestability and redress."

> "We believe the EU's horizontal approach [AI Act] risks stifling innovation. The UK's context-based approach is more proportionate and flexible."

### Doc 3 — AI Opportunities Action Plan 2025

> "AI could be the defining technology of our age — and the UK has a real chance to be a global leader. But we need to move fast. Our analysis suggests the UK is falling behind on compute capacity and AI adoption."

> "The Government accepts all 50 recommendations. We will establish AI Growth Zones to accelerate planning consent for AI data centres; create a National Data Library; and establish an AI Energy Council to manage AI's growing energy demands."

### Doc 4 — Introducing AISI 2023

> "The AI Safety Institute will be the first state-backed organisation focused on advanced AI safety anywhere in the world. It will advance our understanding of AI's risks to safety and security — not to regulate AI, but to provide the scientific foundation for future governance."

> "The Institute's work will include: pre-deployment testing of frontier models; post-deployment monitoring; fundamental safety research; and international coordination on evaluation standards."

### Doc 5 — Data Protection Act 2018

> "Section 49 — Automated decision-making: Where a data controller is required by law to make a significant decision based solely on automated processing [...] the data subject has the right to request human intervention in the decision."

> "Part 4, Section 96 — Automated processing: The processing must include reasonable measures to safeguard the rights, freedoms and legitimate interests of the data subject."

### Doc 6 — Online Safety Act 2023

> "Section 12 — Duties to assess risks of harm from illegal content: A provider of a Part 3 service must carry out an illegal content risk assessment [...] assessing the risk of harms to individuals, including those arising from the use of artificial intelligence."

> "Section 65 — Use of proactive technology: 'Proactive technology' means content identification technology, user profiling technology or behaviour identification technology which utilises artificial intelligence or machine learning."

---

## 3. Recodificación propuesta

### Variables principales

| Variable | Valor IAPP actual | Valor propuesto | Justificación |
|---|---|---|---|
| `regulatory_regime_group` | `strategy_led` | `soft_framework` | DPA 2018 (binding, ICO enforcement alto) + OSA 2023 (binding, Ofcom enforcement, AI explícito) + cuatro docs estratégicos/framework = densidad > strategy_only. Sin ley IA horizontal → no binding_regulation |
| `has_ai_law` | 0 | 0 | Sin ley IA-específica. Confirmado en Government Response (doc 2) |
| `enforcement_level` | high | high | ICO activo con multas DPA; Ofcom operativo con OSA. Más alto que NOR/NZL — sin cambio |
| `has_dedicated_ai_authority` | — | 0 | AISI = institute de research/evaluación, NO regulador. Sin enforcement powers. Sector regulators existentes (ICO, Ofcom) actúan en sus ámbitos pero no son AI-específicos |
| `has_specialized_ai_frameworks` | — | 1 | White Paper Response 2024 (cinco principios) + AISI (evaluación frontier) = frameworks IA especializados en vigor |
| `eea_not_eu` | — | 0 | UK salió del EEA el 31-12-2020 (Brexit). No aplica AI Act ni marco EEA |
| `ai_framework_note` | — | "National AI Strategy 2021; AI White Paper Response 2024 (cinco principios, sin ley horizontal); AI Opportunities Action Plan 2025 (50 recomendaciones); AISI/AI Security Institute (evaluación frontier); DPA 2018 (UK GDPR enforcement); OSA 2023 (plataformas, Ofcom)" | |

### Justificación narrativa del régimen

GBR tiene el régimen IA más sofisticado del corpus entre los países sin ley IA horizontal. El Government Response 2024 establece explícita y deliberadamente que UK NO seguirá el modelo EU AI Act, optando por cinco principios transversales aplicados por reguladores sectoriales existentes. Esto es diferente de NZL (que simplemente no regula) o NOR (que aún no ha transpuesto el AI Act).

Sustento del `soft_framework`:
1. **Binding real (Capa 2):** DPA 2018 (ICO enforcement, multas hasta £17.5M) + OSA 2023 (Ofcom enforcement, multas hasta 10% revenue global). Ambas con provisiones explícitas para sistemas IA.
2. **Framework institucional:** AISI = primer instituto estatal safety IA del mundo. No regula pero establece estándares de evaluación adoptados internacionalmente.
3. **Policy stack completo:** AI Strategy 2021 → AI White Paper 2023 → Government Response 2024 → AI Action Plan 2025. Secuencia de política continua más articulada que cualquier otro país no-EU del corpus (excepto SGP).
4. **Sin ley IA ni bill gubernamental inminente:** el AI (Regulation) Bill [HL] es Private Members' Bill sin respaldo del ejecutivo.

Por qué NO `binding_regulation`: no hay ley IA-específica. Las leyes binding (DPA, OSA) son sectoriales/generales, no AI-specific en su mandato central. A diferencia de EU/DNK/KOR, GBR no ha legislado AI como categoría.

### Hallazgo diferencial GBR

GBR es el caso polar europeo del corpus junto a NZL, pero más sofisticado: posición "pro-innovation, sin ley IA" con el mayor stack de policy e institucionalidad IA fuera de la UE. El AISI (primer instituto estatal safety IA del mundo, lanzado en Bletchley Park nov 2023) y la Government Response 2024 articulan una teoría regulatoria alternativa a la UE — "sector-specific, context-based" — que exporta a USA, JPN, KOR. El AI Opportunities Action Plan 2025 del gobierno Starmer refuerza la apuesta por adopción sobre regulación. Paradoja: el país con mayor liderazgo global en AI safety (AISI) tiene la regulación IA más deliberadamente ligera de Europa.

---

## 4. Tabla diff IAPP → propuesto

| Campo | IAPP (iapp_x1_core) | Propuesto | Tipo de cambio |
|---|---|---|---|
| regulatory_regime_group | strategy_led | soft_framework | ↑ upgrade |
| has_ai_law | 0 | 0 | sin cambio |
| enforcement_level | high | high | sin cambio |
| has_dedicated_ai_authority | (n/d) | 0 | nuevo campo |
| has_specialized_ai_frameworks | (n/d) | 1 | nuevo campo |
| eea_not_eu | (n/d) | 0 | nuevo campo |

---

## 5. Notas de proceso

- Cross-check techieray ejecutado 2026-04-20. Descubrimientos incrementales: ninguno sobre los ya detectados — GBR bien cubierto por IAPP y búsqueda web directa.
- AI White Paper original (CP 815, marzo 2023) disponible solo como HTML en gov.uk. No descargado como PDF — cubierto por Government Response 2024 (doc 2) que es el documento de política vigente y formalmente lo responde.
- Private Members' Bill AI (Regulation) [HL] identificado y excluido: iniciativa parlamentaria privada sin respaldo del ejecutivo; rara vez se convierte en ley.
- OSA 2023 incluida como binding_law AI-adjacent — primera ley britá­nica con provisiones explícitas para IA (chatbots, algoritmos de recomendación, content moderation IA).
- Capa 6 (bill gubernamental pending): vacía. El gobierno Starmer ha señalado posible legislación IA en 2026 pero no hay draft publicado al cierre del corpus (abril 2026).
