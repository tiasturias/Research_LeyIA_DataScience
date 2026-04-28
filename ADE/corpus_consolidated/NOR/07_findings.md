# NOR — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Noruega es el único país del corpus en situación de "EEA pending implementation": no es miembro de la UE sino del EEA, por lo que el EU AI Act no es directamente aplicable y requiere incorporación vía Decisión del Comité EEA + ley nacional de implementación — un proceso en curso con høringsnotat (borrador) publicado en junio 2025 y vigencia prevista para agosto 2026, lo que la convierte en el caso de transición más avanzada hacia binding regulation fuera del bloque UE, distinguible por su AI Regulatory Sandbox operativo desde 2020 (el primero de los países nórdicos) y por el retraso estructural inherente al mecanismo EEA.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 4 | count(manifest.csv) |
| # binding (law + sectoral) | 0 | Sin ley IA vinculante vigente |
| # soft/policy/strategy | 4 | 2 estrategias + bill_pending + DPA strategy |
| Páginas totales corpus | 250 | sum(pages) |
| Páginas binding / soft | 0 / 250 | N/A |
| Primer documento (fecha) | 2020 | National AI Strategy |
| Último documento (fecha) | 2025-06 | Høringsnotat KI-lov |
| Años cubiertos | 5.5 | (2025-06 - 2020) |
| Gap con fecha corpus | ~10 meses | 2026-04-21 - 2025-06 |
| # docs superseded | 0 | Ningún documento reemplazado |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2020 | AI Regulatory Sandbox | Datatilsynet lanza primer sandbox IA de los países nórdicos |
| 2020-01 | National AI Strategy | Estrategia IA nacional noruega. 5 áreas: datos, competencias, I+D, sector público, ética/legal. 67pp EN. |
| 2024-03-22 | Datatilsynet AI Strategy | Estrategia del DPA noruego sobre IA. 3 focos: personas, sociedad, empresas. 12pp NO. |
| 2024-09-26 | Digital Norway 2024-2030 | Estrategia de digitalización nacional con capítulo IA. Meta: país más digitalizado del mundo. 108pp EN. |
| 2025-06-30 | Høringsnotat KI-lov | Borrador de ley IA para implementar EU AI Act. Consulta pública 30-06-2025 a 30-09-2025. Propone Nkom como MSA. Vigencia prevista: agosto 2026. 63pp NO. |
| 2025-09-30 | Consulta cerrada | Høringsnotat consulta cerrada. Stortingsproposisjon pendiente. |
| 2026 (previsto) | KI-lov en vigor | Vigencia prevista summer 2026 vía incorporación EEA |

**Duración:** 5.5 años de evolución regulatoria.
**Emisor principal:** Ministry of Local Government and Modernisation / Digitaliseringsdepartementet / Datatilsynet.
**Diferencial:** País EEA (no UE) con proceso de incorporación en tramite.

---

## 4. Datos que FORTALECEN la tesis

- **Høringsnotat KI-lov 2025** — Borrador de ley IA para implementar EU AI Act en derecho noruego. Citado: "Formålet med høringsnotatet er å informere om innholdet i EUs forordning om kunstig intelligens og foreslå en norsk lov om kunstig intelligens som gjennomfører forordningen i norsk rett."

- **AI Regulatory Sandbox desde 2020** — Datatilsynet opera sandbox IA desde 2020, el primero de los países nórdicos. Capacidad institucional demostrada, no meramente aspiracional.

- **Datatilsynet AI Strategy 2024** — Estrategia del DPA con tres foci operativos (personas, sociedad, empresas). Marco de actuación concreta.

- **Dos estrategias nacionales** — National AI Strategy 2020 + Digital Norway 2024-2030. Segunda generación estratégica con objetivo explícito: "the most digitalised country by 2030."

- **Nkom como MSA propuesta** — høringsnotat propone a Nasjonal kommunikasjonsmyndighet como autoridad coordinatora del AI Act.

- **Proceso EEA** — Incorporación del AI Act requiere Decisión del Comité EEA + ley nacional. Retraso estructural vs. países UE.

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **Sin ley IA vigente** — `has_ai_law = 0`. Norway no tiene ley IA vinculante al cierre del corpus. *Refutador primario.* La KI-lov está en bill_pending, no in_force.

- **Dk tiene Lov nr. 467** — Dinamarca (EEA también) ya tiene ley de implementación del AI Act in_force desde febrero 2025. NOR va ~6 meses por detrás.

- **Suecia tiene estrategia más reciente** — SWE publicó estrategia integral en feb 2026 (top-10 objetivo). NOR tiene estrategia 2020 + Digital Norway 2024.

- **Høringsnotat es solo un paso** — Consulta cerrada sept 2025, Stortingsproposisjon aún pendiente. La ley puede modificarse o retrasarse.

- **Nkom no es agencia dedicada** — Es regulador de telecomunicaciones, no agencia IA dedicada. Como en AUT/BEL.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| DNK | binding_regulation | 4 | 1 | Ley implementation AI Act in_force (Lov nr. 467, feb 2025) — primer país EEA |
| **NOR** | **soft_framework** | **4** | **0** | **EEA pending: AI Act requiere incorporación EEA + ley nacional, høringsnotat 2025, sandbox desde 2020** |
| SWE | binding_regulation | 5 | 1 | Ciclo de política ágil UE (Commission → estrategia feb 2026) |
| GBR | soft_framework | 6 | 2 | No EEA/UE; abandono AI Bill + AISI |

**Análisis:** NOR es único en el bucket soft_framework por:
- Situación EEA (no UE) con proceso de incorporación en trámite
- AI Sandbox operativo desde 2020 (primero nórdico)
- høringsnotat avanzado con vigencia prevista ago 2026
- Retraso estructural vs. DNK (ya tiene ley in_force)

**Contraste clave:** NOR ≈ DNK (ambos EEA) pero DNK ahead en timeline (ley in_force vs. bill_pending).

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 0 (sin cambio — ley no vigente) |
| `regulatory_intensity` | 4/10 (sin cambio vs IAPP) |
| `thematic_coverage` | 8/15 (sin cambio) |
| `enforcement_level` | `medium` (confirmado) |
| `regulatory_regime_group` | Upgrade `strategy_only` → `soft_framework` |
| `has_dedicated_ai_authority` | 0 (Nkom propuesta, no designada) |
| `eea_not_eu` | 1 (diferencial metodológica) |

**Hipótesis testeable:**
- ¿Países EEA (NOR, DNK, ISL) con retrasos de incorporación tienen outcomes distintos a países UE con AI Act directamente aplicable?
- ¿El AI Sandbox operativo (desde 2020) tiene efecto independent sobre adopción IA?

**Caso narrativo útil para:**
- §Discusión como "caso de EEA pending implementation"
- Control para tesis "EU AI Act igual para todos" — NOR no tiene aplicación directa
- Comparación con DNK (EEA ahead), SWE (UE), GBR (no EEA)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| Stortingsproposisjon presentada | 1-3m | regjeringen.no o stortinget.no |
| KI-lov aprobada por Storting | 3-6m | Lovdata.no publicación |
| Incorporación EEA completada | 6-12m | Decisión Comité EEA publicada |
| Nkom designado MSA | 3-6m | Lovdata.no o regjeringen.no |
| KI-Norge operativa | 6-12m | Anuncio oficial o sitio web |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)