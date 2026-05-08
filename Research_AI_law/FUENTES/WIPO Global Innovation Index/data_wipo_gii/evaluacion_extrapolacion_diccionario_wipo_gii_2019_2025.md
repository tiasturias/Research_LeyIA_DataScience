# Evaluación de extrapolación del diccionario LLM WIPO/GII para 2019–2025

## Conclusión ejecutiva

El archivo `diccionario_llm_wipo_gii_2025.md` **sí puede convertirse en una plantilla general para trabajar con los Excel del Global Innovation Index (GII)**, pero **no debe extrapolarse literalmente a cualquier año sin validación**.

La revisión cruzada de `wipo-pub-2000-2024-tech1.xlsx` con `wipo-pub-2000-2025-tech1.xlsx` muestra que entre 2024 y 2025 la **estructura de hojas y columnas es estable**, y la arquitectura conceptual principal también se mantiene: índice global, 2 subíndices, 7 pilares, 21 subpilares y 78 indicadores. Sin embargo, hay cambios de cobertura, de países, de nombres de indicadores, de códigos, de fuentes, de metodología y de rangos observados.

Por tanto:

- **Extrapolable**: diccionario de hojas, diccionario de columnas, lógica de `SCORE`, `RANK`, `VALUE_SCREEN`, `DATAYR`, `SW_OVERALL`, `SW_INCGRP`, `OUTDATED`, `DMC`, y la lógica jerárquica GII.
- **No extrapolable sin recalcular**: lista exacta de indicadores, nombres, códigos `NUM`, rangos, fuentes, URLs, países incluidos, años disponibles, fortalezas/debilidades y cualquier comparación interanual directa.
- **Regla para un LLM**: cada vez que se abra un Excel de otro año, primero debe leer `Index Structure`, `Economies`, `Data` y `Metadata`; luego debe construir el diccionario específico del año antes de analizar.

---

## 1. Comparación estructural 2024 vs 2025

| Campo                     | 2024                                       | 2025                                       |
|:--------------------------|:-------------------------------------------|:-------------------------------------------|
| Archivo Excel             | wipo-pub-2000-2024-tech1.xlsx              | wipo-pub-2000-2025-tech1.xlsx              |
| Hojas                     | Index Structure, Economies, Data, Metadata | Index Structure, Economies, Data, Metadata |
| Columnas por hoja         | idénticas al 2025                          | idénticas al 2024                          |
| Economías                 | 133                                        | 139                                        |
| Filas Data                | 14497                                      | 15151                                      |
| Conceptos GII             | 109                                        | 109                                        |
| Indicadores               | 78                                         | 78                                         |
| Subpilares                | 21                                         | 21                                         |
| Pilares                   | 7                                          | 7                                          |
| Subíndices                | 2                                          | 2                                          |
| Índice global             | 1                                          | 1                                          |
| Tipos de indicadores      | 63 Data, 10 Index, 5 Survey                | 63 Data, 10 Index, 5 Survey                |
| Rango GII SCORE observado | 10.2162 – 67.4731                          | 11.9450 – 65.9620                          |
| Rango SCORE general       | 0 – 100                                    | 0 – 100                                    |
| Rango RANK                | 1 – 133                                    | 1 – 139                                    |
| Rango DATAYR              | 2013 – 2024                                | 2015 – 2025                                |

---

## 2. Hojas y columnas: qué parte del diccionario sí es generalizable

| Hoja            | Columnas estables                                                                                      | Qué se puede extrapolar              | Qué debe recalcularse por año                                                                           |
|:----------------|:-------------------------------------------------------------------------------------------------------|:-------------------------------------|:--------------------------------------------------------------------------------------------------------|
| Index Structure | NUM, NAME, LEVEL, TYPE, PROFILE, DESCRIPTION, SOURCE, WEBSITE                                          | Sí: función de diccionario maestro.  | filas, nombres, descripciones, fuentes, URLs, indicadores agregados/eliminados                          |
| Economies       | ISO3, ECONOMY_NAME, INCOME, REG_UN, REG_UN_CODE, POP, PPPGDP, PPPPC                                    | Sí: metadatos país/economía.         | economías cubiertas, grupos de ingreso, región si WIPO/ONU/Banco Mundial actualiza, población y PIB PPP |
| Data            | ISO3, ECONOMY_NAME, NUM, NAME, DATAYR, VALUE_SCREEN, SCORE, RANK, SW_OVERALL, SW_INCGRP, OUTDATED, DMC | Sí: tabla larga país × concepto GII. | rangos, valores, rankings, años de dato, fortalezas/debilidades, DMC                                    |
| Metadata        | SHEET, COLUMN, DESCRIPTION                                                                             | Sí: glosario técnico de columnas.    | verificar si WIPO cambió alguna descripción                                                             |

---

## 3. Diferencias críticas detectadas entre 2024 y 2025

| Tipo                       | 2024                                                             | 2025                                                                           | Implicancia LLM                                                                     |
|:---------------------------|:-----------------------------------------------------------------|:-------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| Cambio de cobertura        | 133 economías                                                    | 139 economías                                                                  | No asumir universo fijo; calcular países desde Economies o ISO3.                    |
| Economías añadidas en 2025 | No presentes                                                     | Congo, Guinea, Lesotho, Malawi, Seychelles, Venezuela (Bolivarian Republic of) | Comparaciones 2024–2025 deben usar intersección de ISO3 o declarar entradas nuevas. |
| Estructura alta            | 1 índice, 2 subíndices, 7 pilares, 21 subpilares, 78 indicadores | igual                                                                          | La arquitectura general sí es extrapolable entre 2024 y 2025.                       |
| Columnas                   | idénticas                                                        | idénticas                                                                      | El diccionario de columnas es reutilizable.                                         |
| Indicadores                | 78 indicadores                                                   | 78 indicadores                                                                 | El conteo coincide, pero la composición cambió.                                     |
| Códigos que cambian        | IN.3.1.4 existe: E-participation*                                | IN.3.1.4 desaparece; aparece IN.4.2.5 VC investor co-participation/bn PPP$ GDP | No usar lista fija de códigos sin leer Index Structure del año.                     |

---

## 4. Cambios de nombre o reordenamiento de indicadores detectados

Estos cambios muestran por qué el `.md` 2025 no debe copiarse literalmente para 2024 ni para años anteriores.

| Código    | 2024                                               | 2025                                                   | Lectura                                                                         |
|:----------|:---------------------------------------------------|:-------------------------------------------------------|:--------------------------------------------------------------------------------|
| IN.3.1    | Information and communication technologies (ICTs)  | Information and communication technology (ICT)         | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| IN.3.1.3  | Government's online service*                       | Government online service*                             | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| IN.4.2.2  | Venture capital (VC) investors, deals/bn PPP$ GDP  | Venture capital (VC) received, deal count/bn PPP$ GDP  | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| IN.4.2.3  | VC recipients, deals/bn PPP$ GDP                   | Late-stage VC deal count, % global VC                  | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| IN.4.2.4  | VC received, value, % GDP                          | VC investors, deal count/bn PPP$ GDP                   | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| IN.5.1.2  | Firms offering formal training, %                  | Females employed w/advanced degrees, %                 | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| IN.5.1.3  | GERD performed by business, % GDP                  | Youth demographic dividend, %                          | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| IN.5.1.4  | GERD financed by business, %                       | GERD performed by business, % GDP                      | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| IN.5.1.5  | Females employed w/advanced degrees, %             | GERD financed by business, %                           | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| IN.5.2.3  | State of cluster development†                      | University industry & international engagement, top 5* | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| IN.5.2.4  | Joint venture/strategic alliance deals/bn PPP$ GDP | State of cluster development†                          | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |
| OUT.6.1.2 | PCT patents by origin/bn PPP$ GDP                  | PCT patents by inventor origin/bn PPP$ GDP             | cambio de nombre/reordenamiento; verificar DESCRIPTION antes de comparar series |

---

## 5. Códigos presentes solo en uno de los años revisados

| Código   | Año       | Variable                                 | Qué mide                                                                                                                                                                                                                                                                                                        |
|:---------|:----------|:-----------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IN.3.1.4 | solo 2024 | E-participation*                         | The E-Participation Index (EPI) is a measure of citizen engagement in public policy making through e-government programs. It's a supplement to the United Nations E-Government Survey that assesses how well governments use online services to provide information, interact with stakeholders, and engage ... |
| IN.4.2.5 | solo 2025 | VC investor co-participation/bn PPP$ GDP | Indicator that captures VC deals received by investor location, using fractional counting. For each deal, the total is divided equally among all participating investors (i.e., 1/n per investor, where n is the number of investors). The resulting fractions are aggregated by the investors’ country of h... |

---

## 6. Diccionario de columnas estable observado en 2024 y 2025

| SHEET           | COLUMN       | DESCRIPTION                                                                                                                                                                                                                                                                                                  |
|:----------------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Index Structure | NUM          | Complete GII Index                                                                                                                                                                                                                                                                                           |
| Index Structure | NAME         | Detailed names of the Index, SubIndex, Pillar, SubPillar and Indicators                                                                                                                                                                                                                                      |
| Index Structure | LEVEL        | The level of the GII index: Index, SubIndex, Pillar, SubPillar, Indicator                                                                                                                                                                                                                                    |
| Index Structure | TYPE         | Provides the indicator data type (i.e. Data, Index, Survey)                                                                                                                                                                                                                                                  |
| Index Structure | PROFILE      | This is provided to show if the Score or Value is given when looking at the Economy profiles for a pillar, sub-pillar and indicator level.                                                                                                                                                                   |
| Index Structure | DESCRIPTION  | A detailed description of the index, pillars, subpillars and indicators                                                                                                                                                                                                                                      |
| Index Structure | SOURCE       | Indicator data source(s)                                                                                                                                                                                                                                                                                     |
| Index Structure | WEBSITE      | Indicator data source website(s)                                                                                                                                                                                                                                                                             |
| Economies       | ISO3         | Economy ISO3 code in format AAA.                                                                                                                                                                                                                                                                             |
| Economies       | ECONOMY_NAME | Official economy name                                                                                                                                                                                                                                                                                        |
| Economies       | INCOME       | World Bank Income Group Classification: High Income (HI), Upper-middle income (UM), Lower-middle income (LM), Low income (LI)                                                                                                                                                                                |
| Economies       | REG_UN       | The United Nations Statistics Division (UNSD) region classification: Central and Southern Asia; Europe; Latin America and the Caribbean; Northern Africa and Western Asia; Northern America; South East Asia, East Asia, and Oceania; Sub-Saharan Africa                                                     |
| Economies       | REG_UN_CODE  | The United Nations Statistics Division (UNSD) subregion classification code: Central and Southern Asia (CSA), Europe (EUR), Latin America and the Caribbean (LCN), Northern America (NAC), Northern Africa and Western Asia (NAWA), South East Asia, East Asia, and Oceania (SEAO), Sub-Saharan Africa (SSF) |
| Economies       | POP          | Economy population in thousands                                                                                                                                                                                                                                                                              |
| Economies       | PPPGDP       | Economy gross domestic product (GDP) in $billions PPP                                                                                                                                                                                                                                                        |
| Economies       | PPPPC        | Economy GDP per capita, in $PPP                                                                                                                                                                                                                                                                              |
| Data            | ISO3         | Economy ISO3 code                                                                                                                                                                                                                                                                                            |
| Data            | ECONOMY_NAME | Official economy name                                                                                                                                                                                                                                                                                        |
| Data            | NUM          | Complete GII Index                                                                                                                                                                                                                                                                                           |
| Data            | NAME         | Detailed names of the Index, SubIndex, Pillar, SubPillar and Indicators                                                                                                                                                                                                                                      |
| Data            | DATAYR       | The data year available for the given indicator and economy                                                                                                                                                                                                                                                  |
| Data            | VALUE_SCREEN | Screened indicator value                                                                                                                                                                                                                                                                                     |
| Data            | SCORE        | Normalized and aggregated supra-indicator value                                                                                                                                                                                                                                                              |
| Data            | RANK         | The rank of the normalized scores                                                                                                                                                                                                                                                                            |
| Data            | SW_OVERALL   | The overall strengths and weaknesses are the top- and bottom-ranked indicators for each country                                                                                                                                                                                                              |
| Data            | SW_INCGRP    | Income group strengths and weaknesses are the respective high- and low-performing indicators within income groups.                                                                                                                                                                                           |
| Data            | OUTDATED     | Indicates an indicator is outdated when the last available data year for a particular economy is below the most frequent year reported by all economies (i.e. the mode year)                                                                                                                                 |
| Data            | DMC          | Indicates that the data minimum coverage (DMC) requirements were not met at the sub-pillar or pillar level                                                                                                                                                                                                   |

---

## 7. Regla metodológica para usar el Excel de cualquier año GII

### 7.1. Nunca asumir que `VALUE_SCREEN` es comparable entre indicadores

`VALUE_SCREEN` es el valor original o valor mostrado del indicador. Puede ser porcentaje, índice, monto, conteo normalizado por PIB PPP, ranking universitario, gasto, población, exportaciones, etc.

Un LLM debe usar `VALUE_SCREEN` solo para explicar el dato original de una variable concreta. Para comparar desempeño entre países o variables debe usar `SCORE`.

### 7.2. Usar `SCORE` para comparaciones dentro del año

`SCORE` es el valor normalizado o agregado. En indicadores individuales suele estar en escala 0–100. En subpilares, pilares, subíndices e índice global es un puntaje agregado.

### 7.3. Usar `RANK` con cuidado

`RANK = 1` significa mejor posición dentro de esa variable y ese año. El rango máximo depende del número de economías con datos disponibles y del año: en 2024 llega a 133; en 2025 llega a 139.

### 7.4. No comparar rankings interanuales sin advertencia

Los rankings GII no son estrictamente comparables año a año porque:
- entran y salen economías;
- cambian indicadores;
- cambian metodologías;
- se actualizan fuentes;
- cambian datos faltantes;
- cambian reglas de cobertura mínima.

### 7.5. Leer `Index Structure` siempre antes de interpretar indicadores

El nombre, descripción, tipo, perfil, fuente y URL de cada indicador deben extraerse desde `Index Structure` del año correspondiente. No basta con usar el nombre del indicador de 2025.

### 7.6. Leer `Economies` siempre antes de análisis regional o por ingreso

Los grupos `INCOME`, regiones `REG_UN`, población, PIB PPP y PIB PPP per cápita cambian o pueden actualizarse cada año.

### 7.7. Entender `SW_OVERALL` y `SW_INCGRP`

- `SW_OVERALL = S`: fortaleza general relativa.
- `SW_OVERALL = W`: debilidad general relativa.
- `SW_INCGRP = S`: fortaleza frente a economías del mismo grupo de ingreso.
- `SW_INCGRP = W`: debilidad frente a economías del mismo grupo de ingreso.

No significa necesariamente “política pública buena/mala”; significa desempeño relativo dentro del modelo GII.

### 7.8. Entender `OUTDATED`

`OUTDATED = 1` indica que el dato usado para una economía en una variable está rezagado respecto del año modal disponible para esa variable. En 2024 el Excel conserva ceros explícitos en muchos casos; en 2025 aparece mayormente como `1` o vacío. Por eso debe leerse como flag positivo: `1 = dato rezagado`; vacío/0 = no flag.

### 7.9. Entender `DMC`

`DMC = 1` indica problema de cobertura mínima de datos para un pilar/subpilar. No debe tratarse como puntaje; es una alerta de calidad/cobertura.

---

## 8. Qué debe hacer un LLM al recibir un Excel GII de 2019–2025

1. Identificar el año del archivo desde el nombre o el PDF asociado.
2. Leer hojas disponibles.
3. Confirmar que existen `Index Structure`, `Economies`, `Data` y `Metadata`.
4. Extraer columnas reales de cada hoja.
5. Contar economías desde `Economies`.
6. Contar conceptos desde `Index Structure`.
7. Contar indicadores con `LEVEL == "Indicator"`.
8. Contar tipos de indicadores con `TYPE`.
9. Extraer rangos observados de:
   - `SCORE`
   - `RANK`
   - `DATAYR`
   - `VALUE_SCREEN` por indicador, no globalmente.
10. Construir diccionario específico del año con `NUM`, `NAME`, `LEVEL`, `TYPE`, `PROFILE`, `DESCRIPTION`, `SOURCE`, `WEBSITE`.
11. No reutilizar listas de indicadores de otro año salvo que se haya verificado que coinciden.
12. Para comparar años, construir un mapeo por `NUM` y por `NAME`, y detectar:
   - códigos agregados;
   - códigos eliminados;
   - códigos renombrados;
   - códigos con cambio de descripción;
   - fuentes actualizadas;
   - cambios de perfil `Score`/`Value`;
   - cambios de tipo `Data`/`Index`/`Survey`.

---

## 9. Recomendación sobre el `.md` 2025

El `.md` 2025 debe separarse en dos capas:

### Capa A: plantilla universal GII

Esta parte sí se puede usar para 2019–2025:
- explicación de hojas;
- explicación de columnas;
- lógica jerárquica del índice;
- definición conceptual de `SCORE`, `RANK`, `VALUE_SCREEN`;
- advertencias sobre comparabilidad;
- reglas para `OUTDATED`, `DMC`, `SW_OVERALL`, `SW_INCGRP`.

### Capa B: anexo específico del año

Esta parte debe regenerarse para cada año:
- número de economías;
- número de filas;
- lista de indicadores;
- rangos observados;
- fuentes;
- URLs;
- variables añadidas/eliminadas;
- cambios metodológicos;
- países incluidos/excluidos;
- rankings y puntajes.

---

## 10. Respuesta final a la pregunta

Sí, se puede extrapolar **como arquitectura de trabajo**, pero no como diccionario cerrado de variables. Para 2024 y 2025, el diseño del Excel es suficientemente estable como para crear una guía universal para LLM. Sin embargo, cualquier uso serio entre 2019 y 2025 debe recalcular automáticamente el anexo específico del año desde `Index Structure` y `Data`.

La forma correcta no es decir: “este `.md` 2025 sirve para todos los años”.  
La forma correcta es decir: “este `.md` 2025 sirve como base para una plantilla universal, siempre que cada año regenere su inventario de indicadores, rangos, fuentes y cobertura”.

