# Contexto LLM para trabajar con el Excel `2020-Government-AI-Readiness-Index-public-dataset.xlsx`

## Propósito de este archivo

Este `.md` está diseñado para ser entregado como contexto a un LLM que deba leer, limpiar, interpretar, analizar o explicar el Excel del **Government AI Readiness Index 2020** de Oxford Insights. El foco principal es la hoja **`Detailed scores`**, que contiene el puntaje total, los tres pilares y las diez dimensiones por país.

**NOTA:** 2020 establece el framework que se mantendrá (con cambios menores) hasta 2024: 3 pilares (Government, Technology Sector, Data and Infrastructure) y 10 dimensiones, en escala 0-100.

## Fuentes utilizadas y jerarquía de confianza

1. **Fuente principal para datos numéricos:** Excel adjunto `2020-Government-AI-Readiness-Index-public-dataset.xlsx`.
2. **Fuente conceptual:** PDF adjunto `2020_government_ai_readiness_index.pdf`.
3. **Fuente web oficial:** página de Oxford Insights del Government AI Readiness Index 2020.

**Regla para el LLM:** si hay diferencias entre el PDF narrativo y los valores del Excel, usar el **Excel** como fuente de verdad para análisis numérico.

## Qué mide el índice

El índice busca responder: **¿hasta qué punto puede un gobierno aprovechar la IA para beneficiar al público?**

La edición 2020 evalúa **172 gobiernos/países**. El marco usa indicadores agregados en 3 pilares y 10 dimensiones, con puntajes normalizados en escala 0-100.

## Estructura del workbook

El archivo contiene 2 hojas:

| Hoja | Rango usado | Qué contiene | Observaciones para LLM |
|------|---:|---|---|
| `Global ranking` | 172 filas × 3 cols | Ranking, país y puntaje total | Fila 1 es header: `2020 Ranking`, `Country`, `Score`. Sin filas de metadato adicional. |
| `Detailed scores` | 174 filas × 17 cols | País, Overall score, 3 pilares, 10 dimensiones | Fila 1 tiene etiquetas visuales de grupo ("Pillars", "Dimensions"). Fila 2 son encabezados reales. Columnas D (índice 3) y H (índice 7) son separadores vacíos. |

## Reglas de lectura/importación

### Para `Detailed scores`

- Usar la **fila 2** (0-indexed: fila 1) como header real.
- Ignorar la fila 1 para análisis tabular; solo tiene etiquetas visuales: `Pillars` y `Dimensions`.
- Ignorar/eliminar columnas separadoras: columnas D (índice 3) y H (índice 7) en el Excel, que corresponden a columnas sin nombre.
- Las columnas reales son: `Country`, `Overall score`, `Government`, `Technology Sector`, `Data and Infrastructure`, `Vision`, `Governance and Ethics`, `Digital Capacity`, `Adaptability`, `Size`, `Innovation Capacity`, `Human Capital`, `Infrastructure`, `Data Availability`, `Data Representativeness`.
- 172 filas de datos (países).
- No hay valores faltantes en la mayoría de las columnas (excepto `Data Representativeness` con 7 missing).

### Para `Global ranking`

- Usar la **fila 1** como header.
- Columnas: `2020 Ranking`, `Country`, `Score`.
- 172 filas de datos, sin missing.
- Hoja redundante con `Detailed scores`; no agrega información analítica adicional.

## Naturaleza de los valores

- `2020 Ranking` es entero ordinal: 1 = mejor posición.
- `Country` es texto/categoría.
- Todos los puntajes (`Overall score`, pilares y dimensiones) son numéricos continuos normalizados en escala **0-100**.
- Los puntajes NO deben interpretarse como porcentajes literales de cumplimiento.
- El Excel no contiene fórmulas; contiene valores estáticos ya calculados.

## Fórmula de agregación

El `Overall score` es el promedio simple de los 3 pilares:

```text
overall_score = (Government + Technology Sector + Data and Infrastructure) / 3
```

Los pilares, a su vez, se componen de dimensiones (promedios simples dentro de cada pilar).

## Jerarquía conceptual

| Pilar | Dimensiones que lo componen |
|-------|---------------------------|
| Government | Vision, Governance and Ethics, Digital Capacity, Adaptability |
| Technology Sector | Size, Innovation Capacity, Human Capital |
| Data and Infrastructure | Infrastructure, Data Availability, Data Representativeness |

### Pilar: Government

Mide la capacidad del gobierno para diseñar e implementar políticas públicas de IA.

| Dimensión | Interpretación breve |
|-----------|---------------------|
| Vision | Existencia de estrategia nacional de IA y visión de futuro |
| Governance and Ethics | Marco de gobernanza: principios, protección de datos, ciberseguridad |
| Digital Capacity | Capacidad digital del gobierno: servicios online, infraestructura TIC |
| Adaptability | Capacidad del gobierno de adaptarse al cambio tecnológico |

### Pilar: Technology Sector

Mide la madurez del sector tecnológico y la capacidad de innovación del país.

| Dimensión | Interpretación breve |
|-----------|---------------------|
| Size | Tamaño del sector tecnológico (unicornios, startups) |
| Innovation Capacity | Capacidad de innovación: I+D, VC, investigación |
| Human Capital | Talento disponible: STEM, habilidades técnicas |

### Pilar: Data and Infrastructure

Mide la disponibilidad y calidad de datos e infraestructura técnica.

| Dimensión | Interpretación breve |
|-----------|---------------------|
| Infrastructure | Infraestructura digital: telecomunicaciones, cómputo, conectividad |
| Data Availability | Disponibilidad de datos abiertos y gobernanza de datos |
| Data Representativeness | Representatividad de datos: brecha de género, acceso, cobertura |

## Diccionario completo de variables

| Columna Excel | Variable original | Nombre canónico | Sección | Tipo | Rango teórico | Rango observado | Missing |
|:---:|---|---|---|---|---|---:|---:|
| A | Country | country | identificador | string | 172 valores únicos | 172 valores únicos | 0 |
| B | Overall score | overall_score | puntaje final | float | 0-100 | 19.07 a 85.48 | 0 |
| C | Government | government | pilar | float | 0-100 | 9.95 a 93.83 | 0 |
| D | Technology Sector | technology_sector | pilar | float | 0-100 | 15.03 a 77.55 | 0 |
| E | Data and Infrastructure | data_infrastructure | pilar | float | 0-100 | 25.78 a 94.48 | 0 |
| F | Vision | vision | dimensión | float | 0-100 | 0 a 100 | 0 |
| G | Governance and Ethics | governance_ethics | dimensión | float | 0-100 | 0.93 a 92.66 | 0 |
| H | Digital Capacity | digital_capacity | dimensión | float | 0-100 | 14.45 a 93.82 | 0 |
| I | Adaptability | adaptability | dimensión | float | 0-100 | 12.80 a 89.91 | 0 |
| J | Size | size | dimensión | float | 0-100 | 0.70 a 81.65 | 0 |
| K | Innovation Capacity | innovation_capacity | dimensión | float | 0-100 | 17.24 a 87.10 | 0 |
| L | Human Capital | human_capital | dimensión | float | 0-100 | 5.72 a 80.39 | 0 |
| M | Infrastructure | infrastructure | dimensión | float | 0-100 | 12.25 a 93.77 | 0 |
| N | Data Availability | data_availability | dimensión | float | 0-100 | 25.83 a 98.70 | 0 |
| O | Data Representativeness | data_representativeness | dimensión | float | 0-100 | 29.40 a 98.00 | 7 |

### Detalle por variable

#### `Overall score` (columna B)

- **Qué mide:** Puntaje final de preparación gubernamental para IA. Promedio de los 3 pilares.
- **Rango observado:** 19.07 a 85.48
- **Mejor país:** United States of America (85.48)
- **Peor país:** Yemen (19.07)
- **Nota:** No tratar como porcentaje literal. Es un score comparativo 0-100.

#### `Government` (columna C)

- **Qué mide:** Pilar Government: capacidad gubernamental para IA.
- **Rango observado:** 9.95 a 93.83
- **Mejor país:** Singapore (93.83)
- **Peor país:** Venezuela (9.95)

#### `Technology Sector` (columna D)

- **Qué mide:** Pilar Technology Sector: madurez del ecosistema tecnológico.
- **Rango observado:** 15.03 a 77.55
- **Mejor país:** United States of America (77.55)
- **Peor país:** Mozambique (15.03)

#### `Data and Infrastructure` (columna E)

- **Qué mide:** Pilar Data and Infrastructure: datos e infraestructura.
- **Rango observado:** 25.78 a 94.48
- **Mejor país:** United Kingdom (94.48)
- **Peor país:** Yemen (25.78)

#### `Vision` (columna F)

- **Qué mide:** Existencia de estrategia nacional de IA y visión.
- **Rango observado:** 0 a 100
- **Valores únicos:** 3 (0, 50, 100)
- **Mejor país (100):** Argentina (y 33 más empatados en 100)
- **Peor país (0):** Afghanistan (y 118 más empatados en 0)
- **Nota:** Variable con pocos valores discretos (ternaria).

#### `Governance and Ethics` (columna G)

- **Qué mide:** Marco de gobernanza: principios, protección de datos, ciberseguridad.
- **Rango observado:** 0.93 a 92.66
- **Mejor país:** United States of America (92.66)
- **Peor país:** Kiribati (0.93)

#### `Digital Capacity` (columna H)

- **Qué mide:** Capacidad digital del gobierno (servicios online, infraestructura TIC).
- **Rango observado:** 14.45 a 93.82
- **Mejor país:** Singapore (93.82)
- **Peor país:** Venezuela (14.45)

#### `Adaptability` (columna I)

- **Qué mide:** Capacidad de adaptación del gobierno al cambio tecnológico.
- **Rango observado:** 12.80 a 89.91
- **Mejor país:** Singapore (89.91)
- **Peor país:** Venezuela (12.80)

#### `Size` (columna J)

- **Qué mide:** Tamaño del sector tecnológico (unicornios, startups).
- **Rango observado:** 0.70 a 81.65
- **Mejor país:** United States of America (81.65)
- **Peor país:** Tanzania (0.70)

#### `Innovation Capacity` (columna K)

- **Qué mide:** Capacidad de innovación: I+D, VC, investigación.
- **Rango observado:** 17.24 a 87.10
- **Mejor país:** Israel (87.10)
- **Peor país:** Yemen (17.24)

#### `Human Capital` (columna L)

- **Qué mide:** Talento disponible: STEM, habilidades técnicas.
- **Rango observado:** 5.72 a 80.39
- **Mejor país:** Singapore (80.39)
- **Peor país:** Vanuatu (5.72)

#### `Infrastructure` (columna M)

- **Qué mide:** Infraestructura digital: telecomunicaciones, cómputo.
- **Rango observado:** 12.25 a 93.77
- **Mejor país:** Sweden (93.77)
- **Peor país:** Haiti (12.25)

#### `Data Availability` (columna N)

- **Qué mide:** Disponibilidad de datos abiertos y gobernanza de datos.
- **Rango observado:** 25.83 a 98.70
- **Mejor país:** United Kingdom (98.70)
- **Peor país:** Democratic Republic of the Congo (25.83)

#### `Data Representativeness` (columna O)

- **Qué mide:** Representatividad de datos: brecha de género, acceso, cobertura.
- **Rango observado:** 29.40 a 98.00
- **Mejor país:** Norway (98.00)
- **Peor país:** Syrian Arab Republic (29.40)
- **Missing:** 7 países sin dato
- **Nota:** Única variable con valores faltantes en 2020.

## Columnas vacías / separadores visuales

En la hoja `Detailed scores`:

| Columna Excel | Naturaleza | Acción |
|:---:|---|---|
| D (después de Overall score) | Separador vacío | Eliminar |
| H (después de Data and Infrastructure) | Separador vacío | Eliminar |

En la práctica, pandas las leerá como columnas `Unnamed`.

## Rangos observados completos con países extremos

| Variable | Min | País(es) min | Max | País(es) max |
|---|---|---|---:|---:|
| Overall score | 19.07 | Yemen | 85.48 | United States of America |
| Government | 9.95 | Venezuela | 93.83 | Singapore |
| Technology Sector | 15.03 | Mozambique | 77.55 | United States of America |
| Data and Infrastructure | 25.78 | Yemen | 94.48 | United Kingdom |
| Vision | 0 | Afghanistan (y 118 más) | 100 | Argentina (y 33 más) |
| Governance and Ethics | 0.93 | Kiribati | 92.66 | United States of America |
| Digital Capacity | 14.45 | Venezuela | 93.82 | Singapore |
| Adaptability | 12.80 | Venezuela | 89.91 | Singapore |
| Size | 0.70 | Tanzania | 81.65 | United States of America |
| Innovation Capacity | 17.24 | Yemen | 87.10 | Israel |
| Human Capital | 5.72 | Vanuatu | 80.39 | Singapore |
| Infrastructure | 12.25 | Haiti | 93.77 | Sweden |
| Data Availability | 25.83 | DR Congo | 98.70 | United Kingdom |
| Data Representativeness | 29.40 | Syrian Arab Republic | 98.00 | Norway |

## Errores comunes que debe evitar el LLM

1. **Decir que los puntajes son porcentajes absolutos.** Son scores normalizados 0-100, comparativos.
2. **Usar la fila 1 como header.** La fila 1 solo agrupa visualmente pilares/dimensiones.
3. **No eliminar columnas separadoras vacías** (columnas D y H en detailed scores).
4. **Promediar rankings.** Los rankings son ordinales; usar Overall score para promedios.
5. **Confundir pilar con dimensión.** Hay 3 pilares y 10 dimensiones.
6. **Comparar puntajes con 2019.** El marco de 2020 (escala 0-100, 3 pilares) NO es comparable con 2019 (escala 0-10, 4 clusters).
7. **Asumir ISO codes o región.** La hoja solo trae nombres de países.
8. **Inferir indicadores crudos.** El Excel contiene scores ya agregados, no los indicadores subyacentes.
9. **Usar el PDF para reemplazar valores del Excel.** Para cálculos, usar el Excel.

## Pseudocódigo de limpieza (hoja `Detailed scores`)

```python
import pandas as pd

f = "2020-Government-AI-Readiness-Index-public-dataset.xlsx"

# Leer con fila 2 (0-indexed: 1) como header
df = pd.read_excel(f, sheet_name="Detailed scores", header=1)

# Eliminar columnas sin nombre (separadores visuales)
df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]

# Renombrar a snake_case si se desea
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

# Verificar tipos
for col in df.columns:
    if col != "country":
        df[col] = pd.to_numeric(df[col], errors="coerce")
```

## Lista exacta de países (172)

La hoja contiene 172 países. Para la lista completa, leer las filas de datos del Excel.

## Resumen ejecutivo para LLM

El Excel 2020 es el primer año del framework de 3 pilares y 10 dimensiones en escala 0-100. Su estructura es simple: 2 hojas, con `Detailed scores` como hoja principal (15 columnas: país, score total, 3 pilares, 10 dimensiones). El puntaje total es el promedio simple de los 3 pilares. No contiene indicadores crudos. Es el punto de partida de la serie 2020-2024, que comparte la misma estructura básica con cambios menores en años posteriores.
