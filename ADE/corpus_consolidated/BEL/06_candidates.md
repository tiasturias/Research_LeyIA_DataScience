# BEL — Inventario de documentos y propuesta de recodificación

**País:** Belgium (ISO3: BEL)
**Región:** EU
**EU AI Act:** Sí (directamente aplicable)
**Prioridad:** P1-TOP30 (#14 Microsoft AI Diffusion Report 2025)
**Fecha:** 2026-04-19
**Codificador:** Claude Sonnet 4.6 (asistido)
**Revisor humano:** Pendiente

---

## 1. Baseline IAPP

| Variable | Valor IAPP actual |
|---|---|
| `regulatory_regime` | `comprehensive` |
| `regulatory_intensity` | 10 |
| `thematic_coverage` | 14 |
| `has_ai_law` | 1 |

---

## 2. Diagnóstico del ecosistema regulatorio IA

### 2.1 Estructura regulatoria

**Capa 1 — UE directamente aplicable:** EU AI Act desde 01-08-2024.

**Capa 2 — Estrategia nacional:**
- **AI 4 Belgium (2019)** — primer documento estratégico IA. Coalición público-privada liderada por FPS BOSA. 7 objetivos.
- **National Convergence Plan (2022)** — plan de coordinación inter-institucional aprobado en Consejo de Ministros (28-10-2022). 9 pilares, ~70 ejes de acción.

**Capa 3 — Supervisión datos personales + IA:**
- **APD/GBA (2024)** — brochure sobre AI Systems + GDPR y dossier sobre impacto IA en privacidad. DPA belga posicionado como supervisora activa en la intersección RGPD/AI Act.

**Capa 4 — Designación MSA (en proceso):**
- **Government Declaration 31-01-2025 + coalition agreement 2025-2029:** BIPT/IBPT designado como Market Surveillance Authority AI Act. Sin instrumento formal publicado como PDF al cierre del corpus.

### 2.2 Autoridades competentes

- **BIPT/IBPT (Institut belge des services postaux et des télécommunications):** designado MSA del AI Act (Government Declaration 2025). Regulador sectorial telecomunicaciones reconvertido en autoridad IA.
- **APD/GBA (Autorité de Protection des Données / Gegevensbeschermingsautoriteit):** DPA independiente. Supervisión IA en tratamiento de datos personales. Publicó guidance AI/GDPR (sept. 2024).
- **FPS BOSA:** coordinador federal estrategia IA. Gestiona AI 4 Belgium Coalition y National Convergence Plan.
- **Autoridades sectoriales:** BNB (banca), FSMA (mercados financieros), FPS SPF Santé (salud).

### 2.3 Contexto estratégico

Bélgica presenta **régimen de implementación nacional del AI Act menos maduro** entre los EU P1-TOP30 procesados:
- Sin agencia IA nacional operativa (vs. ESP con AESIA, NLD con DCA en AP).
- Incumplimiento del plazo de designación de autoridades (02-08-2025) establecido por el AI Act.
- BIPT designado en el coalition agreement 2025 (De Wever) pero sin instrumento formal publicado.
- APD activa en guidance AI/GDPR pero sin competencias IA formalizadas legalmente.

Sin embargo, Bélgica mantiene un ecosistema de estrategia IA consolidado: AI4Belgium (2019) + Convergence Plan (2022) conforman una arquitectura de políticas coherente. La estructura federal (federal + flamenco + valón + bruselas) complica la implementación uniforme.

---

## 3. Inventario de documentos

### Documento 1 — EU AI Act
| Campo | Valor |
|---|---|
| Archivo | `BEL_EUAIAct_Reg2024_1689.pdf` · Tipo: `binding_law_ai` · Páginas: 144 |
| SHA-256 | `bba630444b3278e881066774002a1d7824308934f49ccfa203e65be43692f55e` |

Ver IRL/CANDIDATES.md §3 Doc 1. Aplicación directa en BEL.

### Documento 2 — AI 4 Belgium (2019)
| Campo | Valor |
|---|---|
| Archivo | `BEL_AI4Belgium_2019.pdf` · Tipo: `policy_strategy` · Páginas: 29 |
| Fecha | 2019-03 · Status: `in_use` (complementado por Convergence Plan 2022) |
| SHA-256 | `51b86741c68c82f0fe90ae02be70a891ebc710bc750082df28cefdeef7d2c015` |

**Citas textuales relevantes:**

> "AI 4 Belgium is a community-led approach to enable Belgian people and organizations to capture the opportunities of AI while facilitating the ongoing transition responsibly."

> "The coalition recommends: (1) Policy support on ethics, regulation, skills and competences; (2) Provide Belgian AI cartography; (3) Co-animate Belgian AI community; (4) Collect EU funding and connect EU ecosystems; (5) Propose concrete action for training in AI; (6) Contribute to the uptake of AI technologies by the industry; (7) Make new products and services based on AI technologies emerge."

### Documento 3 — National Convergence Plan (2022)
| Campo | Valor |
|---|---|
| Archivo | `BEL_ConvergencePlan_2022.pdf` · Tipo: `policy_strategy` · Páginas: 38 |
| Fecha | 2022-10-28 · Status: `in_use` |
| SHA-256 | `1733c1a11c797125b60e0d1166711e843f57f7fd4f96383dec24118fbcbf5fcc` |

**Citas textuales relevantes:**

> "The National Convergence Plan for the Development of Artificial Intelligence proposes concrete actions to make Belgium a #SmartAINation. The plan was approved by the Council of Ministers on 28 October 2022."

> "The plan is structured around 9 pillars: (1) promote ethical and responsible AI; (2) guarantee cybersecurity; (3) boost national competitiveness; (4) foster a data-driven economy; (5) integrate AI into healthcare; (6) advance sustainable mobility; (7) protect the environment; (8) enhance training and lifelong learning; (9) improve public services."

### Documento 4 — APD — AI Systems and the GDPR (2024)
| Campo | Valor |
|---|---|
| Archivo | `BEL_APD_AISystemsGDPR_2024.pdf` · Tipo: `guidelines` · Páginas: 21 |
| Fecha | 2024-09-19 · Status: `in_force` |
| SHA-256 | `fb0f2acc1e55632b14cfad3470dad0363600a042187c9852e6b01bd6270e5720` |

**Citas textuales relevantes:**

> "This brochure provides an overview of the relevant principles under the GDPR with which AI systems should align and indicates how Regulation 2024/1689 laying down harmonised rules on artificial intelligence (the AI Act) builds on these principles."

> "The Belgian DPA considers that the interaction between the GDPR and the AI Act is complex and multidimensional. Both instruments aim to protect fundamental rights, including the right to privacy and data protection, but they address different aspects of AI systems."

### Documento 5 — APD — Impact of AI on Privacy (2024)
| Campo | Valor |
|---|---|
| Archivo | `BEL_APD_AIImpactPrivacy.pdf` · Tipo: `guidelines` · Páginas: 16 |
| Fecha | 2024 · Status: `in_force` |
| SHA-256 | `4d419799f6d5205c184d5ec8e9b17682869877082a40424400d527fe2cc822ae` |

**Citas textuales relevantes:**

> "AI systems can process vast amounts of personal data, raising significant concerns for privacy and data protection. The Belgian DPA identifies six key principles that AI systems must respect under GDPR: lawfulness, fairness, transparency, purpose limitation, data minimisation, and accuracy."

> "The APD recommends that organizations conducting AI projects undertake a Data Protection Impact Assessment (DPIA) in all cases where AI systems are likely to result in a high risk to the rights and freedoms of natural persons."

---

## 4. Propuesta de recodificación

### 4.1 Variables principales

| Variable | Valor IAPP | Propuesta estudio | Cambio |
|---|---|---|---|
| `has_ai_law` | 1 | **1** | Sin cambio |
| `regulatory_regime` | `comprehensive` | **`binding_regulation`** | Reclasificación taxonómica |
| `regulatory_intensity` | 10 | **10** | Sin cambio |
| `thematic_coverage` | 14 | **14** | Sin cambio |
| `enforcement_level` | — | **`medium`** | Adición |
| `regulatory_regime_group` | — | **`binding_regulation`** | Adición |

### 4.2 Justificación

**`binding_regulation`:** Aplicación directa AI Act. Misma base que IRL/FRA/ESP/NLD. Diferencial: menor desarrollo institucional nacional.

**`enforcement_level: medium`** (vs. `high` de ESP/NLD/IRL/FRA):
- **Factor negativo:** Bélgica incumplió el plazo de designación de autoridades AI Act (02-08-2025).
- **Factor negativo:** Sin agencia IA nacional operativa (vs. AESIA/ESP, DCA en AP/NLD).
- **Factor positivo:** APD/GBA activa con dos publicaciones guidance AI/GDPR (sept. 2024).
- **Factor positivo:** BIPT designado MSA en Government Declaration 2025.
- **Factor positivo:** Dos documentos rectores de estrategia (AI4Belgium 2019 + Convergence Plan 2022).
- **Veredicto:** `medium` — ley vinculante (AI Act) con machinery institucional incompleta.

### 4.3 Variables adicionales

| Variable | Valor |
|---|---|
| `ai_law_name` | Regulation (EU) 2024/1689 (AI Act) |
| `ai_law_year` | 2024 |
| `ai_law_status` | in_force |
| `national_strategy` | 1 (AI4Belgium 2019 + Convergence Plan 2022) |
| `has_dedicated_ai_authority` | 0 (BIPT designado MSA pero no agencia IA dedicada; sin instrumento formal publicado) |
| `gdpr_or_equivalent` | 1 (GDPR + Loi du 30 juillet 2018) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `comprehensive` | `binding_regulation` |
| has_ai_law | 1 | 1 ✓ |
| intensity | 10/10 | 10/10 ✓ |
| coverage | 14/15 | 14/15 ✓ |
| has_dedicated_ai_authority | — | 0 |
| Enforcement | no codif. | `medium` |

**Veredicto:** Codificación IAPP correcta. Diferencial BEL respecto a otros EEMM EU P1: implementación nacional del AI Act más rezagada. Incumplimiento del plazo de designación de autoridades (02-08-2025). Sin agencia IA dedicada ni departamento supervisión algorítmica (vs. ESP/NLD). Structure federal compleja distribuye competencias entre nivel federal y tres regiones.

---

## 6. Limitaciones y notas

1. **BIPT designation no formalizada.** Government Declaration 31-01-2025 identifica BIPT como MSA pero sin instrumento legal publicado como PDF al cierre del corpus (2026-04-19). Re-capturar cuando se publique la legislación de implementación.
2. **Estructura federal.** Flandes, Valonia y Bruselas tienen competencias propias en algunas áreas IA. El corpus refleja solo el nivel federal; iniciativas regionales (e.g., Flandes tiene Vlaams AI Plan) no incluidas.
3. **GDPR / Loi du 30 juillet 2018 no incluidas.** Ver IRL/SOURCES.md §5.
4. **AI4Belgium 2019 via Wayback.** Portal ai4belgium.be retorna HTML en fetch directo. Snapshot Wayback 2022 válido (mismo contenido).
5. **Government Declaration 2025.** Documento political completo (90+ páginas), no IA-específico. No incluido; citado como evidencia contextual del BIPT.

---

## 7. Resumen ejecutivo

Bélgica presenta régimen `binding_regulation` vía AI Act con **implementación nacional en rezago** respecto a los otros EU P1-TOP30 procesados:
- Sin agencia IA nacional operativa (vs. AESIA/ESP, DCA en AP/NLD).
- Incumplió plazo 02-08-2025 para designación formal de autoridades AI Act.
- BIPT designado MSA en coalition agreement 2025 pero sin instrumento legal publicado.
- APD/GBA activa con guidance RGPD/IA (sept. 2024) pero sin competencias formalizadas.
- Dos documentos estratégicos consolidados: AI4Belgium (2019) + Convergence Plan (2022).
- Complejidad estructural: tres regiones + nivel federal con competencias distribuidas.

`enforcement_level: medium` — ley vinculante (AI Act) con machinery institucional incompleta.

Corpus: 5 documentos. 1 ley IA-específica UE vinculante + 2 estrategias nacionales + 2 guidelines DPA.
