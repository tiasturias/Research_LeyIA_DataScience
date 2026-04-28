# DNK — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Dinamarca presenta el caso único de "implementación más temprana del AI Act a nivel mundial": su Lov nr. 467/2025 (ley nacional de implementación) entró en vigor el 2 de agosto de 2025, convirtiéndola en la primera ley nacional de implementación del AI Act en vigor de todo el corpus procesado, superando a Hungría (dic 2025), IRL (General Scheme pendiente) y ESP (Anteproyecto pendiente), con Digitaliseringsstyrelsen formalmente designada como autoridad de vigilancia de mercado y punto de contacto nacional.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 4 | count(manifest.csv) |
| # binding (law + sectoral) | 2 | EU AI Act + Lov nr. 467/2025 |
| # soft/policy/strategy | 2 | 2 estrategias IA |
| Páginas totales corpus | 424 | sum(pages) |
| Páginas binding / soft | 322 / 102 | 3.16:1 |
| Primer documento (fecha) | 2019-03 | National AI Strategy |
| Último documento (fecha) | 2025-05 | Lov nr. 467 |
| Años cubiertos | 6 | (2025-05 - 2019-03) |
| Gap con fecha corpus | ~11 meses | 2026-04-21 - 2025-05 |
| # docs superseded | 0 | Ningún documento reemplazado |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2019-03 | National AI Strategy | Primera estrategia nacional IA. 74pp, 24 iniciativas, DKK 60M. |
| 2024-07-12 | EU AI Act publication | Regulation (EU) 2024/1689. Entrada en vigor 01-08-2024. |
| 2024-12-02 | Strategic Approach to AI | Actualización estratégica post-AI Act. Digital Taskforce, Advisory Centre, plataforma modelos daneses. |
| 2025-05-14 | Lov nr. 467/2025 | Ley nacional de implementación AI Act. Adoptada 8-may-2025. |
| 2025-08-02 | Lov nr. 467 vigor | Entrada en vigor. Primera ley de implementación AI Act en vigor del corpus. |

**Duración:** 6 años de evolución regulatoria.
**Emisor principal:** Ministry of Finance / Ministry of Digitalisation / Folketing.
**Diferencial:** Primera ley de implementación AI Act en vigor.

---

## 4. Datos que FORTALECEN la tesis

- **Lov nr. 467/2025 — primera ley de implementación AI Act en vigor** — Citado: "Loven fastsætter supplerende bestemmelser til Europa-Parlamentets og Rådets forordning (EU) 2024/1689 af 13. juni 2024 om harmoniserede regler for kunstig intelligens (AI-forordningen)." Vigente desde 2-ago-2025.

- **Autoridades formalmente designadas** — Citado: "Digitaliseringsstyrelsen er markedsovervågningsmyndighed efter AI-forordningens artikel 70 og national kontaktpunkt efter AI-forordningens artikel 70, stk. 2."

- **Estructura institucional tripartita** — Digitaliseringsstyrelsen (MSA central), Datatilsynet (MSA datos), Domstolsstyrelsen (MSA judicial).

- **Strategic Approach 2024** — Tres iniciativas: Digital Taskforce, Advisory Centre for Responsible AI, plataforma para modelos de lenguaje daneses.

- **National AI Strategy 2019** — 24 iniciativas, DKK 60M. Tres objetivos: liderazgo responsable, IA para beneficio de todos, marco regulatorio.

- **Primacía temporal** — DNK ahead de HUN (dic 2025), IRL (General Scheme feb 2026), ESP (Anteproyecto mar 2025).

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **Lov nr. 467 es "suplementaria"** — La ley es complementaria, no reemplaza el AI Act. Dinamarca sigue dependiendo del EU AI Act directamente aplicable.

- **Documentos en danés** — Lov nr. 467 solo en DA. Menor accesibilidad que docs EN de otros países.

- **HUN también tiene ley promulgada** — Hungría promulgó Act LXXV aunque con posterioridad (dic 2025). DNK no es único en implementación.

- **Datatilsynet sin guidance AI específica** — DPA danés no tiene guidance IA como PDF al cierre del corpus.

- **Enforcement por verificar** — Ley vigente desde ago 2025 (8 meses). Sin track record.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| **DNK** | **binding_regulation** | **4** | **2** | **Primera ley implementación AI Act en vigor (2-ago-2025), ahead de HUN/IRL/ESP** |
| HUN | binding_regulation | 4 | 2 | Ley implementación (dic 2025) |
| ESP | binding_regulation | 5 | 3 | AESIA operativa + sandbox |
| IRL | binding_regulation | 4 | 1 | AI Bill 2026 |

**Análisis:** DNK es único por:
- Primera ley de implementación AI Act en vigor
- Ratio binding/soft más alto (3.16:1)
-has_dedicated_ai_authority = 1

**Contraste:** DNK ≈ HUN (ambos con leyes promulgadas) pero DNK ahead temporalmente.

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 1 (EU AI Act + Lov nr. 467) |
| `regulatory_intensity` | 10/10 (máximo) |
| `thematic_coverage` | 14/15 (máximo) |
| `enforcement_level` | `high` (formal) |
| `regulatory_regime_group` | `binding_regulation` |
| `has_dedicated_ai_authority` | 1 (Digitaliseringsstyrelsen) |

**Hipótesis testeable:**
- ¿Países con implementación más temprana tienen mejor compliance?

**Caso narrativo útil para:**
- §Discusión como "caso de implementación más temprana"
- Comparación con HUN (segundo en implementar)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| Enforcement Lov nr. 467 | 6-12m | Decisiones Digitaliseringsstyrelsen |
| Bekendtgørelse 605/2025 | 3m | retsinformation.dk |
| Datatilsynet guidance AI | 6m | datatilsynet.dk |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)