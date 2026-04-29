# ADE - Análisis Descriptivo Exploratorio (v2)

## Descripción

Este directorio contiene el notebook Jupyter para ejecutar el **Análisis Descriptivo Exploratorio (ADE)** del proyecto *"¿Regular o no regular? Impacto de la regulación de IA en los ecosistemas nacionales"*.

**Versión actual:** v2 (2026-04-28) — actualizada con corpus legal-IA 38/86, x1_master_v2 (propuestas de la skill), variables nuevas derivadas del corpus.

## Estructura

```
ADE/
├── 01_ADE_Analisis_Exploratorio.ipynb     # Notebook principal v2
├── 01_ADE_Analisis_Exploratorio.ipynb.bak # Backup de la versión v1
├── build_notebook.py                       # Constructor del .ipynb v2 (regenerable)
├── outputs/                                # Visualizaciones + tablas exportadas
├── corpus_consolidated/                    # Corpus consolidado por país (planificado)
├── embedded_rag/                           # Datos embeddings (75 países)
├── scripts/                                # Scripts auxiliares de consolidación
├── PLAN_CONSOLIDACION.md                   # Plan de consolidación a legal-rag
└── README.md                               # Este archivo
```

## Cambios v1 → v2

| Elemento | v1 | v2 |
|---|---|---|
| Cells totales | 43 | 62 |
| Fuente X1 principal | `sample_ready_cross_section.csv` (IAPP) | + `x1_master_v2.csv` (IAPP **+** propuestas corpus-legal-ia) |
| Cobertura corpus | 23 países | **38 países en muestra** (+QAT externo) |
| Variables nuevas | — | `has_dedicated_ai_authority`, `ai_law_pathway_declared`, `ai_corpus_n_documents`, `ai_corpus_total_pages`, `ai_corpus_years_span` |
| Sección comparativa IAPP vs Propuesta | — | Sección 7 dedicada con diff plots y tabla de cambios |
| Estado del corpus por país | — | Sección 2 con tabla y gráfico por región |
| Test de robustez X1 propuesta | — | Sección 10.4 — correlación con Y bajo IAPP vs propuesta |
| Análisis Chile | descriptivo + comparación | descriptivo + nota sobre PENDING corpus (sin SCM) |

## Requisitos

- Python 3.9+
- pandas, numpy, matplotlib, seaborn, scipy
- (opcional) jupyter para ejecución interactiva

## Cómo ejecutar

### Modo 1 — Jupyter interactivo

```bash
cd /home/pablo/Research_LeyIA_DataScience
source .venv/bin/activate
jupyter notebook ADE/01_ADE_Analisis_Exploratorio.ipynb
```

### Modo 2 — Ejecución por línea de comandos

```bash
cd ADE
jupyter nbconvert --to notebook --execute 01_ADE_Analisis_Exploratorio.ipynb \
    --output 01_ADE_Analisis_Exploratorio.ipynb
```

### Modo 3 — Regenerar el notebook desde cero

Si necesitas reconstruir el .ipynb (por ejemplo, después de modificar el dataset):

```bash
cd ADE
python3 build_notebook.py
```

## Outputs generados

### Visualizaciones (PNG)

#### Heredadas (renombradas v2)
- `ade_01_group_distribution.png` — Distribución de grupos regulatorios
- `ade_02_y_by_regulatory_group.png` — Boxplots Y por grupo
- `ade_03_y_distributions.png` — Histogramas de variables Y
- `ade_04_y_correlation_matrix.png` — Matriz de correlación Y
- `ade_05_scatter_gdp_outcomes.png` — Scatterplots GDP vs Outcomes
- `ade_06_adoption_vs_internet.png` — Adopción vs Internet por grupo
- `ade_07_regulatory_intensity.png` — Distribución intensidad regulatoria
- `ade_08_full_correlation_matrix.png` — Correlación completa Y/X1/X2

#### Nuevas v2
- `ade_v2_00_corpus_coverage_by_region.png` — Cobertura corpus legal-IA por región
- `ade_v2_01_corpus_metrics.png` — Histogramas de # documentos, páginas y span temporal
- `ade_v2_02_iapp_vs_proposed.png` — Diff plot IAPP vs propuesta corpus
- `ade_v2_03_corpus_extras_vs_y.png` — Variables nuevas (autoridad / pathway) vs AI Readiness

### Tablas (CSV)

#### Heredadas
- `ade_summary_by_group.csv` — Resumen estadísticas por grupo regulatorio
- `ade_correlation_matrix_y.csv` — Matriz de correlación Y
- `ade_countries_list.csv` — Lista de países con datos

#### Nuevas v2
- `ade_v2_iapp_vs_proposed.csv` — Tabla comparativa IAPP vs propuesta por país
- `ade_v2_corpus_status_per_country.csv` — Estado del corpus por país (DONE/PENDING + métricas)

## Variables analizadas

### Variables Y (Resultado - Ecosistema IA)
- `ai_readiness_score` — Government AI Readiness Index (Oxford Insights)
- `ai_adoption_rate` — Tasa de adopción IA (Microsoft)
- `ai_investment_usd_bn_cumulative` — Inversión IA acumulada (Microsoft)
- `ai_startups_cumulative` — Startups IA activas (Microsoft)
- `ai_patents_per100k` — Patentes IA por 100k hab (WIPO)

### Variables X1 (IAPP base)
- `has_ai_law` — ¿Tiene ley IA específica?
- `regulatory_approach` — Enfoque regulatorio
- `regulatory_intensity` (0-10) — Intensidad regulatoria
- `enforcement_level` — Nivel de enforcement
- `thematic_coverage` (0-15) — Temas cubiertos
- `regulatory_status_group` — Grupo colapsado en 4 buckets

### Variables X1 PROPUESTAS por skill `corpus-legal-ia` (NUEVO v2)
- `regulatory_intensity_proposed` — Recodificación basada en corpus extraído
- `thematic_coverage_proposed`
- `regulatory_regime_group_proposed` — 4 buckets harmonizados
- `enforcement_level_proposed`
- `has_ai_law_proposed`

### Variables nuevas derivadas del corpus (NUEVO v2)
- `has_dedicated_ai_authority` (0/1) — País tiene autoridad IA específica designada
- `ai_law_pathway_declared` (0/1) — Existe bill/draft con fecha pública
- `ai_corpus_n_documents` (int) — Número de documentos en el corpus extraído
- `ai_corpus_total_pages` (int) — Suma de páginas en el corpus
- `ai_corpus_years_span` (int) — Span temporal (último año - primer año)

### Variables X2 (Controles)
- `gdp_per_capita_ppp` — GDP per capita PPP (World Bank)
- `internet_penetration` — Penetración Internet
- `gii_score` — Global Innovation Index (WIPO)
- `rd_expenditure` — Gasto en I+D (% PIB)
- `tertiary_education` — Educación terciaria (%)

### Variables X2 Confounders
- `regulatory_quality`, `rule_of_law` (World Bank WGI)
- `has_gdpr_like_law`, `gdpr_similarity_level` (codificación GDPR)
- `fh_total_score` (Freedom House)
- `legal_origin`, `is_common_law` (Legal Origin)

## Muestra utilizada

- **Dataset principal:** 86 países × 105 variables (`sample_ready_cross_section.csv`)
- **Muestra principal del análisis:** 72 países (`complete_principal == 1`)
- **Países con corpus legal-IA extraído:** 38/86 (44%)
- **Países con propuesta X1 de la skill:** 41 (40 en muestra + QAT externo)

## Estado del Corpus Legal-IA

| Categoría | Cuenta |
|---|---|
| Total muestra | 86 |
| **Procesados (DONE)** en muestra | **38** |
| Pendientes en muestra | 48 |
| Procesados fuera de muestra (referencia) | 1 (QAT) |
| Países con bloqueos automáticos documentados | 5 (CMR, KAZ, LBN, BHR, ARM) |

Detalle exacto de avance: `.claude/skills/corpus-legal-ia/sample.md`

## Sub-estudios paralelos (NO incluidos en este ADE)

Los siguientes análisis están en desarrollo separado y NO se cubren aquí:

1. **MVP Top 30** — submuestra N=30 (29 P1-TOP30 DONE + CHL focal). Análisis SCM contrafactual de Chile, modelado OLS/CEM/IV/Bayesian. Carpeta: `notebooks/03a_eda_top30_mvp.ipynb` (planificada).

2. **Proxies de infraestructura** — 6 pilotos (SGP, JPN, FRA, IRL, GBR, ESP) × 33 variables (DC capacity, grid wait, EED compliance, water stress, etc.). Carpeta: `data/raw/proxies/`. Ver `data/raw/proxies/SOURCES_INVENTORY.md`.

3. **NLP del corpus** — análisis textual de los 38 corpus extraídos (topic modeling, similitud entre marcos). Notebook: `notebooks/05_nlp.ipynb` (planificada).

## Documentación de referencia

- **Plan MVP Top 30:** `../ARCHIVOS_MD_CONTEXTO/PLAN_MVP_TOP30_PAISES.md`
- **Aclaración estado Top 30:** `../ARCHIVOS_MD_CONTEXTO/ACLARACION_ESTADO_TOP30_PAISES.md`
- **Hallazgos diferenciales por país:** `../docs/HALLAZGOS_DIFERENCIALES.md` (38 países)
- **Skill `corpus-legal-ia`:** `../.claude/skills/corpus-legal-ia/`
- **Tabla maestra de avance:** `../.claude/skills/corpus-legal-ia/sample.md`
- **Diccionario de variables:** `../info_data/GUIA_VARIABLES_ESTUDIO_ETL.md`
- **Decisiones metodológicas:** `../info_data/DATA_DECISIONS_LOG.md`
- **Bloqueos del corpus:** `../data/raw/legal_corpus/BLOQUEOS_AUTOMATICOS.md`

## Autor

Proyecto: *"¿Regular o no regular? Impacto de la regulación de IA en los ecosistemas nacionales"*

Curso: IMT3860 — Pontificia Universidad Católica de Chile, abril 2026.

Contexto regulatorio chileno: **Boletín 16821-19** (Ley Marco de IA).
