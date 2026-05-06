# Transicion Fase 3 a Fase 4 - Plan para EDA Principal profesional

Proyecto: Research_AI_law  
Fase origen: 3 - Matriz Madre  
Fase destino: 4 - EDA Principal  
Directorio Fase 3: `/home/pablo/Research_LeyIA_DataScience/Research_AI_law/FASE3`  
Version Fase 3 al cierre: `1.1` (base `1.0` + quality fix `country_name_canonical`, 2026-05-06)  
Proposito de este documento: explicar como usar los resultados de Fase 3 para construir un EDA principal profesional, robusto y metodologicamente defendible.

> **Nota sobre version 1.1:** la version 1.1 corrige un bug donde 86 de 199 paises de la wide tenian `country_name_canonical` igual al ISO3 (ej: `ARG` en vez de `Argentina`). Las correcciones son backwards-compatible — Fase 4 puede consumir wide/panel/snapshot via `src.fase3.api` con `version=None` (default) sin cambios. Detalles completos en `FASE3_CIERRE_DOCUMENTACION_TECNICA.md` seccion 12.1.

---

## 1. Objetivo de Fase 4

La Fase 4 debe explorar la Matriz Madre para entender patrones, calidad, relaciones preliminares y capacidad analitica del dataset antes de pasar a feature engineering y modelado.

La pregunta sustantiva del proyecto es:

> Existe una asociacion estadisticamente significativa entre las caracteristicas de la regulacion de IA de un pais y el desarrollo de su ecosistema de IA, despues de controlar por factores socioeconomicos e institucionales?

Fase 4 no debe responder causalmente esta pregunta todavia. Debe preparar el terreno para responderla bien.

Fase 4 debe producir:

- diagnostico de calidad estadistica;
- mapas de cobertura;
- perfiles de pais;
- comparacion de Chile;
- identificacion de variables prometedoras;
- deteccion de ruido y redundancia;
- primeros patrones entre bloques;
- recomendaciones para Fase 5.

---

## 2. Inputs oficiales desde Fase 3

Fase 4 debe leer los datos desde la API publica siempre que sea posible.

Ejemplo:

```python
from src.fase3.api import (
    load_wide,
    load_panel,
    load_snapshot,
    load_dictionary,
    get_block,
    get_chile_snapshot,
)

wide = load_wide()
panel = load_panel()
snapshot = load_snapshot()
dictionary = load_dictionary()
chile = get_chile_snapshot()
```

Archivos principales si se necesita inspeccion manual:

```text
outputs/matriz_madre_wide.csv
outputs/matriz_larga_panel.csv
outputs/matriz_larga_snapshot.csv
outputs/fase3_diccionario_variables.csv
outputs/matriz_madre_trazabilidad.csv
outputs/fase3_reporte_calidad_matriz.csv
outputs/fase3_reporte_calidad_matriz.md
```

La wide es la tabla principal para EDA. El panel y snapshot se usan para auditoria, sensibilidad temporal y chequeos.

---

## 3. Contrato de datos para Fase 4

### 3.1 Wide

Archivo/API:

```text
load_wide()
outputs/matriz_madre_wide.csv
```

Uso:

- EDA pais x atributo;
- distribuciones;
- missingness;
- correlaciones;
- perfiles pais;
- comparacion Chile vs peers;
- seleccion preliminar de variables.

Metadata disponible:

- `iso3`
- `country_name_canonical`
- `entity_type`
- `region`
- `income_group`
- `n_sources_present`
- `source_list`
- `n_variables_available`
- `pct_variables_available`
- `included_in_matrix`
- `included_in_dense_candidate`
- `inclusion_notes`

Cada variable tiene columnas auxiliares:

- `<variable>`
- `<variable>_year_used`
- `<variable>_confidence`

### 3.2 Diccionario

Archivo/API:

```text
load_dictionary()
outputs/fase3_diccionario_variables.csv
```

Uso:

- saber tipo, unidad y direccion de cada variable;
- filtrar variables utiles para Fase 4;
- agrupar por bloques tematicos;
- distinguir variables primarias y redundantes;
- detectar baja cobertura;
- evitar interpretar rankings o scores al reves.

Campos clave:

- `bloque_tematico`
- `unit`
- `direction`
- `pct_complete`
- `n_countries_available`
- `fase4_role`
- `included_in_fase4_eda`
- `is_primary`
- `redundant_with`
- `known_limitations`

### 3.3 Snapshot

Archivo/API:

```text
load_snapshot()
outputs/matriz_larga_snapshot.csv
```

Uso:

- auditar el valor final usado en wide;
- revisar `year_used`;
- estudiar variables por fuente;
- ver `confidence_level`;
- rastrear cambios si una variable parece anomala.

### 3.4 Panel

Archivo/API:

```text
load_panel()
outputs/matriz_larga_panel.csv
```

Uso:

- explorar dinamica temporal;
- revisar tendencia 2018-2026;
- evaluar si el snapshot pierde informacion;
- preparar features temporales para Fase 5.

### 3.5 Trazabilidad

Archivo:

```text
outputs/matriz_madre_trazabilidad.csv
```

Uso:

- verificar cualquier celda;
- defender valores frente a revision academica;
- ubicar fuente, hoja, variable original y row identifier.

---

## 4. Prohibiciones en Fase 4

Fase 4 no debe:

- imputar valores faltantes como si fueran datos reales;
- decidir el modelo final;
- transformar variables sin registrar la regla;
- mezclar territorios o entidades excluidas en la muestra principal;
- usar variables sin consultar el diccionario;
- tratar todos los WIPO scores como outcome final sin discusion;
- asumir que `regulatory_treatment` ya es X causal definitiva;
- asumir que `ecosystem_outcome` ya es Y definitiva;
- convertir missing en cero;
- modificar outputs de Fase 3.

Si Fase 4 necesita nuevos datos, debe documentarlos como extension, no alterar silenciosamente Fase 3.

---

## 5. Estructura recomendada de outputs de Fase 4

Crear una carpeta separada:

```text
outputs/eda_principal/
```

Outputs recomendados:

```text
outputs/eda_principal/
├── README_EDA_PRINCIPAL.md
├── manifest_eda_principal.json
├── eda_quality_overview.csv
├── eda_missingness_by_country.csv
├── eda_missingness_by_variable.csv
├── eda_missingness_by_block.csv
├── eda_variable_summary.csv
├── eda_numeric_distributions.csv
├── eda_categorical_distributions.csv
├── eda_outliers.csv
├── eda_correlations_spearman.csv
├── eda_correlations_pearson.csv
├── eda_redundancy_report.csv
├── eda_block_scores_exploratory.csv
├── eda_country_profiles.csv
├── eda_chile_profile.csv
├── eda_chile_vs_peers.csv
├── eda_singapore_uae_ireland_profiles.csv
├── eda_candidates_for_feature_engineering.csv
├── eda_decisions_for_fase5.yaml
└── EDA_Principal_Fase4.html
```

El HTML o notebook debe ser comunicable a humanos, pero los CSV deben ser la base reproducible.

---

## 6. Pasos recomendados del EDA Principal

### Paso 1 - Cargar y verificar contrato

Acciones:

- cargar `wide`, `dictionary`, `snapshot`, `panel`;
- confirmar version `1.x` actual (al cierre: `1.1` por quality fix de country_name_canonical);
- validar shapes esperados;
- confirmar que no hay entidades excluidas;
- confirmar que Chile esta presente;
- confirmar bloques disponibles.

Checks minimos:

```python
assert wide["iso3"].is_unique
assert (wide["entity_type"] == "country_iso3").all()
assert "CHL" in set(wide["iso3"])
```

### Paso 2 - Separar metadata y variables analiticas

Definir:

- columnas ID;
- columnas de valor;
- columnas `_year_used`;
- columnas `_confidence`.

No analizar columnas auxiliares como si fueran variables sustantivas.

### Paso 3 - Revisar cobertura global

Analisis:

- porcentaje de variables disponibles por pais;
- porcentaje de paises disponibles por variable;
- cobertura por fuente;
- cobertura por bloque;
- cobertura por region e income group.

Preguntas:

- Que paises tienen suficiente informacion para EDA?
- Que variables tienen cobertura demasiado baja?
- Que bloques son mas densos?
- Chile tiene cobertura suficiente para comparaciones?

### Paso 4 - Analizar missingness

Generar:

- missingness por pais;
- missingness por variable;
- missingness por bloque;
- heatmap pais-variable;
- missingness por region;
- missingness por income group.

Clasificar variables:

- alta cobertura: >= 70%;
- cobertura media: 30%-70%;
- baja cobertura: < 30%.

Variables de regulacion IA con baja cobertura no deben eliminarse automaticamente, porque pueden ser sustantivamente centrales.

### Paso 5 - Estadistica descriptiva univariada

Para variables numericas:

- n;
- media;
- mediana;
- desviacion estandar;
- min;
- max;
- p1, p5, p10, p25, p75, p90, p95, p99;
- skewness;
- kurtosis;
- IQR;
- numero de outliers por regla IQR;
- numero de ceros si corresponde;
- rango teorico esperado por `unit`.

Para variables categoricas/binarias:

- frecuencia;
- proporcion;
- numero de categorias;
- categoria modal;
- rare categories;
- cardinalidad.

Separar por `unit`:

- `score_0_100`
- `pct`
- `usd`
- `count`
- `wgi_-2.5_2.5`
- `binary`
- `categorical`

### Paso 6 - Deteccion de outliers y valores anómalos

Identificar:

- paises extremos por variable;
- valores fuera de rango teorico;
- valores raros por bloque;
- diferencias extremas entre fuentes redundantes;
- valores con `year_used` antiguo.

No borrar outliers en Fase 4. Documentarlos para Fase 5-7.

### Paso 7 - Analisis por bloques tematicos

Bloques:

- `regulatory_treatment`
- `ecosystem_outcome`
- `adoption_diffusion`
- `socioeconomic_control`
- `institutional_control`
- `tech_infrastructure_control`

Para cada bloque:

- cobertura;
- distribuciones;
- principales variables;
- redundancias;
- correlaciones internas;
- paises lideres y rezagados;
- Chile dentro del bloque;
- interpretacion preliminar.

Importante: los bloques no son aun modelo causal. Son estructura exploratoria.

### Paso 8 - Correlaciones y asociaciones preliminares

Calcular:

- Pearson para variables numericas razonablemente continuas;
- Spearman para rankings/scores/no linealidad;
- Cramer's V o asociaciones categoricas si aplica;
- point-biserial para binarias vs continuas si aplica;
- matrices por bloque;
- matrices entre bloques.

Priorizar:

- regulatory vs ecosystem;
- regulatory vs adoption;
- ecosystem vs tech infrastructure;
- ecosystem vs socioeconomic;
- regulatory vs institutional.

No interpretar correlacion como causalidad.

### Paso 9 - Redundancia y ruido

Usar:

- `is_primary`;
- `redundant_with`;
- correlaciones altas;
- baja varianza;
- cobertura baja;
- variables casi constantes;
- duplicacion conceptual.

Clasificar variables:

- conservar para Fase 5;
- conservar como contexto;
- candidata a excluir;
- requiere revision humana;
- posible proxy.

Este paso responde parcialmente la pregunta: que variables son senal y que variables son ruido?

### Paso 10 - Binding vs non-binding

Construir una primera lectura descriptiva:

Binding:

- leyes vigentes;
- proyectos de ley;
- autoridad regulatoria;
- convenciones vinculantes;
- obligaciones o enforcement si existe.

Non-binding:

- estrategias nacionales;
- principios;
- declaraciones;
- marcos voluntarios;
- adhesiones a iniciativas internacionales no vinculantes.

Acciones:

- identificar variables IAPP/Stanford/OECD que correspondan a binding/non-binding;
- hacer tablas de frecuencia;
- comparar contra outcomes de ecosistema;
- evaluar si binding y non-binding tienen comportamientos distintos.

No crear aun indice definitivo sin Fase 5.

### Paso 11 - Condiciones habilitantes e inhabilitantes

Crear taxonomia exploratoria de proxies.

Condiciones habilitantes posibles:

- gobierno efectivo;
- rule of law;
- calidad regulatoria;
- infraestructura digital;
- disponibilidad de datos;
- capital humano;
- gasto en R&D;
- adopcion empresarial de IA;
- conectividad;
- innovacion;
- cloud/ICT/OECD;
- ciberseguridad;
- apertura economica.

Condiciones inhabilitantes posibles:

- alta restrictividad;
- baja calidad institucional;
- baja conectividad;
- bajo capital humano;
- baja inversion;
- alta incertidumbre regulatoria;
- baja cobertura de datos;
- indicadores lower-better elevados.

Fase 4 debe identificar buenos candidatos, no cerrar indices finales.

### Paso 12 - Chile como caso focal

Generar perfil de Chile:

- valores por bloque;
- ranking preliminar entre paises comparables;
- distancia a promedio global;
- distancia a LATAM;
- distancia a OECD;
- fortalezas;
- debilidades;
- variables faltantes;
- variables donde Chile es outlier.

Comparaciones recomendadas:

- Chile vs LATAM: Argentina, Brasil, Colombia, Mexico, Peru, Uruguay.
- Chile vs OECD relevantes.
- Chile vs lideres IA: Singapore, United Arab Emirates, Ireland, United States, United Kingdom.

### Paso 13 - Deep dives: Singapur, Emiratos Arabes Unidos e Irlanda

Objetivo:

Responder exploratoriamente:

> Por que Singapur, Emiratos Arabes Unidos e Irlanda parecen tan avanzados o atractivos para IA?

Analizar:

- readiness Oxford;
- WIPO innovation;
- adopcion/difusion;
- infraestructura digital;
- calidad institucional;
- estrategia nacional;
- regulacion binding/non-binding;
- apertura economica;
- capital humano;
- gobierno digital;
- comparacion contra Chile.

Output:

```text
eda_singapore_uae_ireland_profiles.csv
```

Tambien producir narrativa preliminar en el reporte EDA.

### Paso 14 - Exploracion temporal

Usar panel cuando sea posible:

- Oxford 2020-2025;
- WIPO 2021-2025;
- WB 2018-2025;
- OECD 2018-2025;
- Anthropic ventanas recientes;
- Microsoft 2025.

Analizar:

- estabilidad de variables;
- cambios recientes;
- valores antiguos usados por falta de datos;
- sensibilidad del snapshot.

No modelar aun panel completo salvo exploracion.

### Paso 15 - Preparar recomendaciones para Fase 5

Fase 4 debe terminar con una lista clara:

- variables candidatas a outcome;
- variables candidatas a tratamiento regulatorio;
- controles recomendados;
- variables redundantes a resolver;
- variables a transformar;
- variables a imputar o no imputar;
- variables a excluir;
- proxies habilitantes/inhabilitantes;
- posibles indices compuestos.

Output:

```text
eda_candidates_for_feature_engineering.csv
eda_decisions_for_fase5.yaml
```

---

## 7. Estadistica recomendada

Fase 4 debe incluir tanta estadistica descriptiva como sea razonable, sin caer en modelado causal prematuro.

Minimo:

- conteos;
- completitud;
- media;
- mediana;
- desviacion estandar;
- percentiles;
- IQR;
- skewness;
- kurtosis;
- outliers;
- correlaciones Pearson;
- correlaciones Spearman;
- matriz de missingness;
- analisis por region;
- analisis por income group;
- analisis por bloque.

Recomendado:

- PCA exploratorio por bloque solo como diagnostico, no como feature final;
- clustering exploratorio de paises;
- dendrograma/correlacion de variables;
- VIF preliminar para detectar multicolinealidad;
- mutual information exploratoria;
- comparaciones de distribuciones entre grupos binding/non-binding;
- bootstrap de rankings descriptivos si se construyen scores exploratorios;
- analisis de sensibilidad del snapshot para variables con panel.

No recomendado en Fase 4:

- regresion final;
- p-values como prueba de hipotesis principal;
- inferencia causal;
- imputacion definitiva;
- indices compuestos definitivos.

---

## 8. Variables y preguntas futuras

La Fase 3 permite iniciar algunas preguntas, pero no todas estan directamente disponibles.

### 8.1 Binding vs non-binding

Factible con Fase 3 actual.

Fase 4 debe crear una tabla de variables regulatorias y clasificarlas:

- binding;
- non-binding;
- hybrid;
- unknown.

### 8.2 Probabilidad de creacion de ley

No existe como variable directa.

Fase 4 puede identificar proxies:

- proyecto de ley IA;
- estrategia nacional IA;
- numero de autoridades;
- firmas internacionales;
- politica de IA;
- madurez de gobernanza;
- trayectoria institucional.

Fase 5 podria construir `regulatory_momentum_score`.

### 8.3 Condiciones habilitantes e inhabilitantes

Factible como taxonomia exploratoria.

Fase 4 debe mapear variables existentes y recomendar indices para Fase 5.

### 8.4 Datacenters, permisos, impuestos, corpus ambiental

No estan resueltos por Fase 3 actual.

Requieren extension de datos:

- tiempos de permisos de datacenter;
- impuesto corporativo;
- regulacion energetica;
- regulacion ambiental;
- permisos de construccion;
- disponibilidad energetica;
- costo energetico;
- restricciones de agua;
- corpus legal ambiental.

Esto puede ser una Fase 3B o una extension antes de Fase 5.

### 8.5 EEUU por estado y otros paises federales

No mezclar con la matriz pais-pais actual.

Requiere matriz subnacional separada:

```text
unidad = estado/provincia/region subnacional x atributo
```

Casos prioritarios:

- Texas;
- California;
- Washington;
- posiblemente Massachusetts/New York/Virginia;
- estados/provincias de Canada, Alemania, Australia, Brasil, Mexico e India si se decide.

---

## 9. Criterios de calidad para cerrar Fase 4

Fase 4 puede considerarse lista cuando:

- todos los outputs de EDA existen;
- se documento cobertura por pais, variable, bloque, region e income group;
- se identificaron variables con baja cobertura;
- se identificaron variables redundantes;
- se generaron perfiles de Chile, Singapur, Emiratos e Irlanda;
- se propusieron candidatos a outcome y tratamiento sin cerrarlos causalmente;
- se genero lista de variables para Fase 5;
- se documentaron proxies habilitantes/inhabilitantes;
- se documentaron datos faltantes que requieren extension;
- no se modifico Fase 3;
- todo resultado se puede reproducir desde `src.fase3.api`.

---

## 10. Esqueleto recomendado de notebook o pipeline Fase 4

La Fase 4 puede ser notebook + modulos. Recomendado:

```text
src/fase4/
├── __init__.py
├── load.py
├── quality.py
├── missingness.py
├── distributions.py
├── correlations.py
├── blocks.py
├── countries.py
├── reporting.py
└── export.py

notebooks/
└── 03_eda_principal.ipynb
```

El notebook debe comunicar resultados; la logica debe vivir en `src/fase4/`.

---

## 11. Orden recomendado de implementacion

1. Crear carpeta `outputs/eda_principal/`.
2. Crear loader desde `src.fase3.api`.
3. Crear reporte de contrato y calidad inicial.
4. Separar metadata, variables, auxiliares.
5. Calcular missingness global.
6. Calcular descriptivos por variable.
7. Calcular descriptivos por bloque.
8. Generar perfiles de pais.
9. Generar Chile profile.
10. Generar perfiles Singapur, Emiratos e Irlanda.
11. Analizar correlaciones y redundancias.
12. Clasificar binding/non-binding.
13. Mapear condiciones habilitantes/inhabilitantes.
14. Proponer variables para Fase 5.
15. Exportar HTML/Markdown y CSV reproducibles.

---

## 12. Conclusión

Fase 3 entrega una base robusta y profesional para iniciar Fase 4. La tarea central de Fase 4 es convertir esa base en conocimiento exploratorio: entender estructura, cobertura, patrones, ruido, redundancia, comparabilidad y candidatos analiticos.

Si Fase 4 se ejecuta bajo este plan, el proyecto quedara preparado para una Fase 5 de feature engineering mucho mas solida y para una Fase 6 de modelado con supuestos claros, variables justificadas y datos defendibles.

