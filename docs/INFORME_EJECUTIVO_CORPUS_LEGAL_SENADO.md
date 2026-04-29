# Informe Ejecutivo: Extracción del Corpus Legal-IA

## ¿Qué datos se recolectaron de los países del mundo para informar la Ley de Inteligencia Artificial de Chile?

**Proyecto:** *"¿Regular o no regular? Impacto de la regulación de IA en los ecosistemas nacionales"*  
**Boletín de referencia:** 16821-19 (Ley Marco de IA)  
**Fecha:** Abril 2026  
**Elaborado para:** Honorable Senado de Chile

---

## 1. ¿Qué es el Corpus Legal-IA y por qué importa?

Cuando un país decide regular la inteligencia artificial, no lo hace en el vacío. Cada gobierno del mundo ha tomado decisiones distintas: algunos ya tienen leyes aprobadas, otros solo estrategias en papel, y varios aún no han comenzado.

El **Corpus Legal-IA** es el conjunto de documentos oficiales —leyes, estrategias, guías y proyectos de ley— que 38 países del mundo han producido sobre inteligencia artificial. Es como una biblioteca forense que nos permite comparar, país por país, *qué* se reguló, *cómo* se reguló y *con qué resultados* para su ecosistema digital.

Este informe explica, en lenguaje claro, cómo se construyó esa biblioteca y qué hallazgos ofrece para la discusión del proyecto de ley chileno.

---

## 2. ¿Cómo se extrajo? El método de las "seis capas"

Imaginemos que la regulación de IA es una pirámide. No todos los países están en la cima; la mayoría está en los escalones intermedios. Para no perdernos nada, el equipo de investigación diseñó un sistema de búsqueda en **seis niveles**, del más obligatorio al más preparatorio:

### Capa 1: Leyes específicas de IA (la cima)
Documentos con fuerza de ley que mencionan explícitamente a la inteligencia artificial.  
*Ejemplo:* La Unión Europea aprobó el *AI Act* en 2024; Corea del Sur promulgó su *AI Basic Act* en 2025. Taiwán tiene su propia ley desde 2026.

### Capa 2: Leyes sectoriales que afectan a la IA
Normas vigentes de protección de datos, ciberseguridad o propiedad intelectual que, aunque no mencionen "IA" en su título, regulan directamente su uso.  
*Ejemplo:* En Singapur, la ley de protección de datos personales (*PDPA*) rige cómo las empresas de IA manejan la información ciudadana, aunque no exista una "Ley de IA" como tal.

### Capa 3: Estrategias nacionales de IA
Planes gubernamentales que declaran la intención de desarrollar o regular la IA, pero sin fuerza legal vinculante.  
*Ejemplo:* Chile publicó su *Política Nacional de IA* en 2024. Estados Unidos, Australia y el Reino Unido también se mueven primero por estrategias antes que por leyes horizontales.

### Capa 4: Marcos voluntarios y guías técnicas
Códigos de buenas prácticas, checklists de gobernanza o criterios de seguridad publicados por agencias estatales. No son leyes, pero moldean el comportamiento de la industria.  
*Ejemplo:* Alemania produce guías técnicas del BSI (agencia de ciberseguridad) sobre cómo usar IA de forma segura en la administración pública.

### Capa 5: Diagnósticos oficiales co-firmados
Evaluaciones de madurez digital firmadas conjuntamente por el Estado y organismos internacionales como UNESCO o PNUD.  
*Ejemplo:* Mongolia co-editó con la UNESCO una evaluación de preparación para la IA en 2025.

### Capa 6: Proyectos de ley y borradores públicos
Iniciativas legislativas en trámite que permiten ver hacia dónde apunta un país.  
*Ejemplo:* Alemania tiene el *KI-MIG* (proyecto de ley de implementación del AI Act) en primera lectura parlamentaria; Canadá tenía el *AIDA* (Bill C-27), que quedó en suspenso por disolución parlamentaria en 2025.

> **Regla de oro:** se buscó todo, pero se priorizó lo vinculante. Una ley vale más que una estrategia, pero una estrategia vale más que el silencio. Si un país solo tiene estrategia, eso también se registró.

---

## 3. ¿Qué se descartó? Transparencia metodológica

No todo lo que aparece en Google califica como documento oficial. Se excluyeron deliberadamente:

- **Think tanks y ONGs sin co-firma estatal:** Informes de Brookings, GIZ o BID se leyeron como contexto, pero no entraron al corpus oficial.
- **Notas de prensa y blogs gubernamentales:** Informan, pero no regulan.
- **Borradores filtrados sin publicación oficial:** No son verificables.
- **Documentos sin URL de origen trazable:** Si no se puede demostrar de dónde salió, no entra.

> *Ejemplo real:* Ghana produce una guía de IA con apoyo de GIZ, pero como no está firmada por el Estado como co-emisor, quedó fuera del corpus principal y se registró solo como "fuente complementaria".

---

## 4. Los cuatro entregables por país: qué se guardó

Para cada uno de los 38 países procesados, el equipo generó cuatro documentos estandarizados:

### 4.1 Manifesto de trazabilidad (`manifest.csv`)
Una tabla que registra cada PDF descargado con:
- Título exacto del documento
- Fecha de publicación
- Quién lo emitió (Parlamento, Ministerio, agencia regulatoria)
- URL de descarga
- Firma digital (SHA-256) para garantizar que el archivo no fue alterado
- Número de páginas
- Estado vigente: ¿está en force, es un borrador, fue derogado?

*Para qué sirve:* si un asesor parlamentario dice "demuéstreme que esa ley existe", se puede abrir el PDF original y verificar su autenticidad.

### 4.2 Fuentes y citas (`SOURCES.md`)
Citas en formato académico (APA 7) de cada documento, más una evidencia de oficialidad: ¿el PDF está alojado en un dominio `.gov`? ¿Tiene firma de un ministro? ¿Aparece en el Diario Oficial equivalente?

### 4.3 Propuesta de recodificación (`CANDIDATES.md`)
Este es el documento más político. Compara la clasificación previa que existía en bases de datos internacionales (IAPP Tracker) contra lo que el equipo encontró al leer los textos originales.

*Ejemplo concreto:*  
- La base de datos IAPP decía que Singapur tenía "estrategia sin ley" (*strategy_only*).  
- Al leer sus 7 documentos oficiales, el equipo descubrió que tiene una densidad regulatoria tan alta (guías de gobernanza, sandbox obligatorio, leyes sectoriales de datos y ciberseguridad) que propuso reclasificarlo como *soft_framework* (marco blando robusto).  
- Singapur tiene una política pública explícita de **NO crear una ley horizontal de IA**, a diferencia de la UE.

### 4.4 Hallazgo diferencial (`FINDINGS.md`)
Un análisis cualitativo que responde: "¿Qué hace distinto a este país en el mundo?"  
*Ejemplos reales extraídos:*

- **Alemania:** Tiene un "patrón dual": retraso legal formal (incumplió el plazo de agosto 2025 para implementar el AI Act), pero adelanto administrativo real (su agencia BNetzA ya opera una mesa de servicio de IA desde 2024).
- **Dinamarca:** Fue el primer país de la UE en tener ley nacional de implementación del AI Act en vigor (agosto 2025).
- **Australia:** Consultó durante meses si hacer una ley obligatoria, y en diciembre de 2025 decidió explícitamente **no hacerla**, optando por estándares voluntarios.
- **Emiratos Árabes Unidos:** Creó el primer Ministerio de IA del mundo en 2017 y tiene regulación sectorial vinculante en la zona financiera (DIFC).
- **Costa Rica:** Es el primer país de Latinoamérica y Centroamérica con una Estrategia Nacional de IA dedicada (2024-2027).
- **Estados Unidos:** No tiene ley federal de IA, pero su gobierno ejecutivo impuso obligaciones concretas: cada agencia federal debe nombrar un "Jefe de Inteligencia Artificial" (CAIO), hacer inventarios de sistemas de riesgo y reportar al Congreso.

---

## 5. Las cuatro "familias" de regulación que emergieron

De leer los documentos de 38 países surgieron cuatro grupos naturales, que el equipo llamó **regímenes regulatorios**:

### A. `binding_regulation` — Leyes duras y comprensivas
Países con leyes de IA aprobadas y vigentes, con autoridades designadas y poderes sancionatorios.  
*En la muestra:* Unión Europea (AI Act), Corea del Sur, Taiwán, Hungría, Dinamarca, Finlandia, Japón, Polonia, Francia, España, entre otros.

### B. `soft_framework` — Reglas sin ley horizontal, pero con dientes
Países que decidieron **no crear una ley general de IA**, pero compensan con leyes sectoriales vigentes (datos, ciberseguridad), guías técnicas obligatorias en la práctica y autoridades activas.  
*En la muestra:* Singapur, Reino Unido, Estados Unidos, Suiza, Canadá (aunque su proyecto murió), Australia, Israel, India, Emiratos Árabes, Noruega, Costa Rica.

### C. `strategy_only` — Planes en papel, sin respaldo legal
Países con estrategias o políticas nacionales publicadas, pero sin leyes sectoriales robustas ni autoridades designadas para hacerlas cumplir.  
*En la muestra:* Armenia, Líbano, Camerún.

### D. `no_framework` — Sin marco regulatorio de IA
Países donde no se encontró estrategia, ley ni iniciativa estatal significativa sobre IA.  
*En la muestra:* Aún en revisión para los 38 procesados.

> **Para el caso chileno:** Chile aparece hoy como *strategy_only* en la base IAPP, porque tiene la Política Nacional de IA (2024) y el Boletín 16821-19 está en trámite en el Senado. El corpus legal no ha sido procesado aún para Chile, pero se planifica hacerlo tras completar el lote prioritario de 30 países.

---

## 6. ¿Qué datos nuevos se lograron extraer?

Además de clasificar a cada país, el corpus permitió crear variables que no existían en ninguna base de datos internacional:

| Variable nueva | ¿Qué mide? | Ejemplo práctico |
|---|---|---|
| `has_dedicated_ai_authority` | ¿El país designó una autoridad específica para la IA? | Alemania designó a BNetzA; Irlanda creó una AI Office; España tiene la AESIA. |
| `ai_law_pathway_declared` | ¿Existe un proyecto de ley de IA con fecha pública de avance? | Alemania: KI-MIG en primera lectura (marzo 2026). Canadá: AIDA murió (enero 2025). |
| `ai_corpus_n_documents` | ¿Cuántos documentos oficiales tiene el país sobre IA? | Alemania: 8 documentos. Costa Rica: 3 documentos. |
| `ai_corpus_total_pages` | ¿Cuántas páginas suma su regulación? | Alemania: ~310 páginas. Bangladesh: ~100 páginas. |
| `ai_corpus_years_span` | ¿Desde cuándo viene trabajando el tema? | Alemania: desde diciembre de 2020 (5 años de trayectoria). |

Estas variables permiten responder preguntas como:  
- ¿Los países que designaron una autoridad de IA específica tienen mejores resultados en adopción tecnológica?  
- ¿Los países con más documentos regulatorios atraen más inversión, o la ahuyentan?

---

## 7. Estado del corpus y próximos pasos

| Estado | Número de países |
|---|---|
| **Total muestra del estudio** | 86 |
| **Procesados con corpus completo** | **38** |
| **Pendientes de extracción** | 48 |
| **En proceso prioritario (Top 30)** | 29 completados + Chile focal |

Los 38 países con corpus representan el 44 % de la muestra, pero cubren el espectro completo de riqueza económica, regiones geográficas y modelos regulatorios.

---

## 8. Mensaje clave para el debate legislativo

El Corpus Legal-IA demuestra tres cosas que son relevantes para el Senado:

1. **No hay un único modelo correcto.** La UE optó por ley horizontal vinculante; Singapur y Reino Unido por marcos blandos sectoriales; Australia consultó y decidió no legislar. Cada elección tiene trade-offs entre innovación y protección.

2. **El mundo no espera.** Países como Dinamarca, Hungría y Finlandia ya tienen leyes nacionales de implementación del AI Act en vigor. Taiwán aprobó su ley en 2026. Chile está en una ventana de tiempo donde aún puede aprender de estos casos.

3. **La "calidad" de la regulación no se mide solo por tener una ley.** Se mide por si hay autoridades designadas, si los documentos son verificables, si hay trayectoria de enforcement y si el ecosistema responde. El corpus permite comparar a Chile no solo contra la UE, sino contra países de ingreso medio (Costa Rica, Ghana, Jordania) que están tomando decisiones similares.

---

**Documentos de referencia:**
- Plan de consolidación del corpus: `PLAN_CONSOLIDACION.md`
- Hallazgos diferenciales por país: `docs/HALLAZGOS_DIFERENCIALES.md`
- Notebook de análisis exploratorio (ADE v2): `ADE/01_ADE_Analisis_Exploratorio.ipynb`
- Metodología completa de la skill: `.claude/skills/corpus-legal-ia/SKILL.md`

---

*Informe elaborado por el equipo del proyecto LeyIA DataScience, IMT3860 — Introducción a Data Science, Pontificia Universidad Católica de Chile, abril 2026.*
