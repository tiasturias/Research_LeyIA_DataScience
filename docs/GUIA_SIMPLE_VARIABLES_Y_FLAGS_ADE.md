# Guía simple de variables y flags del ADE

Esta guía explica en palabras simples qué información entrega cada bloque de variables del
Análisis Descriptivo Exploratorio (ADE) y qué significan las banderas de completitud usadas
para definir submuestras de países.

## 1. Idea general del estudio

La lógica del estudio puede resumirse así:

```math
X_1 + X_2 \longrightarrow Y
```

Donde:

- `X1` representa cómo regula IA un país.
- `X2` representa condiciones económicas, digitales, institucionales y legales del país.
- `Y` representa qué tan desarrollado está su ecosistema de inteligencia artificial.

La pregunta de fondo es:

```math
\text{¿Los países que regulan más o mejor la IA tienen ecosistemas IA más desarrollados,}
```

```math
\text{incluso considerando sus condiciones estructurales?}
```

---

## 2. Variables Y: resultados del ecosistema IA

Estas variables dicen qué tan desarrollado está el ecosistema de inteligencia artificial de
cada país.

| Variable | Qué información entrega |
|---|---|
| `ai_readiness_score` | Qué tan preparado está un país para adoptar, gobernar y aprovechar IA. Es una medida general de madurez institucional, tecnológica y estratégica. |
| `ai_adoption_rate` | Qué proporción o nivel de adopción de IA existe en empresas, organizaciones o economía del país. Indica uso práctico de IA. |
| `ai_investment_usd_bn_cumulative` | Cuánta inversión acumulada en IA ha recibido el país, medida en miles de millones de dólares. Sirve para ver capital disponible para IA. |
| `ai_startups_cumulative` | Cuántas startups de IA existen o se han acumulado en el país. Mide dinamismo emprendedor en IA. |
| `ai_patents_per100k` | Cuántas patentes relacionadas con IA existen por cada 100 mil habitantes. Mide producción tecnológica ajustada por tamaño poblacional. |

En resumen, las variables `Y` responden:

```math
\text{¿Qué tan fuerte es el ecosistema IA del país?}
```

---

## 3. Variables X1 IAPP: regulación IA según la fuente base

Estas variables describen cómo está regulando cada país la inteligencia artificial según la
codificación base IAPP.

| Variable | Qué información entrega |
|---|---|
| `has_ai_law` | Indica si el país tiene o no una ley específica de IA. Es una variable binaria: `1 = sí`, `0 = no`. |
| `regulatory_approach` | Describe el tipo de enfoque regulatorio: por ejemplo, si el país tiene una estrategia, una ley integral, un enfoque ligero o ningún marco claro. |
| `regulatory_intensity` | Mide qué tan fuerte o exigente es la regulación IA en una escala numérica, usualmente de 0 a 10. |
| `enforcement_level` | Indica qué tan aplicable o exigible es la regulación: bajo, medio, alto o inexistente. |
| `thematic_coverage` | Mide cuántos temas cubre la regulación: riesgos, transparencia, derechos, datos, seguridad, responsabilidad, supervisión, etc. |
| `regulatory_status_group` | Agrupa a los países en categorías más simples: regulación vinculante, estrategia solamente, marco blando o sin marco regulatorio. |

En resumen, las variables `X1 IAPP` responden:

```math
\text{¿Cómo regula IA este país según la fuente base?}
```

---

## 4. Variables X1 propuestas por corpus legal

Estas variables son una segunda lectura de la regulación, basada en documentos legales
revisados por la skill `corpus-legal-ia`.

| Variable | Qué información entrega |
|---|---|
| `has_ai_law_proposed` | Reevalúa si el país tiene una ley IA específica a partir del corpus documental. |
| `regulatory_intensity_proposed` | Propone una nueva intensidad regulatoria basada en los documentos revisados. |
| `thematic_coverage_proposed` | Propone una nueva medición de cuántos temas regulatorios cubre el país según el corpus legal. |
| `regulatory_regime_group_proposed` | Propone una reclasificación del país: regulación vinculante, estrategia, marco blando o sin marco. |
| `enforcement_level_proposed` | Propone una nueva lectura sobre qué tan exigible es el marco regulatorio. |

Estas variables sirven para contrastar la fuente IAPP con evidencia documental directa.

En resumen:

```math
\text{¿El corpus legal confirma, corrige o matiza la clasificación IAPP?}
```

---

## 5. Variables nuevas del corpus legal

Estas variables no vienen de IAPP, sino que fueron creadas a partir del análisis documental.

| Variable | Qué información entrega |
|---|---|
| `has_dedicated_ai_authority` | Indica si el país tiene una institución, agencia o autoridad dedicada específicamente a IA. |
| `ai_law_pathway_declared` | Indica si el país tiene un proyecto, borrador, agenda pública o camino declarado hacia una ley IA. |
| `ai_corpus_n_documents` | Número de documentos legales o regulatorios recopilados para ese país. |
| `ai_corpus_total_pages` | Total de páginas del corpus legal recopilado para ese país. |
| `ai_corpus_years_span` | Rango temporal cubierto por los documentos: diferencia entre el documento más antiguo y el más reciente. |

Estas variables ayudan a medir no solo qué regulación existe, sino también qué tan
documentado y avanzado está el proceso regulatorio.

En resumen:

```math
\text{¿Qué tan desarrollado y documentado está el ecosistema legal IA del país?}
```

---

## 6. Variables X2: controles principales

Estas variables no son el foco principal, pero ayudan a no confundir regulación con
desarrollo económico, digital o institucional.

| Variable | Qué información entrega |
|---|---|
| `gdp_per_capita_ppp` | PIB per cápita ajustado por poder de compra. Mide nivel de desarrollo económico del país. |
| `internet_penetration` | Porcentaje de la población con acceso a internet. Mide infraestructura digital básica. |
| `gii_score` | Puntaje del Global Innovation Index. Mide capacidad general de innovación. |
| `rd_expenditure` | Gasto en investigación y desarrollo como porcentaje del PIB. Mide inversión científica y tecnológica. |
| `tertiary_education` | Nivel de educación terciaria o superior. Aproxima capital humano avanzado. |

En resumen, las variables `X2` responden:

```math
\text{¿El país ya tenía condiciones económicas, digitales e innovadoras para desarrollar IA?}
```

---

## 7. Confounders institucionales y legales

Estos controles adicionales ayudan a distinguir si el efecto observado se debe realmente a
regulación IA o a otras características del país.

| Variable | Qué información entrega |
|---|---|
| `regulatory_quality` | Calidad general del Estado para diseñar e implementar regulación. |
| `rule_of_law` | Fortaleza del Estado de derecho. |
| `has_gdpr_like_law` | Indica si el país tiene una ley de protección de datos similar al GDPR europeo. |
| `gdpr_similarity_level` | Nivel de similitud con el modelo GDPR. |
| `fh_total_score` | Puntaje Freedom House; mide libertades políticas y civiles. |
| `legal_origin` | Tradición jurídica del país: common law, civil law francesa, germánica, etc. |
| `is_common_law` | Indica si el país pertenece a tradición common law. |

En simple, estas variables ayudan a responder:

```math
\text{¿La diferencia entre países se explica por regulación IA o por instituciones previas?}
```

---

## 8. Qué significan las flags de completitud

El dataset original contiene 86 países, pero no todos tienen datos completos para todas las
variables. Por eso se crean flags o banderas de completitud.

Una flag de completitud es una columna que marca si un país tiene suficiente información
para entrar en cierto tipo de análisis.

Normalmente funciona así:

| Valor | Significado |
|---|---|
| `1` | El país tiene los datos mínimos requeridos para ese análisis. |
| `0` | El país no tiene todos los datos necesarios para ese análisis. |

Por eso, cuando el EDA dice:

> La muestra principal, la muestra confounded, la muestra con régimen completo y la muestra
> con tradición legal completa contienen 72 países cada una. La completitud extendida cubre
> 62 países, mientras que la completitud digital cubre 69 países.

Lo que significa es:

> De los 86 países originales, algunos subconjuntos tienen datos suficientemente completos
> para ciertos análisis. La mayoría de los análisis centrales se pueden hacer con 72 países,
> pero algunos análisis más exigentes bajan a 62 o 69 países porque requieren variables
> adicionales que no están disponibles para todos.

---

## 9. Explicación simple de cada flag

### `complete_principal`

Indica que el país tiene los datos mínimos necesarios para el análisis principal.

Un país con `complete_principal = 1` tiene información suficiente en las variables centrales:

- resultados principales del ecosistema IA (`Y`);
- regulación IA base (`X1`);
- controles básicos necesarios para el análisis.

En el EDA:

```text
complete_principal: 72/86
```

Esto significa que 72 de los 86 países pueden usarse en el análisis principal.

En simple:

> `complete_principal` define la muestra base del estudio.

---

### `complete_confounded`

Indica que el país tiene datos suficientes para análisis que consideran posibles
confusores o variables que pueden distorsionar la relación entre regulación IA y ecosistema
IA.

Estos confounders incluyen variables como:

- calidad regulatoria;
- Estado de derecho;
- similitud con GDPR;
- Freedom House;
- tradición legal;
- common law.

En el EDA:

```text
complete_confounded: 72/86
```

Esto significa que 72 países tienen datos suficientes para analizar la relación entre
regulación y ecosistema IA controlando por factores institucionales y legales.

En simple:

> `complete_confounded` permite estudiar si la relación entre regulación IA y ecosistema IA
> sigue existiendo cuando se consideran otras características del país.

---

### `complete_extended`

Indica que el país tiene datos suficientes para un análisis más completo o más exigente,
incluyendo variables adicionales que no están disponibles para todos los países.

Estas variables pueden incluir información más específica o de menor cobertura, por ejemplo:

- gasto en I+D;
- educación terciaria;
- patentes;
- publicaciones;
- otros indicadores complementarios.

En el EDA:

```text
complete_extended: 62/86
```

Esto significa que solo 62 países tienen datos suficientemente completos para un análisis
más amplio y detallado.

En simple:

> `complete_extended` es una muestra más pequeña, pero con más variables disponibles por
> país.

---

### `complete_digital`

Indica que el país tiene datos suficientes sobre infraestructura o condiciones digitales.

Esta flag es importante porque un país puede tener buena regulación IA, pero si no tiene
infraestructura digital, internet o capacidades tecnológicas, su ecosistema IA puede no
desarrollarse igual.

Puede incluir variables como:

- penetración de internet;
- indicadores digitales;
- servicios TIC;
- exportaciones high-tech;
- otras variables relacionadas con capacidad digital.

En el EDA:

```text
complete_digital: 69/86
```

Esto significa que 69 países tienen datos suficientes para análisis relacionados con
condiciones digitales.

En simple:

> `complete_digital` sirve para analizar si el desarrollo IA depende también de la base
> digital del país.

---

### `complete_regime`

Indica que el país tiene información suficiente para clasificar su régimen regulatorio IA.

Un país con `complete_regime = 1` tiene datos suficientes para saber si está en una
categoría como:

- `binding_regulation`;
- `strategy_only`;
- `soft_framework`;
- `no_framework`.

En el EDA:

```text
complete_regime: 72/86
```

Esto significa que 72 países tienen datos suficientes para análisis por grupo regulatorio.

En simple:

> `complete_regime` permite comparar países según el tipo de regulación IA que tienen.

---

### `complete_legal_tradition`

Indica que el país tiene información suficiente sobre su tradición jurídica.

Esto permite incorporar variables como:

- `legal_origin`;
- `is_common_law`.

La tradición legal importa porque países de common law, civil law francesa, civil law
germánica u otras familias jurídicas pueden regular de manera distinta.

En el EDA:

```text
complete_legal_tradition: 72/86
```

Esto significa que 72 países tienen datos suficientes para analizar el rol de la tradición
jurídica.

En simple:

> `complete_legal_tradition` permite estudiar si la forma de regular IA se relaciona con la
> familia jurídica del país.

---

## 10. Resumen rápido de las flags

| Flag | Países | Para qué sirve |
|---|---:|---|
| `complete_principal` | 72/86 | Define la muestra central del análisis. |
| `complete_confounded` | 72/86 | Permite controlar por instituciones, derecho y factores que pueden confundir la relación. |
| `complete_extended` | 62/86 | Permite análisis más completos, pero con menos países por falta de datos adicionales. |
| `complete_digital` | 69/86 | Permite analizar infraestructura y capacidades digitales. |
| `complete_regime` | 72/86 | Permite comparar países por tipo de régimen regulatorio IA. |
| `complete_legal_tradition` | 72/86 | Permite analizar diferencias según tradición jurídica. |

---

## 11. Cómo interpretar las muestras

No todos los análisis usan exactamente los mismos países.

La lógica es:

- Si se quiere un análisis central y amplio, se usa `complete_principal`.
- Si se quiere controlar por factores institucionales o legales, se usa `complete_confounded`.
- Si se quiere incluir más variables, se usa `complete_extended`, pero se pierden países.
- Si se quiere estudiar infraestructura digital, se usa `complete_digital`.
- Si se quiere comparar tipos de regulación IA, se usa `complete_regime`.
- Si se quiere incluir tradición jurídica, se usa `complete_legal_tradition`.

En simple:

> Las flags no son variables sustantivas del fenómeno. Son filtros de calidad de datos.
> Sirven para decidir qué países se pueden usar en cada análisis sin mezclar países con
> datos completos y países con datos incompletos.

