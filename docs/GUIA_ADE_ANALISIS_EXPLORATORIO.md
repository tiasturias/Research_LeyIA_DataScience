# Guía Completa para el Análisis Descriptivo Exploratorio (ADE)

## Proyecto: "¿Regular o no regular? Impacto de la regulación de IA en los ecosistemas nacionales"

---

## 1. Objetivo del ADE

El Análisis Descriptivo Exploratorio (ADE) tiene como propósito:

1. **Comprender la estructura** del dataset final (86 países × 105 variables)
2. **Identificar patrones** en las variables de regulación IA (X1) y resultados del ecosistema (Y)
3. **Detectar relaciones preliminares** entre regulación y desarrollo del ecosistema IA
4. **Preparar el terreno** para el modelamiento estadístico
5. **Generar visualizaciones** que informen la interpretación de resultados

---

## 2. Archivo Principal del ADE

### Dataset Definitivo
- **Ubicación:** `data/interim/sample_ready_cross_section.csv`
- **Dimensiones:** 86 filas × 105 columnas
- **Formato:** CSV con separador comma

### Columnas Principales (para el ADE)

| Sección | Columnas clave | Descripción |
|---------|-----------------|-------------|
| **Identificación** | `iso3` | Código país ISO 3166-1 alpha-3 |
| **X1 Regulación** | `has_ai_law`, `regulatory_approach`, `regulatory_intensity`, `enforcement_level`, `thematic_coverage`, `regulatory_status_group` | Variables de tratamiento |
| **Y Ecosistema IA** | `ai_readiness_score`, `ai_adoption_rate`, `ai_investment_usd_bn_cumulative`, `ai_startups_cumulative`, `ai_patents_per100k` | Variables resultado |
| **X2 Controles** | `gdp_per_capita_ppp`, `internet_penetration`, `gii_score`, `rd_expenditure`, `tertiary_education` | Variables de control core |
| **X2 Confounders** | `regulatory_quality`, `rule_of_law`, `has_gdpr_like_law`, `gdpr_similarity_level`, `fh_total_score`, `legal_origin` | Controles post-auditoría |
| **Flags** | `complete_principal`, `complete_confounded`, `complete_extended` | Indicadores de completitud |

---

## 3. Jerarquía de Muestras para el ADE

### Muestra PRINCIPAL (recomendada para ADE)
- **N = 72 países**
- **Criterio:** 4Y + 5X1 + 5X2 core completos
- **Uso:** Análisis principal del ADE

### Muestra CONFOUNDED (para análisis robusto)
- **N = 72 países**
- **Criterio:** PRINCIPAL + WGI (regulatory_quality, rule_of_law) + GDPR-like confounders
- **Uso:** Análisis con controles institucionales

### Muestra EXTENDED
- **N = 62 países**
- **Criterio:** PRINCIPAL + rd_expenditure + tertiary_education

### Cómo filtrar en Python:

```python
import pandas as pd

# Cargar dataset
df = pd.read_csv('data/interim/sample_ready_cross_section.csv')

# Filtrar muestra principal
df_principal = df[df['complete_principal'] == 1].copy()

# Filtrar muestra confounded
df_confounded = df[df['complete_confounded'] == 1].copy()

# Filtrar muestra extended
df_extended = df[df['complete_extended'] == 1].copy()

print(f"Principal: {len(df_principal)} países")
print(f"Confounded: {len(df_confounded)} países")
print(f"Extended: {len(df_extended)} países")
```

---

## 4. Variables Clave para el ADE

### 4.1 Variables de Regulación (X1) -TRATAMIENTO-

| Variable | Tipo | Valores | Descripción |
|----------|------|---------|-------------|
| `has_ai_law` | binaria | 0, 1 | ¿Tiene ley IA específica vigente? |
| `regulatory_approach` | categórica | none, light_touch, strategy_led, regulation_focused, comprehensive | Enfoque regulatorio |
| `regulatory_intensity` | ordinal | 0-10 | Intensidad regulatoria compuesta |
| `enforcement_level` | ordinal | none, low, medium, high | Nivel de enforcement |
| `thematic_coverage` | integer | 0-15 | Número de temas cubiertos |
| `regulatory_status_group` | categórica | binding_regulation, strategy_only, soft_framework, no_framework | Grupo colapsado |

**Distribución esperada (N=72):**
- binding_regulation: 27 países
- strategy_only: 34 países
- soft_framework: 9 países
- no_framework: 2 países

### 4.2 Variables de Resultado (Y) -OUTCOME-

| Variable | Tipo | Rango | Descripción | Fuente |
|----------|------|-------|-------------|--------|
| `ai_readiness_score` | continua | 0-100 | Government AI Readiness Index | Oxford Insights |
| `ai_adoption_rate` | continua | 0-100 | % adopción IA generativa | Microsoft |
| `ai_investment_usd_bn_cumulative` | continua | 0-∞ | Inversión IA acumulada (USD bn) | Stanford |
| `ai_startups_cumulative` | continua | 0-∞ | Startups IA activas | Stanford |
| `ai_patents_per100k` | continua | 0-∞ | Patentes IA por 100k hab | Stanford |

### 4.3 Variables de Control (X2) -CONFOUNDERS-

| Variable | Tipo | Descripción | Fuente |
|----------|------|-------------|--------|
| `gdp_per_capita_ppp` | continua | GDP per capita PPP | World Bank |
| `internet_penetration` | continua | % población con internet | World Bank |
| `gii_score` | continua | Global Innovation Index | WIPO |
| `rd_expenditure` | continua | Gasto I+D % PIB | World Bank |
| `tertiary_education` | continua | Matrícula terciaria % | World Bank |
| `regulatory_quality` | continua | WGI calidad regulatoria (-2.5 a +2.5) | World Bank |
| `rule_of_law` | continua | WGI estado de derecho (-2.5 a +2.5) | World Bank |
| `has_gdpr_like_law` | binaria | Tiene ley GDPR-like | Codificación manual |
| `gdpr_similarity_level` | ordinal | Nivel alineación GDPR (0-3) | Codificación manual |
| `fh_total_score` | continua | Freedom House score (0-100) | Freedom House |
| `legal_origin` | categórica | Familia legal (5 niveles) | La Porta 2008 |
| `is_common_law` | binaria | Es common law (1) o civil law (0) | Derivado |

---

## 5. Consultas de Referencia para el ADE

### 5.1 Consulta 1: Distribución de grupos regulatorios

```python
# Distribución de regulatory_status_group en muestra principal
df_principal['regulatory_status_group'].value_counts()
```

### 5.2 Consulta 2: Estadísticas descriptivas de Y por grupo regulatorio

```python
# Media de Y por grupo regulatorio
y_vars = ['ai_readiness_score', 'ai_adoption_rate', 
          'ai_investment_usd_bn_cumulative', 'ai_startups_cumulative']

df_principal.groupby('regulatory_status_group')[y_vars].describe()
```

### 5.3 Consulta 3: Correlaciones entre variables Y

```python
# Matriz de correlación de variables Y
import seaborn as sns
import matplotlib.pyplot as plt

y_vars = ['ai_readiness_score', 'ai_adoption_rate', 
          'ai_investment_usd_bn_cumulative', 'ai_startups_cumulative']

corr_matrix = df_principal[y_vars].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlación entre variables Y (Ecosistema IA)')
plt.tight_layout()
plt.savefig('outputs/ade_y_correlation_matrix.png', dpi=150)
plt.show()
```

### 5.4 Consulta 4: Relación X1 vs Y (preliminar)

```python
# Boxplot: regulatory_intensity vs ai_readiness_score
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_principal, x='regulatory_status_group', 
            y='ai_readiness_score', palette='viridis')
plt.title('AI Readiness Score por Grupo Regulatorio')
plt.xlabel('Grupo Regulatorio')
plt.ylabel('AI Readiness Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/ade_y_by_regulatory_group.png', dpi=150)
plt.show()
```

### 5.5 Consulta 5: Scatterplot: GDP vs Outcome con color por regulación

```python
# Scatterplot: gdp_per_capita vs ai_investment
plt.figure(figsize=(12, 8))
scatter = plt.scatter(df_principal['gdp_per_capita_ppp'], 
                     df_principal['ai_investment_usd_bn_cumulative'],
                     c=df_principal['regulatory_intensity'], 
                     cmap='RdYlGn_r', alpha=0.7, s=100)
plt.colorbar(scatter, label='Regulatory Intensity')
plt.xlabel('GDP per capita PPP')
plt.ylabel('AI Investment (USD bn)')
plt.title('Inversión IA vs GDP per capita\n(Color: Intensidad Regulatoria)')
plt.tight_layout()
plt.savefig('outputs/ade_investment_vs_gdp.png', dpi=150)
plt.show()
```

### 5.6 Consulta 6: Heatmap de cobertura de datos

```python
# Crear matriz de presencia de datos
coverage_vars = ['ai_readiness_score', 'ai_adoption_rate', 
                 'ai_investment_usd_bn_cumulative', 'ai_startups_cumulative',
                 'gdp_per_capita_ppp', 'internet_penetration', 'gii_score']

coverage_matrix = df[coverage_vars].notna().astype(int)
coverage_matrix.index = df['iso3']

plt.figure(figsize=(10, 20))
sns.heatmap(coverage_matrix, cbar_kws={'label': 'Datos disponibles (1=Sí, 0=No)'})
plt.title('Matriz de Cobertura de Datos por País')
plt.xlabel('Variable')
plt.ylabel('País')
plt.tight_layout()
plt.savefig('outputs/ade_coverage_matrix.png', dpi=150)
plt.show()
```

---

## 6. Documentación de Referencia

### 6.1 Para entender las variables

| Documento | Ubicación | Contenido |
|-----------|-----------|-----------|
| GUIA_VARIABLES_ESTUDIO_ETL.md | info_data/ | Diccionario completo de variables |
| VARIABLES_IAPP.md | info_data/ | Variables X1 de regulación |
| VARIABLES_OXFORD_INSIGHTS.md | info_data/ | Variables Y de Oxford |
| VARIABLES_MICROSOFT.md | info_data/ | Variables Y de Microsoft |
| VARIABLES_WORLD_BANK_WDI.md | info_data/ | Variables X2 del World Bank |
| VARIABLES_WIPO_GII.md | info_data/ | Variables X2 de WIPO |
| VARIABLES_STANFORND_IA_INDEX.md | info_data/ | Variables Y de Stanford |

### 6.2 Para entender las decisiones metodológicas

| Documento | Ubicación | Contenido |
|-----------|-----------|-----------|
| DATA_DECISIONS_LOG.md | info_data/ | Las 17 decisiones metodológicas |
| SEGUIMIENTO_PAISES_MUESTRA.md | info_data/ | Estado de países y muestras |
| ETL_RUNBOOK.md | info_data/ | Pipeline de datos |

### 6.3 Para entender la taxonomía regulatoria

| Grupo | Descripción | Países típicos |
|-------|-------------|----------------|
| binding_regulation | Ley vinculante + estrategia | UE (27), China, Corea |
| strategy_only | Estrategia sin ley vinculante | Chile, USA, UK, Australia |
| soft_framework | Principios no vinculantes | India, Israel, Suiza |
| no_framework | Sin marco IA | Camerún, Líbano |

---

## 7. Estructura Sugerida del Notebook ADE

### Sección 1: Setup y Carga
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configuración de visualizaciones
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('viridis')

# Cargar dataset
df = pd.read_csv('data/interim/sample_ready_cross_section.csv')
```

### Sección 2: Filtrar a muestra principal
```python
# Usar muestra principal para análisis
df_ade = df[df['complete_principal'] == 1].copy()
print(f"Análisis con {len(df_ade)} países")
```

### Sección 3: Estadísticas descriptivas generales
```python
# Resumen de variables Y
y_vars = ['ai_readiness_score', 'ai_adoption_rate', 
          'ai_investment_usd_bn_cumulative', 'ai_startups_cumulative']
df_ade[y_vars].describe()
```

### Sección 4: Análisis por grupo regulatorio
```python
# Tabla resumen: media de Y por grupo
grouped = df_ade.groupby('regulatory_status_group')[y_vars].agg(['mean', 'std', 'count'])
print(grouped)
```

### Sección 5: Visualizaciones
1. Boxplots de Y por grupo regulatorio
2. Histogramas de variables Y
3. Scatterplots Y vs X2 (GDP, internet, etc.)
4. Heatmap de correlaciones
5. Barras de participación de grupos

### Sección 6: Tests preliminares
```python
# Test ANOVA simple
from scipy.stats import f_oneway

groups = [group['ai_readiness_score'].dropna() 
          for name, group in df_ade.groupby('regulatory_status_group')]
f_stat, p_value = f_oneway(*groups)
print(f"ANOVA: F={f_stat:.2f}, p={p_value:.4f}")
```

### Sección 7: Conclusiones del ADE
- Resumen de hallazgos
- Patrones identificados
- Recomendaciones para modelamiento

---

## 8. Outputs Esperados del ADE

### 8.1 Visualizaciones (guardar en outputs/)

| Archivo | Descripción |
|---------|-------------|
| `ade_y_distribution.png` | Distribución de variables Y |
| `ade_y_by_regulatory_group.png` | Boxplots Y por grupo |
| `ade_y_correlation_matrix.png` | Matriz de correlación Y |
| `ade_investment_vs_gdp.png` | Scatterplot inversión vs GDP |
| `ade_coverage_matrix.png` | Heatmap de cobertura |
| `ade_regulatory_intensity_distribution.png` | Distribución intensidad regulatoria |

### 8.2 Tablas resumen

| Archivo | Descripción |
|---------|-------------|
| `ade_summary_stats.csv` | Estadísticas descriptivas |
| `ade_group_means.csv` | Medias por grupo regulatorio |
| `ade_correlation_matrix.csv` | Matriz de correlación |

---

## 9. Consideraciones Metodológicas

### 9.1 Manejo de valores faltantes
- Las variables Y tienen diferentes coberturas
- Filtrar según el análisis específico
- Documentar países con datos faltantes

### 9.2 Transformaciones recomendadas
- **Log-transform** para variables con sesgo (inversión, startups, patentes)
- **Normalización** si se usará clustering

### 9.3 Variables categóricas
- `regulatory_approach`: 5 niveles (considerar colapsar a 4)
- `regulatory_status_group`: 4 niveles (ya colapsado)
- `legal_origin`: 5 familias (English, French, German, Scandinavian, Socialist)
- `region`: geografía (varias categorías)

---

## 10. Casos de Interés Especial

### Chile en el dataset:
```python
chile = df_ade[df_ade['iso3'] == 'CHL']
print(chile[['iso3', 'regulatory_approach', 'regulatory_intensity', 
             'ai_readiness_score', 'ai_adoption_rate', 
             'ai_investment_usd_bn_cumulative', 'ai_startups_cumulative']])
```

### Países con binding_regulation:
```python
binding = df_ade[df_ade['regulatory_status_group'] == 'binding_regulation']
print(f"N = {len(binding)} países")
print(binding[['iso3', 'regulatory_intensity', 'ai_readiness_score']].head(10))
```

### Países con no_framework:
```python
no_framework = df_ade[df_ade['regulatory_status_group'] == 'no_framework']
print(no_framework[['iso3', 'ai_readiness_score', 'ai_adoption_rate']])
```

---

## 11. Referencias Metodológicas

### Para interpretación de resultados:
- **Stanford AI Index 2025:** https://hai.stanford.edu/ai-index
- **Oxford Insights AI Readiness:** https://oxfordinsights.com/ai-readiness/
- **Microsoft AI Diffusion:** https://www.microsoft.com/en-us/research/group/aiei/ai-diffusion/
- **IAPP Global AI Law Tracker:** https://iapp.org/resources/article/global-ai-legislation-tracker/
- **World Bank WDI:** https://data.worldbank.org/
- **WIPO GII:** https://www.wipo.int/global-innovation-index/

### Para decisiones metodológicas:
- Ver `DATA_DECISIONS_LOG.md` para entender el rationale de cada variable
- Ver `GUIA_VARIABLES_ESTUDIO_ETL.md` para definiciones exactas

---

## 12. Próximos Pasos Post-ADE

Tras completar el ADE, el flujo continúa con:

1. **02_limpieza.ipynb:** Limpieza avanzada, manejo de outliers, transformaciones
2. **04_modelamiento.ipynb:** OLS, K-Means, PCA
3. **05_nlp.ipynb:** Análisis de textos legales

---

## 13. Contacto y Soporte

Para dudas sobre:
- **Variables:** Consultar `info_data/GUIA_VARIABLES_ESTUDIO_ETL.md`
- **Metodología:** Consultar `info_data/DATA_DECISIONS_LOG.md`
- **Datos:** Consultar `notebooks/01_recoleccion.ipynb`
- **Corpus Legal:** Consultar `data/raw/legal_corpus/`

---

**Última actualización:** 2026-04-22
**Proyecto:** "¿Regular o no regular? Impacto de la regulación de IA en los ecosistemas nacionales"
**Contexto:** Chile - Boletín 16821-19 (Ley Marco de IA)
