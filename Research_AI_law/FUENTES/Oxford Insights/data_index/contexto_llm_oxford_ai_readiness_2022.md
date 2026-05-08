# Contexto LLM para trabajar con el Excel `2022-Government-AI-Readiness-Index-public-data.xlsx`

## Propósito de este archivo

Este `.md` está diseñado para ser entregado como contexto a un LLM que deba leer, limpiar, interpretar, analizar o explicar el Excel del **Government AI Readiness Index 2022** de Oxford Insights.

**ESTRUCTURA CASI IDÉNTICA A 2020-2021.** Este archivo documenta solo las diferencias con la edición 2021. Para la descripción completa del framework (3 pilares, 10 dimensiones, escala 0-100), reglas de lectura, y diccionario de variables, consultar `contexto_llm_oxford_ai_readiness_2020.md`.

## Único cambio estructural: `Size` → `Maturity`

| Dimensión | 2020-2021 | 2022 en adelante |
|-----------|-----------|-----------------|
| Columna J | Size | **Maturity** |

El resto de columnas, hojas y estructura son idénticas a 2020-2021.

## Diferencias con 2021

| Aspecto | 2021 | 2022 |
|---------|------|------|
| **Año del índice** | 2021 | 2022 |
| **Cantidad de países** | 160 | **181** (21 países más) |
| **Rango Overall score** | 17.93 a 88.16 | 13.46 a 85.72 |
| **País #1** | United States of America | United States of America |
| **País peor** | Yemen | Afghanistan |
| **Columnas** | Size | **Maturity** (renombrada) |
| **Estructura de hojas** | 2 hojas | Idéntico (nombres: `Global rankings`, `Detailed scores`) |
| **Header en Detailed scores** | Fila 2 (índice 1) | Idéntico |
| **Columnas separadoras** | D y H | Idéntico |
| **Innovation Capacity missing** | 2 | **0** (ningún missing) |
| **Data Representativeness missing** | 1 | **1** |

## Estructura del workbook

| Hoja | Filas × Cols | Header en fila |
|------|-------------|---------------|
| `Global rankings` | 181 × 3 | 1 (índice 0): `2022 Ranking`, `Country`, `Total` |
| `Detailed scores` | 183 × 17 | 2 (índice 1): `Country`, `Overall score`, `Government`, `Technology Sector`, `Data and Infrastructure`, `Vision`, `Governance and Ethics`, `Digital Capacity`, `Adaptability`, **`Maturity`**, `Innovation Capacity`, `Human Capital`, `Infrastructure`, `Data Availability`, `Data Representativeness` |

## Cambios en valores específicos respecto a 2021

| Variable | Rango 2021 | Rango 2022 | Cambio notable |
|---|---|---|---:|
| Overall score | 17.93 - 88.16 | 13.46 - 85.72 | -2.44 max |
| Government | 15.01 - 94.88 | 9.72 - 89.68 | -5.20 max |
| Technology Sector | 9.23 - 83.31 | 10.70 - 81.67 | -1.64 max |
| Data and Infrastructure | 20.03 - 92.71 | 11.53 - 94.17 | +1.46 max |
| Maturity (antes Size) | 2.36 - 87.04 | 2.51 - 84.74 | -2.30 max |

## Sobre el cambio `Size` → `Maturity`

El nombre cambia de `Size` a `Maturity`, pero la medición subyacente es esencialmente la misma: mide la madurez del sector tecnológico (unicornios, startups). El cambio de nombre refleja un refinamiento conceptual: ya no solo el "tamaño" sino también la "madurez" del ecosistema. En 2022, la dimensión sigue midiendo:

- Número de unicornios AI (log transformado)
- Número de unicornios no-AI (log transformado)
- Valor del comercio de servicios TIC per cápita (log transformado)
- Gasto en software informático

Los valores observados son similares a los de `Size` en 2021 (min 2.51, max 84.74).

## Notas específicas de 2022

1. **Aumento de cobertura:** 181 países vs 160 en 2021 (recupera países que 2021 había excluido).
2. **Maturity** reemplaza a `Size` como nombre de dimensión (columna J).
3. **Innovation Capacity** sin missing (recupera los 2 de 2021).
4. **Data Representativeness** mantiene 1 missing.
5. **Vision** sigue siendo ternaria (0, 50, 100), con 58 países en 100 y 108 en 0.

## Rangos observados completos con países extremos

| Variable | Min | País(es) min | Max | País(es) max |
|---|---|---|---:|---:|
| Overall score | 13.46 | Afghanistan | 85.72 | United States of America |
| Government | 9.72 | Haiti | 89.68 | Singapore |
| Technology Sector | 10.70 | Afghanistan | 81.67 | United States of America |
| Data and Infrastructure | 11.53 | Yemen | 94.17 | Singapore |
| Vision | 0 | Switzerland (y 107 más) | 100 | United States of America (y 57 más) |
| Governance and Ethics | 5.95 | Afghanistan | 89.22 | United States of America |
| Digital Capacity | 9.28 | Eritrea | 91.58 | Republic of Korea |
| Adaptability | 11.88 | Haiti | 83.18 | Singapore |
| Maturity | 2.51 | DR Congo | 84.74 | United States of America |
| Innovation Capacity | 0 | Maldives | 93.02 | United States of America |
| Human Capital | 5.70 | Afghanistan | 73.15 | Singapore |
| Infrastructure | 5.57 | Yemen | 92.28 | Singapore |
| Data Availability | 14.02 | South Sudan | 95.64 | Republic of Korea |
| Data Representativeness | 4.71 | Yemen | 99.50 | United States of America |

## Pseudocódigo de limpieza

```python
import pandas as pd

f = "2022-Government-AI-Readiness-Index-public-data.xlsx"
df = pd.read_excel(f, sheet_name="Detailed scores", header=1)
df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

column_map = {
    "Country": "country",
    "Overall score": "overall_score",
    "Government": "government",
    "Technology Sector": "technology_sector",
    "Data and Infrastructure": "data_infrastructure",
    "Vision": "vision",
    "Governance and Ethics": "governance_ethics",
    "Digital Capacity": "digital_capacity",
    "Adaptability": "adaptability",
    "Maturity": "maturity",  # ← NOTA: antes era "size"
    "Innovation Capacity": "innovation_capacity",
    "Human Capital": "human_capital",
    "Infrastructure": "infrastructure",
    "Data Availability": "data_availability",
    "Data Representativeness": "data_representativeness",
}
df = df.rename(columns=column_map)
```

## Resumen

2022 es estructuralmente idéntico a 2020-2021, con el único cambio de renombrar la dimensión `Size` a `Maturity`. La cobertura sube a 181 países. Para todo lo demás (framework, reglas de lectura, columnas separadoras), aplicar el contexto de 2020.
