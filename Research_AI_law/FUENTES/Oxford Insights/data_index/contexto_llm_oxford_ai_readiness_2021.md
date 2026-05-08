# Contexto LLM para trabajar con el Excel `2021-Government-AI-Readiness-Index-public-dataset.xlsx`

## Propósito de este archivo

Este `.md` está diseñado para ser entregado como contexto a un LLM que deba leer, limpiar, interpretar, analizar o explicar el Excel del **Government AI Readiness Index 2021** de Oxford Insights.

**ESTRUCTURA IDÉNTICA A 2020.** Este archivo documenta solo las diferencias con la edición 2020. Para la descripción completa del framework (3 pilares, 10 dimensiones, escala 0-100), reglas de lectura, y diccionario de variables, consultar `contexto_llm_oxford_ai_readiness_2020.md`.

## Diferencias con 2020

| Aspecto | 2020 | 2021 |
|---------|------|------|
| **Año del índice** | 2020 | 2021 |
| **Cantidad de países** | 172 | **160** (12 países menos) |
| **Rango Overall score** | 19.07 a 85.48 | 17.93 a **88.16** |
| **País #1** | United States of America | United States of America |
| **País #194 (peor)** | Yemen | Yemen |
| **Columnas** | Idénticas | Idénticas |
| **Estructura de hojas** | 2 hojas: Global ranking + Detailed scores | Idéntico |
| **Header en Detailed scores** | Fila 2 (índice 1) | Idéntico |
| **Columnas separadoras** | D y H | Idéntico |

## Estructura del workbook

Idéntica a 2020:

| Hoja | Filas × Cols | Header en fila |
|------|-------------|---------------|
| `Global ranking` | 160 × 3 | 1 (índice 0): `2021 Ranking`, `Country`, `Total` |
| `Detailed scores` | 162 × 17 | 2 (índice 1): igual que 2020 |

## Cambios en valores específicos

| Variable | Rango 2020 | Rango 2021 | Diferencia |
|---|---|---|---:|
| Overall score | 19.07 - 85.48 | 17.93 - 88.16 | +2.68 max, -1.14 min |
| Government | 9.95 - 93.83 | 15.01 - 94.88 | +1.05 max |
| Technology Sector | 15.03 - 77.55 | 9.23 - 83.31 | +5.76 max |
| Data and Infrastructure | 25.78 - 94.48 | 20.03 - 92.71 | -1.77 max |

## Variables con cambios

| Nombre | 2020 | 2021 |
|--------|------|------|
| Vision (max) | Argentina (100) | United States of America (100) |
| Vision (min) | Afghanistan (0) | Switzerland (0) |
| Vision unique | 3 valores (0, 50, 100) | Idéntico |
| Digital Capacity (max) | Singapore (93.82) | Singapore (91.77) |
| Innovation Capacity missing | 0 | **2** |
| Data Representativeness missing | 7 | **1** |

## Notas específicas de 2021

1. **Disminución de cobertura:** 160 países vs 172 en 2020 (12 países menos en la muestra).
2. **Innovation Capacity** tiene 2 missing (en 2020 tenía 0).
3. **Data Representativeness** tiene solo 1 missing (mejor que 7 en 2020).
4. **Vision** sigue siendo ternaria (0, 50, 100) con mayoría de países en 0.
5. USA sube su Overall score de 85.48 a 88.16.

## Pseudocódigo de limpieza

Idéntico a 2020, solo cambiar el nombre del archivo:

```python
import pandas as pd

f = "2021-Government-AI-Readiness-Index-public-dataset.xlsx"
df = pd.read_excel(f, sheet_name="Detailed scores", header=1)
df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

# Renombrar columnas (mismo mapping que 2020)
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
    "Size": "size",
    "Innovation Capacity": "innovation_capacity",
    "Human Capital": "human_capital",
    "Infrastructure": "infrastructure",
    "Data Availability": "data_availability",
    "Data Representativeness": "data_representativeness",
}
df = df.rename(columns=column_map)
```

## Rangos observados completos con países extremos

| Variable | Min | País(es) min | Max | País(es) max |
|---|---|---|---:|---:|
| Overall score | 17.93 | Yemen | 88.16 | United States of America |
| Government | 15.01 | Central African Republic | 94.88 | Singapore |
| Technology Sector | 9.23 | Afghanistan | 83.31 | United States of America |
| Data and Infrastructure | 20.03 | Yemen | 92.71 | United States of America |
| Vision | 0 | Switzerland (y 97 más) | 100 | United States of America (y 47 más) |
| Governance and Ethics | 1.73 | Afghanistan | 94.51 | United States of America |
| Digital Capacity | 15.02 | Yemen | 91.77 | Singapore |
| Adaptability | 18.31 | Venezuela | 93.98 | Singapore |
| Size | 2.36 | DR Congo | 87.04 | United States of America |
| Innovation Capacity | 14.01 | Haiti | 88.83 | Israel |
| Human Capital | 8.05 | Maldives | 77.48 | Switzerland |
| Infrastructure | 14.59 | Chad | 91.22 | United States of America |
| Data Availability | 22.74 | Angola | 97.16 | United Kingdom |
| Data Representativeness | 10.50 | Yemen | 96.54 | Belgium |

## Resumen

2021 es estructuralmente idéntico a 2020. Solo cambian los valores (scores y rankings) y la cobertura baja de 172 a 160 países. Usar el contexto de 2020 como referencia principal y este archivo para los valores específicos de 2021.
