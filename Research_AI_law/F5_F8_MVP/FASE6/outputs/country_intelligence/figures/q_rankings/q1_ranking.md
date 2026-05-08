# Q1 — Ranking de Inversión en IA por País

## 1. ¿Qué estoy viendo en esta imagen?

Esta imagen es un **diagrama de barras horizontales** (en inglés, *horizontal bar chart*).

- **Eje Y (vertical, de arriba hacia abajo)**: cada fila representa un **país**, identificado con su código ISO3 de 3 letras (ej. `USA` = Estados Unidos, `CHL` = Chile, `SGP` = Singapur). El gráfico incluye hasta **43 países** de la muestra preregistrada del estudio, aunque no todos los países tienen datos en todos los indicadores. El país que aparece hasta arriba es el de mayor percentil; el de hasta abajo es el de menor percentil.

- **Eje X (horizontal, de izquierda a derecha)**: muestra el **percentil descriptivo**, un número que va de **0 a 1**. No es una calificación, no es una nota absoluta, no es un puntaje de 1 a 100. Es una **medida de posición relativa**: indica dónde está ese país comparado con los otros países de la muestra de 43. Una barra más larga (más cerca del 1) significa que el país está mejor posicionado; una barra más corta (más cerca del 0) significa que está peor posicionado.

- **Colores de las barras**: no son aleatorios. Cada color identifica un tipo de país dentro del estudio:
  - **Rojo**: Chile (`CHL`), el **país focal** del estudio. Este estudio fue motivado por el Boletín 16821-19 que propone una Ley Marco de IA para Chile, por lo que Chile es el centro de todas las comparaciones.
  - **Verde**: Singapur (`SGP`), el **benchmark prioritario #1**. Singapur fue identificado como la referencia aspiracional más relevante para Chile por su tamaño, nivel de ingreso y desempeño en múltiples dimensiones del ecosistema IA.
  - **Azul**: otros países destacados para el análisis comparativo: Estados Unidos (`USA`), China (`CHN`), Estonia (`EST`), Irlanda (`IRL`), Emiratos Árabes Unidos (`ARE`), Corea del Sur (`KOR`), Brasil (`BRA`) y Uruguay (`URY`).
  - **Gris claro**: el resto de los 43 países de la muestra.

- **Orden**: los países están ordenados de **mayor a menor percentil**. El país con la barra más larga (más arriba) es el que tiene la mayor inversión relativa en IA dentro de la muestra. El de la barra más corta (más abajo) es el de menor inversión relativa. Este orden NO fue decidido por ningún investigador — es el resultado de aplicar la fórmula de percentil (ver sección 3) a los datos observados reales.

## 2. ¿Qué pregunta de investigación responde Q1?

Cada "Q" es una **pregunta de investigación** (*research question*) del estudio. La pregunta **Q1** es:

> *"¿Los países con más rasgos regulatorios de IA muestran mejores indicadores de inversión, capital de riesgo o unicornios de IA?"*

En lenguaje simple: ¿los países que tienen más leyes, decretos, normas y regulaciones sobre inteligencia artificial también tienden a tener más inversión privada en tecnología, más startups unicornio de IA y más capital de riesgo disponible para emprendedores?

**Importante**: Q1 NO busca probar que la regulación **cause** (provoque) la inversión. Busca detectar si ambas cosas — regulación e inversión — **ocurren juntas** en los mismos países. En estadística esto se llama una **asociación**, no una relación causal. La diferencia es fundamental: observar que los países con muchas leyes de IA también tienen mucha inversión no significa que las leyes hayan producido esa inversión. Podría ser al revés (países ricos que invierten mucho también legislan más), o podría haber un tercer factor (como el nivel educativo o la infraestructura digital) que explique ambas cosas.

## 3. ¿Qué mide exactamente el percentil de Q1?

El percentil de Q1 que aparece en el gráfico NO viene de una sola fuente de datos. Es el **promedio de 4 percentiles individuales**, uno por cada indicador de inversión. Estos 4 indicadores se llaman **outcomes** (resultados observados) y provienen de dos fuentes internacionales:

| Indicador (outcome) | ¿Qué mide en el mundo real? | Fuente | Países con dato |
|---|---|---|---|
| `oxford_ind_company_investment_emerging_tech` | **Inversión empresarial en tecnologías emergentes**. Mide el nivel de inversión que las empresas privadas de un país destinan a tecnologías de frontera como inteligencia artificial, robótica, biotecnología, blockchain, etc. Un valor alto (ej. USA = 100.0) significa que el sector privado de ese país está apostando fuerte por el futuro tecnológico. Un valor bajo indica poca inversión empresarial en innovación disruptiva. | Oxford Insights — Government AI Readiness Index 2024 | 43 |
| `oxford_ind_ai_unicorns_log` | **Cantidad de unicornios de IA**, en escala logarítmica. Un "unicornio" es una startup tecnológica valorada en más de USD 1,000 millones. Este indicador cuenta específicamente los unicornios cuyo negocio principal es la inteligencia artificial. La escala logarítmica se usa porque la distribución es muy asimétrica (USA tiene decenas, muchos países tienen 0 o 1). Un valor alto indica un ecosistema maduro de startups de IA que lograron escalar a valoraciones enormes. | Oxford Insights — Government AI Readiness Index 2024 | 43 |
| `oxford_ind_vc_availability` | **Disponibilidad de capital de riesgo** (*venture capital*). Mide qué tan accesible es el financiamiento de inversionistas de riesgo para startups tecnológicas en ese país. Responde a la pregunta: "si un emprendedor tiene una idea de IA, ¿qué tan fácil es que encuentre un fondo de VC que lo financie?". Un valor alto (ej. USA = 100.0) indica un ecosistema de VC profundo y líquido. | Oxford Insights — Government AI Readiness Index 2024 | 43 |
| `wipo_c_vencapdeal_score` | **Puntaje de acuerdos de venture capital** según la Organización Mundial de Propiedad Intelectual (WIPO). Refleja el volumen total y el valor monetario de las transacciones (deals) de venture capital que ocurren en el país, combinando cantidad de acuerdos y montos invertidos. Complementa al indicador anterior midiendo no solo la disponibilidad teórica de VC, sino la actividad real de deals. | WIPO — Global Innovation Index 2024 | 40 |

### ¿Cómo se calcula el percentil de Q1 paso a paso?

1. Para cada uno de los 4 indicadores, se toman **todos los países que tienen dato** en ese indicador (entre 40 y 43 países, según cuántos reportaron ese dato).
2. Se ordenan los países **de mayor a menor valor**. El país con el valor más alto queda en la posición 1, el siguiente en la 2, y así sucesivamente.
3. Se asigna un percentil a cada país con esta fórmula:  
   `percentil = (número de países con valor menor o igual al de este país) / (total de países con dato en ese indicador)`
4. Se calcula el **promedio aritmético** de los 4 percentiles individuales. Ese promedio es el percentil de Q1 que ves en el gráfico.

### Ejemplo concreto con Estados Unidos (USA):

| Indicador | Valor observado | Percentil individual |
|---|---|---|
| Inversión empresarial en tecnologías emergentes | 100.0 | ≈ 0.98 (solo 1 país lo supera) |
| Unicornios de IA (log) | muy alto | ≈ 0.98 |
| Disponibilidad de VC | 100.0 | ≈ 0.98 |
| Score de deals VC (WIPO) | muy alto | ≈ 0.93 |
| **Promedio (percentil Q1)** | | **0.967** |

Esto significa que USA está **por encima del 96.7% de los países** de la muestra en los 4 indicadores combinados de inversión en IA. Dicho de otra forma: de cada 100 países en esta muestra, solo 3 tienen mejor inversión que USA.

### Ejemplo concreto con Chile (CHL):

| Indicador | Valor observado | Percentil individual | Etiqueta |
|---|---|---|---|
| Inversión empresarial en tecnologías emergentes | 38.5 | 0.21 | low_performer |
| Unicornios de IA (log) | 16.999 | **0.79** | **high_performer** ★ |
| Disponibilidad de VC | 9.0 | 0.37 | low_performer |
| Score de deals VC (WIPO) | 3.95 | 0.25 | low_performer |
| **Promedio (percentil Q1)** | | **0.406** | middle_performer |

Chile tiene una fortaleza relativa en unicornios de IA (percentil 0.79, es decir mejor que el 79% de los países), pero esta se ve contrarrestada por un desempeño más bajo en los otros tres indicadores (inversión empresarial directa, disponibilidad de capital de riesgo y volumen de deals de VC), lo que produce un percentil promedio de 0.406 — zona media-baja del ranking.

## 4. ¿Qué significa que el percentil sea "descriptivo"?

La palabra **descriptivo** aparece repetidamente en este estudio y es crucial entenderla. Significa **tres cosas**:

1. **In-sample (dentro de la muestra)**: el percentil solo es válido DENTRO de estos 43 países concretos, con estos datos específicos recolectados en 2024-2025. Si mañana agregáramos 10 nuevos países con más inversión que USA, el percentil de USA bajaría automáticamente (porque ahora habría más países por encima). El percentil NO se puede extrapolar a países que no están en la muestra.

2. **No es predicción**: el percentil describe lo que YA SE OBSERVÓ en el pasado reciente (datos 2024). No está prediciendo qué país tendrá más inversión en 2026, 2027 o 2030. No es un pronóstico. Si un país cambia sus políticas, el percentil no se actualiza solo — habría que recolectar nuevos datos.

3. **No es causalidad**: el percentil de inversión NO dice NADA sobre por qué ese país llegó a esa posición. No afirma que la regulación de IA causó la inversión. No afirma que copiar las políticas de USA producirá el mismo nivel de inversión. Solo describe dónde está cada país en comparación con los demás.

## 5. ¿Qué significa un percentil de 0.56? ¿Y uno de 0.21?

Los percentiles se interpretan así en esta investigación:

- **Percentil 0.97 (USA en Q1)**: este país está por encima del 97% de los países. Solo el 3% tiene mejor desempeño. Es un caso excepcional dentro de la muestra.
- **Percentil 0.56 (Brasil en Q1)**: este país está por encima del 56% de los países. El 44% tiene mejor desempeño. Es una posición intermedia, ni destacada ni preocupante.
- **Percentil 0.41 (Chile en Q1)**: este país está por encima del 41% de los países. El 59% tiene mejor desempeño. Es una posición media-baja.
- **Percentil 0.21 (Chile en inversión empresarial)**: este país está por encima de solo el 21% de los países. El 79% tiene mejor desempeño. Es una posición baja.
- **Percentil 0.13 (Perú en Q1)**: este país está por encima de solo el 13% de los países. El 87% tiene mejor desempeño. Es una posición muy baja.

Las etiquetas que verás junto a los percentiles siguen esta escala fija:

| Rango de percentil | Etiqueta | Significado en lenguaje común |
|---|---|---|
| ≥ 0.90 | `top_pioneer` | Está en el 10% superior de la muestra. Caso excepcional. |
| 0.75 – 0.90 | `high_performer` | Está en el cuarto superior (percentil 75 o más). Desempeño alto relativo. |
| 0.40 – 0.75 | `middle_performer` | Está en la zona media (entre percentil 40 y 75). Ni destaca ni preocupa. |
| 0.20 – 0.40 | `low_performer` | Está en el cuarto inferior de la mitad superior (percentil 20-40). Desempeño bajo relativo. |
| < 0.20 | `bottom_laggard` | Está en el 20% inferior de la muestra. Rezagado relativo. |
| Sin dato | `not_ranked_missing` | No se pudo calcular porque el país no tiene datos en suficientes indicadores. |

**Importante**: 0.50 NO es una nota de aprobación. No existe un "aprobado" o "reprobado" en este estudio. 0.50 significa simplemente "este país está exactamente en la mediana de la muestra: la mitad de los países están mejor y la mitad están peor".

## 6. Top 5 y Bottom 5 de Q1

Extraídos directamente de los datos del estudio (`country_q_profile_wide.csv`), ordenados de mayor a menor percentil:

### Los 5 países con mayor inversión relativa en IA:

| Posición | País | ISO3 | Percentil Q1 | Etiqueta |
|---|---|---|---|---|
| **1** | Estados Unidos | USA | 0.967 | top_pioneer |
| **2** | Israel | ISR | 0.959 | top_pioneer |
| **3** | Singapur | SGP | 0.895 | high_performer |
| **4** | Reino Unido | GBR | 0.887 | high_performer |
| **5** | Canadá | CAN | 0.854 | high_performer |

### Los 5 países con menor inversión relativa en IA:

| Posición | País | ISO3 | Percentil Q1 | Etiqueta |
|---|---|---|---|---|
| **39** | México | MEX | 0.238 | low_performer |
| **40** | Rumania | ROU | 0.195 | bottom_laggard |
| **41** | Argentina | ARG | 0.176 | bottom_laggard |
| **42** | Grecia | GRC | 0.153 | bottom_laggard |
| **43** | Perú | PER | 0.125 | bottom_laggard |

## 7. ¿Por qué estos países están en esas posiciones?

**Estados Unidos está en el puesto #1 porque** tiene los valores crudos observados más altos **en los 4 indicadores simultáneamente**:
- Es el país con mayor inversión empresarial privada en tecnologías emergentes del mundo (Silicon Valley concentra una porción enorme del venture capital global).
- Tiene la mayor cantidad de startups unicornio de IA (OpenAI, Anthropic, Scale AI, etc.).
- Posee el ecosistema de venture capital más profundo y líquido del planeta.
- Lidera el ranking WIPO de deals de VC por volumen y valor.

No es que el modelo estadístico "haya decidido" poner a USA arriba — es que los datos reales observados de USA son los más altos en todas las dimensiones de inversión. El ranking simplemente refleja esa realidad observada.

**Israel está en el puesto #2 porque** tiene un ecosistema de startups tecnológicas excepcionalmente denso para su tamaño (a menudo llamado "Startup Nation"). Aunque su población es menor a 10 millones, tiene una concentración de VC per cápita y de unicornios tecnológicos que supera a casi todos los demás países.

**Singapur está en el puesto #3 porque** combina un sector financiero muy desarrollado, políticas agresivas de atracción de inversión tecnológica, y un ecosistema de VC que sirve como puerta de entrada al sudeste asiático. Su percentil de 0.895 lo deja al borde de `top_pioneer`.

**Perú está en el último puesto (#43) porque** sus valores observados en los 4 indicadores son consistentemente los más bajos de la muestra. Esto refleja un ecosistema de inversión tecnológica menos desarrollado en términos relativos: menor inversión empresarial en tecnologías emergentes, menos unicornios, menor disponibilidad de VC y menos deals de venture capital.

### ¿Qué variables provocan este orden de ranking?

El orden NO es producido por una sola variable. Es el resultado de **combinar 4 indicadores distintos**, promediando sus percentiles. Si un país es muy fuerte en 3 indicadores pero débil en 1, su promedio baja. Si es fuerte en los 4, está en la cima. Si es débil en los 4, está en el fondo.

Por eso USA (fuerte en TODO) lidera, mientras que países con desempeño mixto — como Chile (fuerte en unicornios pero débil en VC y deals) — quedan en zona media. No hay una sola causa; es un **perfil multidimensional** de inversión en IA.

## 8. Chile en Q1: detalle completo

| Dato | Valor |
|---|---|
| Percentil Q1 | **0.406** |
| Ranking global | **25 de 43** |
| Etiqueta | `middle_performer` |
| Región | Latin America & Caribbean |
| Grupo de ingreso | High income |
| Cluster regulatorio Q4 | Cluster 1: proyecto de ley IA en curso (pragmático) |

### Desglose por indicador individual:

| Indicador | Valor observado | Percentil | Rank | Etiqueta |
|---|---|---|---|---|
| Inversión empresarial en tecnologías emergentes | 38.5 / 100 | 0.21 | 35/43 | low_performer |
| Unicornios de IA (log) | 16.999 | **0.79** | **8/43** | **high_performer** ★ |
| Disponibilidad de VC | 9.0 / 100 | 0.37 | 27/43 | low_performer |
| Score de deals VC (WIPO) | 3.95 | 0.25 | 31/40 | low_performer |

### Interpretación del perfil chileno:

Chile presenta un perfil de inversión **mixto y polarizado**:
- **Fortaleza**: en unicornios de IA, Chile tiene un desempeño notable (percentil 0.79, rank 8 de 43), superando al 79% de los países de la muestra. Esto sugiere que el ecosistema de startups chileno ha logrado producir empresas de IA con valoraciones significativas (como NotCo, Betterfly, o similares con componentes de IA).
- **Debilidad**: en los otros 3 indicadores — inversión empresarial directa en tecnologías emergentes, disponibilidad de venture capital y volumen de deals de VC — Chile está consistentemente por debajo de la mediana (percentiles 0.21, 0.37, 0.25). Esto indica que el ecosistema de inversión tecnológica chileno, aunque tiene casos de éxito puntuales, aún no alcanza la profundidad y liquidez de los ecosistemas más desarrollados.

La combinación produce un percentil promedio de 0.406, que lo ubica en la **posición 25 de 43 países** — zona media-baja del ranking global de inversión en IA.

## 9. ¿De dónde provienen estos datos?

Los valores observados fueron extraídos de las siguientes fuentes durante la Fase 3 del proyecto (construcción de la *feature matrix*):

- **Oxford Insights — Government AI Readiness Index 2024**: provee 3 de los 4 indicadores de Q1 (inversión empresarial, unicornios IA, disponibilidad de VC). Esta fuente evalúa la preparación de los gobiernos para la IA a través de 39 indicadores agrupados en 3 pilares (gobierno, sector tecnológico, datos e infraestructura).
- **WIPO — Global Innovation Index 2024**: provee el indicador de deals de venture capital. El GII es publicado anualmente por la Organización Mundial de Propiedad Intelectual y rankea a más de 130 economías en capacidades y resultados de innovación.
- **IAPP — AI Legislation Tracker 2024**: no alimenta directamente el percentil de Q1, pero provee los datos de `iapp_ley_ia_vigente` e `iapp_proyecto_ley_ia` usados en los modelos de asociación (Q1_results.csv). Solo 18 países tienen datos IAPP completos.

La muestra preregistrada contiene **43 países**. No todos los países tienen datos en todos los indicadores. En el caso del indicador WIPO de deals de VC, solo 40 países tienen dato (faltan 3).

## 10. La nota metodológica de la imagen

El gráfico incluye una nota al pie que dice:

> *"Nota: posicionamiento descriptivo in-sample; no es predicción independiente ni causalidad. Su robustez debe evaluarse en Fase 7 antes de convertirse en recomendación de política pública."*

Esta nota es **obligatoria** en todos los gráficos del estudio. Desglosémosla:

- **"Posicionamiento descriptivo"**: el gráfico solo describe dónde está cada país en comparación con los demás. No explica por qué está ahí.
- **"In-sample"**: los percentiles solo aplican a esta muestra de 43 países. No pueden extrapolarse a otros países.
- **"No es predicción independiente"**: no estamos prediciendo el futuro. No decimos "USA tendrá el percentil X en 2027".
- **"No es causalidad"**: no afirmamos que la regulación cause la inversión (ni viceversa).
- **"Fase 7"**: este estudio tiene 8 fases. La Fase 7 (análisis de robustez) debe verificar si estos rankings se mantienen estables al aplicar pruebas de sensibilidad (por ejemplo, ¿el top 5 sigue siendo el mismo si quitamos a USA de la muestra?). Solo los hallazgos que pasen Fase 7 como "robustos" deben usarse para recomendaciones de política pública en Fase 8.

## 11. ¿Qué puedo y qué NO puedo concluir de este gráfico?

### Lo que SÍ puedes concluir:

- "Estados Unidos, Israel y Singapur son los 3 países con mayor inversión relativa en IA dentro de esta muestra de 43 países, según datos de Oxford Insights y WIPO de 2024."
- "Chile ocupa la posición 25 de 43 en inversión en IA, con un desempeño mixto: fuerte en unicornios (percentil 0.79) pero débil en disponibilidad de VC (0.37) y deals de VC (0.25)."
- "Los 5 países con menor inversión relativa en IA en esta muestra son México, Rumania, Argentina, Grecia y Perú."
- "El percentil de Q1 es el promedio de 4 indicadores distintos de inversión, no una medición única."

### Lo que NO puedes concluir:

- "La regulación de IA de USA causó su alto nivel de inversión." (El estudio no prueba causalidad.)
- "Si Chile copia las leyes de IA de Singapur, alcanzará su nivel de inversión." (No hay evidencia causal que respalde esta afirmación.)
- "El percentil de Países Bajos (que no está en la muestra) sería X." (El percentil solo aplica a los 43 países observados.)
- "El percentil de Chile en Q1 mejorará en los próximos años." (No es un pronóstico.)
- "Argentina está peor que Chile en inversión porque tiene peores leyes de IA." (No se estableció causalidad.)

## 12. ¿Dónde encuentro más información?

- **Rankings por grupo**: el archivo `country_rankings_by_group.csv` contiene el mismo ranking desglosado por región (LATAM, Europa, etc.), por nivel de ingreso y por grupos personalizados como `chile_latam_peers`.
- **Perfil completo de Chile**: el archivo `country_cards_data/CHL_country_card_data.csv` consolida los datos de Chile en las 5 Qs.
- **Modelos de asociación**: el archivo `q1_results.csv` contiene los coeficientes de regresión que muestran si la regulación se asocia positiva o negativamente con la inversión.
- **Notebook didáctico**: `FASE6/notebooks/06_modeling_AUDITORIA_HUMANA_FASE6_V2_2_VISUAL_DIDACTICO.ipynb` explica todos los gráficos y conceptos con ejemplos.
