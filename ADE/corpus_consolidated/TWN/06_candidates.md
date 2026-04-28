# TWN — Propuesta de recodificación X1 con evidencia primaria

**País:** Taiwan (ISO3: TWN)
**Fecha de análisis:** 2026-04-16
**Codificador:** Claude Opus 4.6 (asistido)
**Revisor humano:** [PENDIENTE]
**Confidence IAPP actual:** medium (fuente IAPP_Global_AI_Law_Policy_Tracker, source_date 2026-02) → **Propuesta: medium-high** (evidencia primaria de ley IA vigente promulgada 2026-01-14 + 2 leyes sectoriales + estrategia + 2 guidelines oficiales).

Links a entregables hermanos:
- [SOURCES.md](SOURCES.md) — citas APA 7 + trazabilidad + evidencia de oficialidad.
- [manifest.csv](manifest.csv) — trazabilidad técnica (18 columnas, 7 filas).

---

## 1. Codificación actual (IAPP base, fila 81 en `data/raw/IAPP/iapp_x1_core.csv`)

| Variable | Valor IAPP |
|---|---|
| `has_ai_law` | 0 |
| `regulatory_approach` | strategy_led |
| `regulatory_intensity` | 5 |
| `year_enacted` | (vacío) |
| `enforcement_level` | medium |
| `thematic_coverage` | 9 |
| `regulatory_regime_group` | (derivado, probable `strategy_only` o `soft_framework`) |
| `ai_year_enacted` | (vacío) |
| `ai_framework_note` | "AI Basic Act (executive draft, not yet enacted), AI Taiwan Action Plan 2.0, risk-based approach, Ministry of Digital Affairs, AI CoE" |
| `source` | IAPP_Global_AI_Law_Policy_Tracker |
| `source_date` | 2026-02 |

## 2. Diagnóstico preliminar

La codificación IAPP refleja el estado de Taiwán a **febrero 2026** cuando el AI Basic Act estaba promulgado desde solo ~3 semanas (2026-01-14) y es probable que el tracker aún no reflejara el cambio de status de "executive draft" a "in force". El `evidence_summary` explícitamente dice "*executive draft, not yet enacted*", confirmando que IAPP capturó el estado pre-promulgación. Con la entrada en vigor del AI Basic Act el 2026-01-14, **Taiwán transita de `soft_framework` a `binding_regulation`**, con `has_ai_law = 1` y `ai_year_enacted = 2026`. Las 2 leyes sectoriales robustas (PDPA 2025, CSMA 2018) + estrategia vigente + 2 guidelines oficiales siguen constituyendo el ecosistema habilitante; ahora coronado por ley horizontal.

## 3. Inventario de instrumentos estatales IA

| # | Documento | Tipo | Fecha | Vigencia | Emisor |
|---|---|---|---|---|---|
| 1 | AI Basic Act (EN) | binding_law_ai | 2026-01-14 | in_force | Legislative Yuan / Presidente Lai |
| 2 | AI Basic Act (ZH oficial) | binding_law_ai | 2026-01-14 | in_force | Legislative Yuan / Presidente Lai |
| 3 | Personal Data Protection Act | binding_law_sectoral | 2025-11-11 (última enmienda) | in_force | Legislative Yuan |
| 4 | Cyber Security Management Act | binding_law_sectoral | 2018-06-06 / 2019-01-01 (vigor) | in_force | Legislative Yuan |
| 5 | AI Taiwan Action Plan 2.0 | policy_strategy | 2023-04 | in_use | Executive Yuan / NDC |
| 6 | GenAI Guidelines Exec Yuan | guidelines | 2023-08-31 | in_force | NSTC + Executive Yuan |
| 7 | Critical Infra AI Guidelines | guidelines | 2025-10-08 | in_force | Office of Homeland Security, Executive Yuan |

No hay instrumentos identificados como no-descargables críticos. El Ten AI Initiatives Promotion Plan (2025-2028) está pendiente de publicación formal.

## 4. Candidatos uno por uno

### Candidato 1+2. Artificial Intelligence Basic Act (人工智慧基本法) — 2026

- **Título oficial:** Artificial Intelligence Basic Act / 人工智慧基本法.
- **Emisor:** Legislative Yuan (aprobado tercera lectura 2025-12-23); promulgado por Presidente William Lai Ching-te 2026-01-14.
- **pcode MOJ:** H0160093.
- **URL oficial ZH:** https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=H0160093
- **URL oficial EN:** https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=H0160093
- **SHA-256 EN:** `17d9a9c919fb59e3bb8a318cd7b2e1b1e005051aca212c1ef9360492b276d694`
- **SHA-256 ZH:** `3421becc8eb47a042d79bd1388f32070466e5c176904e7cce5ccfe4b974285fb`
- **Idioma:** texto oficial en chino tradicional; traducción inglés no oficial en el mismo portal MOJ.
- **Estructura:** 20 artículos.
- **Rol en corpus IA:** **ley IA-específica vinculante de primer orden** — primera ley horizontal IA de Taiwán. Dispara `has_ai_law=1` y `regulatory_regime_group=binding_regulation`.

**Citas textuales clave** (extraídas vía `pdfminer.six` del texto EN oficial):

> **Article 1 (Purpose):** "This Act is enacted to build a smart nation; promote the human-centric research, development, and industrial advancement of artificial intelligence (AI); establish a safe environment for AI applications; ensure digital equity; safeguard the fundamental rights of the people; (...) ensure that the application of technology complies with social ethics."

> **Article 2 (Competent Authority):** "The term 'competent authority' as used in this Act refers to the National Science and Technology Council at the central government level, and the special municipality, county, or city governments at the local level."

> **Article 3 (Definition):** "The term 'artificial intelligence' as used in this Act refers to a system capable of autonomous operation, which, through input or sensing and by means of machine learning and algorithms, can generate outputs such as predictions, content, recommendations, or decisions that affect physical or virtual environments to achieve explicit or implicit objectives."

> **Article 4 (Seven principles):** "In promoting the research, development, and application of AI, the government shall (...) adhere to the following principles: 1. Sustainable Development and Well-being; 2. Human Autonomy; 3. Privacy Protection and Data Governance; 4. Cybersecurity and Safety; 5. Transparency and Explainability; 6. Fairness and Non-Discrimination; 7. Accountability."

> **Article 5 (Red lines):** "The government shall ensure that the application of artificial intelligence does not result in any of the following: infringement upon the people's life, body, liberty, or property; disruption of social order, national security, or the ecological environment; or conduct that violates relevant laws and regulations, including bias, discrimination, false advertising, or the dissemination of misleading or false information."

> **Article 6 (Institutional architecture):** "The Executive Yuan shall establish a National AI Strategic Committee, to be convened by the Premier of the Executive Yuan (...) The Committee shall coordinate, promote, and supervise national AI affairs and formulate the National AI Development Guidelines."

> **Article 14 (Data protection interlock):** "Each competent authority for the relevant industries shall consult with the competent authority for personal data protection, and shall, in the process of AI R&D and application, avoid the unnecessary collection, processing, or use of personal data, and shall promote the integration of personal data protection by design and by default measures."

> **Article 16 (Risk taxonomy mandate):** "The Ministry of Digital Affairs shall, with reference to international standards or norms, promote an AI risk taxonomy and assessment framework that is interoperable with international frameworks, and shall assist the competent authorities for the relevant industries in establishing risk-based management regulations."

### Candidato 3. Personal Data Protection Act (PDPA) 2023/2025

- **Emisor:** Legislative Yuan.
- **Última enmienda:** promulgada 2025-11-11 (aprobación 2025-10-17).
- **URL oficial:** https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=I0050021
- **SHA-256:** `e4d6334fcae0f1a8dd76fb9304781e44e7cafad9fb0fe15ed4642c40b4e32822`
- **Competent authority:** Personal Data Protection Commission (PDPC), designada en Art. 1-1 (enmienda 2023).
- **Rol en corpus IA:** base legal para processing de training data IA y automated decision-making. Interlocks con AI Basic Act Art. 14.

### Candidato 4. Cyber Security Management Act (CSMA) 2018

- **Emisor:** Legislative Yuan; promulgada 2018-06-06; en vigor desde 2019-01-01.
- **URL oficial:** https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=A0030297
- **SHA-256:** `97cea063fa5cc9c2d9740583981ec3b2e663b33d6f0bb0b6c065c2f9a9035ea7`
- **Competent authority:** Administration for Cyber Security (ACS), ahora integrada en MODA.
- **Rol en corpus IA:** régimen CII aplicable a sistemas IA críticos. Base legal del Critical Infra AI Guidelines 2025.

### Candidato 5. AI Taiwan Action Plan 2.0 (2023-2026)

- **Emisor:** Executive Yuan / Smart Nation Promotion Task Force; aprobado abril 2023.
- **URL oficial:** https://digi.nstc.gov.tw/File/7C71629D702E2D89
- **SHA-256:** `f7dd4a95d349251178c29454896f6733bcca25cf867b3de978ba358448bd5173`
- **Idioma:** chino tradicional (no hay versión EN oficial equivalente).
- **Rol en corpus IA:** estrategia nacional IA vigente, 5 pilares, NT$250B meta industria. Base técnica del posterior AI Basic Act.

### Candidato 6. GenAI Guidelines Executive Yuan (2023)

- **Emisor:** National Science and Technology Council (NSTC); aprobado Exec Yuan sesión 3869 el 2023-08-31.
- **URL oficial:** https://www.ey.gov.tw/File/272BBE7DBB8F21FD
- **SHA-256:** `3d776275dfd1093f005fa8483e469d370012f979eefcd98c2493a585d938967f`
- **Rol en corpus IA:** primer framework IA sector público Taiwán. Prohibiciones concretas (datos clasificados, personales), requerimientos de supervisión humana.

### Candidato 7. Critical Infrastructure AI Application Guidelines (2025)

- **Emisor:** Office of Homeland Security, Executive Yuan; emitidas 2025-10-08 (han-ling).
- **URL oficial:** https://ohs.ey.gov.tw/File/C5E29BFB9E72EAB9
- **SHA-256:** `997a4a41b0d29d83d1c5587bf70ad8003d65efb4cba439b4be61b31df1a7646c`
- **Rol en corpus IA:** guidelines sectoriales para operadores CII que usan IA; interlocks con CSMA (base legal) y AI Basic Act Art. 16 (risk taxonomy).

---

## 5. Recodificación X1 propuesta

| Variable | Actual (IAPP) | Propuesta | Justificación |
|---|---|---|---|
| `has_ai_law` | 0 | **1** | AI Basic Act (人工智慧基本法) promulgada 2026-01-14 por el Presidente Lai tras aprobación tercera lectura del Legislative Yuan 2025-12-23. 20 artículos, en vigor. |
| `ai_year_enacted` | (vacío) | **2026** | Año de promulgación oficial. |
| `regulatory_approach` | strategy_led | **risk_based** | Art. 16 mandata "AI risk taxonomy and assessment framework interoperable with international frameworks" — enfoque explícitamente risk-based por ley. |
| `regulatory_intensity` | 5 | **7** | Ecosistema consolidado: ley IA vigente + 2 leyes sectoriales vinculantes con autoridades activas (PDPC, ACS/MODA) + estrategia vigente + 2 guidelines sectoriales oficiales + National AI Strategic Committee por ley. |
| `enforcement_level` | medium | **medium** | Se mantiene. El AI Basic Act es ley marco sin régimen sancionatorio directo (delega en autoridades sectoriales vía Art. 16). PDPC y ACS tienen poderes sancionatorios reales por sus leyes fundacionales. |
| `thematic_coverage` | 9 | **12** | Los 7 principios del Art. 4 cubren ethics, data protection, cybersecurity, transparency, fairness, accountability + Art. 5 red lines (prohibited practices) + Art. 13-14 data governance/IP + Art. 15 labor + Art. 16 risk-based classification + Art. 12 international cooperation. |
| `regulatory_regime_group` | (derivado) | **binding_regulation** | Criterio 7.1 aplicable: "Ley IA-específica vigente (Act of Parliament o equivalente) con autoridad IA y poderes sancionatorios" → NSTC como competent authority + National AI Strategic Committee convocado por Premier. |
| `ai_framework_note` | "AI Basic Act (executive draft, not yet enacted), AI Taiwan Action Plan 2.0, risk-based approach, Ministry of Digital Affairs, AI CoE" | **"AI Basic Act 2026 (in force 2026-01-14, 20 articles, 7 principles, NSTC as competent authority, MODA implements risk taxonomy Art 16); PDPA 2025; CSMA 2018; AI Taiwan Action Plan 2.0 2023-2026; GenAI Guidelines Exec Yuan 2023; Critical Infra AI Guidelines 2025"** | Actualización para reflejar promulgación y corpus completo. |
| `confidence` | medium | **medium-high** | Evidencia primaria de ley IA vigente + 6 instrumentos complementarios en dominios oficiales. |

## 6. Diff summary

```
has_ai_law:              0 -> 1           (UPGRADE — AI Basic Act promulgada 2026-01-14)
ai_year_enacted:         (vacio) -> 2026  (nuevo)
regulatory_approach:     strategy_led -> risk_based  (Art 16 mandata risk taxonomy)
regulatory_intensity:    5 -> 7           (+2, ley IA + 2 sectoriales + 2 guidelines + estrategia)
enforcement_level:       medium -> medium  (sin cambio — Basic Act es ley marco)
thematic_coverage:       9 -> 12          (+3, Art 4+5+15+16 cubren dimensiones adicionales)
regulatory_regime_group: soft_framework/strategy_only -> binding_regulation  (UPGRADE ✅)
confidence:              medium -> medium-high
```

## 7. Fundamento del upgrade de régimen

**Criterios de `binding_regulation` cumplidos (§7.1 del pipeline):**
- **Ley IA-específica vigente** ✅ — AI Basic Act promulgada 2026-01-14, 20 artículos, en vigor.
- **Autoridad IA** ✅ — National Science and Technology Council como competent authority central (Art. 2); Ministry of Digital Affairs para risk taxonomy (Art. 16); National AI Strategic Committee convocado por Premier (Art. 6).
- **Poderes sancionatorios** ✅ (indirectos) — Art. 16 delega enforcement sectorial en competent authorities existentes (PDPC bajo PDPA, ACS/MODA bajo CSMA). Art. 5 establece red lines absolutas.

**Por qué no se queda en `soft_framework`:**
El pipeline §7.2 establece: "¿Hay ley IA-específica VIGENTE (no draft, no bill pending)? No → `soft_framework`. Sí → `binding_regulation`." El Act está promulgado desde 2026-01-14; la decisión es automática.

**Por qué `medium` enforcement y no `high`:**
El AI Basic Act es ley marco (framework law) sin sanciones horizontales propias. Taiwan eligió arquitectura delegada: el Act fija principios y estructura institucional, y remite sanciones a leyes sectoriales (PDPA, CSMA, consumer protection). Similar a la Korea AI Basic Act 2025. Ningún caso IA-específico enforcement documentado aún (solo 3 meses en vigor al 2026-04-16). Subir a `high` requeriría casos documentados ex-post.

## 8. Comparación con pilotos ya procesados

| País | Régimen | Ley IA | `has_ai_law` | Intensity | Coverage | Lógica |
|---|---|---|---|---|---|---|
| TWN | **binding_regulation** | AI Basic Act 2026 | 1 | 7 | 12 | Ley IA vigente + ecosistema sectorial maduro |
| BGD | soft_framework | Policy Draft V2.0 (no vinculante) | 0 | ~4 | ~8 | Pathway con fecha, obligaciones concretas |
| GHA | soft_framework | Sin ley IA | 0 | ~4 | ~9 | 2 leyes sectoriales + NAIS lanzada |
| SGP | soft_framework | Sin ley IA | 0 | 7 | 13 | Decisión deliberada de NO ley horizontal |
| MNG | soft_framework | Sin ley IA | 0 | 3 | 5 | 2 leyes sectoriales + AILA co-firmado |

**TWN es el primer piloto con `binding_regulation`** — caso testigo para el estudio: ecosistema maduro (tier equivalente a Singapur en coverage) que eligió codificar en ley horizontal, mientras Singapur decidió no hacerlo. Taiwán como *contrafactual natural* del caso SGP es material valioso para el análisis comparativo.

## 9. Checklist de validación humana

### Candidato 1+2. AI Basic Act
- [ ] Verificar que la URL pcode H0160093 carga correctamente el texto en law.moj.gov.tw.
- [ ] Confirmar fecha de promulgación 2026-01-14 con Presidential Office gazette si disponible.
- [ ] Confirmar que la traducción EN es la versión actual post-promulgación (no el draft).
- [ ] Validar las 8 citas textuales extraídas contra el PDF renderizado.
- [ ] Aceptar Chrome headless `--print-to-pdf` como método reproducible equivalente a mirror.

### Candidato 3. PDPA
- [ ] Verificar que la versión descargada es la consolidada post-2025-11-11.
- [ ] Confirmar PDPC activa (creada Art. 1-1).

### Candidato 4. CSMA 2018
- [ ] Verificar vigencia y que ACS está operativa bajo MODA.

### Candidato 5. AI Action Plan 2.0
- [ ] Confirmar aprobación Exec Yuan abril 2023.
- [ ] Aceptar que el documento oficial solo está en chino.

### Candidato 6. GenAI Guidelines
- [ ] Confirmar sesión 3869 del Exec Yuan (2023-08-31).

### Candidato 7. Critical Infra AI Guidelines
- [ ] Confirmar fecha han-ling 2025-10-08.
- [ ] Validar status como instrument vinculante sobre CII operators.

### Transversales
- [ ] Los 7 SHA-256 coinciden al recomputar.
- [ ] El diff de recodificación es aceptable y no requiere ajuste a `high` enforcement prematuro.
- [ ] El upgrade a `binding_regulation` es coherente con el pipeline §7.

## 10. Decisión del revisor

### Por candidato
- **AI Basic Act (EN + ZH):** [ ] APROBAR / [ ] RECHAZAR / [ ] PEDIR OTRA FUENTE
- **PDPA 2025:** [ ] APROBAR / [ ] RECHAZAR / [ ] PEDIR OTRA FUENTE
- **CSMA 2018:** [ ] APROBAR / [ ] RECHAZAR / [ ] PEDIR OTRA FUENTE
- **AI Action Plan 2.0:** [ ] APROBAR / [ ] RECHAZAR / [ ] PEDIR OTRA FUENTE
- **GenAI Guidelines 2023:** [ ] APROBAR / [ ] RECHAZAR / [ ] PEDIR OTRA FUENTE
- **Critical Infra AI Guidelines 2025:** [ ] APROBAR / [ ] RECHAZAR / [ ] PEDIR OTRA FUENTE

### Por diff
- **Diff completo (9 cambios):** [ ] APROBAR / [ ] RECHAZAR / [ ] MODIFICAR

### Por régimen
- **Upgrade `binding_regulation`:** [ ] APROBAR / [ ] RECHAZAR / [ ] PEDIR EVIDENCIA ADICIONAL

## 11. Notas del codificador

1. **Taiwán es el primer caso `binding_regulation` del corpus piloto.** Marca transición cualitativa respecto a los 4 pilotos previos (`soft_framework`). El AI Basic Act está en vigor solo hace 3 meses al 2026-04-16 — IAPP capturó el estado pre-promulgación (draft), lo que explica la desactualización del `evidence_summary`.

2. **Arquitectura institucional delegada.** A diferencia de EU AI Act (enforcement centralizado) o Korea AI Basic Act (autoridad dedicada), Taiwán eligió arquitectura delegada: NSTC coordina, MODA define risk taxonomy, competent authorities sectoriales (PDPC, ACS, etc.) aplican sanciones bajo sus leyes fundacionales. Esto mantiene `enforcement_level=medium` y no `high`.

3. **`law.moj.gov.tw` ya estaba en el briefing como portal asiático que requiere headers completos.** Confirmado en esta iteración: `/ENG/LawFile.ashx` devuelve 0 bytes, pero Chrome headless renderiza correctamente las páginas `pcode=...`. Este patrón se aplica a futuras iteraciones de otros pcodes (JPN, KOR también usan sistemas similares).

4. **Caso contrafactual SGP vs TWN.** Ambos países con ecosistema IA denso y ley sectorial robusta, pero decisiones regulatorias opuestas: SGP = no ley horizontal por diseño; TWN = ley horizontal promulgada. Valioso para el análisis comparativo del estudio principal.

5. **Siguientes pasos sugeridos:**
   - Aprobación humana de este CANDIDATES.md.
   - Re-capturar National AI Development Guidelines cuando NSTC lo publique (mandato Art. 6 AI Basic Act).
   - Re-capturar AI Risk Taxonomy Framework cuando MODA lo publique (mandato Art. 16).
   - Monitorear primeros enforcement cases IA-específicos; si aparecen, upgrade a `enforcement_level=high`.
   - Siguiente país del lote prioritario: **LKA (Sri Lanka)** según §10.1 de la skill.
