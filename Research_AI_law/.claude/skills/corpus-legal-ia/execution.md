# Plan de ejecución y tracking de progreso

## Source of truth

El estado completo de los 86 países de la muestra está en **[sample.md](sample.md)** — tabla maestra con ISO3, prioridad, status, régimen propuesto y fecha de completado. **Es la única fuente de verdad** para saber qué países están hechos y cuáles faltan.

## Regla de auto-actualización (OBLIGATORIA)

**Al terminar cada país** (después de generar los 3 entregables y ANTES de presentar el resumen al usuario), la skill DEBE:

1. Actualizar la fila del país en [sample.md](sample.md):
   - `Status` → `DONE`
   - `Régimen propuesto` → el régimen clasificado
   - `Aprobado` → `Pendiente` (hasta que el usuario apruebe; luego cambiar a `Sí`)
   - `Fecha` → fecha del sistema
2. Actualizar los contadores al final de [sample.md](sample.md):
   - `Completados (en muestra)` → N+1 / 86
   - `Pendientes` → 86-(N+1) / 86
3. Actualizar la lista de orden de ejecución (marcar ✅ junto al ISO3).

**Al recibir aprobación del usuario** para un país:
1. Cambiar `Aprobado` → `Sí` en [sample.md](sample.md).

**Nunca saltarse esta actualización.** Si se olvida, el estado se desincroniza y la regla "continúa" no funciona.

## Orden de ejecución (referencia rápida)

### P1-TOP30 — Top 30 Microsoft AI Diffusion 2025 (29 en muestra)

Agrupados por similitud regulatoria para eficiencia de contexto compartido:

**Grupo A — Golfo / Medio Oriente (4 países):**
1. ARE ✅ — #1 ranking. soft_framework. Aprobado.
2. ISR ✅ — #12 ranking. soft_framework. Pendiente aprobación.
3. JOR — #29 ranking. AI Strategy 2023, Data Protection Law 2023. **DIFERIDO** (baja relevancia relativa; procesar después del Grupo B si el usuario lo decide).

**Grupo B — EU AI Act jurisdictions (15 países):**
Comparten AI Act (Reg. 2024/1689) + GDPR. Variación en transposición nacional.
4. IRL (#4), 5. FRA (#5), 6. ESP (#6), 7. NLD (#9), 8. BEL (#14), 9. SWE (#16), 10. AUT (#17), 11. HUN (#18), 12. DNK (#19), 13. DEU (#20), 14. POL (#21), 15. CZE (#24), 16. ITA (#26), 17. FIN (#27), 18. BGR (#28).

**Grupo C — EEA no-UE + UK (3 países):**
19. NOR (#3), 20. GBR (#8), 21. CHE (#15).

**Grupo D — Commonwealth desarrollado (3 países):**
22. NZL (#7), 23. AUS (#11), 24. CAN (#13).

**Grupo E — Asia restante (1 país):**
25. KOR (#25).

**Grupo F — Américas (2 países):**
26. USA (#23), 27. CRI (#30).

**Ya completados del Top 30:**
- SGP (#2) ✅, TWN (#22) ✅.

### P2-IAPP-LOW — Países IAPP baja confianza (20 en muestra)

Procesar después del Top 30: ARM, BHR, BLR, BLZ, BRB, CMR, ECU, ISL, KAZ, LBN, LKA, MAR, MEX, MYS, PAK, PAN, PHL, RUS, SRB, SYC, THA, TUN, UGA, UKR, URY.

Ya completados: BGD ✅, GHA ✅, MNG ✅.

### P3-SAMPLE — Resto de muestra (31 países)

Procesar después de P2: ARG, BRA, CHN, COL, CYP, EGY, EST, GRC, HRV, IDN, IND, JPN, KEN, LTU, LUX, LVA, MLT, MUS, NGA, PER, PRT, ROU, SAU, SVK, SVN, TUR, VNM, ZAF.

### FOCAL — Chile

CHL — procesar DESPUÉS de cubrir al menos el Top 30 para tener contexto comparado sólido.

## Criterios de parada por país

Detener búsqueda cuando:
- Ley IA encontrada (si existe).
- Al menos 1 ley sectorial vinculante relevante (data protection como mínimo).
- Estrategia IA principal encontrada (si existe).
- 1-3 frameworks/guidelines oficiales (si existen).
- Total 3-8 documentos es óptimo. Más de 10 es sobre-exhaustivo.
- Si ecosistema rico (SGP, UE, KOR): llegar hasta 7-10 documentos.

## Continuidad entre sesiones

### Al inicio de sesión

1. Lee `MEMORY.md` en el directorio de memoria del proyecto.
2. Lee [sample.md](sample.md) para estado actualizado.
3. Lee los memos relevantes si aplica.
4. Pregunta al usuario qué países procesar.
5. **NO empieces descarga** hasta que diga "dale" o equivalente.

### Al final de sesión

1. Resume países completados, con links a sus `CANDIDATES.md`.
2. Indica progreso: "X/86 completados, Y pendientes del lote actual".
3. Si descubriste patrones nuevos, actualiza [patterns.md](patterns.md).
4. No dejes archivos temporales.

### Si el usuario dice "continúa" sin especificar país

Consultar [sample.md](sample.md). Tomar el siguiente PENDING según el orden P1→P2→P3→FOCAL. Ritmo: **un país a la vez**.

## Flujo validación humana

### Lo que SIEMPRE pides al terminar un país

- Resumen: nº de PDFs, régimen propuesto, comparación con IAPP (si hay fila).
- Link al `CANDIDATES.md`.
- Pregunta explícita: "¿Apruebas, rechazas, o pides otra fuente?"
- Pregunta de continuación: "¿Sigo con {siguiente_país} o preferís otro?"
- Progreso: "Llevamos X/86 de la muestra (Y/29 del Top 30)."

### Lo que NUNCA haces sin aprobación

- Integrar recodificación a `x1_master.csv` o `x1_master_v2.csv`.
- Modificar archivos fuera de `data/raw/legal_corpus/{ISO3}/`.
- Clasificar país como `binding_regulation` si hay ambigüedad.
- Saltarte países prioritarios de baja confianza.

### Lo que haces tras aprobación

1. Marcar `Revisor humano: [APROBADO — {FECHA}]` en `CANDIDATES.md`.
2. Actualizar `Aprobado` → `Sí` en [sample.md](sample.md).
3. Preparar CSV de recodificación si el usuario lo pide.
4. Seguir con el siguiente país.

## Pendiente: retro-aplicación FINDINGS.md para países completados antes de la skill v2

FINDINGS.md se incorporó como 4º entregable tras AUS (21/86). Los 20 países completados previamente NO tienen FINDINGS.md generado. Lista:

ARE, SGP, TWN, ISR, IRL, FRA, ESP, NLD, BEL, SWE, AUT, HUN, DNK, DEU, NOR, NZL, GBR, BGD, GHA, MNG.

**Cuándo ejecutar:** tras terminar el lote P1-TOP30 (o cuando el usuario lo solicite). No intercalar con países nuevos — respeta el criterio "no atrasar la extracción".

**Cómo ejecutar:** pasada dedicada, genera los 20 FINDINGS.md desde manifest.csv + CANDIDATES.md§Hallazgo diferencial, sin re-descargar ni re-buscar. Al terminar, actualiza `docs/HALLAZGOS_DIFERENCIALES.md` con las 20 entradas en un solo commit lógico.

## Estimación total

- 86 países × 35 min promedio = ~50 horas de trabajo activo del LLM.
- Distribuido en sesiones de 3-5 países (~2h por sesión) → ~12-17 sesiones.
- El usuario autoriza sesión por sesión. No propongas hacer todo de una.
