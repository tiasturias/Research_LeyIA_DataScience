# BLUEPRINT DE ACTUALIZACIÓN — Fase 6.2 Country Intelligence Layer

**Proyecto:** Research_AI_law — Boletín 16821-19 Ley Marco de IA Chile  
**Documento:** Blueprint operativo para extender Fase 6 con una capa país-por-país  
**Versión objetivo:** `fase6-v2.2-country-intelligence-layer`  
**Tipo de documento:** Instrucciones ejecutables para un LLM / agente técnico / auditor metodológico  
**Dependencia obligatoria:** Fase 6 v2.1+ ya ejecutada y con outputs existentes preservados  
**Fase CRISP-DM:** Modeling / Country-level interpretation / Descriptive positioning  
**Propósito:** Mantener todos los outputs actuales de Fase 6 y agregar una capa complementaria `6.2` que permita entender, país por país, cómo se comporta cada entidad de la muestra frente a Q1–Q6, quiénes son pioneros, quiénes son rezagados, por qué aparecen así y qué puede aprender Chile de ellos.

---

## 0. Instrucción principal para el LLM ejecutor

Debes implementar una actualización complementaria de Fase 6 llamada:

```text
FASE 6.2 — Country Intelligence Layer
```

Esta actualización **no reemplaza** los resultados existentes de Fase 6 v2.1+. No debes borrar, renombrar ni sobrescribir los 11 outputs actuales:

```text
fase6_manifest.json
q1_results.csv
q2_results.csv
q2_scores_per_country.csv
q3_results.csv
q4_clusters.csv
q4_distance_matrix.csv
q5_results.csv
q5_scores_per_country.csv
q6_results.csv
q6_scores_per_country.csv
```

Debes conservar esos archivos como outputs canónicos de Fase 6 v2.1+ y agregar una nueva capa de inteligencia país-por-país que produzca:

1. perfiles por país para Q1–Q6;
2. rankings de países por cada pregunta y outcome;
3. rankings por submuestra/grupo: LATAM, Europa, líderes IA, grandes potencias, pares de Chile, etc.;
4. identificación de mejores y peores países por outcome;
5. explicación descriptiva de por qué un país aparece arriba o abajo;
6. análisis comparativo de pioneros vs rezagados;
7. gráficos profesionales listos para Fase 8;
8. data estructurada para country cards: Singapur, Chile, Estonia, Irlanda, Emiratos, China, USA, Brasil, Uruguay, etc.

La Fase 6.2 debe ser **descriptiva, comparativa e interpretativa**, pero no causal. Debe responder preguntas como:

```text
¿Cómo se comporta Singapur en Q1-Q6?
¿Por qué Singapur aparece como pionero en IA?
¿Dónde está Chile frente a Singapur, Estonia o Emiratos?
¿Qué países lideran Q2 adopción y por qué?
¿Qué países quedan rezagados en Q6 sector público y qué brechas explican eso?
¿Qué patrones comparten los mejores?
¿Qué errores o debilidades comparten los peores?
```

Pero no debe afirmar:

```text
Singapur lidera porque su regulación causó X.
Chile tendrá Y si copia a Singapur.
El modelo predice causalmente el futuro de cada país.
```

La regla correcta es:

> Fase 6.2 produce diagnóstico comparado país-por-país y posicionamiento descriptivo in-sample. La robustez de esas lecturas se valida en Fase 7. La narrativa política final se redacta en Fase 8.

---

## 1. Principios metodológicos no negociables

La Fase 6.2 debe respetar íntegramente la metodología corregida de Fase 6 v2.1+:

```yaml
methodology: "inferential_comparative_observational"
primary_estimand: "adjusted_association"
holdout_used: false
train_test_split_used: false
external_validation_used: false
independent_prediction: false
causal_claim: false
```

### 1.1 Permitido

Puedes producir:

```text
ranking descriptivo
percentil dentro de la muestra
posición relativa
score in-sample
residuo observado vs esperado
perfil país
brecha frente a pioneros
comparación entre países
contribución descriptiva de variables
drivers observados
alertas de missingness
gráficos de diagnóstico
```

### 1.2 Prohibido

No puedes producir o afirmar:

```text
test externo
predicción independiente
causalidad fuerte
impacto causal
efecto causal
Singapur lidera porque X causó Y
Chile debe copiar X porque el modelo lo prueba
validación externa
train/test split
holdout
```

### 1.3 Frase metodológica obligatoria

Todo README, manifest, notebook o gráfico de Fase 6.2 debe incluir, al menos una vez, esta advertencia:

> Los rankings, scores y perfiles país-por-país son posicionamientos descriptivos in-sample dentro de la muestra preregistrada. No son predicciones independientes ni estimaciones causales. Su robustez debe evaluarse en Fase 7 antes de convertirse en recomendación política.

---

## 2. Problema que corrige Fase 6.2

La Fase 6 v2.1+ actual está bien como capa estadística general, pero todavía es débil para análisis ejecutivo país-por-país.

### 2.1 Qué responde bien Fase 6 v2.1+

Fase 6 v2.1+ responde:

```text
¿Existe asociación ajustada entre rasgos regulatorios y outcomes de inversión/adopción/innovación/sector público?
¿Cuál es el signo, magnitud, p-value, IC y n_effective por outcome?
¿Qué scores descriptivos in-sample se obtienen para Q2/Q5/Q6?
```

### 2.2 Qué no responde suficientemente

Todavía no responde de manera ordenada:

```text
¿Cómo se comporta cada país en Q1-Q6?
¿En qué Q es fuerte o débil Singapur?
¿Dónde supera Chile a sus pares?
¿Quiénes son los mejores por submuestra?
¿Quiénes son los peores y qué brechas tienen?
¿Qué tienen en común los pioneros?
¿Qué errores se observan en los rezagados?
¿Qué gráficos permiten entender esto sin leer tablas complejas?
```

### 2.3 Objetivo de Fase 6.2

Crear una capa intermedia entre Fase 6 y Fase 7/Fase 8:

```text
Fase 6.1 = modelos generales por Q
Fase 6.2 = inteligencia país-por-país
Fase 7 = robustez de hallazgos y perfiles
Fase 8 = narrativa ejecutiva y política pública
```

---

## 3. Inputs obligatorios

La Fase 6.2 debe leer los outputs ya generados por Fase 6 v2.1+ y los insumos del bundle de Fase 5.

### 3.1 Inputs desde Fase 6

```text
FASE6/outputs/fase6_manifest.json
FASE6/outputs/q1_results.csv
FASE6/outputs/q2_results.csv
FASE6/outputs/q2_scores_per_country.csv
FASE6/outputs/q3_results.csv
FASE6/outputs/q4_clusters.csv
FASE6/outputs/q4_distance_matrix.csv
FASE6/outputs/q5_results.csv
FASE6/outputs/q5_scores_per_country.csv
FASE6/outputs/q6_results.csv
FASE6/outputs/q6_scores_per_country.csv
```

### 3.2 Inputs desde Fase 5

```text
FASE5/outputs/phase6_ready/phase6_feature_matrix.csv
FASE5/outputs/phase6_ready/phase6_analysis_sample_membership.csv
FASE5/outputs/phase6_ready/phase6_modeling_contract.yaml
FASE5/outputs/phase6_ready/phase6_missingness_by_country.csv
FASE5/outputs/phase6_ready/phase6_missingness_by_column.csv
FASE5/outputs/phase6_ready/phase6_variables_catalog.csv
```

### 3.3 Inputs opcionales

Si existen, usarlos:

```text
FASE6/outputs/primary_results_long.csv
FASE6/outputs/model_diagnostics.csv
FASE6/outputs/effective_n_by_model.csv
FASE6/outputs/phase6_effective_n_by_outcome.csv
FASE6/outputs/exploratory_binary_sensitivity.csv
```

Si no existen, Fase 6.2 debe funcionar igual y registrar la ausencia en:

```text
FASE6/outputs/country_intelligence/phase6_2_quality_checks.csv
```

---

## 4. Outputs nuevos de Fase 6.2

Crear una subcarpeta nueva:

```text
FASE6/outputs/country_intelligence/
```

Dentro deben generarse estos archivos.

### 4.1 Outputs tabulares principales

```text
country_q_profile_long.csv
country_q_profile_wide.csv
country_rankings_by_outcome.csv
country_rankings_by_group.csv
country_best_worst_by_q.csv
country_model_contributions.csv
country_residuals_and_gaps.csv
country_cluster_profile.csv
country_headline_flags.csv
country_comparison_pairs.csv
country_learning_patterns.csv
country_graphics_catalog.csv
phase6_2_country_intelligence_manifest.json
phase6_2_quality_checks.csv
```

### 4.2 Outputs específicos para países clave

```text
country_cards_data/
├── CHL_country_card_data.csv
├── SGP_country_card_data.csv
├── EST_country_card_data.csv
├── IRL_country_card_data.csv
├── ARE_country_card_data.csv
├── KOR_country_card_data.csv
├── JPN_country_card_data.csv
├── USA_country_card_data.csv
├── CHN_country_card_data.csv
├── BRA_country_card_data.csv
├── URY_country_card_data.csv
└── README_country_cards.md
```

### 4.3 Outputs gráficos

Crear:

```text
FASE6/outputs/country_intelligence/figures/
```

Con subcarpetas:

```text
figures/
├── q_rankings/
├── q_heatmaps/
├── country_cards/
├── chile_vs_benchmarks/
├── pioneer_vs_laggard/
├── residuals/
├── clusters/
└── executive/
```

Gráficos mínimos obligatorios:

```text
figures/q_heatmaps/heatmap_country_by_q_percentiles.png
figures/q_rankings/q1_investment_ranking.png
figures/q_rankings/q2_adoption_ranking.png
figures/q_rankings/q3_innovation_ranking.png
figures/q_rankings/q4_regulatory_profile_map.png
figures/q_rankings/q5_population_usage_ranking.png
figures/q_rankings/q6_public_sector_ranking.png
figures/country_cards/SGP_country_card_radar.png
figures/country_cards/CHL_country_card_radar.png
figures/chile_vs_benchmarks/chile_vs_singapore_q_profile.png
figures/chile_vs_benchmarks/chile_vs_pioneers_heatmap.png
figures/pioneer_vs_laggard/top_bottom_by_q_panel.png
figures/residuals/observed_vs_expected_selected_outcomes.png
figures/clusters/q4_cluster_profile_map.png
```

---

## 5. Arquitectura de código recomendada

Crear o actualizar esta estructura dentro de Fase 6:

```text
FASE6/src/
├── country_intelligence/
│   ├── __init__.py
│   ├── _paths.py
│   ├── _load.py
│   ├── _scoring.py
│   ├── _rankings.py
│   ├── _profiles.py
│   ├── _contributions.py
│   ├── _residuals.py
│   ├── _groups.py
│   ├── _learning_patterns.py
│   ├── _graphics.py
│   ├── _country_cards.py
│   ├── _validate.py
│   └── run_country_intelligence.py
```

No mezclar esta lógica dentro de `q1_investment.py`, `q2_adoption.py`, etc. Fase 6.2 debe ser una capa agregadora y explicativa que consume outputs ya existentes.

---

## 6. Configuración nueva

Crear:

```text
FASE6/config/phase6_2_country_intelligence.yaml
```

Contenido mínimo:

```yaml
version: "2.2"
module: "country_intelligence_layer"
methodology: "inferential_comparative_observational"
scope: "descriptive_country_level_positioning"
causal_claims_allowed: false
independent_prediction_allowed: false
external_validation_allowed: false

primary_sample:
  expected_n: 43
  primary_key: "iso3"
  focal_country: "CHL"

country_groups:
  focal:
    - CHL
  ai_pioneers:
    - SGP
    - ARE
    - IRL
    - EST
    - KOR
    - ISR
    - USA
    - CHN
  large_ai_powers:
    - USA
    - CHN
    - IND
    - JPN
  chile_latam_peers:
    - ARG
    - BRA
    - COL
    - CRI
    - MEX
    - PER
    - URY
  eu_laggards:
    - GRC
    - ROU
    - HRV
  chile_priority_benchmarks:
    - SGP
    - EST
    - IRL
    - ARE
    - KOR
    - URY
    - BRA

questions:
  Q1:
    label: "Inversión"
    type: "investment"
    primary_outputs:
      - q1_results.csv
    country_score_policy: "derive_from_observed_outcomes_and_model_terms"
  Q2:
    label: "Adopción"
    type: "adoption"
    primary_outputs:
      - q2_scores_per_country.csv
      - q2_results.csv
    country_score_policy: "use_scores_file_plus_observed_percentiles"
  Q3:
    label: "Innovación"
    type: "innovation"
    primary_outputs:
      - q3_results.csv
    country_score_policy: "derive_from_observed_outcomes_and_model_terms"
  Q4:
    label: "Perfil regulatorio"
    type: "clustering"
    primary_outputs:
      - q4_clusters.csv
      - q4_distance_matrix.csv
    country_score_policy: "cluster_membership_and_profile"
  Q5:
    label: "Uso poblacional"
    type: "population_usage"
    primary_outputs:
      - q5_scores_per_country.csv
      - q5_results.csv
    country_score_policy: "use_scores_file_plus_observed_percentiles"
  Q6:
    label: "Sector público"
    type: "public_sector"
    primary_outputs:
      - q6_scores_per_country.csv
      - q6_results.csv
    country_score_policy: "use_scores_file_plus_observed_percentiles"

ranking_policy:
  rank_descending_when_higher_better: true
  percentile_method: "rank_pct"
  ties_method: "average"
  min_non_missing_for_ranking: 10
  missing_country_policy: "include_with_missing_flag_not_ranked"

best_worst_policy:
  top_n_global: 5
  bottom_n_global: 5
  top_n_by_group: 3
  bottom_n_by_group: 3
  require_n_comparable_min: 10

interpretation_policy:
  top_percentile_threshold: 0.80
  bottom_percentile_threshold: 0.20
  pioneer_label_threshold: 0.85
  laggard_label_threshold: 0.15
  missingness_warning_threshold: 0.25

graphics_policy:
  save_png: true
  save_svg: true
  dpi: 180
  use_professional_titles: true
  include_methodology_footer: true
  max_countries_in_single_ranking_chart: 43
  highlight_countries:
    - CHL
    - SGP
    - EST
    - IRL
    - ARE
    - USA
    - CHN
    - BRA
    - URY
```

---

## 7. Definición conceptual de los nuevos archivos

## 7.1 `country_q_profile_long.csv`

Archivo central de Fase 6.2.

### Grano

Una fila por:

```text
country × question × outcome_or_dimension
```

### Columnas mínimas

```text
iso3
country_name
region
income_group
question_id
question_label
dimension_type
outcome
observed_value
score_value
score_source
rank_global
percentile_global
rank_group
percentile_group
group_name
z_score_global
n_comparable_countries
missing_observed_value
missing_score_value
interpretation_label
strength_weakness_label
score_scope
independent_prediction
causal_claim
notes
```

### Valores permitidos

```text
score_scope = in_sample_descriptive_positioning
independent_prediction = false
causal_claim = false
```

### Ejemplo conceptual

```text
SGP | Q2 | Adopción | ms_h2_2025_ai_diffusion_pct | 64.2 | rank 2/42 | top_pioneer
CHL | Q2 | Adopción | ms_h2_2025_ai_diffusion_pct | 18.1 | rank 31/42 | lagging
SGP | Q6 | Sector público | oxford_public_sector_adoption | 92.0 | rank 1/42 | top_pioneer
```

---

## 7.2 `country_q_profile_wide.csv`

Una fila por país, con resumen compacto por Q.

### Columnas mínimas

```text
iso3
country_name
region
income_group
Q1_investment_percentile
Q1_investment_rank
Q1_investment_label
Q2_adoption_percentile
Q2_adoption_rank
Q2_adoption_label
Q3_innovation_percentile
Q3_innovation_rank
Q3_innovation_label
Q4_regulatory_cluster
Q4_regulatory_profile_label
Q5_population_usage_percentile
Q5_population_usage_rank
Q5_population_usage_label
Q6_public_sector_percentile
Q6_public_sector_rank
Q6_public_sector_label
overall_country_profile_score
overall_country_profile_rank
overall_country_profile_label
main_strengths
main_weaknesses
missingness_warnings
recommended_use_in_phase8
```

### Lógica

El score general no debe inventar un índice causal. Debe ser:

```text
promedio descriptivo de percentiles disponibles Q1, Q2, Q3, Q5, Q6 + etiqueta Q4 separada
```

Registrar:

```text
overall_country_profile_score_is_descriptive = true
not_a_causal_or_predictive_index = true
```

---

## 7.3 `country_rankings_by_outcome.csv`

Archivo para rankear todos los países por cada outcome específico.

### Grano

Una fila por:

```text
outcome × country
```

### Columnas mínimas

```text
question_id
question_label
outcome
outcome_label
iso3
country_name
region
income_group
value_used_for_ranking
value_type
rank_desc
rank_asc
percentile
n_ranked
is_top_5_global
is_bottom_5_global
is_top_group
is_bottom_group
group_name
interpretation_label
why_high_or_low_short
missingness_flag
```

### Interpretation labels

```text
top_pioneer
high_performer
middle_performer
low_performer
bottom_laggard
not_ranked_missing
```

---

## 7.4 `country_rankings_by_group.csv`

Ranking dentro de submuestras. Debe permitir responder:

```text
¿Quién es el mejor de LATAM en Q2?
¿Quién es el peor entre países europeos en Q6?
¿Chile está arriba o abajo de sus pares?
¿Singapur lidera entre los pioneros?
```

### Grupos obligatorios

```text
global_43
latam_peers
chile_priority_benchmarks
ai_pioneers
large_ai_powers
europe
east_asia_pacific
north_america
mena
income_high
income_upper_middle
eu_laggards
```

Usar `membership` para regiones e ingreso. Usar YAML para grupos temáticos.

### Columnas mínimas

```text
group_name
group_type
question_id
outcome
iso3
country_name
value_used_for_ranking
rank_within_group
percentile_within_group
n_group_ranked
is_best_in_group
is_worst_in_group
distance_to_group_best
distance_to_group_median
distance_to_chile
interpretation_label
why_best_or_worst
```

---

## 7.5 `country_best_worst_by_q.csv`

Archivo ejecutivo: mejores y peores por cada Q.

### Grano

Una fila por:

```text
question × group × best_or_worst_country
```

### Columnas mínimas

```text
question_id
question_label
group_name
rank_type
iso3
country_name
rank
percentile
value_summary
main_driver_1
main_driver_2
main_driver_3
why_this_country_is_best_or_worst
lesson_for_chile
caution_note
```

### `rank_type`

```text
best_global
worst_global
best_group
worst_group
best_latam
worst_latam
best_benchmark
worst_benchmark
```

---

## 7.6 `country_model_contributions.csv`

Explica drivers descriptivos. No causalidad.

### Grano

Una fila por:

```text
country × question × outcome × term
```

### Columnas mínimas

```text
iso3
country_name
question_id
outcome
model_id
term
term_value
term_percentile
coefficient_or_weight
standardized_contribution
contribution_direction
contribution_rank_within_country
contribution_label
driver_type
interpretation
causal_claim
```

### Interpretación

Ejemplo:

```text
Singapur aparece alto en Q6 no porque una sola variable "cause" liderazgo,
sino porque combina altos valores observados en adopción pública, gobernanza de datos
y política digital gubernamental.
```

---

## 7.7 `country_residuals_and_gaps.csv`

Permite detectar overperformers y underperformers.

### Grano

Una fila por:

```text
country × question × outcome × model
```

### Columnas mínimas

```text
iso3
country_name
question_id
outcome
model_id
observed_value
fitted_value
residual
absolute_residual
residual_rank
residual_percentile
overperformer_underperformer
gap_vs_best
gap_vs_group_best
gap_vs_chile
gap_vs_singapore
interpretation
```

### Labels

```text
overperformer
as_expected
underperformer
not_estimable
```

---

## 7.8 `country_headline_flags.csv`

Detecta países interesantes para narrativa.

### Columnas mínimas

```text
iso3
country_name
is_top_5_q1
is_top_5_q2
is_top_5_q3
is_top_5_q5
is_top_5_q6
is_bottom_5_q1
is_bottom_5_q2
is_bottom_5_q3
is_bottom_5_q5
is_bottom_5_q6
is_consistent_pioneer
is_consistent_laggard
is_overperformer
is_underperformer
is_chile_benchmark
is_latam_leader
is_missing_critical_data
headline_candidate
suggested_headline
caution_note
```

---

## 7.9 `country_learning_patterns.csv`

Archivo más estratégico. Debe responder qué aprender de los mejores y peores.

### Columnas mínimas

```text
pattern_id
question_id
group_name
pattern_type
countries_in_pattern
shared_strengths
shared_weaknesses
regulatory_profile_summary
ecosystem_profile_summary
lesson_for_chile
risk_of_overinterpretation
evidence_strength
recommended_phase8_use
```

### `pattern_type`

```text
pioneer_pattern
laggard_pattern
latam_leader_pattern
latam_gap_pattern
public_sector_success_pattern
adoption_without_hard_law_pattern
strong_regulation_low_adoption_pattern
soft_law_high_adoption_pattern
```

Ejemplo esperado:

```text
pattern_type: adoption_without_hard_law_pattern
countries_in_pattern: SGP;EST;IRL
lesson_for_chile: la adopción alta puede estar asociada a capacidades digitales e institucionales, no solo a tener una ley dura de IA.
risk_of_overinterpretation: no afirmar causalidad; validar en Fase 7.
```

---

## 8. Cálculo de scores por Q

La Fase 6.2 debe construir un score descriptivo por pregunta para cada país.

### 8.1 Q1 — Inversión

Usar outcomes disponibles relacionados con inversión:

```text
oxford_ind_company_investment_emerging_tech
oxford_ind_ai_unicorns_log
oxford_ind_vc_availability
wipo_c_vencapdeal_score
```

Si los valores observados están en `phase6_feature_matrix.csv`, rankearlos directamente.

Calcular:

```text
Q1_investment_percentile = promedio de percentiles disponibles de outcomes Q1
Q1_investment_rank = ranking descendente del promedio
```

No imputar faltantes. Si un país tiene menos del 50% de outcomes Q1 disponibles:

```text
Q1_investment_label = insufficient_data
```

### 8.2 Q2 — Adopción

Usar:

```text
q2_scores_per_country.csv
```

y complementar con valores observados:

```text
ms_h2_2025_ai_diffusion_pct
oecd_5_ict_business_oecd_biz_ai_pct
anthropic_usage_pct
oxford_public_sector_adoption
oxford_ind_adoption_emerging_tech
```

Score Q2:

```text
Q2_adoption_percentile = promedio de percentiles disponibles en scores/modelos primarios + outcomes observados
```

Si hay conflicto entre fuentes, registrar:

```text
Q2_source_disagreement_flag = true
```

### 8.3 Q3 — Innovación

Usar outcomes:

```text
oxford_total_score
wipo_out_score
stanford_fig_6_3_5_volume_of_publications
stanford_fig_6_3_4_ai_patent_count
```

Para conteos sesgados, usar columnas log si existen. Si no, rankear crudo con advertencia.

### 8.4 Q4 — Perfil regulatorio

Usar:

```text
q4_clusters.csv
q4_distance_matrix.csv
```

Pero marcar limitación si Q4 tiene menos de 43 países.

Q4 no debe producir “mejor/peor” normativo automáticamente. Debe producir:

```text
cluster_id
cluster_label
profile_type
countries_in_cluster
chile_same_cluster
singapore_same_cluster
regulatory_profile_summary
```

Si se necesita ranking regulatorio, usar solo como intensidad descriptiva:

```text
n_binding
n_non_binding
regulatory_intensity
```

No decir que un cluster es “mejor” sin relacionarlo con outcomes.

### 8.5 Q5 — Uso poblacional

Usar:

```text
q5_scores_per_country.csv
anthropic_usage_pct
anthropic_collaboration_pct
oxford_ind_adoption_emerging_tech
```

Cuidado: si `anthropic_collaboration_pct` tiene poca variación o valores casi cero, marcar:

```text
low_information_outcome = true
```

### 8.6 Q6 — Sector público

Usar:

```text
q6_scores_per_country.csv
oxford_public_sector_adoption
oxford_e_government_delivery
oxford_government_digital_policy
oxford_ind_data_governance
oxford_governance_ethics
oecd_2_indigo_oecd_indigo_score
oecd_4_digital_gov_oecd_digital_gov_overall
```

Score Q6:

```text
promedio de percentiles disponibles de outcomes de capacidad pública
```

Separar subdimensiones:

```text
public_sector_adoption
government_digital_policy
data_governance
ethics_governance
digital_service_delivery
```

---

## 9. Labels interpretativos

Crear función común de etiquetado.

### 9.1 Percentil global

```python
def label_from_percentile(p):
    if pd.isna(p):
        return "not_ranked_missing"
    if p >= 0.90:
        return "top_pioneer"
    if p >= 0.75:
        return "high_performer"
    if p >= 0.40:
        return "middle_performer"
    if p >= 0.20:
        return "low_performer"
    return "bottom_laggard"
```

### 9.2 Fortalezas y debilidades país

```text
strength = percentil >= 0.75
weakness = percentil <= 0.25
critical_gap = percentil <= 0.10
```

### 9.3 Consistent pioneer

Un país es `consistent_pioneer` si:

```text
percentil >= 0.75 en al menos 3 de Q1, Q2, Q3, Q5, Q6
```

### 9.4 Consistent laggard

Un país es `consistent_laggard` si:

```text
percentil <= 0.25 en al menos 3 de Q1, Q2, Q3, Q5, Q6
```

### 9.5 Benchmark útil para Chile

Un país es benchmark útil si:

```text
es high_performer o top_pioneer en al menos 2 Q
y tiene alguna comparabilidad institucional/regional/tamaño o relevancia estratégica para Chile
```

Ejemplos candidatos:

```text
SGP, EST, IRL, ARE, KOR, URY, BRA
```

---

## 10. Gráficos profesionales obligatorios

Los gráficos deben ser suficientemente claros para que un jefe pueda entender el mensaje sin leer 20 páginas.

### 10.1 Reglas generales de visualización

Cada gráfico debe tener:

```text
título ejecutivo
subtítulo metodológico breve
ejes claros
países destacados: CHL, SGP, EST, IRL, ARE, USA, CHN, BRA, URY
nota al pie: posicionamiento descriptivo in-sample; no causalidad
fuente: Research_AI_law Fase 6.2
```

Guardar en PNG y SVG:

```text
figures/.../*.png
figures/.../*.svg
```

No usar gráficos 3D. No saturar con demasiados colores. Usar colores sobrios.

### 10.2 Heatmap país × Q

Archivo:

```text
figures/q_heatmaps/heatmap_country_by_q_percentiles.png
```

Filas:

```text
43 países o países rankeables
```

Columnas:

```text
Q1 inversión
Q2 adopción
Q3 innovación
Q5 uso poblacional
Q6 sector público
```

Q4 se puede incluir como anotación de cluster, no como percentil si no hay ranking normativo.

Ordenar países por:

```text
overall_country_profile_score descendente
```

Destacar:

```text
CHL
SGP
EST
IRL
ARE
USA
CHN
BRA
URY
```

### 10.3 Ranking por Q

Crear un ranking para cada Q:

```text
q1_investment_ranking.png
q2_adoption_ranking.png
q3_innovation_ranking.png
q5_population_usage_ranking.png
q6_public_sector_ranking.png
```

Cada ranking debe mostrar:

```text
todos los países rankeados si caben
o top 15 + Chile + bottom 10 si el gráfico queda saturado
```

Debe incluir:

```text
rank
país
score/percentil
color o marcador para Chile
color o marcador para Singapur
```

### 10.4 Top/Bottom panel por Q

Archivo:

```text
figures/pioneer_vs_laggard/top_bottom_by_q_panel.png
```

Debe mostrar:

```text
Top 5 y Bottom 5 por Q1
Top 5 y Bottom 5 por Q2
Top 5 y Bottom 5 por Q3
Top 5 y Bottom 5 por Q5
Top 5 y Bottom 5 por Q6
```

Mensaje esperado:

```text
quiénes son pioneros, quiénes son rezagados y en qué dimensión
```

### 10.5 Chile vs Singapur

Archivo:

```text
figures/chile_vs_benchmarks/chile_vs_singapore_q_profile.png
```

Tipo recomendado:

```text
radar chart o slope chart
```

Debe comparar:

```text
Q1, Q2, Q3, Q5, Q6 percentiles
Q4 cluster como texto
```

Texto interpretativo:

```text
Singapur supera a Chile especialmente en [dimensiones].
Chile está más cerca/lejos en [dimensiones].
```

No decir causalidad.

### 10.6 Country card radar

Para países clave:

```text
SGP, CHL, EST, IRL, ARE, KOR, USA, CHN, BRA, URY
```

Archivo ejemplo:

```text
figures/country_cards/SGP_country_card_radar.png
```

Debe incluir:

```text
radar Q1-Q6
top strengths
main weaknesses
cluster Q4
missingness warning
```

### 10.7 Residual plots

Archivo:

```text
figures/residuals/observed_vs_expected_selected_outcomes.png
```

Debe mostrar:

```text
observed_value vs fitted_value
línea de 45°
países destacados
overperformers
underperformers
```

Útil para decir:

```text
este país rinde mejor/peor de lo esperado según el modelo
```

### 10.8 Waterfall de drivers

Para Singapur y Chile:

```text
figures/country_cards/SGP_driver_waterfall.png
figures/country_cards/CHL_driver_waterfall.png
```

Si no hay contribuciones robustas suficientes, reemplazar por bar chart de percentiles por dimensión.

---

## 11. Implementación paso a paso

## Paso 0 — Backup

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP

mkdir -p FASE6/outputs/country_intelligence
cp -r FASE6/outputs/country_intelligence FASE6/outputs/country_intelligence.pre_update_$(date +%Y%m%d_%H%M%S) || true
```

No modificar ni borrar los 11 archivos existentes de Fase 6.

---

## Paso 1 — Pre-flight

Crear `FASE6/src/country_intelligence/_load.py`.

Debe validar:

```python
from pathlib import Path
import json
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[3]
FASE5_BUNDLE = ROOT / "FASE5" / "outputs" / "phase6_ready"
FASE6_OUTPUTS = ROOT / "FASE6" / "outputs"
CI_OUTPUTS = FASE6_OUTPUTS / "country_intelligence"


REQUIRED_FASE6 = [
    "fase6_manifest.json",
    "q1_results.csv",
    "q2_results.csv",
    "q2_scores_per_country.csv",
    "q3_results.csv",
    "q4_clusters.csv",
    "q4_distance_matrix.csv",
    "q5_results.csv",
    "q5_scores_per_country.csv",
    "q6_results.csv",
    "q6_scores_per_country.csv",
]


def validate_preflight():
    checks = []
    for fname in REQUIRED_FASE6:
        path = FASE6_OUTPUTS / fname
        checks.append({
            "check": f"exists_{fname}",
            "status": "PASS" if path.exists() else "FAIL",
            "severity": "P0" if not path.exists() else "INFO",
            "path": str(path),
        })

    manifest = json.loads((FASE6_OUTPUTS / "fase6_manifest.json").read_text())
    checks.append({
        "check": "manifest_no_holdout",
        "status": "PASS" if manifest.get("holdout_used") is False else "FAIL",
        "severity": "P0",
    })
    checks.append({
        "check": "manifest_no_external_validation",
        "status": "PASS" if manifest.get("external_validation_used") is False else "FAIL",
        "severity": "P0",
    })

    fm = pd.read_csv(FASE5_BUNDLE / "phase6_feature_matrix.csv")
    checks.append({
        "check": "feature_matrix_43_rows",
        "status": "PASS" if len(fm) == 43 else "FAIL",
        "severity": "P0",
        "observed": len(fm),
    })
    checks.append({
        "check": "feature_matrix_no_split",
        "status": "PASS" if "split" not in fm.columns else "FAIL",
        "severity": "P0",
    })

    return pd.DataFrame(checks)
```

Si algún `P0` falla, abortar.

---

## Paso 2 — Crear `_scoring.py`

Responsabilidades:

- calcular percentiles;
- calcular rankings;
- crear labels interpretativos;
- no imputar.

```python
import pandas as pd
import numpy as np


def percentile_rank(series: pd.Series, higher_is_better: bool = True) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce")
    if higher_is_better:
        return s.rank(pct=True, method="average")
    return 1 - s.rank(pct=True, method="average")


def descending_rank(series: pd.Series, higher_is_better: bool = True) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce")
    return s.rank(ascending=not higher_is_better, method="min")


def zscore(series: pd.Series) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce")
    if s.std(skipna=True) == 0 or pd.isna(s.std(skipna=True)):
        return pd.Series([pd.NA] * len(s), index=s.index)
    return (s - s.mean(skipna=True)) / s.std(skipna=True)


def label_from_percentile(p):
    if pd.isna(p):
        return "not_ranked_missing"
    if p >= 0.90:
        return "top_pioneer"
    if p >= 0.75:
        return "high_performer"
    if p >= 0.40:
        return "middle_performer"
    if p >= 0.20:
        return "low_performer"
    return "bottom_laggard"


def strength_weakness_label(p):
    if pd.isna(p):
        return "missing"
    if p >= 0.75:
        return "strength"
    if p <= 0.25:
        return "weakness"
    return "neutral"
```

---

## Paso 3 — Crear `_groups.py`

Responsabilidades:

- unir membership con grupos YAML;
- definir submuestras;
- generar rankings por grupo.

```python
import pandas as pd


def assign_custom_groups(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    out = df.copy()
    group_cols = {}
    for group_name, iso_list in config.get("country_groups", {}).items():
        if isinstance(iso_list, list):
            out[f"is_group_{group_name}"] = out["iso3"].isin(iso_list)
    return out


def build_group_membership(membership: pd.DataFrame, config: dict) -> pd.DataFrame:
    rows = []

    for _, r in membership.iterrows():
        iso3 = r["iso3"]
        rows.append({"iso3": iso3, "group_name": "global_43", "group_type": "global"})

        if pd.notna(r.get("region")):
            rows.append({"iso3": iso3, "group_name": str(r["region"]), "group_type": "region"})

        if pd.notna(r.get("income_group")):
            rows.append({"iso3": iso3, "group_name": str(r["income_group"]), "group_type": "income"})

    for group_name, iso_list in config.get("country_groups", {}).items():
        if isinstance(iso_list, list):
            for iso3 in iso_list:
                rows.append({"iso3": iso3, "group_name": group_name, "group_type": "custom"})

    return pd.DataFrame(rows).drop_duplicates()
```

---

## Paso 4 — Crear `_rankings.py`

Responsabilidades:

- rankear por outcome;
- rankear por pregunta;
- rankear por grupo;
- crear best/worst.

```python
import pandas as pd
from ._scoring import percentile_rank, descending_rank, label_from_percentile


def rank_outcome(
    df: pd.DataFrame,
    outcome: str,
    question_id: str,
    question_label: str,
    higher_is_better: bool = True,
) -> pd.DataFrame:
    if outcome not in df.columns:
        return pd.DataFrame()

    out = df[["iso3", "country_name_canonical", "region", "income_group", outcome]].copy()
    out = out.rename(columns={
        "country_name_canonical": "country_name",
        outcome: "value_used_for_ranking",
    })
    out["question_id"] = question_id
    out["question_label"] = question_label
    out["outcome"] = outcome
    out["outcome_label"] = outcome
    out["value_type"] = "observed_or_score"
    out["rank_desc"] = descending_rank(out["value_used_for_ranking"], higher_is_better)
    out["rank_asc"] = descending_rank(out["value_used_for_ranking"], not higher_is_better)
    out["percentile"] = percentile_rank(out["value_used_for_ranking"], higher_is_better)
    out["n_ranked"] = out["value_used_for_ranking"].notna().sum()
    out["is_top_5_global"] = out["rank_desc"] <= 5
    out["is_bottom_5_global"] = out["rank_asc"] <= 5
    out["interpretation_label"] = out["percentile"].apply(label_from_percentile)
    out["missingness_flag"] = out["value_used_for_ranking"].isna()
    out["why_high_or_low_short"] = out["interpretation_label"].map({
        "top_pioneer": "ubicado en el tramo superior de la muestra",
        "high_performer": "desempeño alto relativo",
        "middle_performer": "desempeño intermedio relativo",
        "low_performer": "desempeño bajo relativo",
        "bottom_laggard": "ubicado en el tramo inferior de la muestra",
        "not_ranked_missing": "sin dato suficiente para ranking",
    })
    return out


def build_rankings_by_group(rankings: pd.DataFrame, group_membership: pd.DataFrame) -> pd.DataFrame:
    merged = rankings.merge(group_membership, on="iso3", how="left")
    rows = []
    for (group_name, question_id, outcome), g in merged.groupby(["group_name", "question_id", "outcome"], dropna=False):
        g = g.copy()
        valid = g["value_used_for_ranking"].notna()
        g["rank_within_group"] = g.loc[valid, "value_used_for_ranking"].rank(ascending=False, method="min")
        g["percentile_within_group"] = g.loc[valid, "value_used_for_ranking"].rank(pct=True, method="average")
        g["n_group_ranked"] = valid.sum()
        g["is_best_in_group"] = g["rank_within_group"] == 1
        g["is_worst_in_group"] = g["rank_within_group"] == g["n_group_ranked"]
        best_val = g.loc[valid, "value_used_for_ranking"].max() if valid.any() else pd.NA
        med_val = g.loc[valid, "value_used_for_ranking"].median() if valid.any() else pd.NA
        chile_val = g.loc[g["iso3"].eq("CHL"), "value_used_for_ranking"]
        chile_val = chile_val.iloc[0] if not chile_val.empty else pd.NA
        g["distance_to_group_best"] = best_val - g["value_used_for_ranking"]
        g["distance_to_group_median"] = med_val - g["value_used_for_ranking"]
        g["distance_to_chile"] = g["value_used_for_ranking"] - chile_val if pd.notna(chile_val) else pd.NA
        g["why_best_or_worst"] = g.apply(
            lambda r: "mejor de su grupo" if r.get("is_best_in_group") else ("peor de su grupo" if r.get("is_worst_in_group") else ""),
            axis=1
        )
        rows.append(g)
    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()


def build_best_worst_by_q(rankings: pd.DataFrame, rankings_group: pd.DataFrame, top_n=5, bottom_n=5) -> pd.DataFrame:
    rows = []
    for (q, outcome), g in rankings.groupby(["question_id", "outcome"], dropna=False):
        valid = g[g["value_used_for_ranking"].notna()].copy()
        top = valid.nsmallest(top_n, "rank_desc")
        bottom = valid.nsmallest(bottom_n, "rank_asc")
        for rank_type, sub in [("best_global", top), ("worst_global", bottom)]:
            for _, r in sub.iterrows():
                rows.append({
                    "question_id": q,
                    "question_label": r.get("question_label"),
                    "group_name": "global_43",
                    "rank_type": rank_type,
                    "iso3": r["iso3"],
                    "country_name": r["country_name"],
                    "rank": r["rank_desc"] if rank_type == "best_global" else r["rank_asc"],
                    "percentile": r["percentile"],
                    "value_summary": r["value_used_for_ranking"],
                    "main_driver_1": r["outcome"],
                    "main_driver_2": "",
                    "main_driver_3": "",
                    "why_this_country_is_best_or_worst": r["why_high_or_low_short"],
                    "lesson_for_chile": "comparar perfil país y drivers antes de extraer lección política",
                    "caution_note": "ranking descriptivo in-sample; no causalidad",
                })
    return pd.DataFrame(rows)
```

---

## Paso 5 — Crear `_profiles.py`

Responsabilidades:

- construir `country_q_profile_long`;
- construir `country_q_profile_wide`;
- calcular score general descriptivo.

```python
import pandas as pd
from ._scoring import label_from_percentile, strength_weakness_label


def build_country_q_profile_long(rankings: pd.DataFrame) -> pd.DataFrame:
    out = rankings.copy()
    out["dimension_type"] = "question_outcome"
    out["observed_value"] = out["value_used_for_ranking"]
    out["score_value"] = out["value_used_for_ranking"]
    out["score_source"] = "observed_or_phase6_score"
    out["rank_global"] = out["rank_desc"]
    out["percentile_global"] = out["percentile"]
    out["z_score_global"] = pd.NA
    out["n_comparable_countries"] = out["n_ranked"]
    out["missing_observed_value"] = out["value_used_for_ranking"].isna()
    out["missing_score_value"] = out["value_used_for_ranking"].isna()
    out["strength_weakness_label"] = out["percentile"].apply(strength_weakness_label)
    out["score_scope"] = "in_sample_descriptive_positioning"
    out["independent_prediction"] = False
    out["causal_claim"] = False
    out["notes"] = "Descriptive country-level position; not external prediction or causality."
    keep = [
        "iso3", "country_name", "region", "income_group",
        "question_id", "question_label", "dimension_type", "outcome",
        "observed_value", "score_value", "score_source",
        "rank_global", "percentile_global",
        "rank_desc", "n_comparable_countries",
        "missing_observed_value", "missing_score_value",
        "interpretation_label", "strength_weakness_label",
        "score_scope", "independent_prediction", "causal_claim", "notes",
    ]
    return out[[c for c in keep if c in out.columns]]


def build_country_q_profile_wide(profile_long: pd.DataFrame, clusters: pd.DataFrame | None = None) -> pd.DataFrame:
    q_summary = (
        profile_long
        .groupby(["iso3", "country_name", "region", "income_group", "question_id"], dropna=False)
        .agg(
            question_percentile=("percentile_global", "mean"),
            n_dimensions_available=("percentile_global", "count"),
        )
        .reset_index()
    )
    q_summary["question_label_calc"] = q_summary["question_percentile"].apply(label_from_percentile)

    wide = q_summary.pivot_table(
        index=["iso3", "country_name", "region", "income_group"],
        columns="question_id",
        values="question_percentile",
        aggfunc="mean",
    ).reset_index()

    for q in ["Q1", "Q2", "Q3", "Q5", "Q6"]:
        if q in wide.columns:
            wide[f"{q}_percentile"] = wide[q]
            wide[f"{q}_label"] = wide[q].apply(label_from_percentile)
            wide = wide.drop(columns=[q])

    q_cols = [c for c in wide.columns if c.endswith("_percentile")]
    wide["overall_country_profile_score"] = wide[q_cols].mean(axis=1, skipna=True)
    wide["overall_country_profile_rank"] = wide["overall_country_profile_score"].rank(ascending=False, method="min")
    wide["overall_country_profile_label"] = wide["overall_country_profile_score"].apply(label_from_percentile)

    def strengths(row):
        out = []
        for c in q_cols:
            if pd.notna(row[c]) and row[c] >= 0.75:
                out.append(c.replace("_percentile", ""))
        return ";".join(out)

    def weaknesses(row):
        out = []
        for c in q_cols:
            if pd.notna(row[c]) and row[c] <= 0.25:
                out.append(c.replace("_percentile", ""))
        return ";".join(out)

    wide["main_strengths"] = wide.apply(strengths, axis=1)
    wide["main_weaknesses"] = wide.apply(weaknesses, axis=1)
    wide["missingness_warnings"] = wide[q_cols].isna().sum(axis=1).astype(str) + "_missing_Q_dimensions"
    wide["recommended_use_in_phase8"] = wide["overall_country_profile_label"].map({
        "top_pioneer": "benchmark_case",
        "high_performer": "positive_comparator",
        "middle_performer": "context_case",
        "low_performer": "gap_case",
        "bottom_laggard": "warning_case",
        "not_ranked_missing": "do_not_use_without_caution",
    })

    if clusters is not None and not clusters.empty and "iso3" in clusters.columns:
        cluster_cols = [c for c in clusters.columns if c in {"iso3", "cluster_id", "cluster_label", "cluster_method"}]
        wide = wide.merge(clusters[cluster_cols].drop_duplicates("iso3"), on="iso3", how="left")

    wide["overall_country_profile_score_is_descriptive"] = True
    wide["not_a_causal_or_predictive_index"] = True
    return wide
```

---

## Paso 6 — Crear `_contributions.py`

Responsabilidades:

- calcular contribuciones descriptivas usando coeficientes de Fase 6;
- no decir causalidad;
- producir drivers para country cards.

```python
import pandas as pd


def extract_coefficients(results: dict[str, pd.DataFrame]) -> pd.DataFrame:
    frames = []
    for q, df in results.items():
        if q == "Q4":
            continue
        temp = df.copy()
        temp["question_id"] = temp.get("question_id", q)
        if "term" not in temp.columns and "predictor" in temp.columns:
            temp = temp.rename(columns={"predictor": "term"})
        if "estimate" not in temp.columns and "coefficient" in temp.columns:
            temp = temp.rename(columns={"coefficient": "estimate"})
        if "term" in temp.columns and "estimate" in temp.columns:
            frames.append(temp[["question_id", "outcome", "term", "estimate"]].dropna())
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def build_country_model_contributions(fm: pd.DataFrame, results: dict[str, pd.DataFrame]) -> pd.DataFrame:
    coefs = extract_coefficients(results)
    rows = []
    if coefs.empty:
        return pd.DataFrame()

    for _, coef in coefs.iterrows():
        term = coef["term"]
        if term not in fm.columns or str(term).lower() in {"const", "intercept"}:
            continue

        s = pd.to_numeric(fm[term], errors="coerce")
        if s.std(skipna=True) and s.std(skipna=True) > 0:
            term_z = (s - s.mean(skipna=True)) / s.std(skipna=True)
        else:
            term_z = pd.Series([pd.NA] * len(fm), index=fm.index)

        for idx, r in fm.iterrows():
            contribution = term_z.loc[idx] * coef["estimate"] if pd.notna(term_z.loc[idx]) else pd.NA
            rows.append({
                "iso3": r["iso3"],
                "country_name": r.get("country_name_canonical", r.get("country_name", "")),
                "question_id": coef["question_id"],
                "outcome": coef["outcome"],
                "model_id": "phase6_primary_or_available",
                "term": term,
                "term_value": r.get(term),
                "term_percentile": s.rank(pct=True).loc[idx] if pd.notna(r.get(term)) else pd.NA,
                "coefficient_or_weight": coef["estimate"],
                "standardized_contribution": contribution,
                "contribution_direction": "positive" if pd.notna(contribution) and contribution > 0 else ("negative" if pd.notna(contribution) and contribution < 0 else "neutral_or_missing"),
                "contribution_rank_within_country": pd.NA,
                "contribution_label": "descriptive_driver_not_causal",
                "driver_type": "model_term",
                "interpretation": "Descriptive contribution based on in-sample model coefficient and country value; not causal.",
                "causal_claim": False,
            })

    out = pd.DataFrame(rows)
    if not out.empty:
        out["abs_contribution"] = pd.to_numeric(out["standardized_contribution"], errors="coerce").abs()
        out["contribution_rank_within_country"] = out.groupby(["iso3", "question_id", "outcome"])["abs_contribution"].rank(ascending=False, method="min")
    return out
```

---

## Paso 7 — Crear `_residuals.py`

Responsabilidades:

- calcular observado vs esperado cuando sea posible;
- detectar overperformers/underperformers;
- producir gaps.

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm


DEFAULT_CONTROLS = ["wb_gdp_per_capita_ppp_log", "wb_internet_penetration", "wb_government_effectiveness"]
DEFAULT_TERMS = ["n_binding", "n_non_binding", "regulatory_intensity"]


def fit_simple_prediction(fm: pd.DataFrame, outcome: str):
    predictors = [c for c in DEFAULT_TERMS + DEFAULT_CONTROLS if c in fm.columns]
    if outcome not in fm.columns or not predictors:
        return None, pd.DataFrame()

    sub = fm[["iso3", "country_name_canonical", outcome] + predictors].dropna()
    if len(sub) < max(12, len(predictors) * 4):
        return None, sub

    X = sm.add_constant(sub[predictors], has_constant="add")
    y = sub[outcome]
    model = sm.OLS(y, X).fit(cov_type="HC3")
    sub = sub.copy()
    sub["fitted_value"] = model.predict(X)
    sub["residual"] = y - sub["fitted_value"]
    return model, sub


def build_country_residuals_and_gaps(fm: pd.DataFrame, outcomes_by_q: dict) -> pd.DataFrame:
    rows = []
    for q, outcomes in outcomes_by_q.items():
        if q == "Q4":
            continue
        for outcome in outcomes:
            model, sub = fit_simple_prediction(fm, outcome)
            if model is None or sub.empty:
                continue
            best = sub[outcome].max()
            chile_val = sub.loc[sub["iso3"].eq("CHL"), outcome]
            sgp_val = sub.loc[sub["iso3"].eq("SGP"), outcome]
            chile_val = chile_val.iloc[0] if not chile_val.empty else pd.NA
            sgp_val = sgp_val.iloc[0] if not sgp_val.empty else pd.NA

            sub["absolute_residual"] = sub["residual"].abs()
            sub["residual_rank"] = sub["absolute_residual"].rank(ascending=False, method="min")
            sub["residual_percentile"] = sub["absolute_residual"].rank(pct=True)
            for _, r in sub.iterrows():
                label = "overperformer" if r["residual"] > 0 else ("underperformer" if r["residual"] < 0 else "as_expected")
                rows.append({
                    "iso3": r["iso3"],
                    "country_name": r["country_name_canonical"],
                    "question_id": q,
                    "outcome": outcome,
                    "model_id": "simple_adjusted_internal",
                    "observed_value": r[outcome],
                    "fitted_value": r["fitted_value"],
                    "residual": r["residual"],
                    "absolute_residual": r["absolute_residual"],
                    "residual_rank": r["residual_rank"],
                    "residual_percentile": r["residual_percentile"],
                    "overperformer_underperformer": label,
                    "gap_vs_best": best - r[outcome],
                    "gap_vs_group_best": best - r[outcome],
                    "gap_vs_chile": r[outcome] - chile_val if pd.notna(chile_val) else pd.NA,
                    "gap_vs_singapore": r[outcome] - sgp_val if pd.notna(sgp_val) else pd.NA,
                    "interpretation": "Observed minus fitted within in-sample descriptive model; not causal.",
                })
    return pd.DataFrame(rows)
```

---

## Paso 8 — Crear `_learning_patterns.py`

Responsabilidades:

- identificar patrones de pioneros y rezagados;
- generar lecciones para Chile;
- marcar cautelas.

```python
import pandas as pd


def build_headline_flags(profile_wide: pd.DataFrame) -> pd.DataFrame:
    out = profile_wide[["iso3", "country_name"]].copy()
    q_cols = [c for c in profile_wide.columns if c.endswith("_percentile")]

    for q in ["Q1", "Q2", "Q3", "Q5", "Q6"]:
        col = f"{q}_percentile"
        if col in profile_wide.columns:
            out[f"is_top_5_{q.lower()}"] = profile_wide[col].rank(ascending=False, method="min") <= 5
            out[f"is_bottom_5_{q.lower()}"] = profile_wide[col].rank(ascending=True, method="min") <= 5

    out["is_consistent_pioneer"] = profile_wide[q_cols].ge(0.75).sum(axis=1) >= 3
    out["is_consistent_laggard"] = profile_wide[q_cols].le(0.25).sum(axis=1) >= 3
    out["is_chile_benchmark"] = profile_wide["iso3"].isin(["SGP", "EST", "IRL", "ARE", "KOR", "URY", "BRA"])
    out["is_latam_leader"] = False
    if "region" in profile_wide.columns:
        latam = profile_wide["region"].astype(str).str.contains("Latin", case=False, na=False)
        max_score = profile_wide.loc[latam, "overall_country_profile_score"].max()
        out["is_latam_leader"] = latam & profile_wide["overall_country_profile_score"].eq(max_score)

    out["headline_candidate"] = out[["is_consistent_pioneer", "is_consistent_laggard", "is_chile_benchmark", "is_latam_leader"]].any(axis=1)
    out["suggested_headline"] = out.apply(
        lambda r: "caso pionero consistente" if r["is_consistent_pioneer"] else (
            "caso rezagado para aprendizaje de errores" if r["is_consistent_laggard"] else (
                "benchmark relevante para Chile" if r["is_chile_benchmark"] else ""
            )
        ),
        axis=1
    )
    out["caution_note"] = "Descriptive flag; verify robustness in Fase 7."
    return out


def build_learning_patterns(profile_wide: pd.DataFrame, best_worst: pd.DataFrame) -> pd.DataFrame:
    rows = []

    pioneers = profile_wide[profile_wide["overall_country_profile_label"].isin(["top_pioneer", "high_performer"])]
    laggards = profile_wide[profile_wide["overall_country_profile_label"].isin(["bottom_laggard", "low_performer"])]

    rows.append({
        "pattern_id": "global_pioneer_pattern",
        "question_id": "Q_ALL",
        "group_name": "global_43",
        "pattern_type": "pioneer_pattern",
        "countries_in_pattern": ";".join(pioneers["iso3"].head(10).tolist()),
        "shared_strengths": "high percentiles across multiple Q dimensions",
        "shared_weaknesses": "must be assessed country-by-country",
        "regulatory_profile_summary": "see Q4 cluster profile",
        "ecosystem_profile_summary": "multi-dimensional high performance",
        "lesson_for_chile": "study institutional, adoption and public-sector capabilities of high performers before copying legal form",
        "risk_of_overinterpretation": "Do not infer causality from descriptive ranking.",
        "evidence_strength": "pre_robustness_descriptive",
        "recommended_phase8_use": "benchmark cases after Fase 7 validation",
    })

    rows.append({
        "pattern_id": "global_laggard_pattern",
        "question_id": "Q_ALL",
        "group_name": "global_43",
        "pattern_type": "laggard_pattern",
        "countries_in_pattern": ";".join(laggards["iso3"].head(10).tolist()),
        "shared_strengths": "",
        "shared_weaknesses": "low percentiles across multiple Q dimensions",
        "regulatory_profile_summary": "see Q4 cluster profile",
        "ecosystem_profile_summary": "multi-dimensional lower performance",
        "lesson_for_chile": "identify recurring capability gaps and avoid assuming law alone solves ecosystem weaknesses",
        "risk_of_overinterpretation": "Poor ranking may reflect missingness or structural factors outside regulation.",
        "evidence_strength": "pre_robustness_descriptive",
        "recommended_phase8_use": "warning cases after Fase 7 validation",
    })

    return pd.DataFrame(rows)
```

---

## Paso 9 — Crear `_graphics.py`

Responsabilidades:

- generar gráficos profesionales;
- guardar PNG y SVG;
- no depender de notebooks;
- crear catálogo de figuras.

Usar `matplotlib` y opcionalmente `seaborn`. Si el entorno no tiene seaborn, usar matplotlib puro.

```python
from pathlib import Path
import textwrap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HIGHLIGHTS = {"CHL", "SGP", "EST", "IRL", "ARE", "USA", "CHN", "BRA", "URY"}


def _savefig(fig, path_base: Path):
    path_base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path_base.with_suffix(".png"), dpi=180, bbox_inches="tight")
    fig.savefig(path_base.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def plot_q_ranking(rankings: pd.DataFrame, question_id: str, outdir: Path):
    q = rankings[rankings["question_id"] == question_id].copy()
    if q.empty:
        return []

    # Si hay múltiples outcomes por Q, usar promedio por país.
    agg = (
        q.groupby(["iso3", "country_name"], dropna=False)
         .agg(percentile=("percentile", "mean"))
         .reset_index()
         .sort_values("percentile", ascending=True)
    )
    fig, ax = plt.subplots(figsize=(9, max(6, len(agg) * 0.18)))
    y = range(len(agg))
    colors = ["black" if iso in HIGHLIGHTS else "gray" for iso in agg["iso3"]]
    ax.barh(y, agg["percentile"], color=colors, alpha=0.75)
    ax.set_yticks(y)
    ax.set_yticklabels([f"{r.iso3} — {r.country_name}" for r in agg.itertuples()], fontsize=7)
    ax.set_xlim(0, 1)
    ax.set_xlabel("Percentil descriptivo dentro de la muestra")
    ax.set_title(f"{question_id}: ranking país por desempeño relativo", fontsize=13)
    ax.text(
        0, -1.4,
        "Nota: posicionamiento descriptivo in-sample; no es predicción independiente ni causalidad.",
        fontsize=8
    )
    path = outdir / "q_rankings" / f"{question_id.lower()}_ranking"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def plot_heatmap_country_by_q(profile_wide: pd.DataFrame, outdir: Path):
    q_cols = [c for c in profile_wide.columns if c.endswith("_percentile")]
    if not q_cols:
        return []

    df = profile_wide.sort_values("overall_country_profile_score", ascending=False).copy()
    mat = df[q_cols].astype(float).values
    fig, ax = plt.subplots(figsize=(8, max(7, len(df) * 0.18)))
    im = ax.imshow(mat, aspect="auto", vmin=0, vmax=1)
    ax.set_yticks(range(len(df)))
    ax.set_yticklabels([f"{r.iso3} — {r.country_name}" for r in df.itertuples()], fontsize=7)
    ax.set_xticks(range(len(q_cols)))
    ax.set_xticklabels([c.replace("_percentile", "") for c in q_cols], rotation=45, ha="right")
    ax.set_title("Mapa comparado país × pregunta: percentiles descriptivos", fontsize=13)
    fig.colorbar(im, ax=ax, label="Percentil")
    ax.text(
        0, -2.5,
        "Nota: ranking descriptivo dentro de la muestra preregistrada; no es causalidad.",
        fontsize=8
    )
    path = outdir / "q_heatmaps" / "heatmap_country_by_q_percentiles"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def plot_country_radar(profile_wide: pd.DataFrame, iso3: str, outdir: Path):
    row = profile_wide[profile_wide["iso3"] == iso3]
    if row.empty:
        return []
    row = row.iloc[0]
    q_cols = [c for c in profile_wide.columns if c.endswith("_percentile")]
    labels = [c.replace("_percentile", "") for c in q_cols]
    values = [row[c] if pd.notna(row[c]) else 0 for c in q_cols]
    if not values:
        return []

    angles = np.linspace(0, 2*np.pi, len(values), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.20)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1)
    ax.set_title(f"{iso3} — perfil Q1–Q6", fontsize=13)
    fig.text(
        0.1, 0.02,
        "Nota: percentiles descriptivos in-sample; no causalidad ni predicción independiente.",
        fontsize=8
    )
    path = outdir / "country_cards" / f"{iso3}_country_card_radar"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def plot_chile_vs_singapore(profile_wide: pd.DataFrame, outdir: Path):
    sub = profile_wide[profile_wide["iso3"].isin(["CHL", "SGP"])].copy()
    q_cols = [c for c in profile_wide.columns if c.endswith("_percentile")]
    if len(sub) < 2 or not q_cols:
        return []

    fig, ax = plt.subplots(figsize=(8, 5))
    x = range(len(q_cols))
    for _, r in sub.iterrows():
        ax.plot(x, [r[c] for c in q_cols], marker="o", label=f"{r['iso3']} — {r['country_name']}")
    ax.set_xticks(x)
    ax.set_xticklabels([c.replace("_percentile", "") for c in q_cols], rotation=45, ha="right")
    ax.set_ylim(0, 1)
    ax.set_ylabel("Percentil")
    ax.set_title("Chile vs Singapur — perfil comparado Q1–Q6")
    ax.legend()
    ax.text(
        0, -0.22,
        "Nota: comparación descriptiva dentro de la muestra; validar robustez en Fase 7.",
        transform=ax.transAxes,
        fontsize=8
    )
    path = outdir / "chile_vs_benchmarks" / "chile_vs_singapore_q_profile"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def build_graphics(rankings, profile_wide, outdir: Path) -> pd.DataFrame:
    paths = []
    paths += plot_heatmap_country_by_q(profile_wide, outdir)
    for q in ["Q1", "Q2", "Q3", "Q5", "Q6"]:
        paths += plot_q_ranking(rankings, q, outdir)
    for iso in ["SGP", "CHL", "EST", "IRL", "ARE", "KOR", "USA", "CHN", "BRA", "URY"]:
        paths += plot_country_radar(profile_wide, iso, outdir)
    paths += plot_chile_vs_singapore(profile_wide, outdir)
    return pd.DataFrame({
        "figure_path": paths,
        "figure_type": [Path(p).parent.name for p in paths],
        "methodology_note": "descriptive in-sample positioning; not causal or external prediction",
    })
```

---

## Paso 10 — Crear `_country_cards.py`

Responsabilidades:

- exportar datos de country cards;
- una tarjeta por país clave.

```python
from pathlib import Path
import pandas as pd


KEY_COUNTRIES = ["CHL", "SGP", "EST", "IRL", "ARE", "KOR", "JPN", "USA", "CHN", "BRA", "URY"]


def write_country_card_data(
    profile_wide: pd.DataFrame,
    profile_long: pd.DataFrame,
    rankings_group: pd.DataFrame,
    contributions: pd.DataFrame,
    residuals: pd.DataFrame,
    outdir: Path,
):
    card_dir = outdir / "country_cards_data"
    card_dir.mkdir(parents=True, exist_ok=True)

    written = []
    for iso in KEY_COUNTRIES:
        pieces = []
        pw = profile_wide[profile_wide["iso3"] == iso].copy()
        if not pw.empty:
            pw["section"] = "summary"
            pieces.append(pw)

        pl = profile_long[profile_long["iso3"] == iso].copy()
        if not pl.empty:
            pl["section"] = "q_profile_long"
            pieces.append(pl)

        rg = rankings_group[rankings_group["iso3"] == iso].copy()
        if not rg.empty:
            rg["section"] = "group_rankings"
            pieces.append(rg)

        co = contributions[contributions["iso3"] == iso].copy() if not contributions.empty else pd.DataFrame()
        if not co.empty:
            co["section"] = "model_contributions"
            pieces.append(co)

        rs = residuals[residuals["iso3"] == iso].copy() if not residuals.empty else pd.DataFrame()
        if not rs.empty:
            rs["section"] = "residuals"
            pieces.append(rs)

        if pieces:
            # Exportar varias tablas en formato long común con columnas union.
            card = pd.concat(pieces, ignore_index=True, sort=False)
            path = card_dir / f"{iso}_country_card_data.csv"
            card.to_csv(path, index=False)
            written.append(str(path))

    readme = card_dir / "README_country_cards.md"
    readme.write_text(
        "# Country cards data\n\n"
        "Estos archivos consolidan datos descriptivos país-por-país para Fase 8. "
        "No son predicciones independientes ni inferencias causales.\n",
        encoding="utf-8"
    )
    return written
```

---

## Paso 11 — Crear `run_country_intelligence.py`

Orquestador principal.

```python
from pathlib import Path
import json
import pandas as pd
import yaml
from datetime import datetime, timezone

from ._load import ROOT, FASE5_BUNDLE, FASE6_OUTPUTS, CI_OUTPUTS, validate_preflight
from ._groups import build_group_membership
from ._rankings import rank_outcome, build_rankings_by_group, build_best_worst_by_q
from ._profiles import build_country_q_profile_long, build_country_q_profile_wide
from ._contributions import build_country_model_contributions
from ._residuals import build_country_residuals_and_gaps
from ._learning_patterns import build_headline_flags, build_learning_patterns
from ._graphics import build_graphics
from ._country_cards import write_country_card_data


OUTCOMES_BY_Q = {
    "Q1": [
        "oxford_ind_company_investment_emerging_tech",
        "oxford_ind_ai_unicorns_log",
        "oxford_ind_vc_availability",
        "wipo_c_vencapdeal_score",
    ],
    "Q2": [
        "ms_h2_2025_ai_diffusion_pct",
        "oecd_5_ict_business_oecd_biz_ai_pct",
        "anthropic_usage_pct",
        "oxford_public_sector_adoption",
        "oxford_ind_adoption_emerging_tech",
    ],
    "Q3": [
        "oxford_total_score",
        "wipo_out_score",
        "stanford_fig_6_3_5_volume_of_publications",
        "stanford_fig_6_3_4_ai_patent_count",
    ],
    "Q5": [
        "anthropic_usage_pct",
        "anthropic_collaboration_pct",
        "oxford_ind_adoption_emerging_tech",
    ],
    "Q6": [
        "oxford_public_sector_adoption",
        "oxford_e_government_delivery",
        "oxford_government_digital_policy",
        "oxford_ind_data_governance",
        "oxford_governance_ethics",
        "oecd_2_indigo_oecd_indigo_score",
        "oecd_4_digital_gov_oecd_digital_gov_overall",
    ],
}

QUESTION_LABELS = {
    "Q1": "Inversión",
    "Q2": "Adopción",
    "Q3": "Innovación",
    "Q4": "Perfil regulatorio",
    "Q5": "Uso poblacional",
    "Q6": "Sector público",
}


def load_config():
    path = ROOT / "FASE6" / "config" / "phase6_2_country_intelligence.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_phase6_results():
    files = {
        "Q1": "q1_results.csv",
        "Q2": "q2_results.csv",
        "Q3": "q3_results.csv",
        "Q5": "q5_results.csv",
        "Q6": "q6_results.csv",
    }
    out = {}
    for q, fname in files.items():
        path = FASE6_OUTPUTS / fname
        if path.exists():
            out[q] = pd.read_csv(path)
    return out


def main():
    CI_OUTPUTS.mkdir(parents=True, exist_ok=True)
    (CI_OUTPUTS / "figures").mkdir(parents=True, exist_ok=True)

    preflight = validate_preflight()
    preflight.to_csv(CI_OUTPUTS / "phase6_2_quality_checks.csv", index=False)
    if ((preflight["status"] == "FAIL") & (preflight["severity"] == "P0")).any():
        raise RuntimeError("Fase 6.2 abortada por fallas P0 en pre-flight.")

    config = load_config()
    fm = pd.read_csv(FASE5_BUNDLE / "phase6_feature_matrix.csv")
    membership = pd.read_csv(FASE5_BUNDLE / "phase6_analysis_sample_membership.csv")
    clusters = pd.read_csv(FASE6_OUTPUTS / "q4_clusters.csv") if (FASE6_OUTPUTS / "q4_clusters.csv").exists() else pd.DataFrame()
    phase6_results = load_phase6_results()

    # Construir rankings por outcomes observados en feature matrix.
    ranking_frames = []
    for q, outcomes in OUTCOMES_BY_Q.items():
        for outcome in outcomes:
            if outcome in fm.columns:
                ranking_frames.append(rank_outcome(
                    df=fm,
                    outcome=outcome,
                    question_id=q,
                    question_label=QUESTION_LABELS.get(q, q),
                    higher_is_better=True,
                ))
    rankings = pd.concat(ranking_frames, ignore_index=True) if ranking_frames else pd.DataFrame()
    rankings.to_csv(CI_OUTPUTS / "country_rankings_by_outcome.csv", index=False)

    group_membership = build_group_membership(membership, config)
    rankings_group = build_rankings_by_group(rankings, group_membership) if not rankings.empty else pd.DataFrame()
    rankings_group.to_csv(CI_OUTPUTS / "country_rankings_by_group.csv", index=False)

    best_worst = build_best_worst_by_q(rankings, rankings_group) if not rankings.empty else pd.DataFrame()
    best_worst.to_csv(CI_OUTPUTS / "country_best_worst_by_q.csv", index=False)

    profile_long = build_country_q_profile_long(rankings) if not rankings.empty else pd.DataFrame()
    profile_long.to_csv(CI_OUTPUTS / "country_q_profile_long.csv", index=False)

    profile_wide = build_country_q_profile_wide(profile_long, clusters=clusters) if not profile_long.empty else pd.DataFrame()
    profile_wide.to_csv(CI_OUTPUTS / "country_q_profile_wide.csv", index=False)

    contributions = build_country_model_contributions(fm, phase6_results)
    contributions.to_csv(CI_OUTPUTS / "country_model_contributions.csv", index=False)

    residuals = build_country_residuals_and_gaps(fm, OUTCOMES_BY_Q)
    residuals.to_csv(CI_OUTPUTS / "country_residuals_and_gaps.csv", index=False)

    cluster_profile = clusters.copy()
    if not cluster_profile.empty:
        cluster_profile["score_scope"] = "descriptive_regulatory_typology"
        cluster_profile["independent_prediction"] = False
        cluster_profile["causal_claim"] = False
    cluster_profile.to_csv(CI_OUTPUTS / "country_cluster_profile.csv", index=False)

    headline_flags = build_headline_flags(profile_wide) if not profile_wide.empty else pd.DataFrame()
    headline_flags.to_csv(CI_OUTPUTS / "country_headline_flags.csv", index=False)

    learning = build_learning_patterns(profile_wide, best_worst) if not profile_wide.empty else pd.DataFrame()
    learning.to_csv(CI_OUTPUTS / "country_learning_patterns.csv", index=False)

    # Comparaciones de pares: Chile vs benchmarks.
    pairs = []
    if not profile_wide.empty:
        chile = profile_wide[profile_wide["iso3"] == "CHL"]
        for iso in config.get("country_groups", {}).get("chile_priority_benchmarks", []):
            other = profile_wide[profile_wide["iso3"] == iso]
            if not chile.empty and not other.empty:
                for c in [col for col in profile_wide.columns if col.endswith("_percentile")]:
                    pairs.append({
                        "country_a": "CHL",
                        "country_b": iso,
                        "dimension": c.replace("_percentile", ""),
                        "country_a_percentile": chile[c].iloc[0],
                        "country_b_percentile": other[c].iloc[0],
                        "gap_b_minus_a": other[c].iloc[0] - chile[c].iloc[0],
                        "interpretation": "positive gap means benchmark above Chile",
                    })
    pd.DataFrame(pairs).to_csv(CI_OUTPUTS / "country_comparison_pairs.csv", index=False)

    figures = build_graphics(rankings, profile_wide, CI_OUTPUTS / "figures") if not profile_wide.empty else pd.DataFrame()
    figures.to_csv(CI_OUTPUTS / "country_graphics_catalog.csv", index=False)

    written_cards = write_country_card_data(
        profile_wide=profile_wide,
        profile_long=profile_long,
        rankings_group=rankings_group,
        contributions=contributions,
        residuals=residuals,
        outdir=CI_OUTPUTS,
    )

    manifest = {
        "fase6_2_version": "2.2",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "module": "country_intelligence_layer",
        "methodology": "inferential_comparative_observational",
        "scope": "descriptive_country_level_positioning",
        "holdout_used": False,
        "train_test_split_used": False,
        "external_validation_used": False,
        "independent_prediction": False,
        "causal_claim": False,
        "preserved_existing_fase6_outputs": True,
        "outputs": {
            "country_q_profile_long.csv": "country_question_outcome_long_profile",
            "country_q_profile_wide.csv": "one_row_per_country_summary",
            "country_rankings_by_outcome.csv": "global_rankings_by_outcome",
            "country_rankings_by_group.csv": "subsample_group_rankings",
            "country_best_worst_by_q.csv": "top_bottom_by_question",
            "country_model_contributions.csv": "descriptive_model_term_contributions",
            "country_residuals_and_gaps.csv": "observed_vs_fitted_and_gaps",
            "country_cluster_profile.csv": "q4_regulatory_profile",
            "country_headline_flags.csv": "narrative_candidate_flags",
            "country_learning_patterns.csv": "lessons_from_pioneers_and_laggards",
            "country_graphics_catalog.csv": "generated_figures_catalog",
        },
        "key_country_cards_written": written_cards,
        "n_countries_profiled": int(profile_wide["iso3"].nunique()) if not profile_wide.empty else 0,
        "n_figures": int(len(figures)) if not figures.empty else 0,
    }
    (CI_OUTPUTS / "phase6_2_country_intelligence_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    return manifest


if __name__ == "__main__":
    main()
```

---

## Paso 12 — Tests obligatorios

Crear:

```text
FASE6/tests/test_phase6_2_country_intelligence.py
```

Contenido mínimo:

```python
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
CI = ROOT / "FASE6" / "outputs" / "country_intelligence"


def test_country_intelligence_outputs_exist():
    required = [
        "country_q_profile_long.csv",
        "country_q_profile_wide.csv",
        "country_rankings_by_outcome.csv",
        "country_rankings_by_group.csv",
        "country_best_worst_by_q.csv",
        "country_model_contributions.csv",
        "country_residuals_and_gaps.csv",
        "country_cluster_profile.csv",
        "country_headline_flags.csv",
        "country_learning_patterns.csv",
        "country_graphics_catalog.csv",
        "phase6_2_country_intelligence_manifest.json",
    ]
    for fname in required:
        assert (CI / fname).exists(), fname


def test_country_profiles_include_chile_and_singapore():
    wide = pd.read_csv(CI / "country_q_profile_wide.csv")
    assert "CHL" in set(wide["iso3"])
    assert "SGP" in set(wide["iso3"])


def test_country_profile_semantics():
    long = pd.read_csv(CI / "country_q_profile_long.csv")
    assert "score_scope" in long.columns
    assert long["score_scope"].eq("in_sample_descriptive_positioning").all()
    assert "independent_prediction" in long.columns
    assert long["independent_prediction"].fillna(False).eq(False).all()
    assert "causal_claim" in long.columns
    assert long["causal_claim"].fillna(False).eq(False).all()


def test_rankings_have_questions():
    rankings = pd.read_csv(CI / "country_rankings_by_outcome.csv")
    assert set(["Q1", "Q2", "Q3", "Q5", "Q6"]).intersection(set(rankings["question_id"]))


def test_group_rankings_exist():
    group = pd.read_csv(CI / "country_rankings_by_group.csv")
    assert "group_name" in group.columns
    assert "rank_within_group" in group.columns


def test_manifest_no_causal_or_prediction_claims():
    manifest = json.loads((CI / "phase6_2_country_intelligence_manifest.json").read_text())
    assert manifest["holdout_used"] is False
    assert manifest["train_test_split_used"] is False
    assert manifest["external_validation_used"] is False
    assert manifest["independent_prediction"] is False
    assert manifest["causal_claim"] is False


def test_graphics_catalog_not_empty():
    catalog = pd.read_csv(CI / "country_graphics_catalog.csv")
    assert len(catalog) > 0
```

---

## 13. README para Fase 6.2

Crear:

```text
FASE6/outputs/country_intelligence/README.md
```

Contenido:

```markdown
# Fase 6.2 — Country Intelligence Layer

Esta carpeta contiene la capa país-por-país de Fase 6. Su objetivo es traducir los resultados de modelos generales en perfiles comparados por país para Q1–Q6.

## Qué contiene

- Rankings globales por outcome.
- Rankings por submuestra.
- Perfiles país por Q.
- Mejores y peores países por dimensión.
- Drivers descriptivos.
- Residuales y brechas.
- Country cards data.
- Gráficos profesionales.

## Qué NO contiene

- Predicciones independientes.
- Validación externa.
- Causalidad fuerte.
- Recomendaciones políticas finales.

## Cómo interpretar

Los scores, rankings y percentiles son posicionamiento descriptivo dentro de la muestra preregistrada. Deben pasar por Fase 7 antes de ser usados como hallazgos robustos en Fase 8.
```

---

## 14. Comandos finales de ejecución

Desde la raíz del proyecto:

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP

# 1. Ejecutar Country Intelligence Layer
python3 -m FASE6.src.country_intelligence.run_country_intelligence

# 2. Ejecutar tests
python3 -m pytest FASE6/tests/test_phase6_2_country_intelligence.py -q

# 3. Validar outputs rápidos
python3 - <<'PY'
from pathlib import Path
import pandas as pd
import json

ci = Path("FASE6/outputs/country_intelligence")

required = [
    "country_q_profile_long.csv",
    "country_q_profile_wide.csv",
    "country_rankings_by_outcome.csv",
    "country_rankings_by_group.csv",
    "country_best_worst_by_q.csv",
    "country_headline_flags.csv",
    "country_learning_patterns.csv",
    "country_graphics_catalog.csv",
    "phase6_2_country_intelligence_manifest.json",
]

for fname in required:
    assert (ci / fname).exists(), f"Falta {fname}"

wide = pd.read_csv(ci / "country_q_profile_wide.csv")
assert "CHL" in set(wide["iso3"])
assert "SGP" in set(wide["iso3"])

long = pd.read_csv(ci / "country_q_profile_long.csv")
assert long["independent_prediction"].fillna(False).eq(False).all()
assert long["causal_claim"].fillna(False).eq(False).all()

manifest = json.loads((ci / "phase6_2_country_intelligence_manifest.json").read_text())
assert manifest["external_validation_used"] is False
assert manifest["causal_claim"] is False
assert manifest["independent_prediction"] is False

print("PASS: Fase 6.2 Country Intelligence Layer OK")
PY
```

---

## 15. Criterios de aceptación

Fase 6.2 está completa solo si:

### 15.1 Preservación

- [ ] Los 11 outputs originales de Fase 6 siguen existiendo.
- [ ] Ningún output original fue sobrescrito con semántica distinta.
- [ ] `fase6_manifest.json` sigue declarando no holdout, no split, no external validation.

### 15.2 Outputs nuevos

- [ ] Existe `country_q_profile_long.csv`.
- [ ] Existe `country_q_profile_wide.csv`.
- [ ] Existe `country_rankings_by_outcome.csv`.
- [ ] Existe `country_rankings_by_group.csv`.
- [ ] Existe `country_best_worst_by_q.csv`.
- [ ] Existe `country_model_contributions.csv`.
- [ ] Existe `country_residuals_and_gaps.csv`.
- [ ] Existe `country_cluster_profile.csv`.
- [ ] Existe `country_headline_flags.csv`.
- [ ] Existe `country_learning_patterns.csv`.
- [ ] Existe `country_graphics_catalog.csv`.
- [ ] Existe `phase6_2_country_intelligence_manifest.json`.

### 15.3 Países clave

- [ ] Chile aparece en perfiles.
- [ ] Singapur aparece en perfiles.
- [ ] Estonia aparece si está en muestra.
- [ ] Irlanda aparece si está en muestra.
- [ ] Emiratos aparece si está en muestra.
- [ ] Brasil y Uruguay aparecen si están en muestra.

### 15.4 Rankings

- [ ] Hay rankings para Q1.
- [ ] Hay rankings para Q2.
- [ ] Hay rankings para Q3.
- [ ] Hay rankings para Q5.
- [ ] Hay rankings para Q6.
- [ ] Hay ranking por grupo o submuestra.
- [ ] Hay top/bottom por Q.

### 15.5 Gráficos

- [ ] Existe heatmap país × Q.
- [ ] Existe ranking Q1.
- [ ] Existe ranking Q2.
- [ ] Existe ranking Q3.
- [ ] Existe ranking Q5.
- [ ] Existe ranking Q6.
- [ ] Existe country card radar de Singapur.
- [ ] Existe country card radar de Chile.
- [ ] Existe gráfico Chile vs Singapur.
- [ ] Existe catálogo de figuras.

### 15.6 Semántica

- [ ] Todos los perfiles declaran `independent_prediction = false`.
- [ ] Todos los perfiles declaran `causal_claim = false`.
- [ ] Todos los scores declaran `score_scope = in_sample_descriptive_positioning`.
- [ ] README advierte que Fase 7 debe validar robustez.
- [ ] No se usa lenguaje de causalidad fuerte.

---

## 16. Errores que obligan a rechazar la actualización

### P0 — Rechazo inmediato

- Se borran outputs originales de Fase 6.
- Se crea o usa `train/test split`.
- Se afirma causalidad país-por-país.
- Se llama predicción independiente a los scores.
- No aparece Chile.
- No aparece Singapur.
- No se genera `country_q_profile_wide.csv`.
- No se genera `phase6_2_country_intelligence_manifest.json`.

### P1 — Corrección obligatoria antes de Fase 7

- Falta algún gráfico clave.
- No hay rankings por grupo.
- No hay best/worst por Q.
- Q4 se presenta como ranking normativo sin cautela.
- Los drivers se interpretan causalmente.
- No se documenta missingness.

### P2 — Mejora recomendada

- Gráficos poco elegantes.
- Nombres de columnas mejorables.
- Faltan SVG pero existen PNG.
- Falta algún país no prioritario por missingness documentada.

---

## 17. Cómo debería verse la respuesta sobre Singapur después de Fase 6.2

Fase 6.2 debe permitir generar una ficha técnica como esta:

```markdown
## Singapore — Country Card preliminar

### Posición general
Singapur aparece como país de alto desempeño relativo dentro de la muestra, especialmente en adopción tecnológica y capacidad pública digital.

### Q1 Inversión
- Percentil descriptivo: X
- Ranking global: X/43
- Lectura: alto/medio/bajo desempeño relativo.

### Q2 Adopción
- Percentil descriptivo: X
- Ranking global: X/43
- Lectura: uno de los líderes de adopción.

### Q3 Innovación
- Percentil descriptivo: X
- Ranking global: X/43

### Q4 Perfil regulatorio
- Cluster: X
- Perfil: soft-law / binding / hybrid / project-stage según datos disponibles.
- Cautela: Q4 es tipología descriptiva, no ranking normativo.

### Q5 Uso poblacional
- Percentil descriptivo: X
- Ranking global: X/43

### Q6 Sector público
- Percentil descriptivo: X
- Ranking global: X/43

### Lecciones preliminares para Chile
Singapur debe estudiarse como benchmark de capacidades digitales, adopción pública y gobernanza operativa. No debe concluirse que su desempeño se debe causalmente a una sola variable regulatoria. La robustez de esta lectura debe evaluarse en Fase 7.
```

---

## 18. Cómo debería verse la respuesta sobre mejores y peores

Fase 6.2 debe permitir responder:

```markdown
## Mejores por Q2 — Adopción

1. País A — alto score de difusión IA, alto uso poblacional y fuerte adopción emergente.
2. País B — alto uso en empresas y sector público.
3. País C — fuerte adopción tecnológica pero menor uso poblacional.

### Lección para Chile
Los pioneros no solo tienen regulación; combinan infraestructura, adopción privada, capacidades estatales y/o ecosistema digital.

## Peores por Q2 — Adopción

1. País X — bajo uso en empresas y bajo score de adopción.
2. País Y — bajo uso poblacional y baja difusión.
3. País Z — datos incompletos o baja adopción observada.

### Riesgo a evitar
No basta con aprobar una ley si no existe capacidad de adopción, infraestructura digital y gobernanza operativa.
```

---

## 19. Relación con Fase 7

Después de Fase 6.2, Fase 7 debe usar estos nuevos archivos:

```text
country_q_profile_long.csv
country_q_profile_wide.csv
country_rankings_by_outcome.csv
country_rankings_by_group.csv
country_best_worst_by_q.csv
country_model_contributions.csv
country_residuals_and_gaps.csv
country_headline_flags.csv
country_learning_patterns.csv
```

Fase 7 debe validar:

```text
¿los líderes siguen siendo líderes al excluir outliers?
¿Chile vs Singapur es estable bajo diferentes especificaciones?
¿los peores son realmente rezagados o tienen missingness?
¿los patterns de pioneros sobreviven a sensibilidad?
¿Q4 cluster cambia si se excluyen países influyentes?
```

---

## 20. Relación con Fase 8

Fase 8 debe usar la Fase 6.2 para crear:

```text
Country Cards
Benchmark Briefs
Chile vs Pioneers
Lessons from leaders
Mistakes from laggards
Executive charts
Policy recommendations
```

Pero Fase 8 solo puede usar como hallazgo principal aquello que Fase 7 marque como:

```text
stable
directionally_stable
```

Si Fase 7 marca algo como:

```text
fragile
not_estimable
```

Fase 8 debe usarlo solo como cautela o anexo, no como argumento central.

---

## 21. Reporte final esperado del LLM ejecutor

Al terminar, el LLM debe entregar:

```text
FASE 6.2 — COUNTRY INTELLIGENCE LAYER — REPORTE DE EJECUCIÓN

1. Preservación de outputs Fase 6
- 11 outputs originales presentes: PASS/FAIL
- Ningún archivo original sobrescrito: PASS/FAIL

2. Outputs nuevos
- country_q_profile_long.csv: shape=(...)
- country_q_profile_wide.csv: shape=(...)
- country_rankings_by_outcome.csv: shape=(...)
- country_rankings_by_group.csv: shape=(...)
- country_best_worst_by_q.csv: shape=(...)
- country_model_contributions.csv: shape=(...)
- country_residuals_and_gaps.csv: shape=(...)
- country_cluster_profile.csv: shape=(...)
- country_headline_flags.csv: shape=(...)
- country_learning_patterns.csv: shape=(...)
- country_graphics_catalog.csv: shape=(...)
- manifest: OK/FAIL

3. Países clave
- Chile presente: PASS/FAIL
- Singapur presente: PASS/FAIL
- Estonia presente: PASS/FAIL
- Irlanda presente: PASS/FAIL
- Emiratos presente: PASS/FAIL
- Brasil/Uruguay presentes: PASS/FAIL

4. Rankings y gráficos
- Rankings Q1-Q6: PASS/FAIL
- Rankings por grupo: PASS/FAIL
- Top/Bottom por Q: PASS/FAIL
- Heatmap país × Q: PASS/FAIL
- Country card Singapur: PASS/FAIL
- Country card Chile: PASS/FAIL
- Chile vs Singapur: PASS/FAIL

5. Semántica
- independent_prediction=false: PASS/FAIL
- causal_claim=false: PASS/FAIL
- score_scope=in_sample_descriptive_positioning: PASS/FAIL
- README con cautela metodológica: PASS/FAIL

6. Hallazgos preliminares
- Países pioneros consistentes: [...]
- Países rezagados consistentes: [...]
- Mejores benchmarks para Chile: [...]
- Principales brechas de Chile: [...]
- Advertencias de missingness: [...]

7. Recomendación
- ¿Puede pasar a Fase 7?: SÍ/NO
- Observaciones antes de Fase 7: [...]
```

---

## 22. Prompt listo para usar con otro LLM ejecutor

```text
Actúa como LLM ejecutor técnico del proyecto Research_AI_law. Debes implementar la actualización Fase 6.2 Country Intelligence Layer siguiendo estrictamente el archivo BLUEPRINT_ACTUALIZACION_FASE6_2_COUNTRY_INTELLIGENCE_RESEARCH_AI_LAW.md.

No borres ni modifiques los 11 outputs actuales de Fase 6. Agrega una subcarpeta FASE6/outputs/country_intelligence/ y genera perfiles país-por-país para Q1-Q6, rankings globales, rankings por grupo, mejores y peores por Q, drivers descriptivos, residuales, flags narrativos, patrones de aprendizaje y gráficos profesionales.

Debes incluir Chile y Singapur. Debes permitir responder cómo se comporta Singapur en cada Q, por qué aparece como pionero descriptivo y qué puede aprender Chile, sin afirmar causalidad. Debes producir gráficos para comparar todos los países por Q y rankings por submuestra.

Está prohibido crear train/test split, usar holdout, afirmar causalidad, llamar predicción independiente a los scores o borrar outputs previos. Al final ejecuta tests y entrega reporte con shapes de outputs, países clave, gráficos generados y recomendación para pasar a Fase 7.
```

---

**Fin del blueprint de actualización Fase 6.2.**
