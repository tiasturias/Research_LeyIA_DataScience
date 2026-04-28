Sí se puede adaptar, y la buena noticia es que tu skill **no está realmente amarrada a Claude en su lógica de negocio**: lo que domina es un sistema de reglas, criterios de inclusión/exclusión, plantillas de entregables, heurísticas y flujo operativo. En los `.md` que subiste no veo una sintaxis dependiente de Claude como XML de prompting, tool schemas propios, ni instrucciones imposibles de portar; el núcleo está en `SKILL.md`, `pipeline.md`, `deliverables.md`, `recoding.md`, `execution.md`, `findings.md` y `patterns.md`.       

La adaptación correcta, entonces, **no consiste en “traducir de Claude a GPT” frase por frase**, sino en separar tres capas:

1. **instrucción portable de skill**;
2. **instrucción operativa para Codex en repo local**;
3. **estado vivo del proyecto**.
   Eso es importante porque OpenAI hoy trata los Skills como workflows reutilizables que se pueden instalar/exportar entre productos, pero **no se sincronizan automáticamente entre ChatGPT, Codex y API**. Además, Codex respeta instrucciones de `AGENTS.md` dentro del repo, con reglas de alcance por carpeta. ([OpenAI Help Center][1])

También te tengo que marcar una realidad práctica: **si lo quieres correr “en Codex con GPT-5.4”**, hoy la documentación oficial dice que el Codex CLI/IDE extension soporta la familia **GPT-5.1-Codex** (Max por defecto, Mini opcional), seleccionable desde el model picker, `-m` o `config.toml`. Entonces la migración debe quedar **model-agnóstica para GPT-class models**, pero **operativamente Codex hoy no se documenta como un entorno “GPT-5.4”**. ([OpenAI Help Center][2])

## Veredicto técnico

Tu skill está **bien diseñada en dominio**, pero **mal separada en arquitectura para Codex**. Hoy mezcla:

* reglas estables del skill,
* documentación de referencia,
* y estado mutable del proyecto (`sample.md`, progreso, contadores, países hechos, pendientes, fechas, etc.).  

Para Codex, la arquitectura correcta es esta:

```text
repo/
├── AGENTS.md
├── .agents/
│   └── skills/
│       └── corpus-legal-ia/
│           ├── SKILL.md
│           ├── agents/
│           │   └── openai.yaml
│           ├── references/
│           │   ├── deliverables.md
│           │   ├── download.md
│           │   ├── execution.md
│           │   ├── external_trackers.md
│           │   ├── findings.md
│           │   ├── patterns.md
│           │   ├── pipeline.md
│           │   └── recoding.md
│           └── scripts/
│               ├── download_pdf.sh
│               ├── verify_pdf.sh
│               ├── build_manifest.py
│               ├── update_sample.py
│               ├── build_findings.py
│               └── validate_country_output.py
├── data/
│   ├── interim/
│   │   ├── sample_ready_cross_section.csv
│   │   └── sample.md
│   └── raw/
│       └── legal_corpus/
│           └── {ISO3}/
├── docs/
│   └── HALLAZGOS_DIFERENCIALES.md
└── MEMORY.md
```

### Por qué esta arquitectura es la correcta

`SKILL.md` debe quedar como la capa portable del workflow. Los otros `.md` son material de referencia y conviene moverlos a `references/` para que la skill sea más limpia y escalable. `sample.md`, `docs/HALLAZGOS_DIFERENCIALES.md` y los outputs por país deben quedar como **estado del repo**, no como parte del bundle lógico del skill, porque cambian todo el tiempo y si el skill se instala en varios productos se te puede desincronizar. Esa desincronización es especialmente riesgosa en tu caso porque `sample.md` es explícitamente la “única fuente de verdad” del progreso, y `execution.md` obliga a auto-actualizarlo al cerrar cada país.   ([OpenAI Help Center][1])

## Qué conservar intacto

Estas piezas **no deben perderse** porque son el poder real de la skill:

* El principio rector del pipeline: priorizar leyes vinculantes, pero acumular todo el ecosistema para distinguir `no_framework`, `strategy_only`, `soft_framework` y `binding_regulation`. 
* Las reglas de inclusión, exclusión y casos frontera de co-emisión. 
* La rúbrica de recodificación y los 4 buckets. 
* La estructura exacta de `manifest.csv`, `SOURCES.md`, `CANDIDATES.md` y el checklist final. 
* El tono: español, terse, sin emojis, cierre con pregunta de continuación. 
* Los patrones aprendidos de BGD, GHA, SGP y MNG, porque son el “criterio experto” que evita que el modelo derive regímenes mal.

## Inconsistencias que debes corregir sí o sí

### 1) `SKILL.md` habla de 3 entregables, pero el cuerpo exige 4

En el frontmatter/description se presenta como skill para generar “los 3 entregables estándar”, pero el cuerpo ya exige `manifest.csv`, `SOURCES.md`, `CANDIDATES.md`, `FINDINGS.md` y además actualizar `docs/HALLAZGOS_DIFERENCIALES.md`. Eso es inconsistente y en Codex te va a generar drift entre detección del skill y ejecución real. 

### 2) `findings.md` dice “6 secciones”, pero enumera 8

Ese archivo abre con “Esquema fijo (6 secciones, en este orden)” y luego desarrolla hasta la sección 8, mientras que `deliverables.md` exige `FINDINGS.md` con 8 secciones. Eso hay que corregir.  

### 3) `execution.md` mezcla workflow estable con estado mutable

Tiene reglas atemporales, pero también progreso puntual, listas ya completadas, 21/86, pending por lote, y backlog de FINDINGS retroactivos. Esa información debe vivir fuera del paquete portable o separarse en una zona “live project state”.  

---

# Modificación exacta por archivo

## 1) `SKILL.md`

### Qué debes cambiar

Convierte `SKILL.md` en el **control plane** del skill, no en un briefing largo. Debe:

* describir claramente **cuándo dispararse**;
* enlazar a referencias;
* delegar pasos determinísticos a scripts;
* y mencionar la convivencia con Codex/`AGENTS.md`.

### Cambios concretos

1. Corrige la descripción para que diga **4 entregables**, no 3. 
2. Haz la descripción más portable y menos “chat-only”.
3. Agrega una sección corta tipo:

   * “Cuando se use dentro de un repo con `AGENTS.md`, obedecer `AGENTS.md` para alcance local; usar esta skill como estándar metodológico portable.”
4. Cambia links directos a los `.md` sueltos por rutas bajo `references/`.
5. Reduce el cuerpo; deja instrucciones de alto nivel y manda los detalles a referencias o scripts.
6. Mantén intactas R1–R5, el pipeline de 6 capas, la prohibición de tocar `x1_master*.csv`, el tono y la obligación de actualizar `sample.md` e índice de hallazgos. 

### Cómo debería quedar conceptualmente

* Frontmatter
* Objetivo
* Reglas absolutas
* Flujo resumido
* Qué scripts ejecutar
* Qué referencias leer según etapa
* Tono de salida

### Texto de descripción recomendado

```yaml
---
name: corpus-legal-ia
description: extrae, valida y recodifica corpus legales de gobernanza de ia por país para el estudio de 86 países de leyia datascience. úsala cuando se pida procesar un país, continuar con el siguiente pendiente, validar régimen regulatorio, generar manifest.csv, sources.md, candidates.md y findings.md, o actualizar el progreso del corpus en el repositorio. compatible con chatgpt skills y con entornos codex que trabajen sobre el repo local.
---
```

## 2) `deliverables.md`

### Qué debes cambiar

El contenido es bueno y muy reusable. Aquí la adaptación es menor.

### Cambios concretos

1. Muévelo a `references/deliverables.md`.
2. Agrega al inicio una nota que diga:

   * “si falta dato verificable, marcar `N/A` o dejar vacío según la regla del campo; no inferir ni rellenar por plausibilidad”.
3. Agrega un mini bloque “validación automática recomendada” con checks que luego un script pueda correr:

   * 18 columnas en `manifest.csv`
   * encabezados exactos
   * secciones exactas en `SOURCES.md`
   * secciones exactas en `CANDIDATES.md`
   * checklist final presente.
4. No cambies las taxonomías de `doc_type`, `status`, ni la estructura de secciones. 

### Por qué

Codex rinde mejor cuando una parte del trabajo se puede verificar de forma determinística. Por eso este archivo debe seguir siendo la fuente editorial, pero complementado por un validador.

## 3) `download.md`

### Qué debes cambiar

Tu `download.md` hoy contiene buena doctrina operativa, pero **Codex necesita ejecutar scripts**, no solo leer prose.

### Cambios concretos

1. Muévelo a `references/download.md`.
2. Déjalo como documento de políticas de descarga y edge cases.
3. Extrae los comandos repetibles a scripts:

   * `scripts/download_pdf.sh`
   * `scripts/verify_pdf.sh`
4. Agrega al archivo un bloque inicial:

   * “usar primero `scripts/download_pdf.sh`; consultar este documento solo para headers especiales, mirrors y troubleshooting”.
5. Conserva:

   * curl estándar,
   * Chrome UA,
   * Referer lógico,
   * validación con `file`,
   * `shasum -a 256`,
   * uso de `pdfminer.six` para primeras páginas,
   * y la regla de nombres `{ISO3}_{ShortDocName}_{Year}.pdf`. 

### Por qué

Ese contenido es exactamente el tipo de operación donde Codex gana cuando tiene una rutina ejecutable. Además, tus propios errores comunes ya muestran que el riesgo está en WAF, redirect, HTML disfrazado de PDF y mirrors. 

## 4) `execution.md`

### Qué debes cambiar

Este archivo hoy mezcla “cómo operar” con “estado actual del proyecto”. Hay que partirlo mentalmente en dos.

### Cambios concretos

1. Muévelo a `references/execution.md`.
2. Deja solo reglas invariantes:

   * `sample.md` es source of truth
   * auto-actualización obligatoria
   * flujo de aprobación humana
   * continuidad entre sesiones
   * criterio “un país a la vez”
   * criterio de parada por país. 
3. Saca del archivo:

   * contadores actuales,
   * listas DONE/PENDING específicas,
   * países ya completados,
   * progreso 21/86,
   * backlog puntual de retro-aplicación.
     Eso debe quedar en `sample.md` o en un `STATE.md` de proyecto, no en la skill portable.  
4. Agrega una nota para Codex:

   * “antes de modificar progreso, leer `data/interim/sample.md` vigente del repo local”.

### Por qué

Si mantienes estado vivo dentro del bundle del skill, se rompe la portabilidad. Y eso choca con el hecho de que los Skills se exportan/importan entre productos pero no sincronizan automáticamente. ([OpenAI Help Center][1])

## 5) `external_trackers.md`

### Qué debes cambiar

Muy poco. Es una buena referencia.

### Cambios concretos

1. Muévelo a `references/external_trackers.md`.
2. Refuerza con una frase de apertura:

   * “esta referencia es solo discovery assist; nunca reemplaza fuente estatal ni recoding.”
3. Mantén la regla de no copiar metadata de Techieray y de usarlo solo para discovery previo. 
4. Agrega un apartado pequeño “Codex behavior”:

   * “si el entorno no tiene browser con login o navegación visual, saltar esta capa y documentar que no se ejecutó cross-check externo”.

### Por qué

En ChatGPT/Codex las capacidades de browser pueden variar por superficie. Tu skill no debe colapsar si esa capa falla; debe degradar con gracia.

## 6) `findings.md`

### Qué debes cambiar

Este archivo es muy valioso, pero necesita una corrección formal y otra operacional.

### Cambios concretos

1. Muévelo a `references/findings.md`.
2. Corrige “6 secciones” por **8 secciones**. 
3. Agrega una regla al inicio:

   * “si `manifest.csv` o `CANDIDATES.md` no permiten calcular una métrica, marcar `N/A` y documentar la razón; nunca inferir”.
4. Agrega una línea que diga:

   * “para el índice agregado, usar un script de actualización; no editar a mano si existe automatización”.
5. Mantén intactos:

   * tesis falsable,
   * stress test con al menos 2 refutaciones,
   * peer-group,
   * implicancias para el estudio,
   * banderas de revisita,
   * y el índice `docs/HALLAZGOS_DIFERENCIALES.md`. 

### Por qué

Es una pieza clave del “poder” analítico de la skill. No hay que simplificarla; hay que hacerla más robusta.

## 7) `patterns.md`

### Qué debes cambiar

Es casi perfecto para GPT/Codex. Aquí no cambies la sustancia.

### Cambios concretos

1. Muévelo a `references/patterns.md`.
2. Añade arriba una frase:

   * “estas heurísticas son tie-breakers; nunca reemplazan evidencia primaria”.
3. Mantén las lecciones de Bangladesh, Ghana, Singapur y Mongolia, y las heurísticas derivadas.
4. Agrega una mini sección final:

   * “si un caso nuevo contradice una heurística, actualizar este archivo tras aprobación humana”.

### Por qué

Este archivo es literalmente el “criterio experto acumulado” de la skill.

## 8) `pipeline.md`

### Qué debes cambiar

Muy poco en contenido; bastante en forma.

### Cambios concretos

1. Muévelo a `references/pipeline.md`.
2. Mantén las 6 capas y los criterios de inclusión/exclusión. 
3. Agrega una tabla pequeña “orden de lectura por Codex”:

   * si hay ley IA, igual correr capas 2–6;
   * si no hay ley IA, capas 2–6 completas;
   * si no hay browser, documentar ausencia de techieray;
   * si un documento es tercero, mandarlo a “Fuentes complementarias”.
4. Agrega una nota operativa:

   * “las queries se generan en inglés + idioma local cuando proceda”.

### Por qué

GPT/Codex entiende bien pipelines, pero mejora mucho si le das una secuencia operacional nítida.

## 9) `recoding.md`

### Qué debes cambiar

Casi nada semántico; sí algo de formalización.

### Cambios concretos

1. Muévelo a `references/recoding.md`.
2. Mantén intactos los 4 buckets y las reglas de decisión. 
3. Añade una sección final:

   * “salida estructurada recomendada”
   * con un bloque JSON/YAML sugerido:

     * `has_ai_law`
     * `regulatory_regime_group`
     * `regulatory_intensity`
     * `thematic_coverage`
     * `enforcement_level`
     * `confidence`
     * `justification_summary`
4. Repite expresamente que los drafts no cuentan como ley vigente. 

### Por qué

Esto te permite conectar la parte narrativa con validadores o scripts sin perder el razonamiento.

## 10) `sample.md`

### Este es el archivo más delicado

### Qué debes cambiar

**No debe ser parte del corazón portable de la skill.** Debe seguir existiendo en el repo, pero como **estado local del proyecto**. Hoy contiene la muestra de 86 países, prioridades, status, aprobaciones, fechas, contadores y regla “continúa”. 

### Cambios concretos

1. Sácalo del paquete lógico del skill si vas a distribuir la skill como reusable bundle.
2. Déjalo en `data/interim/sample.md` o genera `sample.md` desde `sample_ready_cross_section.csv`.
3. Haz que `SKILL.md` y `AGENTS.md` digan:

   * “leer `data/interim/sample.md` del repo local”.
4. Si quieres máxima robustez, crea `scripts/update_sample.py` para:

   * marcar `DONE`
   * actualizar `Aprobado`
   * recalcular contadores
   * actualizar el orden de ejecución.
5. Mantén la lógica del orden P1→P2→P3→FOCAL porque es parte del proyecto, no del modelo. 

### Por qué

Si lo dejas dentro del skill portable, se te va a fosilizar una foto parcial del proyecto.

---

# Archivo nuevo imprescindible: `AGENTS.md`

Este archivo es clave para que **Codex en VS Code/CLI/app** trabaje igual que la skill. OpenAI documenta que Codex respeta `AGENTS.md`, que su alcance cubre todo el árbol bajo la carpeta que lo contiene y que archivos más profundos prevalecen si hay conflicto. ([OpenAI][3])

## Qué debe decir `AGENTS.md`

Debe ser una traducción operativa, corta y ejecutable, del corazón de la skill. No copies todo; resume lo decisivo.

### Ejemplo recomendado

```md
# AGENTS.md

## Scope
This file governs the entire repository unless a deeper AGENTS.md overrides it.

## Purpose
This repo maintains the country-by-country AI legal corpus for the 86-country study.

## Mandatory workflow
1. Read `data/interim/sample.md` before selecting a country.
2. Process one country at a time.
3. Do not modify `data/interim/x1_master*.csv`.
4. Generate/update only:
   - `data/raw/legal_corpus/{ISO3}/manifest.csv`
   - `data/raw/legal_corpus/{ISO3}/SOURCES.md`
   - `data/raw/legal_corpus/{ISO3}/CANDIDATES.md`
   - `data/raw/legal_corpus/{ISO3}/FINDINGS.md`
   - `docs/HALLAZGOS_DIFERENCIALES.md`
   - `data/interim/sample.md`
5. Enforce R1-R5 from `.agents/skills/corpus-legal-ia/SKILL.md`.
6. Use the references under `.agents/skills/corpus-legal-ia/references/`.
7. Prefer scripts under `.agents/skills/corpus-legal-ia/scripts/` for deterministic tasks.
8. Never invent URLs, hashes, dates, or statuses.
9. Keep outputs in Spanish, terse, no emojis.

## Key references
- `.agents/skills/corpus-legal-ia/SKILL.md`
- `.agents/skills/corpus-legal-ia/references/pipeline.md`
- `.agents/skills/corpus-legal-ia/references/recoding.md`
- `.agents/skills/corpus-legal-ia/references/deliverables.md`
- `.agents/skills/corpus-legal-ia/references/findings.md`
```

---

# Scripts nuevos que deberías crear

Para mantener “el mismo poder” pero hacerlo realmente sólido en Codex, yo sí agregaría scripts. No reemplazan el juicio del modelo; automatizan lo frágil.

## Mínimos

* `download_pdf.sh`
* `verify_pdf.sh`
* `build_manifest.py`
* `update_sample.py`
* `update_hallazgos_index.py`
* `validate_country_output.py`

## Qué hace cada uno

* `download_pdf.sh`: aplica tu curl estándar con UA/Accept/Referer. 
* `verify_pdf.sh`: corre `file`, chequea tamaño y SHA-256. 
* `build_manifest.py`: arma o valida cabeceras de `manifest.csv`. 
* `update_sample.py`: actualiza `sample.md` según tus reglas. 
* `update_hallazgos_index.py`: agrega la línea de tesis resumida bajo el bucket correcto. 
* `validate_country_output.py`: confirma que existen las secciones obligatorias, los 4 outputs, los contadores y el checklist.

---

# Paso a paso exacto para hacer la migración

## Fase 1 — Reordenar arquitectura

1. Crea `references/` dentro de `.agents/skills/corpus-legal-ia/`.
2. Mueve a `references/`:

   * `deliverables.md`
   * `download.md`
   * `execution.md`
   * `external_trackers.md`
   * `findings.md`
   * `patterns.md`
   * `pipeline.md`
   * `recoding.md`
3. Deja en la raíz del skill solo:

   * `SKILL.md`
   * `agents/openai.yaml`
   * `references/`
   * `scripts/`

## Fase 2 — Corregir inconsistencias

4. Corrige `SKILL.md` para que describa 4 entregables.
5. Corrige `findings.md` para que diga 8 secciones.
6. Limpia `execution.md` de contenido mutable.

## Fase 3 — Hacerlo Codex-friendly

7. Crea `AGENTS.md` en la raíz del repo.
8. Haz que `AGENTS.md` apunte a la skill y a sus referencias.
9. Crea `scripts/` y extrae lo determinístico de `download.md`, `deliverables.md`, `execution.md` y `findings.md`.

## Fase 4 — Blindar estado vivo

10. Deja `sample.md` y `docs/HALLAZGOS_DIFERENCIALES.md` fuera del bundle conceptual del skill; trátalos como datos vivos del repo.
11. Automatiza su actualización con scripts.

## Fase 5 — Validar la migración

12. Prueba un país nuevo con un prompt local en Codex:

* “Lee AGENTS.md y `.agents/skills/corpus-legal-ia/SKILL.md`. Procesa BGR sin tocar x1_master*.csv.”

13. Verifica que produzca:

* `manifest.csv`
* `SOURCES.md`
* `CANDIDATES.md`
* `FINDINGS.md`
* update en `docs/HALLAZGOS_DIFERENCIALES.md`
* update en `sample.md`

14. Compara el resultado con el estilo y profundidad de uno de tus pilotos de referencia.

---

# Cómo mantener la misma personalidad y “poder”

La personalidad actual ya está declarada: español, terse, sin emojis, cierre corto con pregunta de continuación. Eso debe quedar duplicado en `SKILL.md` y resumido en `AGENTS.md`. 

El “poder” no viene de Claude; viene de estas cuatro cosas:

1. la taxonomía de regímenes; 
2. el pipeline de búsqueda de 6 capas; 
3. las plantillas de salida; 
4. las heurísticas aprendidas de los pilotos.

Si preservas eso y añades `AGENTS.md` + scripts + separación de estado, la skill no solo conserva su poder: **queda mejor adaptada a Codex que a su forma actual**.

## Recomendación final sobre modelo

Diseña todo para “GPT-family reasoning model”, pero en Codex hoy apunta a la familia **GPT-5.1-Codex**, no a una dependencia explícita de “GPT-5.4”. Así evitas tener que reescribir la skill cuando cambie el modelo operativo del producto. ([OpenAI Help Center][2])

El siguiente paso más útil es que te escriba una **versión nueva exacta de `SKILL.md` y `AGENTS.md`**, ya lista para pegar en tu repo.

[1]: https://help.openai.com/articles/20001066-skills-in-chatgpt?utm_source=chatgpt.com "Skills in ChatGPT | OpenAI Help Center"
[2]: https://help.openai.com/en/articles/11369540-codex-in-chatgpt?utm_source=chatgpt.com "Using Codex with your ChatGPT plan | OpenAI Help Center"
[3]: https://openai.com/es-ES/index/introducing-codex/?utm_source=chatgpt.com "Presentamos Codex | OpenAI"
