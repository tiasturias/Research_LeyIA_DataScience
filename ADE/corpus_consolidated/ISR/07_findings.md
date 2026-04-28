# ISR — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Israel presenta el caso de "soft_framework filosóficamente articulado": su AI Policy 2023 ("Responsible Innovation") es el documento más explícito del corpus en rechazar una ley IA horizontal a favor de regulación sectorial y "soft regulatory tools", posicionándolo como el equivalente mediterráneo de Singapur — sin embargo, la Privacy Protection Law con Amendment 13 (vigente agosto 2025) introduce obligaciones IA concretas (DPO obligatorio, consentimiento informado, prohibición de web scraping para training) que justifican el upgrade a soft_framework, distinguiéndolo de casos puramente strategy_only y creando un ecosistema único en la región MENA.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 4 | count(manifest.csv) |
| # binding (law + sectoral) | 1 | Privacy Protection Law + Amendment 13 |
| # soft/policy/strategy | 3 | AI Policy 2023 + 2 National AI Programs |
| Páginas totales corpus | 125 | sum(pages) |
| Páginas binding / soft | 18 / 107 | 0.17:1 |
| Primer documento (fecha) | 2023-12 | AI Policy |
| Último documento (fecha) | 2025-04 | National AI Program 2025 |
| Años cubiertos | 1.5 | (2025-04 - 2023-12) |
| Gap con fecha corpus | ~12 meses | 2026-04-21 - 2025-04 |
| # docs superseded | 0 | Ningún documento reemplazado |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2023-12 | AI Policy "Responsible Innovation" | Primera política IA nacional. 7 retos, 5 recomendaciones. Enfoque sectoral, soft law. |
| 2024 | National AI Program 2024 | Programa nacional. NIS 1B presupuesto. National AI Directorate. |
| 2025-04 | National AI Program 2025 Snapshot | Segunda fase. NIS 500M adicionales. 83pp. Roadmap 2025-2027. |
| 2025-08-14 | PPL Amendment 13 vigor | Enmienda introduce: DPO obligatorio, consentimiento IA, prohibición scraping para training. |
| 2025-04-28 | PPA Draft AI Guidance | Borrador de guía IA del Privacy Protection Authority. Solo en hebreo. |

**Duración:** 1.5 años de evolución regulatoria (más corto del corpus).
**Emisor principal:** Ministry of Innovation, Science and Technology / Innovation Authority / Privacy Protection Authority.
**Postura deliberada:** "Responsible Innovation, sectoral regulation, soft law."

---

## 4. Datos que FORTALECEN la tesis

- **AI Policy 2023 rechaza explícitamente ley IA horizontal** — Citado: "Using 'soft' regulatory tools intended to allow for an incremental development of the regulatory framework." Documento más claro de rechazo a regulación horizontal en el corpus.

- **Privacy Protection Law + Amendment 13 binding** — Introduce obligaciones IA concretas: DPO obligatorio, consentimiento informado para IA, prohibición de web scraping para training. Vigente desde agosto 2025.

- **National AI Program 2025 — 83 páginas** — Snapshot completo con NIS 500M adicionales, roadmap 2025-2027, comparativa internacional.

- **Presupuesto significativo** — NIS 1B (2024) + NIS 500M (2025 fase 2) = inversión pública sustancial en IA.

- **National AI Directorate** — Estructura institucional dedicada dentro de Innovation Authority.

- **Similar a Singapur** — Enfoque filosófico idéntico (pro-innovación, sectoral, rechazo ley horizontal). Diferencia: menor densidad de soft law.

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **PPL es ley de privacidad, no IA-específica** — La tesis de "soft_framework" se basa en una ley sectorial (privacidad), no una ley IA. Podría argumentarse que es similar a strategy_only.

- **Amendment 93 vigencia reciente** — Las obligaciones IA concretas (DPO, consentimiento, scraping) entraron en vigor apenas 8 meses antes del cierre del corpus. Efectividad por verificar.

- **Singapur tiene más frameworks** — Singapur tiene 3+ frameworks IA específicos vs. Israel con 1-2. La densidad de soft law es menor.

- **No hay sandbox IA operativo** — A diferencia de NOR (sandbox desde 2020) o UAE (DIFC Reg 10), Israel no tiene sandbox documentado.

- **La región MENA tiene casos similares** — Qatar, Emiratos tienen enfoques light-touch. Israel no es único en la región.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| SGP | soft_framework | 7 | 2 | MGF más maduro globalmente; política explícita de no promulgar ley IA horizontal |
| ARE | soft_framework | 6 | 3 | Primer Ministerio IA mundial; DIFC Reg 10 binding |
| **ISR** | **soft_framework** | **4** | **1** | **Rechazo explícito ley IA horizontal (AI Policy 2023) + PPL Amendment 13 con obligaciones IA concretas** |
| QAT | soft_framework | 6 | 1 | Marco ligero golfo |
| TWN | binding_regulation | 7 | 3 | Ley IA 2026 |

**Análisis:** ISR es único en el bucket soft_framework por:
- Documento más explícito de rechazo a ley IA horizontal
- PPL Amendment 13 con obligaciones IA concretas
- Presupuesto nacional significativo (NIS 1.5B total)
- Nacional AI Directorate como estructura dedicada

**Contraste:** ISR ≈ SGP (filosofía idéntica) pero ISR con menor densidad de soft law.

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 0 (sin cambio — sin ley IA específica) |
| `regulatory_intensity` | Upgrade 4 → 5 (+1 por Amendment 13) |
| `thematic_coverage` | Upgrade 8 → 10 (+2) |
| `enforcement_level` | `medium` (confirmado) |
| `regulatory_regime_group` | Upgrade `strategy_only` → `soft_framework` |

**Hipótesis testeable:**
- ¿Países con rechazo explícito a regulación horizontal tienen mayor adopción IA?
- ¿El Amendment 13 de PPL tendrá enforcement activo?

**Caso narrativo útil para:**
- §Discusión como "Singapur del Mediterráneo" — mismo enfoque filosófico
- Control para tesis "soft_framework sin ley sectorial binding"
- Comparación con ARE/QAT (MENA), SGP (Asia)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| PPA AI Guidance publicado | 3-6m | privacy.org.il |
| Enforcement PPL Amendment 13 | 6-12m | Decisiones PPA |
| Sandbox IA anunciado | 6-12m | Innovation Authority |
| Cambio de política IA | 12-24m | Nuevo documento estratégico |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)