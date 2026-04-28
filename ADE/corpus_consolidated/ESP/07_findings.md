# ESP — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**España presenta el régimen de implementación nacional del AI Act más desarrollado de toda la Unión Europea: única con agencia nacional de supervisión IA operativa (AESIA, A Coruña, desde septiembre 2023 — la primera agencia IA nacional de la UE), pionera en crear el primer sandbox regulatorio de IA de la UE (RD 817/2023, precedente del artículo 57 del AI Act), y con anteproyecto de ley nacional específico en tramitación (marzo 2025) que adelanta a la mayoría de Estados miembros, posicionándola como el caso paradigmático de binding regulation con máxima institucionalización.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 5 | count(manifest.csv) |
| # binding (law + sectoral) | 3 | EU AI Act + RD 729/2023 + RD 817/2023 |
| # soft/policy/strategy | 1 | Estrategia IA 2024 |
| # bill_pending | 1 | Anteproyecto Ley IA 2025 |
| Páginas totales corpus | 308 | sum(pages) |
| Páginas binding / soft | 205 / 103 | 1.99:1 |
| Primer documento (fecha) | 2023-09 | RD 729/2023 AESIA |
| Último documento (fecha) | 2025-03 | Anteproyecto Ley IA |
| Años cubiertos | 1.5 | (2025-03 - 2023-09) |
| Gap con fecha corpus | ~13 meses | 2026-04-21 - 2025-03 |
| # docs superseded | 0 | Ningún documento reemplazado |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2023-09-02 | RD 729/2023 — Estatuto AESIA | Creación de la Agencia Española de Supervisión de IA (A Coruña). Primera agencia IA nacional de la UE. |
| 2023-11-09 | RD 817/2023 — Sandbox IA | Primer sandbox regulatorio de IA de la UE. Precede al artículo 57 del AI Act. |
| 2024-05-14 | Estrategia IA 2024 | Estrategia nacional. €1.500M PRTR + €600M previos = €2.100M. 3 ejes, 8 palancas. |
| 2024-07-12 | EU AI Act publication | Regulation (EU) 2024/1689. Entrada en vigor 01-08-2024. |
| 2025-03-11 | Anteproyecto Ley IA 2025 | "Ley para el buen uso y la gobernanza de la IA". Tramitación urgente. 37 artículos. |

**Duración:** 1.5 años de evolución regulatoria.
**Emisor principal:** Ministerio de Asuntos Económicos y Transformación Digital / SEDIA.
**Diferencial:** Máxima institucionalización UE.

---

## 4. Datos que FORTALECEN la tesis

- **AESIA — primera agencia IA nacional de la UE** — Creada por RD 729/2023 (septiembre 2023), operativa desde entonces. Citado: "La Agencia tiene como fines la minimización de los riesgos significativos sobre la seguridad y salud de las personas, así como sobre sus derechos fundamentales."

- **Primer sandbox IA de la UE** — RD 817/2023 (noviembre 2023). Citado: "Establecer un entorno controlado de pruebas para el ensayo del cumplimiento de la propuesta de Reglamento IA." Vigencia 36 meses o hasta aplicación del AI Act.

- **Anteproyecto Ley IA 2025 más avanzado que IRL** — España publicó en marzo 2025, mientras IRL publicó su General Scheme en febrero 2026. España ahead en timeline.

- **Estrategia IA 2024 con €2.100M** — €1.500M del PRTR + €600M previos. 3 ejes: competitividad, excelencia, adopción responsable.

- **Régimen sancionador propio** — Anteproyecto fija sanciones de €7.5M a €35M o 2-7% facturación (equivalente al AI Act).

- **AESIA con sede en A Coruña** — Única agencia IA nacional con ubicación específica definida en ley.

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **AESIA no es exactamente como se imaginó** — Creada en 2023 bajo el marco del "propuesta de Reglamento IA" (pre-AI Act final). Necesita realineamiento con AI Act definitivo. *Refutador secundario.*

- **Anteproyecto no es ley aprobada** — Puede modificarse o retrasarse en la tramitación parlamentaria. *Refutador primario.*

- **Sandbox es temporal** — 36 meses o hasta aplicación del AI Act. Puede quedar obsoleto.

- **Ecosistema IA doméstico menor que FRA** — España no tiene Mistral AI ni Hugging Face. Dependencia de inversión pública.

- **Francia tiene AI Bill 2026** — IRL y FRA también tienen legislación nacional en desarrollo. España lidera pero no está sola.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| **ESP** | **binding_regulation** | **5** | **3** | **Única con AESIA operativa + sandbox IA + anteproyecto Ley ahead de IRL** |
| IRL | binding_regulation | 4 | 1 | AI Act + DPC Big Tech + AI Bill 2026 |
| FRA | binding_regulation | 5 | 1 | AI Act + ecosistema doméstico + CNIL |
| AUT | binding_regulation | 4 | 1 | Estrategia madura pero incumplimiento plazo |
| NLD | binding_regulation | 5 | 1 | AI Act + DCA único |

**Análisis:** ESP es único en el bucket binding_regulation por:
- Única agencia IA nacional operativa (AESIA)
- Primer sandbox IA de la UE
- Anteproyecto ahead de IRL
- 3 documentos binding vs promedio 1
- has_dedicated_ai_authority = 1

**Contraste:** ESP > IRL en institucionalización nacional (AESIA vs AI Bill pending), aunque IRL tiene jurisdicción Big Tech.

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 1 (EU AI Act + Anteproyecto) |
| `regulatory_intensity` | 10/10 (máximo) |
| `thematic_coverage` | 14/15 (máximo) |
| `enforcement_level` | `high` (AESIA + AEPD + sanciones) |
| `regulatory_regime_group` | `binding_regulation` |
| `has_dedicated_ai_authority` | **1** (AESIA operativa) |

**Hipótesis testeable:**
- ¿Países con agencia IA dedicada tienen mejor enforcement?
- ¿El sandbox temprano da ventaja competitiva?

**Caso narrativo útil para:**
- §Discusión como "caso de máxima institucionalización del AI Act en la UE"
- Control para tesis "agencia dedicada = mejor governance"
- Comparación con IRL (ambos ahead, diferente enfoque)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| Ley IA aprobada | 3-6m | BOE publicación |
| AESIA realineada al AI Act | 6m | RD modificación |
| Sandbox casos piloto | 6-12m | AESIA publicaciones |
| AESGIA expansión competencias | 12m | BOE nuevo RD |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)