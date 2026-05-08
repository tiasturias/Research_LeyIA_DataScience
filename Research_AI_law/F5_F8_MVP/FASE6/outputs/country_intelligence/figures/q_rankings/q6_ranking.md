# Q6 — Ranking de Sector Público y Capacidad Digital por País

## 1. ¿Qué estoy viendo en esta imagen?

Esta imagen es un **diagrama de barras horizontales** (*horizontal bar chart*).

- **Eje Y (vertical)**: cada fila es un **país** (código ISO3 de 3 letras). Los 43 países de la muestra, ordenados de **mayor a menor percentil** de arriba hacia abajo. Quien encabeza la lista tiene la mayor capacidad relativa del sector público en materia de IA y gobierno digital.

- **Eje X (horizontal)**: el **percentil descriptivo de capacidad del sector público en IA**, un valor entre **0.00 y 1.00**. Barra más larga = mejor posicionado en capacidades públicas digitales frente a los otros 42 países.

- **Colores**: rojo = Chile (CHL, país focal), verde = Singapur (SGP, benchmark #1), azul = países destacados, gris claro = resto.

- **Orden**: de mayor a menor percentil, resultado de promediar los percentiles individuales de los 6 (o 7 para Chile) indicadores de sector público.

## 2. ¿Qué pregunta de investigación responde Q6?

La pregunta **Q6** del estudio es:

> *"¿Los países con más rasgos regulatorios de IA muestran mayor capacidad pública, gobernanza digital o adopción estatal de IA?"*

En lenguaje simple: ¿los países con más leyes y normas de IA son también los países cuyos gobiernos tienen más capacidades digitales, mejor gobernanza de datos, políticas digitales más desarrolladas, mejor entrega de servicios de e-government y mayor adopción de IA en el sector público?

**Advertencia específica de Q6**: el sector público es **multidimensional**. Tener buena política digital (visión, planificación) NO es lo mismo que tener buena entrega de servicios (ejecución, portales, trámites). Tener buena gobernanza de datos NO es lo mismo que tener buena gobernanza ética. Q6 captura 6 dimensiones distintas del sector público, y un país puede ser fuerte en unas y débil en otras. El percentil de Q6 promedia todas, lo que puede ocultar estas diferencias internas.

## 3. ¿Qué mide exactamente el percentil de Q6?

El percentil de Q6 es el **promedio de 6 percentiles individuales** (7 para Chile, que tiene un indicador adicional de OECD). Es la Q con **más indicadores** de todo el estudio, lo que la hace la medición más comprehensiva:

| Indicador (outcome) | ¿Qué mide en el mundo real? | Fuente | Países con dato |
|---|---|---|---|
| `oxford_public_sector_adoption` | **Adopción de IA en el sector público**. Evalúa si las entidades gubernamentales del país han incorporado inteligencia artificial en sus operaciones: atención ciudadana, toma de decisiones, análisis de datos, automatización de procesos. Un valor alto (ej. Estonia = 99.6) indica un gobierno que usa IA de forma generalizada. Este indicador también aparece en Q2. | Oxford Insights — Government AI Readiness Index 2024 | 43 |
| `oxford_e_government_delivery` | **Entrega de servicios de gobierno electrónico**. Mide la calidad y cobertura de los servicios digitales que el gobierno ofrece a los ciudadanos: portales de trámites, identidad digital, servicios en línea, interoperabilidad entre instituciones. Un valor alto (ej. Estonia = 100.0, Chile = 96.5) significa que los ciudadanos pueden hacer la mayoría de sus trámites en línea sin papel ni filas. | Oxford Insights — Government AI Readiness Index 2024 | 43 |
| `oxford_government_digital_policy` | **Política digital gubernamental**. Evalúa si el gobierno tiene una estrategia nacional de IA, una política de datos abiertos, una agenda digital, regulaciones de protección de datos y ciberseguridad. Un valor alto indica que el país tiene un marco normativo y estratégico sólido para la transformación digital. Un valor bajo (ej. Chile = 45.0) sugiere que la arquitectura de políticas digitales aún está en construcción. | Oxford Insights — Government AI Readiness Index 2024 | 43 |
| `oxford_ind_data_governance` | **Gobernanza de datos**. Mide la existencia y calidad de marcos para la gestión, protección, compartición y uso ético de datos por parte del gobierno. Incluye leyes de protección de datos, estándares de interoperabilidad, políticas de datos abiertos y mecanismos de supervisión. | Oxford Insights — Government AI Readiness Index 2024 | 43 |
| `oxford_governance_ethics` | **Gobernanza ética de IA/digital**. Evalúa si el país tiene marcos éticos para el desarrollo y uso de IA: principios de IA responsable, comités de ética, evaluaciones de impacto algorítmico, regulaciones contra sesgos y discriminación automatizada. Un valor alto (ej. Chile = 83.8) indica un compromiso con la IA ética. | Oxford Insights — Government AI Readiness Index 2024 | 43 |
| `oecd_2_indigo_oecd_indigo_score` | **Score INDIGO de gobierno digital** de la OECD. Es un indicador compuesto que mide la madurez del gobierno digital en países OECD y socios, evaluando 6 dimensiones: digital por diseño, sector público impulsado por datos, gobierno como plataforma, abierto por defecto, centrado en el usuario, y proactividad. | OECD — Digital Government Index (INDIGO) | 43 |
| `oecd_4_digital_gov_oecd_digital_gov_overall` | **Score general de gobierno digital** de la OECD. Similar al anterior pero a nivel más agregado. **Solo 31 países tienen este dato**. Chile sí lo tiene (0.40), pero no se incluye en el promedio principal de Q6 para mantener comparabilidad. | OECD — Digital Government Review | 31 |

### ¿Cómo se calcula el percentil de Q6?

1. Para cada indicador, se ordenan los países con dato de mayor a menor.
2. Se asigna percentil individual.
3. Se promedian los percentiles de los indicadores disponibles.

**Nota sobre Chile**: Chile tiene los 6 indicadores principales más 2 indicadores adicionales de OECD (`oecd_2_indigo_oecd_indigo_score` y `oecd_4_digital_gov_oecd_digital_gov_overall`). El percentil de Q6 de Chile (0.336) se calcula promediando los 6 indicadores principales (sin incluir `oecd_4_digital_gov_oecd_digital_gov_overall` para mantener comparabilidad con países que no tienen ese dato).

## 4. Interpretación de los valores del percentil

| Percentil | Significado | Etiqueta |
|---|---|---|
| 0.87 (Estonia en Q6) | Está por encima del 87% de los países en capacidades públicas digitales | `high_performer` |
| 0.84 (Dinamarca en Q6) | Está por encima del 84% | `high_performer` |
| 0.66 (Singapur en Q6) | Está por encima del 66% | `middle_performer` |
| 0.34 (Chile en Q6) | Está por encima de solo el 34% de los países. El 66% tiene mayor capacidad pública digital. | `low_performer` |
| 0.11 (China en Q6) | Está por encima de solo el 11% | `bottom_laggard` |

## 5. Top 5 y Bottom 5 de Q6

### Los 5 países con mayor capacidad del sector público en IA:

| Posición | País | ISO3 | Percentil Q6 | Etiqueta |
|---|---|---|---|---|
| **1** | Estonia | EST | 0.868 | high_performer |
| **2** | Dinamarca | DNK | 0.838 | high_performer |
| **3** | Países Bajos | NLD | 0.819 | high_performer |
| **4** | Estados Unidos | USA | 0.783 | high_performer |
| **5** | Francia | FRA | 0.772 | high_performer |

### Los 5 países con menor capacidad del sector público en IA:

| Posición | País | ISO3 | Percentil Q6 | Etiqueta |
|---|---|---|---|---|
| **39** | Bulgaria | BGR | 0.260 | low_performer |
| **40** | Rumania | ROU | 0.212 | low_performer |
| **41** | Qatar | QAT | 0.196 | bottom_laggard |
| **42** | Costa Rica | CRI | 0.187 | bottom_laggard |
| **43** | China | CHN | 0.114 | bottom_laggard |

### Estonia: ¿por qué es #1 en sector público?

Estonia es mundialmente reconocida como el país con el gobierno digital más avanzado del mundo (a menudo llamado "e-Estonia"). Algunos factores que explican su posición:
- **99% de los servicios públicos disponibles en línea** las 24 horas.
- **Identidad digital obligatoria** para todos los ciudadanos desde los 15 años.
- **Sistema X-Road**: una capa de interoperabilidad que conecta todas las bases de datos del gobierno de forma segura.
- **Voto electrónico** desde 2005.
- **Residencia electrónica (e-Residency)**: permite a extranjeros crear y gestionar empresas en Estonia completamente en línea.
- **Política de "once only"**: el ciudadano nunca debe entregar el mismo dato dos veces al gobierno.

Estonia es un caso de estudio mundial en transformación digital del Estado, y por eso fue seleccionado como benchmark para Chile en este estudio.

## 6. Chile en Q6: detalle completo

| Dato | Valor |
|---|---|
| Percentil Q6 | **0.336** |
| Ranking global | **aproximadamente 30 de 43** |
| Etiqueta | `low_performer` |
| ¿Es fortaleza o debilidad? | **Mixto**. Chile tiene una fortaleza y una debilidad muy marcadas dentro de Q6. |

### Desglose por indicador individual:

| Indicador | Valor observado | Percentil | Rank | Etiqueta |
|---|---|---|---|---|
| Adopción IA en sector público | 70.76 | 0.33 | 30/43 | low_performer |
| **Entrega de e-government** | **96.53** | **0.79** | **10/43** | **high_performer** ★ |
| **Política digital gubernamental** | **45.00** | **0.12** | **39/43** | **bottom_laggard** ▼ |
| Gobernanza de datos | 50.00 | 0.36 | 16/43 | low_performer |
| Gobernanza ética de IA | 83.84 | 0.37 | 28/43 | low_performer |
| Score INDIGO (OECD) | 0.083 | 0.26 | 33/43 | low_performer |
| Score gobierno digital OECD (extra) | 0.40 | 0.13 | 28/31 | bottom_laggard |

### Interpretación del perfil chileno en sector público:

Chile presenta en Q6 un perfil **extremadamente polarizado** — más que en cualquier otra Q:

**Fortaleza principal: entrega de e-government (percentil 0.79)**
Chile tiene un sistema de gobierno electrónico notablemente bueno para los estándares de la muestra. Con 96.53 puntos, está en el top 10 mundial (rank 10 de 43). Esto refleja inversiones históricas en digitalización del Estado: ChileAtiende, ClaveÚnica, la plataforma de compras públicas, el portal de transparencia, la interoperabilidad de registros civiles, entre otros. En este indicador, Chile está por encima del 79% de los países de la muestra, incluyendo a varios países europeos.

**Debilidad crítica: política digital gubernamental (percentil 0.12)**
A pesar de tener buena ejecución (e-government delivery), Chile tiene una de las políticas digitales más débiles de la muestra. Con 45.0 puntos y percentil 0.12 (rank 39/43), esto indica que el marco estratégico y normativo para la transformación digital del Estado está rezagado. En otras palabras: Chile **ejecuta bien pero planifica y regula poco** en materia digital. La Ley Marco de IA (Boletín 16821-19) que motiva este estudio busca precisamente cerrar esta brecha: dotar al país de un marco normativo para la IA que acompañe sus capacidades de ejecución.

**Indicadores intermedios**: adopción de IA en sector público (0.33), gobernanza de datos (0.36), gobernanza ética (0.37) — todos en zona baja. El score INDIGO de la OECD (0.26) también es bajo, confirmando que la madurez digital integral del Estado chileno tiene espacio de mejora significativo.

### Resumen del perfil chileno en Q6:

| Dimensión | Desempeño | Mensaje |
|---|---|---|
| Ejecución (e-government delivery) | ★ Alto (0.79) | Chile sabe construir infraestructura digital |
| Planificación (política digital) | ▼ Muy bajo (0.12) | Chile carece de marco estratégico robusto |
| Gobernanza (datos, ética) | Bajo (0.36-0.37) | Los marcos de gobernanza de IA están en desarrollo |
| Madurez integral (INDIGO) | Bajo (0.26) | La madurez digital del Estado es limitada |

## 7. Comparación con Singapur

| Indicador de Q6 | Chile | Singapur | Diferencia |
|---|---|---|---|
| Adopción IA sector público | 0.33 | mayor | Significativa |
| Entrega e-government | **0.79** | mayor | Singapur también es fuerte aquí |
| Política digital | **0.12** | mayor | Brecha enorme en planificación |
| Gobernanza de datos | 0.36 | mayor | Significativa |
| Gobernanza ética | 0.37 | mayor | Moderada |
| Score INDIGO | 0.26 | mayor | Significativa |

La brecha total Chile-Singapur en Q6 es de **0.323 puntos de percentil**, la tercera más grande después de Q3 (0.624) y Q2 (0.500).

## 8. La nota metodológica de la imagen

> *"Nota: posicionamiento descriptivo in-sample; no es predicción independiente ni causalidad. Su robustez debe evaluarse en Fase 7 antes de convertirse en recomendación de política pública."*

Mismo significado que en todos los gráficos. Refuerzo para Q6:
- El hecho de que Chile tenga buena ejecución y mala política NO prueba que una cause la otra.
- Los datos de Oxford Insights y OECD reflejan la situación observada en 2024. No predicen el efecto de la futura Ley Marco de IA.
- La polarización del perfil chileno (fuerte en ejecución, débil en planificación) es un hallazgo descriptivo que Fase 7 debe validar como robusto.

## 9. ¿Qué puedo y qué NO puedo concluir?

### Lo que SÍ puedes concluir:

- "Estonia, Dinamarca, Países Bajos, Estados Unidos y Francia lideran en capacidad del sector público para IA y gobierno digital."
- "Chile tiene un perfil polarizado en Q6: muy buen desempeño en entrega de e-government (percentil 0.79) pero muy bajo en política digital gubernamental (percentil 0.12)."
- "La principal debilidad del sector público chileno en IA no es la ejecución sino el marco estratégico y normativo."
- "Q6 es la pregunta con más indicadores del estudio (6 principales), lo que la convierte en la medición más comprehensiva."

### Lo que NO puedes concluir:

- "La buena ejecución de e-government de Chile se debe a su baja regulación." (No hay prueba causal; podría ser al revés o deberse a otros factores.)
- "Aprobar la Ley Marco de IA automáticamente subirá el percentil de Chile en política digital." (El estudio no hace predicciones.)
- "Estonia es #1 en sector público porque no tiene regulación de IA." (Estonia opera bajo el marco regulatorio de la Unión Europea, incluyendo el EU AI Act.)
- "China tiene el peor sector público digital del mundo." (Solo es el último de esta muestra de 43 países, y puede tener capacidades no capturadas por fuentes occidentales.)

## 10. ¿Dónde encuentro más información?

- **Resultados de modelos Q6**: `q6_results.csv` con 36 filas de asociaciones entre predictores regulatorios y outcomes de sector público.
- **Scores por país**: `q6_scores_per_country.csv` con 606 filas de valores observados.
- **Country card de Chile**: `country_cards_data/CHL_country_card_data.csv`.
- **Country card de Estonia**: `country_cards_data/EST_country_card_data.csv`.
- **Notebook didáctico**: sección 3 del notebook de auditoría humana (Q6).
