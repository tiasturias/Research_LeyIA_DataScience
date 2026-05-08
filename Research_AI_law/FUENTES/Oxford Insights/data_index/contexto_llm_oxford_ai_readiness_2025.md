# Contexto LLM para trabajar con el Excel `2025-Government-AI-Readiness-Index-data-1.xlsx`

## Propósito de este archivo

Este `.md` está diseñado para ser entregado como contexto a un LLM que deba leer, limpiar, interpretar, analizar o explicar el Excel del **Government AI Readiness Index 2025** de Oxford Insights. El foco principal es la hoja **`Dimensions-Pillars`**, porque es la hoja que contiene el puntaje total, los seis pilares y las catorce dimensiones por país.

El objetivo es evitar errores comunes de interpretación: tratar puntajes como porcentajes literales, promediar rankings, usar columnas separadoras como variables, confundir pilares con dimensiones, o inferir indicadores crudos que el Excel no trae.

## Fuentes utilizadas y jerarquía de confianza

1. **Fuente principal para datos numéricos:** Excel adjunto `2025-Government-AI-Readiness-Index-data-1.xlsx`.
2. **Fuente conceptual:** PDF adjunto `2025_government_ai_readiness_index.pdf`, especialmente introducción, framework, full rankings y metodología.
3. **Fuente web oficial:** página de Oxford Insights del Government AI Readiness Index 2025: `https://oxfordinsights.com/ai-readiness/government-ai-readiness-index-2025/`.

**Regla para el LLM:** si hay diferencias entre el PDF narrativo y los valores del Excel, usar el **Excel** como fuente de verdad para análisis numérico. Usar el PDF y la página para marco conceptual, definición del índice y metodología.

## Qué mide el índice

El índice busca responder: **¿hasta qué punto puede un gobierno aprovechar la IA para beneficiar al público?**

La edición 2025 evalúa **195 gobiernos/países**. Según el reporte, el marco usa **69 indicadores**, agrupados en **14 dimensiones** y **6 pilares**. El Excel adjunto NO entrega los 69 indicadores crudos; entrega puntajes ya agregados por país.

## Estructura del workbook

El archivo contiene 2 hojas:

| Hoja | Rango usado | Qué contiene | Observaciones para LLM |
|---|---:|---|---|
| `Global Rankings` | `A1:D197` | Ranking, país y puntaje total. | La columna A está vacía; los encabezados reales están en fila 2, columnas B:D. Es una vista reducida y duplica Ranking/Country/Total Score de `Dimensions-Pillars`. |
| `Dimensions-Pillars` | `A1:Y197` | Ranking, país, Total Score, 6 pilares, 14 dimensiones. | Fila 1 contiene etiquetas visuales de grupo; fila 2 contiene encabezados reales; filas 3-197 contienen países. Columnas D y K están vacías y deben eliminarse. |

## Reglas de lectura/importación

### Para `Dimensions-Pillars`

- Usar la **fila 2** como header real.
- Ignorar la fila 1 para análisis tabular; solo tiene etiquetas visuales: `Pillars` y `Dimensions`.
- Ignorar/eliminar columnas sin nombre: **D** y **K**.
- Las filas de datos son **3 a 197**, equivalentes a **195 países**.
- No hay valores faltantes en las 23 variables reales.
- La hoja está ordenada alfabéticamente por país, no por ranking. Para obtener top/bottom, ordenar por `Ranking` o `Total Score`.

### Para `Global Rankings`

- Usar la **fila 2** como header real.
- Ignorar la columna A vacía.
- Usar columnas B:D: `Ranking`, `Country`, `Total Score`.
- Esta hoja no agrega información analítica adicional frente a `Dimensions-Pillars`; es una vista resumida.

## Naturaleza de los valores

- `Ranking` es un entero ordinal: 1 = mejor posición global; 195 = peor posición global.
- `Country` es texto/categoría.
- Todos los puntajes (`Total Score`, pilares y dimensiones) son numéricos continuos normalizados en escala **0-100**.
- Los puntajes NO deben interpretarse como porcentajes literales de cumplimiento.
- Un puntaje 80 significa mejor desempeño relativo que uno de 60 dentro del marco y la muestra, pero no significa '80% de preparación absoluta'.
- Algunos valores aparecen como enteros porque el resultado redondeado no tiene decimales; para análisis, tratar todos los puntajes como `float`.
- El Excel no contiene fórmulas; contiene valores estáticos ya calculados.

## Fórmula de agregación operacional

El `Total Score` puede aproximarse desde los pilares con los siguientes pesos:

| Pilar | Peso en Total Score |
|---|---:|
| Policy Capacity | 10% |
| AI Infrastructure | 25% |
| Governance | 15% |
| Public Sector Adoption | 15% |
| Development & Diffusion | 25% |
| Resilience | 10% |

Fórmula equivalente:

```text
total_score =
  0.10 * policy_capacity +
  0.25 * ai_infrastructure +
  0.15 * governance +
  0.15 * public_sector_adoption +
  0.25 * development_diffusion +
  0.10 * resilience
```

También puede reconstruirse desde dimensiones con estos pesos:

| Dimensión | Peso en Total Score |
|---|---:|
| Policy vision | 4.00% |
| Policy commitment | 6.00% |
| Compute capacity | 8.33% |
| Enabling technical infrastructure | 8.33% |
| Data quality | 8.33% |
| Governance principles | 7.50% |
| Regulatory compliance | 7.50% |
| Government digital policy | 7.50% |
| e-Government delivery | 7.50% |
| Human capital | 7.50% |
| AI sector maturity | 10.00% |
| AI technology diffusion | 7.50% |
| Societal transition | 5.00% |
| Safety and security | 5.00% |

Fórmula dimensional:

```text
total_score =
  0.04   * policy_vision +
  0.06   * policy_commitment +
  0.0833333333 * compute_capacity +
  0.0833333333 * enabling_technical_infrastructure +
  0.0833333333 * data_quality +
  0.075  * governance_principles +
  0.075  * regulatory_compliance +
  0.075  * government_digital_policy +
  0.075  * e_government_delivery +
  0.075  * human_capital +
  0.10   * ai_sector_maturity +
  0.075  * ai_technology_diffusion +
  0.05   * societal_transition +
  0.05   * safety_security
```

Por redondeo a dos decimales en el Excel, las reconstrucciones pueden diferir por menos de 0,01 puntos.

## Jerarquía conceptual

| Pilar | Dimensiones que lo componen | Interpretación breve |
|---|---|---|
| Policy Capacity | Policy vision, Policy commitment | Mide la capacidad del gobierno para diseñar e implementar políticas públicas de IA alineadas con una visión nacional clara y con compromiso institucional. Incluye visión de política y compromiso de política. |
| AI Infrastructure | Compute capacity, Enabling technical infrastructure, Data quality | Mide las condiciones técnicas para desarrollar, desplegar y usar IA: cómputo, infraestructura digital, conectividad, energía, ciberseguridad y datos. |
| Governance | Governance principles, Regulatory compliance | Mide el marco de gobernanza de IA: principios, normas, protección de derechos, gestión de riesgos, transparencia, protección de datos y capacidad de cumplimiento regulatorio. |
| Public Sector Adoption | Government digital policy, e-Government delivery | Mide si el gobierno está preparado para probar, adoptar y escalar IA en la administración pública y en servicios públicos digitales. |
| Development & Diffusion | Human capital, AI sector maturity, AI technology diffusion | Mide la madurez del ecosistema de IA y su difusión en economía, academia, empresas y sociedad: capital humano, sector IA e incorporación tecnológica. |
| Resilience | Societal transition, Safety and security | Mide la capacidad de gestionar impactos sociales, económicos, ambientales, de seguridad y ciberseguridad asociados a una adopción amplia de IA. |

## Diccionario compacto de variables

| Columna Excel | Variable original | Nombre canónico sugerido | Sección | Tipo para LLM | Rango teórico | Rango observado en Excel | Missing |
|---:|---|---|---|---|---|---:|---:|
| A | Ranking | ranking | identificador | integer/ordinal | 1-195 en esta edición; 1 es mejor posición. | 1 a 195 | 0 |
| B | Country | country | identificador | string/categorical | Texto libre controlado por Oxford Insights; 195 valores únicos. | 195 valores únicos | 0 |
| C | Total Score | total_score | puntaje final | float/continuous score | 0-100; valor normalizado y ponderado. | 12.12 a 88.36 | 0 |
| E | Policy Capacity | policy_capacity | pilar | float/continuous score | 0-100 | 0 a 100 | 0 |
| F | AI Infrastructure | ai_infrastructure | pilar | float/continuous score | 0-100 | 16.63 a 91.77 | 0 |
| G | Governance | governance | pilar | float/continuous score | 0-100 | 1.39 a 94.57 | 0 |
| H | Public Sector Adoption | public_sector_adoption | pilar | float/continuous score | 0-100 | 0 a 99.63 | 0 |
| I | Development & Diffusion | development_diffusion | pilar | float/continuous score | 0-100 | 9.19 a 88.16 | 0 |
| J | Resilience | resilience | pilar | float/continuous score | 0-100 | 7.46 a 90.01 | 0 |
| L | Policy vision | policy_vision | dimensión | float/continuous score | 0-100 | 0 a 100 | 0 |
| M | Policy commitment | policy_commitment | dimensión | float/continuous score | 0-100 | 0 a 100 | 0 |
| N | Compute capacity | compute_capacity | dimensión | float/continuous score | 0-100 | 0 a 90.92 | 0 |
| O | Enabling technical infrastructure | enabling_technical_infrastructure | dimensión | float/continuous score | 0-100 | 17.72 a 89.61 | 0 |
| P | Data quality | data_quality | dimensión | float/continuous score | 0-100 | 13.30 a 96.55 | 0 |
| Q | Governance principles | governance_principles | dimensión | float/continuous score | 0-100 | 0 a 100 | 0 |
| R | Regulatory compliance | regulatory_compliance | dimensión | float/continuous score | 0-100 | 0 a 92.25 | 0 |
| S | Government digital policy | government_digital_policy | dimensión | float/continuous score | 0-100 | 0 a 99.38 | 0 |
| T | e-Government delivery | e_government_delivery | dimensión | float/continuous score | 0-100 | 0 a 99.98 | 0 |
| U | Human capital | human_capital | dimensión | float/continuous score | 0-100 | 6.18 a 85.17 | 0 |
| V | AI sector maturity | ai_sector_maturity | dimensión | float/continuous score | 0-100 | 0.58 a 100 | 0 |
| W | AI technology diffusion | ai_technology_diffusion | dimensión | float/continuous score | 0-100 | 1.21 a 86.51 | 0 |
| X | Societal transition | societal_transition | dimensión | float/continuous score | 0-100 | 14.92 a 90.67 | 0 |
| Y | Safety and security | safety_security | dimensión | float/continuous score | 0-100 | 0 a 100 | 0 |

## Diccionario detallado de variables

### `Ranking`

- **Columna Excel:** `A`
- **Nombre canónico recomendado:** `ranking`
- **Tipo lógico:** `integer/ordinal`
- **Sección:** `identificador`
- **Rango teórico:** 1-195 en esta edición; 1 es mejor posición.
- **Rango observado en el Excel:** 1 a 195
- **Valores únicos observados:** 195
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Posición global del país dentro del índice. Es un orden derivado del Total Score, no una medida continua. Un número menor significa mejor preparación relativa.
- **Notas para LLM:** Usar para ordenar de mejor a peor. No promediar rankings; para promedios usar Total Score o pilares.
- **País(es) en el mínimo observado:** United States of America
- **País(es) en el máximo observado:** Guinea Bissau

### `Country`

- **Columna Excel:** `B`
- **Nombre canónico recomendado:** `country`
- **Tipo lógico:** `string/categorical`
- **Sección:** `identificador`
- **Rango teórico:** Texto libre controlado por Oxford Insights; 195 valores únicos.
- **Rango observado en el Excel:** 195 valores únicos de texto
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Nombre oficial o convencional del país/territorio usado por Oxford Insights. No incluye código ISO ni región.
- **Notas para LLM:** Para joins externos, normalizar nombres con cuidado: algunos nombres son largos o multilaterales, por ejemplo United Kingdom of Great Britain and Northern Ireland o Bolivia (Plurinational State of).

### `Total Score`

- **Columna Excel:** `C`
- **Nombre canónico recomendado:** `total_score`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `puntaje final`
- **Rango teórico:** 0-100; valor normalizado y ponderado.
- **Rango observado en el Excel:** 12.12 a 88.36
- **Valores únicos observados:** 192
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Puntaje final de preparación gubernamental para IA. Resume los seis pilares y las catorce dimensiones en una escala común.
- **Notas para LLM:** No tratar como porcentaje literal. Es un score comparativo. Sirve para rankings, brechas, percentiles, comparación país-país y promedios.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Guinea Bissau
- **País(es) en el máximo observado:** United States of America

### `Policy Capacity`

- **Columna Excel:** `E`
- **Nombre canónico recomendado:** `policy_capacity`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `pilar`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0 a 100
- **Valores únicos observados:** 55
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide la capacidad del gobierno para diseñar e implementar políticas públicas de IA alineadas con una visión nacional clara y con compromiso institucional. Incluye visión de política y compromiso de política.
- **Notas para LLM:** Alto puntaje sugiere que hay estrategia, prioridades, responsables, recursos o cooperación internacional; bajo puntaje sugiere ausencia/debilidad de dirección estatal en IA.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Afghanistan; Bolivia (Plurinational State of); Chad; Democratic People's Republic of Korea; Equatorial Guinea; Eritrea; Grenada; Kiribati; Madagascar; Marshall Islands; Nauru; Niger; Sao Tome and Principe; South Sudan; Sudan; Suriname; Tuvalu; Yemen
- **País(es) en el máximo observado:** Australia; Egypt; Serbia; United Kingdom of Great Britain and Northern Ireland

### `AI Infrastructure`

- **Columna Excel:** `F`
- **Nombre canónico recomendado:** `ai_infrastructure`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `pilar`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 16.63 a 91.77
- **Valores únicos observados:** 190
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide las condiciones técnicas para desarrollar, desplegar y usar IA: cómputo, infraestructura digital, conectividad, energía, ciberseguridad y datos.
- **Notas para LLM:** Un país puede tener buena política pública, pero bajo desempeño en infraestructura si carece de compute, datos o conectividad robusta.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Burundi
- **País(es) en el máximo observado:** United States of America

### `Governance`

- **Columna Excel:** `G`
- **Nombre canónico recomendado:** `governance`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `pilar`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 1.39 a 94.57
- **Valores únicos observados:** 175
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide el marco de gobernanza de IA: principios, normas, protección de derechos, gestión de riesgos, transparencia, protección de datos y capacidad de cumplimiento regulatorio.
- **Notas para LLM:** No mide solo regulación dura; también puede capturar principios, estándares, soft law, sandboxes y autoridades institucionales relevantes.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Marshall Islands
- **País(es) en el máximo observado:** Ireland

### `Public Sector Adoption`

- **Columna Excel:** `H`
- **Nombre canónico recomendado:** `public_sector_adoption`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `pilar`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0 a 99.63
- **Valores únicos observados:** 194
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide si el gobierno está preparado para probar, adoptar y escalar IA en la administración pública y en servicios públicos digitales.
- **Notas para LLM:** Alto puntaje no significa que todo el Estado ya usa IA masivamente; indica mejores condiciones de política digital y entrega e-government para adoptarla.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Eritrea
- **País(es) en el máximo observado:** Estonia

### `Development & Diffusion`

- **Columna Excel:** `I`
- **Nombre canónico recomendado:** `development_diffusion`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `pilar`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 9.19 a 88.16
- **Valores únicos observados:** 191
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide la madurez del ecosistema de IA y su difusión en economía, academia, empresas y sociedad: capital humano, sector IA e incorporación tecnológica.
- **Notas para LLM:** Es clave para distinguir países que tienen estrategia estatal de aquellos que además tienen ecosistema, talento, investigación y adopción privada.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Niger
- **País(es) en el máximo observado:** United States of America

### `Resilience`

- **Columna Excel:** `J`
- **Nombre canónico recomendado:** `resilience`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `pilar`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 7.46 a 90.01
- **Valores únicos observados:** 190
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide la capacidad de gestionar impactos sociales, económicos, ambientales, de seguridad y ciberseguridad asociados a una adopción amplia de IA.
- **Notas para LLM:** Puntajes altos indican mayor preparación ante riesgos y transición social; no debe interpretarse como ausencia total de riesgo.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Yemen
- **País(es) en el máximo observado:** Denmark

### `Policy vision`

- **Columna Excel:** `L`
- **Nombre canónico recomendado:** `policy_vision`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0 a 100
- **Valores únicos observados:** 13
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide si el país cuenta con una visión estratégica para IA. Incluye señales como estrategia nacional de IA, consejo asesor, actualizaciones de estrategia y cooperación internacional en investigación/gobernanza.
- **Notas para LLM:** Suele reflejar existencia o ausencia de documentos y estructuras de alto nivel. En indicadores de escritorio, algunos componentes subyacentes pueden ser binarios u ordinales, pero esta columna ya es un score agregado.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Afghanistan; Belize; Bolivia (Plurinational State of); Chad; Comoros; Democratic People's Republic of Korea; Equatorial Guinea; Eritrea; Grenada; Kiribati; Madagascar; Marshall Islands; Nauru; Nicaragua; Niger; Sao Tome and Principe; Somalia; South Sudan; Sudan; Suriname; Tuvalu; Yemen
- **País(es) en el máximo observado:** Australia; Belgium; Canada; Chile; China; Denmark; Egypt; France; Japan; Serbia; Singapore; United Kingdom of Great Britain and Northern Ireland; United States of America

### `Policy commitment`

- **Columna Excel:** `M`
- **Nombre canónico recomendado:** `policy_commitment`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0 a 100
- **Valores únicos observados:** 11
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide el compromiso concreto para ejecutar la visión de IA: planes, responsables, presupuesto/dedicación de recursos y participación en espacios internacionales.
- **Notas para LLM:** Distingue países que solo declaran visión de aquellos con ejecución, roadmap o recursos.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Afghanistan; Bahamas; Belarus; Bhutan; Bolivia (Plurinational State of); Chad; Congo; Democratic People's Republic of Korea; Dominica; El Salvador; Equatorial Guinea; Eritrea; Eswatini; Gabon; Grenada; Guinea; Guinea Bissau; Honduras; Kiribati; Kyrgyzstan; Liberia; Madagascar; Maldives; Mali; Marshall Islands; Monaco; Mozambique; Myanmar; Nauru; Niger; Palau; Paraguay; Saint Lucia; Samoa; Sao Tome and Principe; Seychelles; Solomon Islands; South Sudan; Sudan; Suriname; Syrian Arab Republic; Timor-Leste; Togo; Tonga; Tuvalu; Uganda; Yemen; Zimbabwe
- **País(es) en el máximo observado:** Australia; Brazil; Egypt; Estonia; India; Israel; Kazakhstan; Netherlands; New Zealand; Norway; Poland; Republic of Korea; Romania; Saudi Arabia; Serbia; Slovenia; Spain; Sweden; Thailand; United Kingdom of Great Britain and Northern Ireland

### `Compute capacity`

- **Columna Excel:** `N`
- **Nombre canónico recomendado:** `compute_capacity`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0 a 90.92
- **Valores únicos observados:** 70
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide disponibilidad de recursos de cómputo para IA, incluyendo capacidad de despliegue y entrenamiento, supercomputadores públicos y empresas de data center domésticas.
- **Notas para LLM:** Un puntaje 0 puede reflejar ausencia de evidencia o bajo desempeño relativo en compute. No equivale a cantidad exacta de GPUs.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Antigua and Barbuda; Barbados; Belize; Benin; Burundi; Cabo Verde; Central African Republic; Chad; Comoros; Congo; Cuba; Democratic People's Republic of Korea; Dominica; Eritrea; Fiji; Gambia (Republic of The); Grenada; Haiti; Kiribati; Liberia; Marshall Islands; Mauritania; Micronesia (Federated States of); Montenegro; Nauru; Niger; Palau; Saint Kitts and Nevis; Saint Lucia; Saint Vincent and the Grenadines; Samoa; San Marino; Sao Tome and Principe; Sierra Leone; South Sudan; Syrian Arab Republic; Tajikistan; Timor-Leste; Tonga; Turkmenistan; Tuvalu; Vanuatu; Yemen
- **País(es) en el máximo observado:** United States of America

### `Enabling technical infrastructure`

- **Columna Excel:** `O`
- **Nombre canónico recomendado:** `enabling_technical_infrastructure`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 17.72 a 89.61
- **Valores únicos observados:** 193
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide infraestructura técnica habilitante: conectividad, ciberseguridad, infraestructura digital, servidores seguros, energía, electricidad, velocidad de banda ancha y cobertura móvil.
- **Notas para LLM:** No es compute IA puro; mide la base técnica general sobre la que se puede montar el uso de IA.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Niger
- **País(es) en el máximo observado:** United States of America

### `Data quality`

- **Columna Excel:** `P`
- **Nombre canónico recomendado:** `data_quality`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 13.30 a 96.55
- **Valores únicos observados:** 192
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide calidad, disponibilidad y accesibilidad de datos útiles para IA, junto con condiciones de conectividad y brechas de acceso digital.
- **Notas para LLM:** Relacionar con open data, acceso a internet, uso de datos y capacidad de circulación segura de información. No contiene datasets crudos.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Yemen
- **País(es) en el máximo observado:** United Kingdom of Great Britain and Northern Ireland

### `Governance principles`

- **Columna Excel:** `Q`
- **Nombre canónico recomendado:** `governance_principles`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0 a 100
- **Valores únicos observados:** 90
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide la existencia de principios y marcos normativos para orientar el desarrollo y uso de IA de forma segura, ética y compatible con derechos, transparencia y seguridad.
- **Notas para LLM:** Puede capturar ética IA, protección de datos, transparencia algorítmica, regulación de ciberseguridad y señales institucionales de gobernanza.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Democratic People's Republic of Korea; Eritrea; Guinea Bissau
- **País(es) en el máximo observado:** Belgium; China; Denmark; Estonia; France; Germany; Ireland; Israel; Italy; Netherlands; Norway; Poland; Portugal; Republic of Korea; Saudi Arabia; Switzerland; United Kingdom of Great Britain and Northern Ireland; Viet Nam

### `Regulatory compliance`

- **Columna Excel:** `R`
- **Nombre canónico recomendado:** `regulatory_compliance`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0 a 92.25
- **Valores únicos observados:** 95
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide la capacidad institucional y regulatoria para hacer cumplir reglas vinculadas a IA, datos, consumidores, competencia y estándares.
- **Notas para LLM:** Un país puede tener principios altos pero menor cumplimiento si carece de autoridades o mecanismos de enforcement.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Central African Republic; Guinea; Liberia; South Sudan
- **País(es) en el máximo observado:** Ukraine

### `Government digital policy`

- **Columna Excel:** `S`
- **Nombre canónico recomendado:** `government_digital_policy`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0 a 99.38
- **Valores únicos observados:** 128
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide si el gobierno cuenta con política digital y de IA para el sector público: estrategia de IA pública, capacitación de funcionarios, evaluación de servicios, gobernanza de datos y apoyo govtech.
- **Notas para LLM:** Refleja intención y capacidad de política para usar IA dentro del Estado; no necesariamente mide resultados finales de servicios.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Afghanistan; Barbados; Bolivia (Plurinational State of); Central African Republic; Côte D'Ivoire; Eritrea; Gabon; Guinea; Honduras; Malawi; Myanmar; Niger; South Sudan
- **País(es) en el máximo observado:** Estonia

### `e-Government delivery`

- **Columna Excel:** `T`
- **Nombre canónico recomendado:** `e_government_delivery`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0 a 99.98
- **Valores únicos observados:** 194
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide madurez de entrega de servicios públicos digitales: digitalización, infraestructura pública digital, interoperabilidad y compras públicas electrónicas.
- **Notas para LLM:** Es un proxy de capacidad estatal digital. Alto e-government facilita adopción de IA en servicios públicos.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Eritrea
- **País(es) en el máximo observado:** Denmark

### `Human capital`

- **Columna Excel:** `U`
- **Nombre canónico recomendado:** `human_capital`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 6.18 a 85.17
- **Valores únicos observados:** 192
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide disponibilidad de talento y habilidades relevantes para IA: formación técnica, talento internacional, graduados STEM, retención de talento y actividad técnica.
- **Notas para LLM:** Debe interpretarse como capacidad de capital humano, no como número bruto de expertos IA.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Samoa
- **País(es) en el máximo observado:** Singapore

### `AI sector maturity`

- **Columna Excel:** `V`
- **Nombre canónico recomendado:** `ai_sector_maturity`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0.58 a 100
- **Valores únicos observados:** 153
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide madurez del sector IA local: empresas IA, modelos avanzados, unicornios, capital de riesgo, apoyo público/PPP a startups y gasto tecnológico.
- **Notas para LLM:** Es una de las dimensiones con mayor peso individual. Alto puntaje indica ecosistema más sofisticado y capaz de proveer soluciones.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Venezuela, Bolivarian Republic of
- **País(es) en el máximo observado:** United States of America

### `AI technology diffusion`

- **Columna Excel:** `W`
- **Nombre canónico recomendado:** `ai_technology_diffusion`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 1.21 a 86.51
- **Valores únicos observados:** 166
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide difusión y uso de IA en empresas, investigación e instituciones: adopción empresarial, papers IA, centros de investigación y gasto I+D.
- **Notas para LLM:** Ayuda a evaluar si la IA está saliendo del diseño de política hacia uso real en economía y conocimiento.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Sierra Leone
- **País(es) en el máximo observado:** Israel

### `Societal transition`

- **Columna Excel:** `X`
- **Nombre canónico recomendado:** `societal_transition`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 14.92 a 90.67
- **Valores únicos observados:** 183
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide preparación social y económica para la transición hacia una economía con mayor adopción de IA, considerando habilidades, instituciones, derechos laborales, efectividad estatal y sostenibilidad.
- **Notas para LLM:** Usar para análisis de riesgo social/laboral y capacidad institucional de transición.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Yemen
- **País(es) en el máximo observado:** Finland

### `Safety and security`

- **Columna Excel:** `Y`
- **Nombre canónico recomendado:** `safety_security`
- **Tipo lógico:** `float/continuous score`
- **Sección:** `dimensión`
- **Rango teórico:** 0-100
- **Rango observado en el Excel:** 0 a 100
- **Valores únicos observados:** 41
- **Valores faltantes:** 0
- **Qué mide / qué quiere decir:** Mide preparación frente a riesgos de seguridad y safety asociados a IA: monitoreo de riesgos sistémicos, instituciones de AI safety, ciberseguridad y políticas de seguridad.
- **Notas para LLM:** No mide desempeño militar. Se orienta a seguridad, ciberseguridad, monitoreo de riesgos y gobernanza de riesgos.
- **Interpretación de escala:** valores más altos indican mejor preparación/desempeño relativo en esa variable.
- **País(es) en el mínimo observado:** Antigua and Barbuda; Bahamas; Burundi; Central African Republic; Dominica; Eritrea; Grenada; Guinea Bissau; Liberia; Marshall Islands; Nauru; Nicaragua; Saint Lucia; State of Palestine; Yemen
- **País(es) en el máximo observado:** Australia; China; Denmark; France; Japan; Kenya; Republic of Korea; Singapore; Spain; United Kingdom of Great Britain and Northern Ireland; United States of America

## Columnas vacías / separadores visuales

| Columna | Encabezado | Estado | Acción recomendada |
|---:|---|---|---|
| D | vacío | 195 valores nulos | Eliminar antes de análisis. |
| K | vacío | 195 valores nulos | Eliminar antes de análisis. |

## Rangos observados por variable con países extremos

Esta tabla resume extremos. Cuando muchos países empatan en 0 o 100, se listan todos para preservar trazabilidad.

| Variable | Min | País(es) min | Max | País(es) max |
|---|---:|---|---:|---|
| Ranking | 1 | United States of America | 195 | Guinea Bissau |
| Total Score | 12.12 | Guinea Bissau | 88.36 | United States of America |
| Policy Capacity | 0 | Afghanistan; Bolivia (Plurinational State of); Chad; Democratic People's Republic of Korea; Equatorial Guinea; Eritrea; Grenada; Kiribati; Madagascar; Marshall Islands; Nauru; Niger; Sao Tome and Principe; South Sudan; Sudan; Suriname; Tuvalu; Yemen | 100 | Australia; Egypt; Serbia; United Kingdom of Great Britain and Northern Ireland |
| AI Infrastructure | 16.63 | Burundi | 91.77 | United States of America |
| Governance | 1.39 | Marshall Islands | 94.57 | Ireland |
| Public Sector Adoption | 0 | Eritrea | 99.63 | Estonia |
| Development & Diffusion | 9.19 | Niger | 88.16 | United States of America |
| Resilience | 7.46 | Yemen | 90.01 | Denmark |
| Policy vision | 0 | Afghanistan; Belize; Bolivia (Plurinational State of); Chad; Comoros; Democratic People's Republic of Korea; Equatorial Guinea; Eritrea; Grenada; Kiribati; Madagascar; Marshall Islands; Nauru; Nicaragua; Niger; Sao Tome and Principe; Somalia; South Sudan; Sudan; Suriname; Tuvalu; Yemen | 100 | Australia; Belgium; Canada; Chile; China; Denmark; Egypt; France; Japan; Serbia; Singapore; United Kingdom of Great Britain and Northern Ireland; United States of America |
| Policy commitment | 0 | Afghanistan; Bahamas; Belarus; Bhutan; Bolivia (Plurinational State of); Chad; Congo; Democratic People's Republic of Korea; Dominica; El Salvador; Equatorial Guinea; Eritrea; Eswatini; Gabon; Grenada; Guinea; Guinea Bissau; Honduras; Kiribati; Kyrgyzstan; Liberia; Madagascar; Maldives; Mali; Marshall Islands; Monaco; Mozambique; Myanmar; Nauru; Niger; Palau; Paraguay; Saint Lucia; Samoa; Sao Tome and Principe; Seychelles; Solomon Islands; South Sudan; Sudan; Suriname; Syrian Arab Republic; Timor-Leste; Togo; Tonga; Tuvalu; Uganda; Yemen; Zimbabwe | 100 | Australia; Brazil; Egypt; Estonia; India; Israel; Kazakhstan; Netherlands; New Zealand; Norway; Poland; Republic of Korea; Romania; Saudi Arabia; Serbia; Slovenia; Spain; Sweden; Thailand; United Kingdom of Great Britain and Northern Ireland |
| Compute capacity | 0 | Antigua and Barbuda; Barbados; Belize; Benin; Burundi; Cabo Verde; Central African Republic; Chad; Comoros; Congo; Cuba; Democratic People's Republic of Korea; Dominica; Eritrea; Fiji; Gambia (Republic of The); Grenada; Haiti; Kiribati; Liberia; Marshall Islands; Mauritania; Micronesia (Federated States of); Montenegro; Nauru; Niger; Palau; Saint Kitts and Nevis; Saint Lucia; Saint Vincent and the Grenadines; Samoa; San Marino; Sao Tome and Principe; Sierra Leone; South Sudan; Syrian Arab Republic; Tajikistan; Timor-Leste; Tonga; Turkmenistan; Tuvalu; Vanuatu; Yemen | 90.92 | United States of America |
| Enabling technical infrastructure | 17.72 | Niger | 89.61 | United States of America |
| Data quality | 13.30 | Yemen | 96.55 | United Kingdom of Great Britain and Northern Ireland |
| Governance principles | 0 | Democratic People's Republic of Korea; Eritrea; Guinea Bissau | 100 | Belgium; China; Denmark; Estonia; France; Germany; Ireland; Israel; Italy; Netherlands; Norway; Poland; Portugal; Republic of Korea; Saudi Arabia; Switzerland; United Kingdom of Great Britain and Northern Ireland; Viet Nam |
| Regulatory compliance | 0 | Central African Republic; Guinea; Liberia; South Sudan | 92.25 | Ukraine |
| Government digital policy | 0 | Afghanistan; Barbados; Bolivia (Plurinational State of); Central African Republic; Côte D'Ivoire; Eritrea; Gabon; Guinea; Honduras; Malawi; Myanmar; Niger; South Sudan | 99.38 | Estonia |
| e-Government delivery | 0 | Eritrea | 99.98 | Denmark |
| Human capital | 6.18 | Samoa | 85.17 | Singapore |
| AI sector maturity | 0.58 | Venezuela, Bolivarian Republic of | 100 | United States of America |
| AI technology diffusion | 1.21 | Sierra Leone | 86.51 | Israel |
| Societal transition | 14.92 | Yemen | 90.67 | Finland |
| Safety and security | 0 | Antigua and Barbuda; Bahamas; Burundi; Central African Republic; Dominica; Eritrea; Grenada; Guinea Bissau; Liberia; Marshall Islands; Nauru; Nicaragua; Saint Lucia; State of Palestine; Yemen | 100 | Australia; China; Denmark; France; Japan; Kenya; Republic of Korea; Singapore; Spain; United Kingdom of Great Britain and Northern Ireland; United States of America |

## Interpretación recomendada por tipo de análisis

### Ranking de países

- Para listar los mejores países: ordenar por `Ranking` ascendente o `Total Score` descendente.
- Para listar los peores países: ordenar por `Ranking` descendente o `Total Score` ascendente.
- No calcular promedio de `Ranking`; usar promedio de `Total Score` o pilares.

### Comparación país-país

- Comparar `Total Score` para visión general.
- Comparar pilares para identificar fortalezas/debilidades macro.
- Comparar dimensiones para diagnóstico más específico.
- No afirmar causalidad: el Excel es un índice agregado, no una evaluación causal.

### Diagnóstico de un país

Orden sugerido:

1. Ubicación global: `Ranking` y `Total Score`.
2. Pilares por encima/debajo de su propio promedio o del promedio regional si se calcula externamente.
3. Dimensiones débiles: valores más bajos dentro del país.
4. Dimensiones fuertes: valores más altos dentro del país.
5. Advertir que el Excel no muestra los indicadores crudos, por lo tanto las causas específicas requieren metodología/fuentes externas.

### Análisis comunicacional

- `Policy Capacity` alto sirve para comunicar existencia de visión política, estrategia o compromiso estatal.
- `AI Infrastructure` bajo sirve para hablar de brechas materiales: compute, datos, conectividad, ciberseguridad, energía.
- `Public Sector Adoption` mide capacidad estatal digital y adopción de IA en gobierno; es útil para hablar de modernización del Estado.
- `Development & Diffusion` mide ecosistema, talento, investigación, empresas y adopción; es útil para hablar de competitividad, innovación e inversión.
- `Governance` y `Resilience` sirven para hablar de riesgos, reglas, seguridad, derechos y transición social.

## Errores comunes que debe evitar el LLM

1. **Decir que los puntajes son porcentajes absolutos.** Son scores normalizados 0-100.
2. **Usar la fila 1 como header.** La fila 1 solo agrupa visualmente pilares/dimensiones.
3. **No eliminar columnas D y K.** Son separadores vacíos.
4. **Promediar rankings.** Los rankings son ordinales; no deben promediarse.
5. **Confundir pilar con dimensión.** Hay 6 pilares y 14 dimensiones.
6. **Inferir indicadores crudos.** El Excel no contiene los 69 indicadores subyacentes.
7. **Asumir región o ingreso.** Esta hoja no trae región ni grupo de ingreso por país.
8. **Asumir ISO codes.** La hoja trae nombres de países, no códigos ISO.
9. **Interpretar empate en 0 como necesariamente 'cero absoluto'.** En algunos indicadores de escritorio, 0 puede significar ausencia de evidencia o no cumplimiento de criterio; en scores agregados, es resultado de normalización/agregación.
10. **Usar el PDF para reemplazar valores del Excel.** El PDF puede contener valores narrativos o rankings que no calzan exactamente con el Excel; para cálculos, usar el Excel.

## Esquema JSON recomendado para un registro país

```json
{
  "ranking": 1,
  "country": "United States of America",
  "total_score": 88.36,
  "pillars": {
    "policy_capacity": 92.5,
    "ai_infrastructure": 91.77,
    "governance": 82.5,
    "public_sector_adoption": 92.87,
    "development_diffusion": 88.16,
    "resilience": 78.28
  },
  "dimensions": {
    "policy_vision": 100,
    "policy_commitment": 87.5,
    "compute_capacity": 90.92,
    "enabling_technical_infrastructure": 89.61,
    "data_quality": 94.77,
    "governance_principles": 75,
    "regulatory_compliance": 90,
    "government_digital_policy": 87.9,
    "e_government_delivery": 97.84,
    "human_capital": 74.56,
    "ai_sector_maturity": 100,
    "ai_technology_diffusion": 85.96,
    "societal_transition": 56.55,
    "safety_security": 100
  }
}
```

**Nota:** el JSON anterior es un esquema de ejemplo. Para valores exactos, leer la fila del país correspondiente en el Excel.

## Pseudocódigo de limpieza

```python
# Leer hoja Dimensions-Pillars
# 1. Usar fila 2 como header.
# 2. Eliminar fila 1.
# 3. Eliminar columnas D y K o columnas con encabezado nulo.
# 4. Convertir todos los puntajes a float.
# 5. Mantener ranking como int y country como string.

score_columns = [
    "total_score",
    "policy_capacity",
    "ai_infrastructure",
    "governance",
    "public_sector_adoption",
    "development_diffusion",
    "resilience",
    "policy_vision",
    "policy_commitment",
    "compute_capacity",
    "enabling_technical_infrastructure",
    "data_quality",
    "governance_principles",
    "regulatory_compliance",
    "government_digital_policy",
    "e_government_delivery",
    "human_capital",
    "ai_sector_maturity",
    "ai_technology_diffusion",
    "societal_transition",
    "safety_security"
]
```

## Lista exacta de países en la hoja

La hoja usa los siguientes nombres de país exactamente como aparecen. Úsese esta lista para joins, filtros y normalización.

```text
Afghanistan
Albania
Algeria
Andorra
Angola
Antigua and Barbuda
Argentina
Armenia
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bhutan
Bolivia (Plurinational State of)
Bosnia and Herzegovina
Botswana
Brazil
Brunei Darussalam
Bulgaria
Burkina Faso
Burundi
Cabo Verde
Cambodia
Cameroon
Canada
Central African Republic
Chad
Chile
China
Colombia
Comoros
Congo
Costa Rica
Côte D'Ivoire
Croatia
Cuba
Cyprus
Czechia
Democratic People's Republic of Korea
Democratic Republic of the Congo
Denmark
Djibouti
Dominica
Dominican Republic
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Eswatini
Ethiopia
Fiji
Finland
France
Gabon
Gambia (Republic of The)
Georgia
Germany
Ghana
Greece
Grenada
Guatemala
Guinea
Guinea Bissau
Guyana
Haiti
Honduras
Hungary
Iceland
India
Indonesia
Iran (Islamic Republic of)
Iraq
Ireland
Israel
Italy
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kiribati
Kuwait
Kyrgyzstan
Lao People's Democratic Republic
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Mauritania
Mauritius
Mexico
Micronesia (Federated States of)
Monaco
Mongolia
Montenegro
Morocco
Mozambique
Myanmar
Namibia
Nauru
Nepal
Netherlands
New Zealand
Nicaragua
Niger
Nigeria
North Macedonia
Norway
Oman
Pakistan
Palau
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
Qatar
Republic of Korea
Republic of Moldova
Romania
Russian Federation
Rwanda
Saint Kitts and Nevis
Saint Lucia
Saint Vincent and the Grenadines
Samoa
San Marino
Sao Tome and Principe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Sudan
Spain
Sri Lanka
State of Palestine
Sudan
Suriname
Sweden
Switzerland
Syrian Arab Republic
Taiwan
Tajikistan
Thailand
Timor-Leste
Togo
Tonga
Trinidad and Tobago
Tunisia
Türkiye
Turkmenistan
Tuvalu
Uganda
Ukraine
United Arab Emirates
United Kingdom of Great Britain and Northern Ireland
United Republic of Tanzania
United States of America
Uruguay
Uzbekistan
Vanuatu
Venezuela, Bolivarian Republic of
Viet Nam
Yemen
Zambia
Zimbabwe
```

## Resumen ejecutivo para LLM

El Excel es una base comparativa de 195 países. La hoja `Dimensions-Pillars` tiene una fila por país y columnas para ranking, país, puntaje total, seis pilares y catorce dimensiones. Todas las columnas de puntaje son scores normalizados 0-100, ya agregados y ponderados. El archivo no incluye los 69 indicadores individuales ni sus fuentes, por lo que cualquier explicación causal de por qué un país obtuvo cierto puntaje debe presentarse como hipótesis o debe verificarse en la metodología/fuentes externas. Para análisis cuantitativo, usar el Excel como fuente de verdad.