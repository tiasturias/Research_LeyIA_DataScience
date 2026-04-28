# AUS — Hallazgos diferenciales

**País:** Australia (ISO3: AUS)
**Fecha de análisis:** 2026-04-21
**Régimen propuesto:** soft_framework ↑ (desde IAPP strategy_led)
**Documentos base:** [CANDIDATES.md](CANDIDATES.md) · [manifest.csv](manifest.csv) · [SOURCES.md](SOURCES.md)

---

## 1. Tesis del hallazgo diferencial

Australia es **el único país del corpus que inició un proceso formal de legislación horizontal de IA — consulta pública de *mandatory guardrails* (sep 2024) — y posteriormente lo abandonó de manera explícita** en el National AI Plan 2025 (dic 2025), reemplazándolo por "updating the existing legal and regulatory framework". La secuencia propuesta → consultada → abandonada, todo documentado en instrumentos oficiales dentro del mismo período del estudio, convierte a AUS en un **cuasi-experimento observacional** sobre la pregunta central del estudio "¿regular o no regular?". Ningún otro país del corpus tiene los tres instrumentos co-presentes (propuesta explícita de ley horizontal, consulta pública cerrada, declaración formal de abandono).

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo / Fuente |
|---|---|---|
| # documentos totales | 7 | count(manifest.csv) |
| # binding (law + sectoral) | 1 | Privacy Amendment Act 2024 |
| # soft/policy/strategy | 6 | resto |
| # descargados con SHA-256 | 5 / 7 | 4 primarios + 1 vía Wayback (doc 7) |
| # con URL confirmada pero sin SHA | 2 / 7 | docs 5, 6 (industry.gov.au y finance.gov.au geo-bloquean) |
| Páginas totales corpus (medibles) | 370 | 78+30+69+87+69+37; doc 6 = N/A |
| Páginas binding / soft medibles | 87 / 283 | ratio 1 : 3.25 |
| Primer documento | 2019-11-07 | AI Ethics Framework |
| Último documento | 2025-12-02 | National AI Plan 2025 |
| Años cubiertos | 6.1 | 2019-11 → 2025-12 |
| Gap fecha último doc → análisis | ~4.6 meses | 2025-12-02 → 2026-04-21 |
| # docs superseded | 2 / 7 (29%) | AI Action Plan 2021, Mandatory Guardrails Proposals 2024 |
| Concentración de emisor (DISR) | 5 / 7 (71%) | AIEthics, AIActionPlan, MandatoryGuardrails, VAIS, NationalAIPlan |

## 3. Evidencia cuantitativa — timeline y proceso

- **2019-11-07** — AI Ethics Framework publicado (CSIRO Data61 / DISR, 8 principios voluntarios, 78pp).
- **2021-06-18** — AI Action Plan publicado (DISR, 30pp, compromiso AUD 124.1M).
- **2024-06-21** — National Framework for Assurance of AI in Government acordado en Data and Digital Ministers Meeting (DoF).
- **2024-09-05** — *Publicación simultánea* de Voluntary AI Safety Standard (69pp, 10 guardrails) y *Proposals Paper for Mandatory Guardrails* (69pp). Apertura de consulta pública.
- **2024-10-04** — Cierre de consulta pública. **Duración: 30 días** (ventana corta vs. estándar de 8 semanas en consultas británicas).
- **2024-12-10** — Privacy and Other Legislation Amendment Act 2024 recibe Royal Assent (único instrumento *binding* del corpus AUS). Schedule 1 Part 15 (ADM transparency): vigencia diferida a **2026-12-10** (2 años de transición).
- **2025-12-02** — National AI Plan 2025 publicado. Supersede AI Action Plan 2021. Abandona explícitamente mandatory guardrails.

**Continuidad institucional:** DISR es emisor dominante (71% de los docs). Sin fragmentación ministerial observable — un solo ministerio ejecuta el giro regulatorio completo, lo que refuerza la interpretación de "cambio de política intencional" vs. "conflicto intra-gobierno".

**Presupuesto público comprometido declarado en docs del corpus:**
- AUD 124.1M en AI Action Plan 2021 (ahora superseded).
- ~A$100B forecast de inversión privada en data centres, mencionado en National AI Plan 2025 (no es gasto público directo).

## 4. Datos que FORTALECEN la tesis

- **Evidencia textual directa del abandono:** National AI Plan 2025 declara en terminos explícitos (vía fuentes verificadas Bird & Bird / White & Case): *"The Government has officially abandoned its intention to introduce mandatory guardrails in favour of updating the existing legal and regulatory framework for AI."* No es interpretación — es declaración ministerial.
- **Evidencia textual directa de la propuesta original:** Proposals Paper 2024 (§Doc 3 en CANDIDATES.md) plantea *"Option A: horizontal mandatory guardrails applying to all sectors for high-risk AI. Option B: sector-specific mandatory requirements"*. No es un discussion paper académico; contiene opciones regulatorias accionables.
- **Densidad de frameworks voluntarios simultánea al abandono:** 10 guardrails en VAIS 2024 + 8 principios AI Ethics 2019 + 5 assurance cornerstones National Framework Assurance = **23 elementos voluntarios agregados**. Esto sostiene la clasificación `soft_framework` (no `strategy_only`), independientemente del abandono de la ley.
- **Único binding concurrente es sectorial, no IA-específico:** Privacy Amendment Act 2024 regula ADM *vía* privacy law (Schedule 1 Part 15), no vía AI law dedicada — coherente con el abandono de la ley horizontal.
- **Superseded ratio 29%:** dos de los siete instrumentos están explícitamente superados por otros del mismo corpus. Esto es inusual: sugiere activismo regulatorio con auto-corrección, no inercia.
- **Concentración emisor DISR = 71%:** el giro no es por rotación ministerial; el mismo aparato ejecuta la reversa.

## 5. Datos que REFUTAN la tesis (stress test)

- **Ventana de consulta corta (30 días):** podría interpretarse como consulta de baja intensidad regulatoria — no un intento serio de legislar, sino un trial balloon. Si es así, "abandono" pierde peso (nunca hubo intención real). **Mitigante:** el volumen del Proposals Paper (69pp con opciones A/B detalladas) es inconsistente con un trial balloon; 30 días es corto pero la profundidad del documento no.
- **Privacy Amendment Act 2024 vigencia diferida a dic 2026:** al cierre del análisis (abril 2026) la provisión ADM aún no está en vigor efectiva. El enforcement sobre IA sigue siendo 0 operativo. Esto debilita `enforcement_level=medium`.
- **Australian AI Safety Institute anunciado pero no operativo:** `has_dedicated_ai_authority=0` es provisional. Si se formaliza en 2026, AUS se acerca más al modelo GBR (AISI como institución visible) que al puramente soft.
- **Peer-group con misma trayectoria:** GBR también abandonó un AI Bill. Si GBR abandonó, entonces "ser único en abandono" requiere matiz: AUS es único en **documentar el abandono en un doc oficial del mismo corpus**, pero el fenómeno no lo es. **Mitigante:** GBR nunca publicó un proposals paper con opciones horizontales listadas como AUS — el abandono británico es más silencioso.
- **National AI Plan 2025 podría revisarse:** es el doc más reciente del corpus; cualquier cambio de gobierno o evento externo (incidente IA) puede revertir la reversa. Horizonte de resiliencia: 12-24 meses.

## 6. Comparación vs peer group (pro-innovation anglófono)

| País | Régimen | # docs | # binding | Páginas totales | Tesis distintiva (1 línea) |
|---|---|---|---|---|---|
| AUS | soft_framework | 7 | 1 | 370 | Retroceso formal y documentado de mandatory guardrails (sep 2024 → dic 2025) |
| GBR | soft_framework | 6 | 2 | ~865 | AI Bill abandonado silenciosamente + AISI como institución consolidada |
| NZL | soft_framework | 5 | 1 | ~270 | Strategy tardía (jul 2025) + Algorithm Charter gubernamental pionero (2020) |
| CAN | pendiente | — | — | — | (aún no procesado; Bill C-27/AIDA murió con elecciones 2025) |

**Observación:** los 3 del clúster comparten régimen `soft_framework` pero se diferencian por **modo de abandono** de la ley IA horizontal: AUS (explícito y documentado), GBR (silencioso + institución AISI), NZL (nunca intentó ley horizontal). AUS es el caso más legible documentalmente.

## 7. Implicancias para el estudio

- **Variable X1 directamente afectada:** `regulatory_regime_group` (strategy_led → soft_framework), `enforcement_level=medium` (provisional, condicional a vigencia 2026-12-10 del Privacy Act ADM), `has_dedicated_ai_authority=0` (provisional, AISI anunciado).
- **Hipótesis del estudio que este caso testea:** AUS es el caso más cercano a un contrafactual observado — "¿qué pasa en el ecosistema IA cuando una democracia avanzada se plantea regular IA y decide no hacerlo?" Útil para comparar métricas X2 de ecosistema pre/post-abandono (2024 Q3 vs 2025 Q4+), si se consigue granularidad temporal adecuada.
- **Uso analítico sugerido:** incluir como caso narrativo en la sección del paper que contraste "regular vs no regular". Junto con UE (regula fuerte) y USA (no regula federalmente), AUS forma un triángulo analítico útil.

## 8. Banderas de re-visita

| Evento trigger | Horizonte | Acción |
|---|---|---|
| Australian AI Safety Institute entra en operación (nombramientos, sitio web oficial) | 6-12 meses | Revisar `has_dedicated_ai_authority` 0 → 1 |
| Schedule 1 Part 15 Privacy Amendment Act entra en vigor (2026-12-10) | 8 meses | Revisar `enforcement_level` (consolidar a medium/high) |
| Nuevo bill IA horizontal introducido en Parliament | hasta 24 meses | Revisar `has_ai_law` y re-evaluar tesis de "abandono" |
| VAIS 2024 o National Framework Assurance reemplazados por nuevas versiones | 12 meses | Actualizar manifest; re-evaluar densidad soft_framework |
| Cambio de gobierno federal que revierta el National AI Plan 2025 | incierto | Re-evaluar toda la tesis |
