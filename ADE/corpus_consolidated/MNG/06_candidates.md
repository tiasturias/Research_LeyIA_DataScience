# MNG — Mongolia

**Fecha de auditoría:** 2026-04-15
**Codificador:** Claude Opus 4.6 (asistido)
**Revisor humano:** [PENDIENTE]
**Confidence IAPP actual:** `(vacío)` → **`medium-high`** (post-validación propuesta)

**Fuentes bibliográficas formales:** ver [SOURCES.md](SOURCES.md) (citas APA 7, URLs primarias, hashes, evidencia de oficialidad)
**Metadatos de trazabilidad:** ver [manifest.csv](manifest.csv)

---

## 1. Codificación actual (IAPP / OECD base — vigente en `x1_master.csv`)

| Variable | Valor actual | Fuente |
|---|---|---|
| `has_ai_law` | 0 | IAPP_supplementary_research 2026-02 |
| `regulatory_approach` | `light_touch` | IAPP_supplementary_research |
| `regulatory_intensity` | 1 (0-10) | IAPP_supplementary_research |
| `enforcement_level` | `none` | IAPP_supplementary_research |
| `thematic_coverage` | 1 (0-15) | IAPP_supplementary_research |
| `regulatory_regime_group` | `strategy_only` / `no_framework` *(derivación ambigua)* | Derivado |
| `ai_year_enacted` | — | — |
| `ai_framework_note` | "Vision 2050 mentions digitalization, no AI-specific legislation or strategy." | IAPP supplementary |

**Diagnóstico preliminar:** La nota IAPP es **materialmente incompleta** al 2026-04. Mongolia aprobó en diciembre 2021 un paquete de 4 leyes digitales (PDPL, CSL, Law on Public Information, Law on Digital Signatures) que **entraron en vigor el 2022-05-01** y son aplicables directamente a sistemas IA. Adicionalmente, MDDIC y UNDP co-publicaron en agosto 2025 el AILA Mongolia (diagnóstico oficial con score 3.0 "Systematization Stage") y el draft de National Strategy for Big Data and AI fue presentado al State Great Khural en febrero-mayo 2025. La codificación IAPP `intensity=1, coverage=1, enforcement=none` subestima sustancialmente el estado real.

---

## 2. Inventario de instrumentos estatales IA (2021 → 2026-04)

| # | Documento | Año | Emisor | Tipo | Status | Archivo local |
|---|---|---|---|---|---|---|
| 1 | Law of Mongolia on Personal Data Protection | 2021-12-17 (in force 2022-05-01) | State Great Khural | Ley vinculante sectorial | En vigor | `MNG_PersonalDataProtectionLaw_2021.pdf` |
| 2 | Law of Mongolia on Cyber Security | 2021-12-17 (in force 2022-05-01) | State Great Khural | Ley vinculante sectorial | En vigor | `MNG_CyberSecurityLaw_2021.pdf` |
| 3 | Artificial Intelligence Landscape Assessment of Mongolia (AILA) | 2025-08 | MDDIC + UNDP | Readiness assessment (co-firmado) | Publicado | `MNG_AILA_UNDP_2025.pdf` |
| 4 | National Strategy on Big Data and Artificial Intelligence | 2025 (draft presentado al Parlamento) | MDDIC | Estrategia nacional IA | Draft — submission a State Great Khural | **No descargable** (sin PDF público al 2026-04-15) |
| 5 | Digital Nation Policy 2022-2027 | 2022 | Government of Mongolia | Política medio plazo | Aprobada | **No descargable** (sin URL PDF en dominio gubernamental) |
| 6 | Law on Public Information and Transparency | 2021-12 | State Great Khural | Ley vinculante transversal | En vigor | No incluido (foco del estudio — tangencial a IA) |
| 7 | Law on Digital Signatures | 2021-12 | State Great Khural | Ley vinculante transversal | En vigor | No incluido (tangencial) |

> **Documento 4** es el instrumento IA-específico más importante de Mongolia, pero sin PDF público al 2026-04-15. Trazabilidad vía MONTSAME (agencia de noticias gubernamental) y UNDP press releases. Re-captura pendiente.

---

## 3. Candidato 1 — Law on Personal Data Protection 2021 [LEY VINCULANTE]

- **Título:** Law of Mongolia on Personal Data Protection
- **Emisor:** State Great Khural (Parliament of Mongolia)
- **Aprobación:** 2021-12-17. **En vigor:** 2022-05-01.
- **URL oficial:** https://legalinfo.mn/en/edtl/16532053734461
- **URL mirror (descarga efectiva):** https://cyrilla.org/api/files/1728476367950dd4g86zulst.pdf
- **SHA-256:** `be3440be370317d521e909ad23742357de60d962a039878a960ffccd12ac53c8`
- **Idioma:** Inglés (traducción no oficial del texto mongol oficial)

### Rol en corpus IA
- Reemplaza Law on Personal Secrecy (1995).
- Introduce el régimen moderno GDPR-like en Mongolia (primera ley data privacy integral en Asia Central central según Greenleaf & Kaldani 2022).
- Aplicable directamente a training data IA (consent, lawful basis, data subject rights, cross-border transfers) y decisiones automatizadas.
- Autoridad supervisoria: Communications Regulatory Commission ampliada + Mongolian Human Rights Commission como órgano de protección.

---

## 4. Candidato 2 — Law on Cyber Security 2021 [LEY VINCULANTE]

- **Título:** Law of Mongolia on Cyber Security
- **Emisor:** State Great Khural (Parliament of Mongolia)
- **Aprobación:** 2021-12-17. **En vigor:** 2022-05-01.
- **URL oficial:** https://legalinfo.mn/en/edtl/16531350476261
- **URL mirror (descarga efectiva):** https://gratanet.com/laravel-filemanager/files/3/ENG-Cybersecurity%20Law%20of%20Mongolia.pdf
- **SHA-256:** `e18aa62c6a3c6c2091276c5ea4110e0074087ed79f8e42af697814aeb3066716`

### Rol en corpus IA
- Primera ley de ciberseguridad de Mongolia (desarrollada durante una década previa).
- Establece **Cyber Security Council**, **Cyber Security National Center** y **Critical Information Infrastructure (CII) regime**.
- Aplicable a infraestructura digital crítica incluidos sistemas IA en sectores CII.

---

## 5. Candidato 3 — AILA Mongolia 2025 [READINESS ASSESSMENT CO-FIRMADO]

- **Título:** Artificial Intelligence Landscape Assessment of Mongolia: Shaping AI to be an empowering force for people and planet
- **Emisor:** MDDIC (Ministry of Digital Development, Innovation and Communications) + UNDP (co-publicación)
- **Fecha:** Agosto 2025
- **URL oficial:** https://www.undp.org/sites/g/files/zskgke326/files/2025-08/aila_eng-final.pdf
- **SHA-256:** `82bbc05b36689df723e2476b088bdba84d58fc4bb05f13596167c18480ff9f77`

### Citas textuales clave (justifican co-emisión estatal)

**Portada:**
> "MINISTRY OF DIGITAL DEVELOPMENT, INNOVATION AND COMMUNICATIONS — ARTIFICIAL INTELLIGENCE LANDSCAPE ASSESSMENT OF MONGOLIA"

**Production team (p.2) — Initiator/Lead:**
> "Mr. Munkhbat Perenlei, Director General of the Innovation Policy Coordination Department, Ministry of Digital Development, Innovation and Communications of Mongolia"

### Rol en corpus
- Diagnóstico oficial con score readiness **3.0 "Systematization Stage"**.
- Base analítica documentada del draft National Strategy for Big Data and AI presentado al Parlamento en 2025.
- Identifica 3 desafíos persistentes: capacity gaps in civil servants, unequal rural infrastructure access, absence of clear ethical/regulatory frameworks.
- Coherente con criterio de inclusión validado en piloto BGD: co-publicación Estado + UN donde el Estado aparece como co-emisor firmante (no solo sujeto de estudio).

---

## 6. Recodificación X1 propuesta

| Variable | Actual (IAPP) | **Propuesta** | Justificación (con cita) |
|---|---|---|---|
| `has_ai_law` | **0** | **0** *(sin cambio)* | Mongolia NO tiene ley IA-específica al 2026-04-15. El draft National Strategy está presentado al Parlamento pero sin adopción formal. Las leyes vinculantes existentes (PDPL, CSL) son sectoriales, no IA-específicas. |
| `regulatory_approach` | `light_touch` | **`strategy_led`** *(↑)* | Draft Strategy in parliamentary review + AILA co-firmado 2025 son instrumentos declarativos consistentes con `strategy_led`; `light_touch` subestima la trayectoria. |
| `regulatory_intensity` | **1** | **3** *(↑ +2)* | 2 leyes sectoriales vinculantes en vigor desde 2022 (PDPL + CSL) con autoridades establecidas + diagnóstico co-firmado + draft strategy en el Parlamento. Supera `intensity=1`. |
| `enforcement_level` | `none` | **`low`** *(↑)* | PDPL y CSL crean autoridades (Communications Regulatory Commission ampliada; Cyber Security Council/National Center) con poderes sancionatorios. `none` es incorrecto — hay enforcement sectorial real. |
| `thematic_coverage` | **1** | **5** *(↑ +4)* | Cobertura actual: data protection (PDPL), cybersecurity (CSL), ethical/responsible AI (AILA dimensions), digital infrastructure (Digital Nation Policy), draft strategy sectors (education, economy, public services). |
| `regulatory_regime_group` | `strategy_only` / `no_framework` (ambigua) | **`soft_framework`** ✅ | Criterios cumplidos: (a) leyes sectoriales vinculantes aplicables a IA con autoridades activas, (b) readiness assessment oficial co-firmado, (c) estrategia IA en proceso parlamentario explícito. No es `no_framework` (existen leyes + diagnóstico). No es `strategy_only` puro (hay base legal vinculante). No es `binding_regulation` (no hay ley IA). |
| `ai_year_enacted` | (vacío) | **(vacío)** | No aplicar hasta adopción formal del National Strategy o ley IA específica. |
| `ai_framework_note` | "Vision 2050 mentions digitalization, no AI-specific legislation or strategy." | **"Binding sectoral base: Law on Personal Data Protection 2021 (in force 2022-05-01) + Law on Cyber Security 2021 (in force 2022-05-01). AI-specific: AILA co-published MDDIC+UNDP Aug 2025 (readiness score 3.0 Systematization Stage); draft National Strategy on Big Data and AI submitted to State Great Khural 2025. Planned: National Council on AI (2025-2026), GPU cluster AI Center, National Data Repository. Digital Nation Policy 2022-2027 as umbrella."** | Refleja estado real 2026-04. |

### Diff summary (propuesto — pendiente aprobación humana)

```
has_ai_law:              0 -> 0          (unchanged; AI strategy still in draft)
regulatory_approach:     light_touch -> strategy_led   (+1 level)
regulatory_intensity:    1 -> 3          (+2)
enforcement_level:       none -> low     (+1 level)
thematic_coverage:       1 -> 5          (+4)
regulatory_regime_group: strategy_only/no_framework (ambiguous) -> soft_framework  (UPGRADE ✅)
confidence:              (empty) -> medium-high
```

### Fundamento del upgrade a `soft_framework`

**Criterio aplicado — Mongolia corresponde a `soft_framework` porque:**
1. **Base legal sectorial vinculante en vigor desde 2022:** PDPL + CSL con autoridades establecidas (Communications Regulatory Commission ampliada, Cyber Security Council).
2. **Diagnóstico IA co-firmado por el Estado:** AILA 2025 con MDDIC como co-emisor y lead de producción.
3. **Pathway regulatorio IA formalmente iniciado:** draft National Strategy presentado al State Great Khural con respaldo UNDP; National Council on AI e infraestructura IA planificada para 2025-2026.
4. **Paquete de 4 leyes digitales 2021/2022** muestra compromiso legislativo consistente con infraestructura regulatoria para economía digital.

**No es `binding_regulation`** porque no hay ley IA-específica vigente.
**No es `strategy_only`** porque hay base legal sectorial vinculante + enforcement real (PDPL + CSL aplican desde 2022).
**No es `no_framework`** porque existen leyes sectoriales con autoridades + diagnóstico IA oficial.

### Comparación Mongolia vs otros pilotos (todos `soft_framework`, ruta distinta)

| Dimensión | Singapore | Bangladesh | Ghana | **Mongolia** |
|---|---|---|---|---|
| Leyes sectoriales vinculantes | PDPA 2012+2020 + CSL 2018 (10+ años) | — | DPA 2012 + CSA 2020 | **PDPL 2021 + CSL 2021 (en vigor 2022)** |
| Instrumento IA-específico | MGF ecosystem + NAIS 2.0 | NAIP V2.0 Draft | NAIS 2023-2033 launched | **AILA 2025 + Draft Strategy (en Parlamento)** |
| Readiness assessment | AI Verify operacional | AIRAM UNESCO 2025 | UNESCO RAM (pendiente) | **AILA UNDP 2025 co-firmado** |
| Autoridad IA | AI Safety Institute + AI Verify Foundation | NDGA (propuesta) | RAI Office (propuesta) | **National Council on AI (propuesto 2025-2026)** |
| Madurez del régimen | Consolidado | En adopción | Recién lanzado | **En construcción activa** |

Mongolia es el caso `soft_framework` **más reciente/temprano** de los 4 pilotos: base legal de 2022 + diagnóstico 2025 + estrategia en Parlamento = trayectoria clara pero sin instrumento IA consolidado.

---

## 7. Checklist de validación humana

### Candidato 1: Law on Personal Data Protection 2021
- [ ] 1. Emisor oficial (State Great Khural) ✅ preverificado
- [ ] 2. Documento primario ✅ preverificado
- [ ] 3. Relevancia: (a) en vigor desde 2022-05-01, aplicable a sistemas IA
- [ ] 4. Aplicabilidad a IA (training data, decisiones automatizadas) ✅
- [ ] 5. Aceptar traducción EN no oficial + mirror CYRILLA dado que legalinfo.mn no expone PDF directo
- [ ] 6. Tipo coherente (ley sectorial vinculante)

### Candidato 2: Law on Cyber Security 2021
- [ ] 1. Emisor oficial (State Great Khural) ✅
- [ ] 2. Documento primario ✅
- [ ] 3. Relevancia: (a) en vigor desde 2022-05-01
- [ ] 4. Aplicabilidad a IA (CII, infraestructura digital crítica) ✅
- [ ] 5. Aceptar mirror GRATA Law Firm (subsidiaria en Ulaanbaatar)
- [ ] 6. Tipo coherente

### Candidato 3: AILA Mongolia 2025
- [ ] 1. Co-emitido por MDDIC ✅ preverificado (portada + Initiator/Lead Dir General MDDIC)
- [ ] 2. Documento primario (reporte oficial) ✅
- [ ] 3. Relevancia: (b) input documentado del draft National Strategy
- [ ] 4. IA explícita (core del documento) ✅
- [ ] 5. Contribuye a thematic_coverage
- [ ] 6. Tipo coherente (readiness assessment)

---

## 8. Decisión del revisor (marcar al final)

### Para cada candidato
**1 (PDPL):** [ ] APROBAR [ ] RECHAZAR [ ] PEDIR OTRA FUENTE
**2 (CSL):** [ ] APROBAR [ ] RECHAZAR [ ] PEDIR OTRA FUENTE
**3 (AILA):** [ ] APROBAR [ ] RECHAZAR [ ] EXCLUIR como referencia secundaria

### Para la recodificación propuesta
- [ ] APROBAR diff completo
- [ ] APROBAR PARCIALMENTE — modificar: ___
- [ ] MANTENER codificación IAPP original

### Sobre el upgrade a `soft_framework`
- [ ] Aceptar upgrade (justificado por PDPL+CSL vigentes + AILA co-firmado + draft strategy en Parlamento)
- [ ] Mantener `strategy_only` (conservador — esperar adopción formal del Strategy)
- [ ] Mantener `no_framework` (no recomendado — contradice evidencia)

### Sobre fuentes adicionales a buscar
- [ ] Intentar capturar National Strategy for Big Data and AI cuando sea publicado
- [ ] Incorporar Digital Nation Policy 2022-2027 si aparece URL oficial
- [ ] No necesario — corpus actual es suficiente para recodificar

---

## 9. Notas del codificador

1. **Búsqueda priorizada de leyes:** encontradas 2 leyes vinculantes sectoriales en vigor desde 2022 (PDPL + CSL), aprobadas en el paquete de 4 leyes digitales de diciembre 2021.

2. **Búsqueda complementaria de iniciativas:** 1 instrumento IA-específico co-firmado por el Estado (AILA UNDP+MDDIC 2025). El National Strategy for Big Data and AI existe como draft presentado al Parlamento pero **sin PDF público al 2026-04-15** — registrado en inventario para re-captura futura.

3. **Completitud:** 3/4 documentos principales descargados con HTTP 200 y SHA-256. El documento faltante (National Strategy) no tiene URL pública.

4. **Confidence upgrade:** `(vacío)` → `medium-high`. La recodificación se sostiene en evidencia primaria directa (leyes en legalinfo.mn + PDF AILA en undp.org + Initiator Lead MDDIC verificado en portada).

5. **Limitación:** los textos EN son traducciones no oficiales. Los textos oficiales están en mongol. Para análisis NLP del estudio, las traducciones EN son suficientes pero debe documentarse como limitación.

6. **Caso particular de `legalinfo.mn`:** portal oficial sin URL directa al PDF (export dinámico). Usamos mirrors verificables (CYRILLA para PDPL, GRATA para CSL) como solución reproducible. Si el usuario prefiere evitar mirrors, alternativa = scraping del portal oficial con headless browser, pero es sobre-ingeniería para el estudio.

7. **Lectura estratégica para el estudio LeyIA:** Mongolia es el caso testigo de **`soft_framework` más reciente** — base legal de 2022 + estrategia IA 2025 en Parlamento. Comparar con Bangladesh (V2.0 Draft 2026, AI Act programado 2028) para observar patrones de adopción regulatoria IA en países en desarrollo con cooperación UN activa.
