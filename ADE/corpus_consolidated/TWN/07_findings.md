# TWN — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Taiwán promulgó el AI Basic Act (人工智慧基本法) el 14 de enero de 2026, transicionando de `soft_framework` a `binding_regulation` — primer caso del corpus piloto con ley IA horizontal vigente. Este caso constituye el contrafactual natural de Singapur: ambos países con ecosistemas IA densos (tier equivalente en cobertura), pero decisiones regulatorias opuestas: SGP rechaza ley horizontal por política explícita; TWN la promulga. La arquitectura taiwanesa es delegada: NSTC como autoridad competente + MODA implementa risk taxonomy (Art. 16) + enforcement sectorial vía PDPA/CSMA.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 7 | count(manifest.csv) |
| # binding (ley IA + ley sectorial) | 3 | AI Basic Act + PDPA + CSMA |
| # guidelines | 2 | GenAI Guidelines Exec Yuan + Critical Infra AI Guidelines |
| # strategy | 1 | AI Taiwan Action Plan 2.0 |
| Páginas totales corpus | ~30 | sum(pages) — docs cortos |
| Binding / Soft ratio | 3:2 | 1.5:1 |
| Primer documento (fecha) | 2018 | CSMA |
| Último documento (fecha) | 2026-01-14 | AI Basic Act |
| Años cubiertos | 8 | (2026-01 - 2018-06) |
| Gap con fecha corpus | ~3 meses | 2026-04-16 - 2026-01-14 |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2018-06-06 | CSMA 2018 | Cyber Security Management Act. Establece ACS (ahora parte MODA). |
| 2023-04 | AI Taiwan Action Plan 2.0 | Estrategia nacional IA. 5 pilares, NT$250B meta industria. |
| 2023-08-31 | GenAI Guidelines Exec Yuan | Guidelines sector público. Prohíbe GenAI con datos clasificados. |
| 2025-10-08 | Critical Infra AI Guidelines | Guidelines para operadores CII usando IA. |
| 2025-11-11 | PDPA última enmienda | Personal Data Protection Act. Crea PDPC. |
| 2025-12-23 | AI Basic Act aprobación | Legislative Yuan approves 3rd reading. |
| 2026-01-14 | AI Basic Act promulgación | Presidente Lai promulga. 20 artículos, entra en vigor. |

**Duración:** 8 años de evolución regulatoria.
**Emisor principal:** Legislative Yuan, Executive Yuan, NSTC, MODA.
**Diferencial:** Transición soft_framework → binding_regulation por ley IA vigente.

---

## 4. Datos que FORTALECEN la tesis

- **AI Basic Act promulgado** — 20 artículos, en vigor desde 2026-01-14. Primera ley IA horizontal de Taiwán.

- **7 principios explícitos Art. 4** — Sustainable Development, Human Autonomy, Privacy, Cybersecurity, Transparency, Fairness, Accountability.

- **Red lines Art. 5** — Prohibiciones absolutas: vida, cuerpo, libertad, propiedad, orden social, seguridad nacional, sesgo, discriminación, desinformación.

- **National AI Strategic Committee Art. 6** — Convocado por Premier del Executive Yuan. Coordina affairs IA a nivel national.

- **Risk taxonomy mandate Art. 16** — MODA debe promover "AI risk taxonomy and assessment framework interoperable with international frameworks". Enfoque risk-based explícito.

- **Arquitectura institucional compleja** — NSTC (competent authority) + MODA (implementación risk taxonomy) + PDPC (datos) + ACS/MODA (ciberseguridad).

- **2 leyes sectoriales** — PDPA 2025 (datos personales), CSMA 2018 (CII), ambas con autoridades activas.

- **Contrafactual SGP** — Mismos mimbros starting point, decisiones regulatorias opuestas.

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **AI Basic Act es ley marco** — Sin sanciones horizontales propias. Delega enforcement en autoridades sectoriales existentes. Enforcement real vía PDPA/CSMA, no vía ley IA.

- **Solo 3 meses en vigor** — AI Basic Act vigente desde 2026-01-14 (3 meses al 2026-04-16). Sin track record enforcement.

- **Traducciones no oficiales** — EN es traducción no oficial en law.moj.gov.tw. Texto autoritativo es chino tradicional.

- **No hay AI Office dedicado** — A diferencia de IRL (AI Bill creando AI Office) o ESP (AESIA), Taiwán沒有 establece agencia IA dedicada.

- **SGP sigue siendo caso comparativo válido** — Ambos ecosystems densos, pero SGP tiene mayor coverage (13 vs 12) y más iterations de frameworks.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | Tesis diferencial |
|---|---|---|---|
| **TWN** | **binding_regulation** | **7** | **Transición soft→binding por ley IA vigente (AI Basic Act 2026), contrafactual natural de SGP** |
| SGP | soft_framework | 7 | Decisión deliberada NO ley IA horizontal |
| ARE | soft_framework | 5 | Pathway hacia binding declarado |
| ISR | soft_framework | 4 | Rechazo explícito ley horizontal + obligations concretas |

**Análisis:** TWN es único por:
- Ley IA horizontal vigente (2026-01-14)
- Arquitectura institucional delegada (NSTC+MODA sectorial)
- Contrafactual directo con SGP (mismo tier, decisiones opuestas)
- Enforcement medio (delegado en autoridades sectoriales)

**Contraste:** TWN ≠ ARE (no pathway to binding — ya binding). TWN ≈ SGP en densidad, diverge en resultado.

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 1 (AI Basic Act vigente 2026-01-14) |
| `ai_year_enacted` | 2026 |
| `regulatory_intensity` | 7/10 (+2 desde IAPP 5) |
| `thematic_coverage` | 12/15 (+3 desde IAPP 9) |
| `enforcement_level` | `medium` (delegado) |
| `regulatory_regime_group` | `binding_regulation` (TRANSICIÓN) |

**Hipótesis testeable:**
- ¿La arquitectura delegada (TWN) produce outcomes de enforcement comparables a la arquitectura centralizada (IRL, ESP)?
- ¿El caso TWN vs SGP permite aislar el efecto de la decisión regulatoria (ley vs. no-ley) controlando por densidad de ecosistema?

**Caso narrativo útil para:**
- §Discusión como "contrafactual natural de SGP"
- Comparación con UE (AI Act) y Asia-Pacífico (KOR, JPN)
- Lecciones sobre arquitecturas institucionales

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| National AI Development Guidelines | 6m | Publicación NSTC (Art. 6) |
| AI Risk Taxonomy Framework | 6m | Publicación MODA (Art. 16) |
| Primeros enforcement cases IA | 12m | Decisions PDPC/ACS/MODA |
| AI Basic Act amendment | 24m | Legislative Yuan |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)