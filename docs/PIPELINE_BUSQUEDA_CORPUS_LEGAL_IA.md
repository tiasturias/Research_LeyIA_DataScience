# Pipeline de búsqueda del corpus legal-IA por país

**Versión:** 1.0
**Fecha:** 2026-04-15
**Aplicable a:** los 86 países de la muestra del estudio LeyIA
**Validado con:** BGD (Bangladesh) y GHA (Ghana) como pilotos

---

## Objetivo

Construir para cada país un corpus documental reproducible y trazable que soporte la recodificación de la variable **X1 (régimen regulatorio de IA)** con evidencia primaria, evitando depender exclusivamente del coding IAPP/OECD.

---

## Fase 1 — Búsqueda priorizada (orden de preferencia)

La búsqueda se hace en capas de menor a mayor incertidumbre. Cuanto más alto esté el instrumento encontrado en la lista, más peso tiene en la recodificación.

### Capa 1 — Ley IA-específica vinculante (máxima prioridad)
- Búsqueda: `"AI Act" OR "Artificial Intelligence Act" OR "Ley de IA" site:gov.{TLD}`
- Criterio: Act of Parliament / Ley del Congreso / Decreto-Ley con nombre IA explícito.
- Si se encuentra → dispara `regulatory_regime_group = binding_regulation` y `has_ai_law = 1`.

### Capa 2 — Leyes sectoriales vinculantes aplicables a IA
Buscar siempre aunque ya exista ley IA, para enriquecer el corpus:
- **Protección de datos personales** (GDPR-like, PDPA, LGPD, etc.) — aplicable a training data y decisiones automatizadas.
- **Ciberseguridad / infraestructura crítica** — aplicable a sistemas IA desplegados en sectores críticos.
- **Plataformas digitales / servicios en línea / contenido algorítmico** — aplicable a sistemas de recomendación y moderación.
- **Propiedad intelectual / copyright** — relevante para training data y outputs generativos.
- **Regulación sectorial con componente IA explícito** (banca, salud, autónomos, defensa).

Si existen → reforzan `soft_framework` o `binding_regulation` según densidad.

### Capa 3 — Estrategia / política nacional IA
- Búsqueda: `"National AI Strategy" OR "AI Roadmap" OR "Estrategia Nacional de IA" site:gov.{TLD}`
- Criterio: instrumento estatal declarativo (no vinculante), con horizonte temporal y pilares.
- Dispara mínimo `strategy_only`; combinado con Capa 2 puede justificar `soft_framework`.

### Capa 4 — Frameworks voluntarios / Model Governance / Guidelines
- Código de buenas prácticas, frameworks de gobernanza (ej. Singapore Model AI Governance Framework, Ghana Responsible AI Office guidelines).
- Toolkits oficiales (ej. AI Verify).
- Dispara densidad temática pero no cambia régimen por sí solos.

### Capa 5 — Diagnósticos / Readiness Assessments co-firmados con organismos internacionales
- UNESCO RAM, OECD AI Policy Observatory country reports, UN reports co-firmados por el gobierno.
- **Solo incluir si el Estado aparece como co-emisor firmante** (no solo como sujeto estudiado).
- Utilidad: `thematic_coverage`, contexto histórico.

### Capa 6 — Proyectos de ley pendientes / borradores públicos
- Bills en tramitación, drafts en consulta pública.
- Valor: trazabilidad de la trayectoria regulatoria; **no alteran régimen actual** pero sí `confidence` y `ai_framework_note`.

---

## Fase 2 — Criterios de inclusión/exclusión

### Incluir si cumple las tres condiciones:
1. **Emisor estatal claro** (Parlamento, Ministerio, Agencia estatal, Presidencia, autoridad regulatoria creada por ley).
2. **URL oficial verificable** (dominio `.gov.{TLD}`, organismo internacional co-firmante, o mirror de organismo intergubernamental regional). Sin URL → excluir estrictamente.
3. **Relevancia IA demostrable**: (a) IA explícita en título/contenido, o (b) ley sectorial directamente aplicable al ciclo de vida IA (datos, seguridad, plataformas), o (c) efecto histórico documentado sobre el ecosistema IA del país.

### Excluir:
- Documentos emitidos por ONGs, think tanks, cooperaciones bilaterales (GIZ, USAID, BID) sin co-firma estatal.
- Notas de prensa, blog posts, comunicados sin documento formal.
- Borradores filtrados sin publicación oficial.
- PDFs sin URL de origen verificable.

### Caso frontera: co-emisiones con organismos internacionales
- **Incluir** si el Estado firma como co-emisor (ej. AIRAM Bangladesh: UNESCO+UNDP+ICT Division GoB).
- **Excluir** si el Estado solo aparece como sujeto de estudio (ej. Wilson Center report *sobre* Ghana).

---

## Fase 3 — Técnica de descarga

1. Herramienta: `curl -sLk -A "Mozilla/5.0 ... Chrome/120"` (follow redirects, ignorar SSL cuando aplicable, bypass básico de bloqueos UA).
2. Registrar en `manifest.csv`:
   - `source_url_primary` (URL emisora oficial)
   - `source_url_mirror` (si aplica)
   - `source_domain`
   - `retrieval_http_status`
   - `retrieval_method` (comando exacto)
   - `sha256` (`shasum -a 256`)
   - `size_bytes`
3. Si una URL oficial devuelve 404/loop/403 sistemáticamente: documentar en notas, buscar mirror gubernamental, o registrar como "no descargable" manteniendo la trazabilidad.
4. Nombrado: `{ISO3}_{ShortDocName}_{Year}.pdf` (ej. `SGP_ModelAIGovFramework_v2_2024.pdf`).

---

## Fase 4 — Documentación entregable por país

Por cada país se genera en `data/raw/legal_corpus/{ISO3}/`:

### `manifest.csv`
Una fila por documento descargado, con 18 campos de trazabilidad.

### `SOURCES.md`
- Citas APA 7 de todos los documentos.
- Tabla de trazabilidad con URL/hash/tamaño/HTTP.
- Evidencia de oficialidad por documento (portada, acknowledgements, co-firmantes, dominio).
- Sección "Fuentes complementarias no incorporadas" (para transparencia).
- Notas de proceso (URLs no accesibles, decisiones editoriales).

### `CANDIDATES.md`
Entregable principal para validación humana. Estructura:
1. Codificación actual (IAPP) — estado base.
2. Inventario de instrumentos estatales identificados (tabla — incluye los no descargables).
3. Un candidato por documento descargado, con:
   - Metadatos completos.
   - Citas textuales clave que justifican cambios de coding.
4. **Recodificación X1 propuesta**, variable por variable, con justificación citada.
5. Diff summary (bloque de código con cambios concretos).
6. Fundamento del upgrade/downgrade de régimen.
7. Checklist de validación humana por candidato (6-7 ítems).
8. Bloque de decisión del revisor (APROBAR/RECHAZAR/PEDIR OTRA FUENTE).
9. Notas del codificador (limitaciones, diferencias frente al baseline).

---

## Fase 5 — Validación humana (obligatoria)

El codificador (Claude) **nunca** marca la recodificación como integrada al pipeline. El usuario:
- Aprueba/rechaza candidato por candidato.
- Aprueba/modifica el diff propuesto.
- Decide sobre upgrades de régimen (el cambio de bucket es la decisión más sensible).

Solo tras aprobación se integra a `data/interim/x1_master_v2.csv`.

---

## Fase 6 — Criterios de decisión de régimen

Los 4 buckets de `regulatory_regime_group`:

| Régimen | Condiciones suficientes |
|---|---|
| `no_framework` | No hay estrategia, ley IA, ni leyes sectoriales relevantes vinculantes en vigor |
| `strategy_only` | Solo estrategia/política declarativa, sin base legal sectorial vinculante relevante ni autoridad designada |
| `soft_framework` | Cualquiera de: (a) estrategia + ≥1 ley sectorial vinculante con autoridad activa relevante para IA, (b) policy/framework con obligaciones concretas (AIAs, red lines, liability) aunque sin ley IA, (c) autoridad IA específica designada con mandato real, (d) pathway legislativo declarado con fecha |
| `binding_regulation` | Ley IA-específica vigente (Act of Parliament o equivalente) con autoridad IA y poderes sancionatorios |

**Regla del estudio:** ante duda entre dos buckets, aplicar el criterio del codificador con justificación explícita en CANDIDATES.md. El revisor humano tiene última palabra.

---

## Fase 7 — Política de actualización

- Si entre la fecha de captura y la fecha de análisis aparece un documento nuevo (ej. AI Act promulgado, nueva versión de estrategia), **re-capturar** manteniendo archivos históricos y agregando los nuevos con nuevo `retrieved_date` y nuevo hash.
- Nunca sobrescribir un archivo descargado: cada versión es evidencia histórica del estudio.

---

## Aplicación ordenada a los 86 países

**Pilotos completados (validados):** BGD, GHA.
**Siguiente en ejecución:** SGP (Singapur).
**Pendientes prioritarios (baja confianza IAPP):** BHR, BLR, BLZ, BRB, CMR, JOR, LBN, LKA, MNG, PAK, PAN, PHL, SYC, TWN.
**Resto:** resto de la muestra según criterio del usuario.
