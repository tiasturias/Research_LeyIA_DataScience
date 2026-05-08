# Techieray Global AI Regulation Tracker — Extracción Manual de Metadatos

**Propósito:** Resolver el cuello de botella de la fuente IAPP, que solo tiene datos completos para 18 de los 43 países de la muestra. Esta extracción manual proveerá variables predictoras (X1) con cobertura completa (~43 países).

**Fuente:** [Global AI Regulation Tracker — Techieray Labs](https://www.techieray.com/GlobalAIRegulationTracker)  
**Autor del tracker:** Raymond Sun  
**API disponible:** `pip install techieray-ai-reg-tracker-api` (plan Mini $25/mes para 200 calls)

---

## Cómo usar los archivos de esta carpeta

Hay **43 archivos** con el formato `ISO3-Nombre.md` (ej. `DEU-Germany.md`, `CHL-Chile.md`). Cada archivo contiene una **plantilla estructurada** con 9 variables a extraer:

### Variables a completar

| Variable | Tipo | Pregunta |
|---|---|---|
| `tr_ley_ia_vigente` | Binaria (SI/NO) | ¿Tiene ley de IA vigente? |
| `tr_proyecto_ley_ia` | Binaria (SI/NO) | ¿Tiene proyecto de ley de IA en trámite? |
| `tr_n_leyes_vigentes` | Conteo | ¿Cuántas leyes de IA vigentes? |
| `tr_n_proyectos_ley` | Conteo | ¿Cuántos proyectos de ley en trámite? |
| `tr_tiene_estrategia_nacional` | Binaria (SI/NO) | ¿Tiene estrategia nacional de IA? |
| `tr_tiene_guia_softlaw` | Binaria (SI/NO) | ¿Tiene guías, frameworks o soft law de IA? |
| `tr_tiene_autoridad_dedicada` | Binaria (SI/NO) | ¿Tiene autoridad específica de IA? |
| `tr_n_instrumentos_total` | Conteo | Número total de instrumentos regulatorios |
| `tr_ultima_actualizacion` | Fecha | Último desarrollo regulatorio registrado |

### Proceso para cada país

1. Abrir el perfil del país en el tracker: `https://www.techieray.com/GlobalAIRegulationTracker#XX` (donde XX es el código ISO de 2 letras, ej. DE, CL, SG)
2. Revisar las 3 categorías: **Latest Macro Developments**, **Sector Developments**, **Bilateral & Multilateral Developments**
3. Para cada entrada relevante, anotar: fecha, título, tipo de instrumento (ley, proyecto, guía, estrategia, decreto)
4. Completar la plantilla del archivo `ISO3-Nombre.md` con los valores extraídos
5. Marcar el estado como ✅ Completado al terminar

### Orden de extracción recomendado

1. **Benchmarks prioritarios (7):** SGP, EST, IRL, ARE, KOR, URY, BRA
2. **País focal:** CHL
3. **Potencias IA:** USA, CHN, IND, JPN
4. **Pioneros consistentes:** DEU, FRA, GBR, NLD
5. **LATAM restantes:** ARG, COL, MEX, PER, CRI
6. **Europa restante:** 16 países europeos
7. **Otros:** AUS, NZL, CAN, ISR, QAT, TWN

### Validación cruzada con IAPP

Para los 18 países que tienen datos en AMBAS fuentes (IAPP + Techieray):
- Comparar `tr_ley_ia_vigente` con `iapp_ley_ia_vigente`
- Comparar `tr_proyecto_ley_ia` con `iapp_proyecto_ley_ia`
- Si hay discrepancia, preferir la fuente más reciente y documentar
- Los 18 países IAPP son: ARE, SGP, NZL, GBR, AUS, ISR, CAN, KOR, TWN, CHL, USA, CHN, IND, JPN, ARG, BRA, COL, PER

### Tiempo estimado

~10-15 minutos por país × 43 países ≈ **8-11 horas de trabajo total**.
