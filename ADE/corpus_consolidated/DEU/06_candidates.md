# DEU — Inventario de documentos y propuesta de recodificación

**País:** Germany (ISO3: DEU)
**Región:** EU
**EU AI Act:** Sí (directamente aplicable)
**Prioridad:** P1-TOP30 (#20 Microsoft AI Diffusion Report 2025)
**Fecha:** 2026-04-20
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

### 2.1 Estructura regulatoria (4 capas operativas)

**Capa 1 — UE directamente aplicable:** EU AI Act desde 01-08-2024.

**Capa 2 — Ley nacional de implementación (BILL PENDING):**
- **KI-MIG (Gesetz zur Durchführung der Verordnung (EU) 2024/1689 — KI-Marktüberwachungs- und Innovationsförderungsgesetz):** Regierungsentwurf aprobado por Kabinett 11-2-2026; primera lectura Bundestag 20-3-2026. Pendiente aprobación parlamentaria. Designaría: Bundesnetzagentur (BNetzA) como MSA principal + KoKIVO + múltiples MSAs sectoriales.

**Capa 3 — Documentos estratégicos:**
- **KI-Strategie 2020 Fortschreibung** (1-12-2020, DE + EN oficial): actualización de la estrategia IA nacional aprobada por Kabinett. 35pp (DE) / 31pp (EN). 12 campos de acción y >100 medidas.
- **BMBF-Aktionsplan KI 2023** (7-11-2023, DE): plan de acción del BMBF (I+D+i IA). 11 campos de acción, >1.600M EUR hasta 2025.

**Capa 4 — Frameworks voluntarios / guidelines:**
- **BSI "Künstliche Intelligenz sicher nutzen"** (23-01-2024, DE): guía BSI para uso seguro de IA, co-publicada con 10 agencias internacionales. 26pp.
- **BfDI Handreichung KI en Behörden** (2025, DE): guía del DPA federal para autoridades públicas sobre IA + GDPR. 46pp.
- **BSI Kriterienkatalog KI-Modelle** (24-06-2025, DE): criterios técnicos para integración de generative AI en administración federal. 16pp. Aspira a Mindeststandard.

### 2.2 Autoridades competentes

**Designación administrativa activa (pre-KI-MIG):**
- **Bundesnetzagentur (BNetzA):** designada por el Kabinett en septiembre 2024 como MSA central de Alemania bajo el AI Act. **KI-Service Desk operativo**; estructura KoKIVO en desarrollo. Designación administrativa, no aún formalizada por ley.
- **BSI (Bundesamt für Sicherheit in der Informationstechnik):** autoridad sectorial ciberseguridad/IA — publica criterios técnicos operativos.
- **BfDI (Bundesbeauftragte für den Datenschutz und die Informationsfreiheit):** DPA federal independiente. Competencia sobre IA + datos personales.

**Designación formal pendiente (KI-MIG):**
- BNetzA como MSA principal + contact point (formalización legal).
- KoKIVO como centro de coordinación creado por ley.
- Designación explícita de BSI y BfDI como MSAs sectoriales.

### 2.3 Contexto estratégico: retraso legal vs. adelanto administrativo

Alemania presenta un **patrón dual** distintivo entre los países EU del corpus:

**Retraso legal formal:**

| País | Ley nacional | Status | Vigor |
|---|---|---|---|
| DNK | Lov nr. 467/2025 | in_force | 2-8-2025 ✓ |
| HUN | Act LXXV of 2025 | in_force | 1-12-2025 ✓ |
| **DEU** | **KI-MIG Gesetzentwurf** | **bill_pending** | **pendiente** |
| IRL | General Scheme | bill_pending | pendiente |
| ESP | Anteproyecto | bill_pending | pendiente |

Alemania incumplió el plazo del AI Act para designar MSA por ley (2-8-2025). Atribuido a la reorganización de gobierno 2025 (creación del BMDS).

**Adelanto administrativo:**
- Designación **de facto** de BNetzA como MSA desde septiembre 2024 (decisión Kabinett).
- KI-Service Desk operativo desde 2025.
- Corpus de guidance Capa 4 robusto: 3 documentos BSI/BfDI específicos de IA publicados 2024-2025.
- Infraestructura institucional: BNetzA (multi-regulador), BSI (ciberseguridad), BfDI (DPA independiente).

**Implicación para codificación:** `has_dedicated_ai_authority = 1` (designación administrativa operativa aunque legalmente formalizada más tarde vía KI-MIG).

---

## 3. Inventario de documentos

### Documento 1 — EU AI Act
| Campo | Valor |
|---|---|
| Archivo | `DEU_EUAIAct_Reg2024_1689.pdf` · Tipo: `binding_law_ai` · Páginas: 144 |
| SHA-256 | `bba630444b3278e881066774002a1d7824308934f49ccfa203e65be43692f55e` |

Ver IRL/CANDIDATES.md §3 Doc 1. Aplicación directa en DEU. Complementado por designación administrativa BNetzA (Kabinett sept. 2024) y por KI-MIG (bill_pending).

### Documento 2 — KI-MIG Gesetzentwurf (bill_pending, 11-02-2026) (DE)
| Campo | Valor |
|---|---|
| Archivo | `DEU_KIMIGEntwurf_2026.pdf` · Tipo: `bill_pending` · Páginas: 76 |
| Fecha | 2026-02-11 · Status: `bill_pending` (Primera lectura Bundestag 20-3-2026) |
| SHA-256 | `acf063a3a2cdfb608af35ae930c72afd24420ea4c0c719cc83f95dae99d80e10` |
| Idioma | DE (R5) |

**Citas textuales relevantes (DE):**

> "§ 1 Aufgaben der Bundesnetzagentur (1) Die Bundesnetzagentur für Elektrizität, Gas, Telekommunikation, Post und Eisenbahnen (Bundesnetzagentur) ist zuständige Marktüberwachungsbehörde nach Artikel 70 Absatz 1 der KI-Verordnung. (2) Die Bundesnetzagentur ist nationaler Ansprechpartner nach Artikel 70 Absatz 2 der KI-Verordnung."

> "§ 4 Koordinierungs- und Kompetenzzentrum für die KI-Verordnung (KoKIVO) Bei der Bundesnetzagentur wird ein Koordinierungs- und Kompetenzzentrum für die KI-Verordnung (KoKIVO) eingerichtet. Das KoKIVO unterstützt die zuständigen Behörden bei ihren Aufgaben nach der KI-Verordnung und stellt eine einheitliche Rechtsanwendung in horizontalen Rechtsfragen sicher."

### Documento 3 — KI-Strategie 2020 Fortschreibung (DE)
| Campo | Valor |
|---|---|
| Archivo | `DEU_KIStrategie_2020.pdf` · Tipo: `policy_strategy` · Páginas: 35 |
| Fecha | 2020-12-01 · Status: `in_use` |
| SHA-256 | `0878b5d3d698732e4117c43ef64d83f268b14ce015abb5e3cd8038be6206a007` |
| Idioma | DE (R5; EN oficial companion disponible — doc. 4) |

**Citas textuales relevantes (DE):**

> "Die Bundesregierung hat die KI-Strategie im November 2018 beschlossen und sich dabei das Ziel gesetzt, Deutschland und Europa zu einem führenden KI-Standort zu machen. Mit der vorliegenden Fortschreibung aktualisiert die Bundesregierung ihre KI-Strategie..."

> "Die Bundesregierung investiert seit 2018 in erheblichem Umfang in Künstliche Intelligenz — insgesamt 3 Milliarden Euro bis 2025."

### Documento 4 — KI-Strategie 2020 Fortschreibung (EN companion)
| Campo | Valor |
|---|---|
| Archivo | `DEU_KIStrategie_2020_EN.pdf` · Tipo: `policy_strategy` · Páginas: 31 |
| Fecha | 2020-12-01 · Status: `in_use` |
| SHA-256 | `47286374355f17ea378e3d7629b5c2bcfc50df0442731b0124a0d120ee35310e` |
| Idioma | EN (traducción oficial del gobierno federal) |

**Citas textuales relevantes:**

> "With this update, the Federal Government is further developing its Artificial Intelligence Strategy and demonstrating that the strategy's measures are continuously being aligned with current AI developments. The update identifies new dynamic fields of action such as sustainability, environmental and climate protection, pandemics, and international networking."

### Documento 5 — BMBF-Aktionsplan KI 2023 (DE)
| Campo | Valor |
|---|---|
| Archivo | `DEU_KIAktionsplan_2023.pdf` · Tipo: `policy_strategy` · Páginas: 36 |
| Fecha | 2023-11-07 · Status: `in_use` |
| SHA-256 | `b8564ee4c19b02b5d56c99fcb91e0c4c1d68fe9258204f559f6453e7761c1978` |
| Idioma | DE (R5) |

**Citas textuales relevantes (DE):**

> "Mit dem BMBF-Aktionsplan Künstliche Intelligenz beschreibt das BMBF seinen Beitrag zur nationalen KI-Strategie und setzt damit neue Impulse für das deutsche KI-Ökosystem. Der Aktionsplan umfasst elf Handlungsfelder..."

> "Das BMBF stellt für Forschung, Entwicklung und Anwendung von KI bis 2025 mehr als 1,6 Milliarden Euro zur Verfügung."

### Documento 6 — BSI "KI sicher nutzen" (23-01-2024, DE)
| Campo | Valor |
|---|---|
| Archivo | `DEU_BSI_KISicherNutzen.pdf` · Tipo: `soft_framework` · Páginas: 26 |
| Fecha | 2024-01-23 · Status: `in_use` |
| SHA-256 | `1363a1e9a3777e495e81400cd9fff2fd84296d54198fd0df7fafe9569a5b92d2` |
| Idioma | DE (R5) |

**Relevancia:** Guía BSI co-publicada con agencias de seguridad de Australia, Canadá, Israel, Japón, NZ, Noruega, Singapur, Suecia, UK y USA. 11 recomendaciones de acción para uso seguro de sistemas IA. Primer framework federal específico de seguridad IA.

### Documento 7 — BfDI Handreichung KI (2025, DE)
| Campo | Valor |
|---|---|
| Archivo | `DEU_BfDI_HandreichungKI_2025.pdf` · Tipo: `soft_framework` · Páginas: 46 |
| Fecha | 2025 · Status: `in_use` |
| SHA-256 | `d9e6b1077efe228ed71440d063057014ad10de3e42ebe91bda6746ca44386245` |
| Idioma | DE (R5) |

**Relevancia:** Orientación del DPA federal independiente para autoridades públicas sobre IA con cumplimiento GDPR/BDSG. Complementa el KI-Fragenkatalog de febrero 2024. Documento clave para autoridades federales que usan IA.

### Documento 8 — BSI Kriterienkatalog generative KI (24-06-2025, DE)
| Campo | Valor |
|---|---|
| Archivo | `DEU_BSI_Kriterienkatalog_2025.pdf` · Tipo: `soft_framework` · Páginas: 16 |
| Fecha | 2025-06-24 · Status: `in_use` |
| SHA-256 | `f7fcc0e47d9d7891b398dc91aef78c4f3b72cf14c41ac19df0eef580d82a07c3` |
| Idioma | DE (R5) |

**Relevancia:** Criterios técnicos BSI para integración de generative AI en administración federal. Cubre governance (ciclo de vida) + criterios técnicos. Aspira a Mindeststandard obligatorio. Referenciado como norma emergente BSI T-25 V 1.0.

---

## 4. Propuesta de recodificación

### 4.1 Variables principales

| Variable | Valor IAPP | Propuesta estudio | Cambio |
|---|---|---|---|
| `has_ai_law` | 1 | **1** | Sin cambio |
| `regulatory_regime` | `comprehensive` | **`binding_regulation`** | Reclasificación taxonómica |
| `regulatory_intensity` | 10 | **10** | Sin cambio |
| `thematic_coverage` | 14 | **14** | Sin cambio |
| `enforcement_level` | `high` (IAPP) | **`high`** | Confirmación |
| `regulatory_regime_group` | — | **`binding_regulation`** | Adición |

### 4.2 Justificación

**`binding_regulation`:** EU AI Act directamente aplicable en DEU. Aunque la ley nacional (KI-MIG) está pendiente de aprobación parlamentaria, la regulación vinculante UE es operativa, y la designación administrativa de BNetzA (sept. 2024) cubre operativamente las funciones de MSA. El régimen es `binding_regulation`.

**`enforcement_level: high`** — confirmado vs. IAPP:
- Inversión pública >3.000M EUR en IA desde 2018 (KI-Strategie 2020).
- Infraestructura institucional de alta capacidad: BNetzA (operador regulatorio en múltiples sectores), BSI (ciberseguridad), BfDI (DPA federal).
- Designación administrativa BNetzA operativa: KI-Service Desk + KoKIVO en desarrollo.
- Corpus de guidance Capa 4 robusto: 3 documentos BSI/BfDI específicos de IA (2024-2025).
- Proceso legislativo avanzado: Gesetzentwurf KI-MIG aprobado por Kabinett, primera lectura parlamentaria completada.

**Nota de matiz:** El retraso en ley nacional formal es un hallazgo diferencial vs. DNK/HUN, pero la combinación de EU AI Act + designación administrativa BNetzA + corpus de guidance mantiene un nivel de enforcement `high`.

### 4.3 Variables adicionales

| Variable | Valor |
|---|---|
| `ai_law_name` | Regulation (EU) 2024/1689 (AI Act) + KI-MIG (bill_pending) |
| `ai_law_year` | 2024 (UE) / 2026 (nacional, pendiente) |
| `ai_law_status` | in_force (EU AI Act) / bill_pending (KI-MIG) |
| `national_strategy` | 1 (KI-Strategie 2020 Fortschreibung + KI-Aktionsplan 2023) |
| `has_dedicated_ai_authority` | **1** (BNetzA designada administrativamente sept. 2024; KI-Service Desk operativo) |
| `has_specialized_ai_frameworks` | 1 (BSI "KI sicher nutzen" + BSI Kriterienkatalog + BfDI Handreichung) |
| `gdpr_or_equivalent` | 1 (GDPR + BDSG 2018) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `comprehensive` | `binding_regulation` |
| has_ai_law | 1 | 1 ✓ |
| intensity | 10/10 | 10/10 ✓ |
| coverage | 14/15 | 14/15 ✓ |
| enforcement | `high` | `high` ✓ |
| has_dedicated_ai_authority | — | 1 (BNetzA administrativa) |
| has_specialized_ai_frameworks | — | 1 (BSI × 2 + BfDI × 1) |

**Veredicto:** Codificación IAPP correcta. Diferencial DEU: **retraso relativo en implementación nacional legal formal** (KI-MIG bill_pending vs. DNK/HUN ya en vigor), **compensado por adelanto administrativo** (BNetzA designada de facto sept. 2024) y un **corpus de guidance Capa 4 más rico** que cualquier otro país EU del corpus (3 documentos BSI/BfDI específicos de IA 2024-2025).

---

## 6. Limitaciones y notas

1. **Corpus DEU predominantemente en DE.** 6 de 8 documentos en DE (R5). Excepción: EU AI Act EN + KI-Strategie 2020 EN (traducción oficial).
2. **KI-MIG aún no aprobado.** Al cierre del corpus (abril 2026), la ley sigue en trámite parlamentario. Una vez aprobada, actualizar `ai_law_status` a `in_force`.
3. **Designación BNetzA: administrativa vs. legal.** La designación de septiembre 2024 (Kabinett) es administrativa y operativa pero no tiene fuerza de ley; KI-MIG la formalizará. Interpretación conservadora: `has_dedicated_ai_authority=1` por existencia operativa demostrada.
4. **Federalismo alemán.** Los Länder tienen competencias en algunos sectores IA (educación, salud, policía). El KI-MIG y autoridades federales operan a nivel federal; legislación de Länder puede complementar pero no está en corpus.
5. **Documentos excluidos conscientemente:**
   - KI-Strategie original 2018 (supersedida por Fortschreibung 2020).
   - BfDI KI-Fragenkatalog 2024 (complementado por Handreichung 2025 — doc. 7).
   - BfDI Handreichung KI Sicherheitsbehörden 2024 (scope sectorial estrecho).
   - DSK Orientierungshilfe KI 2024 (multijurisdiccional Bund + Länder, fuera de scope federal puro).
6. **GDPR + BDSG no incluidos.** Ver IRL/SOURCES.md §5 para exclusión metodológica.

---

## 7. Resumen ejecutivo

Alemania presenta un **patrón regulatorio IA dual distintivo** entre los países EU del corpus:

**Retraso legal formal:**
- KI-MIG (ley nacional implementación): **bill_pending** (Kabinett feb. 2026, Bundestag primera lectura mar. 2026). Retraso vs. DNK (2-8-2025) y HUN (1-12-2025).
- Plazo AI Act designación MSA (2-8-2025): incumplido por ley formal.

**Adelanto administrativo compensatorio:**
- BNetzA designada como MSA **de facto** desde septiembre 2024 (decisión Kabinett).
- KI-Service Desk operativo; estructura KoKIVO en desarrollo.
- Corpus guidance Capa 4 robusto: BSI "KI sicher nutzen" (2024), BSI Kriterienkatalog (2025), BfDI Handreichung (2025).
- Infraestructura institucional de alta capacidad: BNetzA, BSI, BfDI.
- Inversión pública acumulada: >3.000M EUR en IA desde 2018.

**Codificación:** `regulatory_regime: binding_regulation`. `enforcement_level: high`. `has_dedicated_ai_authority: 1` (basado en designación administrativa operativa). `has_specialized_ai_frameworks: 1` (3 documentos federales específicos).

**Corpus: 8 documentos.** 1 ley UE vinculante + 1 ley nacional bill_pending + 3 documentos estratégicos (KI-Strategie DE+EN + Aktionsplan) + 3 frameworks técnicos (BSI × 2 + BfDI × 1).
