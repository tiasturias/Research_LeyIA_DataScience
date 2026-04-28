# AUT — Inventario de documentos y propuesta de recodificación

**País:** Austria (ISO3: AUT)
**Región:** EU
**EU AI Act:** Sí (directamente aplicable)
**Prioridad:** P1-TOP30 (#17 Microsoft AI Diffusion Report 2025)
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
| `enforcement` | `high` |

---

## 2. Diagnóstico del ecosistema regulatorio IA

### 2.1 Estructura regulatoria

**Capa 1 — UE directamente aplicable:** EU AI Act desde 01-08-2024.

**Capa 2 — Estrategia nacional:**
- **AIM AT 2030 (2021)** — estrategia IA nacional federal. Marco agile con 91 medidas en 7 áreas. Coordinación conjunta Federal Chancellery + BMK. 82% medidas implementadas/en implementación a 2026.
- **Umsetzungsplan 2024 (nov. 2024)** — plan de implementación actualizado. 47 medidas concretas de 12 ministerios federales. Informe intermedio + expansión de la estrategia.

**Capa 3 — Supervisión DPA:**
- **DSB guidance DSGVO/KI-VO (2024)** — Datenschutzbehörde publica instrucciones sobre el paralelismo RGPD + AI Act para sectores público y privado.

**Capa 4 — Punto de contacto AI Act:**
- **RTR GmbH AI Service Office** — punto de contacto nacional para el AI Act. No es autoridad de vigilancia formal pero funciona como hub de información.

### 2.2 Autoridades competentes

- **DSB (Datenschutzbehörde):** DPA independiente. Competencia sobre IA que trate datos personales. Publicó guidance DSGVO/KI-VO (2024). Candidata a MSA sectorial del AI Act.
- **RTR GmbH (Rundfunk und Telekom Regulierungs-GmbH):** regulador sectorial telecomunicaciones/medios. Designado AI Service Office (punto de contacto) para el AI Act. Sin competencias de vigilancia de mercado formalizadas al cierre del corpus.
- **Federal Chancellery + BMK:** coordinadores de la estrategia AIM AT 2030. No autoridades regulatorias.
- **Autoridades sectoriales:** FMA (mercados financieros), AGES (alimentos/medicamentos), Arbeitsinspektorat (laboral).

### 2.3 Contexto estratégico

Austria presenta **régimen binding_regulation con buena madurez estratégica pero enforcement institucional en desarrollo**:
- AIM AT 2030 (2021) con alto nivel de implementación (82% medidas) → continuidad política probada.
- Umsetzungsplan 2024: 47 medidas activas en 12 ministerios → coordinación horizontal extensa.
- DSB activo con guidance dual (público + privado) sobre DSGVO/KI-VO.
- Sin agencia IA dedicada; RTR como punto de contacto sin competencias plenas.
- Austria incumplió plazo de designación formal de autoridades AI Act (02-08-2025) — similar a BEL.
- Diferencial respecto a BEL: estrategia IA más madura (2021, 82% implementación) y DSB con guidance específica publicada.

---

## 3. Inventario de documentos

### Documento 1 — EU AI Act
| Campo | Valor |
|---|---|
| Archivo | `AUT_EUAIAct_Reg2024_1689.pdf` · Tipo: `binding_law_ai` · Páginas: 144 |
| SHA-256 | `bba630444b3278e881066774002a1d7824308934f49ccfa203e65be43692f55e` |

Ver IRL/CANDIDATES.md §3 Doc 1. Aplicación directa en AUT.

### Documento 2 — AIM AT 2030 (2021)
| Campo | Valor |
|---|---|
| Archivo | `AUT_AIMAT2030_2021.pdf` · Tipo: `policy_strategy` · Páginas: 76 |
| Fecha | 2021 · Status: `in_use` (82% medidas implementadas a 2026) |
| SHA-256 | `ff518ee8f83fc1ff584fa9928331aca5446ac852dd3394bbfa45a9e43a18e78c` |
| Idioma | DE (R5 — resumen EN de 16pp disponible en bmimi.gv.at) |

**Citas textuales relevantes (DE):**

> "Die österreichische Bundesregierung hat die Strategie für Künstliche Intelligenz AIM AT 2030 in einem partizipativen Prozess mit Expert*innen und Stakeholdern entwickelt. Die Strategie verfolgt eine breite Nutzung von KI zum Wohle der Gesellschaft, die verantwortungsvoll auf Basis der Grund- und Menschenrechte sowie europäischer Werte und des europäischen Rechtsrahmens erfolgt."

> "Die Strategie umfasst 91 Maßnahmen in sieben Handlungsfeldern: (1) Wirtschaft und Arbeit, (2) Qualifizierung, (3) Ethik und Regulierung, (4) Forschung und Innovation, (5) Dateninfrastruktur, (6) Öffentliche Verwaltung, (7) Bildung."

### Documento 3 — Umsetzungsplan 2024
| Campo | Valor |
|---|---|
| Archivo | `AUT_KIUmsetzungsplan_2024.pdf` · Tipo: `policy_strategy` · Páginas: 109 |
| Fecha | 2024-11 · Status: `in_use` |
| SHA-256 | `32c0ad06901fe77b871ed857e11cf9704927ffbd1914d93d04e5bfe3730f894d` |
| Idioma | DE (R5) |

**Citas textuales relevantes (DE):**

> "Der Umsetzungsplan 2024 zur nationalen KI Strategie AIM AT 2030 wurde als Zwischenbericht und Erweiterung der Strategie vorgelegt. Er ergänzt und konkretisiert die KI-Strategie um neue Maßnahmen für die kurz- und mittelfristige Umsetzung."

> "Der Umsetzungsplan enthält 47 Maßnahmen bzw. KI-Projekte aus allen zwölf Bundesministerien, die in Umsetzung oder Planung sind. Darunter fallen z.B.: KI-Fokus in den Leistungsvereinbarungen 2025–27 der öffentlichen Universitäten, Gründung eines 'Österreichischen Kompetenzzentrums für Digitalen Landbau', Vorbereitung eines KI Hub Austria für Forschung und Innovation."

### Documento 4 — DSB — DSGVO/KI-VO öffentlicher Bereich (2024)
| Campo | Valor |
|---|---|
| Archivo | `AUT_DSB_DSGVO_KIVO_Oeffentlich.pdf` · Tipo: `guidelines` · Páginas: 3 |
| Fecha | 2024 · Status: `in_force` |
| SHA-256 | `dde52ebfa37fcdd42575c5a188529e4a1700701d2a5784831a7636e773a7595e` |
| Idioma | DE (R5) |

**Citas textuales relevantes (DE):**

> "Gemäß Art. 2 Abs. 7 KI-VO bleibt die DSGVO von der KI-VO unberührt. Soweit im Rahmen von KI-Systemen personenbezogene Daten verarbeitet werden, bleibt die Datenschutzbehörde zuständig. KI-VO und DSGVO gelten parallel."

> "Die Datenschutzbehörde hat die datenschutzrechtlichen Implikationen der KI-VO geprüft und entsprechende Informationen auf der DSB-Website veröffentlicht sowie ein Rundschreiben an die Verantwortlichen des öffentlichen Bereichs versendet, um auf dieses Thema aufmerksam zu machen."

---

## 4. Propuesta de recodificación

### 4.1 Variables principales

| Variable | Valor IAPP | Propuesta estudio | Cambio |
|---|---|---|---|
| `has_ai_law` | 1 | **1** | Sin cambio |
| `regulatory_regime` | `comprehensive` | **`binding_regulation`** | Reclasificación taxonómica |
| `regulatory_intensity` | 10 | **10** | Sin cambio |
| `thematic_coverage` | 14 | **14** | Sin cambio |
| `enforcement_level` | `high` (IAPP) | **`medium-high`** | Matización |
| `regulatory_regime_group` | — | **`binding_regulation`** | Adición |

### 4.2 Justificación

**`binding_regulation`:** Aplicación directa AI Act + estrategia nacional madura (AIM AT 2030, 82% implementación).

**`enforcement_level: medium-high`** — ligera matización respecto al baseline IAPP `high`:
- **Factor positivo:** AIM AT 2030 con alta tasa de implementación (82% de 91 medidas) → probada capacidad ejecutiva.
- **Factor positivo:** DSB activo con guidance DSGVO/KI-VO específica publicada (2024).
- **Factor positivo:** Umsetzungsplan 2024 con 47 medidas en 12 ministerios → coordinación horizontal.
- **Factor negativo:** Incumplió plazo 02-08-2025 para designación formal de autoridades AI Act.
- **Factor negativo:** Sin agencia IA dedicada; RTR como contact point sin competencias plenas.
- **Veredicto:** `medium-high` — entre BEL (`medium`, estrategia menos madura, incumplimiento) y NLD/ESP (`high`, institucionalidad supervisora más desarrollada). Si el esquema solo permite `medium`/`high`, usar `high` con nota.

### 4.3 Variables adicionales

| Variable | Valor |
|---|---|
| `ai_law_name` | Regulation (EU) 2024/1689 (AI Act) |
| `ai_law_year` | 2024 |
| `ai_law_status` | in_force |
| `national_strategy` | 1 (AIM AT 2030 + Umsetzungsplan 2024) |
| `has_dedicated_ai_authority` | 0 (DSB + RTR como autoridades competentes, no agencia IA dedicada) |
| `gdpr_or_equivalent` | 1 (GDPR + DSG 2018) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `comprehensive` | `binding_regulation` |
| has_ai_law | 1 | 1 ✓ |
| intensity | 10/10 | 10/10 ✓ |
| coverage | 14/15 | 14/15 ✓ |
| enforcement | `high` | `medium-high` (matización) |
| has_dedicated_ai_authority | — | 0 |

**Veredicto:** Codificación IAPP correcta. Matización `enforcement_level` a `medium-high`: AIM AT 2030 con alta ejecución es diferencial positivo vs. BEL, pero incumplimiento plazo AI Act y ausencia de agencia IA dedicada lo sitúan por debajo de NLD/ESP/IRL.

---

## 6. Limitaciones y notas

1. **Corpus en DE.** AIM AT 2030, Umsetzungsplan 2024 y DSB guidance en alemán. R5 aplica. Resumen EN (16pp) disponible para AIM AT 2030.
2. **RTR designación no formalizada.** AI Service Office funcional pero sin instrumento legal publicado con competencias plenas de vigilancia AI Act.
3. **DSB 403.** Portal dsb.gv.at bloquea curl. Wayback snapshot 20240910 válido (digest consistente).
4. **GDPR + DSG 2018 no incluidos.** Ver IRL/SOURCES.md §5.
5. **AIM AT 2030 Annex no incluido.** Medidas sectoriales complementarias; no rector independiente.

---

## 7. Resumen ejecutivo

Austria presenta régimen `binding_regulation` vía AI Act + **estrategia IA nacional de alta madurez ejecutiva**:
- AIM AT 2030 (2021): 91 medidas en 7 áreas → 82% implementadas o en curso a 2026.
- Umsetzungsplan 2024: 47 medidas nuevas de 12 ministerios → gobierno activo y coordinado.
- DSB con guidance DSGVO/KI-VO específica para sectores público y privado (2024).
- Sin agencia IA dedicada; RTR como contact point AI Act sin competencias plenas.
- Incumplió plazo designación formal autoridades AI Act (02-08-2025) — similar a BEL pero con mejor infraestructura estratégica.

`enforcement_level: medium-high` (entre BEL/medium y NLD/ESP/high). Corpus todo en DE (R5).

Corpus: 4 documentos. 1 ley IA-específica UE vinculante + 1 estrategia + 1 plan de implementación + 1 guideline DPA.
