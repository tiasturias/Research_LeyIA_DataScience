# HUN — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Hungría presenta el caso único en el corpus de "implementación nacional del AI Act más avanzada formalmente": es el único país que ya tiene ley nacional de implementación del AI Act promulgada y en vigor (Act LXXV of 2025, desde diciembre 2025), superando a IRL (General Scheme aún pendiente), ESP (Anteproyecto en tramitación) y BEL/AUT (sin legislación nacional), con autoridades formalmente designadas (Ministro de Desarrollo Empresarial como MSA, Consejo Húngaro de IA) y dos estrategias IA sucesivas (2020 + 2025) — aunque el contexto de tensiones UE-Orbán plantea dudas sobre la implementación efectiva.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 4 | count(manifest.csv) |
| # binding (law + sectoral) | 2 | EU AI Act + Act LXXV 2025 |
| # soft/policy/strategy | 2 | 2 estrategias IA |
| Páginas totales corpus | 539 | sum(pages) |
| Páginas binding / soft | 362 / 177 | 2.05:1 |
| Primer documento (fecha) | 2020-09 | AI Strategy 2020 |
| Último documento (fecha) | 2025-10 | Act LXXV |
| Años cubiertos | 5 | (2025-10 - 2020-09) |
| Gap con fecha corpus | ~6 meses | 2026-04-21 - 2025-10 |
| # docs superseded | 0 | Ningún documento reemplazado |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2020-09 | AI Strategy 2020-2030 | Primera estrategia nacional IA. 7 áreas. Resolución 1573/2020. |
| 2024-07-12 | EU AI Act publication | Regulation (EU) 2024/1689. Entrada en vigor 01-08-2024. |
| 2025-09-03 | AI Strategy 2025-2030 | Renovación estratégica. 6 pilares, 3 áreas prioritarias. |
| 2025-10-31 | Act LXXV of 2025 | Ley nacional de implementación AI Act. Promulgada. Magyar Közlöny 127/2025. |
| 2025-12-01 | Act LXXV vigor | Entrada en vigor de la ley de implementación. |

**Duración:** 5 años de evolución regulatoria.
**Emisor principal:** Government of Hungary / National Assembly.
**Diferencial:** Primera ley nacional de implementación AI Act promulgada.

---

## 4. Datos que FORTALECEN la tesis

- **Act LXXV of 2025 — primera ley de implementación AI Act promulgada** — Citado: "E törvény célja, hogy az Európai Unió mesterséges intelligenciáról szóló Rendelet [Reg. (EU) 2024/1689] magyarországi végrehajtásához szükséges intézményi és eljárási kereteket megállapítsa." Hungary ahead de IRL (General Scheme feb 2026) y ESP (Anteproyecto mar 2025).

- **Autoridades formalmente designadas por ley** — Citado: "A mesterséges intelligencia rendszerek piacfelügyeleti hatósága a gazdaságfejlesztési miniszter" (Ministro de Desarrollo Empresarial como MSA).

- **Consejo Húngaro de IA creado por ley** — Citado: "Létrejön a Magyar Mesterséges Intelligencia Tanács, mint az egységes végrehajtást biztosító konzultatív testület."

- **Dos estrategias IA sucesivas** — 2020-2030 y 2025-2030. Continuidad política demostrada a lo largo de 5 años.

- **AI Strategy 2025 con 6 pilares** — Investigación, infraestructura digital, educación, economía digital, sector público, marco ético/regulatorio.

- **Primacía en implementación** — Hungary es el primer país del corpus en promulgar ley nacional de implementación del AI Act.

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **Contexto político HUN-UE** — Hungary bajo procedimiento Art. 7 TEU por violaciones del estado de derecho. La implementación efectiva puede verse comprometida. *Refutador primario.*

- **Ley en húngaro** — Act LXXV y AI Strategy 2025 solo en HU (R5). Menor accesibilidad que docs EN de otros países.

- **NAIH sin guidance AI específica** — DPA húngaro no tiene guidance IA como PDF al cierre del corpus.

- **ESP y IRL también avanzan** — ESP con AESIA operativa, IRL con General Scheme. Hungary lidera formalmente pero no es único.

- **Enforcement por verificar** — La ley está en vigor desde dic 2025 (4 meses antes del cierre). No hay track record de enforcement.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| **HUN** | **binding_regulation** | **4** | **2** | **Única con ley nacional implementación AI Act promulgada (Act LXXV 2025)** |
| ESP | binding_regulation | 5 | 3 | AESIA operativa + sandbox |
| IRL | binding_regulation | 4 | 1 | AI Bill 2026 |
| AUT | binding_regulation | 4 | 1 | Estrategia madura pero incumplimiento |
| BEL | binding_regulation | 5 | 1 | Sin ley nacional |

**Análisis:** HUN es único en el bucket por:
- Primera ley nacional de implementación AI Act promulgada
- has_dedicated_ai_authority = 1 (Ministro MSA + Consejo IA)
- 2 binding laws (EU + nacional)
- Mayor ratio binding/soft (2.05:1)

**Contraste:** HUN > ESP/IRL en formalización jurídica, pero ESP tiene AESIA operativa desde 2023.

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 1 (EU AI Act + Act LXXV) |
| `regulatory_intensity` | 10/10 (máximo) |
| `thematic_coverage` | 14/15 (máximo) |
| `enforcement_level` | `high` (formal, pero efectividad por verificar) |
| `regulatory_regime_group` | `binding_regulation` |
| `has_dedicated_ai_authority` | 1 (Ministro MSA + Consejo IA) |

**Hipótesis testeable:**
- ¿Países con implementación formal avanzada tienen mejor compliance?
- ¿El contexto político afecta enforcement efectivo?

**Caso narrativo útil para:**
- §Discusión como "caso de implementación formal avanzada con dudas de enforcement"
- Control para tesis "ley promulgada = implementación efectiva"
- Comparación con ESP/IRL (otros avanzan pero sin ley promulgada)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| Enforcement Act LXXV | 6-12m | Decisiones del Ministerio MSA |
| NAIH guidance AI | 6m | naih.hu publicación |
| Evaluación UE cumplimiento | 12m | Informes Comisión Europea |
| AI Strategy 2025 implementación | 6-12m | Informes gubernamentales |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)