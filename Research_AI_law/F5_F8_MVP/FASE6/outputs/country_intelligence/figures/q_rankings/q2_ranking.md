# Q2 — Ranking de Adopción de IA por País

## 1. ¿Qué estoy viendo en esta imagen?

Esta imagen es un **diagrama de barras horizontales** (*horizontal bar chart*).

- **Eje Y (vertical)**: cada fila es un **país** (código ISO3). Los 43 países de la muestra preregistrada, ordenados de mayor a menor percentil de arriba hacia abajo. El país que encabeza la lista (barra más larga arriba) es el de mayor adopción de IA relativa en la muestra.

- **Eje X (horizontal)**: el **percentil descriptivo de adopción de IA**, un número entre **0.00 y 1.00**. Cuanto más larga la barra hacia la derecha, mayor es la adopción relativa de IA en ese país comparado con los otros 42. No es una calificación absoluta: es posición relativa.

- **Colores**: siguen el código cromático de todo el estudio:
  - **Rojo**: Chile (`CHL`) — país focal del Boletín 16821-19.
  - **Verde**: Singapur (`SGP`) — benchmark prioritario #1.
  - **Azul**: países destacados (USA, CHN, EST, IRL, ARE, KOR, BRA, URY).
  - **Gris claro**: resto de países de la muestra.

- **Orden**: los países están ordenados **de mayor a menor percentil**. Quien esté más arriba tiene mayor adopción de IA relativa. Quien esté más abajo tiene menor adopción. Este orden es la consecuencia directa de aplicar la fórmula de percentil (sección 3) a los datos observados.

## 2. ¿Qué pregunta de investigación responde Q2?

La pregunta **Q2** del estudio es:

> *"¿Los países con más rasgos regulatorios de IA muestran mayor adopción de IA en empresas, sector público o uso tecnológico?"*

En lenguaje simple: ¿los países que tienen más leyes y normas sobre inteligencia artificial también son países donde las empresas usan más IA, donde más personas usan herramientas como Claude o ChatGPT, y donde el sector público ha incorporado más la IA en sus servicios?

**Advertencia específica de Q2**: a diferencia de Q1 (donde la asociación regulación-inversión fue consistentemente positiva), en Q2 los resultados son **mixtos**. Dependiendo de qué fuente de datos se mire (Microsoft, OECD, Anthropic, Oxford), la asociación puede ser positiva, negativa o no significativa. Esto es importante porque significa que **más regulación NO siempre coincide con más adopción**. En algunos indicadores, los países más regulados muestran MENOS adopción empresarial de IA.

## 3. ¿Qué mide exactamente el percentil de Q2?

El percentil de Q2 es el **promedio de 5 percentiles individuales**, uno por cada indicador de adopción de IA. Estos 5 indicadores provienen de **4 fuentes internacionales distintas** (Microsoft, OECD, Anthropic y Oxford Insights), lo que hace de Q2 la pregunta con fuentes más diversas:

| Indicador (outcome) | ¿Qué mide en el mundo real? | Fuente | Países con dato |
|---|---|---|---|
| `ms_h2_2025_ai_diffusion_pct` | **Difusión de IA en la población**, medido como porcentaje de personas que usan inteligencia artificial. Proviene del informe "AI Diffusion" de Microsoft (segunda mitad de 2025). Un valor como 64.0% (Singapur) significa que 64 de cada 100 personas en ese país usan IA de forma regular. Un valor como 20.8% (Chile) significa que solo 21 de cada 100 usan IA. | Microsoft AI Diffusion Report H2 2025 | 42 |
| `oecd_5_ict_business_oecd_biz_ai_pct` | **Porcentaje de empresas que usan IA**. Mide qué proporción del tejido empresarial de un país ha incorporado inteligencia artificial en sus operaciones. Proviene de la base de datos ICT de la OECD. Un valor alto (ej. 40%) significa que 4 de cada 10 empresas en ese país usan IA. **Chile NO tiene dato en este indicador** — es uno de los 12 países sin cobertura OECD en esta variable. | OECD ICT Business Database | 31 |
| `anthropic_usage_pct` | **Uso relativo de Claude/IA** según datos anonimizados de Anthropic (la empresa creadora de Claude). Es la proporción de consultas a Claude originadas desde ese país, ajustada por población. Este indicador también aparece en Q5. No mide uso absoluto, sino uso en comparación con el tamaño del país. Un valor como 21.7% (Singapur) indica un uso de Claude desproporcionadamente alto para el tamaño de su población. | Anthropic Usage Data 2024 | 42 |
| `oxford_public_sector_adoption` | **Adopción de IA en el sector público**, medido por Oxford Insights. Evalúa en qué medida las entidades gubernamentales de un país han incorporado IA en sus operaciones y servicios a la ciudadanía. Este indicador también aparece en Q6. Un valor alto (ej. Estonia = 99.6) indica un gobierno que usa activamente IA. | Oxford Insights — Government AI Readiness Index 2024 | 43 |
| `oxford_ind_adoption_emerging_tech` | **Adopción de tecnologías emergentes** por parte del sector privado, según Oxford Insights. Mide qué tan rápido las empresas de un país adoptan tecnologías de frontera como IA, robótica, blockchain, etc. Este indicador también aparece en Q5. | Oxford Insights — Government AI Readiness Index 2024 | 43 |

### ¿Cómo se calcula el percentil de Q2?

1. Para cada uno de los 5 indicadores, se toman todos los países con dato.
2. Se ordenan de mayor a menor valor.
3. Se calcula el percentil: `percentil = (países con valor ≤ este país) / (total países con dato)`.
4. Se promedian los 5 percentiles (o los que el país tenga disponibles; si falta un indicador, no se incluye en el promedio).

**Caso especial**: Chile no tiene dato en `oecd_5_ict_business_oecd_biz_ai_pct`. Por lo tanto, su percentil de Q2 se calcula promediando solo 4 indicadores en lugar de 5. Esto puede afectar su posición relativa (para bien o para mal, dependiendo de cuál habría sido su valor en el indicador faltante).

## 4. ¿Qué significa que los percentiles sean "descriptivos"?

Igual que en todos los gráficos de este estudio, el percentil es **descriptivo**:

1. **In-sample**: solo aplica a estos 43 países con estos datos de 2024-2025.
2. **No es predicción**: no pronostica adopción futura.
3. **No es causalidad**: no afirma que la regulación cause la adopción.
4. **Resultados mixtos**: en Q2, a diferencia de Q1, la asociación regulación-adopción NO es uniformemente positiva. En el indicador OECD de adopción empresarial, la asociación es **negativa** (más regulación coincide con menos adopción). En Anthropic y Oxford, la asociación es positiva. Esto es crucial: **el percentil de Q2 describe adopción, no regulación**.

## 5. Interpretación de los valores del percentil

| Percentil | Significado | Etiqueta |
|---|---|---|
| 0.86 (Países Bajos en Q2) | Está por encima del 86% de los países en adopción de IA | `high_performer` |
| 0.81 (Singapur en Q2) | Está por encima del 81% de los países | `high_performer` |
| 0.31 (Chile en Q2) | Está por encima de solo el 31% de los países. El 69% tienen mayor adopción. | `low_performer` |
| 0.09 (China en Q2) | Está por encima de solo el 9% de los países. El 91% tienen mayor adopción. | `bottom_laggard` |

## 6. Top 5 y Bottom 5 de Q2

### Los 5 países con mayor adopción relativa de IA:

| Posición | País | ISO3 | Percentil Q2 | Etiqueta |
|---|---|---|---|---|
| **1** | Países Bajos | NLD | 0.863 | high_performer |
| **2** | Francia | FRA | 0.824 | high_performer |
| **3** | Singapur | SGP | 0.811 | high_performer |
| **4** | Emiratos Árabes Unidos | ARE | 0.770 | high_performer |
| **5** | Alemania | DEU | 0.750 | high_performer |

### Los 5 países con menor adopción relativa de IA:

| Posición | País | ISO3 | Percentil Q2 | Etiqueta |
|---|---|---|---|---|
| **39** | Grecia | GRC | 0.264 | low_performer |
| **40** | Bulgaria | BGR | 0.221 | low_performer |
| **41** | Costa Rica | CRI | 0.200 | low_performer |
| **42** | Rumania | ROU | 0.196 | bottom_laggard |
| **43** | China | CHN | 0.086 | bottom_laggard |

### ¿Por qué China está última en adopción?

Esto puede sorprender, porque China es percibida como una potencia tecnológica. La explicación está en la **composición de indicadores** y en una limitación de datos:

- China tiene **alto desempeño en innovación y preparación** (Q3, percentil 0.871), pero los indicadores de Q2 miden cosas distintas: difusión poblacional de IA, uso empresarial y adopción en sector público.
- El indicador `oecd_5_ict_business_oecd_biz_ai_pct` probablemente no tiene dato para China (la OECD cubre principalmente países miembros), y varios de los otros indicadores pueden reflejar una **penetración más baja de herramientas como Claude** (Anthropic no opera en China) o de las métricas de Microsoft (que usa datos de herramientas como Copilot, con disponibilidad limitada en China).
- El dato de `ms_h2_2025_ai_diffusion_pct` para China puede ser bajo o faltante en las fuentes usadas.
- Esto ilustra una limitación importante del estudio: los datos disponibles favorecen a países occidentales y alineados con las fuentes (OECD, Microsoft, Anthropic). China puede estar subestimada en Q2 por falta de cobertura de fuentes chinas equivalentes.

## 7. Chile en Q2: detalle completo

| Dato | Valor |
|---|---|
| Percentil Q2 | **0.311** |
| Ranking global | **31 de 43** aproximadamente |
| Etiqueta | `low_performer` |
| Indicadores con dato | 4 de 5 (falta OECD biz AI) |

### Desglose por indicador individual:

| Indicador | Valor observado | Percentil | Rank | Etiqueta |
|---|---|---|---|---|
| Difusión de IA — Microsoft H2 2025 | 20.8% | 0.24 | 33/42 | low_performer |
| Empresas que usan IA — OECD | **sin dato** | — | — | not_ranked_missing |
| Uso de Claude/IA — Anthropic | 0.272 | 0.31 | 30/42 | low_performer |
| Adopción IA sector público — Oxford | 70.76 | 0.33 | 30/43 | low_performer |
| Adopción tecnologías emergentes — Oxford | 61.55 | 0.37 | 28/43 | low_performer |

### Interpretación del perfil chileno en adopción:

Chile muestra un perfil de adopción **consistentemente bajo** en los 4 indicadores donde tiene dato:
- **Difusión poblacional (Microsoft)**: solo 20.8% de los chilenos usa IA, comparado con 64.0% en Singapur o 48.1% en Estonia. Chile está en el cuarto inferior.
- **Uso de Claude (Anthropic)**: proporción de 0.272 — baja en comparación con líderes como Singapur (21.97) o Estonia (15.07). Chile está en el tercio inferior.
- **Adopción en sector público (Oxford)**: 70.76 sobre 100 — es un valor absoluto decente, pero relativo a los demás países queda en el tercio inferior porque muchos países (Estonia 99.63, Francia 97.18, EAU 97.27) tienen valores mucho más altos.
- **Adopción de tecnologías emergentes (Oxford)**: 61.55 — nuevamente en el tercio inferior relativo.

A diferencia de Q1 (donde Chile mostró una fortaleza en unicornios), en Q2 Chile **no tiene ninguna fortaleza destacada** en los indicadores de adopción. Su percentil de 0.311 refleja un desempeño consistentemente por debajo de la mediana en todas las dimensiones de adopción de IA.

**Cautela adicional**: la ausencia del dato OECD de adopción empresarial significa que el percentil de Chile en Q2 se calcula con solo 4 de 5 indicadores. Si Chile tuviera un valor alto en ese indicador faltante, su percentil mejoraría. Si tuviera un valor bajo, empeoraría. No lo sabemos.

## 8. Comparación con Singapur

Singapur (percentil Q2 = 0.811) supera a Chile (0.311) por **0.500 puntos de percentil** en adopción de IA. Esta es una de las brechas más grandes entre Chile y su benchmark principal.

| Indicador de Q2 | Chile | Singapur | Diferencia |
|---|---|---|---|
| Difusión de IA (Microsoft) | 20.8% (pctil 0.24) | 64.0% (pctil alto) | Singapur triplica a Chile |
| Uso de Claude (Anthropic) | 0.272 (pctil 0.31) | 21.97 (pctil alto) | Diferencia de orden de magnitud |
| Adopción sector público | 70.76 (pctil 0.33) | valor alto | Brecha significativa |
| Adopción tecnologías emergentes | 61.55 (pctil 0.37) | valor alto | Brecha moderada-alta |

Singapur consistentemente supera a Chile en todos los indicadores de adopción donde ambos tienen datos, por márgenes considerables.

## 9. La nota metodológica de la imagen

> *"Nota: posicionamiento descriptivo in-sample; no es predicción independiente ni causalidad. Su robustez debe evaluarse en Fase 7 antes de convertirse en recomendación de política pública."*

Traducción de cada frase:
- **Posicionamiento descriptivo**: el gráfico solo muestra dónde está cada país. No explica por qué.
- **In-sample**: los percentiles solo aplican a los 43 países observados.
- **No es predicción independiente**: no es un pronóstico del futuro.
- **No es causalidad**: NO estamos diciendo que la regulación cause (o frene) la adopción.
- **Fase 7**: los rankings deben ser validados en la fase de robustez antes de usarse en recomendaciones.

## 10. ¿Qué puedo y qué NO puedo concluir?

### Lo que SÍ puedes concluir:

- "Países Bajos, Francia y Singapur son los líderes en adopción de IA dentro de esta muestra de 43 países."
- "Chile tiene un desempeño consistentemente bajo en adopción de IA, ubicándose en el tercio inferior en los 4 indicadores donde tiene dato."
- "China aparece en último lugar en adopción de IA (percentil 0.086), probablemente por limitaciones de cobertura de las fuentes de datos usadas (OECD, Anthropic, Microsoft)."
- "La asociación entre regulación y adopción es mixta: positiva en algunos indicadores, negativa en otros."

### Lo que NO puedes concluir:

- "La regulación de IA de Países Bajos causó su alta adopción." (No hay prueba de causalidad.)
- "China tiene baja adopción de IA en la realidad." (Puede tener alta adopción en fuentes chinas no capturadas por este estudio.)
- "Si Chile mejora su regulación, automáticamente subirá en este ranking." (No hay evidencia causal.)
- "El percentil de Chile mejorará en los próximos años." (No es un pronóstico.)

## 11. ¿Dónde encuentro más información?

- **Resultados de modelos Q2**: `q2_results.csv` contiene los coeficientes de asociación (fractional logit) entre predictores regulatorios y cada outcome de adopción.
- **Scores por país en Q2**: `q2_scores_per_country.csv` contiene los valores observados de cada país en cada outcome de adopción.
- **Country card de Chile**: `country_cards_data/CHL_country_card_data.csv`.
- **Country card de Singapur**: `country_cards_data/SGP_country_card_data.csv`.
