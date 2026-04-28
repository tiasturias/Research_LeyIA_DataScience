# NOR — Inventario de documentos y propuesta de recodificación

**País:** Norway (ISO3: NOR)
**Región:** Europe-Other (EEA, no UE)
**EU AI Act:** No aplicable directamente (EEA — incorporación en trámite)
**Prioridad:** P1-TOP30 (#59 muestra / P1-TOP30 Microsoft AI Diffusion Report 2025)
**Fecha:** 2026-04-20
**Codificador:** Claude Sonnet 4.6 (asistido)
**Revisor humano:** Pendiente

---

## 1. Baseline IAPP

| Variable | Valor IAPP actual |
|---|---|
| `regulatory_regime` | `strategy_led` |
| `regulatory_intensity` | 4 |
| `thematic_coverage` | 8 |
| `has_ai_law` | 0 |
| `enforcement` | `medium` |

---

## 2. Diagnóstico del ecosistema regulatorio IA

### 2.1 Estructura regulatoria

**Nota previa — EEA vs. UE:** Noruega es miembro del EEA (European Economic Area) pero NO de la UE. El EU AI Act no es directamente aplicable — requiere incorporación al Acuerdo EEA mediante Decisión del Comité del EEA + ley nacional de implementación. Este proceso está en curso.

**Capa 2 — Leyes sectoriales vinculantes (aplicables a IA):**
- **GDPR** incorporado vía EEA Agreement (Personopplysningsloven — Lov om behandling av personopplysninger, 2018). Vinculante. Art. 22 GDPR aplica directamente a sistemas IA de toma de decisiones automatizadas. No incluido en corpus (criterio de exclusión metodológica).

**Capa 3 — Documentos estratégicos:**
- **National Strategy for Artificial Intelligence 2020** (67pp EN): estrategia IA fundacional. Cinco áreas: datos, competencias, I+D, sector público, regulación/ética.
- **The Digital Norway of the Future 2024–2030** (108pp EN): estrategia de digitalización nacional con capítulo AI. Incluye plan de infraestructura IA nacional + KI-Norge.

**Capa 4 — Frameworks voluntarios / guidance:**
- **Datatilsynet "Strategi for arbeid med kunstig intelligens"** (12pp NO, 22-03-2024): marco de actuación del DPA noruego frente a IA. Sustenta el **AI Regulatory Sandbox** operativo desde 2020.

**Capa 6 — Bill pendiente:**
- **Høringsnotat KI-lov 2025** (63pp NO): borrador de ley de IA para implementar el AI Act en el EEA noruego. Consulta pública 30-6-2025 al 30-9-2025. Vigencia prevista: verano 2026. MSA propuesta: Nkom.

### 2.2 Autoridades competentes

**Actualmente activas:**
- **Datatilsynet:** DPA independiente bajo Personopplysningsloven/GDPR. Opera **sandbox IA** desde 2020 — el primero de los países nórdicos. Competencia sobre IA que trate datos personales.
- **Nkom (Nasjonal kommunikasjonsmyndighet):** propuesta como MSA coordinadora en høringsnotat 2025. Actualmente sin mandato IA formal — pendiente aprobación de la KI-lov.

**Nota:** Noruega no tiene MSA formal designada al cierre del corpus (april 2026). Nkom está propuesta pero no designada.

### 2.3 Contexto estratégico: EEA y diferencial nórdico

Noruega es un caso único en el corpus por ser **EEA pero no UE**:

| Aspecto | NOR (EEA) | DNK (EU) | SWE (EU) |
|---|---|---|---|
| EU AI Act | Incorporación pendiente | Directamente aplicable | Directamente aplicable |
| Ley nacional impl. | bill_pending (høring jun. 2025) | in_force (2-8-2025) | bill_pending |
| MSA designada | No | Sí (Digitaliseringsstyrelsen) | Parcialmente |
| AI Sandbox DPA | Sí (desde 2020) | Sí (Datatilsynet DK) | Sí (IMY) |

**Diferencial positivo NOR:**
- Datatilsynet sandbox IA desde 2020 — capacidad institucional demostrada.
- Inversión en infraestructura IA nacional (Digital Norway 2024).
- KI-Norge: nueva arena nacional para uso innovador y responsable de IA (anunciada 2025).
- Høringsnotat 2025 sigue exactamente el modelo danés (Lov nr. 467) — implementación via ley "complementaria".

**Diferencial negativo:**
- No tiene binding AI Act en vigor ni en bill_pending avanzado (vs. DNK que ya tiene ley in_force).
- EEA incorporation adds an extra step vs. EU member states.

---

## 3. Inventario de documentos

### Documento 1 — National Strategy for Artificial Intelligence 2020 (EN)
| Campo | Valor |
|---|---|
| Archivo | `NOR_AIStrategy_2020.pdf` · Tipo: `policy_strategy` · Páginas: 67 |
| Fecha | 2020 · Status: `in_use` (vigente; complementada por Digital Norway 2024) |
| SHA-256 | `892057f082701847309642f89c2992a4e8c203f0195aa352a4b8a505daa2249f` |
| Idioma | EN (oficial) |

**Citas textuales relevantes:**

> "Norway's government will design an AI policy based on Norwegian and international experiences, and will ensure that the laws and regulations are adapted to the opportunities and challenges that AI entails."

> "The Norwegian Government will focus on five areas of policy: (1) Access to data; (2) Competence, research and development; (3) Digitalisation of industry and the public sector; (4) Infrastructure and technology; (5) Ethics and legal frameworks."

> "Norway is well positioned for succeeding with artificial intelligence. We have extensive digital infrastructure and a culture of trust between citizens, business sector and the public sector. We have a society with large high-quality datasets and digital competence."

### Documento 2 — The Digital Norway of the Future 2024–2030 (EN)
| Campo | Valor |
|---|---|
| Archivo | `NOR_DigitalNorway_2024.pdf` · Tipo: `policy_strategy` · Páginas: 108 |
| Fecha | 2024-09-26 · Status: `in_use` |
| SHA-256 | `2f4c03c7f38917ff07fa1aaaf8c82e17cf9fa19647304a712872e083983d5b8f` |
| Idioma | EN (oficial) |

**Citas textuales relevantes:**

> "Towards 2030, the Government will establish a national infrastructure for artificial intelligence (AI), placing Norway at the vanguard of ethical and safe AI use."

> "The Government will establish KI-Norge – a new national arena for innovative and responsible use of AI, which will serve as one component in the national governance system."

> "We are taking the lead on digital transformation. The goal is for Norway to be the world's most digitalised country by 2030."

### Documento 3 — Høringsnotat KI-lov 2025 (NO)
| Campo | Valor |
|---|---|
| Archivo | `NOR_KILovHoringsnotat_2025.pdf` · Tipo: `bill_pending` · Páginas: 63 |
| Fecha | 2025-06-30 · Status: `bill_pending` |
| SHA-256 | `0d9941fff9e7b3cb55459b688c442f046103ee9398a4b7efa3ef8028b4f67621` |
| Idioma | NO (R5) |

**Citas textuales relevantes (NO):**

> "Formålet med høringsnotatet er å informere om innholdet i EUs forordning om kunstig intelligens og foreslå en norsk lov om kunstig intelligens som gjennomfører forordningen i norsk rett."

> "Nkom (Nasjonal kommunikasjonsmyndighet) foreslås som nasjonal koordinerende tilsynsmyndighet etter KI-forordningen artikkel 70."

> "Det foreslås at loven trer i kraft fra og med 2. august 2026, tilsvarende når de sentrale bestemmelsene i KI-forordningen begynner å gjelde i EU."

### Documento 4 — Datatilsynet AI Strategi 2024 (NO)
| Campo | Valor |
|---|---|
| Archivo | `NOR_Datatilsynet_AIStrategi_2024.pdf` · Tipo: `soft_framework` · Páginas: 12 |
| Fecha | 2024-03-22 · Status: `in_use` |
| SHA-256 | `d168011415163d859c35c37207e418ec9349a48a90418e37875d630bb1176683` |
| Idioma | NO (R5) |

**Relevancia:** Marco de actuación del DPA noruego frente a IA. Tres focos: personas (derechos), sociedad (impactos colectivos) y empresas (obligaciones). Sustenta el Regulatory Sandbox IA de Datatilsynet (operativo desde 2020, el primero de los países nórdicos).

---

## 4. Propuesta de recodificación

### 4.1 Variables principales

| Variable | Valor IAPP | Propuesta estudio | Cambio |
|---|---|---|---|
| `has_ai_law` | 0 | **0** | Sin cambio |
| `regulatory_regime` | `strategy_led` | **`soft_framework`** | Reclasificación ascendente |
| `regulatory_intensity` | 4 | **4** | Sin cambio |
| `thematic_coverage` | 8 | **8** | Sin cambio |
| `enforcement_level` | `medium` (IAPP) | **`medium`** | Confirmación |
| `regulatory_regime_group` | — | **`soft_framework`** | Adición |

### 4.2 Justificación

**`soft_framework`** (vs. IAPP `strategy_led` → equivale a `strategy_only` en mi taxonomía):

La reclasificación de `strategy_only` a `soft_framework` se justifica por:
1. **GDPR vinculante vía EEA** (Art. 22 — toma de decisiones automatizadas): existe regulación sectorial de IA de facto.
2. **Datatilsynet AI Regulatory Sandbox** operativo desde 2020 — framework institucional activo, no meramente declarativo.
3. **Datatilsynet AI Estrategia** (2024): guidance específica IA del DPA, con tres focos operativos.
4. **Digital Norway 2024** con capítulo IA + KI-Norge: segunda generación estratégica.
5. **Høringsnotat KI-lov 2025**: el avance a proyecto de ley con consulta pública cerrada muestra progresión hacia `binding_regulation`.

La combinación GDPR vinculante + sandbox activo + DPA guidance + dos estrategias + bill avanzado supera el umbral `strategy_only` → `soft_framework`.

**`enforcement_level: medium`** — confirmado vs. IAPP:
- Datatilsynet activo en AI (sandbox + guidance + enforcement GDPR/IA).
- No hay MSA formal designada bajo AI Act aún.
- Nkom propuesta pero sin mandato legal.
- Sin ley AI Act en vigor.

### 4.3 Variables adicionales

| Variable | Valor |
|---|---|
| `ai_law_name` | KI-lov (høringsnotat jun. 2025 — bill_pending) |
| `ai_law_year` | 2026 (previsto) |
| `ai_law_status` | bill_pending (consulta cerrada; Stortingsproposisjon pendiente) |
| `national_strategy` | 1 (National AI Strategy 2020 + Digital Norway 2024–2030) |
| `has_dedicated_ai_authority` | 0 (Nkom propuesta; Datatilsynet competente en AI/GDPR pero no es MSA AI Act) |
| `gdpr_or_equivalent` | 1 (GDPR + Personopplysningsloven vía EEA) |
| `eea_not_eu` | 1 (nota metodológica: EEA member, EU AI Act applicability via separate EEA incorporation) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `strategy_led` | `soft_framework` |
| has_ai_law | 0 | 0 ✓ |
| intensity | 4/10 | 4/10 ✓ |
| coverage | 8/15 | 8/15 ✓ |
| enforcement | `medium` | `medium` ✓ |
| has_dedicated_ai_authority | — | 0 (Nkom propuesta) |
| eea_not_eu | — | 1 (distinción metodológica) |

**Veredicto:** Reclasificación ascendente vs. IAPP. `strategy_led` → `soft_framework` por: GDPR vinculante + Datatilsynet sandbox IA (desde 2020) + DPA guidance 2024 + høringsnotat 2025 avanzado. Los valores cuantitativos (intensity=4, coverage=8) se mantienen.

---

## 6. Limitaciones y notas

1. **Status høringsnotat al cierre del corpus.** La consulta pública cerró el 30-9-2025. La Stortingsproposisjon (Prop.) al Storting aún no ha sido presentada o publicada al cierre del corpus (abril 2026). Status conservador: `bill_pending`.
2. **Corpus NOR mayoritariamente en EN.** Excepción: høringsnotat (NO) + Datatilsynet estrategia (NO). Dos documentos con R5.
3. **EEA incorporation gap.** El AI Act no entrará en vigor en Noruega por aplicación directa (como en UE), sino via Decisión EEA + ley nacional. El proceso puede añadir 6-12 meses al calendario. El verano 2026 asume coordinación EEA exitosa.
4. **KI-Norge no incluido.** La nueva arena nacional KI-Norge anunciada en Digital Norway 2024 no tiene documento/PDF independiente al cierre del corpus.
5. **Riksrevisjonen "Bruk av kunstig intelligens i staten" (Dok 3:18).** Informe oficial del Auditor General sobre uso de IA en el Estado (2023-2024). No incluido por enfoque de auditoría (no regulatorio directo); útil como fuente complementaria.
6. **Datatilsynet "AI and Privacy" (2018).** Informe inglés temprano. Fecha demasiado anterior (2018) para el estudio; solo referenciado como contexto.

---

## 7. Resumen ejecutivo

Noruega presenta un **soft_framework** con trayectoria clara hacia `binding_regulation`:
- **National AI Strategy 2020** (67pp EN): fundacional, cinco áreas.
- **Digital Norway 2024–2030** (108pp EN): segunda generación + KI-Norge + infraestructura IA nacional.
- **Datatilsynet sandbox IA** desde 2020: primer sandbox nórdico — indicador de capacidad institucional.
- **Datatilsynet AI Estrategia** (12pp NO, 2024): guidance DPA operativa.
- **Høringsnotat KI-lov 2025** (63pp NO): borrador de ley con consulta pública cerrada — vigencia prevista verano 2026, Nkom como MSA propuesta.

**Diferencial EEA:** Noruega no puede beneficiarse de la aplicación directa del EU AI Act — requiere Decisión EEA + ley nacional. Retraso estructural vs. países EU del corpus (incluso vs. DEU con KI-MIG bill_pending).

`enforcement_level: medium` confirmado. `has_dedicated_ai_authority: 0`. `regulatory_regime: soft_framework` (reclasificación ascendente desde IAPP `strategy_led`).

Corpus: 4 documentos. 2 estrategias (EN oficial) + 1 høringsnotat bill_pending (NO) + 1 DPA strategy (NO).
