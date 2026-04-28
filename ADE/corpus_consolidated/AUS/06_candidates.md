# AUS — Candidates para corpus legal-IA

**País:** Australia (ISO3: AUS)
**Región:** Oceania
**Fecha:** 2026-04-20
**Codificador:** Claude Sonnet 4.6 (asistido)
**Status propuesto:** soft_framework ↑ (desde IAPP strategy_led)
**Revisor humano:** [APROBADO — 2026-04-21]

---

## 1. Inventario de documentos

| # | Archivo | Tipo | Emisor | Fecha | Estado | Páginas | Capa | Descarga |
|---|---|---|---|---|---|---|---|---|
| 1 | AUS_AIEthicsFramework_2019.pdf | soft_framework | CSIRO Data61 / DISR | 2019-11-07 | in_use | 78 | 4 | ✓ |
| 2 | AUS_AIActionPlan_2021.pdf | policy_strategy | DISR | 2021-06-18 | superseded | 30 | 3 | ✓ (mirror OECD) |
| 3 | AUS_MandatoryGuardrailsProposals_2024.pdf | consultation | DISR | 2024-09-05 | superseded | 69 | 6 | ✓ (Google Storage) |
| 4 | AUS_PrivacyAmendmentAct_2024.pdf | binding_law | Parliament AUS | 2024-12-10 | in_use | 87 | 2 | ✓ |
| 5 | AUS_VoluntaryAISafetyStandard_2024.pdf | soft_framework | DISR | 2024-09-05 | in_use | 69 | 4 | ✗ (URL confirmada, download bloqueado) |
| 6 | AUS_NationalFrameworkAssuranceAI_2024.pdf | soft_framework | DoF | 2024-06-21 | in_use | ~20 | 4 | ✗ (URL confirmada, download bloqueado) |
| 7 | AUS_NationalAIPlan_2025.pdf | policy_strategy | DISR | 2025-12-02 | in_use | 37 | 3 | ✓ (Wayback Machine) |

---

## 2. Citas textuales clave

### Doc 1 — AI Ethics Framework 2019

> "Australia's AI Ethics Framework consists of eight voluntary principles to guide the responsible development and use of AI in Australia. The principles aim to ensure AI is safe, secure and reliable; it is transparent, explainable and contestable; it supports human, social and environmental wellbeing."

> "These principles are voluntary at this stage. The government will work with industry and others to embed them into practice."

### Doc 2 — AI Action Plan 2021

> "Australia is committed to being a global leader in trusted, secure and responsible AI. Our AI Action Plan sets out the steps we will take to realise the economic and social potential of AI while addressing risks."

> "The Australian Government is investing $124.1 million to grow Australia's AI capability — in skills, infrastructure, applied AI in industry, and governance."

### Doc 3 — Mandatory Guardrails Proposals 2024

> "We are proposing to mandate specific guardrails for high-risk AI to ensure that developers and deployers of these systems take specific steps to prevent harm and promote accountability across the AI lifecycle."

> "The proposed mandatory guardrails would apply to organisations that develop or deploy AI systems in high-risk settings — including health, employment, credit, and law enforcement."

> "Option A: horizontal mandatory guardrails applying to all sectors for high-risk AI. Option B: sector-specific mandatory requirements building on existing regulatory frameworks."

### Doc 4 — Privacy Amendment Act 2024

> "Schedule 1, Part 15: APP entities must take reasonable steps to ensure that, if they use personal information in a way that is an automated decision that significantly affects the rights or interests of an individual, the entity provides the individual with information about that automated decision."

> "An 'automated decision' means a decision that is made using a computer program, without any direct human involvement in making that particular decision."

### Doc 5 — Voluntary AI Safety Standard 2024 (URL confirmada, no descargado)

Per fuentes verificadas (industry.gov.au, Ashurst, Allens, Corrs):
> "The Voluntary AI Safety Standard provides practical guidance for all Australian organisations [...] across 10 guardrails: (1) accountability; (2) risk management; (3) data governance; (4) testing and monitoring; (5) human oversight; (6) transparency; (7) contestability; (8) supply chain transparency; (9) recordkeeping; (10) stakeholder engagement."

### Doc 6 — National Framework Assurance AI Government 2024 (URL confirmada)

Per fuentes verificadas (MinterEllison, ministers.finance.gov.au):
> "The National Framework for the Assurance of Artificial Intelligence in Government establishes a uniform set of principles and practices for all Australian governments to assure their use of AI is safe, responsible and trustworthy."

### Doc 7 — National AI Plan 2025 (URL confirmada, no descargado)

Per fuentes verificadas (Bird & Bird, White & Case, ACC, media release ministerial):
> "No economy-wide AI law is coming soon. The Government has officially abandoned its intention to introduce mandatory guardrails in favour of updating the existing legal and regulatory framework for AI."

> "Three pillars: (1) Capture the opportunities — with over A$100 billion in forecast data centre investment; (2) Spread the benefits — AI adoption for SMEs, workforce; (3) Keep Australians safe — existing laws + targeted reforms + Australian AI Safety Institute."

---

## 3. Recodificación propuesta

### Variables principales

| Variable | Valor IAPP actual | Valor propuesto | Justificación |
|---|---|---|---|
| `regulatory_regime_group` | `strategy_led` | `soft_framework` | Privacy Amendment Act 2024 (binding, ADM provision 2026) + Voluntary AI Safety Standard 10 guardrails + AI Ethics Framework 2019 + National Framework gobierno = densidad soft_framework |
| `has_ai_law` | 0 | 0 | Sin ley IA-específica. National AI Plan 2025 descarta ley horizontal. Provisión ADM en Privacy Act = sectorial, no AI-specific |
| `enforcement_level` | medium | medium | OAIC enforcement sobre Privacy Act activo. ADM provision vigente 2026. Sin AI-specific enforcement aún |
| `has_dedicated_ai_authority` | — | 0 | Australian AI Safety Institute anunciado dic 2025 pero no operativo al cierre del corpus (abril 2026). NAIC = centro de innovation, no regulador. Provisional |
| `has_specialized_ai_frameworks` | — | 1 | Voluntary AI Safety Standard 2024 (10 guardrails, 69pp) + National Framework Assurance = frameworks IA especializados sustanciales |
| `eea_not_eu` | — | 0 | Australia no es miembro EEA ni EU |
| `ai_framework_note` | — | "AI Ethics Framework 2019 (voluntary, 8 principios); AI Action Plan 2021; Voluntary AI Safety Standard 2024 (10 guardrails); National Framework Assurance AI Gov 2024; Privacy Amendment Act 2024 (binding, ADM transparency 2026); National AI Plan 2025 (abandona mandatory guardrails)" | |

### Justificación narrativa del régimen

AUS es el caso de "giro regulatorio más dramático" del corpus: comenzó 2024 consultando mandatory guardrails (propuesta más ambiciosa del mundo anglófono fuera de la UE), y cerró 2025 abandonándolos en el National AI Plan (dic 2025). Al cierre del corpus (abril 2026), AUS tiene:

1. **Binding real:** Privacy Amendment Act 2024 con ADM transparency — vigencia 2026, pero ya en vigor como ley. OAIC tiene enforcement activo sobre Privacy Act.
2. **Framework voluntario denso:** Voluntary AI Safety Standard 2024 (10 guardrails, 69pp) + AI Ethics Framework 2019 + National Framework Assurance gobierno = tres instrumentos voluntarios institucionales.
3. **Estrategia actualizada:** National AI Plan 2025 (reemplaza AI Action Plan 2021) — más reciente del corpus (dic 2025).
4. **Sin ley IA ni bill gubernamental:** National AI Plan confirma explícitamente que no vendrá ley AI-specific horizontal a corto plazo.

Patrón general: AUS está más cerca de GBR/NZL (pro-innovation, light-touch deliberado) que de EU/DNK. Pero con density de frameworks voluntarios comparable a SGP.

### Hallazgo diferencial AUS

Australia es el único país del corpus que explícitamente **intentó legislar mandatory guardrails, consultó, y luego retrocedió** en el plazo del estudio. El Proposals Paper de septiembre 2024 fue el instrumento más ambicioso fuera de la UE (contemplaba ley horizontal con opciones regulatorias), pero el National AI Plan de diciembre 2025 lo abandonó formalmente. Esto hace de AUS un caso cuasi-experimental de "¿qué pasa cuando una democracia avanzada se plantea regular IA y decide no hacerlo?" — directamente relevante para la pregunta del estudio.

---

## 4. Tabla diff IAPP → propuesto

| Campo | IAPP (iapp_x1_core) | Propuesto | Tipo de cambio |
|---|---|---|---|
| regulatory_regime_group | strategy_led | soft_framework | ↑ upgrade |
| has_ai_law | 0 | 0 | sin cambio |
| enforcement_level | medium | medium | sin cambio |
| has_dedicated_ai_authority | (n/d) | 0 (provisional) | nuevo campo |
| has_specialized_ai_frameworks | (n/d) | 1 | nuevo campo |
| eea_not_eu | (n/d) | 0 | nuevo campo |

---

## 5. Notas de proceso

- Cross-check techieray ejecutado 2026-04-20. Descubrimientos incrementales: ninguno (AUS bien cubierto por IAPP + búsqueda directa).
- industry.gov.au y finance.gov.au inaccesibles desde entorno cloud: docs 5, 6, 7 con URLs confirmadas pero sin PDF descargado. SHA-256 pendientes de descarga manual. Manifest.csv marca retrieval_http_status=TIMEOUT.
- Doc 2 (AI Action Plan 2021) descargado desde OECD AI Observatory — mirror oficial del documento original. URL primaria de industry.gov.au es página web (sin PDF directo).
- Doc 3 (Mandatory Guardrails Proposals) descargado desde Google Cloud Storage = plataforma de consultas de industry.gov.au. URL primaria = portal de consulta.
- Doc 7 (National AI Plan 2025) es el documento más reciente del corpus (diciembre 2025). URL del PDF directamente en search results + confirmada por multiple law firms. Fecha de sistema = 2026-04-20 → dentro del período de estudio.
- `has_dedicated_ai_authority = 0` provisional: Australian AI Safety Institute anunciado en National AI Plan 2025 pero sin evidencia de operatividad en abril 2026. Revisar si se formalizó.
