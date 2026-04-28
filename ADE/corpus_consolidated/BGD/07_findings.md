# BGD — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Bangladesh transita de `strategy_only` a `soft_framework` mediante el National AI Policy 2026-2030 (Draft V2.0): marco risk-based completo (4 niveles: prohibited/high/limited/low), AIAs mandatorios, strict liability para high-risk, prohibiciones explícitas (social scoring, mass surveillance), y pathway declarado a AI Act para 2028. Es el caso de "emerging soft_framework con trajectory legislativa formal" en el corpus — comparable a GHA y MNG en el mismo cluster, pero con marco más denso y fecha de AI Act comprometidas.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 5 | count(manifest.csv) |
| # binding (ley IA) | 0 | Sin ley vigente |
| # policy_draft | 2 | NAIP V1.1, NAIP V2.0 |
| # strategy | 1 | NSAI 2020 |
| # readiness_assessment | 1 | AIRAM UNESCO/UNDP 2025 |
| Páginas totales corpus | ~55+ | NSAI 2020 (55pp) + otros |
| Primer documento (fecha) | 2020-03 | NSAI |
| Último documento (fecha) | 2026-02 | NAIP V2.0 |
| Años cubiertos | 6 | (2026-02 - 2020-03) |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2020-03 | NSAI 2020 | Primera estrategia nacional IA. 55pp. |
| 2024 | NAIP 2024 Draft | Borrador inicial. Retirado tras V1.1. |
| 2025-11 | AIRAM 2025 | Readiness Assessment co-firmado UNESCO/UNDP. |
| 2026-01 | NAIP V1.1 Draft | Primera versión pública del NAIP 2026-2030. |
| 2026-02-09 | NAIP V2.0 Draft | Versión post-consulta pública (cerró 8-feb-2026). En revisión del Steering Committee. |

**Duración:** 6 años de evolución regulatoria.
**Emisor principal:** ICT Division, Ministry of Posts, Telecommunications and Information Technology.
**Diferencial:** Transición strategy_only → soft_framework + pathway a binding.

---

## 4. Datos que FORTALECEN la tesis

- **Marco risk-based completo** — 4 niveles: prohibited (unacceptable risk), high-risk, limited-risk, low-risk. §4.1 Regulatory Framework.

- **Prohibiciones explícitas** — AI-enabled social scoring, indiscriminate biometric mass surveillance, manipulative/deceptive AI. §4.9.

- **AIAs mandatorios** — Algorithmic Impact Assessments obligatorios para sistemas IA significativos del sector público y high-risk del sector privado. §4.9.

- **Strict liability** — Para high-risk systems en healthcare, financial services, employment, justice, education, critical infrastructure. §4.11.

- **Pathway legislativo formal** — "Ministry of Law... shall initiate drafting of comprehensive Artificial Intelligence Act by 2028." §7.5.

- **Autoridad designada** — NDGA (National Digital Government Agency) con poderes de certificación, estándares técnicos, oversight AIA. §4.2.

- **Cobertura temática amplia** — Risk classification, prohibited practices, AIA, data governance, disinformation/deepfakes, liability, derechos, cooperacion internacional, sectores.

- **Momentum internacional** — AIRAM 2025 co-firmado UNESCO/UNDP.

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **Sin ley IA vigente** — has_ai_law = 0. El AI Act está programado para 2028, no vigente.

- **NAIP V2.0 es draft** — Status: `draft_under_review`. No adoptado formalmente aún.

- **Enforcement bajo** — No hay autoridad operativa, sanciones, o track record. Solo propuesto en el draft.

- **NDGA no existe formalmente** — Propuesta en el draft, no establecida.

- **GHA y MNG tienen frameworks similares** — No es único en el cluster.

- **Gap implementación** — Historical gap entre políticas y ejecución en Bangladesh.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | Tesis diferencial |
|---|---|---|---|
| **BGD** | **soft_framework** | **5** | **Transición strategy→soft_framework + marco risk-based completo + pathway AI Act 2028** |
| GHA | soft_framework | 4 | NAIS 2023-2033 + Emerging Technologies Bill |
| MNG | soft_framework | 4 | AILA co-firmado + 2 leyes sectoriales |
| SGP | soft_framework | 7 | Decisión deliberada NO ley IA horizontal |

**Análisis:** BGD es comparable a GHA/MNG en el cluster "emerging soft_framework del Sur Global", pero con:
- Marco risk-based más detallado (4 niveles vs. general)
- Pathway a AI Act explícito con fecha (2028)
- Prohibiciones específicas (social scoring, mass surveillance)
- AIAs mandatorios + strict liability

**Contraste:** BGD ≠ SGP (SGP NO tiene pathway a binding, BGD SÍ).

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 0 (sin ley vigente — AI Act 2028 programado) |
| `regulatory_intensity` | 5/10 (+3 desde IAPP 2) |
| `thematic_coverage` | 11/15 (+7 desde IAPP 4) |
| `enforcement_level` | `low` (sin ley vigente) |
| `regulatory_regime_group` | `soft_framework` (TRANSICIÓN desde strategy_only) |

**Hipótesis testeable:**
- ¿El pathway legislativo declarado (BGD 2028) predice transición futura a binding regulation?
- ¿El marco risk-based detallado en policy draft se traduce en ley posterior?

**Caso narrativo útil para:**
- §Discusión como "emerging soft_framework con trajectory legislativa"
- Comparación con GHA/MNG (cluster Sur Global)
- Lecciones sobre diseño de policy drafts

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| Adopción formal NAIP 2026-2030 | 3-6m | Publicación en gazeta oficial |
| Establecimiento NDGA | 6-12m | Decreto/Orden ministerial |
| AI Act drafting iniciado | 12m | Ministry of Law announcement |
| AI Act promulgado | 24m | Legislative milestone |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)