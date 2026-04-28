# DNK — Inventario de documentos y propuesta de recodificación

**País:** Denmark (ISO3: DNK)
**Región:** EU
**EU AI Act:** Sí (directamente aplicable)
**Prioridad:** P1-TOP30 (#19 Microsoft AI Diffusion Report 2025)
**Fecha:** 2026-04-19
**Codificador:** Claude Sonnet 4.6 (asistido)
**Revisor humano:** Pendiente

---

## 1. Baseline IAPP

| Variable | Valor IAPP actual |
|---|---|
| `regulatory_regime` | `comprehensive` |
| `regulatory_intensity` | 10 |
| `thematic_coverage` | 14 |
| `has_ai_law` | 1 |
| `enforcement` | `high` |

---

## 2. Diagnóstico del ecosistema regulatorio IA

### 2.1 Estructura regulatoria

**Capa 1 — UE directamente aplicable:** EU AI Act desde 01-08-2024.

**Capa 2 — Ley nacional de implementación:**
- **Lov nr. 467 af 14. maj 2025** (vigor 2-8-2025): ley nacional que implementa el marco institucional del AI Act en Dinamarca. Adoptada 8-5-2025; publicada 14-5-2025; **en vigor 2-8-2025** — es la **primera ley nacional de implementación del AI Act en vigor en el corpus completo**, precediendo incluso a la Act LXXV de Hungría (vigor 1-12-2025).

**Capa 3 — Documentos estratégicos:**
- **National Strategy for Artificial Intelligence** (marzo 2019, EN): primera estrategia IA nacional. 74pp, 24 iniciativas, DKK 60M. Tres ejes: liderazgo global responsable, IA para las personas, marco regulatorio.
- **Strategic Approach to Artificial Intelligence** (2-12-2024, EN): documento estratégico de actualización post-AI Act. 28pp. Tres pilares: Digital Taskforce para sector público, Centro de Consultoría IA Responsable, plataforma segura para modelos de lenguaje daneses.

### 2.2 Autoridades competentes (designadas por Lov nr. 467/2025)

- **Digitaliseringsstyrelsen (Agencia de Digitalización):** autoridad de vigilancia de mercado (MSA) central + contact point nacional bajo el AI Act. Dependiente del Ministerio de Digitalización.
- **Datatilsynet (Autoridad Danesa de Datos):** MSA sectorial para sistemas IA que traten datos personales. También actúa como DPA bajo GDPR.
- **Domstolsstyrelsen (Administración de Tribunales):** MSA sectorial para sistemas IA en el ámbito judicial.

### 2.3 Contexto estratégico

Dinamarca presenta una implementación nacional del AI Act **más temprana que cualquier otro país del corpus EU procesado**:
- Lov nr. 467: vigor 2-8-2025 — primera ley de implementación AI Act en vigor a nivel mundial entre los corpus procesados.
- Estructura institucional tripartita clara: MSA central (Digitaliseringsstyrelsen) + MSAs sectoriales (Datatilsynet + Domstolsstyrelsen).
- Evolución estratégica documentada: National AI Strategy 2019 (fundamentación) → Strategic Approach 2024 (respuesta al AI Act).
- has_dedicated_ai_authority=1: Digitaliseringsstyrelsen designada formalmente como MSA y contact point.

---

## 3. Inventario de documentos

### Documento 1 — EU AI Act
| Campo | Valor |
|---|---|
| Archivo | `DNK_EUAIAct_Reg2024_1689.pdf` · Tipo: `binding_law_ai` · Páginas: 144 |
| SHA-256 | `bba630444b3278e881066774002a1d7824308934f49ccfa203e65be43692f55e` |

Ver IRL/CANDIDATES.md §3 Doc 1. Aplicación directa en DNK. Complementado por Lov nr. 467/2025 como ley nacional de implementación.

### Documento 2 — Lov nr. 467 af 14. maj 2025
| Campo | Valor |
|---|---|
| Archivo | `DNK_LovNr467_2025_AIAct.pdf` · Tipo: `binding_regulation` · Páginas: 178 |
| Fecha | 2025-05-14 · Status: `in_force` (vigor 2-8-2025) |
| SHA-256 | `254e0c8567c567a0d706825a25da9c5c85b19e4f1796931b0fbfedbec2bbab00` |
| Idioma | DA (incluye EU AI Act como anexo en EN) |

**Título oficial:** *Lov om supplerende bestemmelser til forordningen om kunstig intelligens* (Act on Supplementary Provisions to the Regulation on Artificial Intelligence).

**Citas textuales relevantes (DA):**

> "§ 1. Loven fastsætter supplerende bestemmelser til Europa-Parlamentets og Rådets forordning (EU) 2024/1689 af 13. juni 2024 om harmoniserede regler for kunstig intelligens (AI-forordningen)."

> "§ 4. Digitaliseringsstyrelsen er markedsovervågningsmyndighed efter AI-forordningens artikel 70 og national kontaktpunkt efter AI-forordningens artikel 70, stk. 2."

> "§ 5. Datatilsynet er markedsovervågningsmyndighed inden for sit kompetenceområde, herunder behandling af personoplysninger."

> "§ 6. Domstolsstyrelsen er markedsovervågningsmyndighed for AI-systemer, der anvendes af domstolene."

### Documento 3 — National Strategy for Artificial Intelligence 2019 (EN)
| Campo | Valor |
|---|---|
| Archivo | `DNK_AIStrategy_2019.pdf` · Tipo: `policy_strategy` · Páginas: 74 |
| Fecha | 2019-03 · Status: `in_use` (vigente; actualizada por Strategic Approach 2024) |
| SHA-256 | `fc83323ff261ce18db00ce235508225a3624961d38ef66ba2f3512019e3941df` |

**Citas textuales relevantes:**

> "Denmark's ambition is to be at the forefront of developing and using artificial intelligence (AI). We want to be an inclusive society where AI is a tool that creates prosperity for everyone, advances the green transition, and ensures better welfare solutions. We will achieve this while maintaining our traditions for openness, trust, and security."

> "The strategy contains 24 initiatives organised around three overall objectives: (1) Denmark as a global leader in responsible AI; (2) AI for the benefit of all Danes; (3) A framework for AI — regulation and ethics."

> "The Danish government will invest DKK 60 million in AI initiatives in the coming years, in addition to existing investments in digitalisation, research and education."

### Documento 4 — Strategic Approach to Artificial Intelligence 2024 (EN)
| Campo | Valor |
|---|---|
| Archivo | `DNK_StrategicApproachAI_2024.pdf` · Tipo: `policy_strategy` · Páginas: 28 |
| Fecha | 2024-12-02 · Status: `in_use` |
| SHA-256 | `cc675b7e48fcf0d3cef9d800113cccbe58f9e4bd6fa7135d6ecc79bc66e8ddc9` |

**Citas textuales relevantes:**

> "The Government's strategic approach to artificial intelligence is based on the premise that AI should be used in a way that is safe, ethical, and beneficial to the whole of society. Denmark will be a responsible AI nation."

> "Three key initiatives: (1) A Digital Taskforce for the public sector to coordinate and accelerate the responsible use of AI in government; (2) An Advisory Centre for Responsible AI, providing public authorities with guidance on AI adoption; (3) A secure platform for Danish language models, ensuring Denmark has access to AI capabilities that understand Danish language, culture, and context."

---

## 4. Propuesta de recodificación

### 4.1 Variables principales

| Variable | Valor IAPP | Propuesta estudio | Cambio |
|---|---|---|---|
| `has_ai_law` | 1 | **1** | Sin cambio |
| `regulatory_regime` | `comprehensive` | **`binding_regulation`** | Reclasificación taxonómica |
| `regulatory_intensity` | 10 | **10** | Sin cambio |
| `thematic_coverage` | 14 | **14** | Sin cambio |
| `enforcement_level` | `high` (IAPP) | **`high`** | Confirmación |
| `regulatory_regime_group` | — | **`binding_regulation`** | Adición |

### 4.2 Justificación

**`binding_regulation`:** EU AI Act (directo) + **Lov nr. 467/2025 (ley nacional de implementación en vigor desde 2-8-2025)** — primera ley de implementación AI Act en vigor de todo el corpus. Combinación vinculante completa.

**`enforcement_level: high`** — confirmado vs. IAPP:
- Lov nr. 467/2025 en vigor: primera ley de implementación AI Act en el corpus.
- Autoridades formalmente designadas: Digitaliseringsstyrelsen (MSA central + contact point), Datatilsynet (MSA sectorial datos), Domstolsstyrelsen (MSA sectorial judicial).
- Estructura institucional tripartita operativa.
- Evolución estratégica documentada: 2019 → 2024.
- Datatilsynet como DPA GDPR garantiza supervisión datos/IA desde institución independiente.

**Nota comparativa corpus:** DNK supera a HUN (vigor dic. 2025) en anticipación temporal. Es el primer Estado UE del corpus con ley de implementación AI Act plenamente en vigor.

### 4.3 Variables adicionales

| Variable | Valor |
|---|---|
| `ai_law_name` | Regulation (EU) 2024/1689 (AI Act) + Lov nr. 467 af 14. maj 2025 (implementación nacional) |
| `ai_law_year` | 2024 (UE) / 2025 (nacional) |
| `ai_law_status` | in_force |
| `national_strategy` | 1 (National AI Strategy 2019 + Strategic Approach 2024) |
| `has_dedicated_ai_authority` | 1 (Digitaliseringsstyrelsen como MSA central + contact point) |
| `gdpr_or_equivalent` | 1 (GDPR + Databeskyttelsesloven 2018) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `comprehensive` | `binding_regulation` |
| has_ai_law | 1 | 1 ✓ |
| intensity | 10/10 | 10/10 ✓ |
| coverage | 14/15 | 14/15 ✓ |
| enforcement | `high` | `high` ✓ |
| has_dedicated_ai_authority | — | 1 (Digitaliseringsstyrelsen MSA) |

**Veredicto:** Codificación IAPP correcta. Diferencial DNK: **primera ley nacional de implementación AI Act en vigor del corpus completo** (Lov nr. 467/2025, desde 2-8-2025 — antes que HUN dic. 2025, IRL y ESP pendientes). `has_dedicated_ai_authority=1` por designación formal de Digitaliseringsstyrelsen.

---

## 6. Limitaciones y notas

1. **Lov nr. 467 en DA.** El texto legislativo es en danés. La ley incluye el EU AI Act como anexo (en inglés). No hay traducción EN oficial de la ley complementaria al cierre del corpus.
2. **URL retsinformation.dk: canónica vs. API.** La URL ELI canónica (`/eli/lta/2025/467`) devuelve HTML. El PDF completo se descargó desde el endpoint API (`/api/pdf/249582`). Ambas URLs documentadas.
3. **Bekendtgørelse nr. 605/2025 no incluida.** Reglamento ejecutivo de Lov nr. 467 disponible en retsinformation.dk; no descargado al cierre del corpus por limitación de alcance (implementación legislativa cubierta por la ley principal).
4. **Datatilsynet guidance AI.** La Autoridad Danesa de Datos no ha publicado guidance AI específica como PDF independiente al cierre del corpus.
5. **GDPR + Databeskyttelsesloven (Lov nr. 502/2018) no incluidas.** Ver IRL/SOURCES.md §5 para exclusión metodológica.

---

## 7. Resumen ejecutivo

Dinamarca presenta **el régimen de implementación nacional del AI Act más temprano en vigor** de todo el corpus procesado:
- Lov nr. 467/2025 (vigor 2-8-2025): **primera ley nacional de implementación AI Act en vigor** — antes que HUN (dic. 2025), IRL (General Scheme, bill_pending) y ESP (Anteproyecto, bill_pending).
- Autoridades formalmente designadas: Digitaliseringsstyrelsen (MSA central + contact point) + Datatilsynet (MSA datos) + Domstolsstyrelsen (MSA judicial).
- Evolución estratégica documentada: National AI Strategy 2019 (74pp, fundacional) → Strategic Approach 2024 (28pp, post-AI Act).
- `has_dedicated_ai_authority=1`: Digitaliseringsstyrelsen designada explícitamente.

`enforcement_level: high` confirmado — IAPP correcto. `regulatory_regime: binding_regulation` (EU AI Act + ley nacional vigente).

Corpus: 4 documentos. 1 ley UE vinculante + 1 ley nacional implementación AI Act + 2 estrategias (2019 EN + 2024 EN).
