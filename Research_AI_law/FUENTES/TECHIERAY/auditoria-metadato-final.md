# Auditoría de Resultados - Metadata Regulatoria de IA (Mayo 2026)

## Análisis General del Archivo `tr_regulatory_metadata.csv`

El archivo define atributos clave sobre la postura regulatoria de varios países (Categoría de obligatoriedad, Gobernanza, Autoridades, Leyes vigentes, etc.). Tras contrastar los datos contra la evidencia legislativa de **mayo 2026**, se detectaron los siguientes problemas principales:

1. **China (CHN):** Está categorizada como `non-binding` (no vinculante). Esto es **incorrecto**. China tiene uno de los marcos de IA más estrictos y vinculantes del mundo (Medidas de IA Generativa de 2023, Recomendación de Algoritmos, y enmiendas a la Ley de Ciberseguridad vigentes desde enero de 2026 que imponen multas inmediatas). La categoría debe ser `binding` o `strict`.
2. **Unión Europea (AUT, BEL, DEU, FRA, etc.):** El CSV etiqueta a todos los países del EU AI Act como `non-binding` en la columna de obligatoriedad. Esto es **gravemente incorrecto**. El EU AI Act es un reglamento de aplicación directa, y sus requisitos (aunque progresivos hacia agosto 2026 y dic 2027) son obligatorios (`binding`). 
3. **Taiwán (TWN):** Muestra "mixed" en la obligatoriedad. Con la *Artificial Intelligence Basic Act* aprobada en dic 2025 (y ya vigente), el país avanzó a un modelo regulado.
4. **Corea del Sur (KOR):** Tiene la *Basic AI Act* aprobada, por lo que su obligatoriedad empieza a transicionar, aunque `mixed` o `non-binding` (por el periodo de gracia) es debatible.
5. **Leyes Vigentes (`trleyvigente`):** Hay inconsistencias arrastradas de auditorías anteriores (ej. Europa marcada con `1` cuando la ley de IA general no es plenamente aplicable, pero sí está en vigor parcial).

---

## Cambios Recomendados por Filas (Formato CSV)

A continuación, presento el texto exacto con el que debes reemplazar tu archivo. Se han corregido las columnas `trleyiavigentetrproyectoleyia` (ajustadas según auditorías previas de la UE), y la columna de **obligatoriedad** (`trcategoriaobligatoriedad`), que ahora refleja la realidad de 2026.

```csv
iso3,trleyiavigentetrproyectoleyiatrestrategianacionaliatrtieneguiasoftlawtrtieneautoridaddedicadatrcategoriaobligatoriedadtrnleyesrelacionadastrnautoridadestrsandboxregulatoriotrmarcosvoluntariostrinstitutoseguridadiatrherramientastestingtrmodelogobernanzatradhiereoecdtradoptounesco
ARG,0,1,1,1,1,non-binding,centralized,0,1
BRA,0,1,1,1,1,non-binding,centralized,0,1
CAN,0,0,1,1,1,non-binding,centralized,1,1
CHL,0,1,1,1,0,non-binding,none,1,1
COL,0,1,1,1,0,non-binding,none,1,1
CRI,0,1,0,0,0,non-binding,none,1,1
MEX,0,1,0,0,0,non-binding,none,1,1
PER,0,1,0,0,0,non-binding,none,0,1
URY,0,0,1,1,0,non-binding,none,0,1
USA,0,1,1,1,1,non-binding,centralized,1,1
AUS,0,0,1,1,1,non-binding,centralized,1,1
NZL,0,0,1,1,0,non-binding,none,1,1
CHN,0,1,1,1,1,binding,centralized,0,1
IND,0,1,1,1,1,non-binding,centralized,0,1
JPN,0,1,1,1,1,non-binding,centralized,1,1
KOR,0,1,1,1,1,mixed,centralized,1,1
SGP,0,0,1,1,0,non-binding,none,0,1
TWN,1,0,1,1,1,mixed,centralized,0,1
ISR,0,0,1,1,1,non-binding,centralized,1,1
ARE,0,0,1,1,1,non-binding,centralized,0,1
QAT,0,0,1,0,0,non-binding,none,0,1
AUT,0,1,1,1,1,binding,eudelegated,1,1
BEL,0,1,1,1,1,binding,eudelegated,1,1
BGR,0,1,1,1,1,binding,eudelegated,0,1
HRV,0,1,1,1,1,binding,eudelegated,0,1
CZE,0,1,1,1,1,binding,eudelegated,1,1
DNK,0,1,1,1,1,binding,eudelegated,1,1
EST,0,1,1,1,1,binding,eudelegated,1,1
FIN,0,1,1,1,1,binding,eudelegated,1,1
FRA,0,1,1,1,1,binding,eudelegated,1,1
DEU,0,1,1,1,1,binding,eudelegated,1,1
GRC,0,1,1,1,1,binding,eudelegated,1,1
HUN,0,1,1,1,1,binding,eudelegated,1,1
IRL,0,1,1,1,1,binding,eudelegated,1,1
ITA,0,1,1,1,1,binding,eudelegated,1,1
NLD,0,1,1,1,1,binding,eudelegated,1,1
POL,0,1,1,1,1,binding,eudelegated,1,1
ROU,0,1,1,1,1,binding,eudelegated,0,1
ESP,0,1,1,1,1,binding,eudelegated,1,1
SWE,0,1,1,1,1,binding,eudelegated,1,1
GBR,0,1,1,1,1,non-binding,centralized,1,1
CHE,0,1,1,1,0,non-binding,none,1,1
```

*(Nota: En el archivo corregido he colapsado las banderas binarias separadas por comas, asumiendo el formato estándar CSV, ya que en el raw que compartiste estaban pegadas como `01111`. Dejé el formato separado por comas para que sea legible y evite errores de parsing en tu base de datos).*

### Justificación detallada de los cambios:

1. **China (CHN):** 
   - *Cambio:* Obligatoriedad de `non-binding` a `binding`.
   - *Justificación:* En mayo de 2026, China tiene el modelo regulatorio más estructurado y obligatorio del mundo. Las enmiendas a su Ley de Ciberseguridad (vigentes desde el 1 de enero de 2026) introdujeron sanciones inmediatas y severas para fugas de datos de IA. Además, exige a las empresas extranjeras registros obligatorios de algoritmos ante la CAC y etiquetado obligatorio [web:96][web:99].
2. **Países del EU AI Act (Europa):**
   - *Cambio:* Obligatoriedad de `non-binding` a `binding`. 
   - *Cambio en Ley Vigente/Proyecto:* Ajustado a `0` y `1` (como detectamos en la auditoría previa) porque el reglamento está en etapa de aplicación progresiva (agosto 2026), y los estados deben tramitar leyes locales de adecuación y crear sandboxes para agosto de 2026 [web:96][web:97].
   - *Justificación:* El EU AI Act no es *soft law*; impone obligaciones vinculantes y estrictas, respaldadas por multas que van hasta el 7% de la facturación global, dependiendo de la categoría de riesgo de la IA [web:96].
3. **Corea del Sur (KOR):**
   - *Cambio:* Obligatoriedad a `mixed`.
   - *Justificación:* Con su *Basic AI Act* aprobada en dic 2025 y en periodo de gracia durante 2026, el país está transicionando de normas voluntarias a requerimientos legales fijos para sistemas de alto impacto [web:96].
4. **Canadá (CAN):**
   - *Cambio:* ProyLey a `0`.
   - *Justificación:* El proyecto AIDA murió. Corregimos la bandera binaria para ser consistentes con la auditoría de América.