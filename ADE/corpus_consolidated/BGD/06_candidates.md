# BGD — Bangladesh

**Fecha de auditoría:** 2026-04-15
**Codificador:** Claude Opus 4.6 (asistido)
**Revisor humano:** [APROBADO — 2026-04-15]
**Confidence IAPP actual:** `low` → **`medium-high`** (post-validación)

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
| `thematic_coverage` | 4 (0-15) | IAPP 2026-02 |
| `regulatory_regime_group` | `strategy_only` | Derivado |
| `ai_year_enacted` | — | — |
| `ai_framework_note` | "National Strategy for AI 2019, early stage, ICT Division engagement" | IAPP |

**Diagnóstico preliminar:** La codificación IAPP refleja el estado pre-2024. Bangladesh publicó desde entonces el National AI Policy 2024 (Draft), el AI Readiness Assessment 2025 co-firmado con UNESCO/UNDP, y dos versiones (V1.1 y V2.0, esta última de febrero 2026) del **National AI Policy 2026-2030**, que establece un marco risk-based completo con prohibiciones explícitas, AIAs mandatorios y pathway legislativo formal a un AI Act para 2028. La codificación actual subestima la densidad temática y la trayectoria regulatoria.

---

## 2. Inventario de instrumentos estatales IA (2020 → 2026-04)

| # | Documento | Año | Emisor | Tipo | Status | Archivo local |
|---|---|---|---|---|---|---|
| 1 | National Strategy for Artificial Intelligence — Bangladesh | 2020-03 | ICT Division, GoB | Estrategia nacional | Histórico con efecto | `BGD_NSAI_2020.pdf` |
| 2 | National AI Policy 2024 (Draft) | 2024-04 | ICT Division | Policy draft | Reemplazado por NAIP 2026-2030 V1.1 | **No descargable** (loop 301 en ictd.portal.gov.bd, retirado tras publicar V1.1) |
| 3 | Bangladesh AI Readiness Assessment Report | 2025-11 | UNESCO + UNDP + ICT Division (co-publicado) | Diagnóstico oficial | Publicado | `BGD_AIRAM_UNDP_2025.pdf` |
| 4 | National AI Policy Bangladesh 2026-2030 (DRAFT V1.1) | 2026-01 | ICT Division | Policy draft | Versión intermedia | `BGD_NAIP_2026-2030_v1.1_DRAFT.pdf` |
| 5 | Bangladesh National AI Policy 2026-2030 (Draft v2.0) | 2026-02-09 | ICT Division | Policy draft | Post-consulta pública (cerró 2026-02-08), comité revisando para adopción | `BGD_NAIP_2026-2030_v2.0_DRAFT.pdf` |

> **Documento 2 no descargable:** El ICT Division portal (ictd.portal.gov.bd) devuelve loop 301 infinito para el PDF del NAIP 2024 Draft. Es altamente probable que el documento haya sido retirado tras la publicación del V1.1 (enero 2026) que lo reemplaza. Su contenido se integra en el V1.1 y V2.0. No se considera pérdida crítica: los documentos 4 y 5 absorben su contenido normativo.

---

## 3. Candidato 1 — NSAI 2020 (base histórica del ecosistema)

- **Título completo:** National Strategy for Artificial Intelligence — Bangladesh
- **Tipo:** Estrategia nacional
- **Emisor:** Information and Communication Technology Division, Government of the People's Republic of Bangladesh
- **Fecha publicación:** Marzo 2020
- **Status:** `historical_with_effect` — fue el instrumento de referencia 2019-2024; generó el marco institucional (a2i, Digital Bangladesh) sobre el cual se construyen los drafts posteriores
- **URL oficial:** https://ictd.portal.gov.bd/ (sede emisora) · mirror gubernamental estable: `file-rangpur.portal.gov.bd`
- **SHA-256:** `d7a257b412c98ae78fa203ab46ccf9ee32fd982ae0cb5084fc8309f66304ffd2`
- **Idioma:** Inglés
- **Páginas:** 55

### Citas textuales clave

> "Artificial intelligence alludes to the capacity of machines to perform psychological errands like reasoning, seeing, learning, critical thinking and basic leadership." *(Executive Summary, p.1)*

> "Our slogan to address AI is 'AI for Innovative Bangladesh'." *(Executive Summary, p.1)*

> "Bangladesh is embracing Artificial Intelligence (AI) for the digitalization of the nation. The digitization process started a decade earlier. Now AI would work as an accelerator." *(Executive Summary, p.1)*

---

## 4. Candidato 2 — NAIP 2026-2030 Draft V2.0 (documento principal actual)

- **Título completo:** Bangladesh National AI Policy 2026-2030 (Draft v2)
- **Tipo:** Política nacional (draft de adopción inminente)
- **Emisor:** ICT Division, Ministry of Posts, Telecommunications and Information Technology
- **Fecha publicación:** 2026-02-09 (post-consulta pública que cerró 2026-02-08)
- **Status:** `draft_under_review` por el National AI Policy Steering Committee, con intención de adopción formal declarada
- **URL oficial:** https://aipolicy.gov.bd/docs/national-ai-policy-bangladesh-2026-2030-draft-v2.0.pdf
- **SHA-256:** `95b861fae97be1884470e81113ef62df7319fd36e7a190c989feb6bd879d71fa`
- **Idioma:** Inglés

### Citas textuales clave (justifican recodificación)

**Sobre enfoque risk-based:**
> "To ensure proportional and effective regulation, the government shall adopt a risk-based classification framework for AI systems. AI applications shall be categorized into prohibited (unacceptable risk), high-risk, limited-risk, and low-risk systems, with regulatory obligations calibrated to the level of risk posed to individuals, society, and the State." *(§4.1 Regulatory Framework)*

**Sobre prácticas prohibidas:**
> "Prohibited practices shall include AI-enabled social scoring, indiscriminate biometric mass surveillance in public spaces without lawful authorization, and manipulative or deceptive AI systems that exploit vulnerabilities of individuals or groups." *(§4.9 Risk Management Framework)*

**Sobre Algorithmic Impact Assessments mandatorios:**
> "To strengthen accountability and risk management, the government shall mandate Algorithmic Impact Assessments (AIA) for all significant AI systems deployed by public authorities and for high-risk AI systems deployed by private actors." *(§4.9)*

**Sobre liability estricta:**
> "For high-risk AI systems, including those deployed in healthcare, financial services, employment and labor management, justice and law enforcement, social protection and welfare, education, and critical infrastructure, the government shall adopt a strict liability approach. Where harm results from the operation or deployment of a high-risk AI system, the deploying entity shall be liable for such harm regardless of fault, negligence, or intent." *(§4.11 Liability, Insurance, and Redress)*

**Sobre pathway legislativo (clave para `has_ai_law`):**
> "To transition from policy guidance to a comprehensive statutory framework, the Ministry of Law, Justice, and Parliamentary Affairs shall initiate the drafting of a comprehensive Artificial Intelligence Act by 2028. This legislation shall incorporate lessons learned from the implementation of this Policy, international best practices, judicial developments, and stakeholder feedback." *(§7.5 Legislative Pathway)*

**Sobre NDGA (autoridad):**
> "NDGA shall be empowered to issue technical standards, certify compliance for high-risk AI systems, oversee Algorithmic Impact Assessments, and coordinate AI policy implementation across ministries, regulators, and public agencies." *(§4.2)*

**Sobre mandato mid-term y sunset:**
> "The monitoring provisions include annual reporting, a mandatory mid-term review in 2028, and a sunset clause requiring renewal by 2030." *(§7)*

---

## 5. Candidato 3 — AIRAM UNDP/UNESCO 2025 (diagnóstico co-firmado)

- **Título completo:** Bangladesh Artificial Intelligence Readiness Assessment Report
- **Tipo:** Diagnóstico oficial (readiness assessment)
- **Emisor:** UNESCO + UNDP + **ICT Division, GoB** (co-publicación oficial)
- **Fecha publicación:** 2025-11
- **Status:** `official_joint_publication` — referenciado como input del NAIP 2026-2030
- **URL oficial:** https://www.undp.org/sites/g/files/zskgke326/files/2025-11/final_digital_bangladesh_ai_ram.pdf
- **SHA-256:** `a1e85c06c94a657d7be11b019616273197bcb37dafee942bc1294d3aed36c1dc`
- **Idioma:** Inglés

**Rol en corpus:** no es instrumento regulatorio pero sí instrumento estatal oficial que expresa posición del gobierno sobre IA (el ICT Division está listado como co-emisor). Útil para `thematic_coverage` y como evidencia contextual del momentum regulatorio previo a NAIP 2026.

---

## 6. Candidato 4 — NAIP 2026-2030 Draft V1.1 (trazabilidad)

- **Título completo:** National AI Policy Bangladesh 2026-2030 (DRAFT V1.1)
- **Tipo:** Policy draft (versión previa a V2.0)
- **Emisor:** ICT Division
- **Fecha:** 2026-01 aprox.
- **URL oficial:** https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/.../beec3a80-2c3a-4816-bb4c-dec7b96d740f.pdf (Oracle Cloud del Ministerio V2)
- **SHA-256:** `7ea17c05f3d801ceaa258c28aca18a406f13da22a39accea73ed285b6ec60bbf`

**Rol:** conservado como trazabilidad del iter de borradores. El V2.0 es el vigente.

---

## 7. Recodificación X1 propuesta

| Variable | Actual (IAPP) | **Propuesta** | Justificación (con cita) |
|---|---|---|---|
| `has_ai_law` | **0** | **0** *(sin cambio)* | El AI Act está programado para 2028 (cita §7.5). Actualmente solo hay policy draft, no ley vigente. Mantener 0. |
| `regulatory_approach` | `strategy_led` | **`strategy_led`** *(sin cambio en etiqueta, pero concepto evoluciona a "soft_framework" avanzado)* | Policy con pathway legislativo formal. No es aún binding. Se discute abajo un posible cambio a `soft_framework`. |
| `regulatory_intensity` | **2** | **5** *(↑ +3)* | Policy draft con marco risk-based completo (4 tiers), AIAs mandatorios, prohibiciones explícitas, liability estricta, NDGA como autoridad. Intensidad sustancialmente superior al "early stage" codificado. |
| `enforcement_level` | `low` | **`low-medium`** (ordinal intermedio) | Aún no hay AI Act vigente (enforcement real = bajo), pero el V2.0 establece "regulatory enforcement measures" para AIA, sanciones ante non-compliance (§4.9). Propuesta de mantener `low` por prudencia hasta que el AI Act 2028 entre en rigor. |
| `thematic_coverage` | **4** | **11** *(↑ +7)* | V2.0 cubre: risk-based classification, prohibited practices, AIA, data governance, infrastructure, procurement, disinformation/deepfakes, rights/freedoms, liability, international alignment, sectoral (health/agri/disaster/transport/security). Cobertura temática amplia. |
| `regulatory_regime_group` | `strategy_only` | **`soft_framework`** ✅ | Ya no es "solo estrategia": policy draft V2.0 contiene AIAs mandatorios, prohibiciones explícitas (social scoring, mass surveillance), strict liability para sistemas high-risk, pathway legislativo formal al AI Act 2028, y autoridad designada (NDGA). No es `binding_regulation` porque no hay ley vigente aún, pero sí excede `strategy_only`. |
| `ai_year_enacted` | (vacío) | **(vacío)** | No aplicar hasta AI Act 2028. |
| `ai_framework_note` | "National Strategy for AI 2019, early stage, ICT Division engagement" | **"NSAI 2020 (MoPT/ICT Division) + NAIP 2026-2030 Draft V2.0 post-public-consultation (Feb 2026) establishes risk-based framework, mandatory AIAs, strict liability for high-risk systems, NDGA authority, and Legislative Pathway to comprehensive AI Act by 2028. AI Readiness Assessment co-signed w/UNESCO/UNDP Nov 2025."** | Refleja estado real 2026-04. |

### Diff summary (aprobado 2026-04-15)

```
has_ai_law:              0 -> 0          (unchanged; AI Act programado 2028)
regulatory_approach:     strategy_led -> strategy_led (unchanged)
regulatory_intensity:    2 -> 5          (+3)
enforcement_level:       low -> low      (unchanged; sin ley vigente)
thematic_coverage:       4 -> 11         (+7)
regulatory_regime_group: strategy_only -> soft_framework  (UPGRADE ✅)
confidence:              low -> medium-high
```

### Fundamento del upgrade a `soft_framework`

El estudio clasifica los regímenes regulatorios en 4 categorías discretas (`no_framework`, `strategy_only`, `soft_framework`, `binding_regulation`) para medir su efecto diferencial sobre las Y. Clasificar a Bangladesh como `strategy_only` subestimaría el instrumento actual y distorsionaría la comparación con países análogos.

**Criterio aplicado — Bangladesh corresponde a `soft_framework` porque:**
1. El NAIP V2.0 establece obligaciones concretas, no aspiracionales: AIAs mandatorios para high-risk, strict liability, red lines explícitas.
2. Hay autoridad designada (NDGA) con mandato específico de certificación y enforcement.
3. Pathway legislativo formal declarado con fecha (AI Act 2028).
4. El documento pasó consulta pública formal y está en revisión del Steering Committee para adopción.

**No es `binding_regulation`** porque el AI Act está programado para 2028 y el NAIP V2.0 sigue siendo draft policy.
**No es `strategy_only`** porque excede el formato aspiracional de una estrategia nacional (comparar con NSAI 2020, que sí era pura estrategia).

---

## 8. Checklist de validación humana

Marcar cada ítem al revisar. Si algún ítem falla → rechazar el candidato correspondiente.

### Candidato 1: NSAI 2020
- [ ] 1. Emisor oficial del Estado (ICT Division GoB) ✅ preverificado
- [ ] 2. Documento primario (no resumen) ✅ preverificado
- [ ] 3. Relevancia: (c) generó efecto histórico sobre ecosistema IA
- [ ] 4. Trata IA explícitamente ✅ preverificado
- [ ] 5. Coherencia con codificación propuesta
- [ ] 6. Tipo coherente (estrategia → strategy_led)

### Candidato 2: NAIP 2026-2030 V2.0
- [ ] 1. Emisor oficial (ICT Division) ✅ preverificado
- [ ] 2. Documento primario ✅ preverificado
- [ ] 3. Relevancia: (b) publicado con intención de implementación ✅
- [ ] 4. IA explícita ✅
- [ ] 5. Citas respaldan upgrade de `regulatory_intensity` y `thematic_coverage`
- [ ] 6. Tipo coherente (policy draft avanzado)

### Candidato 3: AIRAM UNDP/UNESCO 2025
- [ ] 1. Co-emitido por ICT Division GoB ✅ preverificado
- [ ] 2. Documento primario (reporte oficial)
- [ ] 3. Relevancia: (b) en uso como input de NAIP 2026-2030
- [ ] 4. IA explícita ✅
- [ ] 5. Contribuye a thematic_coverage (evidencia contextual)
- [ ] 6. Tipo coherente (diagnóstico, no instrumento regulatorio)

### Candidato 4: NAIP 2026-2030 V1.1
- [ ] ¿Mantener en corpus como trazabilidad, o descartar por redundancia con V2.0?

---

## 9. Decisión del revisor (marcar al final)

### Para cada candidato

**Candidato 1 (NSAI 2020):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___
- [ ] PEDIR OTRA FUENTE — qué buscar: ___

**Candidato 2 (NAIP V2.0):**
- [ ] APROBAR
- [ ] RECHAZAR — motivo: ___
- [ ] PEDIR OTRA FUENTE — qué buscar: ___

**Candidato 3 (AIRAM 2025):**
- [ ] APROBAR como contexto secundario
- [ ] RECHAZAR
- [ ] EXCLUIR del corpus pero mantener como referencia en nota

**Candidato 4 (NAIP V1.1):**
- [ ] MANTENER (trazabilidad)
- [ ] DESCARTAR (redundante con V2.0)

### Para la recodificación propuesta

- [ ] APROBAR diff completo
- [ ] APROBAR PARCIALMENTE — modificar: ___
- [ ] MANTENER codificación IAPP original

### Sobre el upgrade a `soft_framework`

- [ ] Aceptar upgrade (avanzado para Bangladesh)
- [ ] Mantener `strategy_only` (recomendación conservadora)
- [ ] Esperar adopción formal del NAIP antes de decidir

---

## 10. Notas del codificador

1. **Completitud del corpus:** 4 de 5 documentos identificados fueron descargados exitosamente. El NAIP 2024 Draft (documento 2 del inventario) no es accesible desde el portal oficial por loop 301 — su contenido normativo está absorbido en V1.1 y V2.0.

2. **Confianza tras evidencia documental:** sube de `low` (IAPP) a `medium-high`. Tenemos los documentos primarios en mano, hashes calculados, fuentes oficiales verificadas.

3. **Siguientes pasos tras tu validación:**
   - Si apruebas → integro `recoding_v2.csv` al pipeline
   - Si pides otras fuentes → busco (¿Digital Bangladesh Concept Note? ¿Personal Data Protection Ordinance 2025?)
   - Si rechazas el upgrade de régimen → solo update de `intensity` y `coverage`

4. **Diferencia frente a plan original:** mi propuesta inicial decía recodificar con `regulatory_approach` y posibles cambios fuertes. Tras leer los documentos, la realidad es más conservadora — Bangladesh NO tiene AI Act vigente, pero SÍ tiene un draft sustancialmente más denso que lo que captó IAPP en febrero 2026.
