# SWE — Inventario de documentos y propuesta de recodificación

**País:** Sweden (ISO3: SWE)
**Región:** EU
**EU AI Act:** Sí (directamente aplicable)
**Prioridad:** P1-TOP30 (#16 Microsoft AI Diffusion Report 2025)
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

**Capa 2 — Estrategia nacional:**
- **AI Commission Roadmap / SOU 2025:12 (nov. 2024)** — 75 propuestas al Gobierno. Catalizador de la política IA 2025-2026. Órgano gubernamental ad hoc creado en 2023.
- **Sweden's AI Strategy (feb. 2026)** — primera estrategia IA integral. Objetivo: top-10 global. 3 áreas: societal, sostenible, competitividad.
- **Action Plan for Sweden's AI Strategy (feb. 2026)** — medidas concretas, plazos y responsables.

**Capa 3 — Supervisión DPA:**
- **IMY AI-strategi (2024)** — DPA sueco define posicionamiento y prioridades IA. Activo en enforcement RGPD + AI Act.

**Capa 4 — Mandato Digg + IMY (2024):** Gobierno comisionó a Digg (digitalización pública) + IMY para desarrollar riktlinjer (directrices) para uso de IA generativa en administración pública. Publicación pendiente como PDF final.

### 2.2 Autoridades competentes

- **IMY (Integritetsskyddsmyndigheten):** DPA independiente. Supervisión IA en tratamiento datos personales. MSA sectorial AI Act (candidato). Historial activo de enforcement RGPD.
- **Digg (Myndigheten för digital förvaltning):** Coordinador digitalización pública. Mandato para riktlinjer IA generativa (2024). No es regulador IA formal.
- **Vinnova:** Agencia nacional de innovación. Principal financiador de AI Sweden (centro de IA aplicada). No autoridad regulatoria.
- **AI Sweden:** Plataforma público-privada (140+ socios, academia + industria + gobierno). No autoridad regulatoria.
- **Autoridades sectoriales:** Finansinspektionen (finanzas), IVO (salud), Datainspektionen (datos — fusionado en IMY).

### 2.3 Contexto estratégico

Suecia presenta perfil de **alto desarrollo estratégico IA** con transición hacia implementación institucional robusta:
- AI Commission (órgano gubernamental 2023) → 75 propuestas → Estrategia IA integral (feb. 2026): proceso de política rápido y articulado.
- IMY activo en supervisión IA/RGPD desde 2024, con estrategia interna publicada.
- Sin agencia IA nacional operativa (vs. ESP/AESIA), pero IMY + Digg cubren las dos competencias principales.
- Objetivo explícito top-10 global: ambición alta, respaldada por propuesta de €1.5B de inversión adicional.
- Tradición nórdica de governance digital fuerte (GDPR enforcement riguroso).

---

## 3. Inventario de documentos

### Documento 1 — EU AI Act
| Campo | Valor |
|---|---|
| Archivo | `SWE_EUAIAct_Reg2024_1689.pdf` · Tipo: `binding_law_ai` · Páginas: 144 |
| SHA-256 | `bba630444b3278e881066774002a1d7824308934f49ccfa203e65be43692f55e` |

Ver IRL/CANDIDATES.md §3 Doc 1. Aplicación directa en SWE.

### Documento 2 — AI Commission Roadmap (SOU 2025:12)
| Campo | Valor |
|---|---|
| Archivo | `SWE_AICommission_Roadmap_2024.pdf` · Tipo: `policy_strategy` · Páginas: 136 |
| Fecha | 2024-11-26 · Status: `in_use` |
| SHA-256 | `a29c76eb6ff0ca53849583aa2d3ced80fa9e8b0bec391657d53d24dbb8503ebd` |

**Citas textuales relevantes:**

> "The AI Commission presents a total of 75 proposals for measures, including new inquiries, assignments to government agencies and expanded central government commitments in the form of financing. This is an urgent roadmap for AI in Sweden."

> "Sweden is falling behind in AI development. This is alarming and requires the Government to take a number of urgent steps to avoid Sweden being left behind in international competition, with negative consequences for welfare, security and competitiveness."

> "The Commission proposes that an AI task force be established under the supervision of the Prime Minister's Office to fast-track the implementation of critical AI measures."

### Documento 3 — Sweden's AI Strategy (2026)
| Campo | Valor |
|---|---|
| Archivo | `SWE_AIStrategy_2026.pdf` · Tipo: `policy_strategy` · Páginas: 24 |
| Fecha | 2026-02 · Status: `in_use` |
| SHA-256 | `5b9aec58bc65c6b039e1d07e0bc7f094df4bd61b157fbb61559426bf22e3b445` |

**Citas textuales relevantes:**

> "For the first time ever, Sweden has a holistic AI strategy. The strategy aims for Sweden to be among the world's top ten countries in the field of artificial intelligence."

> "The strategy is divided into three areas: societal development, sustainable development, and competitiveness and innovation, covering everything from the labour market and education to rules simplification, energy and defence, to the business sector, entrepreneurship and research."

> "Sweden will drive development for responsible and secure AI and push for stable international rules, with a focus on mitigating existing risks and protecting personal privacy, copyright and security."

### Documento 4 — Action Plan for Sweden's AI Strategy (2026)
| Campo | Valor |
|---|---|
| Archivo | `SWE_AIStrategyActionPlan_2026.pdf` · Tipo: `policy_strategy` · Páginas: 13 |
| Fecha | 2026-02 · Status: `in_use` |
| SHA-256 | `6c750d7a5aa92591d63b4215e9c2fe59c668f6d56d8710fde3c1652de46fe23a` |

**Citas textuales relevantes:**

> "This action plan sets out concrete measures under each area of Sweden's AI Strategy, specifying timelines, responsible agencies, and budget commitments to achieve the objective of top-10 global AI ranking."

> "Key assignments: Vinnova — AI innovation ecosystem; NAISS — AI compute infrastructure; Digg + IMY — guidelines for generative AI in public administration; Swedish Research Council — AI research funding."

### Documento 5 — IMY AI-strategi (2024)
| Campo | Valor |
|---|---|
| Archivo | `SWE_IMY_AIStrategi.pdf` · Tipo: `guidelines` · Páginas: 5 |
| Fecha | 2024 · Status: `in_force` |
| SHA-256 | `6da4cb82d206861789e717b96ad79c949f69ee2b2d420943c57aed0ac609d08b` |
| Idioma | SV (sueco) — limitación R5 |

**Citas textuales relevantes (SV):**

> "IMY ska verka för att den personliga integriteten skyddas i en tid av snabb AI-utveckling. Myndigheten identifierar tre prioriterade områden: AI inom hälso- och sjukvård, AI i arbetslivet och AI-system med uppgifter om barn."

> "IMY följer noga hur AI-förordningen (EU 2024/1689) kompletterar och samverkar med dataskyddsförordningen, och planerar vägledning och tillsyn inom dessa områden."

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

**`binding_regulation`:** Aplicación directa AI Act + estrategia nacional integral publicada (feb. 2026).

**`enforcement_level: high`** — confirmado respecto a baseline IAPP:
- IMY con historial RGPD activo y estrategia IA interna (2024).
- AI Commission con 75 propuestas formalizadas (SOU 2025:12), proceso de política completo.
- Sweden's AI Strategy (feb. 2026): primera estrategia integral, objetivo top-10, medidas concretas.
- Action Plan con asignaciones presupuestarias a agencias (Vinnova, NAISS, Digg, IMY).
- Mandato Digg+IMY para riktlinjer IA generativa → implementación AI Act en sector público.

### 4.3 Variables adicionales

| Variable | Valor |
|---|---|
| `ai_law_name` | Regulation (EU) 2024/1689 (AI Act) |
| `ai_law_year` | 2024 |
| `ai_law_status` | in_force |
| `national_strategy` | 1 (AI Commission Roadmap 2024 + Sweden's AI Strategy 2026) |
| `has_dedicated_ai_authority` | 0 (IMY + Digg como autoridades competentes, no agencia IA dedicada) |
| `gdpr_or_equivalent` | 1 (GDPR + Lag 2018:218) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `comprehensive` | `binding_regulation` |
| has_ai_law | 1 | 1 ✓ |
| intensity | 10/10 | 10/10 ✓ |
| coverage | 14/15 | 14/15 ✓ |
| enforcement | `high` | `high` ✓ |
| has_dedicated_ai_authority | — | 0 |

**Veredicto:** Codificación IAPP correcta. Diferencial SWE: ciclo de política IA más rápido del corpus UE — AI Commission (2023) → 75 propuestas (nov. 2024) → Estrategia integral (feb. 2026). Sin agencia IA dedicada pero IMY+Digg cubren supervisión. `enforcement_level: high` confirmado por historial IMY + nueva infraestructura estratégica.

---

## 6. Limitaciones y notas

1. **Estrategia IA (feb. 2026) muy reciente.** Publicada 2 meses antes del cierre del corpus. Plan de acción en implementación inicial; efectividad por verificar.
2. **IMY AI-strategi en SV.** No disponible en EN. Limitación R5. Contenido deducible del portal EN de IMY.
3. **Digg riktlinjer IA generativa.** Mandato recibido agosto 2024; publicación final pendiente como PDF. Re-capturar en actualización.
4. **Sin agencia IA dedicada.** A diferencia de ESP (AESIA) o NLD (DCA en AP). IMY + Digg distribuyen competencias regulatorias.
5. **GDPR / Lag 2018:218 no incluida.** Ver IRL/SOURCES.md §5.

---

## 7. Resumen ejecutivo

Suecia presenta régimen `binding_regulation` vía AI Act + **ciclo de política IA más ágil del corpus UE**:
- AI Commission (2023) → SOU 2025:12 con 75 propuestas (nov. 2024) → AI Strategy integral (feb. 2026): 14 meses.
- Primera estrategia IA holística, objetivo top-10 global, €1.5B propuesta inversión adicional.
- IMY (DPA) activo en supervisión IA/RGPD con estrategia interna publicada (2024).
- Sin agencia IA nacional dedicada pero IMY+Digg como autoridades competentes.
- Tradición nórdica de governance digital: enforcement RGPD robusto, alta transparencia institucional.

`enforcement_level: high` confirmado — IAPP correcto. `regulatory_regime: binding_regulation` (reclasificación taxonómica de `comprehensive`).

Corpus: 5 documentos. 1 ley IA-específica UE vinculante + 1 informe comisión (SOU) + 1 estrategia + 1 plan de acción + 1 guideline DPA.
