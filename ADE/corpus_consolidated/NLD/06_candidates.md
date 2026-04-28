# NLD — Inventario de documentos y propuesta de recodificación

**País:** Netherlands (ISO3: NLD)
**Región:** EU
**EU AI Act:** Sí (directamente aplicable)
**Prioridad:** P1-TOP30 (#9 Microsoft AI Diffusion Report 2025)
**Fecha:** 2026-04-19
**Codificador:** Claude Opus 4.7 (asistido)
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
- **SAPAI 2019** — plan estratégico IA original. 3 pilares (ecosistema, economía, ética/habilidades).
- **Government-wide Vision on Generative AI 2024** — visión gubernamental específica GenAI post-ChatGPT.

**Capa 3 — Instrumentos de compliance:**
- **AIIA 2.0 (2024)** — AI Impact Assessment 2.0 (IenW). Herramienta obligatoria-de-facto para proyectos IA gubernamentales.
- **IAMA 2021** (no incluido como PDF pero referenciado). Motie parlamentaria 29-03-2022 apoya uso obligatorio.
- **Algoritmeregister** (desde 2024) — registro público de algoritmos gubernamentales.

**Capa 4 — Supervisión algorítmica:**
- **AP (Autoriteit Persoonsgegevens)** con **DCA** (Department for Coordination of Algorithmic Oversight) desde 01-01-2023 — único DPA UE con departamento dedicado.

### 2.2 Autoridades competentes

- **Autoriteit Persoonsgegevens (AP):** autoridad DP y algoritmewaakhond. Publica semestralmente Rapportage Algoritmerisico's. Coordinador previsible del AI Act en NL.
- **RDI (Rijksinspectie Digitale Infrastructuur):** autoridad sectorial infraestructuras digitales.
- **Autoridades sectoriales:** DNB (banca central), AFM (mercados), ACM (competencia y consumo), NVWA (alimentos/productos).
- **NL AI Coalitie (NL AIC):** plataforma público-privada (no autoridad regulatoria).

### 2.3 Contexto estratégico

Países Bajos tiene alto nivel de compromiso institucional con gobernanza algorítmica, condicionado por el escándalo **"Toeslagenaffaire"** (affaire de las ayudas a la infancia, 2019-2021) donde el algoritmo de la Belastingdienst discriminó a familias, causando la caída del Gabinete Rutte III (enero 2021). Este episodio catalizó:
- Creación del DCA en la AP (enero 2023).
- Algoritmeregister obligatorio (2024).
- AIIA + IAMA como estándares de compliance para el sector público.

NL presenta combinación única: aplicación UE AI Act + instrumentos gubernamentales internos maduros + trauma institucional que empuja vigilancia robusta.

---

## 3. Inventario de documentos

### Documento 1 — EU AI Act
| Campo | Valor |
|---|---|
| Archivo | `NLD_EUAIAct_Reg2024_1689.pdf` · Tipo: `binding_law_ai` · Páginas: 144 |
| SHA-256 | `bba630444b3278e881066774002a1d7824308934f49ccfa203e65be43692f55e` |

Ver IRL/CANDIDATES.md §3 Doc 1. Aplicación directa en NLD.

### Documento 2 — SAPAI 2019
| Campo | Valor |
|---|---|
| Archivo | `NLD_SAPAI_2019.pdf` · Tipo: `policy_strategy` · Páginas: 64 |
| Fecha | 08-10-2019 · Status: `in_use` (parcialmente vigente; complementado por Vision GenAI 2024) |
| SHA-256 | `12340c65d1bdb4c47bc8016129ebfdaaf3ec81102eb5fc6f3b074c89906bb1ef` |

**Citas textuales relevantes:**

> "Het kabinet wil dat Nederland de kansen die kunstmatige intelligentie biedt benut. Daarom is het Strategisch Actieplan voor Artificiële Intelligentie (SAPAI) opgesteld." (Samenvatting)

> "De SAPAI rust op drie pijlers: (1) het benutten van maatschappelijke en economische kansen, (2) het creëren van de juiste randvoorwaarden en (3) het versterken van de basis."

### Documento 3 — Government-wide Vision on Generative AI (2024)
| Campo | Valor |
|---|---|
| Archivo | `NLD_GenAIVision_2024.pdf` · Tipo: `policy_strategy` · Páginas: 54 |
| Fecha | 17-01-2024 · Status: `in_use` |
| SHA-256 | `478e898cd358f032260395347b0f681e2ff2693a9fb64ca5ee95523999e5a161` |

**Citas textuales relevantes:**

> "This government-wide vision sets out how the government intends to deal with generative AI in the coming period, based on four principles: generative AI is developed and used safely; it is developed and used fairly; it serves human well-being and protects human autonomy; and it contributes to sustainability and prosperity."

> "The government pursues six action lines: (1) Collaboration: national, European and international; (2) Continuously monitor developments; (3) Shape policy and laws; (4) Build knowledge and skills; (5) Experiment responsibly within the government; (6) Apply strong oversight."

### Documento 4 — AP Toezicht op AI & Algoritmes
| Campo | Valor |
|---|---|
| Archivo | `NLD_AP_ToezichtAIAlgoritmes.pdf` · Tipo: `guidelines` · Páginas: 11 |
| Fecha | 2023 · Status: `in_force` |
| SHA-256 | `7a7690a4c20c571c98fd3deec6c8dfa53d5a681b3a4636e46c984d9e21ac5bc2` |

**Citas textuales relevantes:**

> "De Autoriteit Persoonsgegevens heeft de afgelopen jaren signalen ontvangen over de risico's van algoritmes voor de bescherming van persoonsgegevens. [...] Met ingang van 1 januari 2023 heeft de AP structureel budget gekregen om het toezicht op algoritmes en AI te versterken."

> "De AP richt hiertoe een algoritme-coördinerend toezicht op, het Department for Coordination of Algorithmic oversight (DCA)."

### Documento 5 — AIIA 2.0 (2024)
| Campo | Valor |
|---|---|
| Archivo | `NLD_AIImpactAssessment_2024.pdf` · Tipo: `guidelines` · Páginas: 43 |
| Fecha | 2024-03 · Status: `in_use` |
| SHA-256 | `641825930d518679defd944484de7abcbf5bb214b489d191c199bedcdb305416` |

**Citas textuales relevantes:**

> "The AI Impact Assessment (AIIA) is a tool for teams that are working on an AI project within the government. The AIIA guides them in analysing and documenting their AI project. This ensures the responsible use of AI."

> "Version 2.0 has been adapted to take account of (a) the definitive version of the AI Act and (b) the rise of generative AI systems. It is no longer necessary to complete both an AIIA and an IAMA, except in cases where additional assistance is needed in assessing fundamental rights."

---

## 4. Propuesta de recodificación

### 4.1 Variables principales

| Variable | Valor IAPP | Propuesta estudio | Cambio |
|---|---|---|---|
| `has_ai_law` | 1 | **1** | Sin cambio |
| `regulatory_regime` | `comprehensive` | **`binding_regulation`** | Reclasificación taxonómica |
| `regulatory_intensity` | 10 | **10** | Sin cambio |
| `thematic_coverage` | 14 | **14** | Sin cambio |
| `enforcement_level` | — | **`high`** | Adición |
| `regulatory_regime_group` | — | **`binding_regulation`** | Adición |

### 4.2 Justificación

**`binding_regulation`:** Aplicación directa AI Act + institucionalidad supervisora reforzada (DCA en AP).

**`enforcement_level: high`:**
- AP con DCA dedicado desde enero 2023 (único en UE).
- Historia de enforcement DP activa post-Toeslagenaffaire.
- Tweede Kamer políticamente sensibilizada hacia supervisión algorítmica.
- Algoritmeregister público obligatorio.

### 4.3 Variables adicionales

| Variable | Valor |
|---|---|
| `ai_law_name` | Regulation (EU) 2024/1689 (AI Act) |
| `ai_law_year` | 2024 |
| `ai_law_status` | in_force |
| `national_strategy` | 1 (SAPAI 2019 + Vision GenAI 2024) |
| `has_dedicated_ai_authority` | 0 (DCA es departamento dentro de AP, no agencia autónoma como AESIA) |
| `gdpr_or_equivalent` | 1 (GDPR + UAVG) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `comprehensive` | `binding_regulation` |
| has_ai_law | 1 | 1 ✓ |
| intensity | 10/10 | 10/10 ✓ |
| coverage | 14/15 | 14/15 ✓ |
| Enforcement | no codif. | `high` |

**Veredicto:** Codificación IAPP correcta. Diferencial NLD: DCA dentro de la AP + Algoritmeregister + AIIA/IAMA como instrumentos maduros — dan a NL un ecosistema de governance algorítmica más profundo que otros EEMM aunque sin agencia IA independiente (distinto de ESP/AESIA).

---

## 6. Limitaciones y notas

1. **IAMA no incluido como PDF.** Referenciado textualmente. Re-capturar si se confirma como instrumento obligatorio post-AI Act.
2. **Algoritmeregister es portal web.** No incluible como PDF. Citado como evidencia de governance.
3. **GDPR/UAVG no incluidas.** Razones metodológicas (IRL/SOURCES.md §5).
4. **Government-wide Monitor 2025.** Publicado 3-12-2025; informe de seguimiento. No incluido: suplemento monitorizador, no documento rector.
5. **Werkagenda Digitaliseren 2022.** Cobertura amplia no IA-específica. No incluida.

---

## 7. Resumen ejecutivo

Países Bajos presenta régimen `binding_regulation` vía AI Act + **gobernanza algorítmica gubernamental más madura de la UE**:
- Único DPA europeo con departamento específico algoritmos/IA (DCA en AP desde enero 2023).
- Algoritmeregister público obligatorio (2024) para organismos gubernamentales.
- Dos instrumentos de impact assessment institucionalizados: AIIA 2.0 (IenW, 2024) y IAMA (Min BZK / Utrecht U., 2021).
- Dos documentos rectores simultáneos: SAPAI 2019 (IA general) + Vision GenAI 2024 (específica GenAI).

Contexto explicativo: **Toeslagenaffaire** (algoritmo Belastingdienst, caída Gabinete Rutte III, enero 2021) como catalizador institucional. Combinación UE AI Act + trauma doméstico → supervisión reforzada.

Corpus: 5 documentos. 1 ley IA-específica UE vinculante + 2 estrategias nacionales + 2 guidelines (DP supervisor + impact assessment gubernamental).
