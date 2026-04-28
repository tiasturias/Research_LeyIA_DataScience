# SGP — Singapur

**Fecha de auditoría:** 2026-04-15
**Codificador:** Claude Opus 4.6 (asistido)
**Revisor humano:** [PENDIENTE]
**Confidence IAPP actual:** `(vacío)` → **`high`** (post-validación propuesta)

**Fuentes bibliográficas formales:** ver [SOURCES.md](SOURCES.md) (citas APA 7, URLs primarias, hashes, evidencia de oficialidad)
**Metadatos de trazabilidad:** ver [manifest.csv](manifest.csv)

---

## 1. Codificación actual (IAPP / OECD base — vigente en `x1_master.csv`)

| Variable | Valor actual | Fuente |
|---|---|---|
| `has_ai_law` | 0 | IAPP 2026-02 |
| `regulatory_approach` | `strategy_led` | IAPP 2026-02 |
| `regulatory_intensity` | 6 (0-10) | IAPP 2026-02 |
| `enforcement_level` | `medium` | IAPP 2026-02 |
| `thematic_coverage` | 12 (0-15) | IAPP 2026-02 |
| `regulatory_regime_group` | `strategy_only` (derivado) | Derivado — **inconsistente con la evidencia** |
| `ai_year_enacted` | — | — |
| `ai_framework_note` | "National AI Strategy updated 2023, Model AI Governance Framework (voluntary), AI Verify toolkit, numerous sector frameworks, AI Safety Institute, GenAI Sandbox" | IAPP |

**Diagnóstico preliminar:** La nota IAPP ya reconoce densidad alta (`intensity=6`, `coverage=12`, `enforcement=medium`), pero la **clasificación derivada de régimen como `strategy_only`** es incoherente con esos valores. Singapur tiene la arquitectura soft-law más densa del mundo + dos leyes sectoriales vinculantes robustas con autoridades activas (PDPC, CSA, MAS). La corrección es subir a `soft_framework`. No hay base para `binding_regulation` porque la política declarada es explícitamente **no promulgar una ley IA horizontal**.

---

## 2. Inventario de instrumentos estatales IA (2012 → 2026-04)

| # | Documento | Año | Emisor | Tipo | Status | Archivo local |
|---|---|---|---|---|---|---|
| 1 | Personal Data Protection Act 2012 (+ Amendment 2020) | 2012 / 2020 | Parliament of Singapore | Ley vinculante sectorial | En vigor | `SGP_PDPA_2012.pdf` |
| 2 | Cybersecurity Act 2018 | 2018 | Parliament of Singapore | Ley vinculante sectorial | En vigor | `SGP_CybersecurityAct_2018.pdf` |
| 3 | MAS FEAT Principles | 2018-11 | Monetary Authority of Singapore | Soft-framework sectorial (finanzas) | En uso | `SGP_MAS_FEAT_2018.pdf` |
| 4 | Model AI Governance Framework (Second Edition) | 2020-01 | PDPC + IMDA | Soft-framework horizontal | En uso | `SGP_MGF_2ndEd_2020.pdf` |
| 5 | National AI Strategy 2.0 | 2023-12 | SNDGO / Smart Nation Group | Estrategia nacional IA | En vigor | `SGP_NAIS2.0_2023.pdf` |
| 6 | Model AI Governance Framework for Generative AI | 2024-05 | IMDA + AI Verify Foundation | Soft-framework horizontal | En uso | `SGP_MGF_GenAI_2024.pdf` |
| 7 | Model AI Governance Framework for Agentic AI | 2026-01 | IMDA | Soft-framework horizontal | En uso | `SGP_MGF_AgenticAI_2026.pdf` |
| 8 | MAS Consultation Paper on AI Risk Management Guidelines | 2025 | MAS | Consulta pública | En consulta | **No incluido** (consultation paper, no final) |
| 9 | MinLaw Guide for Using Generative AI in the Legal Sector | 2026-03 | Ministry of Law | Guía sectorial | En uso | **No incluido** (muy específico al sector legal) |
| 10 | AI Verify Toolkit | 2022+ | IMDA + AI Verify Foundation | Toolkit software | En uso | **No aplicable** (software, no documento constitutivo) |

---

## 3. Candidato 1 — PDPA 2012 (+ Amendment 2020) [LEY VINCULANTE]

- **Título:** Personal Data Protection Act 2012 (consolidated, incl. Amendment Act 40/2020)
- **Emisor:** Parliament of the Republic of Singapore
- **Status:** En vigor. Enmendado sustantivamente en 2020.
- **URL oficial:** https://sso.agc.gov.sg/Act/PDPA2012?ViewType=Pdf (Singapore Statutes Online / Attorney-General's Chambers)
- **SHA-256:** `0e996ae99839f19e27f97024692e090197cf44a14709f93cd74a7d2efc1476db`

### Rol en corpus IA
- Establece la **Personal Data Protection Commission (PDPC)** como autoridad regulatoria de datos.
- Enmienda 2020 introdujo: data portability right, **mandatory breach notification**, enhanced consent framework — todos impactan directamente pipelines de training data IA.
- La PDPC es co-emisora del Model AI Governance Framework (documento 4), lo que hace que el soft-framework horizontal tenga **respaldo directo de autoridad vinculante**.

---

## 4. Candidato 2 — Cybersecurity Act 2018 [LEY VINCULANTE]

- **Título:** Cybersecurity Act 2018 (No. 9 of 2018)
- **Emisor:** Parliament of Singapore
- **Aprobación:** Passed 2018-02-05; en vigor 2018-08-31.
- **URL oficial:** https://sso.agc.gov.sg/Act/CA2018?ViewType=Pdf
- **SHA-256:** `61d393108172968b0862eada75c65902c8dd7e2b38868da736809fc3d6ebcb01`

### Rol en corpus IA
- Establece la **Cyber Security Agency (CSA)** y el régimen de Critical Information Infrastructure (CII).
- Aplicable a sistemas IA desplegados en sectores CII (banca, salud, energía, telcos, transporte, servicios gubernamentales).
- Dispara obligaciones de reporte de incidentes, audits de seguridad, licensing de proveedores — todo aplicable al stack IA de sistemas críticos.

---

## 5. Candidato 3 — MAS FEAT Principles 2018 [SOFT-FRAMEWORK SECTORIAL]

- **Título:** Principles to Promote Fairness, Ethics, Accountability and Transparency (FEAT) in the Use of AI and Data Analytics in Singapore's Financial Sector
- **Emisor:** Monetary Authority of Singapore (banco central + regulador financiero integrado)
- **Fecha:** 2018-11-12
- **URL oficial:** https://www.mas.gov.sg/-/media/MAS/News%20and%20Publications/Monographs%20and%20Information%20Papers/FEAT%20Principles%20Final.pdf
- **SHA-256:** `3934194d3d17a435124f514583c337432ce002b9c6fbef736d4f33849cf3d299`

### Citas textuales clave

**Sobre autoridad detrás del instrumento:**
> "This document has been prepared by the Monetary Authority of Singapore (MAS) to guide firms offering financial products and services on the responsible use of AI and data analytics (AIDA), to strengthen internal governance around data management and use."

**Principios fundacionales (base de todo el discurso global regulatorio de IA en finanzas 2018-2026):**
> "Fairness: Individuals or groups of individuals are not systematically disadvantaged through AIDA-driven decisions... Ethics: AIDA-driven decisions are held to at least the same ethical standards as human driven decisions... Accountability: Use of AIDA in AIDA-driven decision-making is approved by an appropriate internal authority... Transparency: Use of AIDA is proactively disclosed to data subjects as part of general communication."

### Rol en corpus
- Primer instrumento regulatorio global de IA en finanzas (noviembre 2018, antes que la UE, OECD AI Principles o NIST AI RMF).
- Base del **Veritas Initiative** (MAS + consorcio industrial) que en 2022 publicó assessment methodologies operacionales.
- Aunque "non-binding", son **expectativas supervisorias** del MAS sobre instituciones reguladas — en la práctica vinculantes vía la relación supervisor-supervisado.

---

## 6. Candidato 4 — Model AI Governance Framework (Second Edition, 2020)

- **Título:** Model Artificial Intelligence Governance Framework (Second Edition)
- **Emisor:** PDPC + IMDA (ambas autoridades gubernamentales oficiales)
- **Fecha:** 2020-01-21 (lanzado en WEF Davos 2020)
- **URL oficial:** https://www.imda.gov.sg/-/media/imda/files/infocomm-media-landscape/sg-digital/tech-pillars/artificial-intelligence/second-edition-of-the-model-ai-governance-framework.pdf
- **SHA-256:** `2eb76732a9d2f58b97b006a72136676b448c84b1406388fd7ec68e27f2afddb4`

### Rol en corpus
- Framework voluntario estándar para IA tradicional. La primera edición (2019) fue pionera global.
- Cubre 4 áreas: internal governance structures, determining level of human involvement, operations management, stakeholder interaction.
- Base conceptual del **AI Verify toolkit** (lanzado 2022) — instrumento operacional para certificación voluntaria.
- Acompañado por ISAGO (Implementation and Self-Assessment Guide) y Compendium of Use Cases.

---

## 7. Candidato 5 — National AI Strategy 2.0 (2023) [ESTRATEGIA NACIONAL]

- **Título:** National AI Strategy 2.0: AI for the Public Good, for Singapore and the World
- **Emisor:** Smart Nation and Digital Government Office (SNDGO) + Smart Nation Group, Government of Singapore
- **Lanzamiento:** 2023-12-04 por Deputy Prime Minister Lawrence Wong
- **URL oficial:** https://file.go.gov.sg/nais2023.pdf
- **SHA-256:** `34317684b098c43d7b063ec3a9c00ec0fc7275dd0bc272dd82213dbf4faa0316`

### Citas textuales clave

**Sobre sistemas:**
> "NAIS 2.0 will be driven by 3 Systems — Activity Drivers, People & Communities, and Infrastructure & Environment."

**Sobre sectores prioritarios:**
> "Five priority sectors: manufacturing, financial services, transport & logistics, biomedical sciences, public services."

**Sobre governance:**
> "Maintain a trusted environment through our Model AI Governance Framework, AI Verify, and active participation in international AI governance fora."

### Rol en corpus
- Instrumento declarativo — define dirección estratégica nacional para la próxima década.
- Explícitamente referencia el MGF (documento 4) y AI Verify como pilar de gobernanza, consolidando el approach framework-led.

---

## 8. Candidato 6 — MGF for Generative AI (2024)

- **Título:** Model AI Governance Framework for Generative AI
- **Emisor:** IMDA + AI Verify Foundation
- **Fecha:** 2024-05-30 (post-consulta pública Ene-Mar 2024 con 70+ responses)
- **URL oficial:** https://aiverifyfoundation.sg/wp-content/uploads/2024/05/Model-AI-Governance-Framework-for-Generative-AI-May-2024-1-1.pdf
- **SHA-256:** `01ab29b1e24e3d832a1087bd993d9bcfd5170d26ea0c7512d1c8303cd5dc7fb6`

### Rol en corpus
- Extiende el MGF 2020 a GenAI.
- 9 dimensiones: accountability, data, trusted development and deployment, incident reporting, testing and assurance, security, content provenance, safety and alignment R&D, AI for public good.
- Co-desarrollado con tech MNCs (Microsoft, OpenAI, Google), auditoras (KPMG, EY), agencias gubernamentales extranjeras (US Dept of Commerce) — evidencia de legitimidad internacional.

---

## 9. Candidato 7 — MGF for Agentic AI (2026)

- **Título:** Model AI Governance Framework for Agentic AI
- **Emisor:** IMDA
- **Fecha:** 2026-01-22 (lanzado en WEF Davos 2026 por Minister for Digital Development and Information)
- **URL oficial:** https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
- **SHA-256:** `b84c8c94f6392cf2be474cfd6e07f7af213874fa10ac26ebd5249f6df4aeef7b`

### Rol en corpus
- **Primer framework global de governance específicamente para agentic AI** (AI agents con autonomous planning, reasoning and action).
- 4 dimensiones: bounding risks upfront, human accountability, technical controls, end-user responsibility.
- Living document, feedback loop abierto — Singapur se posiciona como laboratorio regulatorio global.
- Evidencia de que el soft-framework de Singapur **sigue densificándose en 2026** (relevante para `confidence` y para el análisis longitudinal).

---

## 10. Recodificación X1 propuesta

| Variable | Actual (IAPP) | **Propuesta** | Justificación (con cita) |
|---|---|---|---|
| `has_ai_law` | **0** | **0** *(sin cambio)* | Singapur NO tiene ley IA-específica vinculante. Posición declarada: "principles-based / framework-led, not prescriptive legislation" (IMDA 2026). PDPA y Cybersecurity Act son sectoriales, no IA-específicas. |
| `regulatory_approach` | `strategy_led` | **`framework_led`** *(etiqueta más precisa — a confirmar con el esquema de categorías del estudio)* | El instrumento dominante no es la estrategia NAIS 2.0 sino el ecosistema MGF + AI Verify + FEAT. Si el esquema del estudio solo admite `strategy_led / regulation_led / binding`, mantener `strategy_led`. |
| `regulatory_intensity` | **6** | **7** *(↑ +1)* | MGF Agentic AI 2026 añade dimensión no capturada en febrero 2026 por IAPP; profundización de MAS hacia guidelines supervisorias via consultation 2025; MinLaw Guide GenAI en legal sector. Justifica upgrade marginal. |
| `enforcement_level` | `medium` | **`medium-high`** *(↑ marginal)* | PDPC y CSA tienen poderes sancionatorios reales y activos. MAS tiene autoridad supervisoria plena sobre instituciones financieras que operan IA. FEAT + Veritas crean trazabilidad supervisoria concreta. Aunque no hay enforcement IA-específico, el perímetro legal es robusto. |
| `thematic_coverage` | **12** | **13** *(↑ +1)* | Añadir: agentic AI governance (dimensión nueva 2026), sector-specific GenAI guidance (legal sector 2026). Casi saturación (13/15). |
| `regulatory_regime_group` | `strategy_only` *(derivación incoherente con IAPP intensity=6)* | **`soft_framework`** ✅ **(UPGRADE/CORRECCIÓN)** | Clasificar a Singapur como `strategy_only` es manifiestamente erróneo dada (a) la densidad soft-law mundialmente líder, (b) la existencia de dos leyes sectoriales vinculantes con autoridades activas, (c) sector-specific binding expectations vía MAS. NO es `binding_regulation` porque no hay ley IA horizontal. |
| `ai_year_enacted` | (vacío) | **(vacío)** | No aplicar — no hay ley IA horizontal. Opcional: documentar 2018 (FEAT) como "first sector-specific AI expectations". |
| `ai_framework_note` | "National AI Strategy updated 2023, Model AI Governance Framework (voluntary), AI Verify toolkit, numerous sector frameworks, AI Safety Institute, GenAI Sandbox" | **"Framework-led approach: no horizontal AI law by policy choice. Binding base: PDPA 2012+2020 (PDPC), Cybersecurity Act 2018 (CSA). Soft-law ecosystem: Model AI Gov Framework 2nd Ed 2020 + GenAI 2024 + Agentic AI 2026 (IMDA), MAS FEAT 2018 (Veritas). NAIS 2.0 2023 strategy. Operational tools: AI Verify, GenAI Sandbox, AI Safety Institute. MAS AI Risk Management Guidelines in consultation 2025."** | Refleja estado real 2026-04. |

### Diff summary (propuesto — pendiente aprobación humana)

```
has_ai_law:              0 -> 0                (unchanged; by policy)
regulatory_approach:     strategy_led -> strategy_led  (unchanged if schema lacks framework_led)
regulatory_intensity:    6 -> 7                (+1)
enforcement_level:       medium -> medium      (unchanged; marginal upgrade suggested)
thematic_coverage:       12 -> 13              (+1)
regulatory_regime_group: strategy_only -> soft_framework   (CORRECTION ✅)
confidence:              (empty) -> high
```

### Fundamento del upgrade a `soft_framework`

**Criterio aplicado — Singapur corresponde claramente a `soft_framework`:**
1. **Base legal sectorial vinculante robusta:** PDPA 2012+2020 + Cybersecurity Act 2018, ambas con autoridades activas (PDPC, CSA) y poderes sancionatorios.
2. **Soft-law horizontal mundialmente pionero:** MGF (2019/2020/2024/2026) es el single-most-cited voluntary AI framework globalmente.
3. **Soft-law sectorial vinculante-en-la-práctica:** FEAT 2018 → Veritas 2022 → MAS AI Risk Management Guidelines (consultation 2025) es un pipeline supervisorio real sobre instituciones financieras.
4. **Autoridades IA específicas designadas:** PDPC es co-autora del MGF; IMDA lidera AI Verify Foundation; AI Safety Institute creada 2024.
5. **Estrategia NAIS 2.0** explícitamente lanzada por Deputy PM (ahora PM) en 2023 — respaldo político al más alto nivel.

**No es `binding_regulation`** porque Singapur ha declarado explícitamente que **no tiene intención de promulgar una ley IA horizontal** y no existe Act of Parliament IA-específico.
**No es `strategy_only`** porque excede ampliamente el formato de sola estrategia — la arquitectura real es estrategia + frameworks + leyes sectoriales vinculantes + autoridades activas.

### Comparación con Bangladesh y Ghana (todos `soft_framework`, rutas distintas)

| Dimensión | Singapore | Bangladesh | Ghana |
|---|---|---|---|
| Instrumento IA principal | MGF ecosystem (MGF 2020/GenAI 2024/Agentic 2026) + NAIS 2.0 | NAIP 2026-2030 Draft V2.0 | NAIS 2023-2033 |
| Leyes sectoriales vinculantes | PDPA 2012+2020 + Cybersecurity Act 2018 (con autoridades 10+ años activas) | — (PDP Ordinance 2025 draft) | DPA 2012 + Cybersecurity Act 2020 |
| Autoridad IA específica | AI Safety Institute + AI Verify Foundation (operativas) | NDGA (propuesta en NAIP) | RAI Office (propuesta en NAIS) |
| Pathway legislativo IA | **Explícitamente no** (policy-led) | AI Act 2028 (explícito) | Emerging Technologies Bill (anunciado) |
| Densidad soft-law | **Máxima global** | Media | Baja-media |
| Enforcement real sobre IA | Alto (via PDPC/CSA/MAS) | Bajo (autoridades proyectadas) | Medio (via DPC/CSA, sin autoridad IA) |

Singapur es el **caso paradigmático de `soft_framework` maduro**: máxima densidad soft-law + base legal sectorial vigente y ejecutiva, deliberadamente sin ley IA horizontal. Bangladesh y Ghana son `soft_framework` en desarrollo; Singapur es `soft_framework` consolidado.

---

## 11. Checklist de validación humana

### Candidato 1: PDPA 2012
- [ ] 1. Emisor oficial (Parliament of Singapore) ✅ preverificado
- [ ] 2. Documento primario (Act of Parliament consolidated) ✅
- [ ] 3. Relevancia: (a) en vigor, aplicable a sistemas IA que procesan datos
- [ ] 4. Aplicabilidad a IA (training data, decisiones automatizadas) ✅
- [ ] 5. Coherencia con codificación propuesta
- [ ] 6. Tipo coherente (ley sectorial vinculante)

### Candidato 2: Cybersecurity Act 2018
- [ ] 1. Emisor oficial (Parliament of Singapore) ✅
- [ ] 2. Documento primario ✅
- [ ] 3. Relevancia: (a) en vigor
- [ ] 4. Aplicabilidad a IA (sistemas críticos digitales) ✅
- [ ] 5. Coherencia con codificación
- [ ] 6. Tipo coherente

### Candidato 3: MAS FEAT 2018
- [ ] 1. Emisor oficial (MAS, regulador financiero) ✅
- [ ] 2. Documento primario ✅
- [ ] 3. Relevancia: (a) en uso supervisorio activo
- [ ] 4. IA explícita ✅
- [ ] 5. Aceptar como "soft-framework sectorial vinculante-en-la-práctica"
- [ ] 6. Tipo coherente

### Candidato 4: MGF 2nd Ed 2020
- [ ] 1. Emisor oficial (PDPC + IMDA) ✅
- [ ] 2. Documento primario ✅
- [ ] 3. Relevancia: (a) en uso
- [ ] 4. IA explícita ✅
- [ ] 5. Contribuye al upgrade
- [ ] 6. Tipo coherente (soft-framework horizontal)

### Candidato 5: NAIS 2.0
- [ ] 1. Emisor oficial (SNDGO) ✅
- [ ] 2. Documento primario ✅
- [ ] 3. Relevancia: (a) en vigor, lanzada por Deputy PM
- [ ] 4. IA explícita ✅
- [ ] 5. Coherente con estrategia nacional
- [ ] 6. Tipo coherente

### Candidato 6: MGF GenAI 2024
- [ ] 1. Emisor oficial (IMDA + AI Verify Foundation) ✅
- [ ] 2. Documento primario ✅
- [ ] 3. Relevancia: (b) publicado post-consulta formal
- [ ] 4. IA explícita ✅
- [ ] 5. Aceptar AI Verify Foundation como emisor gubernamental efectivo (subsidiaria IMDA)
- [ ] 6. Tipo coherente

### Candidato 7: MGF Agentic AI 2026
- [ ] 1. Emisor oficial (IMDA) ✅
- [ ] 2. Documento primario ✅
- [ ] 3. Relevancia: (b) lanzado por Minister en WEF Davos 2026-01-22
- [ ] 4. IA explícita (agentic AI) ✅
- [ ] 5. Evidencia de densificación 2026
- [ ] 6. Tipo coherente

---

## 12. Decisión del revisor (marcar al final)

### Para cada candidato
**1 (PDPA):** [ ] APROBAR [ ] RECHAZAR [ ] PEDIR OTRA FUENTE
**2 (CSA Act):** [ ] APROBAR [ ] RECHAZAR [ ] PEDIR OTRA FUENTE
**3 (FEAT):** [ ] APROBAR [ ] RECHAZAR [ ] PEDIR OTRA FUENTE
**4 (MGF 2020):** [ ] APROBAR [ ] RECHAZAR [ ] PEDIR OTRA FUENTE
**5 (NAIS 2.0):** [ ] APROBAR [ ] RECHAZAR [ ] PEDIR OTRA FUENTE
**6 (MGF GenAI 2024):** [ ] APROBAR [ ] RECHAZAR [ ] PEDIR OTRA FUENTE
**7 (MGF Agentic 2026):** [ ] APROBAR [ ] RECHAZAR [ ] PEDIR OTRA FUENTE

### Para la recodificación propuesta
- [ ] APROBAR diff completo
- [ ] APROBAR PARCIALMENTE — modificar: ___
- [ ] MANTENER codificación IAPP original

### Sobre el upgrade/corrección a `soft_framework`
- [ ] Aceptar corrección (la clasificación `strategy_only` derivada era inconsistente con intensity=6)
- [ ] Mantener `strategy_only` (no recomendado — inconsistente)

### Sobre instrumentos adicionales a buscar (opcional)
- [ ] Incorporar MAS AI Risk Management Guidelines cuando se finalicen post-consulta 2025
- [ ] Incorporar MinLaw Guide for GenAI in Legal Sector (2026-03) como sector-specific
- [ ] No necesario — corpus actual es suficientemente representativo

---

## 13. Notas del codificador

1. **Búsqueda priorizada de leyes:** Singapur NO tiene ley IA-específica (decisión de política explícita). Encontradas 2 leyes vinculantes sectoriales con 10+ años de aplicación activa: PDPA 2012 (con Amendment 2020) y Cybersecurity Act 2018.

2. **Búsqueda complementaria de iniciativas:** 5 instrumentos adicionales descargados para capturar la densidad soft-law mundialmente líder: FEAT 2018 (finanzas), MGF 2020 + MGF GenAI 2024 + MGF Agentic 2026 (horizontal), NAIS 2.0 2023 (estrategia).

3. **Completitud:** 7/7 documentos descargados con HTTP 200 y SHA-256. Todos en dominios oficiales (`sso.agc.gov.sg`, `mas.gov.sg`, `imda.gov.sg`, `go.gov.sg`, `aiverifyfoundation.sg`).

4. **Confidence upgrade:** `(vacío)` → `high`. Singapur es uno de los países más documentados globalmente en materia IA-regulatoria; evidencia primaria abundante y consistente.

5. **Punto frontera del estudio:** Singapur prueba que `has_ai_law=0` NO equivale a `strategy_only`. La clasificación actual de régimen derivada del framework IAPP introduce ruido en el estudio — recomiendo que la re-derivación de `regulatory_regime_group` use la evidencia primaria del corpus, no una regla automática basada solo en `has_ai_law`.

6. **Inconsistencia IAPP detectada:** `regulatory_intensity=6` + `enforcement=medium` + `thematic_coverage=12` son inconsistentes con la derivación `regulatory_regime_group=strategy_only`. La corrección a `soft_framework` es tanto recodificación como **armonización interna** de la variable.

7. **Siguientes pasos tras validación:**
   - Si apruebas → integro al pipeline como caso referencial `soft_framework` consolidado.
   - Si detecto futuros frameworks (MAS final guidelines, sector-specific additions) → re-captura sin perder el histórico.

8. **Relevancia para el estudio LeyIA:** Singapur es el contrafactual clave para Chile. Ambos países tienen altos niveles de desarrollo y adopción IA; Singapur opta por `soft_framework` robusto; Chile está en camino a `binding_regulation` con la Ley 16821-19. El análisis comparado de ecosistemas entre ambos debería ser central en el informe final.
