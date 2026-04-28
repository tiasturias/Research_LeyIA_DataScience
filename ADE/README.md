# ADE - Análisis Descriptivo Exploratorio

## Descripción

Este directorio contiene el notebook Jupyter para ejecutar el Análisis Descriptivo Exploratorio (ADE) del proyecto "¿Regular o no regular? Impacto de la regulación de IA en los ecosistemas nacionales".

## Estructura

```
ADE/
├── 01_ADE_Analisis_Exploratorio.ipynb  # Notebook principal del ADE
├── outputs/                              # Visualizaciones generadas
│   ├── ade_01_group_distribution.png
│   ├── ade_02_y_by_regulatory_group.png
│   ├── ade_03_y_distributions.png
│   ├── ade_04_y_correlation_matrix.png
│   ├── ade_05_scatter_gdp_outcomes.png
│   ├── ade_06_adoption_vs_internet.png
│   ├── ade_07_regulatory_intensity.png
│   ├── ade_08_full_correlation_matrix.png
│   ├── ade_summary_by_group.csv
│   ├── ade_correlation_matrix_y.csv
│   └── ade_countries_list.csv
└── README.md                             # Este archivo
```

## Requisitos

- Python 3.9+
- pandas
- numpy
- matplotlib
- seaborn
- scipy

## Cómo ejecutar

1. **Activar el entorno virtual:**
   ```bash
   cd /home/pablo/Research_LeyIA_DataScience
   source .venv/bin/activate
   ```

2. **Ejecutar Jupyter:**
   ```bash
   jupyter notebook ADE/01_ADE_Analisis_Exploratorio.ipynb
   ```

3. **O ejecutar en línea de comandos:**
   ```bash
   cd ADE
   jupyter nbconvert --to notebook --execute 01_ADE_Analisis_Exploratorio.ipynb
   ```

## Outputs generados

### Visualizaciones (PNG)
- `ade_01_group_distribution.png` - Distribución de grupos regulatorios
- `ade_02_y_by_regulatory_group.png` - Boxplots de Y por grupo
- `ade_03_y_distributions.png` - Histogramas de variables Y
- `ade_04_y_correlation_matrix.png` - Matriz de correlación Y
- `ade_05_scatter_gdp_outcomes.png` - Scatterplots GDP vs Outcomes
- `ade_06_adoption_vs_internet.png` - Adopción vs Internet por grupo
- `ade_07_regulatory_intensity.png` - Distribución de intensidad regulatoria
- `ade_08_full_correlation_matrix.png` - Correlación completa

### Tablas (CSV)
- `ade_summary_by_group.csv` - Resumen de estadísticas por grupo
- `ade_correlation_matrix_y.csv` - Matriz de correlación Y
- `ade_countries_list.csv` - Lista de países con datos

## Variables analizadas

### Variables Y (Resultado - Ecosistema IA)
- `ai_readiness_score` - Government AI Readiness Index
- `ai_adoption_rate` - Tasa de adopción IA
- `ai_investment_usd_bn_cumulative` - Inversión IA acumulada
- `ai_startups_cumulative` - Startups IA activas
- `ai_patents_per100k` - Patentes IA por 100k hab

### Variables X1 (Tratamiento - Regulación IA)
- `has_ai_law` - ¿Tiene ley IA específica?
- `regulatory_approach` - Enfoque regulatorio
- `regulatory_intensity` - Intensidad regulatoria (0-10)
- `enforcement_level` - Nivel de enforcement
- `thematic_coverage` - Temas cubiertos (0-15)
- `regulatory_status_group` - Grupo colapsado

### Variables X2 (Controles)
- `gdp_per_capita_ppp` - GDP per capita PPP
- `internet_penetration` - Penetración de internet
- `gii_score` - Global Innovation Index
- `rd_expenditure` - Gasto en I+D
- `tertiary_education` - Educación terciaria

## Muestra utilizada

El notebook utiliza la **muestra PRINCIPAL** con 72 países que tienen datos completos para:
- 4 variables Y principales
- 5 variables X1 de regulación
- 5 variables X2 core

## Documentación de referencia

- **Guía ADE:** `../docs/GUIA_ADE_ANALISIS_EXPLORATORIO.md`
- **Diccionario de variables:** `../info_data/GUIA_VARIABLES_ESTUDIO_ETL.md`
- **Decisiones metodológicas:** `../info_data/DATA_DECISIONS_LOG.md`
- **Seguimiento de países:** `../info_data/SEGUIMIENTO_PAISES_MUESTRA.md`

## Autor

Proyecto: "¿Regular o no regular? Impacto de la regulación de IA en los ecosistemas nacionales"

Contexto: Chile - Boletín 16821-19 (Ley Marco de IA)
