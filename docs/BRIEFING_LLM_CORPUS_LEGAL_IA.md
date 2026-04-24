# BRIEFING — Continuación de la extracción del corpus legal-IA por país

**Destinatario:** LLM de Anthropic (Claude Opus 4.6 o Sonnet 4.6) que recibe esta tarea sin contexto previo.
**Autor:** Claude Opus 4.6, para continuidad entre sesiones.
**Fecha de referencia:** 2026-04-15. La fecha "hoy" al leer este documento la define el timestamp del sistema.
**Proyecto raíz:** `/Users/francoia/Documents/MIA/Proyecto Data-Science/Research_LeyIA_DataScience/`

---

## 0. Cómo leer este documento

Lee el documento completo antes de ejecutar cualquier acción. Contiene:

1. **Contexto del estudio** — de qué trata el proyecto y por qué importa esta tarea.
2. **Tu rol específico** — qué producir, qué no producir, qué no decidir unilateralmente.
3. **Pipeline de búsqueda** — las 6 capas priorizadas aplicables a todos los países.
4. **Criterios de inclusión/exclusión** — regla estricta de URL verificable, co-emisión estatal, etc.
5. **Pipeline técnico de descarga** — comandos concretos, headers, patrones de error ya observados.
6. **Estructura de entregables** — los 3 archivos que produces por país y sus secciones exactas.
7. **Reglas de recodificación** — los 4 buckets de régimen y cómo decidir entre ellos.
8. **Validación humana** — lo que NO haces sin autorización del usuario.
9. **Patrones aprendidos en los 4 pilotos** — qué esperar país por país.
10. **Plan de ejecución por lotes** — orden sugerido y países prioritarios.

Reglas absolutas, en orden de prioridad:
- **R1 — URL verificable obligatoria:** un documento sin URL de origen trazable NO entra al corpus. Esta es regla del usuario, estricta.
- **R2 — Validación humana antes de integrar:** nunca modificas `data/interim/x1_master*.csv`. Generas propuestas en `CANDIDATES.md` y el usuario aprueba/rechaza.
- **R3 — Acumular variedad:** aunque encuentres una ley IA-específica, sigue buscando estrategias y frameworks del mismo país para máxima variedad de datos. Y si no hay ley, aún así extrae todas las iniciativas disponibles.
- **R4 — Fecha efectiva de búsqueda:** considerar documentos hasta la fecha actual del sistema. No limitarse a un año. Acumular desde la primera ley digital/data del país hasta el presente.
- **R5 — Idioma:** aceptar traducciones no oficiales cuando el texto oficial solo esté disponible en idioma local. Documentar como limitación. No rechazar documento por idioma.

---

## 1. Contexto del estudio

### 1.1 El proyecto

**Título:** "¿Regular o no regular? Análisis comparativo del impacto de marcos regulatorios de IA en el desarrollo de ecosistemas de IA".

**Objetivo práctico:** informar la decisión de Chile sobre el Proyecto de Ley 16821-19 (AI Framework Law chilena) mediante un análisis comparativo cuantitativo de 86 países.

**Usuario:** investigador data scientist liderando el estudio. Prefiere respuestas terse, comunicación en español, Markdown para entregables, trazabilidad fuerte.

**Email del usuario:** brunel.fr99@gmail.com.

### 1.2 Estructura de variables

- **X1** = variables de régimen regulatorio IA (el foco del corpus legal). 86 países × 8 dimensiones aproximadas.
- **Y** = variables de outcomes de ecosistema IA (Stanford AI Index, Microsoft AI Diffusion, adoption panels, etc.).
- **Controles** = legal origin, GDP, educación, etc.

**La tarea del corpus legal es construir la variable X1 con evidencia primaria**, reemplazando o corrigiendo la codificación base de IAPP Global AI Law & Policy Tracker (que tiene baja confianza en varios países).

### 1.3 Estado de los 4 pilotos completados

Al momento de escribir este briefing (2026-04-15), están validados:

| País | ISO3 | Nº docs | Régimen propuesto | Status |
|---|---|---|---|---|
| Bangladesh | BGD | 4 | `soft_framework` | Revisado y aprobado por usuario |
| Ghana | GHA | 4 | `soft_framework` | Entregado, pendiente aprobación final |
| Singapur | SGP | 7 | `soft_framework` (corrección) | Entregado, pendiente aprobación final |
| Mongolia | MNG | 3 | `soft_framework` | Entregado, pendiente aprobación final |

Todos los pilotos están en `data/raw/legal_corpus/{ISO3}/` con los 3 entregables estándar. **Léelos antes de empezar un país nuevo** — son tus plantillas de referencia.

### 1.4 Países pendientes (82 restantes)

Lista completa en `data/raw/IAPP/iapp_x1_core.csv` (86 filas, una por país). Los 4 pilotos ya hechos son BGD, GHA, MNG, SGP — el resto está pendiente.

**Lote prioritario de baja confianza IAPP (13 países, `source = IAPP_supplementary_research`, `evidence_summary` pobre):**

BHR, BLR, BLZ, BRB, CMR, JOR, LBN, LKA, PAK, PAN, PHL, SYC, TWN.

Estos son los siguientes a procesar — la codificación IAPP actual es probablemente incompleta o errónea, como pasó con Mongolia. Orden sugerido: TWN primero (país grande con arquitectura regulatoria IA conocida), luego LKA, PAK, PHL (Asia), luego JOR, LBN, BHR (MENA), luego los pequeños.

**Lote secundario (desarrollados, ya codificados pero con densidad alta que merece corpus):** ARE, ARG, AUS, AUT, BEL, BRA, CAN, CHE, CHL, CHN, DEU, DNK, ESP, EST, FIN, FRA, GBR, IND, IRL, ISR, ITA, JPN, KOR, MEX, NLD, NOR, NZL, POL, PRT, SWE, TUR, USA, ZAF + resto UE.

**Chile (CHL)** tiene importancia especial porque es el caso de interés del estudio. Recomiendo tratarlo DESPUÉS de cubrir al menos el lote prioritario + 5-10 países desarrollados para contexto comparado.

---

## 2. Tu rol específico

### 2.1 Qué produces

Por cada país que proceses, generas **exactamente estos 3 archivos** en `data/raw/legal_corpus/{ISO3}/`:

1. **`manifest.csv`** — una fila por PDF descargado, 18 columnas de trazabilidad.
2. **`SOURCES.md`** — citas APA 7 + tabla de trazabilidad + evidencia de oficialidad + notas de proceso.
3. **`CANDIDATES.md`** — entregable principal para el usuario: inventario, citas textuales, recodificación propuesta con diff summary, checklist de validación.

Plus: los PDFs de los documentos descargados en la misma carpeta.

### 2.2 Qué NO haces

- **No modificas** `data/interim/x1_master.csv` ni `data/interim/x1_master_v2.csv`. Eso lo hace el usuario tras aprobar tu recodificación.
- **No marcas** nada como "integrado al pipeline" sin aprobación explícita.
- **No borras** archivos que ya existen en el corpus de otros países.
- **No inventas** URLs ni hashes. Si una fuente no es descargable, la registras como "no descargable" con notas; no fabricas una URL plausible.
- **No asumes** que un framework de think tank (OECD AI Policy Observatory reports, Brookings, Wilson Center, think tanks nacionales) es instrumento estatal — a menos que esté co-firmado por el gobierno del país.
- **No clasificas automáticamente** por heurística sin leer evidencia primaria. `has_ai_law=0` NO implica `strategy_only`. Singapur fue el caso testigo: intensity=6 pero derivación a `strategy_only` era incoherente — correcto era `soft_framework`.

### 2.3 Qué decides tú vs. qué decide el usuario

**Tú decides:**
- Qué documentos son candidatos (aplicando criterios de inclusión).
- Qué URLs efectivas de descarga usar (oficial vs mirror verificable).
- Qué citas textuales extraer para justificar recodificación.
- Qué recodificación **proponer** — variable por variable, con justificación.
- Qué régimen (`no_framework / strategy_only / soft_framework / binding_regulation`) proponer.

**El usuario decide:**
- Aprobación final documento por documento.
- Aprobación del diff de recodificación.
- Integración al pipeline de análisis.

### 2.4 Formato y tono de comunicación con el usuario

- **Español.** El usuario escribe en español, responde en español.
- **Terse.** Sin preámbulos, sin recap de lo que hiciste en cada paso, sin emojis (a menos que ya estén en plantillas existentes).
- **Enlaces clicables en formato markdown VSCode.** Usa `[filename.ext](data/raw/legal_corpus/XXX/filename.ext)` para que el usuario pueda abrir archivos desde la conversación.
- **Final de turno:** 1-2 frases resumiendo qué cambió y qué sigue. Nada más.

---

## 3. Pipeline de búsqueda (6 capas, en orden de prioridad)

Documento maestro: `docs/PIPELINE_BUSQUEDA_CORPUS_LEGAL_IA.md`. Léelo antes de empezar.

### Capa 1 — Ley IA-específica vinculante
Búsqueda: `"AI Act" OR "Artificial Intelligence Act" OR "Ley de IA" site:gov.{TLD}` + variantes en idioma local.

Si se encuentra → dispara `regulatory_regime_group = binding_regulation` y `has_ai_law = 1`.

Casos conocidos: UE (AI Act 2024), Corea del Sur (AI Basic Act 2025), EEUU estados específicos (California SB 1047, Colorado AI Act). China (Interim Measures GenAI, Deep Synthesis Provisions) está en zona gris — binding pero sectorial/administrativo.

### Capa 2 — Leyes sectoriales vinculantes aplicables a IA
**Siempre buscar**, aunque exista ley IA, para enriquecer el corpus. Tipos:
- **Protección de datos personales** (GDPR-like, PDPA, LGPD, PIPL, PDPL, HIPAA, etc.) — aplicable a training data y automated decision-making.
- **Ciberseguridad / infraestructura crítica** — aplicable a sistemas IA en sectores críticos.
- **Plataformas digitales / servicios en línea / contenido algorítmico** (DSA, Online Safety Acts, etc.) — aplicable a recomendación/moderación.
- **Propiedad intelectual / copyright** — training data y outputs generativos.
- **Regulación sectorial con componente IA explícito** (banca — ej. MAS FEAT; salud; autónomos; defensa).

### Capa 3 — Estrategia / política nacional IA
Búsqueda: `"National AI Strategy" OR "AI Roadmap" OR "Estrategia Nacional de IA" site:gov.{TLD}`. Variantes en idioma local.

Dispara mínimo `strategy_only`; combinado con Capa 2 puede justificar `soft_framework`.

### Capa 4 — Frameworks voluntarios / Model Governance / Guidelines
Códigos de buenas prácticas, frameworks de gobernanza, toolkits oficiales. Ej. Singapore MGF, Japan AI Guidelines, UK AI Regulatory Principles, USA NIST AI RMF.

Aumentan densidad temática pero no cambian régimen por sí solos.

### Capa 5 — Diagnósticos / Readiness Assessments co-firmados
**Solo** si el Estado es co-emisor firmante (no solo sujeto estudiado). Tipos típicos:
- UNESCO RAM (Readiness Assessment Methodology) — co-firmado por gobierno y UNESCO.
- UNDP AI Landscape Assessments (AILA) — co-firmado por MDDIC/Ministerio Digital + UNDP.
- OECD AI Policy Observatory country profiles — solo como contexto, NO incluir (no hay co-emisión, OECD es observador).
- ADB / Banco Mundial digital readiness reports con co-autoría gubernamental.

### Capa 6 — Proyectos de ley pendientes / borradores públicos
Bills en tramitación, drafts en consulta pública. Valor: trazabilidad de trayectoria. **No alteran régimen actual**, pero sí `confidence` y `ai_framework_note`.

---

## 4. Criterios de inclusión/exclusión

### 4.1 Incluir SÍ cumple las 3 condiciones:
1. **Emisor estatal claro.** Parlamento, Ministerio, Agencia estatal con mandato legal, Presidencia, autoridad regulatoria creada por ley, agencia supervisoria sectorial (banco central, regulador de telecom, regulador financiero).
2. **URL oficial verificable.** Dominio `.gov.{TLD}` / `.go.{TLD}` / `.gouv.{TLD}` / dominio equivalente nacional; o organismo internacional co-firmante (undp.org, unesco.org); o mirror verificable cuando el portal oficial no expone PDF directo (caso Mongolia legalinfo.mn → CYRILLA, GRATA).
3. **Relevancia IA demostrable.** (a) IA explícita en título/contenido, o (b) ley sectorial directamente aplicable al ciclo de vida IA, o (c) efecto histórico documentado sobre ecosistema IA.

### 4.2 Excluir SIEMPRE:
- Documentos emitidos por ONGs / think tanks / cooperaciones bilaterales (GIZ, USAID, BID, AFD) SIN co-firma estatal. Caso real: Ghana AI Practitioners' Guide (GIZ + Heritors Labs 2025) — excluido del corpus, registrado solo como contexto.
- Notas de prensa, blog posts, comunicados.
- Borradores filtrados sin publicación oficial.
- PDFs sin URL de origen verificable (R1 es absoluta).
- Reportes sobre el país por observatorios terceros (Wilson Center, Brookings, think tanks académicos). Pueden ir en "Fuentes complementarias".

### 4.3 Caso frontera: co-emisiones con organismos internacionales

**Incluir** si el Estado firma como co-emisor. Verificación:
- Leer portada del PDF → ¿aparece nombre del ministerio/gobierno junto al nombre del organismo internacional?
- Leer acknowledgements / production team (páginas 1-5) → ¿hay funcionarios gubernamentales listados como "Initiator, Lead" o "co-author"?
- Si SÍ → incluir.
- Si SOLO aparece como counterpart / consulted / interviewed → no incluir como instrumento estatal.

Caso validado: AILA Mongolia 2025 — portada dice "MINISTRY OF DIGITAL DEVELOPMENT, INNOVATION AND COMMUNICATIONS", production team p.2 tiene "Mr. Munkhbat Perenlei, Director General of the Innovation Policy Coordination Department, MDDIC" como Initiator/Lead. → **Incluido**.

### 4.4 Casos edge

- **Subsidiarias gubernamentales efectivas:** AI Verify Foundation (Singapur) es "wholly-owned not-for-profit subsidiary of IMDA". → Tratar como emisor gubernamental efectivo. Precedente internacional: BSI (UK), NIST (USA).
- **Agencias creadas por ley específica:** Cyber Security Agency de Singapur, Data Protection Commission de Ghana, PDPC de Singapur — todas son emisores estatales plenos.
- **Mirrors no gubernamentales estables:** `africadataprotection.org` para Ghana NAIS, `cyrilla.org` para Mongolia PDPL. Aceptables cuando (a) el texto está ausente en dominio gubernamental o (b) el portal oficial no expone PDF directo; siempre dejar trazabilidad de la URL emisora en `source_url_primary`.

---

## 5. Pipeline técnico de descarga

### 5.1 Herramienta estándar

```bash
curl -sLk \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept: application/pdf,text/html;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Referer: {URL_REFERRER_LOGICA}" \
  -w "HTTP:%{http_code} SIZE:%{size_download}\n" \
  -o {ISO3}_{ShortDocName}_{Year}.pdf \
  "{URL}"
```

Flags:
- `-s` silent
- `-L` follow redirects
- `-k` ignorar SSL cuando aplicable
- UA Chrome completo (crítico para sitios con bloqueos anti-scraping tipo AGC Singapore, algunos portales gov africanos, UNDP a veces).
- Referer = URL lógica de "desde dónde vendrías" al PDF. Críticamente importante en sso.agc.gov.sg, legalinfo.mn, algunos portales UE.

### 5.2 Patrones de error ya observados

| Síntoma | Causa probable | Solución |
|---|---|---|
| HTTP 403 con UA "Mozilla/5.0" simple | WAF bloquea UA genérico | Usar UA Chrome completo + headers Accept + Referer |
| HTTP 500 con URL de PDF aparente | Endpoint de export dinámico (no URL estable) | Buscar mirror verificable o WebFetch página para extraer URL real |
| File tipo "HTML document" tras HTTP 200 | Redirect implícito a página login / bot challenge | Revisar headers de respuesta, agregar cookies si es necesario |
| File tipo "JSON data" tras HTTP 200/404 | Endpoint API sin credenciales | Buscar URL alternativa en página pública |
| Loop 301 infinito | Documento retirado, redirect a página padre | Buscar mirror gubernamental regional o confirmar retirada |
| HTTP 200 pero size < 2KB | Página de error servida con status 200 | Validar con `file` que sea PDF real |

**Siempre validar:** `file {archivo}.pdf` debe reportar `PDF document` (no `HTML`, no `JSON data`, no `empty`).

### 5.3 Nombrado de archivos

Patrón: `{ISO3}_{ShortDocName}_{Year}.pdf`

Ejemplos reales:
- `SGP_PDPA_2012.pdf`
- `MNG_CyberSecurityLaw_2021.pdf`
- `GHA_NAIS_2023-2033.pdf`
- `BGD_NAIP_2026-2030_v2.0_DRAFT.pdf`

Reglas:
- Sin espacios. Usar `_`.
- Sin caracteres especiales (`(`, `)`, `&`, `,`).
- Year = año de publicación / rango si la estrategia cubre un período (ej. `2023-2033`).
- Si hay versión (v1, v2), incluirla: `_v2.0_DRAFT`.

### 5.4 Validación post-descarga

```bash
file *.pdf          # Confirmar "PDF document"
shasum -a 256 *.pdf # Computar SHA-256 para manifest.csv
```

Si `pdfminer.six` está disponible, extraer texto de primeras páginas para verificar autoría/emisor. Si no está disponible, instalarlo con `python3 -m pip install --quiet pdfminer.six`. Usar `from pdfminer.high_level import extract_text`.

### 5.5 Descarga en paralelo

Agrupar descargas independientes en UN solo `Bash` tool call con `&&` para eficiencia. Ejemplo del patrón usado en Singapur:

```bash
cd /ruta/al/corpus/SGP && \
curl ... -o doc1.pdf "URL1" && \
curl ... -o doc2.pdf "URL2" && \
curl ... -o doc3.pdf "URL3" && \
shasum -a 256 *.pdf
```

---

## 6. Estructura de entregables (exacta)

Lee los 4 pilotos antes de escribir los de un país nuevo. Las plantillas mejoran con cada iteración — usa siempre la plantilla más reciente (Singapur o Mongolia).

### 6.1 `manifest.csv`

Cabecera exacta (18 columnas):

```
iso3,filename,document_title,doc_type,issuer,publication_date,status,language,source_url_primary,source_url_mirror,source_domain,retrieved_date,retrieval_http_status,retrieval_method,sha256,size_bytes,pages,notes
```

Convenciones:
- `doc_type`: `binding_law_sectoral | binding_law_ai | strategy | policy_strategy | policy_draft | soft_framework | soft_framework_sectoral | readiness_assessment | guidelines | bill_pending`.
- `status`: `in_force | in_use | draft_under_review | draft_public_consultation | historical_with_effect | official_joint_publication | bill_pending | draft_public_consultation | approved_cabinet_{FECHA}`.
- `publication_date`: `YYYY-MM-DD` o `YYYY-MM` o `YYYY`.
- `retrieved_date`: fecha del sistema al momento de descarga.
- `retrieval_method`: string describiendo comando usado (ej. `"curl -sLk -A Chrome/120 -H Referer:sso.agc.gov.sg"`).
- `pages`: dejar vacío si no verificable fácil; llenarlo si `file` lo reporta.
- `notes`: texto en español, ≤3 oraciones, incluyendo por qué este documento se eligió / detalles de status.

### 6.2 `SOURCES.md`

Secciones exactas, en este orden:

1. **Cabecera:** país, ISO3, fecha de recopilación, codificador.
2. **Citas en formato académico (APA 7)** — una por documento, en orden cronológico.
3. **Tabla de trazabilidad completa** — columnas: `#`, `Documento`, `URL de descarga efectiva`, `Dominio`, `HTTP`, `Tamaño`, `SHA-256` (primeros 8 chars + últimos 4).
4. **Evidencia de oficialidad por documento** — un bloque por documento con: emisor declarado, aprobación/fecha, dominio de hosting, status, relevancia IA.
5. **Verificación de integridad** — párrafo corto sobre SHA-256 y reproducibilidad.
6. **Fuentes complementarias (no incorporadas al corpus)** — documentos identificados pero no cumplen criterios (ej. think tanks, reportes académicos, borradores no publicados). Registrarlos en transparencia.
7. **Notas de proceso** — decisiones editoriales, URLs no accesibles, mirrors usados, políticas de actualización.

### 6.3 `CANDIDATES.md`

Secciones exactas, en este orden:

1. **Cabecera:** país, fecha, codificador, **Revisor humano: [PENDIENTE]**, confidence IAPP actual → propuesta, links a SOURCES.md y manifest.csv.
2. **Codificación actual (IAPP / OECD base)** — tabla con `has_ai_law`, `regulatory_approach`, `regulatory_intensity`, `enforcement_level`, `thematic_coverage`, `regulatory_regime_group`, `ai_year_enacted`, `ai_framework_note`. Consultar `data/raw/IAPP/iapp_x1_core.csv` para estos valores.
3. **Diagnóstico preliminar** — 1 párrafo: por qué la codificación actual es/no es correcta.
4. **Inventario de instrumentos estatales IA** — tabla con una fila por documento (incluidos los no descargables, con la razón).
5. **Candidatos uno por uno** — para cada documento descargado, bloque con:
   - Metadatos (título, emisor, fecha, URL, SHA-256, idioma).
   - Rol en corpus IA.
   - Citas textuales clave (3-5 citas relevantes para justificar recodificación). Marcadas con `>` Markdown.
6. **Recodificación X1 propuesta** — tabla con `Variable | Actual (IAPP) | Propuesta | Justificación (con cita)`.
7. **Diff summary** — bloque de código con cambios concretos:
   ```
   has_ai_law:              0 -> 0
   regulatory_intensity:    2 -> 4          (+2)
   ...
   regulatory_regime_group: strategy_only -> soft_framework  (UPGRADE ✅)
   confidence:              low -> medium-high
   ```
8. **Fundamento del upgrade/downgrade de régimen** — criterios cumplidos, por qué SÍ / por qué NO el bucket adyacente.
9. **Comparación con pilotos ya procesados** (si aplica) — tabla mostrando el país nuevo vs BGD/GHA/SGP/MNG para contextualizar el régimen.
10. **Checklist de validación humana** — por candidato, 6-7 ítems con `[ ]`.
11. **Decisión del revisor** — bloque con `[ ] APROBAR / [ ] RECHAZAR / [ ] PEDIR OTRA FUENTE` por candidato + por diff + por régimen.
12. **Notas del codificador** — limitaciones, diferencias frente a IAPP, siguientes pasos sugeridos.

### 6.4 Plantillas de referencia

Usa el archivo más reciente como base — copia y adapta:

- `data/raw/legal_corpus/MNG/CANDIDATES.md` — más reciente, caso con 3 docs y estrategia aún no publicada.
- `data/raw/legal_corpus/SGP/CANDIDATES.md` — más completo, caso con 7 docs y corrección de derivación IAPP.
- `data/raw/legal_corpus/GHA/CANDIDATES.md` — caso con 4 docs, leyes sectoriales + estrategia recién lanzada.
- `data/raw/legal_corpus/BGD/CANDIDATES.md` — caso validado por el usuario (aprobado 2026-04-15).

---

## 7. Reglas de recodificación

### 7.1 Los 4 buckets de `regulatory_regime_group`

| Régimen | Condiciones suficientes |
|---|---|
| `no_framework` | No hay estrategia, ley IA, ni leyes sectoriales relevantes vinculantes en vigor |
| `strategy_only` | Solo estrategia/política declarativa, sin base legal sectorial vinculante relevante ni autoridad designada |
| `soft_framework` | Cualquiera de: (a) estrategia + ≥1 ley sectorial vinculante con autoridad activa relevante para IA, (b) policy/framework con obligaciones concretas (AIAs, red lines, liability) aunque sin ley IA, (c) autoridad IA específica designada con mandato real, (d) pathway legislativo declarado con fecha |
| `binding_regulation` | Ley IA-específica vigente (Act of Parliament o equivalente) con autoridad IA y poderes sancionatorios |

### 7.2 Reglas de decisión entre buckets adyacentes

**`no_framework` vs `strategy_only`:**
- ¿Hay al menos una estrategia IA oficial publicada, aunque sea preliminar?
  - No → `no_framework`.
  - Sí → `strategy_only` (mínimo).

**`strategy_only` vs `soft_framework`:**
- ¿Hay al menos una ley sectorial vinculante relevante (data protection, cybersecurity) en vigor con autoridad activa?
  - No → `strategy_only`.
  - Sí → `soft_framework`.
- ¿O hay obligaciones concretas (AIAs, red lines, liability, pathway legislativo con fecha)?
  - Sí → `soft_framework`.

**`soft_framework` vs `binding_regulation`:**
- ¿Hay ley IA-específica VIGENTE (no draft, no bill pending)?
  - No → `soft_framework`.
  - Sí → `binding_regulation`.

### 7.3 Reglas de intensidad (0-10) y cobertura (0-15)

Estas escalas son continuas. Orientación:

**`regulatory_intensity` (0-10):**
- 0-1: casi nada o menciones peripherales.
- 2-3: estrategia declarativa básica sin base legal sectorial.
- 4-5: estrategia + 1-2 leyes sectoriales o framework voluntario robusto.
- 6-7: ecosistema denso de frameworks + leyes sectoriales + autoridades activas.
- 8-9: ley IA-específica vigente con enforcement.
- 10: ley IA comprehensive con trayectoria de enforcement multi-año (UE post-AI-Act 2027+).

**`thematic_coverage` (0-15):** contar cuántos de estos temas están cubiertos por los instrumentos del país:
1. AI ethics/principles
2. Data protection aplicable a IA
3. Cybersecurity aplicable a IA
4. Algorithmic transparency / explainability
5. Bias / fairness
6. Human oversight / accountability
7. High-risk classification (risk-based approach)
8. Prohibited practices (social scoring, mass surveillance, etc.)
9. Liability / redress
10. Generative AI specific
11. Copyright / IP para training data
12. Sector-specific: health
13. Sector-specific: finance
14. Sector-specific: public services
15. International cooperation / AI governance fora

### 7.4 Reglas de `enforcement_level`

- `none`: sin autoridades activas con poderes relevantes a IA.
- `low`: autoridades existen pero sin casos documentados o poderes limitados.
- `medium`: autoridades activas con poderes sancionatorios reales, casos aplicados a sistemas digitales/data.
- `high`: autoridades con IA-specific enforcement documentado (multas, prohibiciones, orders).

### 7.5 Reglas de `has_ai_law`

- **0:** no hay ley IA-específica vigente. Draft bills, policies, frameworks no cuentan.
- **1:** hay ley IA-específica vigente (ej. EU AI Act para estados miembros UE, Korea AI Basic Act, California SB 1047 si se promulga para CA específicamente).

### 7.6 Cuándo mantener `has_ai_law=0` aunque haya mucha densidad

Singapur es el caso testigo: intensity=6/7, coverage=12/13, ecosystem soft-law mundialmente líder → pero `has_ai_law=0` porque la política declarada es NO promulgar ley horizontal. El régimen es `soft_framework`, no `binding_regulation`.

---

## 8. Validación humana

### 8.1 Lo que SIEMPRE pides

Al terminar un país, presenta al usuario:
- Resumen: nº de PDFs, régimen propuesto, cambio vs IAPP.
- Link al `CANDIDATES.md` para que lo revise.
- Pregunta explícita: "¿Apruebas, rechazas, o pides otra fuente?"
- Pregunta de continuación: "¿Sigo con {siguiente_país} o preferís otro?"

### 8.2 Lo que NUNCA haces sin aprobación

- Integrar recodificación a `x1_master.csv` o `x1_master_v2.csv`.
- Modificar archivos fuera de `data/raw/legal_corpus/{ISO3}/`.
- Clasificar un país como `binding_regulation` si hay ambigüedad.
- Saltarte países prioritarios de baja confianza.

### 8.3 Lo que haces tras aprobación

1. Marcar `Revisor humano: [APROBADO — {FECHA}]` en `CANDIDATES.md` del país aprobado.
2. Preparar CSV de recodificación si el usuario lo pide.
3. Seguir con el siguiente país.

---

## 9. Patrones aprendidos en los 4 pilotos

### 9.1 Bangladesh (BGD) — patrón "policy draft denso"

**Régimen final:** `soft_framework`.

**Ruta:** Sin ley IA. Strategy 2020 + Policy Draft V2.0 2026 con obligaciones concretas (AIAs mandatorios, strict liability, red lines) + pathway a AI Act 2028 declarado con fecha + AIRAM UNESCO/UNDP co-firmado 2025.

**Lección:** un policy draft post-consulta pública con obligaciones concretas y autoridad designada vale como `soft_framework` aunque no sea vinculante todavía. El pathway legislativo declarado con FECHA es el criterio clave.

### 9.2 Ghana (GHA) — patrón "leyes sectoriales + estrategia lanzada"

**Régimen final:** `soft_framework`.

**Ruta:** Sin ley IA. Dos leyes sectoriales vinculantes robustas (Data Protection Act 2012 + Cybersecurity Act 2020) con autoridades activas (DPC, CSA) + NAIS 2023-2033 lanzada por Presidente en 2026-04 + DEPS 2024.

**Lección:** la presencia de leyes sectoriales vinculantes DESDE HACE AÑOS con autoridades establecidas justifica `soft_framework` incluso si la estrategia IA es reciente.

### 9.3 Singapur (SGP) — patrón "corrección de IAPP + densidad soft-law máxima"

**Régimen final:** `soft_framework` (corrección de `strategy_only` incoherente).

**Ruta:** 7 documentos — PDPA 2012+2020 + CSL 2018 (vinculantes) + MAS FEAT 2018 + MGF 2020 + MGF GenAI 2024 + MGF Agentic 2026 + NAIS 2.0 2023.

**Lección:** `has_ai_law=0` NO implica `strategy_only`. Siempre releer la derivación IAPP de `regulatory_regime_group` contra la evidencia primaria. Si `intensity ≥ 4` y hay leyes sectoriales vigentes → es `soft_framework`.

### 9.4 Mongolia (MNG) — patrón "IAPP supplementary desactualizado"

**Régimen final:** `soft_framework` (upgrade desde `light_touch` / `no_framework` ambiguo).

**Ruta:** Paquete de 4 leyes digitales dic-2021 en vigor desde may-2022 (PDPL + CSL + otras 2) + AILA UNDP+MDDIC 2025 + draft National Strategy presentado a State Great Khural 2025.

**Lección:** los países con `source = IAPP_supplementary_research` son los más probables de estar desactualizados. La codificación `light_touch, intensity=1, coverage=1` es sospechosa por defecto — verificar si hay leyes sectoriales vinculantes que IAPP no capturó.

### 9.5 Reglas heurísticas derivadas

1. **Si el país tiene GDPR-like + CSL-like desde hace ≥2 años** → mínimo `soft_framework`, sin importar lo que diga IAPP.
2. **Si el país tiene draft strategy post-consulta pública con obligaciones concretas** → revisar si califica para `soft_framework`.
3. **Si IAPP dice `light_touch` + `intensity=1` + `coverage=1`** → casi siempre está desactualizado. Buscar agresivamente.
4. **Si IAPP dice `strategy_led` + `intensity≥5`** pero deriva a `strategy_only` → probablemente `soft_framework` correcto.
5. **Ante duda entre `strategy_only` y `soft_framework`** → elegir `soft_framework` si (a) hay autoridad real con poderes o (b) hay pathway legislativo con fecha.
6. **Ante duda entre `soft_framework` y `binding_regulation`** → mantener `soft_framework` a menos que haya ley IA-específica VIGENTE. Drafts no cuentan.

### 9.6 Sitios útiles por región

- **SSO / legalinfo.mn / AGC Singapore:** portales legislativos oficiales asiáticos. Requieren headers completos.
- **IMDA.gov.sg / PDPC.gov.sg:** agencias IA/data Singapur.
- **legalinfo.mn mirrors:** CYRILLA (cyrilla.org), GRATA (gratanet.com), DLA Piper.
- **UNDP repo (undp.org/sites/g/files/):** AILAs, readiness assessments.
- **UNESCO Digital Library:** RAMs co-firmados.
- **moj.go.kr / bareun-gov / korea.kr:** Corea del Sur.
- **csa.gov.gh / nita.gov.gh:** Ghana.
- **moc.gov.gh:** Ghana digital ministry.
- **go.gov.sg:** servicio oficial de URL cortas Singapur.
- **aiverifyfoundation.sg:** subsidiaria IMDA.

---

## 10. Plan de ejecución por lotes

### 10.1 Lote prioritario (13 países, baja confianza IAPP)

Orden sugerido por facilidad de acceso a documentos oficiales:

1. **TWN (Taiwan)** — gran volumen documental, inglés disponible, arquitectura regulatoria IA conocida (AI Basic Act en trámite).
2. **LKA (Sri Lanka)** — Digital Strategy, Data Protection Act 2022.
3. **PAK (Pakistan)** — Personal Data Protection Bill, National AI Policy Draft.
4. **PHL (Philippines)** — Data Privacy Act 2012, NAISR 2021, CREATE MORE Act.
5. **JOR (Jordan)** — AI Strategy 2023, Data Protection Law 2023.
6. **LBN (Lebanon)** — limitado, verificar e-Transactions Law.
7. **BHR (Bahrain)** — PDPL 2018, AI initiatives EDB.
8. **CMR (Cameroon)** — Digital Strategy, Cyber Law 2010.
9. **PAN (Panama)** — Ley 81/2019 sobre datos personales, AI initiatives.
10. **BLR (Belarus)** — edge case político, verificar si aplica.
11. **BRB (Barbados)** — Data Protection Act 2019.
12. **BLZ (Belize)** — limitado probable.
13. **SYC (Seychelles)** — limitado probable.

Para cada país, estimar 30-45 min de trabajo: 5 min búsqueda web, 10 min descarga, 20-30 min redacción de entregables.

### 10.2 Lote secundario (países desarrollados con codificación IAPP decente)

Después del lote prioritario, procesar en orden:
- UE-27 (pueden agruparse por similitud: todos comparten AI Act + GDPR, variación en implementación nacional).
- EEUU, Canadá, Reino Unido, Australia, Nueva Zelanda (common law).
- Japón, Corea del Sur, China (Asia desarrollada).
- América Latina: Brasil, México, Argentina, Chile, Colombia, Perú, Uruguay.
- Resto: Turquía, Israel, Sudáfrica, países del Golfo, India.

**Chile (CHL)** al final o en paralelo con el lote latino — es el caso focal del estudio.

### 10.3 Criterios de parada por país

Detén la búsqueda de un país cuando:
- Has encontrado la ley IA si existe.
- Has encontrado al menos 1 ley sectorial vinculante relevante (data protection como mínimo).
- Has encontrado la estrategia IA principal si existe.
- Has encontrado 1-3 frameworks/guidelines oficiales si existen.
- Total de 3-8 documentos por país es óptimo. Más de 10 es sobre-exhaustivo.

No te detengas por exceso. Si un país tiene ecosistema rico (ej. Singapur, UE, Corea), llega hasta 7-10 documentos.

### 10.4 Estimación total

- 82 países × 35 min promedio = ~48 horas de trabajo activo del LLM.
- Distribuido en sesiones de 3-5 países cada una (~2h por sesión) → ~10-15 sesiones.
- El usuario autoriza sesión por sesión. No pierdas el tiempo proponiendo hacer todo de una.

---

## 11. Memoria persistente y continuidad entre sesiones

### 11.1 Sistema de memoria

El proyecto usa un sistema de memoria persistente en:
```
/Users/francoia/.claude/projects/-Users-francoia-Documents-MIA-Proyecto-Data-Science-Research-LeyIA-DataScience/memory/
```

Archivos clave:
- `MEMORY.md` — índice.
- `project_leyia.md` — contexto general del proyecto.
- `pipeline_corpus_legal.md` — protocolo validado.

Cuando aprendas algo nuevo (ej. un país tiene un portal legislativo particular que requiere técnica X, o un documento clave con URL inestable), **actualiza los memos** para futuros LLMs.

### 11.2 Al inicio de cada sesión

1. Lee `MEMORY.md` para orientarte.
2. Lee los memos relevantes (`pipeline_corpus_legal.md` es mandatorio).
3. Lee `docs/PIPELINE_BUSQUEDA_CORPUS_LEGAL_IA.md` y este briefing (`docs/BRIEFING_LLM_CORPUS_LEGAL_IA.md`).
4. Revisa `data/raw/legal_corpus/` para saber qué países están completos.
5. Pregunta al usuario qué países procesar en esta sesión.

### 11.3 Al final de cada sesión

1. Resume qué países completaste, con links a sus `CANDIDATES.md`.
2. Indica cuántos quedan del lote prioritario.
3. Si descubriste patrones nuevos (sitios fuentes, técnicas de descarga), actualiza memos.
4. Deja el estado limpio: no dejes archivos temporales en carpetas de países.

---

## 12. Reglas operativas que el usuario ya estableció

Estas son preferencias del usuario que heredaste. Respétalas:

1. **Español** en toda comunicación.
2. **Terse.** Sin preámbulos, sin recap de lo obvio.
3. **Sin emojis** a menos que estén en plantillas existentes (ej. ✅ en las tablas de diff).
4. **Links markdown** siempre para archivos: `[nombre](ruta/relativa)`.
5. **Fecha correcta:** hoy es la fecha del sistema, no "2024" por default. Usa la fecha actual al llenar `retrieved_date`.
6. **Trazabilidad estricta:** URL obligatoria, SHA-256 obligatorio, sin excepciones.
7. **Todos los drafts retenidos:** si un país tiene múltiples versiones de un documento (V1, V2), mantener ambas. Útil para análisis de evolución.
8. **IA en sentido amplio:** no solo leyes IA-específicas. Cualquier iniciativa estatal relevante a IA cuenta — leyes, estrategias, decretos, whitepapers, roadmaps, directivas sectoriales con componente IA.
9. **Vigencia relajada:** instrumentos aceptables si (a) en uso activo, (b) publicados con intención de implementar, o (c) históricamente en fuerza con efecto documentado sobre ecosistema.
10. **PRIORIZAR leyes** — las leyes vinculantes son más impactantes para el desarrollo del ecosistema IA que las estrategias. Si un país tiene ley, buscar ley primero. Si no tiene, buscar todas las iniciativas.
11. **Human-in-the-loop** obligatorio. No integración automática al pipeline.

---

## 13. Tu primera acción al empezar una sesión nueva

1. Lee este briefing completo.
2. Lee los 4 CANDIDATES.md de los pilotos (BGD, GHA, SGP, MNG) — son tus plantillas.
3. Lee `docs/PIPELINE_BUSQUEDA_CORPUS_LEGAL_IA.md`.
4. Lee los memos en `/Users/francoia/.claude/projects/.../memory/`.
5. Lista al usuario lo que vas a hacer: "Voy a procesar {país} siguiendo el pipeline estándar. ¿Confirmas?".
6. Espera confirmación. NO empieces descarga hasta que el usuario diga "dale" o equivalente.

Si el usuario dice "continúa" o "seguí" sin especificar país, toma el siguiente del lote prioritario según el orden del §10.1 que aún no tenga carpeta en `data/raw/legal_corpus/`.

---

## 14. Errores comunes a evitar

Basado en la experiencia acumulada:

1. **No asumir régimen sin leer citas.** Incluso países "obvios" como Singapur tenían errores de derivación en IAPP.
2. **No confundir co-emisión con counterpart.** Lee production team / acknowledgements.
3. **No usar URLs de think tanks como si fueran oficiales.** Wilson Center, Brookings, etc. NO son instrumentos estatales.
4. **No descargar PDFs sin validar con `file`.** Muchos WAFs sirven HTML de error con status 200.
5. **No dejar HTTP 403 sin intentar headers completos.** AGC Singapore, UNDP a veces, algunos portales gov exigen Referer + UA Chrome.
6. **No inventar fechas.** Si no conoces la fecha exacta de aprobación, deja el año y documenta en notas.
7. **No proponer `binding_regulation` para drafts.** Solo leyes vigentes.
8. **No olvidar la R1.** URL verificable obligatoria. No excepciones.
9. **No saltarte la lectura de plantillas.** Cada CANDIDATES.md subsecuente mejora al previo.
10. **No empezar descarga antes de confirmación del usuario** en sesión nueva.

---

## 15. Glosario abreviado

- **IAPP:** International Association of Privacy Professionals — publicador del Global AI Law & Policy Tracker (fuente de codificación base).
- **AILA:** Artificial Intelligence Landscape Assessment (UNDP, país-específicos).
- **AIRAM / RAM:** AI Readiness Assessment Methodology (UNESCO, país-específicos).
- **CII:** Critical Information Infrastructure (designación legal en leyes de ciberseguridad).
- **DPC:** Data Protection Commission (Ghana, y genérico para autoridades de datos).
- **PDPC:** Personal Data Protection Commission (Singapur).
- **CSA:** Cyber Security Agency (Singapur), Cyber Security Authority (Ghana).
- **MGF:** Model AI Governance Framework (Singapur).
- **NAIS / NAIP:** National AI Strategy / Policy.
- **MoCD / MDDIC:** ministerios digitales (Ghana = MoCD; Mongolia = MDDIC).
- **R1-R5:** reglas absolutas listadas en §0.

---

## 16. Verificación final antes de entregar un país

Checklist que ejecutas mentalmente antes de responder al usuario:

- [ ] Todos los PDFs validados con `file` como "PDF document".
- [ ] SHA-256 calculado para todos.
- [ ] `manifest.csv` tiene 18 columnas y una fila por PDF.
- [ ] `SOURCES.md` tiene citas APA 7 para todos los docs.
- [ ] `CANDIDATES.md` tiene inventario completo (incluidos no descargables).
- [ ] Recodificación propuesta con diff summary claro.
- [ ] Checklist de validación humana presente.
- [ ] Todos los links internos funcionan (nombres de archivo exactos).
- [ ] Comparación con pilotos previos si el régimen no es trivial.
- [ ] Tono del resumen final: terse, español, sin emojis, 2-4 frases + pregunta de continuación.

---

**Fin del briefing.**

Si algo no está claro en este documento, **pregunta al usuario antes de proceder**. Es preferible una pregunta de clarificación a una decisión errada que el usuario tenga que revertir.
