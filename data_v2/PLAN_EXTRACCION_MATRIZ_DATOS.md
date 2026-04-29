# Plan de Extracción Estandarizada - Matriz de Datos País × Atributo

## Proyecto: LeyIA DataScience  
## Objetivo: Generar matriz consolidada de 86 países × atributos de fuentesconfiables  
## Exclusiones: legal_corpus (carpeta excluida deliberadamente)  
## Fecha: 2026-04-28

---

## 1. Alcance y Principios

### 1.1 Estructura objetivo

- **Filas (N)**: 86 países de la muestra autoritativa
- **Columnas (M)**: Todos los atributos obtainable de cada fuente confiable
- **Valor por celda**: Valor observado o NA si no disponible
- **Metadatos por columna**: `{nombre_attr}_{fuente}_{año}` para trazabilidad completa

### 1.2 Principios de diseño

1. **Trazabilidad completa**: Cada atributo debe responder a las preguntas:
   - ¿De qué documento fuente proviene?
   - ¿Qué significa exactamente?
   - ¿Qué año/grabación representa?
   
2. **Sin jerarquía X1/Y/X2**: No categorizamos como variables independientes o dependientes.
   Cada atributo es un "hecho observado" de un estudio específico.

3. **Matriz densa**: Preferimos muchos atributos con NA a pocos con NA mínimos.
   La completitud se evalúa post-extracción.

4. **Un atributo = una columna**: No resumir, no agregar, no consolidar en fase de extracción.
   Consolidación es fase de análisis.

### 1.3 Fuentes incluidas (10 carpetas)

| Carpeta | Contenido | Atributos objetivo |
|--------|----------|------------------|
| `IAPP/` | IAPP Global AI Law & Policy Tracker | Regulación IA, enfoque, intensidad, enforcement, cobertura temáticas |
| `Oxford Insights/` | Government AI Readiness Index 2025 | Índices compuestos, indicadores por dimensión, rankings |
| `Microsoft/` | AI Diffusion Study | Tasas de adopción IA empresarial |
| `STANFORD AI INDEX 25/` | AI Index Report 2025 (cap. 1, 4, 6) | Inversión privada, startups, patentes, publicaciones |
| `WIPO Global Innovation Index/` | GII 2025 | Scores de innovación, rankings, indicadores de input/output |
| `World Bank WDI/` | World Development Indicators | GDP, infraestructura, gobernanza, capital humano |
| `FreedomHouse/` | Freedom in the World 2025 | Scores liberties, status político |
| `GDPR_coding/` | GDPR-Like Laws (DLA Piper) | Leyes protección datos, similitud GDPR |
| `LegalOrigin/` | Legal Origins (La Porta 2008) | Familia jurídica |
| `OECD/` | OECD AI Policy Initiatives | Iniciativas de política IA |

---

## 2. Inventario de Atributos por Fuente

### 2.1 IAPP — Regulación IA

**Fuente primaria**: `data/raw/IAPP/iapp_x1_core.csv`  
**Versión**: Feb 2026 (IAPP Global AI Law & Policy Tracker)  
**Cobertura**: 86 países

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `iapp_has_ai_law` | `iapp_has_ai_law` | integer (0/1) | ¿Existe ley IA específica vinculante? | IAPP |
| `iapp_regulatory_approach` | `iapp_regulatory_approach` | categorical | none / light_touch / strategy_led / comprehensive | IAPP |
| `iapp_regulatory_intensity` | `iapp_regulatory_intensity` | integer (0-10) | Intensidad regulatoria calculada por IAPP | IAPP |
| `iapp_year_enacted` | `iapp_year_enacted` | float | Año promulgación ley principal (NULL si no hay ley) | IAPP |
| `iapp_enforcement_level` | `iapp_enforcement_level` | categorical | none / low / medium / high | IAPP |
| `iapp_thematic_coverage` | `iapp_thematic_coverage` | integer (0-15) | Número de temas regulatorios cubiertos | IAPP |
| `iapp_evidence_summary` | `iapp_evidence_summary` | text | Resumen cualitativo de la regulación | IAPP |
| `iapp_source` | `iapp_source` | string | Tracker o supplementary | IAPP |
| `iapp_source_date` | `iapp_source_date` | string (YYYY-MM) | Fecha de versión del tracker | IAPP |

**Fuente secundaria**: `data/raw/IAPP/iapp_all_coded.csv`  
**Contiene**: Muestra extendida IAPP con campos adicionales

**Notas de extracción**:
- Para países EU (27): `has_ai_law=1`, `year_enacted=2024`, `approach=comprehensive`
- Significado `regulatory_intensity`:
  - Existencia ley: 0-3 puntos
  - Obligaciones concretas: 0-3 puntos
  - Sanciones: 0-2 puntos
  - Autoridad competente: 0-2 puntos

---

### 2.2 Oxford Insights — Government AI Readiness Index

**Fuente primaria**: `data/raw/Oxford Insights/oxford_ai_readiness_snapshot_latest.csv`  
**Versión**: 2025  
**Cobertura**: ~195 países  
**Metodología**: https://oxfordinsights.com Methodology Report 2025

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `oxford_rank` | `oxford_rank` | integer | Ranking reportado por Oxford | Oxford 2025 |
| `oxford_readiness_score` | `oxford_readiness_score` | float (0-100) | Índice compuesto de preparación | Oxford 2025 |
| `oxford_cluster_governance` | `oxford_cluster_governance` | float | Promedio cluster Governance & Ethics | Oxford 2025 |
| `oxford_cluster_infrastructure` | `oxford_cluster_infrastructure_and_data` | float | Promedio cluster Infrastructure & Data | Oxford 2025 |
| `oxford_cluster_skills` | `oxford_cluster_skills_and_education` | float | Promedio cluster Skills & Education | Oxford 2025 |
| `oxford_cluster_public_services` | `oxford_cluster_government_and_public_services` | float | Promedio cluster Gov & Public Services | Oxford 2025 |
| `oxford_indicator_privacy_laws` | `oxford_indicator_privacy_laws` | float (raw) | Indicador: privacy laws | Oxford 2025 |
| `oxford_indicator_ai_strategy` | `oxford_indicator_ai_strategy` | float (raw) | Indicador: AI strategy | Oxford 2025 |
| `oxford_indicator_data_availability` | `oxford_indicator_data_availability` | float (raw) | Indicador: data availability | Oxford 2025 |
| `oxford_indicator_ai_startups` | `oxford_indicator_ai_startups` | float (raw) | Indicador: AI startups | Oxford 2025 |
| `oxford_indicator_log_ai_startups` | `oxford_indicator_log_ai_startups` | float | Log(AI startups) | Oxford 2025 |
| `oxford_indicator_digital_public_services` | `oxford_indicator_digital_public_services` | float (raw) | Indicador: digital public services | Oxford 2025 |
| `oxford_indicator_gov_effectiveness` | `oxford_indicator_effectiveness_of_government` | float (raw) | Indicador: government effectiveness | Oxford 2025 |
| `oxford_indicator_tech_skills` | `oxford_indicator_technology_skills` | float (raw) | Indicador: technology skills | Oxford 2025 |
| `oxford_indicator_private_innovation` | `oxford_indicator_private_sector_innovation_capability` | float (raw) | Indicador: private sector innovation | Oxford 2025 |
| `oxford_indicator_procurement` | `oxford_indicator_govt_procurement_advanced_technology_products` | float (raw) | Indicador: govt procurement | Oxford 2025 |
| `oxford_indicator_data_capability_gov` | `oxford_indicator_data_capability_in_government` | float (raw) | Indicador: data capability in gov | Oxford 2025 |
| `oxford_indicator_ict_vision` | `oxford_indicator_importance_of_icts_to_government_vision_of_future` | float (raw) | Indicador: ICT importance in vision | Oxford 2025 |

**Fuente extendida**: `data/raw/Oxford Insights/oxford_ai_readiness_wide.csv`  
**Contiene**: Formato wide con todos los indicadores por país

**Notas de extracción**:
- Escala 0-100
- 6 pilares: Government, Technology Sector, Data & Infrastructure, Skills & Education, Government & Public Services, Development & Diffusion
- 14 dimensiones del índice
- Ver: `oxford_ai_readiness_study.csv` para metadata detallado

---

### 2.3 Microsoft AI for Good Institute — AI Diffusion

**Fuente primaria**: `data/raw/Microsoft/microsoft_ai_diffusion_study.csv`  
**Versión**: H1_2025 + H2_2025  
**Cobertura**: 76 países  
**Metodología**: Encuesta a tomadores de decisiones empresariales

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `ms_ai_adoption_h1_2025` | `ms_ai_user_share_h1_2025` | float (%) | Porcentaje adopción H1 2025 | Microsoft AIEI |
| `ms_ai_adoption_h2_2025` | `ms_ai_user_share_h2_2025` | float (%) | Porcentaje adopción H2 2025 | Microsoft AIEI |
| `ms_ai_adoption_change_pp` | `ms_ai_user_share_change_pp` | float (pp) | Cambio H1→H2 en puntos porcentuales | Microsoft AIEI |
| `ms_report_edition` | `ms_report_edition` | string | Edición del reporte | Microsoft AIEI |

**Fuente extendida**: `data/raw/Microsoft/microsoft_ai_diffusion_snapshot.csv`  
**Contiene**: Snapshot de adopción por país

**Fuente panel**: `data/raw/Microsoft/microsoft_ai_adoption_panel.csv`  
**Contiene**: Panel histórico de adopción (si existe serie temporal)

**Notas de extracción**:
- Pregunta de encuesta: "¿Usa IA generativa en su trabajo?"
- Muestra sesgada a empresas grandes y países con adopción temprana
- Los 10 primeros: ARE (64%), SGP (60.9%), NOR (46.4%), IRL (44.6%), FRA (44%), ESP (41.8%), NZL (40.5%), NLD (38.9%), GBR (38.9%)

---

### 2.4 Stanford AI Index Report 2025

**Carpeta**: `data/raw/STANFORD AI INDEX 25/`  
**Versión**: 2025  
**Cobertura**: ~80 países

#### 2.4.1 Capítulo 4 — Economía

**Carpeta**: `4. Economy/Data/`

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `stanford_ai_investment_2013_2024` | `stanford_fig_4_3_9` | float (USD billions) | Inversión privada IA acumulada 2013-2024 | Stanford Fig. 4.3.9 |
| `stanford_ai_startups_count` | `stanford_fig_4_3_10` | integer | Número de startups IA activas | Stanford Fig. 4.3.10 |
| `stanford_ai_investment_2024` | `stanford_fig_4_2_14` | float (USD billions) | Inversión privada 2024 | Stanford Fig. 4.2.14 |
| `stanford_ai_incubators` | `stanford_fig_4_2_15` | integer | Número de incubators/accelerators | Stanford Fig. 4.2.15 |
| `stanford_ai_corporate_investment` | `stanford_fig_4_2_16` | float (USD billions) | Inversión corporativa IA | Stanford Fig. 4.2.16 |
| `stanford_ai_deals` | `stanford_fig_4_2_17` | integer | Número de deals M&A | Stanford Fig. 4.2.17 |
| `stanford_ai_total_funding` | `stanford_fig_4_2_18` | float | Funding total IA | Stanford Fig. 4.2.18 |
| `stanford_private_investment_by_country` | `stanford_fig_4_2_19` | float | Inversión privada por país (detallado) | Stanford Fig. 4.2.19 |

#### 2.4.2 Capítulo 1 — Research & Development

**Carpeta**: `1. Research and Development/Data/`

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `stanford_ai_publications_global` | `stanford_fig_1_2_1` | integer | Publicaciones IA a nivel global | Stanford Fig. 1.2.1 |
| `stanford_ai_citations` | `stanford_fig_1_2_2` | integer | Citas de publicaciones IA | Stanford Fig. 1.2.2 |
| `stanford_language_model_performance` | `stanford_fig_1_3_1` | float | Performance en benchmarks | Stanford Fig. 1.3.1 |

**Notas de extracción**:
- Figuras principales de inversión: 4.3.9, 4.2.14, 4.2.19
- USA domina con ~60-70% del total mundial
- China ~15%
- Resto del mundo fragmentado

---

### 2.5 WIPO Global Innovation Index

**Fuente primaria**: `data/raw/WIPO Global Innovation Index/wipo_gii_snapshot_latest.csv`  
**Versión**: 2025  
**Cobertura**: ~130 países

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `wipo_gii_rank` | `wipo_gii_rank` | integer | Ranking GII | WIPO 2025 |
| `wipo_gii_score` | `wipo_gii_score` | float (0-100) | Score Global Innovation Index | WIPO 2025 |
| `wipo_income_group` | `wipo_income_group_wipo` | categorical | HI / UM / LM / LI | WIPO 2025 |
| `wipo_region` | `wipo_region_un` | string | Región ONU | WIPO 2025 |

**Indicadores derivados (en formato long)**: `wipo_gii_all_raw.csv`  
**Contiene**: 109 indicadores individuales

| Atributo en matriz | Nombre columna (indicador) | Tipo | Descripción | Origen |
|-------------------|-------------------------|------|--------------|--------|
| `wipo_innovation_input_subindex` | `wipo_innovation_input_subindex` | float | Subíndice de Input | WIPO 2025 |
| `wipo_innovation_output_subindex` | `wipo_innovation_output_subindex` | float | Subíndice de Output | WIPO 2025 |
| `wipo_patents_by_origin` | `wipo_patents_by_origin` | integer | Patentes solicitadas por residentes | WIPO 2025 |
| `wipo_utility_models` | `wipo_utility_models` | integer | Modelos de utilidad | WIPO 2025 |
| `wipo_scientific_publications` | `wipo_scientific_publications` | integer | Publicaciones científicas | WIPO 2025 |
| `wipo_ipsh_per_million` | `wipo_ipsh_per_million` | integer | Solicitudes de propiedad industrial por millón | WIPO 2025 |
| `wipo_tertiary_enrollment` | `wipo_tertiary_enrollment` | float (%) | Matriculación terciaria | WIPO 2025 |
| `wipo_rd_expenditure_gdp` | `wipo_rd_expenditure_gdp` | float (%) | Gasto I+D como % del PIB | WIPO 2025 |
| `wipo_researchers_fulltime` | `wipo_researchers_fulltime` | integer | Investigadores en equivalencia tiempo completo | WIPO 2025 |
| `wipo_gerd_per_population` | `wipo_gerd_per_population` | float | GASTOS EN I+D PER CAPITA | WIPO 2025 |
| `wipo_global brand_value` | `wipo_global_brand_value` | float | Valor de marcas globales | WIPO 2025 |
| `wipo_exports_high_tech` | `wipo_exports_high_tech` | float (%) | Exportaciones Alta Tecnología | WIPO 2025 |

**Panel histórico**: `wipo_gii_overall_panel.csv`  
**Contiene**: Serie temporal de GII por país

**Notas de extracción**:
- 7 pilares: Institutions, Human capital & research, Infrastructure, Market sophistication, Business sophistication, Knowledge & technology outputs, Creative outputs
- Top 2025: Switzerland (67.5), Sweden (56.1), USA (55.9), UK (55.7), Korea (55.1)
- América Latina: Chile (49), México (58), Brasil (67), Colombia (69), Argentina (77), Perú (89)

---

### 2.6 World Bank World Development Indicators

**Carpeta**: `data/raw/World Bank WDI/`  
**Versión**: 2024-2025  
**Cobertura**: ~200 países

#### 2.6.1 Controles principales

**Archivo**: `data/raw/World Bank WDI/wdi_core_controls.csv`

| Atributo en matriz | Nombre columna | Tipo | Código WB | Descripción | Origen |
|-------------------|----------------|------|---------|-------------|--------|
| `wb_gdp_per_capita_ppp` | `wb_gdp_per_capita_ppp` | float | NY.GDP.PCAP.PP.CD | PIB per cápita PPA (USD constantes) | WB WDI |

**Archivo**: `data/raw/World Bank WDI/digital_economy_86.csv`

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `wb_internet_penetration` | `wb_internet_penetration` | float (%) | Penetración de internet | WB WDI |
| `wb_mobile_subscriptions` | `wb_mobile_subscriptions` | float | Suscripciones móviles por 100 hab | WB WDI |
| `wb_ict_service_exports` | `wb_ict_service_exports_pct` | float (%) | Exportaciones servicios ICT | WB WDI |
| `wb_high_tech_exports` | `wb_high_tech_exports_pct` | float (%) | Exportaciones Alta Tecnología | WB WDI |

#### 2.6.2 Gobernanza (WGI)

**Archivo**: `data/raw/World Bank WDI/wdi_governance.csv`

| Atributo en matriz | Nombre columna | Tipo | Código WB | Descripción | Origen |
|-------------------|----------------|------|---------|-------------|--------|
| `wb_regulatory_quality` | `wb_regulatory_quality` | float | WV.GEN.GNDS | Calidad regulatoria | WB WGI |
| `wb_rule_of_law` | `wb_rule_of_law` | float | WV.RLLE | Estado de derecho | WB WGI |
| `wb_gov_effectiveness` | `wb_government_effectiveness` | float | WV.GELE | Efectividad gubernamental | WB WGI |
| `wb_corruption_control` | `wb_control_of_corruption` | float | WV.CC | Control de corrupción | WB WGI |
| `wb_voice_accountability` | `wb_voice_and_accountability` | float | WV.VA | Voz y rendición de cuentas | WB WGI |
| `wb_political_stability` | `wb_political_stability_no_violence` | float |WV.PS | Estabilidad política | WB WGI |

#### 2.6.3 Estructura económica

**Archivo**: `data/raw/World Bank WDI/wdi_economic_structure.csv`

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `wb_industry_value_added` | `wb_industry_value_added_gdp` | float (%) | Valor agregado industrial | WB WDI |
| `wb_services_value_added` | `wb_services_value_added_gdp` | float (%) | Valor agregado servicios | WB WDI |
| `wb_manufacturing_value_added` | `wb_manufacturing_value_added_gdp` | float (%) | Valor agregado manufacturas | WB WDI |
| `wb_employment_industry` | `wb_employment_in_industry_pct` | float (%) | Empleo en industria | WB WDI |
| `wb_gdp_current_usd` | `wb_gdp_current_usd` | float | PIB actual USD | WB WDI |
| `wb_trade_gdp` | `wb_trade_gdp` | float (%) | Comercio como % del PIB | WB WDI |

#### 2.6.4 Capital humano

**Archivo**: `data/raw/World Bank WDI/wdi_human_capital_infra.csv`

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `wb_tertiary_enrollment` | `wb_tertiary_enrollment_rate` | float (%) | Matriculación terciaria | WB WDI |
| `wb_school_life_expectancy` | `wb_school_life_expectancy` | float | Esperanza de vida escolar | WB WDI |
| `wb_primary_completion_rate` | `wb_primary_completion_rate` | float (%) | Tasa finalización primaria | WB WDI |
| `wb_health_expenditure_gdp` | `wb_health_expenditure_gdp` | float (%) | Gasto en salud % PIB | WB WDI |

#### 2.6.5 Expansión 2022-2023

**Archivo**: `data/raw/World Bank WDI/wdi_expansion_22.csv`

**Contiene**: Indicadores adicionales de WGI para completeness

**Notas de extracción**:
- Window temporal: usar 2022-2023 como base
- Imputar para países con datos faltantes usando serie temporal del país
- Todos los códigos WB siguen convención `NY.`, `SP.`, `IC.`, etc.

---

### 2.7 Freedom House — Freedom in the World

**Fuente primaria**: `data/raw/FreedomHouse/freedom_in_the_world_2025.csv`  
**Versión**: 2025 (datos año 2024)  
**Cobertura**: ~195 países

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `fh_status` | `fh_status` | categorical | F / PF / NF (Free / Partially Free / Not Free) | FH 2025 |
| `fh_total_score` | `fh_total_score` | integer (0-100) | Score total (100=most free) | FH 2025 |
| `fh_political_rights` | `fh_pr_score` | integer (0-60) | Political Rights score | FH 2025 |
| `fh_civil_liberties` | `fh_cl_score` | integer (0-40) | Civil Liberties score | FH 2025 |
| `fh_year` | `fh_year` | integer | Año del informe | FH 2025 |

**Interpretación**:
- F (Free): 70-100 puntos
- PF (Partially Free): 40-69 puntos
- NF (Not Free): 0-39 puntos

**Ejemplos**:
- Chile: F (95)
- Argentina: F (84)
- Brasil: F (72)
- México: F (72)
- Venezuela: NF (30)
- China: NF (9)

---

### 2.8 GDPR Coding (DLA Piper)

**Fuente primaria**: `data/raw/GDPR_coding/gdpr_like_coding.csv`  
**Versión**: 2025  
**Cobertura**: 86 países

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `gdpr_has_law` | `gdpr_has_gdpr_like_law` | integer (0/1) | ¿Tiene ley de protección de datos? | DLA Piper |
| `gdpr_similarity_level` | `gdpr_similarity_level` | integer (0-3) | Nivel de similitud GDPR | DLA Piper |
| `gdpr_law_name` | `gdpr_law_name` | string | Nombre de la ley de datos | DLA Piper |
| `gdpr_law_year` | `gdpr_law_year` | integer | Año de promulgación | DLA Piper |
| `gdpr_has_authority` | `gdpr_has_dpa` | integer (0/1) | ¿Tiene autoridad de protección de datos? | DLA Piper |
| `gdpr_eu_status` | `gdpr_eu_status` | categorical | eu_member / adequacy / none | DLA Piper |
| `gdpr_enforcement_active` | `gdpr_enforcement_active` | integer (0/1) | ¿ Enforcement activo? | DLA Piper |

**Escala similarity_level**:
- 0: Ninguna ley
- 1: Parcial
- 2: Sustancial (similar a GDPR)
- 3: Equivalente / adaptada (ej: Argentina, Uruguay, Andorra, etc.)

**Ejemplos**:
- Argentina: similarity=3 (ley 25.326, EU adequacy 2003)
- Chile: similarity=1 (ley 19628, partial)
- México: similarity=2 (LFPDPPP 2010)
- Brasil: similarity=2 (LGPD 2018)

---

### 2.9 Legal Origin (La Porta 2008)

**Fuente primaria**: `data/raw/LegalOrigin/legal_origin_coding.csv`  
**Versión**: 2008 + actualizaciones  
**Cobertura**: 86 países

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `legal_origin` | `legal_origin` | categorical | English / French / German / Socialist / Scandinavian | La Porta 2008 |
| `is_common_law` | `is_common_law` | integer (0/1) | ¿Sistema common law? | La Porta 2008 |
| `legal_origin_notes` | `legal_origin_source_notes` | text | Notas sobre origen legal | La Porta 2008 |

**Familias jurídicas**:
- English: Common law (UK, USA, Australia, India, etc.)
- French: Civil code francesa (Francia, Italia, España, LATAM)
- German: Civil code germánica (Alemania, Austria, Suiza)
- Socialist: Ex-socialista (China, Vietnam, Europa Oriental)
- Scandinavian: Derecho nórdico (Suecia, Noruega, Dinamarca)

**Importancia**: Los países common law típicamente regulan menos tecnología que civil law

---

### 2.10 OECD AI Policy Initiatives

**Fuente primaria**: `data/raw/OECD/oecd_ai_policy_initiatives_study.csv`  
**Versión**: 2024  
**Cobertura**: ~40 países

| Atributo en matriz | Nombre columna | Tipo | Descripción | Origen |
|-------------------|----------------|------|--------------|--------|
| `oecd_n_initiatives` | `oecd_count_initiatives` | integer | Número total de iniciativas políticas | OECD.AI |
| `oecd_has_national_strategy` | `oecd_has_strategy` | integer (0/1) | ¿Tiene estrategia nacional IA? | OECD.AI |
| `oecd_has_regulation` | `oecd_has_ai_regulation` | integer (0/1) | ¿Tiene regulación IA? | OECD.AI |
| `oecd_first_initiative_year` | `oecd_first_year` | integer | Año de primera iniciativa | OECD.AI |

**Archivo de iniciativas por país**: `oecd_ai_country_profiles.csv`  
**Contiene**: Perfiles por país con iniciativas específicas

**Notas de extracción**:
- Útil para cross-check con IAPP
- OECD.AI Policy Observatory es fuente oficial

---

## 3. Procedimiento de Extracción

### 3.1 Paso 1: Cargar países objetivo

```
# Leer lista de 86 países
# Fuente: data/interim/sample_ready_cross_section.csv (columna iso3)
# Output: lista_paises.csv
```

**Validar**: Asegurar que cada fuente tiene ISO3 como identificador

### 3.2 Paso 2: Por cada fuente

```
PARA CADA carpeta en data/raw:
    1. Identificar archivo(s) principal(es)
    2. Mapear atributos a nombres de columna estandarizados
    3. LEFT JOIN con lista_paises por iso3
    4. Completar con NA donde no hay dato
    5. Guardar como {fuente}_matriz.csv
    6. Documentar columnas en metadata
```

### 3.3 Paso 3: Merge horizontal

```
# Merge de todas las fuentes por iso3
# Input: {fuente}_matriz.csv para cada fuente
# Output: data_collection/matriz_consolidada_paises_atributos.csv
```

### 3.4 Paso 4: Validación

```
1. Verificar que cada país tiene iso3
2. Contar NA por columna y por fila
3. Generar reporte de completitud
4. Documentar limitaciones
```

---

## 4. Convenciones de Nombres

### 4.1 Prefijos por fuente

| Fuente | Prefijo |
|--------|--------|
| IAPP | `iapp_` |
| Oxford Insights | `oxford_` |
| Microsoft | `ms_` |
| Stanford AI Index | `stanford_` |
| WIPO GII | `wipo_` |
| World Bank WDI | `wb_` |
| Freedom House | `fh_` |
| GDPR Coding | `gdpr_` |
| Legal Origin | `legal_` |
| OECD | `oecd_` |

### 4.2 Formato de nombres

- Minúsculas con guiones bajos: `ai_readiness_score`
- Nombres descriptivos: `regulatory_quality` no `rq`
- Años incluido: `ms_ai_adoption_h1_2025` no `ms_adoption`
- Prefijo de fuente obligatorio: `oxford_`, no `readiness_`

### 4.3 Metadatos obligatorios por columna

Cada columna en la matriz debe incluir:

```
{columna}_source: Nombre del archivo fuente
{columna}_description: Significado exacto del atributo
{columna}_year: Año de la fuente / año del dato
{columna}_original_name: Nombre original en la fuente
```

**Ejemplo**:
```
oxford_readiness_score_source: oxford_ai_readiness_snapshot_latest.csv
oxford_readiness_score_description:Índice compuesto de preparación gubernamental para IA
oxford_readiness_score_year: 2025
oxford_readiness_score_original_name: ai_readiness_score
```

---

## 5. Estructura de Salida

### 5.1 Directorio data_collection/

```
data_collection/
├── matriz_consolidada_paises_atributos.csv
├── metadata_columnas.csv
├── fuentes/
│   ├── iapp_matriz.csv
│   ├── oxford_matriz.csv
│   ├── microsoft_matriz.csv
│   ├── stanford_matriz.csv
│   ├── wipo_matriz.csv
│   ├── wb_matriz.csv
│   ├── freedomhouse_matriz.csv
│   ├── gdpr_matriz.csv
│   ├── legalorigin_matriz.csv
│   └── oecd_matriz.csv
├── reportes/
│   ├── completitud_por_columna.csv
│   ├── completitud_por_pais.csv
│   └── lista_paises_excluidos.csv
└── README.md
```

### 5.2 Columnas obligatorias

Siempre incluir en matriz consolidado:

```
iso3: Código ISO3 del país
country_name: Nombre oficial del país
region: Región (UN/OTRO)
income_group: Grupo de ingreso WB
```

---

## 6. Casos de Uso

### 6.1 Análisis descriptivo

- Comparar distributions por atributo
- Rankings por cada índice
- Correlación entre atributos

### 6.2 Análisis comparativo

- Agrupar por atributos categóricos
- Comparar grupos por atributos numéricos
- Análisis de varianza

### 6.3 Correlación y modelos

- Matrices de correlación
- Regresión multivariada
- Componentes principales

### 6.4 Series temporales

- Unir panel histórico por fuente
- Análisis de tendencias

---

## 7. Limitaciones Conocidas

### 7.1 Cobertura

| Fuente | Países cubiertos | Notas |
|--------|----------------|--------|
| Microsoft AI Diffusion | 76 | No cubre todos los 86 |
| Stanford AI Index | ~80 | USA, CHN dominan |
| OECD | ~40 | Solo países con iniciativas |

### 7.2 Ventanas temporales

| Fuente | Año exacto | Notas |
|--------|----------|--------|
| Oxford Insights | 2025 | Reportado en 2025 |
| Microsoft | H1/H2 2025 | Dos mediciones |
| Freedom House | 2025 (datos 2024) | Año del informe |
| WIPO GII | 2025 | 2025 edition |
| WB WDI | 2022-2024 | Varía por indicador |

### 7.3 Datos faltantes esperados

- Microsoft: 10 países sin adopción
- WIPO: Países de ingreso bajo
- WB: Indicadores sensibles
- OECD: Solo países con políticas

---

## 8. Calidad y Validación

### 8.1 Checks obligatorios

1. **Unicidad de iso3**: Verificar que cada país aparece una vez
2. **Range check**: Verificar valores dentro de rangos conocidos
3. **Consistencia categórica**: Verificar valores válidos para categoricals
4. **Completitud**: Reportar % NA por columna y fila

### 8.2 Documentación de limpieza

- Documentar valores atípicos (outliers)
- Documentar decisiones de codificación
- Documentar fuentes de incertidumbre

---

## 9. Referencias

### 9.1 Metodología fuentes

- IAPP Tracker: https://iapp.org/resources/
- Oxford Insights: https://oxfordinsights.com
- Microsoft AIEI: https://www.microsoft.com/en-us/research/group/aiei/
- Stanford AI Index: https://aiindex.stanford.edu
- WIPO GII: https://www.wipo.int/eds/pubdocs/en/wipo-pub-2000-2025-tech1.pdf
- World Bank WDI: https://databank.worldbank.org
- Freedom House: https://freedomhouse.org
- DLA Piper: https://www.dlapiperdataprotection.com
- La Porta 2008: "The Economic Consequences of Legal Origins"
- OECD.AI: https://oecd.ai

### 9.2 Documentación proyecto

- Metodología ETL: `ARCHIVOS_MD_CONTEXTO/GUIA_VARIABLES_ESTUDIO_ETL.md`
- Data decisions: `info_data/DATA_DECISIONS_LOG.md`
- Auditoría: `docs/INFORME_AUDITORIA_Y_PLAN_CORPUS.md`

---

## 10. Ejemplo de Columnas Resultantes

Preview de matriz consolidada (solo primeras 20 columnas):

```csv
iso3,country_name,region,wb_income_group,iapp_has_ai_law,iapp_regulatory_approach,iapp_regulatory_intensity,oxford_readiness_score,oxford_rank,ms_ai_adoption_h2_2025,stanford_ai_investment_2013_2024,wipo_gii_score,wipo_gii_rank,wb_gdp_per_capita_ppp,wb_internet_penetration,wb_regulatory_quality,fh_total_score,gdpr_has_law,gdpr_similarity_level,legal_origin,is_common_law
USA,United States,North America,HI,0,soft_framework,6,88.36,1,,254.6,55.9,1,76332,91.3,1.52,95,1,2,English,1
CHN,China,East Asia,UM,1,comprehensive,7,76.27,8,,100.2,32.4,12,21157,75.8,-0.24,9,1,2,Socialist,0
DEU,Germany,Europe,HI,1,comprehensive,10,76.78,6,,13.1,50.1,9,64184,91.9,1.65,93,1,3,German,0
...
```

---

## 11. Acciones siguientes

1. **Ejecutar extracción**: Crear scripts para cada fuente
2. **Validar merge**: Verificar iso3 matching
3. **Reportar completitud**: Generar estadísticas NA
4. **Documentar decisiones**: Log deextracción

---

*Documento generado para implementación de pipeline de extracción estandarizada.*  
*Fecha: 2026-04-28*  
*Proyecto: LeyIA DataScience - Matriz de Datos País × Atributo*