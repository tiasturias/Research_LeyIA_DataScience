# Observado vs Esperado — Overperformers y Underperformers del Ecosistema IA

## 1. ¿Qué estoy viendo?

Un **gráfico de dispersión** (*scatter plot*) con una línea diagonal de 45°. Cada punto representa un **país en un outcome específico** (combinación país × indicador). El gráfico compara el valor real observado de cada país con el valor que un modelo estadístico interno "esperaría" dadas sus características.

- **Eje X (horizontal)**: **valor ajustado/esperado** (*fitted value*). Es lo que un modelo OLS simple — usando controles mínimos como PIB per cápita y penetración de internet — predice que debería ser el valor de ese país en ese outcome. En lenguaje simple: "dadas las características básicas de este país, ¿qué valor sería típico o esperable?".
- **Eje Y (vertical)**: **valor observado real**. Es el dato crudo del país en ese outcome, tal como fue recolectado de Oxford Insights, WIPO, OECD, Anthropic o Microsoft.
- **Línea diagonal de 45°**: la línea donde valor observado = valor esperado. Representa el desempeño "típico" o "según lo esperado".
- **Puntos sobre la línea**: países que **rinden más de lo esperado** (*overperformers*). Tienen valores reales superiores a lo que el modelo predice dadas sus características básicas.
- **Puntos bajo la línea**: países que **rinden menos de lo esperado** (*underperformers*). Tienen valores reales inferiores a lo que el modelo predice.
- **Puntos sobre la línea**: países que rinden **según lo esperado**.

## 2. ¿Qué es un overperformer?

Un **overperformer** es un país cuyo valor observado en un outcome es **mayor** que el valor que el modelo esperaría basándose en sus características estructurales (PIB per cápita, penetración de internet, etc.).

**Ejemplo hipotético**: si un país tiene un PIB per cápita mediano y una penetración de internet del 70%, el modelo podría predecir que su inversión en tecnologías emergentes sea de 40 puntos. Pero si el valor real es 70, ese país es un overperformer: **rinde más de lo que sus características básicas harían esperar**. Hay algo en ese país — políticas, cultura, ecosistema — que le permite superar las expectativas del modelo.

## 3. ¿Qué es un underperformer?

Un **underperformer** es un país cuyo valor observado es **menor** que el valor esperado por el modelo. Tiene características estructurales (PIB, internet) que harían esperar un mejor desempeño, pero sus valores reales están por debajo.

**Ejemplo hipotético**: un país con PIB per cápita alto y 95% de penetración de internet "debería" tener alta adopción de IA. Si su valor real es bajo, es un underperformer: **rinde menos de lo esperado**. Hay factores — institucionales, regulatorios, culturales — que frenan su desempeño a pesar de tener condiciones favorables.

## 4. ¿Cómo se construye este gráfico?

1. Para cada outcome de Q1-Q6, se ajusta un **modelo OLS simple** (regresión lineal con errores estándar) usando controles estructurales básicos (PIB per cápita, penetración de internet).
2. El modelo produce un **valor ajustado** (*fitted value*) para cada país en cada outcome: "dadas tus características, este es el valor que estadísticamente te correspondería".
3. Se grafica el valor observado (eje Y) contra el valor ajustado (eje X).
4. La **distancia vertical** entre el punto y la línea de 45° es el **residual**: `residual = valor_observado − valor_ajustado`.
   - Residual positivo = overperformer (rinde más de lo esperado).
   - Residual negativo = underperformer (rinde menos de lo esperado).

**Importante**: este modelo es **interno y descriptivo**. No es un modelo validado externamente. Solo sirve para identificar visualmente qué países se desvían de la tendencia general de la muestra.

## 5. ¿Qué significan los residuales?

El archivo `country_residuals_and_gaps.csv` contiene 854 filas de residuales (país × outcome). Algunas interpretaciones:

| Tipo | Residual | Significado |
|---|---|---|
| **Overperformer** | Positivo y grande | El país supera ampliamente lo esperado. Puede indicar políticas efectivas, ecosistema dinámico, o factores no capturados por el modelo. |
| **Underperformer** | Negativo y grande | El país está muy por debajo de lo esperado. Puede indicar barreras institucionales, baja capacidad de ejecución, o factores adversos no medidos. |
| **As expected** | Cercano a cero | El país rinde aproximadamente según lo esperado por sus características estructurales. |

**Cautela**: "overperformer" no significa "país exitoso en términos absolutos". Significa "país que rinde mejor de lo que el modelo predice dadas sus características". Un país puede ser overperformer y aún así tener valores absolutos bajos (si sus características estructurales son muy limitadas). Similarmente, un país puede ser underperformer y tener valores absolutos altos (si sus características harían esperar aún más).

## 6. ¿Qué información adicional aporta este gráfico?

A diferencia de los rankings (que solo muestran posición relativa), este gráfico revela **si el desempeño de un país es sorprendente o esperable dadas sus circunstancias**. Dos países pueden tener el mismo percentil pero uno ser overperformer (está rindiendo más de lo que le correspondería) y otro underperformer (está rindiendo menos).

Esto es útil para política pública: un overperformer puede ser un **caso de estudio** ("¿qué está haciendo bien este país para superar sus limitaciones estructurales?"). Un underperformer puede ser un **caso de alerta** ("¿qué está frenando a este país a pesar de tener condiciones favorables?").

## 7. El caso de Chile

Chile aparece tanto como overperformer como underperformer, dependiendo del outcome:

- **Overperformer en**: `oxford_e_government_delivery` (entrega de e-government). Chile tiene 96.53 puntos, muy por encima de lo que el modelo esperaría dadas sus características. Esto confirma que la infraestructura digital del Estado chileno es una **fortaleza genuina** que supera las expectativas estructurales.
- **Underperformer en**: varios outcomes de inversión e innovación. A pesar de ser un país de ingreso alto con buena penetración de internet, sus valores en VC, deals y output de innovación están por debajo de lo esperado.

## 8. Nota metodológica

> *"Nota: posicionamiento descriptivo in-sample; no es predicción independiente ni causalidad."*

- **Modelo interno simple**: usa solo controles básicos (PIB, internet). No incluye todos los factores relevantes. Los residuales dependen de qué variables se incluyan en el modelo.
- **No es validación externa**: el modelo no fue probado con datos independientes.
- **No es causalidad**: ser overperformer no significa que las políticas del país CAUSARON el buen desempeño.
- **Fase 7**: la estabilidad de over/underperformers debe validarse.

## 9. ¿Qué puedo concluir?

**SÍ**: "Algunos países rinden sistemáticamente por encima de lo esperado por sus características estructurales (overperformers), y otros por debajo (underperformers). Chile es overperformer en e-government delivery pero underperformer en inversión e innovación."

**NO**: "El overperformance de Chile en e-government se debe a X política específica." (No se estableció causalidad.) "Ser underperformer significa que el país tiene malas políticas." (Puede reflejar factores no medidos por el modelo.)
