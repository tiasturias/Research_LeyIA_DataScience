# Pipeline de búsqueda — 6 capas + criterios

## Principio rector

**Priorizar leyes vinculantes > iniciativas blandas.** Las leyes tienen impacto directo sobre el ecosistema IA. Pero SIEMPRE acumular ambos tipos para cubrir los 4 regímenes posibles (`no_framework`, `strategy_only`, `soft_framework`, `binding_regulation`).

- Si el país tiene ley IA → registrarla Y seguir buscando estrategias, frameworks, guidelines.
- Si NO tiene ley IA → buscar leyes sectoriales vinculantes (data protection, cyber, IP) Y toda iniciativa estatal IA.

## Paso previo — Cross-check techieray (discovery híbrido)

Antes de ejecutar las 6 capas, consultar **techieray Global AI Regulation Tracker** (https://www.techieray.com/GlobalAIRegulationTracker) en el browser para el país. Leer las 8 categorías y anotar títulos/fechas/emisores no vistos como queries dirigidas. Detalle completo + licencia + restricciones en [external_trackers.md](external_trackers.md). **Nunca** copiar texto/metadata al corpus; solo usar como pista.

## Capa 1 — Ley IA-específica vinculante

**Búsqueda:** `"AI Act" OR "Artificial Intelligence Act" OR "Ley de IA" site:gov.{TLD}` + variantes en idioma local.

**Disparador:** si se encuentra → `regulatory_regime_group = binding_regulation` y `has_ai_law = 1`.

**Casos conocidos:**
- UE: AI Act 2024.
- Corea del Sur: AI Basic Act 2025.
- EEUU: California SB 1047, Colorado AI Act (específicos por estado).
- China: Interim Measures GenAI, Deep Synthesis Provisions (zona gris — binding sectorial/administrativo).

## Capa 2 — Leyes sectoriales vinculantes aplicables a IA

**Siempre buscar**, aunque exista ley IA, para enriquecer el corpus.

Tipos:
- **Protección de datos personales** (GDPR-like, PDPA, LGPD, PIPL, PDPL, HIPAA) — aplicable a training data y automated decision-making.
- **Ciberseguridad / infraestructura crítica** — aplicable a sistemas IA en sectores críticos.
- **Plataformas digitales / servicios en línea / contenido algorítmico** (DSA, Online Safety Acts) — aplicable a recomendación/moderación.
- **Propiedad intelectual / copyright** — training data y outputs generativos.
- **Regulación sectorial con componente IA explícito** (banca — MAS FEAT; salud; autónomos; defensa).

## Capa 3 — Estrategia / política nacional IA

**Búsqueda:** `"National AI Strategy" OR "AI Roadmap" OR "Estrategia Nacional de IA" site:gov.{TLD}`. Variantes en idioma local.

Dispara mínimo `strategy_only`; combinado con Capa 2 puede justificar `soft_framework`.

## Capa 4 — Frameworks voluntarios / Model Governance / Guidelines

Códigos de buenas prácticas, frameworks de gobernanza, toolkits oficiales.

Ejemplos: Singapore MGF, Japan AI Guidelines, UK AI Regulatory Principles, USA NIST AI RMF.

Aumentan densidad temática pero no cambian régimen por sí solos.

## Capa 5 — Diagnósticos / Readiness Assessments co-firmados

**Solo** si el Estado es co-emisor firmante (no solo sujeto estudiado).

Tipos:
- **UNESCO RAM** (Readiness Assessment Methodology) — co-firmado por gobierno + UNESCO.
- **UNDP AILA** (AI Landscape Assessment) — co-firmado por Ministerio Digital + UNDP.
- **OECD AI Policy Observatory country profiles** — NO incluir (OECD es observador, no co-emisor).
- **ADB / Banco Mundial** digital readiness reports con co-autoría gubernamental.

## Capa 6 — Proyectos de ley pendientes / borradores públicos

Bills en tramitación, drafts en consulta pública.

**Valor:** trazabilidad de trayectoria. **No alteran régimen actual**, pero sí `confidence` y `ai_framework_note`.

---

## Criterios de inclusión (3 condiciones obligatorias)

1. **Emisor estatal claro.** Parlamento, Ministerio, Agencia estatal, Presidencia, autoridad regulatoria creada por ley, agencia supervisoria sectorial (banco central, regulador telecom/financiero).
2. **URL oficial verificable.** Dominio `.gov.{TLD}` / `.go.{TLD}` / `.gouv.{TLD}` equivalente nacional; o organismo internacional co-firmante (undp.org, unesco.org); o mirror verificable cuando el portal oficial no expone PDF directo (caso Mongolia legalinfo.mn → CYRILLA, GRATA).
3. **Relevancia IA demostrable.** (a) IA explícita en título/contenido, (b) ley sectorial directamente aplicable al ciclo de vida IA, o (c) efecto histórico documentado sobre ecosistema IA.

## Criterios de exclusión

- Documentos emitidos por ONGs / think tanks / cooperaciones bilaterales (GIZ, USAID, BID, AFD) **sin** co-firma estatal. Caso real: Ghana AI Practitioners' Guide (GIZ + Heritors Labs 2025) — excluido del corpus.
- Notas de prensa, blog posts, comunicados.
- Borradores filtrados sin publicación oficial.
- PDFs sin URL de origen verificable (**R1 absoluta**).
- Reportes sobre el país por observatorios terceros (Wilson Center, Brookings, think tanks académicos). Pueden ir en "Fuentes complementarias".

## Caso frontera: co-emisiones con organismos internacionales

**Incluir** si el Estado firma como co-emisor.

Verificación:
1. Portada del PDF → ¿aparece ministerio/gobierno junto a organismo internacional?
2. Acknowledgements / production team (páginas 1-5) → ¿funcionarios gubernamentales listados como "Initiator, Lead" o "co-author"?
3. Si SÍ → incluir.
4. Si SOLO aparece como counterpart / consulted / interviewed → NO incluir como instrumento estatal.

**Caso validado:** AILA Mongolia 2025 — portada dice "MINISTRY OF DIGITAL DEVELOPMENT, INNOVATION AND COMMUNICATIONS", production team p.2 tiene "Mr. Munkhbat Perenlei, Director General of the Innovation Policy Coordination Department, MDDIC" como Initiator/Lead → **Incluido**.

## Casos edge

- **Subsidiarias gubernamentales efectivas:** AI Verify Foundation (Singapur) es "wholly-owned not-for-profit subsidiary of IMDA" → tratar como emisor gubernamental efectivo. Precedente: BSI (UK), NIST (USA).
- **Agencias creadas por ley específica:** Cyber Security Agency de Singapur, DPC de Ghana, PDPC de Singapur — emisores estatales plenos.
- **Mirrors no gubernamentales estables:** `africadataprotection.org` para Ghana NAIS, `cyrilla.org` para Mongolia PDPL. Aceptables cuando (a) el texto está ausente en dominio gubernamental, o (b) el portal oficial no expone PDF directo. Siempre dejar trazabilidad de la URL emisora en `source_url_primary`.
