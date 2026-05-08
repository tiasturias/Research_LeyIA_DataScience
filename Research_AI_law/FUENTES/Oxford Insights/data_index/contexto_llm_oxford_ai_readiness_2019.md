# Contexto LLM para trabajar con el Excel `SHARED_-2019-Index-data-for-report.xlsx`

## Propósito de este archivo

Este `.md` está diseñado para ser entregado como contexto a un LLM que deba leer, limpiar, interpretar, analizar o explicar el Excel del **Government AI Readiness Index 2019** (edición 2018/19) de Oxford Insights. El foco principal es la hoja **`Data`**, porque contiene los indicadores crudos, los puntajes normalizados y el índice agregado por país.

**ADVERTENCIA CRÍTICA:** La edición 2019 es **estructuralmente diferente** a las ediciones 2020-2025. Usa una escala 0-10 (no 0-100), 4 clusters temáticos (no pilares), indicadores en escalas heterogéneas, y un formato de regional groupings en la hoja Rankings. NO debe analizarse con el mismo código/herramientas que las ediciones posteriores.

## Fuentes utilizadas y jerarquía de confianza

1. **Fuente principal para datos numéricos:** Excel adjunto `SHARED_-2019-Index-data-for-report.xlsx`.
2. **Fuente conceptual:** PDF adjunto `2019_government_ai_readiness_index.pdf`, especialmente introducción, metodología y rankings completos.
3. **Fuente web oficial:** página de Oxford Insights del Government AI Readiness Index 2019.

**Regla para el LLM:** si hay diferencias entre el PDF narrativo y los valores del Excel, usar el **Excel** como fuente de verdad para análisis numérico.

## Qué mide el índice (edición 2018/19)

El índice busca responder: **¿hasta qué punto pueden los gobiernos aprovechar la IA para beneficiar al público?**

La edición 2018/19 evalúa **194 gobiernos/países** usando un marco de **4 clusters** y **12 indicadores**. El Excel contiene tanto los valores crudos de los indicadores como versiones normalizadas (0-1), promedios por cluster y un índice general en escala 0-10.

## Estructura del workbook

El archivo contiene 2 hojas:

| Hoja | Filas | Columnas usadas | Qué contiene | Observaciones para LLM |
|------|-----:|---:|---|---|
| `Rankings` | 198 | 31 | Ranking global y rankings regionales lado a lado | Cada bloque de 3 columnas es una región: Rank, Country, Score. La fila 1 son etiquetas regionales; fila 2 son encabezados reales. |
| `Data` | 201 | 33 | Indicadores crudos, normalizados, promedios por cluster e índice | 3 filas de encabezado (Cluster, Indicator, Source), fila "Max Score", luego 194 filas de países. |

## Reglas de lectura/importación

### Para `Rankings`

- La fila 1 contiene etiquetas regionales (Asia-Pacific, Africa, etc.) como headers de grupo.
- La fila 2 contiene encabezados reales: `Rank (of 194)`, `Country`, `Score` para cada región.
- Las filas 3 a 197 contienen datos (194 países con rankings regionales).
- Cada bloque de 3 columnas (Rank, Country, Score) es una región diferente.
- Columna A-C: Ranking global. Columna D-F: Asia-Pacific, etc.
- **Advertencia:** Un país aparece en su región correspondiente, NO necesariamente en todas las columnas.

### Para `Data`

| Fila índice | Contenido | Acción |
|-------------|-----------|--------|
| 0 | Cluster labels (Governance, Infrastructure and data, etc.) | Ignorar para análisis tabular |
| 1 | Indicator names (Privacy laws, AI strategy, etc.) | Usar como nombres de variables |
| 2 | Source (fuente de cada indicador) | Usar como metadato, no como dato |
| 3-4 | Vacías | Ignorar |
| 5 | "Max Score" (valores máximos posibles) | Usar como referencia de escala, no como dato |
| 6 | Vacía | Ignorar |
| 7-200 | Datos de 194 países | Datos reales. Col 0 = Country, Cols 1-12 = indicadores crudos, Cols 14-24 = normalizados, Col 26 = INDEX SCORE |

## Naturaleza de los valores (CRÍTICO para 2019)

### Escala del índice general

- El **INDEX SCORE** (columna 26) y los **puntajes en Rankings** están en escala **0-10** (NO 0-100 como 2020-2025).
- Un puntaje 9.19 no significa "91.9%", es un valor en escala 0-10.

### Indicadores crudos (columnas 1-12)

Cada indicador crudo tiene su propia escala original:

| Indicador | Escala original | Tipo |
|-----------|----------------|------|
| Privacy laws | 0 o 1 | Binario |
| AI strategy | 0, 1 o 2 | Ordinal (0=none, 1=forthcoming, 2=yes) |
| Data availability | 1-100 | Continuo |
| Gov't procurement | ~1.6-7 | Continuo (subíndice WEF) |
| Data capability (in govt) | 0-1 | Continuo (UN e-gov index) |
| Technology skills | 2.2-7 | Continuo (WEF) |
| AI startups | 0-5053 | Conteo (sesgo fuerte) |
| Log of AI startups | 0-3.7 | Log-transformado |
| Innovation capability | 16.8-100 | Continuo (WEF) |
| Digital public services | 0-1 | Continuo (UN) |
| Effectiveness of government | 16.21-100 | Continuo (World Bank) |
| Importance of ICTs to govt vision | 2.3-7 | Continuo (WEF) |

### Indicadores normalizados (columnas 14-24)

Son transformaciones de los indicadores crudos a escala **0-1** (teóricamente), aunque algunas columnas tienen rangos 0-0.9 o similares. Los valores 0 pueden significar "no cumple criterio" o "no hay evidencia".

### Promedios por cluster (columnas 29-32)

Son los promedios simple de los indicadores normalizados dentro de cada cluster, en escala **0-1**.

| Columna | Cluster | Indicadores que incluye |
|---------|---------|------------------------|
| 29 | Average: Governance | Privacy laws + AI strategy |
| 30 | Average: Infrastructure and data | Data availability + Gov't procurement + Data capability |
| 31 | Average: Skills and education | Technology skills + Log of AI startups + Innovation capability |
| 32 | Average: Government and public services | Digital public services + Effectiveness of government + Importance of ICTs |

## Fórmula de agregación

El INDEX SCORE (0-10) se calcula como:

```text
index_score = sum(cluster_averages) * 2.5
```

Donde `cluster_averages` es la suma de los 4 promedios de cluster (cada uno en escala 0-1).

Cada promedio de cluster es el promedio simple de los indicadores normalizados de ese cluster.

La multiplicación por 2.5 lleva la suma (máximo teórico 4.0) a la escala 0-10.

## Jerarquía conceptual (4 clusters, 12 indicadores)

| Cluster | Indicadores incluidos | Interpretación breve |
|---------|----------------------|---------------------|
| Governance | Privacy laws, AI strategy | Marco normativo y estratégico para IA: leyes de protección de datos y existencia de estrategia nacional de IA |
| Infrastructure and data | Data availability, Gov't procurement of advanced tech, Data capability (in govt) | Disponibilidad de datos abiertos, capacidad estatal de comprar tecnología avanzada, y capacidad de datos en el gobierno |
| Skills and education | Technology skills, Log of AI startups, (Private sector) innovation capability | Talento técnico, ecosistema emprendedor IA, y capacidad de innovación del sector privado |
| Government and public services | Digital public services, Effectiveness of government, Importance of ICTs to govt vision | Madurez de servicios públicos digitales, efectividad gubernamental, y visión TIC del gobierno |

## Diccionario completo de variables

### Columnas de la hoja `Data`

#### Identificadores y puntaje final

| Columna | Nombre original | Nombre canónico | Sección | Tipo | Rango teórico | Rango observado | Missing |
|:---:|---|---|---|---|---|---:|---:|
| 0 | (país) | country | identificador | string | 194 valores únicos | 194 valores únicos | 0 |
| 26 | INDEX SCORE | index_score | puntaje final | float continuo | 0-10 | 0.17 a 9.19 | 0 |

#### Cluster: Governance (indicadores crudos)

##### `Privacy laws (yes = 1, no = 0)` — Columna 1

- **Nombre canónico:** `privacy_laws`
- **Tipo:** binario (0/1)
- **Cluster:** Governance
- **Rango observado:** 0 a 1
- **Valores únicos:** 2
- **Missing:** 0
- **Qué mide:** Si el país cuenta con legislación de protección de datos y privacidad (1 = sí, 0 = no).
- **Fuente original:** UN data protection and privacy legislation
- **Notas para LLM:** Es un indicador binario. Un valor de 1 es "mejor". No mide calidad de la ley, solo existencia.
- **País(es) en mínimo (0):** (países sin ley de privacidad — en 2019, aún no había GDPR fuera de Europa)

##### `AI strategy` — Columna 2

- **Nombre canónico:** `ai_strategy`
- **Tipo:** ordinal (0/1/2)
- **Cluster:** Governance
- **Rango observado:** 0 a 2
- **Valores únicos:** 3
- **Missing:** 0
- **Qué mide:** 0 = no tiene estrategia IA, 1 = estrategia próxima ("forthcoming"), 2 = tiene estrategia IA.
- **Fuente original:** Medium article (desk research Oxford Insights)
- **Notas para LLM:** No mide calidad o implementación de la estrategia, solo su existencia o anuncio.
- **País(es) en mínimo (0):** países sin estrategia IA conocida
- **País(es) en máximo (2):** países con estrategia IA publicada

#### Cluster: Infrastructure and data (indicadores crudos)

##### `Data availability` — Columna 3

- **Nombre canónico:** `data_availability`
- **Tipo:** float continuo
- **Cluster:** Infrastructure and data
- **Rango teórico:** 1-100
- **Rango observado:** 1 a 100
- **Valores únicos:** 55
- **Missing:** 0
- **Qué mide:** Disponibilidad de datos abiertos según OKFN Open Data Index.
- **Fuente original:** OKFN Open Data Index 2016/2017

##### `Gov't procurement of advanced technology products` — Columna 4

- **Nombre canónico:** `govt_procurement_advanced_tech`
- **Tipo:** float continuo
- **Cluster:** Infrastructure and data
- **Rango observado:** 1.63 a 7.00
- **Valores únicos:** 139
- **Fuente original:** Subindicator in WEF Networked Readiness Index 2016

##### `Data capability (in govt)` — Columna 5

- **Nombre canónico:** `data_capability_govt`
- **Tipo:** float continuo
- **Cluster:** Infrastructure and data
- **Rango observado:** 0.06 a 1.00
- **Valores únicos:** 191
- **Fuente original:** UN e-government index 2018

#### Cluster: Skills and education (indicadores crudos)

##### `Technology skills` — Columna 6

- **Nombre canónico:** `technology_skills`
- **Tipo:** float continuo
- **Cluster:** Skills and education
- **Rango observado:** 2.2 a 7.0
- **Valores únicos:** 33
- **Fuente original:** Subindicator in WEF Global Competitiveness Report 2018

##### `AI startups` — Columna 7

- **Nombre canónico:** `ai_startups`
- **Tipo:** entero (conteo)
- **Cluster:** Skills and education
- **Rango observado:** 0 a 5053
- **Valores únicos:** 50
- **Fuente original:** Crunchbase
- **Notas para LLM:** Distribución muy sesgada. USA (5053) domina. La mayoría de países tiene 0 o valores muy bajos. Existe también `Log of AI startups` (col 8) como transformación logarítmica.

##### `Log of AI startups` — Columna 8

- **Nombre canónico:** `log_ai_startups`
- **Tipo:** float continuo
- **Cluster:** Skills and education
- **Rango observado:** 0 a 3.70
- **Valores únicos:** 49
- **Notas para LLM:** Transformación logarítmica de AI startups. 0 puede significar 0 startups o log(1)=0.

##### `(Private sector) innovation capability` — Columna 9

- **Nombre canónico:** `innovation_capability`
- **Tipo:** float continuo
- **Cluster:** Skills and education
- **Rango observado:** 16.8 a 100.0
- **Valores únicos:** 123
- **Fuente original:** Subindicator in WEF Global Competitiveness Report 2018

#### Cluster: Government and public services (indicadores crudos)

##### `Digital public services` — Columna 10

- **Nombre canónico:** `digital_public_services`
- **Tipo:** float continuo
- **Cluster:** Government and public services
- **Rango observado:** 0 a 1.00
- **Valores únicos:** 101
- **Fuente original:** UN online service index from UN eGovernment Survey

##### `Effectiveness of government` — Columna 11

- **Nombre canónico:** `govt_effectiveness`
- **Tipo:** float continuo
- **Cluster:** Government and public services
- **Rango observado:** 16.21 a 100.0
- **Valores únicos:** 124
- **Fuente original:** World Bank 2017 Government Effectiveness

##### `Importance of ICTs to government vision of the future` — Columna 12

- **Nombre canónico:** `ict_govt_vision`
- **Tipo:** float continuo
- **Cluster:** Government and public services
- **Rango observado:** 2.31 a 7.00
- **Valores únicos:** 139
- **Fuente original:** Subindicator in WEF Networked Readiness Index 2016

### Indicadores normalizados (columnas 14-24)

Son versiones normalizadas a escala 0-1 de los indicadores crudos. Siguen la misma agrupación por cluster:

| Columna | Indicador normalizado | Rango observado | Indicador crudo origen |
|:---:|---|---|---|
| 14 | NORMALISED: Privacy laws | 0 a 1 | Col 1 |
| 15 | NORMALISED: AI strategy | 0 a 1 | Col 2 |
| 16 | NORMALISED: Data availability | 0 a 0.90 | Col 3 |
| 17 | NORMALISED: Gov't procurement | 0 a 0.81 | Col 4 |
| 18 | NORMALISED: Data capability (in govt) | 0 a 0.92 | Col 5 |
| 19 | NORMALISED: Technology skills | 0 a 0.83 | Col 6 |
| 20 | NORMALISED: Log of AI startups | 0 a 1 | Col 8 |
| 21 | NORMALISED: Innovation capability | 0 a 0.88 | Col 9 |
| 22 | NORMALISED: Digital public services | 0 a 1 | Col 10 |
| 23 | NORMALISED: Govt effectiveness | 0 a 1 | Col 11 |
| 24 | NORMALISED: ICT govt vision | 0 a 0.87 | Col 12 |

### Promedios por cluster (columnas 29-32, escala 0-1)

| Columna | Nombre | Cluster | Rango observado |
|:---:|---|---|---:|
| 29 | Average: Governance | Governance | 0 a 1.00 |
| 30 | Average: Infrastructure and data | Infrastructure and data | 0.02 a 0.75 |
| 31 | Average: Skills and education | Skills and education | 0 a 0.90 |
| 32 | Average: Government and public services | Government and public services | 0 a 0.94 |

### Columna INDEX SCORE (columna 26)

- **Nombre canónico:** `index_score`
- **Tipo:** float continuo
- **Escala:** 0-10
- **Rango observado:** 0.17 a 9.19
- **Valores únicos:** 193
- **Missing:** 0
- **Mejor país:** Singapore (9.19)
- **Peor país:** Somalia (0.17)
- **Fórmula:** `sum(cluster_averages) * 2.5`
- **Nota para LLM:** NO dividir por 10 y tratar como porcentaje. La escala es 0-10, no 0-100.

## Columnas vacías / separadores visuales

| Columna | Contenido | Acción |
|:---:|---|---|
| 13 | Vacía entre raw y normalised | Ignorar/eliminar |
| 25 | Vacía entre normalised e INDEX SCORE | Ignorar/eliminar |
| 27 | Vacía entre INDEX SCORE y averages | Ignorar/eliminar |
| 28 | "Sum of cluster averages" | Solo metadato; no usar para análisis |

## Rangos observados completos con países extremos

| Variable global | Min | País(es) min | Max | País(es) max |
|---|---|---|---:|---:|
| INDEX SCORE | 0.17 | Somalia | 9.19 | Singapore |
| Governance avg | 0 | (varios) | 1.00 | Singapore, UK, Germany, USA, Finland... |
| Infrastructure avg | 0.02 | (varios) | 0.75 | Singapore, UK, USA, Netherlands... |
| Skills avg | 0 | (varios) | 0.90 | USA |
| Govt & public services avg | 0 | (varios) | 0.94 | UK |

## Errores comunes que debe evitar el LLM

1. **Tratar el INDEX SCORE como escala 0-100.** Es escala 0-10. Multiplicar por 10 es INCORRECTO para comparar con años posteriores; el marco cambió completamente.
2. **Usar el mismo código de limpieza que para 2020-2025.** La estructura de hojas, headers y columnas es completamente diferente.
3. **Confundir indicadores crudos con normalizados.** Ambos están presentes. Los crudos tienen escalas heterogéneas.
4. **No eliminar filas de encabezado.** Las filas 0-6 no son datos de país (Cluster, Indicator, Source, Max Score).
5. **Promediar rankings.** Los rankings son ordinales.
6. **Comparar puntajes 2019 con 2020+ directamente.** No son comparables: escala (0-10 vs 0-100), marco (4 clusters vs 3 pilares/6 pilares) y metodología cambiaron.
7. **Usar la hoja Rankings sin entender su estructura multi-región.** Cada columna pertenece a una región diferente.
8. **Interpretar 0 en AI startups como "no hay datos".** Puede ser 0 real (no hay startups) o dato faltante.
9. **Usar el PDF para reemplazar valores del Excel.** Para cálculos, usar el Excel como fuente de verdad.

## Pseudocódigo de limpieza (hoja `Data`)

```python
import pandas as pd

# Leer hoja Data
f = "SHARED_-2019-Index-data-for-report.xlsx"
df = pd.read_excel(f, sheet_name="Data", header=None)

# 1. Filas 0-2 son encabezados; filas 3-4 vacías; fila 5 Max Score; fila 6 vacía
#    Datos reales: filas 7 a 200 (índice 7:200)
data = df.iloc[7:].copy()

# 2. Columna 0 = Country
#    Columnas 1-12 = raw indicators
#    Columnas 14-24 = normalised indicators  
#    Columna 26 = INDEX SCORE
#    Columnas 29-32 = cluster averages

# 3. Renombrar columnas
column_names = {
    0: "country",
    1: "privacy_laws",
    2: "ai_strategy",
    3: "data_availability",
    4: "govt_procurement_advanced_tech",
    5: "data_capability_govt",
    6: "technology_skills",
    7: "ai_startups",
    8: "log_ai_startups",
    9: "innovation_capability",
    10: "digital_public_services",
    11: "govt_effectiveness",
    12: "ict_govt_vision",
    14: "norm_privacy_laws",
    15: "norm_ai_strategy",
    16: "norm_data_availability",
    17: "norm_govt_procurement",
    18: "norm_data_capability",
    19: "norm_technology_skills",
    20: "norm_log_ai_startups",
    21: "norm_innovation_capability",
    22: "norm_digital_public_services",
    23: "norm_govt_effectiveness",
    24: "norm_ict_govt_vision",
    26: "index_score",
    29: "avg_governance",
    30: "avg_infrastructure_data",
    31: "avg_skills_education",
    32: "avg_govt_public_services",
}

# Seleccionar solo las columnas relevantes
use_cols = list(column_names.keys())
data = data[use_cols]
data.columns = [column_names[c] for c in use_cols]

# 4. Convertir a tipos numéricos
for col in data.columns:
    if col != "country":
        data[col] = pd.to_numeric(data[col], errors="coerce")

# 5. Limpiar nombres de país (eliminar " (the)" al final si existe)
data["country"] = data["country"].str.replace(r"\s*\(the\)$", "", regex=True).str.strip()
```

## Lista exacta de países (194)

```
Singapore
United Kingdom of Great Britain and Northern Ireland
Germany
United States of America
Finland
Sweden
Canada
France
Denmark
Japan
Australia
Norway
New Zealand
Netherlands
Italy
Austria
India
Switzerland
United Arab Emirates
China
Israel
Malaysia
Estonia
Belgium
Luxembourg
Republic of Korea
Poland
Iceland
Russian Federation
Portugal
Czech Republic
Mexico
Latvia
Ireland
Uruguay
Spain
Lithuania
Slovenia
Chile
Brazil
Taiwan
Qatar
Malta
Colombia
Slovakia
Turkey
Bulgaria
Hungary
Greece
Philippines
Argentina
Kenya
Cyprus
Tunisia
Romania
Thailand
Indonesia
Serbia
Oman
Mauritius
North Macedonia
Croatia
Ukraine
Azerbaijan
Kazakhstan
Costa Rica
Montenegro
South Africa
Panama
Viet Nam
Peru
Iran
Trinidad and Tobago
Jordan
Ghana
Georgia
Dominican Republic
Saudi Arabia
Kuwait
Morocco
Armenia
Ecuador
Albania
Pakistan
El Salvador
Republic of Moldova
Jamaica
Nepal
Bolivia
Seychelles
Uganda
Zambia
Senegal
Tanzania
Bosnia and Herzegovina
Honduras
Kyrgyzstan
Tajikistan
Rwanda
Bahrain
Cabo Verde
Paraguay
Bangladesh
Côte d'Ivoire
Sri Lanka
Benin
Nigeria
Gambia
Mali
Zimbabwe
Egypt
Lebanon
Namibia
Malawi
Guatemala
Bhutan
Nicaragua
Lesotho
Cameroon
Botswana
Brunei Darussalam
Belarus
Mongolia
Burkina Faso
Cambodia
Ethiopia
Mozambique
Chad
Angola
Liechtenstein
Madagascar
Gabon
Bahamas
Venezuela
Monaco
Barbados
Lao People's Democratic Republic
Liberia
Andorra
Guinea
Algeria
Saint Kitts and Nevis
Dominica
Antigua and Barbuda
Guyana
San Marino
Niger
Burundi
Saint Vincent and the Grenadines
Haiti
Mauritania
Yemen
Saint Lucia
Eswatini
Suriname
Iraq
Sao Tome and Principe
Uzbekistan
Myanmar
Sierra Leone
Equatorial Guinea
Togo
Congo
Grenada
Maldives
Tonga
Fiji
Vanuatu
Palau
Samoa
Belize
Cuba
Timor-Leste
Afghanistan
Syrian Arab Republic
Kiribati
Tuvalu
Marshall Islands
Papua New Guinea
Djibouti
Solomon Islands
Turkmenistan
Libya
Democratic Republic of the Congo
Nauru
Micronesia
Sudan
Central African Republic
Comoros
Guinea-Bissau
South Sudan
Eritrea
Democratic People's Republic of Korea
Somalia
```

## Resumen ejecutivo para LLM

El Excel 2019 es **sui generis** dentro de la serie Oxford Insights. Usa escala 0-10 (no 0-100), 4 clusters con 12 indicadores (no pilares/dimensiones), y contiene tanto valores crudos como normalizados. La hoja `Data` tiene 3 filas de metadatos, una fila "Max Score" y 194 países. La hoja `Rankings` mezcla rankings globales y regionales en columnas paralelas. Para cualquier análisis cuantitativo, **no comparar directamente con ediciones 2020-2025**; el marco metodológico cambió completamente entre 2019 y 2020.
