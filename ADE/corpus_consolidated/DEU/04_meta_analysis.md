# DEU - Embedding Data Complet

## 1. Metadata
- **ISO3:** DEU
- **Región:** Europe
- **OECD:** True
- **Legal Origin:** German

## 2. Regulatory Framework
- **Grupo:** binding_regulation
- **Intensidad:** 10/10
- **Enfoque:** comprehensive
- **Enforcement:** high
- **Cover:** 14/15
- **GDPR-like:** True, similarity 3

## 3. Ecosystem IA
- **AI Readiness:** 76.78/100
- **Adopción:** 28.6%
- **Inversión:** $13.2708B
- **Startups:** 394.0
- **Patentes/100k:** 1.2176

## 4. Controls
- **GDP per capita:** $73551.9348
- **GII:** 55.4554
- **Internet:** 93.5%
- **R&D:** 3.1324%

## 5. Governance
- **Regulatory Quality:** 1.457
- **Rule of Law:** 1.5512
- **Freedom House:** 93/100 (F)

## 6. Documentos Legales (8)
| Título | Tipo | Fecha | Pág |
|---|---|---|---|
| Regulation (EU) 2024/1689 of the Europea | binding_law_ai | 2024-07-12 | 144 |
| Regierungsentwurf: Gesetz zur Durchführu | bill_pending | 2026-02-11 | 76 |
| Strategie Künstliche Intelligenz der Bun | policy_strategy | 2020-12-01 | 35 |
| Artificial Intelligence Strategy of the  | policy_strategy | 2020-12-01 | 31 |
| BMBF-Aktionsplan Künstliche Intelligenz  | policy_strategy | 2023-11-07 | 36 |
| Wegweiser für den digitalen Alltag: Küns | soft_framework | 2024-01-23 | 26 |
| Handreichung KI in Behörden – Datenschut | soft_framework | 2025-01-01 | 46 |
| Kriterienkatalog des BSI zur Integration | soft_framework | 2025-06-24 | 16 |

## 7. Análisis Diferencial
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
| 2025-06-24 | BSI Kriter...