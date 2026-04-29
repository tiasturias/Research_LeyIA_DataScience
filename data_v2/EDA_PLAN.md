# Plan EDA — Análisis Exploratorio de la Matriz País × Atributos

## Contexto

- **Input**: `matriz_consolidada_paises_atributos.csv` (86 países × 366 atributos)
- **Output**: Notebook `eda_legal_ai.ipynb` con análisis completo y visualizaciones
- **Objetivo**: Enterner la estrutura de la matriz, identificar patrones de datos faltantes, construir submatrices densas, y analizar correlaciones y outliers

---

## 0. Setup y Configuración

### 0.1 Imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from scipy import stats
from scipy.spatial.distance import mahalanobis
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Configuración visual
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 10
plt.rcParams['savefig.bbox'] = 'tight'
sns.set_theme(style="whitegrid", palette="viridis")
COLORS = sns.color_palette("viridis", 8)
```

### 0.2 Carga de datos
```python
df = pd.read_csv('matriz_consolidada_paises_atributos.csv')
print(f"Shape: {df.shape}")
print(f"Países: {df['iso3'].nunique()}")
print(f"Atributos: {df.shape[1] - 1}")
print(f"Completitud global: {df.notna().sum().sum() / df.size * 100:.1f}%")
```

### 0.3 Diccionario de fuentes
```python
SOURCE_META = {
    'iapp':    {'name': 'IAPP AI Legislation Tracker',     'color': '#1b9e77'},
    'oxford':  {'name': 'Oxford AI Readiness Index',       'color': '#d95f02'},
    'wipo':    {'name': 'WIPO Global Innovation Index',    'color': '#7570b3'},
    'ms':      {'name': 'Microsoft AI Diffusion Study',    'color': '#e7298a'},
    'gdpr':    {'name': 'GDPR-like Data Protection Coding','color': '#66a61e'},
    'fh':      {'name': 'Freedom House FiW 2025',          'color': '#e6ab02'},
    'oecd':    {'name': 'OECD AI Policy Observatory',      'color': '#a6761d'},
    'wb':      {'name': 'World Bank WDI',                   'color': '#666666'},
    'stanford': {'name': 'Stanford AI Index 2025',          'color': '#984ea3'},
    'legal':   {'name': 'Legal Origin Coding',              'color': '#999999'},
}

def get_source(col):
    """Extraer prefijo de fuente de un nombre de columna."""
    if col in ('iso3', 'country_name', 'region', 'income_group', 'is_common_law', 'legal_origin'):
        return 'meta'
    return col.split('_')[0]
```

---

## 1. Limpieza de la Matriz

### 1.1 Eliminar columnas metadato y sin datos

**Columnas a eliminar (0 datos):**
- `oxford_cluster_governance`, `oxford_cluster_government_and_public_services`, `oxford_cluster_infrastructure_and_data`, `oxford_cluster_skills_and_education`
- `wipo_international_restrictions`

**Columnas a eliminar (metadato descriptivo, no analítico):**
- `country_name` (redundante con iso3)
- `iapp_source`, `iapp_source_date`, `iapp_evidence_summary`, `iapp_jurisdiction_iapp`
- `fh_country_name`, `fh_notes`, `fh_year`
- `gdpr_country_name`, `gdpr_notes`, `gdpr_dp_law_name`
- `oxford_ai_readiness_score`, `oxford_oxford_rank_reported` (duplicadas de `oxford_readiness_score` y `oxford_rank`)

```python
drop_zero_cols = [c for c in df.columns if df[c].notna().sum() == 0]
drop_meta = [
    'country_name',
    'iapp_source', 'iapp_source_date', 'iapp_evidence_summary', 'iapp_jurisdiction_iapp',
    'fh_country_name', 'fh_notes', 'fh_year',
    'gdpr_country_name', 'gdpr_notes', 'gdpr_dp_law_name',
    'oxford_ai_readiness_score', 'oxford_oxford_rank_reported',
]
```

### 1.2 Resolver columnas duplicadas

Para cada par duplicado, quedarse con la versión con MÁS datos:

| Columna a MANTENER | Columna a ELIMINAR | Motivo |
|---|---|---|
| `fh_fh_total_score` (84/86) | `fh_total_score` (2/86) | Más datos en fh_fh_* |
| `fh_fh_pr_score` (84/86) | `fh_political_rights_score` (2/86) | Más datos en fh_fh_* |
| `fh_fh_cl_score` (84/86) | `fh_civil_liberties_score` (2/86) | Más datos en fh_fh_* |
| `fh_fh_status` (84/86) | `fh_status` (2/86) | Más datos en fh_fh_* |
| `gdpr_gdpr_similarity_level` (84/86) | `gdpr_similarity_level` (2/86) | Más datos en gdpr_gdpr_* |
| `gdpr_law_name` (2/86) | Ya eliminado en metadato | — |
| `ms_ai_user_share_h1_2025` (73/86) | `ms_ai_adoption_h1_2025` (2/86) | Más datos en ms_ai_user_* |
| `ms_ai_user_share_h2_2025` (73/86) | `ms_ai_adoption_h2_2025` (2/86) | Más datos en ms_ai_user_* |
| `ms_ai_user_share_change_pp` (73/86) | `ms_ai_adoption_change_pp` (2/86) | Más datos en ms_ai_user_* |

```python
drop_duplicates = [
    'fh_total_score', 'fh_political_rights_score', 'fh_civil_liberties_score', 'fh_status',
    'gdpr_similarity_level', 'gdpr_law_name', 'gdpr_law_year',
    'ms_ai_adoption_h1_2025', 'ms_ai_adoption_h2_2025', 'ms_ai_adoption_change_pp',
]
```

### 1.3 Colapsar WB por métrica (tomar año más reciente disponible)

 Para cada métrica WB con variantes por año, crear una columna consolidada tomando el valor del año más reciente disponible:

| Métrica original (variantes) | Columna resultante |
|---|---|
| `wb_education_expenditure_pct_gdp_*` | `wb_education_expenditure_pct_gdp` |
| `wb_exports_pct_gdp_*` | `wb_exports_pct_gdp` |
| `wb_internet_penetration_*` | `wb_internet_penetration` |
| `wb_mobile_subscriptions_per100_*` | `wb_mobile_subscriptions_per100` |
| `wb_patent_applications_residents_*` | `wb_patent_applications_residents` |
| `wb_rd_expenditure_pct_gdp_*` | `wb_rd_expenditure_pct_gdp` |
| `wb_tertiary_education_*` | `wb_tertiary_education` |
| `wb_high_tech_exports_pct_*` | `wb_high_tech_exports_pct` |
| `wb_ict_service_exports_pct_*` | `wb_ict_service_exports_pct` |
| Mantener sin colapsar (1 sola variante): | `wb_control_of_corruption_2023`, `wb_fdi_net_inflows_2024`, `wb_gdp_current_usd_2024`, `wb_gdp_per_capita_ppp_2024`, `wb_government_effectiveness_2023`, `wb_inflation_consumer_prices_2024`, `wb_labor_force_2024`, `wb_political_stability_2023`, `wb_population_2024`, `wb_regulatory_quality_2023`, `wb_rule_of_law_2023`, `wb_unemployment_rate_2024`, `wb_voice_accountability_2023` |
| Eliminar (duplicado con renombrada): | `wb_fdi_net_inflows_usd_2024`, `wb_gdp_current_usd_bn_2024`, `wb_voice_and_accountability_2023`, `wb_tertiary_education_rate_2023`, `wb_inflation_2024`, `wb_rd_expenditure_2016` a `2022` (ya colapsadas), `wb_education_expenditure_pct_gdp_2020` a `2024` (ya colapsadas), etc. |
| Eliminar (dato original suelto con 1-2 valores): | `wb_year`, `wb_exports_pct_gdp_2023`, `wb_internet_penetration_2022`, `wb_mobile_subscriptions_per100_2022`, `wb_rd_expenditure_2016`...`2021`, `wb_education_expenditure_pct_gdp_2020`...`2024`, etc. |

```python
# Lógica de colapso
def collapse_wb_metric(df, metric_prefix):
    """Para una métrica WB con variantes por año,
    crear una columna con el valor del año más reciente disponible."""
    year_cols = [c for c in df.columns if c.startswith(metric_prefix) and c[-4:].isdigit()]
    if len(year_cols) <= 1:
        return df, year_cols
    # Tomar el año más reciente con dato
    def pick_latest(row):
        for c in sorted(year_cols, key=lambda x: int(x[-4:]), reverse=True):
            if pd.notna(row[c]):
                return row[c]
        return np.nan
    df[metric_prefix] = df.apply(pick_latest, axis=1)
    return df, year_cols
```

### 1.4 Filtrar y renombrar Stanford

**Eliminar columnas Stanford con <5% completitud (<5 valores de 86):**
- ~140 columnas de figure labels, year columns, descripciones

**Renombrar las ~15-20 columnas Stanford supervivientes (>5% completitud) con nombres interpretables:**

| Columna original | Nombre propuesto |
|---|---|
| `stanford_fig_1.2.4` | `stanford_ai_patents_per100k` |
| `stanford_fig_1.3.3` | `stanford_notable_ml_models_country` |
| `stanford_fig_4.2.13` | `stanford_ai_skill_penetration_category` |
| `stanford_fig_4.2.15` | `stanford_ai_skill_penetration_rate_value` |
| `stanford_fig_4.2.19` | `stanford_ai_hiring_rate_value` |
| `stanford_fig_4.2.22` | `stanford_net_ai_talent_migration_value` |
| `stanford_fig_4.3.8` | `stanford_ai_investment_value` |
| `stanford_fig_4.3.9` | `stanford_ai_investment_cumulative` |
| `stanford_fig_4.3.12` | `stanford_ai_newly_funded_companies` |
| `stanford_fig_4.3.13` | `stanford_ai_newly_funded_companies_cumulative` |
| `stanford_fig_6.2.1` | `stanford_ai_bills_passed` |
| `stanford_fig_6.2.15` | `stanford_ai_mentions_parliamentary_value` |
| `stanford_fig_6.2.16` | `stanford_ai_mentions_parliamentary_cumulative` |
| `stanford_fig_6.3.1` | `stanford_ai_public_contracts_total_value` |
| `stanford_fig_6.3.2` | `stanford_ai_public_contracts_n` |
| `stanford_fig_6.3.3` | `stanford_ai_public_contracts_median_value` |
| `stanford_fig_6.3.4` | `stanford_ai_public_contracts_per_capita` |

**NOTA**: Revisar en el notebook los tipos de dato. Las columnas `stanford_fig_4.2.13`, `stanford_fig_4.2.14`, `stanford_fig_4.2.17`, `stanford_fig_4.2.18`, `stanford_fig_4.2.23` son categóricas (bins/regiones) → se excluyen de correlación numérica o se codifican.

### 1.5 Codificar variables categóricas

Crear variables codificadas para análisis numérico:

| Variable original | Variable codificada | Esquema |
|---|---|---|
| `iapp_regulatory_approach` | `iapp_approach_ordinal` | none=0, light_touch=1, strategy_led=2, comprehensive=3 |
| `iapp_enforcement_level` | `iapp_enforcement_ordinal` | none=0, low=1, medium=2, high=3 |
| `gdpr_eu_status` | `gdpr_eu_member`, `gdpr_eu_adequacy` | Dummies (one-hot k-1: reference=none) |
| `income_group` | `income_ordinal` | LM=0, UM=1, HI=2 |
| `legal_origin` | `legal_french`, `legal_english`, `legal_socialist`, `legal_german` | Dummies (reference=scandinavian) |
| `region` | `region_europe`, `region_latam`, `region_mena`, `region_asia`, `region_africa` | Dummies (agrupación regional) |
| `fh_fh_status` | `fh_free`, `fh_partly_free` | Dummies (reference=not_free) |
| `iapp_has_ai_law` | Ya es binaria | 0/1 |
| `gdpr_has_gdpr_like_law` | Ya es binaria | 0/1 |
| `gdpr_has_dpa` | Ya es binaria | 0/1 |
| `gdpr_enforcement_active` | Ya es binaria | 0/1 |
| `is_common_law` | Ya es binaria | 0/1 |

```python
approach_map = {'none': 0, 'light_touch': 1, 'strategy_led': 2, 'comprehensive': 3}
enforcement_map = {'none': 0, 'low': 1, 'medium': 2, 'high': 3}
income_map = {'LM': 0, 'UM': 1, 'HI': 2}
```

### 1.6 Resultadoesperado de la limpieza

- **Matriz limpia**: ~120-140 atributos × 86 países
- **Columnas eliminadas**: ~220 (metadato, duplicadas, 0 datos, Stanford <5%)
- **Columnas colapsadas WB**: 53 → ~25
- **Columnas codificadas nuevas**: ~15 dummies/ordinales

Guardar como `matriz_limpia.csv`.

---

## 2. Análisis de NA (Datos Faltantes)

### 2.1 NA por atributo — Tabla de completitud

```python
completitud = pd.DataFrame({
    'atributo': df_limpio.columns,
    'fuente': [get_source(c) for c in df_limpio.columns],
    'n_valores': df_limpio.notna().sum().values,
    'pct_completitud': (df_limpio.notna().sum().values / 86 * 100).round(1),
}).sort_values('pct_completitud', ascending=False)

completitud.to_csv('eda_completitud_atributos.csv', index=False)
```

### 2.2 NA por atributo — Histograma de completitud

**Gráfico 1**: Histograma de completitud (% de valores no-NA) por atributo

```python
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(completitud['pct_completitud'], bins=20, edgecolor='black', color=COLORS[0])
ax.axvline(x=80, color='red', linestyle='--', label='Umbral 80%')
ax.axvline(x=50, color='orange', linestyle='--', label='Umbral 50%')
ax.set_xlabel('Completitud (%)')
ax.set_ylabel('Número de atributos')
ax.set_title('Distribución de completitud por atributo')
ax.legend()
plt.tight_layout()
plt.savefig('fig_01_histograma_completitud.png')
```

### 2.3 NA por atributo — Heatmap por fuente

**Gráfico 2**: Heatmap atributo × país con NA = blanco, valor = color (agrupado por fuente)

```python
# Ordenar columnas por fuente y completitud
cols_ordered = df_limpio.columns.tolist()
# Agrupar por fuente
source_groups = {}
for c in cols_ordered:
    s = get_source(c)
    source_groups.setdefault(s, []).append(c)

# Heatmap con seaborn
fig, ax = plt.subplots(figsize=(20, 16))
sns.heatmap(df_limpio.set_index('iso3')[all_numeric_cols].notna().astype(int),
            cmap='YlGnBu', cbar_kws={'label': 'Dato presente'}, ax=ax)
ax.set_title('Mapa de calor de datos faltantes (1=dato, 0=NA)')
plt.tight_layout()
plt.savefig('fig_02_heatmap_na.png')
```

### 2.4 NA por fuente — Barplot apilado

**Gráfico 3**: Para cada fuente: % de completitud, número de atributos

```python
source_comp = completitud.groupby('fuente').agg(
    n_attrs=('atributo', 'count'),
    avg_pct=('pct_completitud', 'mean'),
    median_pct=('pct_completitud', 'median'),
).sort_values('avg_pct', ascending=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
# Barplot de completitud promedio
source_comp['avg_pct'].plot(kind='barh', ax=ax1, color=[SOURCE_META.get(s, {}).get('color', '#999') for s in source_comp.index])
ax1.set_xlabel('Completitud promedio (%)')
ax1.set_title('Completitud promedio por fuente')
# Barplot de número de atributos
source_comp['n_attrs'].plot(kind='barh', ax=ax2, color=[SOURCE_META.get(s, {}).get('color', '#999') for s in source_comp.index])
ax2.set_xlabel('Número de atributos')
ax2.set_title('Atributos por fuente')
plt.tight_layout()
plt.savefig('fig_03_completitud_por_fuente.png')
```

### 2.5 NA por país — Tabla y ranking

```python
pais_comp = pd.DataFrame({
    'iso3': df_limpio['iso3'],
    'n_atributos': df_limpio.notna().sum(axis=1).values,
    'pct_completitud': (df_limpio.notna().sum(axis=1).values / df_limpio.shape[1] * 100).round(1),
}).sort_values('pct_completitud', ascending=False)

pais_comp.to_csv('eda_completitud_paises.csv', index=False)
```

### 2.6 NA por país — Barplot horizontal

**Gráfico 4**: Barplot horizontal de completitud por país (ordenado de mayor a menor)

```python
fig, ax = plt.subplots(figsize=(10, 20))
ax.barh(pais_comp['iso3'], pais_comp['pct_completitud'], color=COLORS[0])
ax.axvline(x=50, color='red', linestyle='--')
ax.set_xlabel('Completitud (%)')
ax.set_title('Completitud por país')
plt.tight_layout()
plt.savefig('fig_04_completitud_por_pais.png')
```

### 2.7 Correlación de NA

**Gráfico 5**: Heatmap de correlación de NA entre variables clave — ¿si falta una, falta la otra?

```python
# Seleccionar top 30 variables por completitud
top_vars = completitud.head(30)['atributo'].tolist()
na_matrix = df_limpio[top_vars].isna().astype(float)
na_corr = na_matrix.corr()

fig, ax = plt.subplots(figsize=(14, 12))
sns.heatmap(na_corr, cmap='RdBu_r', center=0, ax=ax, vmin=-1, vmax=1)
ax.set_title('Correlación de NA entre variables (si falta una, ¿falta la otra?)')
plt.tight_layout()
plt.savefig('fig_05_correlacion_na.png')
```

### 2.8 Profiling de países con baja completitud

**Gráfico 6**: Scatter plot completitud vs PIB per cápita (coloreado por income_group)

```python
fig, ax = plt.subplots(figsize=(10, 6))
for ig in ['LM', 'UM', 'HI']:
    mask = df_limpio['income_group'] == ig
    ax.scatter(df_limpio.loc[mask, 'wipo_ppp_per_capita'],
               pais_comp.loc[mask, 'pct_completitud'],
               label=ig, alpha=0.7)
ax.set_xlabel('PIB per cápita PPP (USD)')
ax.set_ylabel('Completitud (%)')
ax.set_title('Completitud vs PIB per cápita por grupo de ingreso')
ax.legend()
plt.tight_layout()
plt.savefig('fig_06_completitud_vs_ppp.png')
```

### 2.9 Identificar países sin datos Microsoft

```python
no_ms = df_limpio[df_limpio['ms_ai_user_share_h2_2025'].isna()]['iso3'].tolist()
print(f"Países sin datos Microsoft ({len(no_ms)}): {', '.join(no_ms)}")
print("Características comunes: micro-estados, UE sin survey, TWN/BLZ sin WIPO")
```

---

## 3. Construcción de Submatrices Densas

### 3.1 Definición de 3 submatrices

| Submatriz | Criterio | Atributos | Países | Variable clave excluida |
|---|---|---|---|---|
| **Core A** | 100% completitud, solo numéricas/binarias | ~24 | 86 | `ms_ai_user_share_h2_2025` (solo 73/86) |
| **Core B** | ≥95% completitud (≤4 NA) | ~31 | 82-84 | — |
| **Core C** | ≥80% completitud (≤17 NA) | ~37 | 73 | — |

### 3.2 Variables de cada Core

**Core A — 100% denso (24 variables × 86 países):**
1. `iso3`
2. `iapp_has_ai_law` (binaria)
3. `iapp_regulatory_intensity` (0-10)
4. `iapp_thematic_coverage` (0-10)
5. `iapp_approach_ordinal` (0-3)
6. `iapp_enforcement_ordinal` (0-3)
7. `oxford_readiness_score`
8. `oxford_rank`
9. `oxford_pillar_policy_capacity`
10. `oxford_pillar_ai_infrastructure`
11. `oxford_pillar_governance`
12. `oxford_pillar_public_sector_adoption`
13. `oxford_pillar_development_and_diffusion`
14. `oxford_pillar_resilience`
15. `oxford_dimension_compute_capacity`
16. `oxford_dimension_policy_vision`
17. `oxford_dimension_e_government_delivery`
18. `oxford_dimension_safety_and_security`
19. `gdpr_has_gdpr_like_law` (binaria)
20. `gdpr_has_dpa` (binaria)
21. `gdpr_enforcement_active` (binaria)
22. `is_common_law` (binaria)
23. `income_ordinal` (0-2)
24. `region_europe`, `region_latam`, `region_mena`, `region_asia`, `region_africa` (dummies)

**Core B — ≥95% denso (agrega 7 variables, pierde BLZ+TWN):**
25. `wipo_gii_score`
26. `wipo_gii_rank`
27. `wipo_ppp_per_capita`
28. `wipo_business_sophistication`
29. `wipo_infrastructure`
30. `wipo_institutional_environment`
31. `gdpr_gdpr_similarity_level`

**Core C — ≥80% denso (agrega 6 variables, pierde 13 países sin MS):**
32. `ms_ai_user_share_h2_2025`
33. `ms_ai_user_share_h1_2025`
34. `ms_ai_user_share_change_pp`
35. `fh_fh_total_score`
36. `fh_fh_pr_score`
37. `fh_fh_cl_score`

### 3.3 Generación de submatrices

```python
# Core A: 100% denso
core_a_vars = [v for v in CORE_A_VARS if v in df_limpio.columns]
core_a = df_limpio.set_index('iso3')[core_a_vars]
core_a = core_a.dropna()
print(f"Core A: {core_a.shape[0]} países × {core_a.shape[1]} variables")
core_a.to_csv('matriz_core_A.csv')

# Core B: >=95% denso
core_b_vars = CORE_A_VARS + CORE_B_EXTRA_VARS
core_b = df_limpio.set_index('iso3')[[v for v in core_b_vars if v in df_limpio.columns]]
core_b = core_b.dropna()
print(f"Core B: {core_b.shape[0]} países × {core_b.shape[1]} variables")
core_b.to_csv('matriz_core_B.csv')

# Core C: >=80% denso
core_c_vars = core_b_vars + CORE_C_EXTRA_VARS
core_c = df_limpio.set_index('iso3')[[v for v in core_c_vars if v in df_limpio.columns]]
core_c = core_c.dropna()
print(f"Core C: {core_c.shape[0]} países × {core_c.shape[1]} variables")
core_c.to_csv('matriz_core_C.csv')
```

### 3.4 Validación de submatrices

**Gráfico 7**: Comparación de la distribución de variables clave entre Core A, B, C

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
for i, var in enumerate(['oxford_readiness_score', 'wipo_gii_score', 'iapp_regulatory_intensity',
                          'ms_ai_user_share_h2_2025', 'gdpr_gdpr_similarity_level', 'fh_fh_total_score']):
    ax = axes[i // 3, i % 3]
    data_a = core_a[var] if var in core_a.columns else None
    data_b = core_b[var] if var in core_b.columns else None
    data_c = core_c[var] if var in core_c.columns else None
    # KDE plot for each core
    if data_a is not None: sns.kdeplot(data_a, ax=ax, label='Core A')
    if data_b is not None: sns.kdeplot(data_b, ax=ax, label='Core B')
    if data_c is not None: sns.kdeplot(data_c, ax=ax, label='Core C')
    ax.set_title(var)
    ax.legend()
plt.tight_layout()
plt.savefig('fig_07_distribucion_cores.png')
```

---

## 4. Análisis de Correlación

### 4.1 Correlación Pearson sobre Core B (variable principal de análisis)

**Gráfico 8**: Heatmap de correlación Pearson (Core B, 31 variables × 82 países)

```python
# Usar Core B como base principal de correlación
corr_matrix = core_b.corr(method='pearson')

fig, ax = plt.subplots(figsize=(18, 16))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, cmap='RdBu_r', center=0,
            vmin=-1, vmax=1, annot=True, fmt='.2f', linewidths=0.5,
            ax=ax, cbar_kws={'label': 'Correlación Pearson'})
ax.set_title('Matriz de Correlación — Core B (82 países × 31 variables)')
plt.tight_layout()
plt.savefig('fig_08_correlacion_pearson_coreB.png')
```

### 4.2 Correlaciones fuertes (|r| > 0.5)

```python
# Extraer duplas con correlación fuerte
strong_corr = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        r = corr_matrix.iloc[i, j]
        if abs(r) > 0.5:
            strong_corr.append({
                'var_1': corr_matrix.columns[i],
                'var_2': corr_matrix.columns[j],
                'r': round(r, 3),
                'abs_r': round(abs(r), 3)
            })

strong_corr_df = pd.DataFrame(strong_corr).sort_values('abs_r', ascending=False)
strong_corr_df.to_csv('eda_correlaciones_fuertes.csv', index=False)
print(f"Correlaciones fuertes (|r|>0.5): {len(strong_corr_df)}")
display(strong_corr_df.head(20))
```

### 4.3 Scatter plots de correlaciones clave

**Gráfico 9**: Panel de 6 scatter plots de duplas correlacionadas

```python
scatter_pairs = [
    ('oxford_readiness_score', 'wipo_gii_score', 'Oxford Readiness vs WIPO GII Score'),
    ('iapp_regulatory_intensity', 'gdpr_gdpr_similarity_level', 'Regulatory Intensity vs GDPR Similarity'),
    ('wipo_ppp_per_capita', 'oxford_pillar_ai_infrastructure', 'GDP per capita vs AI Infrastructure'),
    ('oxford_readiness_score', 'fh_fh_total_score', 'AI Readiness vs Freedom House Score'),
    ('iapp_regulatory_intensity', 'ms_ai_user_share_h2_2025', 'Regulatory Intensity vs AI Adoption'),
    ('wipo_gii_score', 'gdpr_gdpr_similarity_level', 'Innovation vs GDPR Similarity'),
]

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
for idx, (x_var, y_var, title) in enumerate(scatter_pairs):
    ax = axes[idx // 3, idx % 3]
    df_plot = df_limpio.copy()
    # Color por income_group
    colors = {'HI': '#2ca02c', 'UM': '#ff7f0e', 'LM': '#d62728'}
    for ig, color in colors.items():
        mask = df_plot['income_group'] == ig
        ax.scatter(df_plot.loc[mask, x_var], df_plot.loc[mask, y_var],
                   c=color, label=ig, alpha=0.7, edgecolors='black', linewidth=0.5)
    # Annotate outliers
    for _, row in df_plot.iterrows():
        if pd.notna(row[x_var]) and pd.notna(row[y_var]):
            ax.annotate(row['iso3'], (row[x_var], row[y_var]), fontsize=5, alpha=0.6)
    ax.set_xlabel(x_var)
    ax.set_ylabel(y_var)
    ax.set_title(title)
    ax.legend()
plt.tight_layout()
plt.savefig('fig_09_scatter_correlaciones.png')
```

### 4.4 Correlación parcial controlando por ingreso

```python
from pingouin import partial_corr

# Correlación parcial entre regulatory_intensity y AI adoption, controlando por ppp_per_capita
# Si no hay pingouin, usar residuals:
# 1. Regresar y sobre x1 y control
# 2. Correlacionar residuos

# Alternativa sin pingouin: residualizar manualmente
from sklearn.linear_model import LinearRegression

def partial_corr(df, x, y, controls):
    """Correlación parcial entre x e y, controlando por controls."""
    sub = df[[x, y] + controls].dropna()
    # Regresar x sobre controls
    reg_x = LinearRegression().fit(sub[controls], sub[x])
    res_x = sub[x] - reg_x.predict(sub[controls])
    # Regresar y sobre controls
    reg_y = LinearRegression().fit(sub[controls], sub[y])
    res_y = sub[y] - reg_y.predict(sub[controls])
    return np.corrcoef(res_x, res_y)[0, 1]

# Correlaciones parciales clave
pairs = [
    ('iapp_regulatory_intensity', 'ms_ai_user_share_h2_2025', ['wipo_ppp_per_capita']),
    ('iapp_regulatory_intensity', 'ms_ai_user_share_h2_2025', ['oxford_readiness_score']),
    ('oxford_readiness_score', 'wipo_gii_score', ['wipo_ppp_per_capita']),
    ('gdpr_gdpr_similarity_level', 'wipo_gii_score', ['wipo_ppp_per_capita']),
]

for x, y, controls in pairs:
    r_raw = df_limpio[[x, y]].dropna().corr().iloc[0, 1]
    r_partial = partial_corr(df_limpio, x, y, controls)
    print(f"{x} <-> {y} | controls={controls}")
    print(f"  r_raw={r_raw:.3f}, r_partial={r_partial:.3f}, diff={r_raw - r_partial:.3f}")
```

### 4.5 V de Cramer entre variables categóricas

```python
from scipy.stats import chi2_contingency

def cramers_v(x, y):
    """Calcular V de Cramer entre dos variables categóricas."""
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    return np.sqrt(phi2 / min(r - 1, k - 1))

cat_vars = ['iapp_regulatory_approach', 'iapp_enforcement_level', 'gdpr_eu_status',
            'income_group', 'legal_origin', 'region', 'fh_fh_status']

cramer_matrix = pd.DataFrame(index=cat_vars, columns=cat_vars)
for v1 in cat_vars:
    for v2 in cat_vars:
        sub = df_limpio[[v1, v2]].dropna()
        if len(sub) > 5:
            cramer_matrix.loc[v1, v2] = cramers_v(sub[v1], sub[v2])
        else:
            cramer_matrix.loc[v1, v2] = np.nan

cramer_matrix = cramer_matrix.astype(float)
```

**Gráfico 10**: Heatmap de V de Cramer

```python
fig, ax = plt.subplots(figsize=(8, 7))
sns.heatmap(cramer_matrix.astype(float), cmap='YlOrRd', annot=True, fmt='.2f',
            vmin=0, vmax=1, ax=ax, cbar_kws={'label': "V de Cramer"})
ax.set_title("Asociación entre variables categóricas (V de Cramer)")
plt.tight_layout()
plt.savefig('fig_10_cramer_v.png')
```

### 4.6 Correlación por grupo de ingreso

**Gráfico 11**: Scatter plot `oxford_readiness_score` vs `wipo_gii_score` facetado por income_group

```python
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
for i, ig in enumerate(['LM', 'UM', 'HI']):
    mask = df_limpio['income_group'] == ig
    sub = df_limpio[mask][['oxford_readiness_score', 'wipo_gii_score']].dropna()
    r = sub.corr().iloc[0, 1]
    axes[i].scatter(sub['oxford_readiness_score'], sub['wipo_gii_score'], color=COLORS[i])
    axes[i].set_title(f'{ig} (n={len(sub)}, r={r:.2f})')
    axes[i].set_xlabel('Oxford Readiness Score')
    axes[i].set_ylabel('WIPO GII Score')
    for iso in df_limpio.loc[mask, 'iso3']:
        x = df_limpio.loc[df_limpio['iso3']==iso, 'oxford_readiness_score'].values
        y = df_limpio.loc[df_limpio['iso3']==iso, 'wipo_gii_score'].values
        if len(x) > 0 and len(y) > 0 and pd.notna(x[0]) and pd.notna(y[0]):
            axes[i].annotate(iso, (x[0], y[0]), fontsize=5)
plt.tight_layout()
plt.savefig('fig_11_correlacion_por_ingreso.png')
```

### 4.7 EU vs Non-EU: Efecto del tratado supranacional

**Gráfico 12**: Boxplot de `iapp_regulatory_intensity` por `gdpr_eu_status`

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
vars_by_eu = ['iapp_regulatory_intensity', 'oxford_readiness_score', 'ms_ai_user_share_h2_2025']
for i, var in enumerate(vars_by_eu):
    sub = df_limpio[['iso3', 'gdpr_eu_status', var]].dropna()
    sns.boxplot(data=sub, x='gdpr_eu_status', y=var, ax=axes[i])
    axes[i].set_title(f'{var} by EU status')
plt.tight_layout()
plt.savefig('fig_12_eu_vs_noneu.png')
```

---

## 5. Detección de Outliers

### 5.1 Outliers Univariados

**Por cada variable numérica**: calcular z-score y flaggear |z| > 3

```python
outliers_univariados = []
numeric_cols = core_b.select_dtypes(include=[np.number]).columns.tolist()

for col in numeric_cols:
    vals = core_b[col].dropna()
    z = stats.zscore(vals)
    outlier_mask = np.abs(z) > 3
    for idx in vals.index[outlier_mask]:
        outliers_univariados.append({
            'iso3': idx,
            'variable': col,
            'valor': vals[idx],
            'z_score': z[vals.index.get_loc(idx)],
            'percentil': stats.percentileofscore(vals, vals[idx])
        })

outliers_df = pd.DataFrame(outliers_univariados)
outliers_df = outliers_df.sort_values('z_score', key=abs, ascending=False)
outliers_df.to_csv('eda_outliers_univariados.csv', index=False)

# Resumen: cuántos outliers por país
outlier_summary = outliers_df.groupby('iso3').size().sort_values(ascending=False)
print("Países con más outliers univariados:")
display(outlier_summary.head(15))
```

**Gráfico 13**: Boxplots de variables clave para identificar outliers visualmente

```python
key_vars_boxplot = [
    'oxford_readiness_score', 'wipo_gii_score', 'iapp_regulatory_intensity',
    'ms_ai_user_share_h2_2025', 'wipo_ppp_per_capita', 'fh_fh_total_score'
]

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
for i, var in enumerate(key_vars_boxplot):
    ax = axes[i // 3, i % 3]
    sub = df_limpio[['iso3', var]].dropna()
    bp = ax.boxplot(sub[var], vert=True, patch_artist=True)
    ax.set_title(var)
    ax.set_ylabel('Valor')
    # Annotate outliers
    q1, q3 = sub[var].quantile(0.25), sub[var].quantile(0.75)
    iqr = q3 - q1
    outliers_mask = (sub[var] < q1 - 1.5 * iqr) | (sub[var] > q3 + 1.5 * iqr)
    for iso in sub.loc[outliers_mask, 'iso3']:
        x_noise = np.random.normal(1, 0.05)
        y = sub.loc[sub['iso3'] == iso, var].values[0]
        ax.annotate(iso, (x_noise, y), fontsize=7, color='red')
plt.tight_layout()
plt.savefig('fig_13_boxplots_outliers.png')
```

### 5.2 Outliers Multivariados — Distancia Mahalanobis

```python
from scipy.spatial.distance import mahalanobis

# Usar Core B (82 países × variables numéricas)
core_b_numeric = core_b.select_dtypes(include=[np.number]).dropna()
scaler = StandardScaler()
core_b_scaled = pd.DataFrame(
    scaler.fit_transform(core_b_numeric),
    columns=core_b_numeric.columns,
    index=core_b_numeric.index
)

# Calcular distancia Mahalanobis
cov_matrix = core_b_scaled.cov().values
inv_cov = np.linalg.pinv(cov_matrix)
means = core_b_scaled.mean().values

mahal_distances = []
for idx in core_b_scaled.index:
    row = core_b_scaled.loc[idx].values
    d = mahalanobis(row, means, inv_cov)
    mahal_distances.append({'iso3': idx, 'mahal_dist': d})

mahal_df = pd.DataFrame(mahal_distances).sort_values('mahal_dist', ascending=False)

# Umbral: chi2 con df = número de variables, p=0.01
threshold = stats.chi2.ppf(0.99, df=len(core_b_numeric.columns))
mahal_df['outlier'] = mahal_df['mahal_dist'] > threshold

print(f"Outliers multivariados (Mahalanobis, p<0.01):")
display(mahal_df[mahal_df['outlier']])
```

**Gráfico 14**: Scatter de distancia Mahalanobis, flagged outliers en rojo

```python
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(range(len(mahal_df)), mahal_df['mahal_dist'].values, 
           c=mahal_df['outlier'].map({True: 'red', False: 'blue'}))
ax.axhline(y=threshold**0.5, color='red', linestyle='--', label=f'Umbral chi2 (p=0.01)')
for idx, row in mahal_df.iterrows():
    if row['outlier']:
        ax.annotate(row['iso3'], (idx, row['mahal_dist']), fontsize=8, color='red')
ax.set_xlabel('País (ordenado por distancia)')
ax.set_ylabel('Distancia Mahalanobis')
ax.set_title('Detección de outliers multivariados (Mahalanobis)')
ax.legend()
plt.tight_layout()
plt.savefig('fig_14_mahalanobis.png')
```

### 5.3 Outliers Multivariados — Isolation Forest

```python
iso_forest = IsolationForest(contamination=0.1, random_state=42, n_estimators=100)
core_b_scaled_clean = core_b_scaled.dropna()
outlier_labels = iso_forest.fit_predict(core_b_scaled_clean)

if_df = pd.DataFrame({
    'iso3': core_b_scaled_clean.index,
    'outlier_score': iso_forest.decision_function(core_b_scaled_clean),
    'is_outlier': outlier_labels == -1
}).sort_values('outlier_score')

print("Outliers detectados por Isolation Forest:")
display(if_df[if_df['is_outlier']])
```

### 5.4 Comparación Mahalanobis vs Isolation Forest

**Gráfico 15**: Scatter Mahalanobis vs Isolation Forest score

```python
merged = mahal_df.merge(if_df[['iso3', 'outlier_score', 'is_outlier']], on='iso3')
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(merged['mahal_dist'], merged['outlier_score'],
           c=merged['is_outlier'].map({True: 'red', False: 'blue'}), alpha=0.7)
for _, row in merged.iterrows():
    if row['is_outlier'] or row['mahal_dist'] > threshold**0.5:
        ax.annotate(row['iso3'], (row['mahal_dist'], row['outlier_score']), fontsize=7)
ax.set_xlabel('Distancia Mahalanobis')
ax.set_ylabel('Isolation Forest Score')
ax.set_title('Outliers: Mahalanobis vs Isolation Forest')
plt.tight_layout()
plt.savefig('fig_15_mahalanobis_vs_iforest.png')
```

### 5.5 Outliers Contextuales — Regulatory Over/Underperformers

**Definición**: Países cuya intensidad regulatoria difiere de lo predicho por su nivel de desarrollo

```python
from sklearn.linear_model import LinearRegression

sub = df_limpio[['iso3', 'iapp_regulatory_intensity', 'wipo_ppp_per_capita', 'oxford_readiness_score']].dropna()

# Regresar iapp_regulatory_intensity sobre wipo_ppp_per_capita y oxford_readiness_score
X = sub[['wipo_ppp_per_capita', 'oxford_readiness_score']]
y = sub['iapp_regulatory_intensity']
reg = LinearRegression().fit(X, y)
sub['predicted_intensity'] = reg.predict(X)
sub['residual'] = sub['iapp_regulatory_intensity'] - sub['predicted_intensity']

# Overperformers: regulatory intensity > predicted
# Underperformers: regulatory intensity < predicted
overperformers = sub.nlargest(10, 'residual')
underperformers = sub.nsmallest(10, 'residual')

print("=== REGULATORY OVERPERFORMERS (more regulation than predicted) ===")
display(overperformers[['iso3', 'iapp_regulatory_intensity', 'predicted_intensity', 'residual']])

print("\n=== REGULATORY UNDERPERFORMERS (less regulation than predicted) ===")
display(underperformers[['iso3', 'iapp_regulatory_intensity', 'predicted_intensity', 'residual']])
```

**Gráfico 16**: Scatter predicted vs actual regulatory intensity con over/underperformers señalizados

```python
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(sub['predicted_intensity'], sub['iapp_regulatory_intensity'], alpha=0.5)
ax.plot([0, 10], [0, 10], 'k--', label='Predicción perfecta')
for _, row in sub.iterrows():
    if abs(row['residual']) > 2.5:
        ax.annotate(row['iso3'], (row['predicted_intensity'], row['iapp_regulatory_intensity']),
                     fontsize=7, color='red' if row['residual'] > 0 else 'blue')
ax.set_xlabel('Intensidad Regulatoria Predicha')
ax.set_ylabel('Intensidad Regulatoria Observada')
ax.set_title('Regulatory Over/Underperformers')
ax.legend()
plt.tight_layout()
plt.savefig('fig_16_regulatory_overperformers.png')
```

### 5.6 Adoption Paradox — Alta adopción IA con baja regulación

**Definición**: Países con alta `ms_ai_user_share_h2_2025` pero baja `iapp_regulatory_intensity`

```python
sub2 = df_limpio[['iso3', 'iapp_regulatory_intensity', 'ms_ai_user_share_h2_2025', 'oxford_readiness_score']].dropna()

# Normalizar ambas dimensiones
sub2['reg_norm'] = (sub2['iapp_regulatory_intensity'] - sub2['iapp_regulatory_intensity'].mean()) / sub2['iapp_regulatory_intensity'].std()
sub2['adopt_norm'] = (sub2['ms_ai_user_share_h2_2025'] - sub2['ms_ai_user_share_h2_2025'].mean()) / sub2['ms_ai_user_share_h2_2025'].std()

# Adoption paradox: alta adopción, baja regulación
sub2['adoption_paradox_score'] = sub2['adopt_norm'] - sub2['reg_norm']
paradox = sub2.nlargest(10, 'adoption_paradox_score')
print("=== ADOPTION PARADOX (alta adopción, baja regulación) ===")
display(paradox[['iso3', 'iapp_regulatory_intensity', 'ms_ai_user_share_h2_2025', 'adoption_paradox_score']])
```

**Gráfico 17**: Cuadrante regulatory_intensity vs AI adoption

```python
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(sub2['iapp_regulatory_intensity'], sub2['ms_ai_user_share_h2_2025'], alpha=0.5)
# Líneas de referencia (medianas)
ax.axvline(x=sub2['iapp_regulatory_intensity'].median(), color='gray', linestyle='--')
ax.axhline(y=sub2['ms_ai_user_share_h2_2025'].median(), color='gray', linestyle='--')
# Etiquetar esquinas
ax.text(1, 30, 'Low Reg, High Adoption\n(Paradox)', fontsize=10, color='red', ha='center')
ax.text(9, 30, 'High Reg, High Adoption\n(Aligned)', fontsize=10, color='green', ha='center')
ax.text(1, 5, 'Low Reg, Low Adoption\n(Emerging)', fontsize=10, color='blue', ha='center')
ax.text(9, 5, 'High Reg, Low Adoption\n(Restrictive)', fontsize=10, color='orange', ha='center')
# Annotate paradox countries
for _, row in paradox.head(5).iterrows():
    ax.annotate(row['iso3'], (row['iapp_regulatory_intensity'], row['ms_ai_user_share_h2_2025']),
                fontsize=8, fontweight='bold')
ax.set_xlabel('Regulatory Intensity (IAPP)')
ax.set_ylabel('AI Adoption Share H2 2025 (Microsoft)')
ax.set_title('Adoption Paradox: Regulatory Intensity vs AI Adoption')
plt.tight_layout()
plt.savefig('fig_17_adoption_paradox.png')
```

### 5.7 Casos especiales a flaggear

```python
# EU members: all have regulatory_intensity=10
eu_members = df_limpio[df_limpio['gdpr_eu_status'] == 'eu_member']['iso3'].tolist()
print(f"EU members ({len(eu_members)}): {', '.join(eu_members)}")
print(f"Todos tienen iapp_regulatory_intensity=10: {(df_limpio[df_limpio['gdpr_eu_status']=='eu_member']['iapp_regulatory_intensity']==10).all()}")

# CHL: focal case
chl = df_limpio[df_limpio['iso3'] == 'CHL']
print(f"\n=== CHL ===")
for col in chl.columns:
    val = chl[col].values[0]
    if pd.notna(val):
        print(f"  {col}: {val}")

# USA: outlier esperado
usa = df_limpio[df_limpio['iso3'] == 'USA']
print(f"\n=== USA ===")
for col in usa.columns:
    val = usa[col].values[0]
    if pd.notna(val):
        print(f"  {col}: {val}")
```

**Gráfico 18**: Perfil radar de CHL, USA, y promedios por grupo

```python
from math import pi

def radar_chart(df, countries, variables, labels=None):
    """Crear gráfico radar para países seleccionados."""
    categories = labels or variables
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    for i, iso in enumerate(countries):
        values = []
        for var in variables:
            val = df.loc[df['iso3']==iso, var].values
            values.append(val[0] if len(val) > 0 and pd.notna(val[0]) else 0)
        # Normalizar
        values_norm = [(v - df[var].min()) / (df[var].max() - df[var].min()) for v, var in zip(values, variables)]
        values_norm += values_norm[:1]
        ax.plot(angles, values_norm, 'o-', linewidth=2, label=iso, color=colors[i % len(colors)])
        ax.fill(angles, values_norm, alpha=0.1, color=colors[i % len(colors)])
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=8)
    ax.set_title('Perfil Radar: CHL, USA, y promedios')
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    return fig

# Seleccionar variables normalizables
radar_vars = ['oxford_readiness_score', 'wipo_gii_score', 'iapp_regulatory_intensity',
              'ms_ai_user_share_h2_2025', 'gdpr_gdpr_similarity_level', 'fh_fh_total_score']
radar_labels = ['AI Readiness', 'Innovation', 'Regul. Intensity',
                'AI Adoption', 'GDPR Similarity', 'Freedom House']

fig = radar_chart(df_limpio, ['CHL', 'USA', 'DEU', 'CHN', 'SGP'], radar_vars, radar_labels)
plt.savefig('fig_18_radar_perfiles.png')
```

---

## 6. Análisis de Componentes Principales (PCA)

### 6.1 PCA sobre Core B

```python
core_b_numeric = core_b.select_dtypes(include=[np.number]).dropna()
scaler = StandardScaler()
core_b_scaled = scaler.fit_transform(core_b_numeric)

pca = PCA(n_components=min(len(core_b_numeric.columns), len(core_b_numeric)))
pca_data = pca.fit_transform(core_b_scaled)

# Varianza explicada
print("Varianza explicada por componente:")
for i, (ev, ratio) in enumerate(zip(pca.explained_variance_, pca.explained_variance_ratio_)):
    print(f"  PC{i+1}: {ev:.2f} ({ratio*100:.1f}%)")
print(f"Varianza acumulada (PC1-PC5): {sum(pca.explained_variance_ratio_[:5])*100:.1f}%")
```

### 6.2 Scree plot

**Gráfico 19**: Scree plot y varianza acumulada

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Scree plot
ax1.bar(range(1, len(pca.explained_variance_ratio_)+1), pca.explained_variance_ratio_ * 100,
        color=COLORS[0], edgecolor='black')
ax1.set_xlabel('Componente Principal')
ax1.set_ylabel('Varianza Explicada (%)')
ax1.set_title('Scree Plot')

# Varianza acumulada
cumulative = np.cumsum(pca.explained_variance_ratio_) * 100
ax2.plot(range(1, len(cumulative)+1), cumulative, 'o-', color=COLORS[1])
ax2.axhline(y=80, color='red', linestyle='--', label='Umbral 80%')
ax2.axhline(y=90, color='orange', linestyle='--', label='Umbral 90%')
ax2.set_xlabel('Número de Componentes')
ax2.set_ylabel('Varianza Acumulada (%)')
ax2.set_title('Varianza Acumulada')
ax2.legend()
plt.tight_layout()
plt.savefig('fig_19_pca_scree.png')
```

### 6.3 Biplot PC1 vs PC2

**Gráfico 20**: PCA biplot con países coloreados por income_group y vectores de carga

```python
loadings = pd.DataFrame(pca.components_[:2].T, 
                        columns=['PC1', 'PC2'], 
                        index=core_b_numeric.columns)

fig, ax = plt.subplots(figsize=(12, 10))

# Plot países
colors_ig = {'LM': '#d62728', 'UM': '#ff7f0e', 'HI': '#2ca02c'}
for ig, color in colors_ig.items():
    mask = core_b.index.isin(df_limpio[df_limpio['income_group']==ig]['iso3'])
    ax.scatter(pca_data[mask, 0], pca_data[mask, 1], c=color, label=ig, alpha=0.7, s=40)

# Annotate países
for i, iso in enumerate(core_b_numeric.index):
    ax.annotate(iso, (pca_data[i, 0], pca_data[i, 1]), fontsize=5, alpha=0.6)

# Plot vectores de carga (top 10 variables por carga)
top_vars = loadings.abs().sum(axis=1).nlargest(10).index
for var in top_vars:
    ax.annotate('', xy=(loadings.loc[var, 'PC1']*3, loadings.loc[var, 'PC2']*3),
                xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax.text(loadings.loc[var, 'PC1']*3.2, loadings.loc[var, 'PC2']*3.2,
            var.replace('oxford_', 'o_').replace('wipo_', 'w_').replace('iapp_', 'i_'),
            fontsize=7, color='red')

ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% varianza)')
ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% varianza)')
ax.set_title('PCA Biplot — Core B (82 países)')
ax.legend()
ax.axhline(y=0, color='gray', linewidth=0.5)
ax.axvline(x=0, color='gray', linewidth=0.5)
plt.tight_layout()
plt.savefig('fig_20_pca_biplot.png')
```

### 6.4 Loadings de las primeras 5 componentes

**Gráfico 21**: Heatmap de loadings PC1-PC5

```python
loadings_5 = pd.DataFrame(pca.components_[:5].T,
                           columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5'],
                           index=core_b_numeric.columns)

fig, ax = plt.subplots(figsize=(10, 14))
sns.heatmap(loadings_5, cmap='RdBu_r', center=0, annot=True, fmt='.2f', ax=ax)
ax.set_title('Cargas (Loadings) de las 5 primeras Componentes Principales')
plt.tight_layout()
plt.savefig('fig_21_pca_loadings.png')
```

---

## 7. Resumen y Conclusiones

### 7.1 Tabla resumen de hallazgos

Crear un DataFrame con hallazgos clave para incluir en el reporte:

| Hallazgo | Variable(s) | Dirección | Magnitud | Nota |
|---|---|---|---|---|
| Correlación Oxford-WIPO | `oxford_readiness_score` ↔ `wipo_gii_score` | Positiva fuerte | r ≈ 0.90+ | Países innovadores = países preparados para IA |
| Correlación PIB-Readiness | `wipo_ppp_per_capita` ↔ `oxford_readiness_score` | Positiva | r ≈ 0.70+ | Desarrollo económico predice preparación IA |
| EU Regulatory Cluster | `gdpr_eu_status=eu_member` → `iapp_regulatory_intensity=10` | Perfecta | 100% | 27 países EU = cluster artificial |
| Adoption Paradox | `iapp_regulatory_intensity` ↔ `ms_ai_user_share_h2_2025` | ¿Negativa o nula? | r ≈ ? | ¿Más regulación = menos adopción? |
| GDPR-Innovation | `gdpr_gdpr_similarity_level` ↔ `wipo_gii_score` | Positiva | r ≈ ? | Países GDPR-like = más innovadores (¿o más ricos?) |
| Freedom-Readiness | `fh_fh_total_score` ↔ `oxford_readiness_score` | Positiva | r ≈ ? | ¿Democracias más preparadas para IA? |

### 7.2 Outliers flaggeados

| País | Tipo de Outlier | Variable(s) | Valor | Contexto |
|---|---|---|---|---|
| USA | Univariado | `wipo_ppp_per_capita`, `ms_ai_user_share` | Alto | Outlier esperado: economy + AI leader |
| CHN | Multivariado | Regulatory intensity vs readiness | Alto reg, alto readiness | Autoritario con alta capacidad IA |
| ... | ... | ... | ... | ... |

### 7.3 Limitaciones del análisis

1. **EU AI Act**: 27 países comparten `regulatory_intensity=10` y `approach=comprehensive` por tratado supranacional → inflar correlaciones artificiales
2. **Microsoft Adoption**: 13 países sin datos de adopción (micro-estados, EU pequeños) → sesgo de selección
3. **Stanford**: Completitud 10.8% → excluidos del análisis correlacional principal
4. **WIPO**: BLZ y TWN sin datos → excluidos de Core B
5. **Causalidad**: Correlación NO implica causalidad; la relación regulación-adopción es endógena

### 7.4 Siguientes pasos

- [ ] Construir modelos de regresión para explicar `iapp_regulatory_intensity` y `ms_ai_user_share_h2_2025`
- [ ] Análisis de clustering (K-means, hierarchical) sobre Core B
- [ ] Modelo de efectos fijos con dummy de EU membership
- [ ] Incluir datos de `legal_corpus` (SOURCES.md, CANDIDATES.md) como variables explicativas
- [ ] Robustez: correr análisis con y sin EU, con y sin USA

---

## 8. Estructura del Notebook

```
eda_legal_ai.ipynb
├── 0. Setup y Configuración
│   ├── 0.1 Imports
│   ├── 0.2 Carga de datos
│   └── 0.3 Diccionario de fuentes
├── 1. Limpieza de la Matriz
│   ├── 1.1 Eliminar columnas metadato y sin datos
│   ├── 1.2 Resolver columnas duplicadas
│   ├── 1.3 Colapsar WB por métrica
│   ├── 1.4 Filtrar y renombrar Stanford
│   ├── 1.5 Codificar variables categóricas
│   └── 1.6 Guardar matriz limpia
├── 2. Análisis de NA
│   ├── 2.1 NA por atributo — Tabla
│   ├── 2.2 Histograma de completitud
│   ├── 2.3 Heatmap NA por fuente
│   ├── 2.4 Barplot completitud por fuente
│   ├── 2.5 NA por país — Ranking
│   ├── 2.6 Barplot completitud por país
│   ├── 2.7 Correlación de NA
│   ├── 2.8 Completitud vs PIB per cápita
│   └── 2.9 Países sin datos Microsoft
├── 3. Construcción de Submatrices Densas
│   ├── 3.1 Definición de Core A, B, C
│   ├── 3.2 Generación de CSVs
│   └── 3.3 Validación (KDE por Core)
├── 4. Análisis de Correlación
│   ├── 4.1 Heatmap Pearson (Core B)
│   ├── 4.2 Correlaciones fuertes (|r|>0.5)
│   ├── 4.3 Scatter plots clave
│   ├── 4.4 Correlación parcial (control ingreso)
│   ├── 4.5 V de Cramer (categóricas)
│   ├── 4.6 Correlación por grupo de ingreso
│   └── 4.7 EU vs Non-EU
├── 5. Detección de Outliers
│   ├── 5.1 Outliers univariados (z-score)
│   ├── 5.2 Outliers multivariados (Mahalanobis)
│   ├── 5.3 Outliers multivariados (Isolation Forest)
│   ├── 5.4 Comparación Mahalanobis vs IF
│   ├── 5.5 Regulatory Over/Underperformers
│   ├── 5.6 Adoption Paradox
│   └── 5.7 Casos especiales (EU, CHL, USA)
├── 6. PCA
│   ├── 6.1 PCA sobre Core B
│   ├── 6.2 Scree plot
│   ├── 6.3 Biplot PC1 vs PC2
│   └── 6.4 Loadings PC1-PC5
└── 7. Resumen y Conclusiones
    ├── 7.1 Tabla de hallazgos
    ├── 7.2 Outliers flaggeados
    ├── 7.3 Limitaciones
    └── 7.4 Siguientes pasos
```

---

## Entregables

| Archivo | Descripción |
|---|---|
| `eda_legal_ai.ipynb` | Notebook completo con análisis y 21 figuras |
| `matriz_limpia.csv` | Matriz limpia (~120-140 atributos × 86 países) |
| `matriz_core_A.csv` | Submatriz 100% densa (24 vars × 86 países) |
| `matriz_core_B.csv` | Submatriz ≥95% densa (31 vars × 82 países) |
| `matriz_core_C.csv` | Submatriz ≥80% densa (37 vars × 73 países) |
| `eda_completitud_atributos.csv` | Tabla de completitud por atributo (matriz limpia) |
| `eda_completitud_paises.csv` | Tabla de completitud por país (matriz limpia) |
| `eda_correlaciones_fuertes.csv` | Duplas con |r|>0.5 |
| `eda_outliers_univariados.csv` | Outliers univariados |
| `fig_01` a `fig_21` | 21 figuras PNG |
| `EDA_PLAN.md` | Este documento |