# DEU — Hallazgo Diferencial

## 1. Tesis del hallazgo diferencial

**Alemania presenta un patrón regulatorio IA "dual" distintivo: retraso legal formal (KI-MIG bill_pending, incumpliendo el plazo AI Act de agosto 2025) compensado por adelanto administrativo (BNetzA designada de facto desde septiembre 2024 con KI-Service Desk operativo) y el corpus de guidance Capa 4 más rico del corpus EU (3 documentos BSI/BfDI específicos de IA 2024-2025). Este patrón contrasta con DNK y HUN que ya tienen leyes nacionales de implementación en vigor.**

---

## 2. Evidencia cuantitativa — densidad del corpus

| Métrica | Valor | Cálculo |
|---|---|---|
| # documentos totales | 8 | count(manifest.csv) |
| # binding (law + sectoral) | 1 | EU AI Act (KI-MIG bill_pending) |
| # bill_pending | 1 | KI-MIG |
| # soft/policy/strategy | 6 | 3 estrategias + 3 frameworks BSI/BfDI |
| Páginas totales corpus | 310 | sum(pages) |
| Páginas binding / soft | 144 / 166 | 0.87:1 |
| Primer documento (fecha) | 2020-12 | KI-Strategie 2020 |
| Último documento (fecha) | 2026-02 | KI-MIG Entwurf |
| Años cubiertos | ~5 | (2026-02 - 2020-12) |
| Gap con fecha corpus | ~2 meses | 2026-04-21 - 2026-02 |
| # docs superseded | 0 | Ningún documento reemplazado |

---

## 3. Evidencia cuantitativa — timeline y proceso

| Fecha | Hito | Detalle |
|---|---|---|
| 2020-12-01 | KI-Strategie 2020 Fortschreibung | Estrategia IA federal actualizada. 35pp, 12 campos de acción, >100 medidas. |
| 2023-11-07 | BMBF-Aktionsplan KI 2023 | Plan de acción I+D+i. 36pp, 11 campos de acción, >1.600M EUR. |
| 2024-01-23 | BSI "KI sicher nutzen" | Guía seguridad IA co-publicada con 10 agencias internacionales. 26pp. |
| 2024-07-12 | EU AI Act publication | Regulation (EU) 2024/1689. Entrada en vigor 01-08-2024. |
| 2024-09 | Designación administrativa BNetzA | Kabinett designa BNetzA como MSA central de facto. |
| 2025-01 | BfDI Handreichung KI | Guía DPA federal para autoridades sobre IA + GDPR. 46pp. |
| 2025-06-24 | BSI Kriterienkatalog generative KI | Criterios técnicos para GenAI en administración federal. 16pp. |
| 2026-02-11 | KI-MIG Regierungsentwurf | Aprobado por Kabinett. 76pp. Primera lectura Bundestag 20-3-2026. |
| 2025-08-02 | Plazo AI Act (designación MSA) | **INCUMPLIDO** — KI-MIG aún bill_pending |

**Duración:** ~5 años de evolución regulatoria.
**Emisor principal:** Bundesregierung, BMBF, BSI, BfDI, BMDS.
**Diferencial:** Patrón dual: retraso legal + adelanto administrativo.

---

## 4. Datos que FORTALECEN la tesis

- **KI-MIG bill_pending** — Ley nacional de implementación AI Act pendiente de aprobación parlamentaria. Primera lectura Bundestag 20-3-2026. Incumplimiento del plazo AI Act (2-ago-2025).

- **BNetzA MSA de facto** — Citado: "Die Bundesnetzagentur... ist zuständige Marktüberwachungsbehörde nach Artikel 70 Absatz 1 der KI-Verordnung." Designación administrativa septiembre 2024 (pre-KI-MIG). KI-Service Desk operativo.

- **KoKIVO en desarrollo** — Citado: "Bei der Bundesnetzagentur wird ein Koordinierungs- und Kompetenzzentrum für die KI-Verordnung (KoKIVO) eingerichtet."

- **Corpus Capa 4 más rico EU** — 3 documentos BSI/BfDI específicos de IA (2024-2025):
  - BSI "KI sicher nutzen" (2024): 11 recomendaciones, co-publicado con 10 agencias internacionales.
  - BfDI Handreichung KI (2025): guía GDPR/IA para autoridades federales.
  - BSI Kriterienkatalog (2025): criterios GenAI para administración federal, aspira a Mindeststandard.

- **Inversión pública** — >3.000M EUR acumulados desde 2018.

- **Infraestructura institucional** — BNetzA (regulador multi-sector), BSI (ciberseguridad), BfDI (DPA federal independiente).

---

## 5. Datos que REFUTAN la tesis (stress test honesto)

- **DNK y HUN ya tienen leyes en vigor** — DNK (2-ago-2025), HUN (1-dic-2025). DEU aún bill_pending.

- **Designación BNetzA es administrativa** — No tiene fuerza de ley; KI-MIG la formalizará. Puede revocarse.

- **KI-MIG podría no aprobarse** — Proceso legislativo en curso; sin garantía de aprobación.

- **Federalismo alemán** — Länder tienen competencias en educación, salud, policía. Regulación federal no cubre todo.

- **Corpus mayoritariamente en DE** — 6/8 documentos en alemán. Menor accesibilidad comparativa.

- **Retraso real** — Incumplimiento del plazo AI Act (2-ago-2025) es un hecho.

---

## 6. Comparación vs peer group

| País | Régimen | # docs | # binding | Tesis diferencial |
|---|---|---|---|---|
| **DEU** | **binding_regulation** | **8** | **1** | **Patrón dual: retraso legal (KI-MIG bill_pending) + adelanto administrativo (BNetzA MSA de facto)** |
| DNK | binding_regulation | 4 | 2 | Primera ley implementación AI Act en vigor (2-ago-2025) |
| HUN | binding_regulation | 4 | 2 | Ley implementación en vigor (1-dic-2025) |
| ESP | binding_regulation | 5 | 3 | AESIA operativa + sandbox |
| IRL | binding_regulation | 4 | 1 | AI Bill 2026 creando AI Office |

**Análisis:** DEU es único por:
- Retraso legal formal (KI-MIG bill_pending) vs. DNK/HUN en vigor
- Adelanto administrativo compensatorio (BNetzA MSA de facto sept. 2024)
- Corpus de guidance Capa 4 más extenso (3 docs BSI/BfDI)

**Contraste:** DEU ≈ DNK/HUN en enforcement resultado, pero con mecanismo diferente.

---

## 7. Implicancias para el estudio

| Variable X1 | Efecto potencial |
|---|---|
| `has_ai_law` | 1 (EU AI Act + KI-MIG pending) |
| `regulatory_intensity` | 10/10 (máximo) |
| `thematic_coverage` | 14/15 (máximo) |
| `enforcement_level` | `high` (formal) |
| `regulatory_regime_group` | `binding_regulation` |
| `has_dedicated_ai_authority` | 1 (BNetzA administrativa) |
| `has_specialized_ai_frameworks` | 1 (BSI × 2 + BfDI × 1) |

**Hipótesis testeable:**
- ¿Países con implementación administrativa temprana tienen mejor compliance que países con implementación legal tardía?

**Caso narrativo útil para:**
- §Discusión como "caso de implementación administrativa temprana"
- Comparación con DNK/HUN (implementación legal clásica)

---

## 8. Banderas de re-visita

| Evento | Horizonte | Trigger observable |
|---|---|---|
| Aprobación KI-MIG | 3-6m | Bundestag/Bundesrat vote |
| Enmiendas KI-MIG | 3-6m | Textos oficiales |
| BSI Mindeststandard | 6-12m | Publicación como Mindeststandard |
| KoKIVO operativo | 3-6m | bnetzagentur.de/KI |

---

## Links

- [CANDIDATES.md](CANDIDATES.md)
- [SOURCES.md](SOURCES.md)
- [manifest.csv](manifest.csv)