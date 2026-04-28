---
name: corpus-legal-ia
description: Extraer el corpus legal-IA de países de la muestra (86 países) del proyecto LeyIA DataScience. Úsala cuando el usuario pida procesar un país nuevo del corpus legal, continuar con el siguiente país del lote, validar regímenes regulatorios IA, o generar los 3 entregables estándar (manifest.csv + SOURCES.md + CANDIDATES.md). Disparadores típicos: "extrae corpus de {país}", "procesa {ISO3}", "continúa con el siguiente país", "¿qué corpus legal tiene {país}?".
---

# Skill: Corpus Legal-IA por País

Produces per-country legal corpus para el estudio "¿Regular o no regular?" (86 países, foco Chile 16821-19).

**Estado actual de la muestra:** ver [sample.md](sample.md) — tabla maestra con los 86 países, su status (DONE/PENDING), régimen propuesto, y fecha de completado. Es la **única fuente de verdad** del progreso.

## Reglas absolutas (R1-R5)

- **R1 — URL verificable obligatoria.** Documento sin URL de origen trazable NO entra al corpus. Sin excepciones.
- **R2 — Validación humana antes de integrar.** Nunca modificas `data/interim/x1_master*.csv`. Generas propuestas en `CANDIDATES.md`; el usuario aprueba/rechaza.
- **R3 — Acumular variedad.** Aunque encuentres ley IA-específica, sigue buscando estrategias y frameworks. Si no hay ley, extrae TODAS las iniciativas disponibles. **Priorizar leyes vinculantes > iniciativas** (más impacto en ecosistema), pero acumular ambas para cubrir los 4 regímenes posibles.
- **R4 — Fecha efectiva.** Considerar documentos hasta la fecha del sistema. No limitarse a un año.
- **R5 — Idioma.** Aceptar traducciones no oficiales si el texto oficial solo está en idioma local. Documentar como limitación.

## Lo que produces por país

En `data/raw/legal_corpus/{ISO3}/`:
1. **`manifest.csv`** — 18 columnas de trazabilidad, una fila por PDF.
2. **`SOURCES.md`** — citas APA 7 + tabla trazabilidad + evidencia oficialidad.
3. **`CANDIDATES.md`** — inventario + citas textuales + recodificación propuesta.
4. **`FINDINGS.md`** — hallazgo diferencial profundizado con métricas cuantitativas (stress test de la tesis).
5. **PDFs** descargados.

Además, tras cada país actualizas el índice agregado en `docs/HALLAZGOS_DIFERENCIALES.md`.

Ver [deliverables.md](deliverables.md) para estructura exacta de (1)-(3) y [findings.md](findings.md) para el esquema de (4) + índice agregado.

## Pipeline de 6 capas (en orden de prioridad)

1. Ley IA-específica vinculante → `binding_regulation`
2. Leyes sectoriales vinculantes (data protection, ciberseguridad, IP, sectoriales)
3. Estrategia / política nacional IA → mínimo `strategy_only`
4. Frameworks voluntarios / Model Governance / Guidelines
5. Readiness Assessments co-firmados (solo si Estado es co-emisor firmante)
6. Bills pendientes / drafts públicos

Ver [pipeline.md](pipeline.md) para detalle de capas y criterios inclusión/exclusión.

## Lo que NO haces sin aprobación humana

- Modificar `data/interim/x1_master*.csv`.
- Clasificar `binding_regulation` si hay ambigüedad.
- Saltarte países prioritarios.
- Inventar URLs o hashes.
- Tratar think tanks (Wilson, Brookings, GIZ) como emisores estatales sin co-firma.
- Asumir régimen por heurística sin leer evidencia primaria (Singapur fue el caso testigo).

## Flujo al recibir "procesa {país}"

0. **Verifica que el país está en la muestra de 86** consultando [sample.md](sample.md). Si no está, avisa al usuario y pregunta si procesar como referencia externa.
1. Lee [pipeline.md](pipeline.md) si no la tienes en contexto.
2. Consulta `data/raw/IAPP/iapp_x1_core.csv` para la codificación IAPP actual del país.
3. **Cross-check discovery en techieray** (workflow híbrido gratuito) — ver [external_trackers.md](external_trackers.md). Abrir el mapa, leer las 8 categorías del país, anotar títulos/fechas/emisores no vistos. Usar como queries dirigidas en el paso siguiente. Nunca copiar texto/metadata al corpus.
4. Ejecuta búsqueda web por las 6 capas (incorporando pistas del paso 3).
4. Descarga PDFs siguiendo [download.md](download.md).
5. Genera los 3 entregables siguiendo [deliverables.md](deliverables.md).
6. Propone recodificación siguiendo [recoding.md](recoding.md).
7. **Genera FINDINGS.md** (4º entregable) siguiendo [findings.md](findings.md) — hallazgo diferencial con evidencia cuantitativa, stress test (fortalece/refuta), peer-group, banderas de re-visita.
8. **Actualiza el índice agregado** `docs/HALLAZGOS_DIFERENCIALES.md` — agrega la entrada del país bajo su bucket de régimen, incrementa contador N/86, actualiza fecha.
9. **Auto-actualiza [sample.md](sample.md):** marca el país como DONE, actualiza régimen, contadores y lista de orden. Ver [execution.md](execution.md) §Regla de auto-actualización.
10. Presenta al usuario con resumen terse + tesis diferencial (1 línea) + pregunta de aprobación + progreso (X/86).

## Archivos de apoyo

- [sample.md](sample.md) — **TABLA MAESTRA** de los 86 países: estado, régimen, prioridad, aprobación. Source of truth del progreso.
- [execution.md](execution.md) — orden de ejecución, regla de auto-actualización, criterios de parada, continuidad entre sesiones.
- [pipeline.md](pipeline.md) — 6 capas de búsqueda + inclusión/exclusión.
- [download.md](download.md) — comandos curl, headers, patrones de error observados.
- [deliverables.md](deliverables.md) — estructura exacta de los 3 archivos.
- [recoding.md](recoding.md) — 4 buckets de régimen + reglas de decisión + escalas.
- [patterns.md](patterns.md) — lecciones de pilotos + heurísticas.
- [external_trackers.md](external_trackers.md) — trackers de terceros (techieray) + workflow híbrido de discovery.
- [findings.md](findings.md) — esquema del entregable FINDINGS.md (hallazgo diferencial + métricas cuantitativas) e índice agregado.

## Tono de comunicación con el usuario

Español. Terse. Sin emojis (salvo ✅ en tablas de diff heredadas). Links markdown clicables `[archivo](ruta)`. Final de turno: 1-2 frases + pregunta de continuación.

## Backup de emergencia

Si esta skill se pierde o está incompleta, el briefing maestro está en [docs/BRIEFING_LLM_CORPUS_LEGAL_IA.md](../../../docs/BRIEFING_LLM_CORPUS_LEGAL_IA.md) — documento autocontenido de ~670 líneas con todo el contexto.
