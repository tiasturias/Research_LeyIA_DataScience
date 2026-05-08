# Contexto LLM para trabajar con el Excel `2023-Government-AI-Readiness-Index-Public-Indicator-Data.xlsx`

## Propósito de este archivo

Este `.md` está diseñado para ser entregado como contexto a un LLM que deba leer, limpiar, interpretar, analizar o explicar el Excel del **Government AI Readiness Index 2023** de Oxford Insights.

**ARCHIVO MÁS COMPLETO DE LA SERIE 2020-2024.** A diferencia de 2020-2022, este Excel incluye una tercera hoja (`Indicator scores`) con los **40 indicadores crudos** que alimentan el índice, con sus fuentes documentadas. Las hojas de rankings y scores agregados mantienen la misma estructura que 2022.

## Fuentes utilizadas y jerarquía de confianza

1. **Fuente principal para datos numéricos:** Excel adjunto `2023-Government-AI-Readiness-Index-Public-Indicator-Data.xlsx`.
2. **Fuente conceptual:** PDF adjunto `2023_government_ai_readiness_index.pdf`.
3. **Fuente web oficial:** página de Oxford Insights del Government AI Readiness Index 2023.

**Regla para el LLM:** si hay diferencias entre el PDF narrativo y los valores del Excel, usar el **Excel** como fuente de verdad para análisis numérico.

## Qué mide el índice

La edición 2023 evalúa **193 gobiernos/países**. El marco usa **40 indicadores** agrupados en **10 dimensiones** y **3 pilares**, con puntajes normalizados en escala 0-100. Es el mismo framework de 2022 (3 pilares, 10 dimensiones, con `Maturity` en vez de `Size`).

## Estructura del workbook

El archivo contiene **3 hojas** (único año con datos de indicadores):

| Hoja | Filas × Cols | Qué contiene | Observaciones para LLM |
|------|------------:|---|------------------------|
| `Global rankings` | 193 × 3 | Ranking, país y puntaje total | Header fila 1: `2023 Ranking`, `Country`, `Total`. 193 países. |
| `Pillar & dimension scores` | 195 × 17 | País, Total score, 3 pilares, 10 dimensiones | Misma estructura que 2022. Fila 1 etiquetas visuales, fila 2 headers reales. Columnas D y H son separadores. |
| **`Indicator scores`** | **198 × 40** | **40 indicadores crudos por país** | **HOJA NUEVA.** 3 filas de encabezado (Pillar, Dimension, Indicator) + 1 fila de fuentes (Source). Col 0 = Country. Columnas 1-39 = indicadores. |

## Reglas de lectura/importación

### Para `Pillar & dimension scores`

Idéntico a 2022: usar fila 2 (índice 1) como header real, ignorar fila 1, eliminar columnas sin nombre.

### Para `Indicator scores` (HOJA NUEVA - CRÍTICA)

- **Fila 1** (índice 0): Pillar headers — identifica a qué pilar pertenece cada grupo de columnas.
- **Fila 2** (índice 1): Dimension headers — identifica a qué dimensión pertenece cada grupo de columnas.
- **Fila 3** (índice 2): Indicator names — **usar como nombres de variables**.
- **Fila 4** (índice 3): Source — fuente de cada indicador.
- **Filas 5-197** (índices 4-196): Datos de 193 países. Col 0 = Country, Cols 1-39 = indicadores.
- NO hay columnas separadoras vacías entre indicadores.
- Algunos indicadores tienen valores faltantes (entre 1 y 14 missing dependiendo del indicador).
- Los valores de los indicadores están NORMALIZADOS en escala 0-100 (a diferencia de 2019 que tenía crudos + normalizados separados).

## Naturaleza de los valores

- Todos los scores en `Pillar & dimension scores` y `Global rankings`: escala **0-100**, scores normalizados y agregados.
- Todos los indicadores en `Indicator scores`: escala **0-100**, son los valores normalizados de cada indicador crudo.
- El Excel no contiene los valores crudos originales (ej. número real de GPUs, cantidad exacta de startups), solo sus transformaciones normalizadas 0-100.
- La columna `Source` indica la fuente original de cada indicador.

## Fórmula de agregación

Misma que 2020-2022:

```text
overall_score = (Government + Technology Sector + Data and Infrastructure) / 3
```

Cada pilar es el promedio simple de sus dimensiones. Cada dimensión es el promedio simple de sus indicadores constituyentes.

## Jerarquía conceptual completa (3 pilares, 10 dimensiones, 40 indicadores)

### Pilar: Government

| Dimensión | Indicadores (normalizados 0-100) |
|-----------|--------------------------------|
| **Vision** | AI strategy |
| **Governance & Ethics** | Data protection and privacy laws, Cybersecurity, Regulatory quality, Ethical principles, Accountability |
| **Digital Capacity** | Online services, Foundational IT infrastructure, Government Promotion of Investment in Emerging Technologies |
| **Adaptability** | Government Effectiveness, Government responsiveness to change, Procurement Data |

### Pilar: Technology Sector

| Dimensión | Indicadores (normalizados 0-100) |
|-----------|--------------------------------|
| **Maturity** | Number of AI Unicorns (log), Number of non-AI Unicorns (log), Value of trade in ICT services per capita (log), Value of trade in ICT goods per capita (log), Computer software spending |
| **Innovation Capacity** | Time spent dealing with government regulations, VC availability, R&D Spending (log), Company investment in emerging technology, AI research papers (log) |
| **Human Capital** | Graduates in STEM or computer science, Github Activity (log), Female STEM Graduates, Quality of Engineering and Technology Higher Ed, ICT skills |

### Pilar: Data & Infrastructure

| Dimensión | Indicadores (normalizados 0-100) |
|-----------|--------------------------------|
| **Infrastructure** | Telecommunications Infrastructure, Supercomputers (log), Broadband Quality, 5G Infrastructure, Adoption of Emerging Technologies |
| **Data Availability** | Open Data, Data governance, Mobile-cellular telephone subscriptions, Households with internet access, Statistical Capacity |
| **Data Representativeness** | Cost of cheapest internet-enabled device (% of monthly GDP per capita), Gender gap in internet access |

## Diccionario completo de variables

### Hoja `Pillar & dimension scores`

Idéntica a 2022. Ver `contexto_llm_oxford_ai_readiness_2022.md` para el diccionario completo.

Columnas: `Country`, `Total score`, `Government`, `Technology Sector`, `Data and Infrastructure`, `Vision`, `Governance and Ethics`, `Digital Capacity`, `Adaptability`, `Maturity`, `Innovation Capacity`, `Human Capital`, `Infrastructure`, `Data Availability`, `Data Representativeness`.

### Hoja `Indicator scores`: diccionario de los 40 indicadores

#### Government > Vision

##### `AI strategy` (columna 1)

- **Nombre canónico:** `ind_ai_strategy`
- **Dimensión:** Vision
- **Pilar:** Government
- **Escala:** 0-100 (ternario: 0, 50, 100)
- **Rango observado:** 0 a 100
- **Valores únicos:** 3
- **Missing:** 1
- **Fuente:** desk research
- **Qué mide:** Existencia y madurez de estrategia nacional de IA (0 = no tiene, 50 = en desarrollo, 100 = publicada/implementada).
- **Peor país:** Angola (0)
- **Mejor país:** Azerbaijan (100)

#### Government > Governance & Ethics

##### `Data protection and privacy laws` (columna 2)

- **Nombre canónico:** `ind_data_protection_laws`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Valores únicos:** 8
- **Missing:** 2
- **Fuente:** UN data protection and privacy legislation worldwide
- **Qué mide:** Existencia y cobertura de leyes de protección de datos.

##### `Cybersecurity` (columna 3)

- **Nombre canónico:** `ind_cybersecurity`
- **Escala:** 0-100
- **Rango observado:** 1.35 a 100
- **Missing:** 1
- **Fuente:** Global Cybersecurity Index

##### `Regulatory quality` (columna 4)

- **Nombre canónico:** `ind_regulatory_quality`
- **Escala:** 0-100
- **Rango observado:** 2.20 a 94.20
- **Missing:** 1
- **Fuente:** WGI Indicators

##### `Ethical principles` (columna 5)

- **Nombre canónico:** `ind_ethical_principles`
- **Escala:** 0-100 (ternario)
- **Rango observado:** 0 a 100
- **Valores únicos:** 3
- **Missing:** 1
- **Fuente:** desk research
- **Qué mide:** Existencia de principios éticos para IA (0 = no, 50 = en desarrollo, 100 = sí).

##### `Accountability` (columna 6)

- **Nombre canónico:** `ind_accountability`
- **Escala:** 0-100
- **Rango observado:** 9.60 a 85.40
- **Missing:** 1
- **Fuente:** WGI Indicators

#### Government > Digital Capacity

##### `Online services` (columna 7)

- **Nombre canónico:** `ind_online_services`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Missing:** 1
- **Fuente:** UN E-gov Online Services Index
- **Mejor país:** Finland (100)

##### `Foundational IT infrastructure` (columna 8)

- **Nombre canónico:** `ind_foundational_it`
- **Escala:** 0-100
- **Rango observado:** 0.30 a 99.00
- **Missing:** 1
- **Fuente:** Govtech Maturity Index

##### `Government Promotion of Investment in Emerging Technologies` (columna 9)

- **Nombre canónico:** `ind_govt_promotion_emerging_tech`
- **Escala:** 0-100
- **Rango observado:** 0.05 a 100
- **Missing:** 10
- **Fuente:** Network Readiness Index

#### Government > Adaptability

##### `Government Effectiveness` (columna 10)

- **Nombre canónico:** `ind_govt_effectiveness`
- **Escala:** 0-100
- **Rango observado:** 2.20 a 92.80
- **Missing:** 1
- **Fuente:** WGI Indicators

##### `Government responsiveness to change` (columna 11)

- **Nombre canónico:** `ind_govt_responsiveness`
- **Escala:** 0-100
- **Rango observado:** 7.20 a 85.22
- **Missing:** 7
- **Fuente:** Global Competitiveness Index

##### `Procurement Data` (columna 12)

- **Nombre canónico:** `ind_procurement_data`
- **Escala:** 0-100
- **Rango observado:** 0 a 96.00
- **Missing:** 7
- **Fuente:** Procurement page for the index

#### Technology Sector > Maturity

##### `Number of AI Unicorns log transformation` (columna 13)

- **Nombre canónico:** `ind_ai_unicorns_log`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Valores únicos:** 7
- **Missing:** 1
- **Fuente:** CB Insights

##### `Number of non-AI Unicorns log transformation` (columna 14)

- **Nombre canónico:** `ind_non_ai_unicorns_log`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Valores únicos:** 17
- **Missing:** 1
- **Fuente:** CB Insights

##### `Value of trade in ICT services (per capita) log transformation` (columna 15)

- **Nombre canónico:** `ind_ict_trade_services_log`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Missing:** 2
- **Fuente:** UNCTAD

##### `Value of trade in ICT goods (per capita) log transformation` (columna 16)

- **Nombre canónico:** `ind_ict_trade_goods_log`
- **Escala:** 0-100
- **Rango observado:** 8.63 a 100
- **Missing:** 2
- **Fuente:** UNCTAD

##### `Computer software spending` (columna 17)

- **Nombre canónico:** `ind_software_spending`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Missing:** 10
- **Fuente:** Global Innovation Index

#### Technology Sector > Innovation Capacity

##### `Time spent dealing with government regulations` (columna 18)

- **Nombre canónico:** `ind_time_govt_regulations`
- **Escala:** 0-100
- **Rango observado:** 71.20 a 99.90
- **Missing:** 14
- **Fuente:** World Bank

##### `VC availability` (columna 19)

- **Nombre canónico:** `ind_vc_availability`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Valores únicos:** 52
- **Missing:** 14
- **Fuente:** Global Innovation Index

##### `R&D Spending log transformation` (columna 20)

- **Nombre canónico:** `ind_rd_spending_log`
- **Escala:** 0-100
- **Rango observado:** 0.55 a 100
- **Missing:** 4
- **Fuente:** UNESCO

##### `Company investment in emerging technology` (columna 21)

- **Nombre canónico:** `ind_company_investment_emerging_tech`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Missing:** 10
- **Fuente:** Network Readiness Index

##### `AI research papers log transformation` (columna 22)

- **Nombre canónico:** `ind_ai_research_papers_log`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Missing:** 1
- **Fuente:** Scimago

#### Technology Sector > Human Capital

##### `Graduates in STEM or computer science` (columna 23)

- **Nombre canónico:** `ind_stem_graduates`
- **Escala:** 0-100
- **Rango observado:** 1.68 a 100
- **Missing:** 1
- **Fuente:** UNESCO

##### `Github Activity log transformation` (columna 24)

- **Nombre canónico:** `ind_github_activity_log`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Missing:** 1
- **Fuente:** Github 2021 Octoverse report

##### `Female STEM Graduates` (columna 25)

- **Nombre canónico:** `ind_female_stem_graduates`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Missing:** 4
- **Fuente:** World Bank

##### `Quality of Engineering and Technology Higher Ed` (columna 26)

- **Nombre canónico:** `ind_eng_tech_higher_ed_quality`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Valores únicos:** 53
- **Missing:** 1
- **Fuente:** QS University Rankings (Engineering & Technology)

##### `ICT skills` (columna 27)

- **Nombre canónico:** `ind_ict_skills`
- **Escala:** 0-100
- **Rango observado:** 2.66 a 100
- **Missing:** 13
- **Fuente:** ITU

#### Data & Infrastructure > Infrastructure

##### `Telecommunications Infrastructure` (columna 28)

- **Nombre canónico:** `ind_telecom_infrastructure`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Missing:** 1
- **Fuente:** UN E-gov Telecommunications Infrastructure Index

##### `Supercomputers log transformation` (columna 29)

- **Nombre canónico:** `ind_supercomputers_log`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Valores únicos:** 17
- **Missing:** 1
- **Fuente:** Top 500 supercomputers

##### `Broadband Quality` (columna 30)

- **Nombre canónico:** `ind_broadband_quality`
- **Escala:** 0-100
- **Rango observado:** 18.40 a 85.30
- **Missing:** 10
- **Fuente:** EIU Inclusive Internet Index

##### `5G Infrastructure` (columna 31)

- **Nombre canónico:** `ind_5g_infrastructure`
- **Escala:** 0-100 (binario)
- **Rango observado:** 0 a 100
- **Valores únicos:** 2
- **Missing:** 1
- **Fuente:** Ookla 5G Map

##### `Adoption of Emerging Technologies` (columna 32)

- **Nombre canónico:** `ind_adoption_emerging_tech`
- **Escala:** 0-100
- **Rango observado:** 0 a 100
- **Missing:** 10
- **Fuente:** Network Readiness Index

#### Data & Infrastructure > Data Availability

##### `Open Data` (columna 33)

- **Nombre canónico:** `ind_open_data`
- **Escala:** 0-100
- **Rango observado:** 0 a 90.00
- **Valores únicos:** 34
- **Missing:** 7
- **Fuente:** Global Data Barometer

##### `Data governance` (columna 34)

- **Nombre canónico:** `ind_data_governance`
- **Escala:** 0-100 (ternario)
- **Rango observado:** 0 a 100
- **Valores únicos:** 3
- **Missing:** 1
- **Fuente:** Govtech Maturity Index

##### `Mobile-cellular telephone subscriptions` (columna 35)

- **Nombre canónico:** `ind_mobile_subscriptions`
- **Escala:** 0-100
- **Rango observado:** 15.15 a 100
- **Missing:** 1
- **Fuente:** ITU

##### `Households with internet access` (columna 36)

- **Nombre canónico:** `ind_households_internet`
- **Escala:** 0-100
- **Rango observado:** 1.92 a 100
- **Missing:** 2
- **Fuente:** ITU

##### `Statistical Capacity` (columna 37)

- **Nombre canónico:** `ind_statistical_capacity`
- **Escala:** 0-100
- **Rango observado:** 19.62 a 90.09
- **Missing:** 2
- **Fuente:** SPI Github repo

#### Data & Infrastructure > Data Representativeness

##### `Cost of cheapest internet-enabled device (% of monthly GDP per capita)` (columna 38)

- **Nombre canónico:** `ind_cost_internet_device`
- **Escala:** 0-100 (invertido: 100 = más barato/mejor)
- **Rango observado:** 0 a 100
- **Missing:** 3
- **Fuente:** GSMA Mobile Connectivity Index

##### `Gender gap in internet access` (columna 39)

- **Nombre canónico:** `ind_gender_gap_internet`
- **Escala:** 0-100 (100 = sin brecha)
- **Rango observado:** 72.00 a 100
- **Missing:** 10
- **Fuente:** EIU Inclusive Internet Index

## Rangos observados: Hoja `Pillar & dimension scores`

| Variable | Min | País(es) min | Max | País(es) max |
|---|---|---|---:|---:|
| Total score | 9.20 | Dem. People's Republic of Korea | 84.80 | United States of America |
| Government | 8.03 | Dem. People's Republic of Korea | 90.40 | Singapore |
| Technology Sector | 14.27 | Dem. People's Republic of Korea | 81.02 | United States of America |
| Data and Infrastructure | 5.29 | Dem. People's Republic of Korea | 89.32 | Singapore |
| Vision | 0 | Afghanistan (y 113 más) | 100 | Argentina (y 64 más) |
| Governance and Ethics | 3.29 | Dem. People's Republic of Korea | 92.68 | Finland |
| Digital Capacity | 8.05 | Dem. People's Republic of Korea | 91.57 | Republic of Korea |
| Adaptability | 11.60 | Haiti | 82.17 | Singapore |
| Maturity | 0 | Dem. People's Republic of Korea | 84.77 | United States of America |
| Innovation Capacity | 5.21 | Seychelles | 89.81 | Israel |
| Human Capital | 6.84 | Afghanistan | 72.38 | United Arab Emirates |
| Infrastructure | 1.69 | Dem. People's Republic of Korea | 88.34 | United States of America |
| Data Availability | 8.88 | Dem. People's Republic of Korea | 95.65 | Republic of Korea |
| Data Representativeness | 1.37 | Syrian Arab Republic | 99.65 | Qatar |

## Rangos observados: Hoja `Indicator scores`

(Tabla resumen de los 40 indicadores. Para detalles completos, ver diccionario arriba.)

| Indicador | Min | Max | Missing |
|-----------|---:|---:|---:|
| AI strategy | 0 | 100 | 1 |
| Data protection laws | 0 | 100 | 2 |
| Cybersecurity | 1.35 | 100 | 1 |
| Regulatory quality | 2.20 | 94.20 | 1 |
| Ethical principles | 0 | 100 | 1 |
| Accountability | 9.60 | 85.40 | 1 |
| Online services | 0 | 100 | 1 |
| Foundational IT | 0.30 | 99.00 | 1 |
| Govt promotion emerging tech | 0.05 | 100 | 10 |
| Govt effectiveness | 2.20 | 92.80 | 1 |
| Govt responsiveness | 7.20 | 85.22 | 7 |
| Procurement Data | 0 | 96.00 | 7 |
| AI Unicorns (log) | 0 | 100 | 1 |
| Non-AI Unicorns (log) | 0 | 100 | 1 |
| ICT trade services (log) | 0 | 100 | 2 |
| ICT trade goods (log) | 8.63 | 100 | 2 |
| Software spending | 0 | 100 | 10 |
| Time govt regulations | 71.20 | 99.90 | 14 |
| VC availability | 0 | 100 | 14 |
| R&D Spending (log) | 0.55 | 100 | 4 |
| Company investment emerging tech | 0 | 100 | 10 |
| AI research papers (log) | 0 | 100 | 1 |
| STEM graduates | 1.68 | 100 | 1 |
| Github activity (log) | 0 | 100 | 1 |
| Female STEM graduates | 0 | 100 | 4 |
| Eng/Tech higher ed quality | 0 | 100 | 1 |
| ICT skills | 2.66 | 100 | 13 |
| Telecom infrastructure | 0 | 100 | 1 |
| Supercomputers (log) | 0 | 100 | 1 |
| Broadband quality | 18.40 | 85.30 | 10 |
| 5G infrastructure | 0 | 100 | 1 |
| Adoption emerging tech | 0 | 100 | 10 |
| Open Data | 0 | 90.00 | 7 |
| Data governance | 0 | 100 | 1 |
| Mobile subscriptions | 15.15 | 100 | 1 |
| Households internet | 1.92 | 100 | 2 |
| Statistical capacity | 19.62 | 90.09 | 2 |
| Cost internet device | 0 | 100 | 3 |
| Gender gap internet | 72.00 | 100 | 10 |

## Columnas vacías / separadores visuales

En `Pillar & dimension scores`: mismas columnas separadoras que 2020-2022 (columnas D y H, que aparecen como `Unnamed`).

En `Indicator scores`: **no hay** columnas separadoras. Todas las columnas 1-39 contienen datos de indicadores.

## Errores comunes que debe evitar el LLM

1. **No usar las 3 filas de encabezado de Indicator scores correctamente.** Pillar está en fila 1, Dimension en fila 2, Indicator en fila 3, Source en fila 4. Usar SOLO la fila 3 como nombres de columna.
2. **Tratar los indicadores como valores crudos originales.** Ya están normalizados 0-100.
3. **Ignorar la hoja Indicator scores.** Es la única edición (2023) que tiene datos de indicadores individuales.
4. **No documentar los missing values.** Varios indicadores tienen entre 1 y 14 missing. Esto es normal y debe informarse.
5. **Promediar indicadores de distintas dimensiones sin tener en cuenta los pesos.** La agregación a dimensión es promedio simple; de dimensión a pilar es promedio simple; de pilar a total es promedio simple.
6. **Interpretar 0 como "no hay información".** En algunos indicadores (ej. AI Unicorns, 5G), 0 es un valor válido que significa "no tiene".
7. **Confundir con la estructura de 2019.** 2023 usa escala 0-100 y 3 pilares, no 0-10 y 4 clusters.

## Pseudocódigo de limpieza

```python
import pandas as pd

f = "2023-Government-AI-Readiness-Index-Public-Indicator-Data.xlsx"

# --- Pillar & dimension scores ---
df_pillars = pd.read_excel(f, sheet_name="Pillar & dimension scores", header=1)
df_pillars = df_pillars.loc[:, ~df_pillars.columns.str.contains("^Unnamed", na=False)]
df_pillars = df_pillars.rename(columns={
    "Country": "country",
    "Total score": "total_score",
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
})

# --- Indicator scores ---
df_raw = pd.read_excel(f, sheet_name="Indicator scores", header=None)

# Fila 3 (índice 2) tiene los nombres de indicadores
indicators = df_raw.iloc[2, 1:40].tolist()  # Cols 1-39
source_row = df_raw.iloc[3, 1:40].tolist()

# Datos: filas 4 en adelante
df_indicators = df_raw.iloc[4:].copy()
df_indicators.columns = ["country"] + indicators

# Convertir a numérico
for col in df_indicators.columns:
    if col != "country":
        df_indicators[col] = pd.to_numeric(df_indicators[col], errors="coerce")
```

## Resumen

2023 es el año más valioso para análisis detallado porque incluye los **40 indicadores individuales** en la hoja `Indicator scores`. Mantiene el mismo framework de 3 pilares y 10 dimensiones de 2022 (con `Maturity`). Es la única edición de la serie 2020-2024 que permite descomposición completa del índice hasta el nivel de indicador individual. La cobertura es de 193 países.
