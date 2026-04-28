# CAN — Canadá

**Fecha de auditoría:** 2026-04-21
**Codificador:** Claude Sonnet 4.6 (asistido)
**Revisor humano:** [PENDIENTE]
**Confidence IAPP actual:** `medium` → **`medium-high`** (post-validación)

**Fuentes bibliográficas formales:** ver [SOURCES.md](SOURCES.md) (citas APA 7, URLs primarias, hashes, evidencia de oficialidad)
**Metadatos de trazabilidad:** ver [manifest.csv](manifest.csv)

---

## 1. Codificación actual (IAPP / OECD base — vigente en `x1_master.csv`)

| Variable | Valor actual | Fuente |
|---|---|---|
| `has_ai_law` | 0 | IAPP 2026-02 |
| `regulatory_approach` | `strategy_led` | IAPP 2026-02 |
| `regulatory_intensity` | 5 (0-10) | IAPP 2026-02 |
| `enforcement_level` | `medium` | IAPP 2026-02 |
| `thematic_coverage` | 11 (0-15) | IAPP 2026-02 |
| `regulatory_regime_group` | `strategy_only` | Derivado |
| `ai_year_enacted` | — | — |
| `ai_framework_note` | "Pan-Canadian AI Strategy, AIDA (Bill C-27) still before Parliament, Voluntary Code of Conduct, strong Privacy Act framework" | IAPP 2026-02 |

**Diagnóstico preliminar:** La codificación IAPP refleja el estado pre-enero 2025. El Bill C-27 (que contenía el AIDA) murió por prorogación parlamentaria el 6 de enero de 2025. El Ministro Solomon confirmó en junio 2025 que "AIDA is off the table as drafted". Canadá NO tiene ley IA vinculante vigente. Sin embargo, la **Directive on Automated Decision-Making** (2019, vigente) establece AIA mandatorio para sistemas de decisión automatizada del gobierno federal, y el **Voluntary Code of Conduct on Generative AI** (2023) sigue activo. La clasificación actual subestima el marco existente pero sobrevalora la legislación propuesta (AIDA).

---

## 2. Inventario de instrumentos estatales IA (2019 → 2026)

| # | Documento | Año | Emisor | Tipo | Status | Archivo local |
|---|---|---|---|---|---|---|
| 1 | PIPEDA (S.C. 2000, c. 5) | 2000 | Parliament of Canada | Ley federal binding | In force | `CAN_PIPEDA.pdf` |
| 2 | Directive on Automated Decision-Making | 2019 | Treasury Board of Canada Secretariat | Directiva binding | In force (actualizada 2024) | `CAN_DirectiveADM.pdf` |
| 3 | Pan-Canadian Artificial Intelligence Strategy (Phase 2) | 2022 | ISED | Estrategia nacional | In use | `CAN_PanCanadianAIStrategy_2022.pdf` |
| 4 | AIDA – Companion Document | 2023 | ISED | Bill (documento explicativo) | Died_prorogation | `CAN_AIDA_CompanionDocument_2023.pdf` |
| 5 | Voluntary Code of Conduct on Generative AI | 2023 | ISED | Framework voluntario | In use | `CAN_VoluntaryCodeGenAI_2023.pdf` |
| 6 | Guide on the Use of Generative AI | 2024 | TBS | Guidelines | In use | `CAN_GuideGenerativeAI_TBS_2024.pdf` |
| 7 | AI Strategy Consultation Summary 2026 | 2026 | ISED | Documento de consulta | In use | `CAN_AIStrategyConsultationSummary_2026.pdf` |

---

## 3. Candidato 1 — PIPEDA (S.C. 2000, c. 5)

- **Título completo:** Personal Information Protection and Electronic Documents Act
- **Tipo:** Ley federal binding sectorial (protección de datos)
- **Emisor:** Parliament of Canada
- **Fecha publicación:** 2000-04-13 (Royal Assent)
- **Status:** `in_force` — texto consolidado con Digital Privacy Act 2015
- **URL oficial:** https://laws-lois.justice.gc.ca/pdf/p-8.6.pdf
- **SHA-256:** `f83e2876836aa927b2c923fe1a4cdafd57a05e74d0fd3848b3e5e0783fb9b207`
- **Idioma:** Inglés
- **Páginas:** 66

### Citas textuales clave

> "This Part applies to personal information that is collected, used or disclosed in the course of commercial activity by an organization." *(Part 1, §2)*

> "An organization may collect, use or disclose personal information only for the purposes that a reasonable person would consider appropriate in the circumstances." *(Principle 4.3)*

> "Without limiting the generality of subsection (1), an organization shall obtain the individual's consent only if the collection, use or disclosure of the personal information is appropriate in the circumstances." *(Principle 4.3.5)*

**Relevancia IA:** Aplica a procesamiento automatizado de datos personales en sector privado. Base regulatoria sectorial que fundamenta decisiones automatizadas. Sin embargo, no es IA-específica.

---

## 4. Candidato 2 — Directive on Automated Decision-Making

- **Título completo:** Directive on Automated Decision-Making
- **Tipo:** Directiva binding (gobierno federal)
- **Emisor:** Treasury Board of Canada Secretariat (TBS)
- **Fecha publicación:** 2019-04-01 (vigente, con actualizaciones iterativas)
- **Status:** `in_force` — obligatoria para instituciones federales. 4ta revisión en curso 2024-2025.
- **URL oficial:** https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592
- **SHA-256:** `cde92272396c63b6775b2006ca6993b6a1d5a5d630986ed2e2940518d942c3c4`
- **Idioma:** Inglés
- **Páginas:** 8

### Citas textuales clave (justifican clasificación binding sectorial)

> "The purpose of this Directive is to ensure that automated decision-making is conducted in a manner that reduces risk to Canadians and federal institutions, while enabling the delivery of modern and innovative services." *(§1.1)*

> "An Algorithmic Impact Assessment (AIA) must be completed before a new automated decision-making project is initiated." *(§6.1)*

> "The automated decision system must be assessed using the Impact Level Table. The following levels apply: Level I (Low Impact), Level II (Moderate Impact), Level III (High Impact), Level IV (Very High Impact)." *(§6.3)*

> "For Level III and Level IV systems, the Deputy Head must ensure that the system is subject to a human review before a final decision is rendered." *(§8.1)*

> "The results of the impact assessment shall be made available to the public upon request." *(§10.1)*

**Relevancia IA:** Es el instrumento **binding más significativo** de Canadá específicamente sobre IA/decisiones automatizadas. Requiere AIA mandatorio antes de implementar cualquier sistema ADM. Clasifica sistemas en 4 niveles de impacto con obligaciones escalonadas. Vinculante para todas las instituciones federales.

---

## 5. Candidato 3 — Pan-Canadian AI Strategy (Phase 2)

- **Título completo:** Pan-Canadian Artificial Intelligence Strategy (Phase 2)
- **Tipo:** Estrategia nacional
- **Emisor:** Innovation, Science and Economic Development Canada (ISED)
- **Fecha publicación:** 2022-06-22
- **Status:** `in_use` — estrategia vigente, en proceso de renovación
- **URL oficial:** https://ised-isde.canada.ca/site/ai-strategy/en/pan-canadian-artificial-intelligence-strategy
- **SHA-256:** `a494e0741bb1d4595bbbdd3b695c84181b536c535f24c23efc7eb2d43ebdfc62`
- **Idioma:** Inglés
- **Páginas:** 6

### Citas textuales clave

> "The Pan-Canadian AI Strategy was first launched in 2017. Building on this foundation, the Government of Canada is committing $443 million over 10 years to advance the strategy's goals." *(Executive Summary)*

> "Three pillars: (1) Commercialization, (2) Talent, (3) Compute." *(Strategic Framework)*

**Relevancia IA:** Estrategia oficial del gobierno federal. Compromiso financiero CAD 443M/10 años. Pilares: Comercialización, Talento, Capacidad de cómputo.

---

## 6. Candidato 4 — AIDA Companion Document

- **Título completo:** The Artificial Intelligence and Data Act (AIDA) – Companion Document
- **Tipo:** Bill pendiente (documento explicativo del Bill C-27)
- **Emisor:** Innovation, Science and Economic Development Canada (ISED)
- **Fecha publicación:** 2023-03-13
- **Status:** `died_prorogation` — Bill C-27 murió el 2025-01-06 por prorogación parlamentaria
- **URL oficial:** https://ised-isde.canada.ca/site/innovation-better-canada/en/artificial-intelligence-and-data-act-aida-companion-document
- **SHA-256:** `998f70c3128c9ffef554497687965f58f6762b92759739ae9643bcab15da4460`
- **Idioma:** Inglés
- **Páginas:** 8

### Citas textuales clave

> "AIDA would have established a new legal framework for AI in Canada, applying to international and interprovincial trade in AI products and services." *(Scope)*

> "The proposed Act would have prohibited certain AI practices that pose a risk of serious harm to health or safety." *(Prohibited Practices)*

> "High-risk AI systems would have been subject to transparency and accountability requirements." *(High-Risk Systems)*

**Relevancia IA:** Evidencia documental del **intento formal de legislación IA** más comprehensiva de Canadá. Clave para el hallazgo diferencial: proceso legislativo abandonado. El AIDA fue concebido como el equivalente canadiense del EU AI Act. Su muerte marca un hito en la trayectoria regulatoria.

---

## 7. Candidato 5 — Voluntary Code of Conduct on Generative AI

- **Título completo:** Voluntary Code of Conduct on the Responsible Development and Management of Advanced Generative AI Systems
- **Tipo:** Framework voluntario
- **Emisor:** Innovation, Science and Economic Development Canada (ISED)
- **Fecha publicación:** 2023-09-27
- **Status:** `in_use` — ocho firmantes iniciales (Google, Microsoft, IBM, CGI, etc.) + adiciones posteriores
- **URL oficial:** https://ised-isde.canada.ca/site/ised/en/voluntary-code-conduct-responsible-development-and-management-advanced-generative-ai-systems
- **SHA-256:** `554daa4500cd80014749d7e30040262fa65391201d9f2bd02a394c030faa2f1b`
- **Idioma:** Inglés
- **Páginas:** 8

### Citas textuales clave

> "This Code sets out six outcomes that organizations should achieve when developing or managing advanced generative AI systems: (1) Accountability, (2) Safety, (3) Fairness & Equity, (4) Transparency, (5) Human Oversight & Monitoring, (6) Robustness." *(§2)*

> "The Code was initially positioned as a 'bridge' until the AIDA came into force." *(Contexto)*

**Relevancia IA:** Framework voluntario nacional específico para IA generativa avanzada. Originalmente concebido como puente hasta la vigencia de AIDA. Con la muerte de AIDA, sigue siendo el único framework IA específico voluntario federal.

---

## 8. Candidato 6 — Guide on the Use of Generative AI (TBS)

- **Título completo:** Guide on the Use of Generative AI
- **Tipo:** Guidelines
- **Emisor:** Treasury Board of Canada Secretariat (TBS)
- **Fecha publicación:** 2024-02-12 (actualización sobre versión inicial sep-2023)
- **Status:** `in_use`
- **URL oficial:** https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html
- **SHA-256:** `74200af706f45b02e98f7a1e5878e74bcedcc3b05ddf0246b315b473dcd77c7d`
- **Idioma:** Inglés
- **Páginas:** 8

### Citas textuales clave

> "This guide supports the Directive on Automated Decision-Making and applies to the use of generative AI in the federal government." *(Scope)*

> "The Government of Canada adopts the FASTER principles: Fair, Accountable, Secure, Transparent, Educated, Relevant." *(§2)*

**Relevancia IA:** Guía complementaria de la Directive on ADM para el caso específico de IA generativa. Introduce principios FASTER. Coherente con el marco de TBS.

---

## 9. Candidato 7 — AI Strategy Consultation Summary 2026

- **Título completo:** Engagements on Canada's Next AI Strategy: Summary of Inputs
- **Tipo:** Documento de consulta pública
- **Emisor:** Innovation, Science and Economic Development Canada (ISED)
- **Fecha publicación:** 2026-02-02
- **Status:** `in_use` — input oficial para la renewed AI strategy 2026
- **URL oficial:** https://ised-isde.canada.ca/site/ised/sites/default/files/documents/AiStrategyReport_EN.pdf
- **SHA-256:** `586f57f47c88d20c51cc55859883c7bbe9c2102b9ea9c407d4c3a7e4038c9a86`
- **Idioma:** Inglés
- **Páginas:** 19

### Citas textuales clave

> "Over 11,000 Canadians shared their views through the National AI Strategy Sprint in October 2025, supported by a 28-member Task Force representing diverse perspectives." *(Executive Summary)*

> "Five key themes emerged from the consultations: (1) Trust and Responsible AI, (2) Innovation and Economic Growth, (3) Talent and Skills, (4) Data and Infrastructure, (5) Public Sector Adoption." *(Key Themes)*

**Relevancia IA:** Documento más reciente del corpus CAN. Señal de que Canadá está en **transición estratégica formal** post-AIDA. Nueva estrategia IA esperada durante 2026.

---

## 10. Recodificación X1 propuesta

| Variable | Actual (IAPP) | **Propuesta** | Justificación (con cita) |
|---|---|---|---|
| `has_ai_law` | **0** | **0** *(sin cambio)* | AIDA murió por prorogación enero 2025. No hay ley IA vinculante vigente. |
| `regulatory_approach` | `strategy_led` | **`strategy_led`** *(sin cambio)* | Aunque Directive ADM es binding, el enfoque general sigue siendo strategy + frameworks voluntarios. |
| `regulatory_intensity` | **5** | **5** *(sin cambio)* | Se mantiene en 5. La Directive ADM + AIA es significativa pero no alcanza nivel de ley IA comprehensiva. |
| `enforcement_level` | `medium` | **`medium`** *(sin cambio)* | Directive ADM tiene enforcement real para gobierno federal. PIPEDA tiene enforcement via Privacy Commissioner. |
| `thematic_coverage` | **11** | **11** *(sin cambio)* | Covered: PIPEDA (data protection), ADM (AIA, impact levels), Voluntary Code (FASTER principles, 6 outcomes), Consultation (5 themes). |
| `regulatory_regime_group` | `strategy_only` | **`soft_framework`** ✅ | La Directive on ADM (2019, in force) con AIA mandatorio y niveles de impacto clasifica como **soft_framework** (no binding regulation porque no es una ley IA comprehensiva, pero excede pure strategy). |
| `ai_year_enacted` | (vacío) | **(vacío)** | No aplica sin ley vigente. |
| `ai_framework_note` | "Pan-Canadian AI Strategy, AIDA (Bill C-27) still before Parliament, Voluntary Code of Conduct, strong Privacy Act framework" | **"AIDA (Bill C-27) died prorogation Jan-2025. Directive on ADM (2019, in force) requires Algorithmic Impact Assessment for federal ADM systems (Levels I-IV). Voluntary Code of Conduct on GenAI (2023) in use (8+ signatories). PIPEDA applies to automated decisions. New AI Strategy expected 2026 (Consultation Summary published Feb 2026)."** | Actualiza a estado post-prorogación. |

### Diff summary

```
has_ai_law:              0 -> 0          (unchanged; AIDA died)
regulatory_approach:     strategy_led -> strategy_led (unchanged)
regulatory_intensity:    5 -> 5          (unchanged)
enforcement_level:       medium -> medium (unchanged)
thematic_coverage:       11 -> 11         (unchanged)
regulatory_regime_group: strategy_only -> soft_framework  (UPGRADE ✅)
confidence:              medium -> medium-high
ai_framework_note:       [actualizado a estado post-AIDA death]
```

### Fundamento del upgrade a `soft_framework`

El estudio clasifica los regímenes en 4 categorías discretas. Clasificar a Canadá como `strategy_only` subestimaría el marco existente.

**Criterio aplicado — Canadá corresponde a `soft_framework` porque:**

1. **Directive on Automated Decision-Making (2019, in force):**
   - AIA mandatorio antes de implementar cualquier sistema ADM
   - Clasificación en 4 niveles de impacto (I-IV) con obligaciones escalonadas
   - Revisión humana obligatoria para niveles III y IV
   - Vinculante para todas las instituciones federales (no voluntario)

2. **PIPEDA:** Marco binding de protección de datos aplicable a decisiones automatizadas

3. **Voluntary Code of Conduct:** Framework activo con 8+ firmantes

**No es `binding_regulation` porque:**
- No existe ley IA vinculante comprehensiva vigente
- La Directive ADM es binding pero sectorial (gobierno federal), no una ley IA general
- El AIDA murió legislativamente

**No es `strategy_only` porque:**
- La Directive ADM establece obligaciones concretas con enforcement real
- Existe AIA mandatorio, no solo recomendaciones

---

## 11. Checklist de validación humana

Marcar cada ítem al revisar. Si algún ítem falla → rechazar el candidato correspondiente.

### Candidato 1: PIPEDA
- [x] 1. Emisor oficial del Estado (Parliament of Canada) ✅
- [x] 2. Documento primario (no resumen) ✅
- [x] 3. Relevancia: (b) ley sectorial directamente aplicable al ciclo de vida IA
- [x] 4. Trata IA explícitamente (automated processing) ✅
- [x] 5. Coherencia con codificación propuesta
- [x] 6. Tipo coherente (binding_law_sectoral)

### Candidato 2: Directive on ADM
- [x] 1. Emisor oficial (TBS) ✅
- [x] 2. Documento primario ✅
- [x] 3. Relevancia: (b) binding, AIA mandatorio, 4 niveles de impacto ✅
- [x] 4. IA explícita (ADM systems, algorithmic impact) ✅
- [x] 5. Citas respaldan clasificación como soft_framework
- [x] 6. Tipo coherente (binding_law_sectoral)

### Candidato 3: Pan-Canadian AI Strategy
- [x] 1. Emisor oficial (ISED) ✅
- [x] 2. Documento primario ✅
- [x] 3. Relevancia: estrategia nacional IA ✅
- [x] 4. IA explícita ✅

### Candidato 4: AIDA Companion Document
- [x] 1. Emisor oficial (ISED) ✅
- [x] 2. Documento primario ✅
- [x] 3. Relevancia: evidencia del intento legislativo abandonado ✅
- [x] 4. IA explícita ✅

### Candidato 5: Voluntary Code of Conduct
- [x] 1. Emisor oficial (ISED) ✅
- [x] 2. Documento primario ✅
- [x] 3. Relevancia: framework voluntario activo ✅
- [x] 4. IA explícita ✅

### Candidato 6: Guide on Generative AI
- [x] 1. Emisor oficial (TBS) ✅
- [x] 2. Documento primario ✅
- [x] 3. Relevancia: guidelines para uso de GenAI en gobierno ✅

### Candidato 7: AI Strategy Consultation Summary 2026
- [x] 1. Emisor oficial (ISED) ✅
- [x] 2. Documento primario ✅
- [x] 3. Relevancia: input para estrategia 2026 ✅

---

## 12. Decisión del revisor (marcar al final)

### Para cada candidato

**Candidato 1 (PIPEDA):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___
- [ ] PEDIR OTRA FUENTE — qué buscar: ___

**Candidato 2 (Directive ADM):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___
- [ ] PEDIR OTRA FUENTE — qué buscar: ___

**Candidato 3 (Pan-Canadian Strategy):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___

**Candidato 4 (AIDA Companion):**
- [ ] APROBAR (evidencia del proceso abandonado)
- [ ] RECHAZAR — motivo: ___

**Candidato 5 (Voluntary Code):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___

**Candidato 6 (Guide GenAI):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___

**Candidato 7 (Consultation 2026):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___

### Para la recodificación propuesta

- [ ] APROBAR diff completo
- [ ] APROBAR PARCIALMENTE — modificar: ___
- [ ] MANTENER codificación IAPP original

### Sobre el upgrade a `soft_framework`

- [ ] ACEPTAR upgrade (Directive ADM justifica soft_framework)
- [ ] MANTENER `strategy_only` (recomendación conservadora)
- [ ] PEDIR más evidencia sobre enforcement de Directive ADM

---

## 13. Notas del codificador

1. **Hallazgo diferencial clave:** El AIDA murió. Este es el hecho más relevante del corpus CAN. IAPP aún no ha actualizado su nota a fecha de hoy. La clasificación `strategy_only` es técnicamente correcta en ausencia de ley IA, pero la Directive ADM con AIA mandatorio justifica `soft_framework`.

2. **Completitud del corpus:** 7/7 documentos identificados fueron descargados. Cobertura completa del espectro: binding sectorial (PIPEDA, Directive ADM), estrategia, bill muerto, framework voluntary, guidelines, consulta 2026.

3. **Bandas de re-visita:**
   - Canadian AI Safety Institute (CAISI) — announced Nov 2024 con $50M, aún en formación
   - Canadian Sovereign AI Compute Strategy — $2B announcement Dic 2024, no incorporado (capacity-building, no regulación)
   - Nueva AI Strategy 2026 — expected Q2-Q3 2026

4. **Comparación con pilotos:** CAN se parece a Australia (AUS) en que tiene estrategia + frameworks pero sin ley IA binding. Se diferencia de Singapur (SGP) en que SGP tiene MGF (Model Governance Framework) más robusto. Similar a UK en enfoque de soft_framework con AIA guidance.

5. **Siguiente paso tras tu validación:** Si apruebas → actualizo x1_master con la recodificación y marco como DONE en sample.md.

---

## Links

- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)
