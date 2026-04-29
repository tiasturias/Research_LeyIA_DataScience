# CLAUDE.md — Contexto profundo del proyecto LeyIA DataScience

> **Para:** Claude Opus / Sonnet en conversaciones futuras  
> **Propósito:** Contexto completo del proyecto sin necesidad de leer cada archivo  
> **Foco principal:** `data_v2/` — dataset definitivo y activo de trabajo  
> **Fecha de actualización:** 2026-04-29

---

## 1. ¿Qué es este proyecto?

**Proyecto académico IMT3860 — Introducción a Data Science (Pontificia Universidad Católica de Chile, abril 2026)**

**Pregunta de investigación:**
> *¿Existe una asociación estadísticamente significativa entre las características de la regulación de IA de un país y el desarrollo de su ecosistema de IA, después de controlar por factores socioeconómicos e institucionales?*

**Contexto legislativo:** Chile tiene en tramitación el **Boletín 16821-19** ("Ley Marco de Inteligencia Artificial"), aprobado por la Cámara de Diputados y actualmente en la Comisión de Ciencia, Tecnología e Innovación del Senado. El proyecto busca generar evidencia empírica para informar esa decisión legislativa concreta.

**Audiencia objetivo:** Legisladores del Senado chileno, Ministerio de Ciencia, y academia.

**Entregable final:** Notebook Jupyter completo + video presentación (8 min) — semana del 7-14 mayo 2026.

---

## 2. Arquitectura del proyecto

```
/home/pablo/Research_LeyIA_DataScience/
├── data_v2/                      ← FUENTE PRINCIPAL DE DATOS (aquí trabajamos)
│   ├── matriz_consolidada_paises_atributos.csv   ← 86 países × 366 atributos (matriz bruta)
│   ├── matriz_limpia.csv                         ← ~120-140 atributos × 86 países (post-limpieza)
│   ├── matriz_core_A.csv                         ← 100% denso: ~24 vars × 86 países
│   ├── matriz_core_B.csv                         ← ≥95% denso: ~31 vars × 82 países
│   ├── matriz_core_C.csv                         ← ≥80% denso: ~37 vars × 73 países
│   ├── matriz_dense_62pais.csv                   ← submatriz densa 62 países
│   ├── metadata_atributos.csv                    ← diccionario completo de atributos
│   ├── {ISO3}/                                   ← carpeta por cada uno de los 86 países
│   │   ├── atributos_completos.csv               ← todos los atributos del país
│   │   ├── atributos_transpuesto.csv             ← mismo dato, orientación transpuesta
│   │   └── HALLAZGOS_CLAVE.md                    ← análisis narrativo del país
│   ├── EDA_PLAN.md                               ← plan detallado del EDA (21 figuras)
│   ├── PLAN_EXTRACCION_MATRIZ_DATOS.md           ← plan de extracción y convenciones
│   ├── eda_legal_ai.ipynb                        ← notebook EDA principal
│   ├── EDA_Legal_IA_Matriz_Diccionario_V2.xlsx   ← diccionario Excel con metadatos
│   ├── eda_completitud_atributos.csv             ← completitud por atributo
│   ├── eda_completitud_paises.csv                ← completitud por país
│   ├── eda_correlaciones_fuertes.csv             ← pares con |r| > 0.5
│   ├── eda_outliers_univariados.csv              ← outliers por z-score
│   ├── cluster_profiles.csv                      ← perfiles de 2 clusters K-means
│   ├── regression_model1_results.csv             ← modelo 1: Y=iapp_regulatory_intensity
│   ├── regression_model2_results.csv             ← modelo 2: Y=ms_ai_user_share_h2_2025
│   └── DEU_FRA_GBR_CHN_HALLAZGOS.md             ← perfil comparativo 4 países clave
│
├── ARCHIVOS_MD_CONTEXTO/         ← documentación metodológica (consultar solo si necesario)
├── ADE/                          ← análisis exploratorio de documentos legales (ADE/NLP)
├── docs/                         ← informes, guías, briefings
├── data/                         ← datos legados (NO usar, reemplazado por data_v2)
├── src/                          ← scripts de scraping/ETL
├── notebooks/                    ← notebooks legados
└── context_llm/                  ← este archivo y documentación LLM
```

---

## 3. El dataset definitivo: `data_v2/`

### 3.1 Matriz bruta: `matriz_consolidada_paises_atributos.csv`

- **86 filas** = 86 países de la muestra (identificados por `iso3`)
- **366 columnas** = todos los atributos extraídos de 10 fuentes
- Contiene columnas raw sin limpiar (duplicados, NAs, metadatos descriptivos)

### 3.2 Matriz limpia: `matriz_limpia.csv`

Post-limpieza según `EDA_PLAN.md` sección 1:
- **~120-140 atributos** × **86 países**
- Eliminadas: columnas con 0 datos, metadatos descriptivos, duplicadas, Stanford <5% completitud
- Colapsadas: variantes temporales WB → una columna por métrica (año más reciente)
- Añadidas: variables codificadas (dummies + ordinales)

### 3.3 Submatrices densas

| Submatriz | Criterio | Variables aprox. | Países | Uso principal |
|-----------|----------|-----------------|--------|---------------|
| `matriz_core_A.csv` | 100% completitud | ~24 | 86 | Correlación sin NAs |
| `matriz_core_B.csv` | ≥95% completitud | ~31 | 82 | Análisis principal (pierde BLZ, TWN) |
| `matriz_core_C.csv` | ≥80% completitud | ~37 | 73 | Incluye Microsoft adoption (pierde 13 sin MS) |

**Core B es la submatriz de análisis principal** para regresión y PCA.

### 3.4 Estructura por país

Cada uno de los 86 países tiene su carpeta `data_v2/{ISO3}/` con:
- `atributos_completos.csv` — todos sus valores
- `HALLAZGOS_CLAVE.md` — análisis narrativo con interpretaciones

**Los 86 países:** ARE, ARG, ARM, AUS, AUT, BEL, BGD, BGR, BHR, BLR, BLZ, BRA, BRB, CAN, CHE, CHL, CHN, CMR, COL, CRI, CYP, CZE, DEU, DNK, ECU, EGY, ESP, EST, FIN, FRA, GBR, GHA, GRC, HRV, HUN, IDN, IND, IRL, ISL, ISR, ITA, JOR, JPN, KAZ, KEN, KOR, LBN, LKA, LTU, LUX, LVA, MAR, MEX, MLT, MNG, MUS, MYS, NGA, NLD, NOR, NZL, PAK, PAN, PER, PHL, POL, PRT, ROU, RUS, SAU, SGP, SRB, SVK, SVN, SWE, SYC, THA, TUN, TUR, TWN, UGA, UKR, URY, USA, VNM, ZAF

---

## 4. Las 10 fuentes y sus prefijos de columna

Cada columna en la matriz lleva un prefijo que identifica su fuente:

| Prefijo | Fuente | Año | Cobertura | Variables clave |
|---------|--------|-----|-----------|-----------------|
| `iapp_` | IAPP Global AI Law & Policy Tracker | 2026-02 | 86/86 | `has_ai_law`, `regulatory_approach`, `regulatory_intensity` (0-10), `enforcement_level`, `thematic_coverage` (0-15) |
| `oxford_` | Oxford Insights Gov. AI Readiness Index | 2025 | 86/86 | `readiness_score` (0-100), `rank`, 6 pilares, 14 dimensiones |
| `ms_` | Microsoft AI for Good / AIEI | H1+H2 2025 | 73/86 | `ms_ai_user_share_h1_2025`, `_h2_2025`, `_change_pp` (% adopción empresarial) |
| `stanford_` | Stanford AI Index 2025 | 2024-2025 | ~50/86 | inversión privada, patentes, talent migration, bills passed, startups |
| `wipo_` | WIPO Global Innovation Index | 2025 | 84/86 | `gii_score` (0-100), `gii_rank`, 7 pilares, PPP per cápita |
| `wb_` | World Bank WDI + WGI | 2022-2024 | 86/86 | GDP, internet, governance indicators (WGI escala -2.5 a 2.5) |
| `fh_` | Freedom House Freedom in the World | 2025 | 84/86 | `fh_total_score` (0-100), `fh_status` (F/PF/NF), PR+CL scores |
| `gdpr_` | DLA Piper Data Protection Laws of the World | 2025 | 84/86 | `has_gdpr_like_law`, `similarity_level` (0-3), `eu_status`, `has_dpa` |
| `legal_` | La Porta et al. 2008 | estático | 86/86 | `legal_origin` (English/French/German/Socialist/Scandinavian), `is_common_law` |
| `oecd_` | OECD AI Policy Observatory | 2024 | ~40/86 | `n_total_initiatives`, `n_binding`, `n_regulations`, `n_strategies` |

### Variables codificadas añadidas en matriz_limpia

| Variable original | Variable codificada | Esquema |
|-------------------|---------------------|---------|
| `iapp_regulatory_approach` | `iapp_approach_ordinal` | none=0, light_touch=1, strategy_led=2, comprehensive=3 |
| `iapp_enforcement_level` | `iapp_enforcement_ordinal` | none=0, low=1, medium=2, high=3 |
| `gdpr_eu_status` | `gdpr_eu_member`, `gdpr_eu_adequacy` | dummies |
| `income_group` | `income_ordinal` | LM=0, UM=1, HI=2 |
| `legal_origin` | `legal_french`, `legal_english`, `legal_socialist`, `legal_german` | dummies |
| `region` | `region_europe`, `region_latam`, `region_mena`, `region_asia`, `region_africa` | dummies |

---

## 5. Variables de investigación (roles analíticos)

### Variables dependientes (Y) — lo que queremos explicar

1. **`iapp_regulatory_intensity`** (0-10) — intensidad regulatoria IA
   - Suma ponderada: existencia ley (0-3) + obligaciones (0-3) + sanciones (0-2) + autoridad (0-2)
   - **Problema crítico:** 27 países EU tienen automáticamente `intensity=10` por el EU AI Act → cluster artificial que infla correlaciones

2. **`ms_ai_user_share_h2_2025`** (%) — adopción de IA generativa en empresas
   - Encuesta Microsoft a decision-makers empresariales, H2 2025
   - Top: ARE (64%), SGP (60.9%), NOR (46.4%), IRL (44.6%), FRA (44%)
   - Solo disponible en 73/86 países

3. **`iapp_regulatory_approach`** (categorical) — enfoque regulatorio
   - none / light_touch / strategy_led / regulation_focused / comprehensive

### Variables independientes (X1) — regulación IA

- `iapp_has_ai_law` (0/1)
- `iapp_regulatory_intensity` (0-10)
- `iapp_thematic_coverage` (0-15)
- `iapp_approach_ordinal` (0-3)
- `iapp_enforcement_ordinal` (0-3)
- `gdpr_gdpr_similarity_level` (0-3)
- `gdpr_has_gdpr_like_law` (0/1)
- `gdpr_eu_member` (dummy)

### Variables de control (X2) — factores estructurales

- `wipo_ppp_per_capita` — PIB PPA per cápita (proxy de desarrollo)
- `wipo_gii_score` — capacidad de innovación
- `oxford_readiness_score` — preparación gubernamental IA
- `wb_regulatory_quality_2023` — calidad institucional
- `wb_rule_of_law_2023` — estado de derecho
- `fh_fh_total_score` — libertades políticas
- `income_ordinal` — grupo de ingreso
- `is_common_law` — sistema jurídico
- `region_*` — dummies regionales

---

## 6. Hallazgos del análisis hasta la fecha (abril 2026)

### 6.1 Regresión Modelo 1: Y = `iapp_regulatory_intensity`

Archivo: `data_v2/regression_model1_results.csv`

| Variable | Coef. | p-valor | Interpretación |
|----------|-------|---------|----------------|
| `wipo_gii_score` | +0.124 | <0.001 | Más innovación → más regulación |
| `income_ordinal` | +1.238 | 0.002 | Países más ricos regulan más |
| `gdpr_eu_eu_member` | **+6.143** | <0.001 | **EU AI Act: efecto dominante** |
| `gdpr_has_gdpr_like_law` | +1.409 | 0.088 | Tendencia positiva (borderline) |
| `wb_regulatory_quality_2023` | -1.175 | 0.056 | Paradoja: mejor calidad → menos IA-ley |

**Hallazgo central:** El coeficiente de `gdpr_eu_eu_member` (+6.14) domina el modelo y distorsiona los resultados. Los análisis deben ejecutarse con y sin los 27 países EU.

### 6.2 Regresión Modelo 2: Y = `ms_ai_user_share_h2_2025` (adopción IA)

Archivo: `data_v2/regression_model2_results.csv`

| Variable | Coef. | p-valor | Interpretación |
|----------|-------|---------|----------------|
| `wipo_gii_score` | +0.679 | <0.001 | Innovación predice adopción fuertemente |
| `region_europe` | -6.479 | 0.020 | Europa adopta menos que otros (controlling for GII) |
| `iapp_regulatory_intensity` | +0.418 | 0.546 | **NO significativo** — regulación no predice adopción |
| `iapp_approach_ordinal` | +1.396 | 0.568 | **NO significativo** |

**Hallazgo central:** La regulación IA no explica significativamente la adopción empresarial de IA. El predictor dominante es la capacidad de innovación general (GII).

### 6.3 Clustering K-means (2 clusters sobre Core A)

Archivo: `data_v2/cluster_profiles.csv`

| Cluster | Reg. Intensity | AI Readiness | GII Score | Gov. Effect. | Income | Descripción |
|---------|---------------|--------------|-----------|--------------|--------|-------------|
| 0 | 8.18 | 70.28 | 50.05 | 1.27 | 1.94 (≈HI) | "Reguladores avanzados" — EU + HI desarrollados |
| 1 | 4.21 | 56.87 | 31.49 | 0.04 | 0.93 (≈UM) | "Ecosistema emergente" — países en desarrollo |

### 6.4 Correlaciones fuertes conocidas (|r| > 0.7)

- `oxford_readiness_score` ↔ `wipo_gii_score`: r ≈ 0.90+ (multicolinealidad latente)
- `wipo_ppp_per_capita` ↔ `oxford_readiness_score`: r ≈ 0.75+
- Países EU: `iapp_regulatory_intensity=10` en el 100% de los casos → cluster artificial

### 6.5 Caso focal: Chile (CHL)

CHL es el caso de referencia del estudio porque encarna la decisión que se está tomando:

| Dimensión | CHL | Interpretación |
|-----------|-----|----------------|
| `iapp_has_ai_law` | 0 | No tiene ley IA vigente (Boletín 16821-19 en tramitación) |
| `iapp_regulatory_approach` | strategy_led | Tiene Política Nacional IA 2021 |
| `iapp_regulatory_intensity` | 4/10 | Bajo-medio |
| `oxford_readiness_score` | 59.3 (#50) | Media global |
| `oxford_pillar_policy_capacity` | 82.94 | Muy alto (voluntad política) |
| `oxford_dimension_compute_capacity` | 18.18 | **Crítico: brecha dramática** |
| `ms_ai_user_share_h2_2025` | 20.8% | Bajo vs. top (ARE 64%, SGP 61%) |
| `wipo_gii_score` | 33.07 (#51) | Último HI de la muestra |
| `wb_gdp_per_capita_ppp_2024` | $36,181 | HI pero bajo para el grupo |
| `fh_fh_total_score` | 94/100 (Free) | Líder democrático LATAM |
| `gdpr_similarity_level` | 2 (sustancial) | Ley 21.719 (2024), enforcement pendiente |
| `stanford_net_ai_talent_migration` | -0.19 | **Fuga de talento IA** |

**La tensión central de CHL:** Policy vision 100/100 pero compute capacity 18/100. Voluntad institucional excepcional pero ecosistema IA débil. Aprobar una ley robusta sin infraestructura ni enforcement puede crear obligaciones sin los medios de cumplirlas.

---

## 7. El plan EDA: `data_v2/EDA_PLAN.md`

El EDA está planificado en 7 secciones con **21 figuras** en `data_v2/eda_legal_ai.ipynb`:

| Sección | Contenido | Archivos de salida |
|---------|-----------|-------------------|
| 1. Limpieza | Eliminar columnas vacías/meta, colapsar WB, codificar categóricas | `matriz_limpia.csv` |
| 2. Análisis de NA | Completitud por atributo y país, heatmaps, correlación de NA | `eda_completitud_*.csv`, fig_01-06 |
| 3. Submatrices | Construir Core A/B/C, validar distribuciones | `matriz_core_*.csv`, fig_07 |
| 4. Correlación | Pearson (Core B), Cramer V (categóricas), parciales, EU vs non-EU | `eda_correlaciones_fuertes.csv`, fig_08-12 |
| 5. Outliers | Z-score, Mahalanobis, Isolation Forest, regulatory over/underperformers, adoption paradox | `eda_outliers_univariados.csv`, fig_13-18 |
| 6. PCA | Scree plot, biplot PC1 vs PC2, loadings PC1-PC5 | fig_19-21 |
| 7. Resumen | Tabla hallazgos, outliers flaggeados, limitaciones, next steps | — |

### Limitaciones críticas a tener siempre presentes

1. **EU cluster artificial:** 27 países EU tienen `regulatory_intensity=10` por el EU AI Act → siempre correr modelos con y sin EU
2. **Microsoft adoption:** 13 países sin dato (micro-estados, algunos EU pequeños, TWN, BLZ) → sesgo de selección
3. **Stanford baja cobertura:** ~50/86 países, USA y CHN dominan → excluir de correlación principal
4. **WIPO:** BLZ y TWN sin GII → excluidos de Core B
5. **Causalidad:** Correlación NO implica causalidad; regulación-adopción es relación endógena
6. **Cross-section:** Solo 1 año de datos → no se pueden inferir dinámicas causales

---

## 8. Siguientes pasos del proyecto (al 2026-04-29)

- [ ] Completar el notebook `eda_legal_ai.ipynb` con las 21 figuras del EDA_PLAN
- [ ] Correr modelos de regresión OLS con y sin EU (robustez)
- [ ] Análisis de clustering (K-means + hierarchical) sobre Core B
- [ ] Modelo con dummy de EU membership como control explícito
- [ ] Incorporar datos del corpus legal (ADE/NLP) como variables textuales
- [ ] Radar chart comparativo: CHL vs SGP vs DEU vs USA vs CHN
- [ ] Adoption paradox: cuadrante regulación × adopción

---

## 9. Documentos clave de referencia (leer si se necesita más detalle)

| Documento | Ruta | Contenido |
|-----------|------|-----------|
| EDA Plan completo | `data_v2/EDA_PLAN.md` | 21 figuras con código Python exacto |
| Plan extracción | `data_v2/PLAN_EXTRACCION_MATRIZ_DATOS.md` | Convenciones de nombres y fuentes |
| Diccionario atributos | `data_v2/metadata_atributos.csv` | 136 atributos del dataset "limpio objetivo" con descripción, fuente, año, tipo |
| Perfil Chile | `data_v2/CHL/HALLAZGOS_CLAVE.md` | Análisis profundo del caso focal |
| Perfil DEU/FRA/GBR/CHN | `data_v2/DEU_FRA_GBR_CHN_HALLAZGOS.md` | Países de contraste clave |
| Propuesta original | `context_llm/PROYECTO DATASCIENCE .md` | Pregunta de investigación, cronograma |
| DATA_DECISIONS_LOG | `ARCHIVOS_MD_CONTEXTO/DATA_DECISIONS_LOG.md` | Decisiones de diseño y sus motivos |
| GUIA_VARIABLES_ETL | `ARCHIVOS_MD_CONTEXTO/GUIA_VARIABLES_ESTUDIO_ETL.md` | Metodología detallada |
| Informe corpus | `docs/INFORME_EJECUTIVO_CORPUS_LEGAL_SENADO.md` | Informe para el Senado chileno |

---

## 10. Entorno técnico

- **Python:** pandas, numpy, matplotlib, seaborn, scipy, sklearn, statsmodels
- **Entorno:** Jupyter Notebook (`.ipynb`), VSCode con extensión Jupyter
- **Working directory:** `/home/pablo/Research_LeyIA_DataScience/`
- **Dataset principal:** `data_v2/matriz_consolidada_paises_atributos.csv` (86 × 366)
- **Dataset de análisis:** `data_v2/matriz_core_B.csv` (82 × ~31, ≥95% denso)
- **Identificador de países:** `iso3` (ISO 3166-1 alpha-3)

### Convenciones de nombres de columnas

```
{prefijo_fuente}_{nombre_atributo}
# Ejemplos:
iapp_regulatory_intensity
oxford_readiness_score
ms_ai_user_share_h2_2025
wipo_gii_score
wb_government_effectiveness_2023
fh_fh_total_score        ← doble prefijo porque así quedó en la extracción
gdpr_gdpr_similarity_level  ← ídem
```

---

## 11. Orientación para tareas comunes

**Si te piden trabajar con el dataset:**
→ Cargar `data_v2/matriz_consolidada_paises_atributos.csv` como punto de partida
→ Para análisis, usar `data_v2/matriz_core_B.csv` directamente

**Si te piden explorar un país específico:**
→ Leer `data_v2/{ISO3}/HALLAZGOS_CLAVE.md` (ya procesado y analizado)

**Si te piden entender un atributo:**
→ Consultar `data_v2/metadata_atributos.csv` (columnas: atributo, fuente, descripcion, año, tipo)

**Si te piden continuar el EDA:**
→ El plan está en `data_v2/EDA_PLAN.md` con código Python exacto por sección

**Si te piden comparar regulación:**
→ Variables clave: `iapp_regulatory_intensity`, `iapp_regulatory_approach`, `gdpr_gdpr_similarity_level`, `gdpr_eu_status`
→ Siempre controlar por `income_ordinal`, `wipo_gii_score`, `gdpr_eu_member`

**Si te piden hablar del caso Chile:**
→ Chile (CHL) es el focal case: no tiene ley IA, tiene Boletín 16821-19 en tramitación, alta voluntad política pero baja infraestructura de cómputo

**Si el análisis incluye países EU:**
→ Advertir que los 27 países EU tienen `iapp_regulatory_intensity=10` por el EU AI Act → siempre hacer análisis con/sin EU

---

*Este documento fue generado el 2026-04-29 para proveer contexto persistente a futuros asistentes LLM trabajando en este proyecto.*
