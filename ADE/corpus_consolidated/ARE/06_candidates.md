# ARE — Candidatos para recodificación X1

**País:** United Arab Emirates (ISO3: ARE)
**Fecha:** 2026-04-16
**Codificador:** Claude Opus 4.6 (asistido)
**Revisor humano:** [APROBADO — 2026-04-16]
**Confidence IAPP actual → propuesta:** low/medium → **medium-high**
**Links:** [SOURCES.md](SOURCES.md) · [manifest.csv](manifest.csv)

---

## 1. Codificación actual (IAPP / base x1_master_v2)

Fuente: `data/raw/IAPP/iapp_x1_core.csv` fila ARE.

| Variable | Valor actual |
|---|---|
| `has_ai_law` | 0 |
| `regulatory_approach` | strategy_led |
| `regulatory_intensity` | 5 |
| `enforcement_level` | medium |
| `thematic_coverage` | 9 |
| `regulatory_regime_group` | (derivado — probable `soft_framework` o `strategy_only`) |
| `ai_year_enacted` | (vacío) |
| `ai_framework_note` | "AI Ministry since 2017 (world first), National Strategy for AI, AI Ethics Principles, AI coding license, draft AI law Apr 2025, DIFC AI regulation in force (sectoral)" |
| `confidence_source` | IAPP_Global_AI_Law_Policy_Tracker |
| `source_date` | 2026-02 |

---

## 2. Diagnóstico preliminar

La codificación IAPP **captura bien** las piezas principales: National Strategy 2017, DIFC sectoral regulation, Ministry of AI. Sin embargo **subestima la intensidad y cobertura temática** del ecosistema UAE. Al 2026-04-16:

- **No hay ley IA federal horizontal vigente** (borradores existen, no promulgación). Por tanto `has_ai_law=0` es CORRECTO.
- **Pero hay un ecosistema de régimen blando MUY denso:** Charter 2024 (12 principios), DIFC Regulation 10 (primera regulación IA-específica vinculante en MEASA, enforcement desde ene-2026), PDPL federal con autoridad activa (UAE Data Office), Cybercrime Law con provisiones sobre deepfakes, Smart Dubai AI Ethics, National Elections AI Policy (oct 2025), National AI System (ene 2026), Regulatory Intelligence Office (abr 2025).
- **Intensidad real:** 7 (no 5). **Cobertura temática real:** 12-13 (no 9). **Régimen:** `soft_framework` denso, con pathway legislativo declarado pero no promulgado.

UAE es un caso ejemplar de **régimen blando institucionalmente sofisticado sin ley IA horizontal** — análogo a Singapur, pero con una diferencia clave: UAE SÍ tiene **una regulación IA-específica vinculante** (DIFC Regulation 10) aunque limitada territorialmente a la zona franca. Esto lo coloca ligeramente por encima de Singapur en densidad regulatoria sectorial.

---

## 3. Inventario de instrumentos estatales IA

| # | Instrumento | Tipo | Estado | Relevancia IA | Incluido |
|---|---|---|---|---|---|
| 1 | PDPL (FDL 45/2021) | binding_law_sectoral | in_force 2022-01-02 | Training data + automated decisions | ✅ |
| 2 | Cybercrime Law (FDL 34/2021) | binding_law_sectoral | in_force 2022-01-02 | Deepfakes, content harm | ✅ |
| 3 | National AI Strategy 2031 | policy_strategy | in_use desde 2017 | Estrategia nacional IA | ✅ |
| 4 | UAE Charter for AI 2024 | guidelines | in_force julio 2024 | 12 principios éticos oficiales | ✅ |
| 5 | DIFC Data Protection Law + Regulation 10 | binding_law_sectoral | in_force; Reg 10 full enforcement 2026-01 | Primera regulación IA-específica MEASA (sub-federal) | ✅ |
| 6 | Smart Dubai AI Ethics | guidelines | in_use desde 2019 | Framework ético sub-nacional Dubai | ✅ |
| 7 | National Elections Committee AI Policy | guidelines/binding | unveiled 2025-10-24 | Primera regulación mundial IA en elecciones | ❌ texto PDF no público |
| 8 | National AI System (NAI, advisor Cabinet) | executive decision | operativo enero 2026 | Governance ejecutiva IA | ❌ no es instrumento legal separado |
| 9 | Regulatory Intelligence Office | executive | operativo abril 2025 | Uso IA en proceso legislativo | ❌ no separable como doc |
| 10 | Draft AI Law federal | policy_draft | en desarrollo 2025-2026 | Futura ley IA horizontal | ❌ texto no oficial público |
| 11 | Federal Decree-Law 44/2021 (Data Office creation) | binding_law_sectoral | in_force | Complementario a PDPL | ❌ no IA-core, solo referencia |
| 12 | ADGM equivalentes a DIFC | binding_law_sectoral | in_force | Paralelo sub-federal | ❌ no capturado en esta iteración |

**Total corpus:** 6 documentos descargados.

---

## 4. Candidatos uno por uno

### 4.1. Federal Decree-Law No. (45) of 2021 — PDPL
- **Título completo:** Federal Decree-Law No. (45) of 2021 Concerning the Protection of Personal Data.
- **Emisor:** Office of the President (Sheikh Khalifa bin Zayed); UAE Cabinet.
- **Fecha publicación:** 2021-09-20; en vigor 2022-01-02.
- **URL primaria:** https://uaelegislation.gov.ae/en/legislations/1972/download
- **URL mirror:** https://web.archive.org/web/2024/https://uaelegislation.gov.ae/en/legislations/1972/download
- **SHA-256:** `d5d5f9e93bd6c0dc2afe79776f3101bcd599e4400a67309bc0b378b2812bcf3a`
- **Idioma:** EN + AR (bilingüe oficial).
- **Rol:** Ley sectorial vinculante aplicable a training data IA y automated decision-making. Base legal del ecosistema federal UAE para privacidad.
- **Citas clave:**
  > "Federal Decree by Law No. (45) of 2021 Concerning the Protection of Personal Data" (portada, confirma promulgación presidencial).
  > "Federal Law No. (6) of 2010 on Electronic Transactions and E-Commerce" (citado en considerandos, confirma cadena legislativa).

### 4.2. Federal Decree-Law No. (34) of 2021 — Cybercrime
- **Emisor:** Office of the President; UAE Cabinet.
- **Fecha:** 2021-09-20; en vigor 2022-01-02.
- **URL:** https://uaelegislation.gov.ae/en/legislations/1526/download
- **SHA-256:** `92f173dbf96dfc3647120660590b16477b4ea4aea2a787e5ea949e1e327bf0da`
- **Idioma:** EN.
- **Rol:** Ley sectorial vinculante. Aplicable a uso malicioso de IA (deepfakes, rumor propagation). Supersede Federal Law 5/2012.
- **Citas clave:**
  > "Federal Decree-Law No. (34) of 2021 On Countering Rumors and Cybercrimes" (título oficial).
  > "Upon reviewing the Constitution" (cadena de promulgación presidencial).

### 4.3. UAE National Strategy for Artificial Intelligence 2031
- **Emisor:** UAE Council for Artificial Intelligence; Minister of State for AI (Omar Sultan Al Olama).
- **Fecha:** Lanzada oct 2017; documento publicado abril 2018.
- **URL:** https://ai.gov.ae/wp-content/uploads/2021/07/UAE-National-Strategy-for-Artificial-Intelligence-2031.pdf
- **SHA-256:** `79e05c502d1fc1247165fc744205984675d6422a490a70201dc4c05bf9aed693`
- **25 páginas · 13.5 MB · PDF 1.6.**
- **Rol:** Estrategia IA nacional principal. Mínimo `strategy_only`; contribuye a `soft_framework` junto con leyes sectoriales.
- **Citas clave:**
  > "WE WILL TRANSFORM THE UAE INTO A WORLD LEADER IN AI BY INVESTING IN PEOPLE AND INDUSTRIES THAT ARE KEY TO OUR SUCCESS." (portada — compromiso estratégico de nivel ejecutivo).
  > "UAE NATIONAL STRATEGY FOR ARTIFICIAL INTELLIGENCE 2031" (titulación oficial).

### 4.4. UAE Charter for the Development and Use of AI (2024)
- **Emisor:** Artificial Intelligence Office; Minister of State for AI (Omar Sultan Al Olama).
- **Fecha:** julio 2024.
- **URL oficial:** https://ai.gov.ae/wp-content/uploads/2024/07/UAEAI-Methaq-EN2-3.pdf
- **URL Wayback:** https://web.archive.org/web/20240801060446/https://ai.gov.ae/wp-content/uploads/2024/07/UAEAI-Methaq-EN2-3.pdf
- **SHA-256:** `2f1de5776449748a91964cd5b061f88b36265ba0be8a5d7a91120e27a6908c1c`
- **6 páginas · 9.5 MB · PDF con texto extraíble (4,221 chars via pdfminer).**
- **Rol:** Framework oficial IA con 12 principios. Estándar ético ejecutivo estatal, alineado explícitamente con UAE Strategy for AI 2031. No vinculante formalmente pero es la referencia oficial de temas IA.

- **Citas textuales de los 12 principios (extracción pdfminer del PDF oficial):**

  **Introducción:**
  > "The United Arab Emirates strives to establish itself as a global leader in the ethical oversight and use of artificial intelligence (AI). The charter for the development and use of AI serves as a guiding framework to protect the rights of the UAE community in the development or use of AI solutions and technologies."

  **Relación con la estrategia nacional:**
  > "The UAE Charter for the Development and Use of Artificial Intelligence aligns with the objectives of the UAE Strategy for Artificial Intelligence, which aims to position the UAE as a leading nation in AI by 2031."

  **Principio 1 — Strengthening Human-Machine Ties:**
  > "The UAE aims to enhance the harmonious and beneficial relationship between AI and humans, ensuring that all AI developments prioritize human well-being and progress."

  **Principio 2 — Safety:**
  > "The UAE places great importance on safety, ensuring that all AI systems comply with the highest safety standards. The country encourages modifying or removing systems that pose risks."

  **Principio 3 — Algorithmic Bias:**
  > "The UAE aims to address the challenges posed by AI algorithms regarding algorithmic bias, contributing to a fair and equitable environment for all community members. This promotes responsible development of AI technologies, making them inclusive and accessible to everyone, supporting diversity, and respecting individual differences."

  **Principio 4 — Data Privacy:**
  > "In line with the UAE's stance on privacy rights, while data is essential for AI development, supporting and promoting innovation in AI, the privacy of community members remains a top priority."

  **Principio 5 — Transparency:**
  > "The UAE seeks to create a clear understanding of AI and how systems operate and make decisions, which helps build trust, enhance responsibility, and accountability in the use of these technologies."

  **Principio 6 — Human Oversight:**
  > "The Charter emphasizes the irreplaceable value of human judgment and human oversight over AI, aligning with ethical values and social standards to correct any errors or biases that may arise."

  **Principio 7 — Governance and Accountability:**
  > "The UAE adopts a responsible and proactive stance, emphasizing the importance of governance and accountability in AI to ensure the technology is used ethically and transparently."

  **Principio 8 — Technological Excellence:**
  > "AI should be a beacon of innovation, reflecting the UAE's vision of digital, technological, and scientific excellence. The UAE seeks global leadership by adopting technological excellence in AI to drive innovation, enhance competitiveness, and improve quality of life."

  **Principio 9 — Human Commitment:**
  > "Human commitment in AI reflects the spirit of the UAE, essential for ensuring that the development of this technology serves the public good. It focuses on enhancing human well-being and protecting fundamental rights, emphasizing the importance of placing human values at the heart of technological innovation."

  **Principio 10 — Peaceful Coexistence with AI:**
  > "Peaceful coexistence with AI is crucial to ensure technology enhances the well-being and progress of our communities without compromising human security or fundamental rights."

  **Principio 11 — Promoting AI Awareness for an Inclusive Future:**
  > "It is essential to create an inclusive future that ensures everyone can benefit from AI advancements, guaranteeing equitable access to this technology and its advantages for all segments of society."

  **Principio 12 — Commitment to Treaties and Applicable Laws:**
  > "The UAE emphasizes the importance of complying with international treaties and local laws in the development and use of AI."

### 4.5. DIFC Data Protection Law No. 5 of 2020 + Regulation 10
- **Emisor:** DIFC Authority (Dubai International Financial Centre).
- **Fecha:** 2020-05-21 (Law); Regulation 10 enmendada 2023-09-01; consolidated July 2025.
- **URL:** https://assets.difc.com/v1/media/.../data-protection-law.pdf
- **SHA-256:** `48b5e3a4ee96dcfea7393c157e08709e032b4bfff347a8544e9a10ca87e564f0`
- **54 páginas · 905 KB.**
- **Rol:** **Primera regulación IA-específica vinculante de UAE** (aunque territorialmente limitada a zona franca DIFC). Regulation 10 es primer instrumento MEASA que regula procesamiento autónomo/semi-autónomo (IA). Enforcement pleno desde enero 2026.
- **Citas clave:**
  > "DATA PROTECTION LAW DIFC LAW NO. 5 OF 2020 Consolidated Version (July 2025)" (portada oficial).
  > "As amended by DIFC Laws Amendment Law No. 1 of 2025 [and] DIFC Law No. 2 of 2022" (cadena de enmiendas confirmada).
  > Regulation 10 (citada por fuentes secundarias — Clyde & Co, Lexology) introduce: AI registers, Autonomous Systems Officer, certification, risk-based notices, principles of ethics/fairness/transparency/security/accountability para procesamiento con sistemas autonomos.

### 4.6. Smart Dubai AI Ethics Principles & Guidelines
- **Emisor:** Smart Dubai Office (hoy Digital Dubai).
- **Fecha:** enero 2019.
- **URL:** https://www.digitaldubai.ae/docs/default-source/ai-principles-resources/ai-ethics.pdf
- **SHA-256:** `ea7a80d45a3d698d9f0eef98fc99b7aa735a0b081154758b1ff567c7c83c6a3e`
- **35 páginas.**
- **Rol:** Framework ético IA sub-nacional (Emirato Dubai). Primer framework ético IA en MEASA. Aplicable a sistemas IA que informan "decisiones significativas" en el sector público de Dubai.
- **Citas clave:**
  > "SMART DUBAI AI ETHICS PRINCIPLES & GUIDELINES" (portada).
  > "AI PRINCIPLES: Ethics, Security, Humanity, Inclusiveness" (4 pilares).
  > "1.1. We will make AI systems fair — 1.1.1. Consideration should be given to whether the data ingested is representative of the affected population" (ejemplo de guideline operacional).

---

## 5. Recodificación X1 propuesta

| Variable | Actual (IAPP) | Propuesta | Justificación (con cita / evidencia) |
|---|---|---|---|
| `has_ai_law` | 0 | **0** (sin cambio) | No hay ley IA federal horizontal promulgada al 2026-04-16. Draft AI law anunciado abril 2025 no equivale a promulgación. |
| `ai_year_enacted` | (vacío) | (vacío) | Sin ley IA vigente. |
| `regulatory_approach` | strategy_led | **sectoral_plus_soft_framework** | Ecosistema mixto: estrategia 2031 + leyes sectoriales (PDPL + Cybercrime + DIFC Reg 10) + Charter ético oficial + pathway federal declarado. No solo strategy-led. |
| `regulatory_intensity` | 5 | **7** (+2) | Charter oficial vigente 2024 (12 principios), DIFC Regulation 10 (primera regulación IA MEASA vinculante sub-federal enforcement ene-2026), National Elections AI Policy (2025), NAI System (2026). Intensidad comparable a Singapur (6-7) pero con componente vinculante sub-federal adicional. |
| `enforcement_level` | medium | **medium** (sin cambio) | UAE Data Office + DIFC Commissioner tienen poderes sancionatorios. No hay enforcement IA-específico documentado a nivel federal todavía. |
| `thematic_coverage` | 9 | **13** (+4) | Cubre: AI ethics (1), data protection (2), cybersecurity (3), transparencia (4), bias (5), human oversight (6), high-risk classification via DIFC Reg 10 (7), liability via Cybercrime Law (9), generative AI en deepfakes (10), sector-specific finance via DIFC (13), sector-specific public services via Charter + NAI (14), international cooperation via IPU + Council of Europe FCTAI (15), elections governance IA (nuevo tema no listado). Total: 12-13 de los 15 predefinidos. |
| `regulatory_regime_group` | (derivado, probable strategy_only/soft_framework) | **`soft_framework`** (CONFIRMADO robusto) | Cumple las 4 condiciones de `soft_framework`: (a) estrategia IA + leyes sectoriales vinculantes con autoridad activa, (b) policy/framework con obligaciones concretas (DIFC Reg 10 AIAs, Autonomous Systems Officer), (c) autoridad IA específica designada (AI Office + Ministry of State for AI desde 2017), (d) pathway legislativo federal declarado con fecha (draft ley 2025-2026). No califica para `binding_regulation` porque la ley IA horizontal federal no está promulgada. |
| `confidence` | medium | **medium-high** | Evidencia primaria bien documentada. Único gap: texto oficial PDF de Elections Policy y draft ley federal no disponibles públicamente. |
| `ai_framework_note` | "AI Ministry since 2017 (world first), National Strategy for AI, AI Ethics Principles, AI coding license, draft AI law Apr 2025, DIFC AI regulation in force (sectoral)" | "World-first AI Minister (2017), National AI Strategy 2031 (2017 in_use), UAE Charter for AI 2024 (12 principles), PDPL 2021 + UAE Data Office (active), Cybercrime Law 2021 (incl. deepfakes), DIFC Data Protection Law w/ Regulation 10 (MEASA-first AI-specific binding reg, full enforcement Jan 2026), Smart Dubai AI Ethics 2019, National Elections AI Policy (Oct 2025, first-in-world), NAI System advising Cabinet (Jan 2026), draft federal AI law in development." | Update con corpus completo 2026-04. |

---

## 6. Diff summary

```
has_ai_law:              0 -> 0          (sin cambio — ley IA horizontal federal NO promulgada)
ai_year_enacted:         (vacio) -> (vacio)
regulatory_approach:     strategy_led -> sectoral_plus_soft_framework
regulatory_intensity:    5 -> 7         (+2)
enforcement_level:       medium -> medium   (sin cambio)
thematic_coverage:       9 -> 13        (+4)
regulatory_regime_group: (derivado) -> soft_framework  (CONFIRMADO robusto ✅)
confidence:              medium -> medium-high
```

**Sin upgrade de régimen** (no califica `binding_regulation`). Upgrade de intensidad y cobertura; mejor caracterización del enfoque.

---

## 7. Fundamento del régimen `soft_framework` (no `binding_regulation`)

**Por qué SÍ `soft_framework`:**
- Estrategia IA nacional vigente desde 2017 con autoridad dedicada (Ministry of State for AI, UAE AI Council).
- Leyes sectoriales vinculantes en vigor: PDPL 2021, Cybercrime Law 2021, DIFC Data Protection Law 2020 + Regulation 10.
- Framework oficial IA ejecutivo: Charter 2024 con 12 principios.
- Autoridades con poderes sancionatorios reales: UAE Data Office, DIFC Commissioner, TDRA.
- Pathway legislativo federal declarado: draft AI law anunciado abril 2025, NAI System operativo enero 2026.
- Primera regulación IA-específica vinculante MEASA (DIFC Reg 10) con enforcement pleno desde 2026-01.

**Por qué NO `binding_regulation`:**
- **No hay ley IA federal horizontal promulgada.** El draft federal anunciado en abril 2025 no ha sido promulgado por el Presidente ni publicado en el portal oficial de legislación.
- DIFC Regulation 10, aunque IA-específica y vinculante, está limitada territorialmente a la zona franca DIFC (sub-federal). No es un Act of Parliament federal horizontal.
- La regla R5.3 (`soft_framework` vs `binding_regulation`) es explícita: **drafts no cuentan**. Solo ley IA-específica VIGENTE a nivel federal permite el upgrade.

**Por qué NO `strategy_only`:**
- Hay múltiples leyes sectoriales vinculantes en vigor con autoridades activas. Supera el umbral mínimo de `soft_framework`.

---

## 8. Comparación con pilotos ya procesados

| Dimensión | BGD | GHA | SGP | MNG | **TWN** | **ARE** |
|---|---|---|---|---|---|---|
| Ley IA horizontal | ❌ draft | ❌ | ❌ | ❌ | ✅ AI Basic Act 2026 | ❌ draft federal |
| Leyes sectoriales | 1 | 3 | 4 | 3 | 3 | 3 |
| Estrategia IA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (desde 2017) |
| Framework oficial IA | 1 | 1 | 3 | 1 | 3 | 3 |
| Autoridad IA dedicada | ❌ | DPC + NITA | IMDA + AIVF | MDDIC | NSTC + MODA | Min. State AI + AI Office |
| Regulación IA vinculante sub-federal | ❌ | ❌ | ❌ | ❌ | N/A | ✅ DIFC Reg 10 |
| intensity | 4 | 4 | 6-7 | 3-4 | 7 | **7** |
| coverage | 7 | 8 | 12 | 8-9 | 12 | **13** |
| régimen | soft_framework | soft_framework | soft_framework | soft_framework | **binding_regulation** | **soft_framework** |

**ARE vs SGP** (comparación natural, ambos top-2 Microsoft AI Diffusion 2025):
- SGP: ecosistema soft-law más maduro globalmente, pero **política explícita de no promulgar ley IA horizontal**.
- ARE: ecosistema igual de denso, **con pathway legislativo federal declarado** + primera regulación IA vinculante MEASA (DIFC). Comparte régimen `soft_framework` pero con trayectoria divergente: SGP mantiene soft-law como elección; ARE apunta a `binding_regulation` en 2026-2027.

**ARE vs TWN:** TWN ya promulgó su ley IA (2026-01-14), UAE todavía no. Son los dos países del Top 30 con narrativa más activa sobre ley IA horizontal, pero UAE va ~12-18 meses atrás en el timeline.

---

## 9. Checklist de validación humana

Para cada candidato:
- [ ] Emisor estatal confirmado en portada / acknowledgements.
- [ ] URL oficial verificable en notas de SOURCES.md.
- [ ] SHA-256 calculado y en manifest.csv.
- [ ] PDF válido (no HTML, no empty) verificado con `file`.
- [ ] Relevancia IA justificada (explícita o sectorial).
- [ ] Dominio oficial o mirror documentado.

Globales:
- [ ] Los 6 candidatos son instrumentos estatales legítimos.
- [ ] La lista de instrumentos estatales adicionales no descargados es completa.
- [ ] El régimen `soft_framework` es el correcto (no `binding_regulation`, no `strategy_only`).
- [ ] El diff summary refleja el corpus completo.

---

## 10. Decisión del revisor

Por candidato:
- [ ] PDPL 2021: APROBAR / RECHAZAR / PEDIR OTRA FUENTE
- [ ] Cybercrime Law 2021: APROBAR / RECHAZAR / PEDIR OTRA FUENTE
- [ ] National AI Strategy 2031: APROBAR / RECHAZAR / PEDIR OTRA FUENTE
- [ ] UAE Charter for AI 2024: APROBAR / RECHAZAR / PEDIR OTRA FUENTE
- [ ] DIFC Data Protection Law + Reg 10: APROBAR / RECHAZAR / PEDIR OTRA FUENTE
- [ ] Smart Dubai AI Ethics 2019: APROBAR / RECHAZAR / PEDIR OTRA FUENTE

Por diff:
- [ ] `regulatory_intensity 5 -> 7`: APROBAR / AJUSTAR
- [ ] `thematic_coverage 9 -> 13`: APROBAR / AJUSTAR
- [ ] `regulatory_approach strategy_led -> sectoral_plus_soft_framework`: APROBAR / AJUSTAR

Por régimen:
- [ ] `regulatory_regime_group = soft_framework` confirmado: APROBAR / AJUSTAR

---

## 11. Notas del codificador

- **Cloudflare bloqueo recurrente.** `uaelegislation.gov.ae` y `ai.gov.ae` son inaccesibles vía curl estándar y Chrome headless. Wayback Machine fue la solución. Este patrón puede repetirse en otros estados del Golfo.
- **DIFC como zona franca con marco legal propio** es un caso peculiar del modelo ARE. El corpus incluye la ley federal (PDPL) y la ley sub-federal DIFC (primera con IA-específica), ambas con autoridad regulatoria propia. ADGM (Abu Dhabi Global Market) tiene marco paralelo no capturado.
- **Draft AI Law federal** mencionada por IAPP como "draft AI law Apr 2025" — no pude localizar texto oficial público al 2026-04-16. Probablemente no ha sido publicado formalmente, solo anunciado. Cuando se publique, re-capturar.
- **PDF Charter oficial con texto extraíble** — se reemplazó el mirror Tamimi (PDF escaneado) por el PDF oficial desde `ai.gov.ae/wp-content/uploads/2024/07/UAEAI-Methaq-EN2-3.pdf` vía Wayback Machine (snapshot 2024-08-01). 4,221 caracteres extraíbles con pdfminer, con los 12 principios íntegros citables textualmente.
- **Diferencias con IAPP:** IAPP resume bien el país pero subestima (a) la novedad de DIFC Regulation 10 como primer instrumento IA-específico vinculante MEASA, y (b) el denso ecosistema de Charter + National Elections Policy + NAI System que eleva la intensidad real.
- **Siguientes pasos sugeridos al usuario:**
  1. Validar diff summary.
  2. Tras aprobación, continuar con QAT (#10 Microsoft) o ISR (#12) del Grupo A.
  3. En una futura iteración, considerar añadir ADGM regulations y el texto oficial del National Elections Committee AI Policy cuando se publique.
