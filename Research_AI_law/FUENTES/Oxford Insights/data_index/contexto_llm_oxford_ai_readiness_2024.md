# Contexto LLM para trabajar con el Excel `2024-GAIRI-data.xlsx`

## Propósito de este archivo

Este `.md` está diseñado para ser entregado como contexto a un LLM que deba leer, limpiar, interpretar, analizar o explicar el Excel del **Government AI Readiness Index 2024** (GAIRI 2024) de Oxford Insights.

**NOTA SOBRE EL NOMBRE DEL ARCHIVO:** Este es el primer año que usa el acrónimo **GAIRI** (Government AI Readiness Index) en el nombre del archivo, en vez del nombre largo. La estructura sigue siendo esencialmente la misma que 2022-2023 (3 pilares, 10 dimensiones), pero con dos diferencias importantes en el formato de la hoja de scores detallados.

## Fuentes utilizadas y jerarquía de confianza

1. **Fuente principal para datos numéricos:** Excel adjunto `2024-GAIRI-data.xlsx`.
2. **Fuente conceptual:** PDF adjunto `2024_government_ai_readiness_index.pdf`.
3. **Fuente web oficial:** página de Oxford Insights del Government AI Readiness Index 2024.

## Qué mide el índice

La edición 2024 evalúa **188 gobiernos/países**. Mantiene el marco de **3 pilares** (Government, Technology Sector, Data and Infrastructure) y **10 dimensiones** (con `Maturity`), en escala 0-100.

## Estructura del workbook

El archivo contiene **2 hojas** (como 2020-2022, sin la hoja de indicadores de 2023):

| Hoja | Filas × Cols | Qué contiene | Observaciones para LLM |
|------|------------:|---|------------------------|
| `Ranking` | 188 × 3 | Ranking, país y puntaje total 2024 | Header fila 1: `Rank`, `Country`, `2024 Total`. |
| `Scores per pillar and dimension` | 188 × 16 | País, Total, **Ranking**, 3 pilares, 10 dimensiones | **NUEVO:** incluye columna `Ranking` dentro de la hoja de scores. Fila 1 etiquetas visuales, fila 2 headers reales. |

## Diferencias clave con 2023

| Aspecto | 2023 | 2024 |
|---------|------|------|
| **Nombre del archivo** | `...Public-Indicator-Data.xlsx` | **`GAIRI-data.xlsx`** |
| **Nombres de hojas** | `Global rankings`, `Pillar & dimension scores`, `Indicator scores` | **`Ranking`**, **`Scores per pillar and dimension`** |
| **Columna Ranking en scores** | No | **Sí** (columna C en detailed scores) |
| **Hoja de indicadores** | Sí (40 indicadores) | **No** |
| **Países** | 193 | **188** |
| **Overall score range** | 9.20 - 84.80 | 14.62 - 87.03 |
| **País #1** | United States of America | United States of America |
| **Peor país** | Dem. People's Republic of Korea | Yemen |
| **Dimensiones** | 10 (con Maturity) | **10 (con Maturity)** — sin cambios |

## Reglas de lectura/importación

### Para `Scores per pillar and dimension`

- Usar la **fila 2** (índice 1) como header real.
- Ignorar la fila 1 para análisis tabular (etiquetas visuales: `Pillars`, `Dimensions`).
- Columnas separadoras: columna F (índice 6) — entre Data and Infrastructure y Vision.
- **NUEVO:** Ahora incluye `Ranking` como columna C, ANTES de los pilares.
- Columnas reales: `Country`, `Total`, `Ranking`, `Government`, `Technology Sector`, `Data and Infrastructure`, `Vision`, `Governance and Ethics`, `Digital Capacity`, `Adaptability`, `Maturity`, `Innovation Capacity`, `Human Capital`, `Infrastructure`, `Data Availability`, `Data Representativeness`.

### Para `Ranking`

- Usar la **fila 1** como header.
- Columnas: `Rank`, `Country`, `2024 Total`.
- 188 filas de datos.

## Naturaleza de los valores

- Misma escala 0-100 que 2020-2023.
- `Ranking` es entero ordinal (1-188, con 82 missing en la hoja detailed scores porque no todos los países tienen ranking, solo los primeros 106).
- **IMPORTANTE:** En la hoja `Scores per pillar and dimension`, la columna `Ranking` tiene 82 missing (solo 106 países rankeados). Esto es diferente al `Ranking` de la hoja `Ranking` que tiene 188 valores completos.

## Fórmula de agregación

Idéntica a 2020-2023:

```text
total_score = (Government + Technology Sector + Data and Infrastructure) / 3
```

## Jerarquía conceptual

Idéntica a 2022-2023:

| Pilar | Dimensiones |
|-------|------------|
| Government | Vision, Governance and Ethics, Digital Capacity, Adaptability |
| Technology Sector | Maturity, Innovation Capacity, Human Capital |
| Data and Infrastructure | Infrastructure, Data Availability, Data Representativeness |

## Diccionario completo de variables

| Columna Excel | Nombre canónico | Sección | Tipo | Rango teórico | Rango observado | Missing |
|:---:|---|---|---|---|---|---:|
| A | country | identificador | string | 188 valores | 188 valores | 0 |
| B | total | puntaje final | float | 0-100 | 14.62 a 87.03 | 0 |
| C | ranking | ranking | int/ordinal | 1-188 | 1 a 106 | **82** |
| D | government | pilar | float | 0-100 | 7.52 a 90.96 | 0 |
| E | technology_sector | pilar | float | 0-100 | 15.87 a 80.94 | 0 |
| F | data_infrastructure | pilar | float | 0-100 | 10.56 a 93.14 | 0 |
| G | vision | dimensión | float | 0-100 | 0 a 100 | 0 |
| H | governance_ethics | dimensión | float | 0-100 | 0.11 a 97.38 | 0 |
| I | digital_capacity | dimensión | float | 0-100 | 7.85 a 91.30 | 0 |
| J | adaptability | dimensión | float | 0-100 | 5.64 a 89.70 | 0 |
| K | maturity | dimensión | float | 0-100 | 0.77 a 83.80 | 0 |
| L | innovation_capacity | dimensión | float | 0-100 | 11.00 a 92.48 | 0 |
| M | human_capital | dimensión | float | 0-100 | 11.01 a 76.47 | 0 |
| N | infrastructure | dimensión | float | 0-100 | 7.22 a 88.38 | 0 |
| O | data_availability | dimensión | float | 0-100 | 15.14 a 98.32 | 0 |
| P | data_representativeness | dimensión | float | 0-100 | 5.00 a 100 | 0 |

### Detalle de cambios en variables respecto a 2023

| Variable | Cambio respecto a 2023 | Nota |
|----------|----------------------|------|
| Ranking (en detailed) | **NUEVO** | 82 missing. Solo 106 países tienen ranking aquí. |
| Total score | +2.23 max | Sube de 84.80 a 87.03 |
| Government | +0.56 max | Singapore sigue liderando (90.96) |
| Governance and Ethics | +4.70 max | Denmark lidera (97.38), no USA |
| Data Representativeness | Sin missing | En 2023 tenía 2 missing; en 2024 tiene 0 |
| Vision unique | 3 valores | Sigue siendo ternaria (0, 50, 100) |
| Maturity | -0.97 max | Baja de 84.77 a 83.80 |

## Rangos observados completos con países extremos

| Variable | Min | País(es) min | Max | País(es) max |
|---|---|---|---:|---:|
| Total | 14.62 | Yemen | 87.03 | United States of America |
| Ranking | 1 | United States of America | 106 | Barbados |
| Government | 7.52 | Haiti | 90.96 | Singapore |
| Technology Sector | 15.87 | Angola | 80.94 | United States of America |
| Data and Infrastructure | 10.56 | Yemen | 93.14 | Singapore |
| Vision | 0 | Switzerland | 100 | United States of America |
| Governance and Ethics | 0.11 | Eritrea | 97.38 | Denmark |
| Digital Capacity | 7.85 | Eritrea | 91.30 | United Arab Emirates |
| Adaptability | 5.64 | Yemen | 89.70 | Singapore |
| Maturity | 0.77 | DR Congo | 83.80 | United States of America |
| Innovation Capacity | 11.00 | Maldives | 92.48 | United States of America |
| Human Capital | 11.01 | Afghanistan | 76.47 | Singapore |
| Infrastructure | 7.22 | Afghanistan | 88.38 | United States of America |
| Data Availability | 15.14 | Yemen | 98.32 | Republic of Korea |
| Data Representativeness | 5.00 | Syrian Arab Republic | 100 | United Kingdom |

## Columnas vacías / separadores visuales

En `Scores per pillar and dimension`:

| Columna Excel | Contenido | Acción |
|:---:|---|---|
| F (índice 6) | Separador entre Data and Infrastructure y Vision | Eliminar (aparece como `Unnamed`) |

## Errores comunes que debe evitar el LLM

1. **No notar la columna Ranking en detailed scores.** Es nueva en 2024 y tiene 82 missing. No confundir con la hoja `Ranking` que tiene ranking completo.
2. **Usar la fila 1 como header.** Sigue siendo solo etiquetas visuales.
3. **No eliminar la columna separadora** (columna F en Excel).
4. **Buscar una hoja de indicadores.** En 2024 no existe. Solo 2023 tiene `Indicator scores`.
5. **Asumir que todos los países tienen ranking en detailed scores.** Solo 106 de 188 tienen valor.
6. **Comparar indicadores a nivel de detalle con 2023.** No hay datos de indicadores en 2024.

## Pseudocódigo de limpieza

```python
import pandas as pd

f = "2024-GAIRI-data.xlsx"

# Scores per pillar and dimension
df = pd.read_excel(f, sheet_name="Scores per pillar and dimension", header=1)
df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

column_map = {
    "Country": "country",
    "Total": "total",
    "Ranking": "ranking",
    "Government": "government",
    "Technology Sector": "technology_sector",
    "Data and Infrastructure": "data_infrastructure",
    "Vision": "vision",
    "Governance and Ethics": "governance_ethics",
    "Digital Capacity": "digital_capacity",
    "Adaptability": "adaptability",
    "Maturity": "maturity",
    "Innovation Capacity": "innovation_capacity",
    "Human Capital": "human_capital",
    "Infrastructure": "infrastructure",
    "Data Availability": "data_availability",
    "Data Representativeness": "data_representativeness",
}
df = df.rename(columns=column_map)

# Ranking column: 82 missing values (only top 106 countries have ranking here)
df["ranking"] = pd.to_numeric(df["ranking"], errors="coerce")
```

## Resumen

2024 es estructuralmente similar a 2022-2023 (3 pilares, 10 dimensiones, escala 0-100), con dos diferencias principales: (1) incluye columna `Ranking` dentro de la hoja de scores detallados (con 82 missing), y (2) no incluye la hoja de indicadores individuales que sí tenía 2023. La cobertura es de 188 países. Es la última edición antes del rediseño mayor de 2025 (6 pilares, 14 dimensiones).
