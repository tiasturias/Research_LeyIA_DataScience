# Heatmap País × Q — Mapa de Calor del Ecosistema IA por País

## 1. ¿Qué estoy viendo en esta imagen?

Esta imagen es un **mapa de calor** (*heatmap*), un tipo de gráfico que usa colores para representar valores numéricos en una matriz bidimensional.

### Estructura de la matriz:

- **Filas (eje Y, vertical)**: cada fila es un **país** (código ISO3). Hay **42 países** perfilados en esta versión de Fase 6.2 (de los 43 de la muestra, Taiwán —TWN— está ausente por datos faltantes en varias dimensiones Q). Los países están ordenados de **arriba hacia abajo** según su **score general** (*overall_country_profile_score*) — los de mayor puntaje promedio arriba, los de menor abajo.

- **Columnas (eje X, horizontal)**: cada columna es una **pregunta de investigación (Q)**. Las 5 columnas son: **Q1** (Inversión), **Q2** (Adopción), **Q3** (Innovación), **Q5** (Uso poblacional), **Q6** (Sector público). Q4 no aparece porque Q4 es un perfil regulatorio (clustering), no un percentil continuo.

- **Cada celda**: el color de cada celda representa el **percentil descriptivo** de ese país en esa Q. La escala de colores es **RdYlGn** (Red-Yellow-Green):
  - **Rojo** intenso = percentil muy bajo (cercano a 0.00) → el país está muy por debajo de la mediana en esa dimensión.
  - **Amarillo** = percentil intermedio (cercano a 0.50) → el país está en la mediana de la muestra.
  - **Verde** intenso = percentil muy alto (cercano a 1.00) → el país está muy por encima de la mediana.

- **¿Por qué este orden?** Los países están ordenados de arriba hacia abajo por su **score general descriptivo** (promedio de percentiles en Q1, Q2, Q3, Q5, Q6). Los países con más verde en sus filas (alto desempeño en múltiples Qs) aparecen arriba. Los países con más rojo (bajo desempeño) aparecen abajo.

### ¿Qué patrón se ve a simple vista?

Al mirar el heatmap de arriba hacia abajo, se observa una **transición de verde a rojo**: los países en la parte superior tienen predominantemente celdas verdes (alto desempeño en múltiples dimensiones), mientras que los de la parte inferior tienen predominantemente celdas rojas (bajo desempeño). Esto revela que los países tienden a ser consistentes: quien es fuerte en inversión (Q1) suele serlo también en innovación (Q3) y sector público (Q6), y viceversa.

Sin embargo, hay **excepciones notables** — celdas que rompen el patrón de su fila. Por ejemplo:
- **China (CHN)** tiene una celda muy verde en Q3 (innovación, percentil 0.871) pero celdas muy rojas en Q2 (adopción, 0.086) y Q6 (sector público, 0.114). Es un país con desempeño **extremadamente polarizado**.
- **Corea del Sur (KOR)** tiene una celda verde en Q3 (0.894) pero una celda roja en Q1 (inversión, 0.357). Fuerte en innovación, débil en inversión relativa.
- **Chile (CHL)** tiene celdas predominantemente amarillo-anaranjadas (zona media-baja), sin verdes intensos pero tampoco rojos extremos, reflejando un perfil consistentemente intermedio-bajo.

## 2. ¿Qué preguntas de investigación representan las columnas?

| Columna | Nombre completo | Pregunta que responde |
|---|---|---|
| **Q1** | Inversión | ¿Los países con más regulación de IA muestran mejores indicadores de inversión, capital de riesgo o unicornios de IA? |
| **Q2** | Adopción empresarial | ¿Los países con más regulación de IA muestran mayor adopción de IA en empresas y uso tecnológico? |
| **Q3** | Innovación | ¿Los países con más regulación de IA muestran mejores indicadores de innovación o preparación tecnológica? |
| **Q5** | Uso poblacional | ¿Los países con más regulación de IA muestran mayor uso social o poblacional de IA? |
| **Q6** | Sector público | ¿Los países con más regulación de IA muestran mayor capacidad pública, gobernanza digital o adopción estatal? |

**Q4 no aparece en el heatmap** porque Q4 es una tipología regulatoria cualitativa (clusters), no un percentil continuo. Q4 se analiza por separado en el gráfico `q4_regulatory_profile_map.png`.

## 3. ¿Qué es el percentil que da color a cada celda?

Cada celda coloreada representa el **percentil descriptivo promedio** de ese país en todos los indicadores (outcomes) de esa Q:

| Q | Indicadores promediados | Fuentes |
|---|---|---|
| Q1 | 4 indicadores de inversión (inversión empresarial, unicornios IA, disponibilidad VC, deals VC) | Oxford Insights, WIPO |
| Q2 | 5 indicadores de adopción (difusión MS, empresas OECD, uso Anthropic, adopción pública, adopción tech emergente) | Microsoft, OECD, Anthropic, Oxford |
| Q3 | 2 indicadores de innovación (preparación país Oxford, output innovación WIPO) | Oxford Insights, WIPO |
| Q5 | 3 indicadores de uso poblacional (uso Anthropic, colaboración Anthropic, adopción tech emergente) | Anthropic, Oxford |
| Q6 | 6 indicadores de sector público (adopción pública, e-gov delivery, política digital, gobernanza datos, gobernanza ética, INDIGO OECD) | Oxford Insights, OECD |

El percentil va de 0 a 1. **NO es una calificación, NO es un puntaje absoluto, NO es un pronóstico**. Es una medida de posición relativa: dónde está ese país comparado con los otros 41-42 países en esa dimensión específica.

**Significado de la escala de colores con ejemplos concretos:**

| Color aproximado | Rango de percentil | Ejemplo |
|---|---|---|
| Verde intenso | ≥ 0.90 | USA en Q3 (0.976), USA en Q1 (0.967), Israel en Q1 (0.959) |
| Verde claro | 0.75 – 0.90 | Singapur en Q1 (0.895), Singapur en Q2 (0.811), Alemania en Q5 (0.771) |
| Amarillo | 0.40 – 0.75 | Chile en Q1 (0.406), Brasil en Q2 (0.534), España en Q5 (0.599) |
| Naranja | 0.20 – 0.40 | Chile en Q6 (0.336), Chile en Q2 (0.311), Argentina en Q1 (0.176 es rojo ya) |
| Rojo intenso | < 0.20 | China en Q5 (0.116), China en Q6 (0.114), Costa Rica en Q3 (0.047) |

## 4. ¿Cómo se calcula el score general que ordena las filas?

El `overall_country_profile_score` que determina el orden de los países en el heatmap es el **promedio simple** de los percentiles del país en Q1, Q2, Q3, Q5 y Q6:

```
score_general = (percentil_Q1 + percentil_Q2 + percentil_Q3 + percentil_Q5 + percentil_Q6) / 5
```

Este score NO es un índice compuesto validado externamente. Es un **promedio descriptivo interno** que sirve únicamente para ordenar los países en visualizaciones como este heatmap. No debe interpretarse como un ranking de "calidad del ecosistema IA" ni como una medida de "éxito" o "fracaso".

## 5. Distribución de países por categoría general

De los 42 países perfilados, la distribución de etiquetas según su score general es:

| Etiqueta | Cantidad | Significado |
|---|---|---|
| `high_performer` | 6 países | Percentil promedio ≥ 0.75 en el conjunto de las 5 Qs |
| `middle_performer` | 21 países | Percentil promedio entre 0.40 y 0.75 |
| `low_performer` | 15 países | Percentil promedio entre 0.20 y 0.40 |

**No hay ningún país clasificado como `top_pioneer` (≥0.90) ni como `bottom_laggard` (<0.20) en el score general**, aunque sí los hay en Qs individuales. Esto significa que ningún país es excepcionalmente fuerte o excepcionalmente débil en TODAS las dimensiones simultáneamente — todos tienen fortalezas y debilidades.

## 6. Top 5 países por score general

| Posición | País | ISO3 | Score general | Etiqueta |
|---|---|---|---|---|
| **1** | Estados Unidos | USA | 0.854 | high_performer |
| **2** | Países Bajos | NLD | 0.789 | high_performer |
| **3** | Francia | FRA | 0.787 | high_performer |
| **4** | Singapur | SGP | 0.772 | high_performer |
| **5** | Reino Unido | GBR | 0.762 | high_performer |

## 7. Pioneros y rezagados consistentes

El estudio define dos categorías especiales basadas en la **consistencia** del desempeño a través de las Qs:

### Pioneros consistentes (6 países)
Países con percentil ≥ 0.75 en **al menos 3 de las 5 Qs**:

| País | ISO3 | ¿En qué Qs destacan? |
|---|---|---|
| Alemania | DEU | Q2, Q3, Q5 |
| Francia | FRA | Q2, Q3, Q6 |
| Reino Unido | GBR | Q1, Q3, Q5 |
| Países Bajos | NLD | Q2, Q3, Q5, Q6 |
| Singapur | SGP | Q1, Q2, Q3 |
| Estados Unidos | USA | Q1, Q3, Q5, Q6 |

Estos 6 países aparecen consistentemente verdes en el heatmap. Son los **casos de referencia** más sólidos para aprender sobre ecosistemas IA de alto desempeño.

### Rezagados consistentes (3 países)
Países con percentil ≤ 0.25 en **al menos 3 de las 5 Qs**:

| País | ISO3 | ¿En qué Qs están rezagados? |
|---|---|---|
| China | CHN | Q2, Q5, Q6 |
| Costa Rica | CRI | Q2, Q3, Q6 |
| Rumania | ROU | Q1, Q2, Q3, Q6 |

## 8. Chile en el heatmap

| Dato | Valor |
|---|---|
| Percentil Q1 (Inversión) | 0.406 |
| Percentil Q2 (Adopción) | 0.311 |
| Percentil Q3 (Innovación) | 0.211 |
| Percentil Q5 (Uso poblacional) | 0.418 |
| Percentil Q6 (Sector público) | 0.336 |
| **Score general** | **0.336** |
| **Ranking global** | **31 de 42** |
| **Etiqueta** | `low_performer` |

En el heatmap, la fila de Chile (CHL) aparece aproximadamente en el **cuarto inferior** de la matriz (alrededor de la fila 31), con colores predominantemente **amarillo-anaranjados**. No tiene celdas verdes (ningún percentil ≥ 0.75), pero tampoco celdas rojas extremas (ningún percentil < 0.20, salvo el borde con Q3 en 0.211).

El patrón visual de Chile es de un **desempeño consistentemente intermedio-bajo**: no hay una dimensión donde destaque claramente ni una donde colapse totalmente. Es un perfil de "parejidad hacia abajo".

## 9. ¿Para qué sirve este heatmap?

Este gráfico está diseñado para **lectura ejecutiva rápida**:

- **De un vistazo** se puede identificar qué países son consistentemente fuertes (mucho verde) y cuáles son consistentemente débiles (mucho rojo).
- **Comparando columnas** se puede ver en qué Qs hay más variabilidad entre países (columnas con mezcla de verdes y rojos) y en cuáles los países son más parejos (columna más uniforme).
- **Comparando filas** se puede ver si un país es "parejo" (mismo color en todas las columnas) o "polarizado" (verde en unas, rojo en otras).
- **Para Chile**: se ve claramente que está en la mitad inferior de la tabla, sin fortalezas destacadas (ausencia de verde) y con Q3 como su punto más débil (el color más cercano al rojo en su fila).

## 10. La nota metodológica

> *"Nota: posicionamiento descriptivo in-sample; no es predicción independiente ni causalidad. Su robustez debe evaluarse en Fase 7 antes de convertirse en recomendación de política pública."*

- **Descriptivo**: los colores solo muestran dónde está cada país respecto a los demás. No explican por qué.
- **In-sample**: los percentiles aplican solo a estos 42 países con estos datos. No se extrapolan.
- **No es predicción**: no anticipa posiciones futuras.
- **No es causalidad**: no afirma que el color de una celda sea causado por la regulación del país.
- **Fase 7**: los patrones observados (pioneros, rezagados, polarización) deben validarse en la fase de robustez.

## 11. ¿Qué puedo y qué NO puedo concluir?

### Lo que SÍ puedes concluir:

- "Estados Unidos, Países Bajos, Francia, Singapur y Reino Unido tienen los perfiles de ecosistema IA más consistentemente altos de la muestra."
- "Chile (fila ~31, score 0.336) está en el tercio inferior del heatmap, con desempeño intermedio-bajo en las 5 dimensiones."
- "Hay 6 países que destacan consistentemente (pioneros) y 3 que están consistentemente rezagados."
- "China es el país más polarizado: muy fuerte en Q3 (innovación) pero muy débil en Q2, Q5 y Q6."

### Lo que NO puedes concluir:

- "El país X es mejor que el país Y en todo." (El heatmap muestra 5 dimensiones independientes; un país puede ser mejor en unas y peor en otras.)
- "La regulación de IA causa el color verde/rojo de las celdas." (No hay afirmación causal.)
- "Si Chile mejora su percentil en Q3, subirá automáticamente en el ranking general." (El score general es un promedio descriptivo, no un modelo dinámico.)
- "Los 6 pioneros consistentes deben ser imitados en todo." (Fase 7 debe validar primero.)
