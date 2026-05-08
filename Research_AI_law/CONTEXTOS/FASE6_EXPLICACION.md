# FASE6: Modeling — Guía Didáctica y Técnica Completa

## 1. Propósito de este Documento

Este archivo es el manual de navegación para la **FASE6 (Modeling)** del proyecto `Research_AI_law`. Su objetivo es explicar, paso a paso y sin ambigüedades, qué hace esta fase, por qué existen 4 sub-preguntas (Q1, Q2, Q3, Q4), cómo cada una contribuye a responder la hipótesis principal, qué modelos se entrenan y por qué se eligieron, y cómo se consume el bundle de datos entregado por FASE5.

**No se usan analogías externas.** Todo se explica en el lenguaje exacto del proyecto.

---

## 2. ¿Qué es la FASE6? Contexto en el Pipeline CRISP-DM

El proyecto sigue la metodología **CRISP-DM** (Cross Industry Standard Process for Data Mining), que tiene 6 fases:

1. **Entendimiento del Negocio:** ¿Qué pregunta de política pública queremos responder?
2. **Entendimiento de los Datos:** ¿Qué datos tenemos? ¿De dónde vienen?
3. **Preparación de los Datos:** Limpieza, transformaciones, feature engineering.
4. **Modelado:** Aplicar algoritmos matemáticos a los datos preparados.
5. **Evaluación:** ¿Son confiables los resultados?
6. **Despliegue:** Entregar el informe al tomador de decisiones.

**FASE6 es el Paso 4: Modelado.**

En esta fase, tomamos la **tabla de datos maestra** que FASE5 construyó (`phase6_feature_matrix.csv`, 43 países × 126 columnas) y aplicamos algoritmos estadísticos y de machine learning para:
- Medir asociaciones entre regulación (X1) y ecosistema (Y).
- Controlar por factores socioeconómicos (X2).
- Descubrir patrones naturales en los perfiles regulatorios.

---

## 3. El Inventario de Entradas: El Bundle `phase6_ready`

FASE5 entregó una caja de herramientas llamada `phase6_ready` con **12 archivos**. FASE6 los consume **todos**, no solo el CSV principal.

| # | Archivo | Qué contiene | Por qué lo usa FASE6 |
|---|---|---|---|
| 1 | `phase6_feature_matrix.csv` | La tabla maestra: 43 países, 126 columnas. | Es el dataset que los modelos "ven". |
| 2 | `phase6_modeling_contract.yaml` | El contrato semántico: qué variable es X1, qué es Y_Q1, qué es X2, etc. | Evita que hardcodeemos nombres de columnas. Garantiza que usemos las variables correctas para cada sub-pregunta. |
| 3 | `phase6_column_groups.yaml` | Grupos de columnas: `one_hot_cols`, `robust_zscore_cols`, `regulatory_aggregate_cols`, etc. | Permite seleccionar features por tipo (ej. "dame todas las one-hots"). |
| 4 | `phase6_schema.json` / `.csv` | Schema de cada columna: tipo de dato, % de nulos, rol MVP. | Validación de tipos y justificación de N efectivo. |
| 5 | `phase6_train_test_split.csv` | Qué países son train y cuáles test. | Separación de datos para evaluar generalización. |
| 6 | `phase6_missingness_by_column.csv` | Nulos por columna. | Justificar por qué Q2 tiene N=25 y no N=43. |
| 7 | `phase6_missingness_by_country.csv` | Nulos por país. | Identificar países problemáticos antes de modelar. |
| 8 | `phase6_transform_params.csv` | Parámetros de transformación: mediana, MAD, estado. | Detectar z-scores inválidos (ej. MAD=0 en IAPP binarios). |
| 9 | `phase6_variables_catalog.csv` | Catálogo: fuente, definición, limitaciones conocidas. | Anotar el origen de cada variable en los resultados. |
| 10 | `phase6_ready_manifest.json` | Hashes SHA-256 de todos los archivos del bundle. | **Validar integridad:** si FASE5 fue modificada, FASE6 se detiene. |
| 11 | `phase6_llm_context.json` | Reglas duras de transición: no recompute, no impute, preserve missingness. | Gobernanza programática. |
| 12 | `FASE5/src/api` (implícito) | API preferida para consumir el bundle. | Interfaz de carga estándar. |

**Regla de oro:** FASE6 **lee** estos archivos. **Nunca los modifica.**

---

## 4. La Hipótesis Principal del Proyecto

> **Hipótesis Principal:** ¿Existe una asociación estadísticamente significativa entre las características de la regulación de inteligencia artificial de un país y el desarrollo de su ecosistema de IA, después de controlar por factores socioeconómicos e institucionales?

### Descomposición de la hipótesis

| Componente | Notación | Significado en el proyecto |
|---|---|---|
| **Tratamiento / Regulación** | X1 | ¿Qué tan regulado está el país? Leyes de IA, estrategias, autoridades, mecanismos binding. |
| **Controles** | X2 | Factores que también afectan el ecosistema y podrían confundir la relación: PIB, educación, calidad del gobierno, inversión en I+D, infraestructura digital. |
| **Resultado / Ecosistema** | Y | El "desarrollo del ecosistema de IA". |

**El problema:** La palabra "desarrollo" es abstracta. No es una variable que podamos medir directamente con un solo número.

---

## 5. El Error Común: Pensar que hay una sola Y

Muchos proyectos de ciencia de datos caen en el error de pensar:

> *"Y = desarrollo del ecosistema = una sola columna en Excel"*

**Eso es falso.** En este proyecto, **Y es un vector de 3 dimensiones** (más una cuarta descriptiva):

```
Y = [ Y_inversión , Y_adopción , Y_innovación ]
```

Cada dimensión mide algo distinto:
- **Y_inversión:** ¿Hay dinero? (unicornios, capital de riesgo, deals).
- **Y_adopción:** ¿Se está usando? (difusión Microsoft, uso Anthropic, adopción sector público).
- **Y_innovación:** ¿Se crea conocimiento? (patentes, papers, índices WIPO/Oxford).

**¿Por qué no sumamos todo en un índice?**
- Porque inversión se mide en **USD**, adopción en **porcentajes**, innovación en **scores**.
- Porque cada dimensión tiene **datos faltantes en países distintos**.
- Porque un país puede ser alto en innovación pero bajo inversión (ej. Japón).

**La hipótesis principal, por lo tanto, NO se responde con un solo modelo.** Se responde ejecutando modelos separados para cada dimensión de Y y luego **sintetizando** los resultados.

---

## 6. Las 4 Sub-Preguntas: 4 Dimensiones del Ecosistema

FASE6 descompone la hipótesis principal en 4 sub-preguntas operativas. Cada una tiene sus propias variables Y, sus propios datos disponibles y su propio modelo.

---

### **Q1 — Inversión: ¿La regulación afecta la inversión privada en IA?**

**¿Qué pregunta?**
¿Un país con más leyes de IA atrae más o menos inversión (unicornios, capital de riesgo)?

**Variables Y (Resultado):**
- `oxford_ind_company_investment_emerging_tech`
- `oxford_ind_ai_unicorns_log`
- `oxford_ind_non_ai_unicorns_log`
- `oxford_ind_vc_availability`
- `wipo_c_vencapdeal_score`

**Variables X1 (Tratamiento):**
- `n_binding` (número de mecanismos regulatorios "duros") — **0% missing, 43 países.**
- `regulatory_intensity` (proporción binding/total) — **0% missing.**
- `iapp_ley_ia_vigente` (¿tiene ley de IA?) — **58% missing, solo 18 países.**

**Variables X2 (Controles):**
- `wb_gdp_per_capita_ppp_log_z` (PIB per cápita)
- `wb_internet_penetration_z` (penetración internet)
- `wb_tertiary_education_enrollment_z` (educación terciaria)
- `wb_rd_expenditure_pct_gdp_z` (gasto I+D)
- `wb_government_effectiveness_z`, `wb_rule_of_law_z`, `wb_regulatory_quality_z` (instituciones)

**N efectivo:** **34 países** (tras eliminar filas con NaN en Y + X1 + X2).

**Modelos entrenados:**
1. **OLS (Mínimos Cuadrados Ordinarios):** El modelo lineal clásico. Es altamente interpretable: cada coeficiente dice "por cada unidad más de regulación, la inversión sube/baja X puntos, manteniendo todo lo demás constante". Ideal para explicarle al Congreso.
2. **Ridge Regression:** OLS con un "freno" (penalización L2). Evita que variables colineales (ej. PIB e internet) distorsionen los coeficientes. Útil cuando X2 tiene muchas dimensiones.
3. **Lasso Regression:** Similar a Ridge pero con penalización L1. Tiende a anular coeficientes irrelevantes, haciendo selección automática de variables.
4. **PSM (Propensity Score Matching):** Intenta simular un experimento. Empareja países "gemelos" económicos donde uno tiene ley de IA y el otro no, para aislar el efecto de la ley. **Limitación:** solo ~9-10 países tienen ley en la submuestra completa, por lo que los pares emparejados pueden ser pocos.

**¿Por qué estos modelos?**
- N=34 es suficiente para regresión lineal.
- La interpretabilidad es prioridad (stakeholders políticos).
- Ridge/Lasso estabilizan coeficientes ante la colinealidad de controles socioeconómicos.

---

### **Q2 — Adopción: ¿Qué tipo de regulación se asocia con mayor adopción de IA?**

**¿Qué pregunta?**
¿Los países con cierto tipo de regulación tienen mayor difusión de IA en empresas y gobierno?

**Variables Y (Resultado):**
- `ms_h2_2025_ai_diffusion_pct` (difusión Microsoft)
- `anthropic_usage_pct` (uso Anthropic)
- `oxford_public_sector_adoption` (adopción sector público)
- `oxford_ind_adoption_emerging_tech` (adopción empresarial)
- `oecd_5_ict_business_oecd_biz_ai_pct` (adopción OECD, **28% missing**)

**Variables X1 y X2:** Similares a Q1.

**N efectivo:** **25 países** (el cuello de botella es `oecd_biz_ai_pct` con 12 faltantes).

**Modelos entrenados:**
1. **Regresión Logística:** Separa países en "alta adopción" vs "baja adopción" (usando la mediana como corte). Predice probabilidades. Muy interpretable: un coeficiente positivo significa "más regulación se asocia con mayor odds de alta adopción".
2. **Random Forest (Clasificación):** Un conjunto de árboles de decisión. Mide "importancia de variables" (¿qué factores son más predictivos?). Usamos `max_depth=4` para evitar sobreajuste con N pequeño.

**¿Por qué estos modelos?**
- Y es categórica (alta/baja), no numérica. Regresión lineal no serviría.
- Logística da odds ratios (fáciles de explicar a no-técnicos).
- Random Forest captura relaciones no lineales (ej. quizás regulación media es buena, pero alta es mala).

---

### **Q3 — Innovación: ¿Hay relación entre regulación e indicadores de innovación?**

**¿Qué pregunta?**
¿Los países con marcos regulatorios más desarrollados producen más patentes, papers y scores de innovación?

**Variables Y (Resultado):**
- `wipo_out_score` (outputs WIPO)
- `oxford_total_score` (score total Oxford)
- `wipo_gii_score` (Global Innovation Index)
- `oxford_innovation_capacity` (capacidad innovación)
- `oxford_ind_ai_research_papers_log` (papers IA)
- `stanford_fig_6_3_5_fig_6_3_5_volume_of_publications` (**39.5% missing**)
- `wb_patent_applications_residents` (patentes)

**N efectivo:** **21 países** (con Stanford) o **~40** (sin Stanford).

**Modelos entrenados:**
1. **Ridge Regression:** Estabiliza coeficientes cuando hay pocos países (N=21) y muchos controles. Evita que un solo país outlier (USA o China en patentes) domine todo.
2. **Gradient Boosting Regressor (GBR):** Modela relaciones no lineales. Usamos pocos árboles (`n_estimators=200`, `max_depth=3`) para no sobreajustar.

**¿Por qué estos modelos?**
- N=21 es críticamente bajo. Ridge es más estable que OLS aquí.
- GBR sirve como benchmark no lineal: si Ridge y GBR coinciden en signo, el hallazgo es más robusto.

---

### **Q4 — Tipos Regulatorios: ¿Qué perfiles regulatorios existen?**

**¿Qué pregunta?**
No buscamos causalidad aquí. Buscamos **describir**: ¿existen grupos naturales de países según su perfil regulatorio?

**Variables:**
- 5 one-hots de `iapp_categoria_obligatoriedad` (tipo de obligatoriedad)
- 4 one-hots de `iapp_modelo_gobernanza` (modelo institucional)
- 5 agregados: `n_binding`, `n_non_binding`, `n_hybrid`, `regulatory_intensity`, `n_regulatory_mechanisms`

**Total: 14 features. 0% missing. 43 países.**

**Modelos entrenados:**
1. **K-Means Clustering:** Agrupa países en k grupos (probamos k=3 y k=4) minimizando la distancia interna. Algoritmo clásico, rápido, fácil de explicar.
2. **Hierarchical Clustering (HCA):** Construye un "árbol genealógico" de similitud entre países. Usamos distancia **Jaccard** para variables binarias y **Euclidean** para agregados. Método `ward`.
3. **Silhouette Score:** Métrica que dice qué tan "bien separados" están los clusters (rango -1 a 1). Nos ayuda a decidir si k=3 o k=4 es mejor.

**¿Por qué estos modelos?**
- Q4 es **no supervisado**: no hay Y. Solo hay X (perfil regulatorio).
- K-Means es el estándar para clustering de perfiles.
- HCA produce dendrogramas visualmente poderosos para el notebook.
- El silhouette score da una justificación objetiva del número de clusters.

**¿Cómo ayuda Q4 a la hipótesis principal?**
Q4 responde: *"¿En qué grupo de países está Chile?"* Si Chile está en un cluster con países de baja inversión, eso es información valiosa para el policymaker, aunque no sea causal.

---

## 7. ¿Por Qué No Hacemos Un Solo Modelo Gigante?

Podría parecer más elegante tener un único modelo:

```
Y_mega = β₁ × Regulación + β₂ × PIB + β₃ × Educación + ...
```

**Esto es inviable por 5 razones concretas:**

### Razón 1: Y no es una sola cosa
"Desarrollo del ecosistema" no es medible con una sola variable. Es un concepto multidimensional que requiere 3 familias de indicadores (inversión, adopción, innovación).

### Razón 2: Diferentes tipos de Y requieren diferentes familias de modelos
- Inversión e innovación son **continuas** (scores, counts) → Regresión.
- Adopción se clasifica mejor como **alta/baja** → Clasificación.
- Tipos regulatorios no tienen Y → Clustering descriptivo.

### Razón 3: Diferentes patrones de datos faltantes (missingness)
- Q1: N=34 (solo 3 variables con pocos missings).
- Q2: N=25 (OECD business AI tiene 12 missings).
- Q3: N=21 (Stanford publications tiene 17 missings).
- Q4: N=43 (agregados completos).

Si hiciéramos un solo modelo, tendríamos que usar **el mínimo común denominador: N=21**. Perderíamos 22 países de información valiosa en Q1.

### Razón 4: Diferentes escalas y unidades
- Inversión Oxford: score 0-100.
- Adopción Microsoft: porcentaje %.
- Innovación WIPO: score 0-100.
- Patentes: conteo bruto (0 a 1,400,000).

No tienen sentido sumarse en una sola ecuación sin transformaciones que las hagan comparables.

### Razón 5: Diferentes objetivos de inferencia
- Q1-Q3 buscan **asociación/causalidad** (¿X1 afecta Y?).
- Q4 busca **tipología** (¿qué tipos de X1 existen?).

Son preguntas epistemológicamente distintas.

---

## 8. Modelos a Entrenar y Justificación Técnica

Aquí profundizamos en **por qué** cada modelo fue seleccionado según el plan MVP y las restricciones del proyecto.

### 8.1 OLS (Ordinary Least Squares)

**Qué hace:** Encuentra la línea recta que mejor se ajusta a los datos minimizando el error cuadrático medio.

**Fórmula:**
```
Y = β₀ + β₁ × X1 + β₂ × X2 + ... + ε
```

**Por qué se usa:**
- Máxima interpretabilidad. β₁ dice exactamente cuánto cambia Y por cada unidad de X1.
- Es el estándar de oro en econometría y ciencia política.
- Los stakeholders (Congreso, ministerios) pueden entenderlo sin ser data scientists.

**Limitación:** Sensible a outliers (USA, CHN) y a colinealidad entre X2.

### 8.2 Ridge Regression (L2)

**Qué hace:** Igual que OLS pero penaliza coeficientes grandes.

**Fórmula:**
```
min( Σ(error²) + λ × Σ(β²) )
```

**Por qué se usa:**
- Cuando los controles X2 están correlacionados (ej. PIB e internet), Ridge estabiliza las estimaciones.
- Reduce varianza a costa de un poco de sesgo. Con N=34 o N=21, la varianza es el enemigo.

### 8.3 Lasso Regression (L1)

**Qué hace:** Similar a Ridge pero puede llevar coeficientes exactamente a cero.

**Fórmula:**
```
min( Σ(error²) + λ × Σ|β| )
```

**Por qué se usa:**
- Selección automática de variables. Si `wb_mobile_subscriptions` no predice nada, Lasso le pone coeficiente 0.
- Útil para entender qué controles realmente importan.

### 8.4 Regresión Logística

**Qué hace:** Predice la probabilidad de pertenecer a una clase (alta adopción = 1, baja adopción = 0).

**Fórmula:**
```
P(Y=1) = 1 / (1 + e^-(β₀ + β₁X1 + β₂X2))
```

**Por qué se usa:**
- Y en Q2 es binaria (alta/baja adopción). Regresión lineal daría probabilidades >100% o <0%.
- Los coeficientes se interpretan como **log-odds**: "un punto más de regulación aumenta los odds de alta adopción en un factor de e^β".

### 8.5 Random Forest (Clasificación)

**Qué hace:** Conjunto de árboles de decisión que votan por la clase.

**Por qué se usa:**
- Captura relaciones no lineales (ej. regulación media = buena, alta = mala).
- Entrega **feature importance**: ranking de qué variables son más predictivas.
- Con `max_depth=4`, evitamos sobreajuste ante N=25.

### 8.6 Gradient Boosting Regressor (GBR)

**Qué hace:** Construye árboles secuenciales donde cada nuevo árbol corrige los errores del anterior.

**Por qué se usa:**
- Benchmark no lineal para Q3. Si Ridge y GBR coinciden en dirección (signo) del efecto de la regulación, el hallazgo es robusto.
- Con `max_depth=3` y pocos árboles, limitamos la complejidad.

### 8.7 K-Means Clustering

**Qué hace:** Divide N puntos en k grupos minimizando la varianza intra-grupo.

**Por qué se usa:**
- Algoritmo estándar para descubrir perfiles naturales.
- Rápido, determinístico (con `random_state`), fácil de visualizar.

### 8.8 Hierarchical Clustering (HCA)

**Qué hace:** Construye una jerarquía de clusters (dendrograma).

**Por qué se usa:**
- No requiere predefinir k. El dendrograma muestra qué países son más similares.
- Permite usar distancias mixtas (Jaccard para binarias, Euclidean para numéricas).

### 8.9 PSM (Propensity Score Matching)

**Qué hace:** Intenta simular un experimento aleatorio en datos observacionales.

**Pasos:**
1. Entrenar un modelo logístico: ¿qué probabilidad tiene un país de tener ley de IA, dado sus controles X2? (Propensity Score).
2. Emparejar cada país "tratado" (con ley) con un país "control" (sin ley) que tenga un Propensity Score similar.
3. Comparar el resultado Y entre los gemelos emparejados.

**Por qué se usa:**
- Es la única técnica en FASE6 que busca **inferencia causal** explícita.
- Responde: "¿Qué le habría pasado a Chile si NO hubiera ley de IA?" (el contrafactual).

**Limitación:** Con ~9 países tratados, los matches pueden ser escasos. Si hay <5 pares, el resultado es "indicativo", no conclusivo.

---

## 9. Cómo se Responde la Hipótesis Principal (La Magia de la Síntesis)

FASE6 **no responde sola** la hipótesis principal. Responde **4 preguntas parciales**. La síntesis ocurre en FASE8.

### Flujo de evidencia:

```
FASE6 (Modeling)          FASE7 (Evaluación)           FASE8 (Reporting)
      │                           │                            │
      ▼                           ▼                            ▼
Q1: "No hay efecto           ¿Son estables los            HIPÓTESIS PRINCIPAL:
    significativo en          coeficientes si              "La evidencia es mixta:
    inversión"                 sacamos a USA?"              No se encontró efecto
    (p=0.34)                                               significativo en inversión
                                                          ni innovación. En adopción
Q2: "Mayor regulación        ¿Mejora vs baseline?           se observa una asociación
    binding se asocia         (¿mejor que adivinar?)       positiva pero débil."
    con mayor adopción"
    (p=0.03)                   ¿Qué pasa sin Chile?

Q3: "No hay efecto           Sensibilidad temporal
    en innovación"            (¿panel vs snapshot?)
    (p=0.71)

Q4: "Existen 3 clusters:     Validación de clusters
    Duro, Suave, Mixto"       (¿silhouette > 0.5?)
    Chile está en Suave.
```

### Ejemplo de síntesis con datos ficticios (para ilustrar):

> **FASE8 diría:**
> "El modelo Q1 (N=34) encontró que `n_binding` tiene un coeficiente de -0.12 (IC95: -0.45 a 0.21, p=0.48). Es decir, no hay evidencia de que más regulación dura reduzca la inversión, pero tampoco la aumenta.
>
> El modelo Q2 (N=25) encontró que `regulatory_intensity` se asocia con mayor odds de alta adopción (OR=1.4, p=0.02). Sin embargo, al excluir a USA (sensitivity analysis de FASE7), el efecto desaparece.
>
> El modelo Q3 (N=21) no encontró asociación entre regulación e innovación (R²=0.08).
>
> Q4 ubica a Chile en el cluster 'Regulación Suave + Alta Adopción Pública', junto a Nueva Zelanda y Australia.
>
> **Conclusión para el policymaker:** La evidencia empírica no respalda que una regulación más restrictiva cause un ecosistema de IA más desarrollado. Chile, en su situación actual, no parece estar en desventaja por tener un marco regulatorio 'suave'."

**Nota clave:** Esta síntesis es FASE8. FASE6 solo entrega los números de los modelos.

---

## 10. La Fórmula Matemática de la Hipótesis Principal

Aunque la respondemos por partes, la estructura matemática subyacente es:

### Para Q1 y Q3 (Regresión):
```
Y_i = β₀ + β₁ × X1_i + Σ(γ_j × X2_ji) + ε_i

Donde:
- Y_i = resultado del país i (inversión o innovación)
- X1_i = tratamiento regulatorio del país i (n_binding, regulatory_intensity)
- X2_ji = control j del país i (PIB, educación, gobierno...)
- β₁ = coeficiente de interés: "efecto de la regulación"
- ε_i = error aleatorio
```

**Interpretación de β₁:**
- Si β₁ > 0 y p < 0.05: Más regulación se asocia con más Y (inversión/innovación).
- Si β₁ < 0 y p < 0.05: Más regulación se asocia con menos Y.
- Si p > 0.05: No hay evidencia estadística de asociación.

### Para Q2 (Clasificación):
```
log( P(Y_i=1) / (1 - P(Y_i=1)) ) = β₀ + β₁ × X1_i + Σ(γ_j × X2_ji)

Donde:
- Y_i = 1 si país i tiene "alta adopción", 0 si "baja adopción"
- P(Y_i=1) = probabilidad de alta adopción
- El lado izquierdo se llama "log-odds"
```

### Para Q4 (Clustering):
No hay fórmula de regresión. Se minimiza:
```
Σ(distancia(punto, centroide_del_cluster))²
```

---

## 11. Ejemplo Concreto con los Datos Reales del Proyecto

### Escenario: Ejecutar Q1 con `oxford_ind_company_investment_emerging_tech` como Y

**Paso 1:** `load_phase6.py` carga `phase6_feature_matrix.csv`.

**Paso 2:** Lee `phase6_modeling_contract.yaml` y ve que para Q1:
- Y = `oxford_ind_company_investment_emerging_tech`
- X1 = `n_binding`, `regulatory_intensity`
- X2 = `wb_gdp_per_capita_ppp_log_z`, `wb_government_effectiveness_z`, etc.

**Paso 3:** Filtra a los 34 países del train set (usando `phase6_train_test_split.csv`).

**Paso 4:** Aplica `dropna()`. Resultado: 34 filas completas.

**Paso 5:** Corre OLS:
```
inversión = 45.2 + (-2.1) × n_binding + 3.4 × PIB_log + 1.8 × gobierno + ε
```

**Paso 6:** Interpretación:
- Coeficiente de `n_binding` = -2.1. Significa: "por cada mecanismo binding adicional, la inversión baja 2.1 puntos, manteniendo PIB y gobierno constantes".
- P-value = 0.34. No es significativo (mayor a 0.05).
- R² = 0.28. El modelo explica el 28% de la variación en inversión.

**Paso 7:** PSM:
- 9 países tienen `iapp_ley_ia_vigente = 1`.
- Se emparejan con 8 controles similares (caliper 0.1).
- Comparación de inversión media: Tratados = 62.5, Controles = 58.3.
- Diferencia = 4.2 puntos (no significativa estadísticamente).

**Paso 8:** Exportar a `q1_results.csv`.

---

## 12. El Rol de `load_phase6.py`: El Guardián del Bundle

`load_phase6.py` es el primer archivo que se ejecuta en FASE6. Sus funciones son:

### 12.1 Validar Integridad
Lee `phase6_ready_manifest.json`, calcula el hash SHA-256 de cada archivo del bundle, y compara. Si difieren, lanza un error y detiene todo.

**¿Por qué?** Si FASE5 fue alterada, los resultados de FASE6 serán inválidos. Este es un control de calidad automático.

### 12.2 Cargar el Contrato Semántico
Lee `phase6_modeling_contract.yaml`. Este archivo dice:
- "Para Q1, las variables Y son estas 5."
- "Para Q2, las variables Y son estas 9."
- "Las variables X1 son estas 6."
- "Las variables X2 son estas 12."

Esto evita que el programador hardcodee nombres de columnas y se equivoque.

### 12.3 Construir las Matrices de Diseño
Para cada sub-pregunta, extrae del `phase6_feature_matrix.csv`:
- Solo las columnas relevantes (Y, X1, X2).
- Solo los países del train set.
- Elimina filas con NaN (`dropna()`).
- Retorna (X, y) listo para `sklearn` o `statsmodels`.

### 12.4 Proveer Metadatos para el Notebook
Carga `phase6_missingness_by_column.csv`, `phase6_transform_params.csv`, etc., para que el notebook `06_modeling.ipynb` pueda mostrar tablas explicativas al auditor.

---

## 13. Flujo de Trabajo de FASE6 (Paso a Paso)

```
INICIO FASE6
│
├─► 1. Validar bundle (manifest.json + hashes)
│   └─► Si falla → DETENER
│
├─► 2. Cargar datos (feature_matrix + contract + groups)
│
├─► 3. Ejecutar Q4 (Clustering)
│   ├─► K-Means (k=3, k=4)
│   ├─► Hierarchical Clustering
│   ├─► Silhouette Score
│   └─► Exportar: q4_clusters.csv, q4_distance_matrix.csv
│
├─► 4. Ejecutar Q1 (Inversión)
│   ├─► OLS por cada Y (5 modelos)
│   ├─► Ridge/Lasso por cada Y
│   ├─► PSM (si hay ≥5 pares)
│   └─► Exportar: q1_results.csv, q1_psm_matched_pairs.csv
│
├─► 5. Ejecutar Q2 (Adopción)
│   ├─► Binarizar Y por mediana
│   ├─► Logistic Regression
│   ├─► Random Forest
│   └─► Exportar: q2_results.csv
│
├─► 6. Ejecutar Q3 (Innovación)
│   ├─► Ridge por cada Y
│   ├─► Gradient Boosting por cada Y
│   ├─► Robustness: con/sin Stanford
│   └─► Exportar: q3_results.csv
│
├─► 7. Validar outputs con tests
│   └─► pytest FASE6/tests/
│
├─► 8. Generar notebook 06_modeling.ipynb
│   └─► Visualizaciones: dendrogramas, ROC, forest plots
│
└─► 9. Generar fase6_manifest.json
    └─► FIN FASE6
```

---

## 14. Reglas Duras de FASE6

Estas reglas provienen de `phase6_llm_context.json` y son inviolables:

1. **No recomputar FASE5:** FASE6 consume `phase6_ready`. No regenera transforms, no recalcula z-scores.
2. **No imputar:** Si un país no tiene dato en una variable, se elimina (`dropna`). No se inventan valores.
3. **No mutar FASE3 ni FASE4:** Solo lectura vía APIs.
4. **Preservar missingness:** El N efectivo por sub-pregunta debe documentarse explícitamente.
5. **Excel auditable NO es input:** El `MVP_AUDITABLE.xlsx` de FASE5 es para humanos, no para modelos.

---

## 15. Criterios de Aceptación para dar por Terminada FASE6

- [ ] `pytest FASE6/tests/` pasa al 100%.
- [ ] Los hashes SHA-256 del bundle FASE5 no cambiaron tras ejecutar FASE6.
- [ ] Q1-Q4 generan CSVs no vacíos en `FASE6/outputs/`.
- [ ] `q4_clusters.csv` tiene exactamente 43 filas.
- [ ] PSM tiene ≥5 pares o está documentado como "insufficient_n".
- [ ] `06_modeling.ipynb` ejecuta todas las celdas sin error.
- [ ] Chile (CHL) aparece en todos los outputs relevantes.
- [ ] `fase6_manifest.json` documenta git commit + hashes de inputs y outputs.

---

## 16. Resumen Visual del Sistema

```
┌─────────────────────────────────────────────────────────────────┐
│                        HIPÓTESIS PRINCIPAL                      │
│  ¿Regulación de IA ↔ Desarrollo del ecosistema de IA?          │
│  (controlando por PIB, educación, gobierno, etc.)              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
   ┌──────────┐         ┌──────────┐         ┌──────────┐
   │   Q1     │         │   Q2     │         │   Q3     │
   │Inversión │         │Adopción  │         │Innovación│
   │(N=34)    │         │(N=25)    │         │(N=21)    │
   │Regresión │         │Clasific. │         │Regresión │
   │OLS/Ridge │         │Logit/RF  │         │Ridge/GBR │
   └────┬─────┘         └────┬─────┘         └────┬─────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌────────┴────────┐
                    │       Q4        │
                    │Tipos Regulatorios│
                    │   (N=43)        │
                    │  Clustering     │
                    │ K-Means / HCA   │
                    └────────┬────────┘
                             │
                             ▼
               ┌─────────────────────────────┐
               │      FASE7 (Evaluación)     │
               │  • ¿Overfitting?            │
               │  • ¿Sensitivity? (sin USA)  │
               │  • ¿Baseline comparisons?   │
               └─────────────┬───────────────┘
                             │
                             ▼
               ┌─────────────────────────────┐
               │      FASE8 (Reporting)      │
               │  Síntesis de Q1+Q2+Q3+Q4    │
               │  Respuesta a la Hipótesis   │
               │  Principal en lenguaje      │
               │  político                   │
               └─────────────────────────────┘
```

---

## 17. Glosario Rápido

| Término | Significado |
|---|---|
| **X1** | Variables de tratamiento regulatorio (la "medicina"). |
| **X2** | Variables de control socioeconómico/institucional. |
| **Y** | Variable resultado (outcome) del ecosistema. |
| **N** | Número de países con datos completos para un modelo. |
| **OLS** | Regresión lineal ordinaria (mínimos cuadrados). |
| **Ridge** | Regresión con penalización L2 (reduce varianza). |
| **Lasso** | Regresión con penalización L1 (selecciona variables). |
| **PSM** | Propensity Score Matching (emparejamiento causal). |
| **Logit** | Regresión logística (predice probabilidades). |
| **RF** | Random Forest (ensamble de árboles). |
| **GBR** | Gradient Boosting Regressor (árboles secuenciales). |
| **K-Means** | Algoritmo de clustering por centroides. |
| **HCA** | Hierarchical Clustering (clustering jerárquico). |
| **One-hot** | Codificación binaria de variables categóricas. |
| **Z-score** | Estandarización (valor - mediana) / MAD. |
| **MAD** | Median Absolute Deviation (desviación robusta). |
| **dropna()** | Eliminar filas con valores faltantes. |

---

**Fin del documento.**
