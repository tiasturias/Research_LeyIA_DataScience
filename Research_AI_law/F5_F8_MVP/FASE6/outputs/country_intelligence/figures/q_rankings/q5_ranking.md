# Q5 — Ranking de Uso Poblacional de IA por País

## 1. ¿Qué estoy viendo en esta imagen?

Esta imagen es un **diagrama de barras horizontales** (*horizontal bar chart*).

- **Eje Y (vertical)**: cada fila es un **país** (código ISO3 de 3 letras). Los países de la muestra preregistrada, ordenados de **mayor a menor percentil** de arriba hacia abajo. El país más arriba es el que muestra mayor uso poblacional de IA relativo dentro de los 43 países.

- **Eje X (horizontal)**: el **percentil descriptivo de uso poblacional de IA**, un número entre **0.00 y 1.00**. Una barra más larga significa que la población de ese país usa más IA (en términos relativos) comparada con los otros 42 países.

- **Colores**: rojo = Chile (CHL, país focal), verde = Singapur (SGP, benchmark #1), azul = países destacados para comparación (USA, CHN, EST, IRL, ARE, KOR, BRA, URY), gris claro = resto de países.

- **Orden**: los países están ordenados de mayor a menor percentil, determinado por el promedio de los 3 indicadores de uso poblacional de IA.

## 2. ¿Qué pregunta de investigación responde Q5?

La pregunta **Q5** del estudio es:

> *"¿Los países con más rasgos regulatorios de IA muestran mayor uso social o poblacional de IA?"*

En lenguaje simple: ¿en los países con más leyes y normas de IA, la población general (las personas comunes, no solo las empresas o el gobierno) usa más herramientas de inteligencia artificial como Claude, ChatGPT, asistentes de IA, etc.?

**Advertencia específica de Q5**: algunos indicadores de Q5 tienen **poca variación** entre países. Por ejemplo, `anthropic_collaboration_pct` (colaboración humano-IA) tiene valores muy cercanos a cero en muchos países, lo que dificulta detectar patrones claros. La asociación entre regulación y uso poblacional debe interpretarse con cautela adicional.

## 3. ¿Qué mide exactamente el percentil de Q5?

El percentil de Q5 es el **promedio de 3 percentiles individuales**, uno por cada indicador de uso poblacional de IA:

| Indicador (outcome) | ¿Qué mide en el mundo real? | Fuente | Países con dato |
|---|---|---|---|
| `anthropic_usage_pct` | **Uso relativo de Claude/IA por parte de la población**. Mide la proporción de consultas a Claude (el asistente de IA de Anthropic) originadas desde cada país, ajustada por el tamaño de la población. Este indicador también aparece en Q2. Un valor alto (ej. Singapur = 21.97) significa que los habitantes de ese país usan Claude de forma desproporcionadamente intensa para su tamaño poblacional. Un valor bajo (ej. Chile = 0.27) indica un uso mucho menor. NO mide el uso absoluto de todas las IAs, sino específicamente Claude en relación al tamaño del país. | Anthropic Usage Data 2024 | 42 |
| `anthropic_collaboration_pct` | **Colaboración humano-IA**. Mide en qué proporción los usuarios de Claude interactúan con la IA de forma colaborativa (diálogo extenso, co-creación, trabajo conjunto) en lugar de consultas simples de una sola pregunta. Un valor alto indica que los usuarios de ese país tienden a usar la IA como un compañero de trabajo, no solo como un buscador. **Precaución**: este indicador tiene muy poca variación entre países y valores cercanos a cero, por lo que su aporte al percentil de Q5 es limitado. | Anthropic Usage Data 2024 | 42 |
| `oxford_ind_adoption_emerging_tech` | **Adopción de tecnologías emergentes** por parte del sector privado y la sociedad. Mide qué tan rápido el país en su conjunto adopta tecnologías de frontera (IA, robótica, blockchain, biotecnología). Este indicador también aparece en Q2. Refleja tanto la adopción empresarial como la apertura social a nuevas tecnologías. | Oxford Insights — Government AI Readiness Index 2024 | 43 |

### ¿Cómo se calcula el percentil de Q5?

1. Para cada indicador, se ordenan los países con dato de mayor a menor.
2. Se asigna el percentil individual: `percentil = (países con valor ≤ este) / (total con dato)`.
3. Se promedian los 3 percentiles.

### Particularidad de Q5: poca variación en collaboration_pct

El indicador `anthropic_collaboration_pct` tiene valores muy cercanos a cero en casi todos los países y muy poca variación. Esto significa que:
- Aporta poca información para distinguir países (todos están cerca del mismo valor).
- El percentil de Q5 está dominado por los otros 2 indicadores (`anthropic_usage_pct` y `oxford_ind_adoption_emerging_tech`), que sí tienen variación sustancial.
- En los modelos de asociación (Q5_results.csv), este indicador forzó un fallback de fractional logit a OLS simple porque no cumplía los supuestos del modelo fraccional.

## 4. Interpretación de los valores del percentil

| Percentil | Significado | Etiqueta |
|---|---|---|
| 0.85 (USA en Q5) | Está por encima del 85% de los países en uso poblacional de IA | `high_performer` |
| 0.77 (Alemania en Q5) | Está por encima del 77% | `high_performer` |
| 0.66 (Singapur en Q5) | Está por encima del 66% | `middle_performer` |
| 0.42 (Chile en Q5) | Está por encima del 42% de los países. El 58% tiene mayor uso poblacional. | `middle_performer` |
| 0.10 (Uruguay en Q5) | Está por encima de solo el 10% de los países | `bottom_laggard` |

## 5. Top 5 y Bottom 5 de Q5

### Los 5 países con mayor uso poblacional de IA:

| Posición | País | ISO3 | Percentil Q5 | Etiqueta |
|---|---|---|---|---|
| **1** | Estados Unidos | USA | 0.849 | high_performer |
| **2** | Alemania | DEU | 0.771 | high_performer |
| **3** | Reino Unido | GBR | 0.764 | high_performer |
| **4** | Países Bajos | NLD | 0.762 | high_performer |
| **5** | Japón | JPN | 0.755 | high_performer |

### Los 5 países con menor uso poblacional de IA:

| Posición | País | ISO3 | Percentil Q5 | Etiqueta |
|---|---|---|---|---|
| **39** | Grecia | GRC | 0.270 | low_performer |
| **40** | Bulgaria | BGR | 0.126 | bottom_laggard |
| **41** | Croacia | HRV | 0.126 | bottom_laggard |
| **42** | China | CHN | 0.116 | bottom_laggard |
| **43** | Uruguay | URY | 0.102 | bottom_laggard |

### ¿Por qué China está tan abajo en Q5?

Similar a lo observado en Q2, China aparece en el bottom 5 de Q5 (percentil 0.116). La explicación más probable es una **limitación de cobertura de las fuentes**: el indicador `anthropic_usage_pct` mide específicamente el uso de Claude, un producto de Anthropic que **no está disponible en China**. Por lo tanto, el valor de China en este indicador es cercano a cero por razones de acceso al producto, no porque la población china no use IA (de hecho, usan intensivamente herramientas locales como Baidu's Ernie Bot, Alibaba's Tongyi Qianwen, o ByteDance's Doubao). Esta es una limitación reconocida del estudio: las fuentes de datos favorecen a países donde operan las empresas occidentales de IA.

## 6. Chile en Q5: detalle completo

| Dato | Valor |
|---|---|
| Percentil Q5 | **0.418** |
| Ranking global | **aproximadamente 24 de 43** |
| Etiqueta | `middle_performer` |
| ¿Es fortaleza o debilidad? | **Ninguna**. Q5 no aparece ni como fortaleza ni como debilidad principal de Chile. Es su dimensión más cercana a la mediana. |

### Desglose por indicador individual:

| Indicador | Valor observado | Percentil | Rank | Etiqueta |
|---|---|---|---|---|
| Uso de Claude/IA (Anthropic) | 0.272 | 0.31 | 30/42 | low_performer |
| Colaboración humano-IA (Anthropic) | 16.667 | **0.57** | **1/42** | **middle_performer** |
| Adopción tecnologías emergentes (Oxford) | 61.55 | 0.37 | 28/43 | low_performer |

### ¡Atención! Chile es #1 en colaboración humano-IA

El dato más llamativo del perfil chileno en Q5 es que Chile aparece en el **ranking #1** en `anthropic_collaboration_pct` con un valor de 16.667. Sin embargo, hay que interpretar esto con **mucha cautela**:

- **¿Qué significa ser #1 en colaboración?** Significa que, entre los usuarios chilenos de Claude, la proporción de interacciones colaborativas (diálogos extensos, co-creación) es la más alta de los 42 países con dato.
- **Pero el percentil es solo 0.57**: a pesar de ser #1 en ranking, el percentil es apenas 0.57 (middle_performer). Esto revela que el liderazgo es por un margen muy pequeño — la diferencia entre el #1 y el #21 en este indicador es mínima. Como se mencionó antes, este indicador tiene muy poca variación, por lo que "ser #1" no implica una ventaja sustancial.
- **¿Por qué Chile lidera este indicador?** Es difícil saberlo con certeza. Podría reflejar patrones culturales de uso de tecnología, el perfil de los early adopters chilenos de Claude, o simplemente ser un artefacto estadístico de una muestra pequeña de usuarios en Chile.

### Interpretación general del perfil chileno en Q5:

Q5 es, junto con Q1, la dimensión donde Chile está **más cerca de la mediana** (percentil 0.418). No es una fortaleza destacada, pero tampoco es una debilidad pronunciada como Q3.

- **Uso de Claude**: bajo en términos relativos (percentil 0.31), lo que sugiere que la adopción de asistentes de IA por la población general chilena aún es limitada comparada con países como Singapur, Estonia o Estados Unidos.
- **Adopción de tecnologías emergentes**: moderadamente baja (percentil 0.37), similar al patrón observado en Q2.
- **Colaboración humano-IA**: alto en ranking pero con poca significancia práctica por la baja variabilidad del indicador.

## 7. Comparación con Singapur (la brecha más pequeña del estudio)

| Dimensión | Chile | Singapur | Brecha |
|---|---|---|---|
| Q1 (Inversión) | 0.406 | 0.895 | 0.489 |
| Q2 (Adopción) | 0.311 | 0.811 | 0.500 |
| Q3 (Innovación) | 0.211 | 0.835 | 0.624 ← la mayor |
| **Q5 (Uso poblacional)** | **0.418** | **0.660** | **0.242 ← la menor** |
| Q6 (Sector público) | 0.336 | 0.659 | 0.323 |

Q5 es la dimensión donde Chile está **más cerca de Singapur**. La brecha de 0.242 puntos de percentil es sustancialmente menor que en cualquier otra Q. Esto sugiere que, en uso poblacional de IA, la distancia entre Chile y su benchmark principal no es tan pronunciada como en inversión, adopción o innovación.

## 8. La nota metodológica de la imagen

> *"Nota: posicionamiento descriptivo in-sample; no es predicción independiente ni causalidad. Su robustez debe evaluarse en Fase 7 antes de convertirse en recomendación de política pública."*

**Refuerzo para Q5**: además de las cautelas estándar (no causalidad, no predicción, in-sample), en Q5 hay que recordar que:
- Los datos de Anthropic reflejan solo una plataforma de IA (Claude) y no capturan el uso de ChatGPT, Gemini, Copilot u otras herramientas.
- China y posiblemente otros países tienen valores artificialmente bajos en Anthropic por falta de disponibilidad del producto.
- El indicador de colaboración tiene tan poca variación que su contribución al ranking es marginal.

## 9. ¿Qué puedo y qué NO puedo concluir?

### Lo que SÍ puedes concluir:

- "Estados Unidos, Alemania, Reino Unido, Países Bajos y Japón lideran en uso poblacional de IA dentro de esta muestra, según datos de Anthropic y Oxford."
- "Chile tiene un desempeño intermedio en uso poblacional de IA (percentil 0.418), siendo Q5 la dimensión donde está más cerca de Singapur (brecha de solo 0.242)."
- "Chile aparece como #1 en ranking de colaboración humano-IA, aunque la ventaja es pequeña porque el indicador tiene poca variabilidad entre países."
- "China y Uruguay están en el bottom de Q5, aunque en el caso de China esto puede reflejar falta de acceso a Claude más que falta de uso de IA."

### Lo que NO puedes concluir:

- "La población chilena usa más IA que la de Singapur en colaboración." (El dato solo mide Claude; no mide ChatGPT, Copilot, Gemini, ni herramientas locales.)
- "El uso poblacional de IA en Chile mejorará si se aprueba la Ley Marco de IA." (No hay evidencia causal.)
- "China tiene baja adopción poblacional de IA." (Probablemente tiene alta adopción en plataformas chinas no capturadas por este estudio.)
- "Uruguay es el país con menor uso de IA del mundo." (Solo es el último de esta muestra de 43 países.)

## 10. ¿Dónde encuentro más información?

- **Resultados de modelos Q5**: `q5_results.csv` contiene los coeficientes de asociación (fractional logit + sensibilidad binaria) y los fallbacks aplicados.
- **Scores por país en Q5**: `q5_scores_per_country.csv` con 297 filas de valores observados.
- **Country card de Chile**: `country_cards_data/CHL_country_card_data.csv`.
- **Notebook didáctico**: sección 4 del notebook de auditoría humana (Q5).
