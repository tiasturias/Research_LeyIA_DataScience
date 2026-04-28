# TWN - Embedding Data Complet

## 1. Metadata
- **ISO3:** TWN
- **Región:** South East Asia, East Asia, and Oceania
- **OECD:** False
- **Legal Origin:** German

## 2. Regulatory Framework
- **Grupo:** strategy_only
- **Intensidad:** 5/10
- **Enfoque:** strategy_led
- **Enforcement:** medium
- **Cover:** 9/15
- **GDPR-like:** True, similarity 2

## 3. Ecosystem IA
- **AI Readiness:** 64.81/100
- **Adopción:** 28.4%
- **Inversión:** $0.9719B
- **Startups:** 42.0
- **Patentes/100k:** None

## 4. Controls
- **GDP per capita:** $None
- **GII:** None
- **Internet:** None%
- **R&D:** None%

## 5. Governance
- **Regulatory Quality:** None
- **Rule of Law:** None
- **Freedom House:** 94/100 (F)

## 6. Documentos Legales (7)
| Título | Tipo | Fecha | Pág |
|---|---|---|---|
| Artificial Intelligence Basic Act (Taiwa | binding_law_ai | 2026-01-14 | 3 |
| 人工智慧基本法 (Artificial Intelligence Basic A | binding_law_ai | 2026-01-14 | 3 |
| Personal Data Protection Act (Taiwan) | binding_law_sectoral | 2025-11-11 | 8 |
| Cyber Security Management Act (Taiwan) | binding_law_sectoral | 2018-06-06 | 7 |
| AI Taiwan Action Plan 2.0 (2023-2026) | policy_strategy | 2023-04 |  |
| Reference Guidelines for the Use of Gene | guidelines | 2023-08-31 | 5 |
| Reference Guidelines for AI Applications | guidelines | 2025-10-08 | 4 |

## 7. Análisis Diferencial
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
| 2026-01-14 | AI Basic Act promulga...