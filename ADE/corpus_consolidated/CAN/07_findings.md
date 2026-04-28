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
| 2024-02-12 | Guide on Generative AI (TBS) | Actualización, principios FASTER |
| 2025-01-06 | Prorogación parlamentaria | Bill C-27 murió; snap election llamada |
| 2025-06 | Declaración Ministro Solomon | "AIDA is off the table as drafted" |
| 2025-10 | National AI Strategy Sprint | 11,000+ participantes, Task Force 28 miembros |
| 2026-02-02 | AI Strategy Consultation Summary | Input para estrategia renovada 2026 |

**Duración consulta pública:** National AI Strategy Sprint octubre 2025 — 2 semanas (estimado; fecha exacta no especificada).

**Emisor principal:** ISED (Innovation, Science and Economic Development Canada) para estrategia y frameworks; TBS (Treasury Board) para Directive ADM y guías.

---

## 4. Datos que FORTALECEN la tesis

- **AIDA Companion Document** (§AIDA): "AIDA would have established a new legal framework for AI in Canada, applying to international and interprovincial trade in AI products and services." — Evidencia de que el gobierno sí intentó legislación comprehensiva.

- **Directive on ADM** (§6.1): "An Algorithmic Impact Assessment (AIA) must be completed before a new automated decision-making project is initiated." — Binding sectorial real, no aspiracional.

- **Directive on ADM** (§6.3): 4 niveles de impacto (I-IV) con obligaciones escalonadas y revisión humana obligatoria para niveles III-IV. Metodología estructurada.

- **Ministerio de ISED**: Mismo emisor para Pan-Canadian Strategy (2022), AIDA (2023), Voluntary Code (2023), Consultation (2026). Continuidad institucional.

- **Presupuesto**: CAD 443M comprometidos en Pan-Canadian Strategy Phase 2. Inversión pública significativa en el ecosistema.

- **Timeline 26 años**: Desde PIPEDA (2000) hasta Consultation (2026). Evolución continua del marco regulatorio.

- **7 documentos**: Densidad alta vs promedio del corpus (~4-5 docs). ecosistema maduro.

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **Directive ADM es binding**: El argumento de "sin ley IA" podría refutarse diciendo que Canadá SÍ tiene regulación binding (Directive ADM con AIA mandatorio). La tesis se sustenta en que es sectorial (gobierno federal), no comprehensiva como AI Act. *Validación: la Directive aplica solo a instituciones federales, no al sector privado directamente.*

- **Nueva estrategia 2026 podría reintroducir legislación**: La AI Strategy Consultation Summary (Feb 2026) es input para una nueva estrategia. Podría incluir pathway legislativo. *Trigger: Q2-Q3 2026 announcement.*

- **CAISI (Canadian AI Safety Institute)**: Anunciado Nov 2024 con $50M. Si se materializa como autoridad regulatoria, podría cambiar el panorama. *Flag: horizonte 12m.*

- **Provincial regulations**: Québec tiene萌萌 (Law 25), BC tiene privacy laws. El corpus solo cubre federal. *Limitación metodológica: análisis solo federal.*

---

## 6. Comparación vs peer group (clúster pro-innovation anglófono)

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| AUS | soft_framework | 7 | 1 | Retroceso explícito de mandatory guardrails (sep 2024 → dic 2025) |
| GBR | soft_framework | 6 | 2 | Abandono AI Bill + AISI como institución (2024) |
| NZL | soft_framework | 5 | 1 | Strategy tardía (jul 2025) + Algorithm Charter |
| **CAN** | **soft_framework** | **7** | **2** | **AIDA (Bill C-27) murió por prorogación enero 2025 — legislative retreat deliberado** |

**Análisis:** CAN se distingue por:
- Mayor # binding docs (2) vs AUS/NZL (1)
- Mismo # docs que AUS (7)
- Único con muerte formal de bill por prorogación (AUS fue decisión ministerial, GBR fue withdrawn)

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 0 (sin cambio) — muerto |
| `regulatory_intensity` | 5 (sin cambio significativo) — Directive ADM es sustancial pero sectorial |
| `regulatory_regime_group` | Upgrade de `strategy_only` → `soft_framework` por Directive ADM con AIA mandatorio |
| `confidence` | Sube a `medium-high` por evidencia documental sólida |

**Hipótesis testeable:** ¿Un ecosistema IA maduro sin legislación IA binding (por decisión política) tiene outcomes diferentes a ecosistemas maduros con legislación (UE) o sin legislación por inacción (NZL)?

**Caso narrativo útil para:** 
- §Discusión del paper como "caso de legislación fallida"
- Control negativo para hipótesis "regulación binding = menor inversión"
- Comparación con GBR (abandono por distinta razón) y AUS (mandatory abortado)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| Nueva AI Strategy 2026 incluye pathway legislativo | 6m | Publicación de estrategia (esperado Q2-Q3 2026) |
| Canadian AI Safety Institute operativo | 12m | Anuncio de director/ejecución de presupuesto |
| Bill IA reintroducido en Parliament | 6-12m | Búsqueda: "Bill C- AI" en parl.ca |
| Provincial legislation (Québec, BC) relevan federal | 24m | Monitoreo Laws Loon |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)
