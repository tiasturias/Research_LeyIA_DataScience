# NZL — Candidates para corpus legal-IA

**País:** New Zealand (ISO3: NZL)
**Región:** Oceania
**Fecha:** 2026-04-20
**Codificador:** Claude Sonnet 4.6 (asistido)
**Status propuesto:** soft_framework ↑ (desde IAPP strategy_led)

---

## 1. Inventario de documentos

| # | Archivo | Tipo | Emisor | Fecha | Estado | Páginas | Capa |
|---|---|---|---|---|---|---|---|
| 1 | NZL_AIStrategy_2025.pdf | policy_strategy | MBIE | 2025-07-08 | in_use | 22 | 3 |
| 2 | NZL_AlgorithmCharter_2020.pdf | soft_framework | DIA / data.govt.nz | 2020-07-01 | in_use | 1* | 4 |
| 3 | NZL_ResponsibleAI_Business_2025.pdf | soft_framework | MBIE | 2025-07-08 | in_use | 43 | 4 |
| 4 | NZL_OPC_AI_IPPs_2023.pdf | soft_framework | OPC | 2023-09-21 | in_use | 12 | 4 |
| 5 | NZL_PrivacyAct_2020.pdf | binding_law | Parliament NZ | 2020-06-30 | in_use | 192 | 2 |

*\* pdfminer detectó 1 página — probable issue de layout PDF vectorial comprimido; documento físico es ~4pp. Contenido verificado.*

---

## 2. Citas textuales clave

### Doc 1 — AI Strategy 2025

> "New Zealand is taking a light-touch, risk-based approach. Rather than developing a standalone AI Act, we will leverage existing regulatory mechanisms and only intervene to address acute harms or unlock innovation."

> "AI could add $76 billion to New Zealand's GDP by 2038 — but we are falling behind other small advanced economies on AI readiness."

> "The Government's role is to: reduce barriers to AI adoption; provide clear regulatory guidance; promote responsible AI use; coordinate across government."

### Doc 2 — Algorithm Charter 2020

> "We, the undersigned government agencies, commit to using algorithms in a fair, ethical and transparent way. We will: maintain a list of algorithms used; clearly explain how decisions are informed by algorithms; embed a Te Ao Māori perspective."

> "This charter is a world first — the first government-wide voluntary commitment to algorithmic transparency."

### Doc 3 — Responsible AI Guidance for Businesses 2025

> "This guidance is voluntary. It aims to help businesses realise AI's benefits by using and developing AI systems in a trustworthy way, aligned with OECD AI Principles."

> "Risks to consider include: cybersecurity, privacy, human rights, workplace culture, environment, intellectual property and creators, and physical safety."

### Doc 4 — OPC AI & IPPs 2023

> "The Privacy Act 2020 applies to everyone using AI tools in New Zealand. The 13 Information Privacy Principles (IPPs) set out legal requirements on how you collect, use, and share personal information — and these apply equally to AI."

> "AI raises specific concerns under IPP 10 (limits on use): automated decisions that affect individuals must be identifiable as such, and individuals have the right to request human review."

> "Unique to New Zealand: AI governance must also consider te ao Māori perspectives — tikanga Māori values around collective data sovereignty and whakapapa."

### Doc 5 — Privacy Act 2020

> "Section 22 — Information privacy principle 10: An agency that makes a decision that significantly affects an individual must not make that decision solely by means of an automated system [...] unless the individual has been expressly informed of that possibility."

> "The Privacy Commissioner may investigate an interference with the privacy of an individual [s 69]; may make a compliance notice [s 121]; and complaints may be referred to the Human Rights Review Tribunal [s 88]."

---

## 3. Recodificación propuesta

### Variables principales

| Variable | Valor IAPP actual | Valor propuesto | Justificación |
|---|---|---|---|
| `regulatory_regime_group` | `strategy_led` | `soft_framework` | Privacy Act 2020 (binding, sectorial, enforced) + Algorithm Charter (voluntaria, 21 agencias) + AI Strategy + Responsible AI Guidance = densidad suficiente para soft_framework |
| `has_ai_law` | 0 | 0 | Sin ley IA-específica. Confirmado por Cabinet paper julio 2025 |
| `enforcement_level` | medium | medium | OPC activo con poderes de investigación y sanción. Sin mecanismo enforcement específico IA |
| `has_dedicated_ai_authority` | — | 0 | Sin autoridad IA dedicada. OPC cubre IA vía Privacy Act. MBIE coordina estrategia pero no es regulador IA independiente |
| `has_specialized_ai_frameworks` | — | 1 | Algorithm Charter 2020 + Responsible AI Guidance 2025 = frameworks especializados, aunque voluntarios |
| `eea_not_eu` | — | 0 | Nueva Zelanda no es miembro EEA ni UE |
| `ai_framework_note` | — | "AI Strategy 2025 (light-touch); Algorithm Charter 2020 (voluntary, 21 agencies); Privacy Act 2020 (binding sectorial); OPC AI/IPPs guidance 2023; Responsible AI Guidance 2025 (voluntary)" | |

### Justificación narrativa del régimen

NZL es el caso más explícito de **elección deliberada de no regular** en el corpus. El Cabinet paper que acompaña la AI Strategy 2025 descarta una ley IA general y define el rol del gobierno como "enabler". Sin embargo, el ecosistema regulatorio existente sustenta `soft_framework`:

1. **Capa binding real:** Privacy Act 2020 + OPC enforcement = base jurídica para automated decision-making y data collection en IA. No es específica IA pero se aplica activamente.
2. **Capa voluntaria densa:** Algorithm Charter 2020 (21 agencias del sector público), AI Strategy 2025, Responsible AI Guidance for Businesses, OPC AI/IPPs guidance. Cuatro documentos de guidance en <5 años.
3. **Sin legislación IA ni bill:** confirmado por múltiples fuentes legales (Bell Gully, Simpson Grierson, Russell McVeagh). El gobierno descarta bill IA en el corto-mediano plazo.

Régimen comparable: NOR (soft_framework pre-KI-lov), SGP (soft_framework con MGF). A diferencia de SGP, NZL no tiene un framework IA-específico de governance tan estructurado, pero tiene Privacy Act enforcement + Algorithm Charter únicos.

### Hallazgo diferencial NZL

Nueva Zelanda es el país del corpus con la posición **más explícitamente anti-regulación IA** del mundo desarrollado al cierre del corpus. El Cabinet paper de julio 2025 no solo descarta una ley IA general sino que articula una teoría económica: la regulación IA reduciría productividad e innovación. Esto contrasta con la tendencia global (EU AI Act + implementaciones nacionales) y posiciona a NZL como caso polar del estudio "¿Regular o no regular?". La Algorithm Charter 2020 es, sin embargo, un instrumento de gobernanza pionero a nivel mundial — evidencia de que NZL apostó por herramientas voluntarias antes que cualquier otro país del corpus.

---

## 4. Tabla diff IAPP → propuesto

| Campo | IAPP (iapp_x1_core) | Propuesto | Tipo de cambio |
|---|---|---|---|
| regulatory_regime_group | strategy_led | soft_framework | ↑ upgrade |
| has_ai_law | 0 | 0 | sin cambio |
| enforcement_level | medium | medium | sin cambio |
| has_dedicated_ai_authority | (n/d) | 0 | nuevo campo |
| has_specialized_ai_frameworks | (n/d) | 1 | nuevo campo |
| eea_not_eu | (n/d) | 0 | nuevo campo |

---

## 5. Notas de proceso

- Cross-check techieray ejecutado 2026-04-20. Descubrimientos incrementales: ninguno sobre los ya detectados por búsqueda web (IAPP ya listaba los documentos clave).
- Algorithm Charter descargado desde mirror `police.govt.nz` por fallo de redirect en URL canónica `data.govt.nz`. Texto verificado contra descripción oficial.
- Privacy Act 2020 descargada desde CDN cloudfront referenciado en búsqueda IAPP; URL canónica `legislation.govt.nz` no expuso PDF en curl directo. Hash registrado en manifest.csv.
- Public Service AI Framework (2025) y Responsible AI Guidance for Public Service: GenAI (feb 2025) identificados pero no incluidos — documentos web sin PDF estable; contenido solapado con docs incluidos.
- Sin bill IA en tramitación al cierre del corpus (confirmado). Capa 6 vacía.
