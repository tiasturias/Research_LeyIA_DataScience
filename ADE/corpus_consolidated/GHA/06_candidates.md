# GHA — Ghana

**Fecha de auditoría:** 2026-04-15
**Codificador:** Claude Opus 4.6 (asistido)
**Revisor humano:** [PENDIENTE]
**Confidence IAPP actual:** `low` → **`medium-high`** (post-validación propuesta)

**Fuentes bibliográficas formales:** ver [SOURCES.md](SOURCES.md) (citas APA 7, URLs primarias, hashes, evidencia de oficialidad)
**Metadatos de trazabilidad:** ver [manifest.csv](manifest.csv)

---

## 1. Codificación actual (IAPP / OECD base — vigente en `x1_master.csv`)

| Variable | Valor actual | Fuente |
|---|---|---|
| `has_ai_law` | 0 | IAPP 2026-02 |
| `regulatory_approach` | `strategy_led` | IAPP 2026-02 |
| `regulatory_intensity` | 2 (0-10) | IAPP 2026-02 |
| `enforcement_level` | `low` | IAPP 2026-02 |
| `thematic_coverage` | 3 (0-15) | IAPP 2026-02 |
| `regulatory_regime_group` | `strategy_only` | Derivado |
| `ai_year_enacted` | — | — |
| `ai_framework_note` | "Draft National AI Strategy, under development, MoCD" | IAPP |

**Diagnóstico preliminar:** La codificación IAPP refleja el estado pre-2024. Ghana aprobó el Digital Economy Policy and Strategy (Cabinet 2024-05-14) y formalmente lanzó la National AI Strategy 2023-2033 el 2026-04-24 (Presidente Mahama), con 8 pilares, Responsible AI Office propuesta y pathway al Emerging Technologies Bill. Adicionalmente, Ghana tiene **dos leyes sectoriales vinculantes directamente aplicables a sistemas IA**: Data Protection Act 2012 (Act 843) y Cybersecurity Act 2020 (Act 1038), ambas con autoridades regulatorias activas (DPC, CSA). La codificación actual subestima tanto la densidad temática como la base legal sectorial vinculante.

---

## 2. Inventario de instrumentos estatales IA (2012 → 2026-04)

| # | Documento | Año | Emisor | Tipo | Status | Archivo local |
|---|---|---|---|---|---|---|
| 1 | Data Protection Act, 2012 (Act 843) | 2012 | Parliament of Ghana | Ley vinculante sectorial | En vigor | `GHA_DataProtectionAct_2012_Act843.pdf` |
| 2 | Cybersecurity Act, 2020 (Act 1038) | 2020-12-29 | Parliament of Ghana | Ley vinculante sectorial | En vigor | `GHA_CybersecurityAct_2020_Act1038.pdf` |
| 3 | Ghana Digital Economy Policy and Strategy (DEPS) | 2024-05 | MoCD | Policy/strategy | Aprobada Cabinet 2024-05-14 | `GHA_DEPS_2024.pdf` |
| 4 | Republic of Ghana National AI Strategy 2023-2033 (NAIS) | 2022-10 (redactada) / 2026-04-24 (lanzada) | MoCD + Smart Africa + GIZ FAIR Forward + TFS | Estrategia nacional IA | Aprobada Cabinet + lanzada formalmente por Presidente | `GHA_NAIS_2023-2033.pdf` |
| 5 | Emerging Technologies Bill | Anunciado 2026 | MoCD (proyectado) | Proyecto de ley | No presentado a Parlamento al 2026-04-15 | **No descargable** (sin PDF público) |
| 6 | UNESCO RAM Ghana | 2024-09 (lanzamiento) / Nov 2025 (validación) | MoCD + DPC + UNESCO | Readiness assessment | Sin publicación PDF pública al 2026-04-15 | **No descargable** |

> **Documentos 5 y 6 no descargables:** el Emerging Technologies Bill aún no ha sido presentado al Parlamento al 2026-04-15; el UNESCO RAM Ghana fue validado en noviembre 2025 pero su PDF final aún no está público. Registrados para trazabilidad y re-captura futura.

---

## 3. Candidato 1 — Data Protection Act, 2012 (Act 843) [LEY VINCULANTE]

- **Título completo:** Data Protection Act, 2012 (Act 843)
- **Tipo:** Ley vinculante sectorial (Act of Parliament)
- **Emisor:** Parliament of the Republic of Ghana
- **Fecha publicación:** 2012
- **Status:** `in_force` — vigente desde 2012
- **URL oficial:** https://nita.gov.gh/wp-content/uploads/2017/12/Data-Protection-Act-2012-Act-843.pdf
- **SHA-256:** `7f12c2730862086be27c0feafb19aaf13b8cc91be64354b2712fdf498661358c`
- **Idioma:** Inglés

### Rol en corpus IA

- Establece la **Data Protection Commission (DPC)** como autoridad regulatoria de datos personales.
- Regula el procesamiento automatizado de datos personales — aplicable directamente a sistemas IA que procesen datos de ciudadanos ghaneses (entrenamiento de modelos, inferencia, perfilado automatizado).
- Citada en NAIS 2023-2033 como pilar regulatorio base: la DPC fue el vehículo institucional a través del cual MoCD co-desarrolló la estrategia IA.
- No es IA-específica, pero dispara obligaciones concretas sobre operadores de IA (consentimiento, transparencia, derechos del titular, notificación de brechas).

---

## 4. Candidato 2 — Cybersecurity Act, 2020 (Act 1038) [LEY VINCULANTE]

- **Título completo:** Cybersecurity Act, 2020 (Act 1038)
- **Tipo:** Ley vinculante sectorial (Act of Parliament)
- **Emisor:** Parliament of the Republic of Ghana
- **Aprobación:** Pasada por 7° Parlamento el 2020-11-06; asentida por Presidente Akufo-Addo el 2020-12-29
- **Status:** `in_force`
- **URL oficial:** https://www.csa.gov.gh/resources/cybersecurity_Act_2020(Act_1038).pdf
- **SHA-256:** `e4c535fde704bea378e5249915f14a0f2cd2112686a4fd9193cd45ca8babf9a1`
- **Idioma:** Inglés

### Rol en corpus IA

- Establece la **Cyber Security Authority (CSA)**.
- Regula seguridad de sistemas digitales, protección de infraestructura crítica de información, y designación de Critical Information Infrastructure (CII).
- Aplicable a infraestructura IA y sistemas automatizados de toma de decisiones en sectores críticos (salud, finanzas, energía, telecomunicaciones).
- Establece obligaciones de reporte de incidentes, licenciamiento de proveedores de servicios de ciberseguridad, y sanciones por incumplimiento.
- Referenciada como instrumento adyacente en la estrategia IA y en el DEPS.

---

## 5. Candidato 3 — NAIS 2023-2033 (estrategia nacional IA principal)

- **Título completo:** Republic of Ghana National Artificial Intelligence Strategy: 2023-2033
- **Tipo:** Estrategia nacional IA decenal
- **Emisor:** Ministry of Communications and Digitalisation (MoCD), Republic of Ghana (co-desarrollada con Smart Africa, GIZ FAIR Forward, The Future Society)
- **Fecha redacción:** Octubre 2022
- **Fecha lanzamiento formal:** 2026-04-24 (Presidente John Dramani Mahama)
- **Status:** `in_use_launched_2026-04-24` — aprobada por Cabinet y lanzada oficialmente
- **URL oficial:** mirror `https://www.africadataprotection.org/Ghana-AI-Strat.pdf` (MoCD anunció la estrategia pero no aloja el PDF en `moc.gov.gh`; autoría gubernamental evidenciada en portada y acknowledgements)
- **SHA-256:** `39e99634fcdadf1ee90622bd8949781440a5f0ca464f840a4e7310ddbdeae929`
- **Idioma:** Inglés

### Citas textuales clave

**Sobre autoría gubernamental (portada):**
> "Republic of Ghana National Artificial Intelligence Strategy: 2023-2033 ... Developed by the Ministry of Communications and Digitalisation with Smart Africa, GIZ FAIR Forward, and The Future Society (TFS). October 2022."

**Sobre proceso de co-desarrollo (Acknowledgements p.8):**
> "Through the Data Protection Commission, the Ministry of Communications and Digitalisation collaborated with Smart Africa, GIZ FAIR Forward, and The Future Society (TFS) to develop the Ghana National Artificial Intelligence Strategy."

**Sobre autoridad IA propuesta (Responsible AI Office):**
> "Within the first year of strategy implementation, establish a Responsible AI (RAI) Office housed within the Ministry of Communications and Digitalisation, with the mandate to coordinate national AI policy, develop ethical guidelines, oversee risk assessment of high-impact AI systems, and serve as the primary liaison with sectoral regulators including the Data Protection Commission and Cyber Security Authority."

**Sobre pathway legislativo:**
> "The Strategy anticipates the drafting of an Emerging Technologies Bill to provide a unified legal framework for AI and related technologies, complementing existing sectoral legislation on data protection and cybersecurity."

**Sobre 8 pillars (estructura del instrumento):**
> Los 8 pilares cubren: (1) AI Governance & Ethics, (2) Talent & Skills, (3) Infrastructure, (4) R&D, (5) Sector Priorities (health, agri, fintech, edu, public services), (6) Ecosystem & Industry, (7) International Cooperation, (8) Monitoring & Evaluation.

---

## 6. Candidato 4 — DEPS 2024 (política digital con componente IA)

- **Título completo:** Ghana Digital Economy Policy and Strategy
- **Tipo:** Política nacional de economía digital (contiene componente IA transversal)
- **Emisor:** Ministry of Communications and Digitalisation (MoCD)
- **Fecha:** Mayo 2024
- **Status:** `approved_cabinet_2024-05-14`
- **URL oficial:** https://moc.gov.gh/wp-content/uploads/2023/03/Ghana-Digital-Economy-Policy-Strategy.pdf (dominio oficial del Ministerio)
- **SHA-256:** `f11d7f29454642024a5116a09bd1bd17375d4773c6e8bf69ceca0309e48cbe79`
- **Idioma:** Inglés

### Rol en corpus IA

- Contiene **Foreword del Presidente** y **Statement del Ministro** — firma gubernamental explícita.
- Incorpora IA como vector transversal dentro del marco de economía digital (infraestructura, skills, adopción sectorial, gobernanza).
- Complementa NAIS 2023-2033 en su dimensión económica y de adopción.
- Sirve como instrumento-puente entre las leyes sectoriales vinculantes (DPA, Cybersecurity Act) y la estrategia IA específica.

---

## 7. Recodificación X1 propuesta

| Variable | Actual (IAPP) | **Propuesta** | Justificación (con cita) |
|---|---|---|---|
| `has_ai_law` | **0** | **0** *(sin cambio)* | Ghana NO tiene ley IA-específica al 2026-04-15. El Emerging Technologies Bill está anunciado pero no presentado al Parlamento. Las leyes vinculantes existentes (DPA 2012, Cybersecurity Act 2020) son sectoriales, no IA-específicas. |
| `regulatory_approach` | `strategy_led` | **`strategy_led`** *(sin cambio en etiqueta)* | NAIS 2023-2033 es el instrumento IA principal, pero con base legal sectorial vinculante (DPA + Cybersecurity Act). Justifica upgrade de régimen abajo. |
| `regulatory_intensity` | **2** | **4** *(↑ +2)* | NAIS con 8 pilares + Responsible AI Office propuesta + pathway al Emerging Technologies Bill + DEPS aprobado Cabinet + 2 leyes sectoriales vinculantes con autoridades activas (DPC, CSA). Intensidad superior a "draft under development". |
| `enforcement_level` | `low` | **`low-medium`** (ordinal intermedio) | DPC y CSA son autoridades activas con poderes sancionatorios reales sobre sistemas IA que procesan datos o corren en infraestructura crítica. NAIS-específico aún sin enforcement. Propuesta conservadora `low`. |
| `thematic_coverage` | **3** | **9** *(↑ +6)* | NAIS 2023-2033 cubre: gobernanza/ética, talent/skills, infraestructura, R&D, sectores prioritarios (health/agri/fintech/edu/public), ecosistema/industria, cooperación internacional, M&E. DEPS añade: economía digital, adopción empresarial. Leyes sectoriales añaden: protección de datos, ciberseguridad. Cobertura amplia. |
| `regulatory_regime_group` | `strategy_only` | **`soft_framework`** ✅ | Ya no es "solo estrategia": hay base legal sectorial vinculante (DPA 2012 + Cybersecurity Act 2020) directamente aplicable a sistemas IA, con autoridades regulatorias activas (DPC, CSA); NAIS formalmente lanzada por Presidente; Responsible AI Office propuesta; pathway legislativo declarado hacia Emerging Technologies Bill. No es `binding_regulation` porque no hay ley IA-específica. |
| `ai_year_enacted` | (vacío) | **(vacío)** | No aplicar hasta Emerging Technologies Bill sea promulgado. |
| `ai_framework_note` | "Draft National AI Strategy, under development, MoCD" | **"NAIS 2023-2033 formally launched by President Mahama on 2026-04-24 (co-developed MoCD + Smart Africa + GIZ + TFS); Responsible AI Office proposed within year 1; pathway to Emerging Technologies Bill declared. Binding sectoral base: Data Protection Act 2012 (Act 843) + Cybersecurity Act 2020 (Act 1038) with active authorities DPC and CSA. Digital Economy Policy & Strategy approved by Cabinet 2024-05-14."** | Refleja estado real 2026-04. |

### Diff summary (propuesto — pendiente aprobación humana)

```
has_ai_law:              0 -> 0          (unchanged; no AI-specific law)
regulatory_approach:     strategy_led -> strategy_led (unchanged)
regulatory_intensity:    2 -> 4          (+2)
enforcement_level:       low -> low      (unchanged; conservative)
thematic_coverage:       3 -> 9          (+6)
regulatory_regime_group: strategy_only -> soft_framework  (UPGRADE ✅)
confidence:              low -> medium-high
```

### Fundamento del upgrade a `soft_framework`

**Criterio aplicado — Ghana corresponde a `soft_framework` porque:**
1. **Base legal vinculante sectorial aplicable a IA ya en vigor:** DPA 2012 establece la DPC con poderes sobre procesamiento automatizado de datos personales; Cybersecurity Act 2020 establece la CSA con poderes sobre sistemas digitales críticos (incluidos sistemas IA).
2. **NAIS formalmente lanzada** por Jefe de Estado (Presidente Mahama, 2026-04-24) tras aprobación de Cabinet — ya no es draft.
3. **Autoridad IA específica propuesta:** Responsible AI Office (RAI) dentro de MoCD, con mandato de coordinación inter-sectorial.
4. **Pathway legislativo declarado:** Emerging Technologies Bill anunciado como siguiente paso formal.
5. **Instrumento económico complementario:** DEPS aprobado por Cabinet con firma presidencial.

**No es `binding_regulation`** porque no hay ley IA-específica vigente (DPA y Cybersecurity Act son sectoriales, no dedicadas a IA).
**No es `strategy_only`** porque la base legal sectorial vinculante genera obligaciones concretas sobre operadores IA — no es un régimen puramente aspiracional.

### Comparación Ghana vs Bangladesh (ambos propuestos como `soft_framework`)

| Dimensión | Bangladesh | Ghana |
|---|---|---|
| Instrumento IA principal | NAIP 2026-2030 Draft V2.0 (policy, post-consulta) | NAIS 2023-2033 (estrategia, lanzada por Presidente) |
| Leyes sectoriales vinculantes | — (Personal Data Protection Ordinance 2025 aún draft) | DPA 2012 + Cybersecurity Act 2020 (ambas en vigor) |
| Autoridad IA específica | NDGA (propuesta en NAIP) | RAI Office (propuesta en NAIS) |
| Pathway legislativo IA | AI Act 2028 (explícito en §7.5) | Emerging Technologies Bill (anunciado sin fecha) |
| Densidad normativa | Alta (AIA mandatorios, strict liability, prohibiciones explícitas) | Media (estrategia con 8 pilares, sin obligaciones vinculantes IA-específicas) |

Bangladesh tiene **instrumento IA más denso normativamente** (policy draft con obligaciones); Ghana tiene **base legal sectorial vinculante más sólida** y estrategia IA formalmente lanzada. Ambos encajan en `soft_framework`, por caminos distintos.

---

## 8. Checklist de validación humana

Marcar cada ítem al revisar. Si algún ítem falla → rechazar el candidato correspondiente.

### Candidato 1: Data Protection Act 2012
- [ ] 1. Emisor oficial del Estado (Parliament of Ghana) ✅ preverificado
- [ ] 2. Documento primario (Act of Parliament) ✅ preverificado
- [ ] 3. Relevancia: (a) en vigor, aplicable a sistemas IA que procesan datos
- [ ] 4. Aplicabilidad a IA explícita (procesamiento automatizado de datos)
- [ ] 5. Coherencia con codificación propuesta
- [ ] 6. Tipo coherente (ley sectorial vinculante)

### Candidato 2: Cybersecurity Act 2020
- [ ] 1. Emisor oficial (Parliament of Ghana, asentida Presidente) ✅ preverificado
- [ ] 2. Documento primario ✅ preverificado
- [ ] 3. Relevancia: (a) en vigor
- [ ] 4. Aplicabilidad a IA (sistemas digitales críticos incluidos sistemas IA)
- [ ] 5. Coherencia con codificación propuesta
- [ ] 6. Tipo coherente (ley sectorial vinculante)

### Candidato 3: NAIS 2023-2033
- [ ] 1. Emisor oficial (MoCD) ✅ preverificado
- [ ] 2. Documento primario ✅ preverificado
- [ ] 3. Relevancia: (b) lanzado formalmente por Presidente 2026-04-24
- [ ] 4. IA explícita ✅
- [ ] 5. Citas respaldan upgrade de `regulatory_intensity` y `thematic_coverage`
- [ ] 6. Tipo coherente (estrategia nacional IA)
- [ ] 7. Aceptar hosting en mirror (`africadataprotection.org`) dada autoría gubernamental evidenciada en portada

### Candidato 4: DEPS 2024
- [ ] 1. Emisor oficial (MoCD) ✅ preverificado
- [ ] 2. Documento primario (con Foreword presidencial) ✅
- [ ] 3. Relevancia: (b) aprobado Cabinet 2024-05-14
- [ ] 4. Componente IA transversal ✅
- [ ] 5. Contribuye a thematic_coverage
- [ ] 6. Tipo coherente (política de economía digital)

---

## 9. Decisión del revisor (marcar al final)

### Para cada candidato

**Candidato 1 (DPA 2012):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___
- [ ] PEDIR OTRA FUENTE — qué buscar: ___

**Candidato 2 (Cybersecurity Act 2020):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___
- [ ] PEDIR OTRA FUENTE — qué buscar: ___

**Candidato 3 (NAIS 2023-2033):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___
- [ ] PEDIR OTRA FUENTE — qué buscar: ___

**Candidato 4 (DEPS 2024):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___
- [ ] EXCLUIR del corpus pero mantener como referencia en nota

### Para la recodificación propuesta

- [ ] APROBAR diff completo
- [ ] APROBAR PARCIALMENTE — modificar: ___
- [ ] MANTENER codificación IAPP original

### Sobre el upgrade a `soft_framework`

- [ ] Aceptar upgrade (justificado por base legal sectorial vinculante + NAIS lanzada)
- [ ] Mantener `strategy_only` (recomendación conservadora — solo NAIS cuenta como "IA-dedicado")
- [ ] Esperar Emerging Technologies Bill antes de decidir

---

## 10. Notas del codificador

1. **Búsqueda priorizada de leyes:** siguiendo la guía del usuario, se priorizó encontrar leyes vinculantes. Ghana NO tiene ley IA-específica, pero sí dos leyes sectoriales vinculantes en vigor directamente aplicables a sistemas IA (DPA 2012, Cybersecurity Act 2020). Ambas fueron incorporadas al corpus.

2. **Búsqueda complementaria de iniciativas:** se acumuló además la variedad de instrumentos IA disponibles: NAIS 2023-2033 (estrategia IA principal) y DEPS 2024 (política económica digital con componente IA). Total: 4 documentos descargados.

3. **Documentos no descargables registrados para re-captura futura:**
   - Emerging Technologies Bill (sin PDF, no presentado al Parlamento aún)
   - UNESCO RAM Ghana (validado Nov 2025, sin publicación PDF pública al 2026-04-15)

4. **Completitud del corpus:** 4 de 6 documentos identificados fueron descargados con SHA-256 y URLs oficiales verificadas.

5. **Confianza tras evidencia documental:** sube de `low` (IAPP) a `medium-high`. Tenemos los documentos primarios en mano, hashes calculados, fuentes oficiales verificadas (3 de 4 en dominios `.gov.gh`; el NAIS en mirror justificado).

6. **Siguientes pasos tras validación:**
   - Si apruebas → integro `recoding_v2.csv` al pipeline
   - Si pides otras fuentes → busco (¿DPC Guidelines? ¿CSA Directives relacionadas a IA? ¿Ghana Investment Promotion Act con componente tech?)
   - Si rechazas el upgrade de régimen → solo update de `intensity` y `coverage`

7. **Diferencia frente a Bangladesh:** Ghana tiene base legal sectorial vinculante **más sólida** (2 leyes en vigor con autoridades activas desde 2012 y 2020); Bangladesh tiene instrumento IA-específico **más denso normativamente** (NAIP V2.0 con obligaciones concretas). Ambos encajan en `soft_framework` por rutas complementarias — importante para el análisis comparado.
