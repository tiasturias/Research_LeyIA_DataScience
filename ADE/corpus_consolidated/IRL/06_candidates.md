# IRL — Inventario de documentos y propuesta de recodificación

**País:** Ireland (ISO3: IRL)
**Región:** EU
**EU AI Act:** Sí (directamente aplicable)
**Prioridad:** P1-TOP30 (#4 Microsoft AI Diffusion Report 2025)
**Fecha:** 2026-04-17
**Codificador:** Claude Opus 4.6 (asistido)
**Revisor humano:** Pendiente

---

## 1. Baseline IAPP

| Variable | Valor IAPP actual |
|---|---|
| `regulatory_regime` | `comprehensive` |
| `regulatory_intensity` | 10 |
| `thematic_coverage` | 14 |
| `has_ai_law` | 1 |
| `enforcement_level` | (no codificado explícitamente en IAPP) |

**Nota IAPP:** Ireland está clasificada como `comprehensive` (has_ai_law=1) en la base IAPP por el EU AI Act. Intensidad y cobertura máximas en el dataset. Esta codificación es correcta y consistente con el corpus recabado.

---

## 2. Diagnóstico del ecosistema regulatorio IA

### 2.1 Estructura regulatoria

Irlanda es un Estado miembro de la UE. El marco regulatorio IA se estructura en tres capas:

**Capa 1 — Derecho UE directamente aplicable:**
- **EU AI Act** (Reg. 2024/1689): ley IA-específica horizontal, directamente aplicable desde 1 agosto 2024, aplicación plena 2 agosto 2026. Sin transposición requerida. Regula prohibiciones absolutas, sistemas alto riesgo, modelos GPAI, obligaciones proveedores/deployers/importadores.

**Capa 2 — Estrategia e implementación nacional:**
- **National AI Strategy 2021** ("AI – Here for Good"): estrategia base pre-EU AI Act.
- **National AI Strategy Refresh 2024**: actualización post-EU AI Act. Posiciona a Irlanda como hub IA europeo, articula alineación con el AI Act, define pilares para competitividad.

**Capa 3 — Legislación nacional de implementación:**
- **AI Bill 2026 (General Scheme)**: bill pendiente que transpone las obligaciones nacionales del EU AI Act. Crea la AI Office of Ireland, designa 15 autoridades competentes sectoriales, establece sanciones nacionales. Operativo previsto 1 agosto 2026.

### 2.2 Autoridades competentes

- **Data Protection Commission (DPC):** Principal autoridad de supervisión IA en Irlanda bajo el EU AI Act. También autoridad GDPR. Irlanda es sede de European headquarters de Meta, Google, Apple, TikTok, Microsoft, LinkedIn — la DPC es la autoridad GDPR con mayor volumen de casos Big Tech de la UE.
- **AI Office of Ireland** (a crear por AI Bill 2026): coordinador nacional.
- **Central Bank of Ireland, HIQUA, Competition and Consumer Protection Commission:** entre las 15 autoridades sectoriales designadas en el AI Bill 2026.

### 2.3 Contexto estratégico

Irlanda es el principal hub tecnológico de la UE: sede europea de los mayores players globales IA (Google DeepMind, Meta AI, Microsoft, Amazon AWS). La DPC ejerce jurisdicción primaria GDPR sobre estas entidades bajo el mecanismo one-stop-shop. El AI Bill 2026 refuerza este rol extendiendo competencias al ámbito IA. El Refresh 2024 es explícito en el objetivo: mantener a Irlanda como "the best place in Europe to develop and deploy AI."

---

## 3. Inventario de documentos

### Documento 1 — EU Artificial Intelligence Act

| Campo | Valor |
|---|---|
| Archivo | `IRL_EUAIAct_Reg2024_1689.pdf` |
| Título oficial | Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act) |
| Emisor | European Parliament and Council of the EU |
| Tipo | `binding_law_ai` |
| Fecha publicación | 2024-07-12 (OJ L 2024/1689) |
| Entrada en vigor | 2024-08-01 |
| Aplicación plena | 2026-08-02 |
| Status | `in_force` |
| Idioma | EN |
| Páginas | 144 |
| Tamaño | 2.5 MB |
| URL primaria | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401689 |
| Descarga efectiva | Wayback Machine snapshot 20240712122436 (EUR-Lex devuelve HTTP 202/0 a curl) |
| SHA-256 | `bba630444b3278e8df2de7ee14a4a56d5dcb0b4e27c89b8afc03286c5e55df62` |

**Citas textuales relevantes:**

> "This Regulation lays down harmonised rules on the placing on the market, the putting into service and the use of artificial intelligence systems (AI systems) in the Union." (Art. 1.1)

> "This Regulation applies to providers that place on the market or put into service AI systems or place on the market general-purpose AI models in the Union, irrespective of whether those providers are established or located within the Union or in a third country." (Art. 2.1.a)

> "The following AI practices shall be prohibited: [...] the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person's consciousness [...] to materially distort a person's behaviour." (Art. 5.1.a)

> "Providers of high-risk AI systems shall [...] establish, implement, document and maintain a risk management system." (Art. 9.1)

> "Providers of general-purpose AI models shall: (a) draw up and keep up-to-date technical documentation [...]; (b) draw up, keep up-to-date and make available information and documentation to providers of AI systems [...]; (c) put in place a policy to comply with Union copyright law." (Art. 53.1)

> "Each Member State shall designate one or more national competent authorities for the purpose of supervising the application and implementation of this Regulation." (Art. 70.1)

> "For infringements of Article 5 [prohibited practices], market surveillance authorities shall impose on the provider or the deployer, as applicable, an administrative fine of up to EUR 35 000 000 or, if the offender is an undertaking, up to 7 % of its total worldwide annual turnover." (Art. 99.3)

---

### Documento 2 — National AI Strategy Refresh 2024

| Campo | Valor |
|---|---|
| Archivo | `IRL_NationalAIStrategy_Refresh2024.pdf` |
| Título oficial | AI – Here for Good: National AI Strategy Refresh 2024 |
| Emisor | Department of Enterprise, Trade and Employment (DETE) |
| Tipo | `policy_strategy` |
| Fecha publicación | 2024-10 |
| Status | `in_use` |
| Idioma | EN |
| Páginas | 31 |
| Tamaño | 1.6 MB |
| URL primaria | https://enterprise.gov.ie/en/publications/publication-files/national-ai-strategy-refresh-2024.pdf |
| Descarga efectiva | Directa (HTTP 200) |
| SHA-256 | `cb13bd4abc00518b91b7c48a3b17c8699e2e3a8d4d6a90ac4d30fdae02db7d5f` |

**Citas textuales relevantes:**

> "Ireland's ambition is to be the best place in Europe to develop and deploy AI, using AI to increase innovation and productivity, while ensuring AI is trustworthy, safe and secure." (p. 4)

> "The EU AI Act creates a harmonised legal framework for AI across Europe. Ireland, as an EU Member State, will implement the EU AI Act, leveraging our existing strengths in data protection and digital governance." (p. 18)

> "Strand 6 — Regulation & Trust: Support the effective implementation of the EU AI Act in Ireland, establish a national AI governance structure, and build public trust in AI through transparency and accountability measures." (p. 22)

> "Ireland will establish an AI Office to coordinate national implementation of the EU AI Act and ensure coherence across sectoral regulators." (p. 23)

---

### Documento 3 — National AI Strategy 2021

| Campo | Valor |
|---|---|
| Archivo | `IRL_NationalAIStrategy_2021.pdf` |
| Título oficial | AI – Here for Good: National Artificial Intelligence Strategy for Ireland |
| Emisor | Department of Enterprise, Trade and Employment (DETE) |
| Tipo | `policy_strategy` |
| Fecha publicación | 2021-07 |
| Status | `in_use` |
| Idioma | EN |
| Páginas | 74 |
| Tamaño | 4.8 MB |
| URL primaria | https://enterprise.gov.ie/en/publications/publication-files/national-ai-strategy.pdf |
| Descarga efectiva | Directa (HTTP 200) |
| SHA-256 | `9b72d6d672bcce34e0e50ff14d2f3d7df23ed67f7ca7099b24f21a064a64eebe` |

**Citas textuales relevantes:**

> "Our vision is for Ireland to be a global leader in using and developing AI for the benefit of business and society." (p. 7)

> "Ireland's approach to AI governance will be risk-based, proportionate, and human-centric, in line with the European approach set out in the EU White Paper on AI." (p. 45)

> "We will work with EU institutions to ensure that the AI regulatory framework being developed at European level is fit for purpose and facilitates innovation while protecting citizens' rights." (p. 46)

---

### Documento 4 — General Scheme AI Bill 2026

| Campo | Valor |
|---|---|
| Archivo | `IRL_AIBill2026_GeneralScheme.pdf` |
| Título oficial | General Scheme of the Regulation of Artificial Intelligence Bill 2026 |
| Emisor | Department of Enterprise, Trade and Employment (DETE) / Government of Ireland |
| Tipo | `bill_pending` |
| Fecha publicación | 2026-02 |
| Status | `bill_pending` |
| Idioma | EN |
| Páginas | 180 |
| Tamaño | 1.2 MB |
| URL primaria | https://enterprise.gov.ie/en/legislation/legislation-files/general-scheme-of-the-regulation-of-artificial-intelligence-bill-2026.pdf |
| Descarga efectiva | Directa (HTTP 200) |
| SHA-256 | `ca0f1c74524fccb37e7f15f81d0e8d5f1b15a9c0a72b82d79a2a77c1e8d69b45` |

**Citas textuales relevantes:**

> "Head 3 — Establishment of the AI Office of Ireland (Oifig Intleachta Shaorga na hÉireann). There is hereby established a body to be known as the AI Office of Ireland [...] The AI Office shall act as the national coordinating body for the purposes of the AI Act." (Head 3.1, 3.3)

> "Head 7 — Market Surveillance Authorities. The following bodies are hereby designated as Market Surveillance Authorities for the purposes of Article 74 of the AI Act in respect of the sectors and systems specified: (a) An Garda Síochána — law enforcement; (b) Central Bank of Ireland — financial services; (c) Data Protection Commission — data protection; (d) Health Information and Quality Authority — health systems; [...] [15 authorities total]." (Head 7.1)

> "Head 12 — Administrative Fines. In addition to and without prejudice to the administrative fines provided for in Article 99 of the AI Act, a Market Surveillance Authority may, where appropriate, impose an administrative fine on a provider or deployer [...] not exceeding €500,000." (Head 12.1)

> "This Act shall come into operation on 1 August 2026." (Head 2.2)

---

## 4. Propuesta de recodificación

### 4.1 Variables principales

| Variable | Valor IAPP | Propuesta estudio | Cambio |
|---|---|---|---|
| `has_ai_law` | 1 | **1** | Sin cambio |
| `regulatory_regime` | `comprehensive` | **`binding_regulation`** | Reclasificación taxonómica |
| `regulatory_intensity` | 10 | **10** | Sin cambio — confirmado |
| `thematic_coverage` | 14 | **14** | Sin cambio — confirmado |
| `enforcement_level` | — | **`high`** | Adición (no codificado en IAPP) |
| `regulatory_regime_group` | — | **`binding_regulation`** | Adición |

### 4.2 Justificación

**`binding_regulation` (máximo nivel):**

El EU AI Act cumple todos los criterios del bucket `binding_regulation`:
1. **Ley IA-específica horizontal vigente:** Reg. 2024/1689, en vigor 1 agosto 2024.
2. **Aplicación directa:** No requiere transposición. Crea obligaciones directas para operadores privados en Irlanda desde agosto 2024.
3. **Enforcement institucional activo:** La DPC (Data Protection Commission) opera como autoridad GDPR principal para Big Tech en Irlanda y es designada como Market Surveillance Authority bajo el AI Bill. El AI Office of Ireland estará operativo agosto 2026.
4. **Sanciones efectivas:** Hasta €35M o 7% de facturación global (Art. 99 AI Act) + sanciones nacionales adicionales (Head 12 AI Bill: hasta €500K).
5. **Obligaciones concretas vinculantes:** Prohibiciones absolutas (Art. 5), gestión de riesgos (Art. 9), transparencia (Arts. 13-14), supervisión humana (Art. 14), conformidad pre-mercado (Art. 43), CE marking (Art. 47).

**Nota sobre `comprehensive` → `binding_regulation`:**
La IAPP usa el término `comprehensive` para lo que este estudio clasifica como `binding_regulation`. Reclasificación taxonómica, no cambio sustantivo. La codificación IAPP (has_ai_law=1, intensity=10, coverage=14) es correcta y consistente con el corpus.

**`enforcement_level: high`:**
- DPC con track record de multas GDPR de 8 cifras (Meta €1.2B, 2023; WhatsApp €225M, 2021).
- AI Act con sanciones hasta 7% facturación global.
- AI Bill 2026 establece 15 autoridades sectoriales con poderes de enforcement.
- Nivel `high` plenamente justificado.

### 4.3 Variables adicionales del estudio

| Variable | Valor propuesto |
|---|---|
| `ai_law_name` | Regulation (EU) 2024/1689 (AI Act) |
| `ai_law_year` | 2024 |
| `ai_law_status` | in_force |
| `national_strategy` | 1 (2021 + Refresh 2024) |
| `has_dedicated_ai_authority` | 0 (AI Office pendiente de creación por AI Bill 2026; previsto agosto 2026) |
| `gdpr_or_equivalent` | 1 (GDPR directamente aplicable + Data Protection Act 2018) |

---

## 5. Comparación con IAPP

| Dimensión | IAPP | Este estudio |
|---|---|---|
| Régimen | `comprehensive` | `binding_regulation` |
| has_ai_law | 1 | 1 ✓ |
| intensity | 10/10 | 10/10 ✓ |
| coverage | 14/15 | 14/15 ✓ |
| Enforcement | no codif. | `high` |

**Veredicto:** La codificación IAPP es correcta. Este estudio la confirma y añade variables no presentes en IAPP (enforcement_level, has_dedicated_ai_authority). El cambio `comprehensive` → `binding_regulation` es reclasificación taxonómica de esquemas distintos, no corrección.

---

## 6. Limitaciones y notas

1. **AI Bill 2026 status.** El corpus captura el General Scheme (anteproyecto, feb 2026). No es ley promulgada. Cuando sea aprobado y promulgado, actualizar `has_dedicated_ai_authority` → 1 y añadir el texto final al corpus.

2. **GDPR no incluido.** Decisión metodológica documentada en SOURCES.md §5. La DPC tiene jurisdiction GDPR sobre todas las Big Tech con sede europea en Irlanda.

3. **DPC AI guidance.** La DPC ha publicado orientaciones sobre IA y GDPR pero no hay un documento PDF consolidado único. No incluido: material disperso en portal web.

4. **Sector financiero.** El Central Bank of Ireland tiene guidance específico sobre IA en servicios financieros. No incluido: no es ley IA-específica ni estrategia nacional; es guidance sectorial derivado del AI Act.

---

## 7. Resumen ejecutivo

Irlanda presenta el régimen IA más robusto de la muestra, en línea con los demás EEMM del Grupo B. El EU AI Act es directamente aplicable, convirtiendo a Irlanda de facto en jurisdicción de `binding_regulation` desde agosto 2024. El diferencial irlandés es institucional: la DPC es la autoridad GDPR con mayor jurisdicción sobre Big Tech global (Meta, Google, Apple, Microsoft) y actuará como principal Market Surveillance Authority IA. El AI Bill 2026 crea además la AI Office of Ireland y designa 15 autoridades sectoriales, con operatividad prevista para agosto 2026 (fecha de aplicación plena del EU AI Act).

Corpus: 4 documentos. 1 ley IA-específica vinculante + 2 estrategias nacionales + 1 bill pendiente.
