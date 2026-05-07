# Cierre tecnico Fase 5 MVP

Fecha de cierre: 2026-05-06

## Estado

Fase 5 queda cerrada como preparacion de datos MVP para Fase 6.

La fase deja una base reproducible, auditable y lista para modelado, sin modificar Fase 3 ni Fase 4. El foco de esta fase fue convertir la Matriz Madre y las decisiones EDA en una matriz de features gobernada por contratos claros.

## Funcion de Fase 5 dentro del proyecto

Fase 5 cumple el rol CRISP-DM de `Data Preparation`. En terminos practicos:

- toma datos limpios y trazables de Fase 3;
- toma criterios metodologicos de Fase 4;
- define la muestra MVP;
- selecciona variables reales observadas;
- crea transformaciones reproducibles;
- documenta faltantes y cobertura;
- entrega a Fase 6 una matriz unica de modelado.

Esto evita que Fase 6 mezcle exploracion, limpieza y modelado en el mismo paso.

## Insumos usados

Desde Fase 3:

- Matriz Madre wide oficial.
- Diccionario de variables.
- Trazabilidad de celdas para auditoria en Excel.

Desde Fase 4:

- Decisiones EDA revisadas para Fase 5.
- Taxonomia regulatoria binding, non-binding e hybrid.
- Criterios de submuestra y cautelas metodologicas.

Todos estos insumos quedan hasheados en `outputs/fase5_manifest.json`.

## Resultados principales

- Muestra MVP: 43 paises.
- Variables observadas core: 40 variables reales verificadas contra Fase 3.
- Matriz humana principal: `6_Matriz_40_Humana` en el Excel, 43 paises x 40 variables observadas, mas 4 identificadores.
- Feature matrix tecnica: `outputs/feature_matrix_mvp.csv`, 43 filas x 126 columnas.
- Cobertura minima: 41.86%.
- Umbral preregistrado de cobertura: 30%.
- Imputacion: ninguna.
- Outliers: preservados.
- Fase 3/Fase 4 modificadas: no.
- API publica: `FASE5.src.api`.

## Diferencia entre 40 variables y 126 columnas

Las 40 variables son el nucleo observado del estudio. Son las variables sustantivas que representan regulacion IA, inversion, adopcion, innovacion y controles.

Las 126 columnas de `feature_matrix_mvp.csv` incluyen ademas:

- metadatos de pais;
- variables observadas originales;
- transformaciones log;
- z-scores robustos;
- agregados regulatorios derivados de Fase 4;
- codificaciones one-hot de categorias regulatorias;
- columna `split` para modelado.

Por eso el Excel separa:

- `6_Matriz_40_Humana`: lectura humana sustantiva;
- `11_Features_Fase6`: matriz tecnica para modelado;
- `12_Diccionario_Cols`: explicacion de cada columna tecnica.

## Excel auditable

`outputs/MVP_AUDITABLE.xlsx` fue reorganizado para lectura humana. Contiene 15 hojas:

- `0_Leer_Primero`: guia ejecutiva en lenguaje simple.
- `1_Hipotesis`: hipotesis principal y subpreguntas Q1-Q4.
- `2_Como_Auditar`: protocolo human-in-the-loop para auditar variables y celdas.
- `3_Paises_43`: paises, regiones, grupos de ingreso, motivos de inclusion y notas.
- `4_Ingreso_Region`: explicacion de `income_group`, conteos por grupo y regiones.
- `5_Variables_40`: las 40 variables reales, ID V01-V40, codigo exacto y rol analitico.
- `6_Matriz_40_Humana`: matriz principal 43 x 40 para auditoria sustantiva.
- `7_Leyenda_Colores`: significado exacto de los colores usados.
- `8_Casos_Atencion`: casos que requieren cuidado, incluyendo Taiwan.
- `9_Normalizacion`: explicacion didactica y metodologica de normalizacion, escalado, logs, z-scores, one-hot y no imputacion.
- `10_Cobertura`: completitud por variable.
- `11_Features_Fase6`: matriz tecnica completa para Fase 6.
- `12_Diccionario_Cols`: diccionario de las 126 columnas.
- `13_Trazabilidad`: origen de datos de Fase 3.
- `14_Transformaciones`: parametros log y robust z-score.

Las cabeceras usan colores para distinguir variables observadas, metadatos, transformaciones y columnas tecnicas.

## Sobre income_group

`income_group` es metadata de pais heredada desde Fase 3, basada en clasificacion tipo World Bank. Se usa como contexto/posible control; no es una variable creada por Fase 5.

Distribucion en la muestra MVP:

- High income: 35.
- Upper middle income: 6.
- Lower middle income: 1.
- Sin clasificacion disponible: 1.

## Artefactos listos para Fase 6

Fase 6 debe consumir preferentemente:

- `FASE5.src.api.load_phase6_feature_matrix()`
- `FASE5.src.api.load_phase6_schema()`
- `FASE5.src.api.load_phase6_column_groups()`
- `FASE5.src.api.load_phase6_modeling_contract()`
- `FASE5.src.api.load_phase6_ready_manifest()`
- `FASE5.src.api.load_phase6_llm_context()`

Ademas, Fase 5 entrega un bundle tecnico independiente en:

`FASE5/outputs/phase6_ready/`

Este bundle es la interfaz maquina-a-maquina entre preparacion y modelado. No esta optimizado para lectura humana; para auditoria humana usar `MVP_AUDITABLE.xlsx`.

Archivos del bundle:

- `phase6_feature_matrix.csv`
- `phase6_schema.csv`
- `phase6_schema.json`
- `phase6_column_groups.yaml`
- `phase6_modeling_contract.yaml`
- `phase6_missingness_by_column.csv`
- `phase6_missingness_by_country.csv`
- `phase6_variables_catalog.csv`
- `phase6_transform_params.csv`
- `phase6_train_test_split.csv`
- `phase6_llm_context.json`
- `phase6_ready_manifest.json`

## Validacion ejecutada

```bash
make fase5-all
```

Resultado:

- Build Fase 5: OK.
- Tests Fase 5: 15 passed.
- Validador Fase 5: OK.
- Notebook Fase 5: ejecuta sin errores y no cambia outputs oficiales.

## Restricciones metodologicas preservadas

- Fase 3 y Fase 4 son insumos inmutables.
- No se crean variables fantasma.
- No se imputan faltantes.
- No se eliminan outliers en Fase 5.
- NLP legal queda fuera del MVP.
- Los parametros de transformacion son auditables.
- El split train/test queda congelado para modelado inicial.

---

## Actualizacion v2.0 - 2026-05-07

Fase 5 queda actualizada de forma backwards-compatible para habilitar Fase 6 v0.4 con Q1-Q6. Esta actualizacion no reabre Fase 3 ni Fase 4, no incorpora PCA y no cambia la submuestra de 43 paises.

Cambios principales:

- Variables observadas core: 40 -> 46.
- Nuevas variables v2.0: `oxford_e_government_delivery`, `oxford_government_digital_policy`, `oxford_ind_data_governance`, `oxford_governance_ethics`, `oecd_2_indigo_oecd_indigo_score`, `oecd_4_digital_gov_oecd_digital_gov_overall`.
- Feature matrix tecnica: `43 x 138`.
- Excel auditable: 17 hojas, agregando `5b_Variables_46_Detalle` y `11b_Features_Fase6_v2`.
- Bundle `phase6_ready/`: version `0.2`, contrato Q1-Q6, Q5/Q6 y `overlap_y_variables`.
- Tests Fase 5: 28 passed.

Decision F5-V2-004:

No se incorpora reduccion dimensional PCA en Fase 5. Fase 4 ya contiene analisis exploratorio de redundancia y estructura de varianza (`eda_redundancy_report.csv`, `eda_inter_block_correlations.csv`, `eda_candidates_for_feature_engineering.csv`). Con N=43 y p aproximado mayor a 100, PCA no es estable ni suficientemente interpretable para audiencia politica. Q4 clustering y Ridge/Lasso cubren la funcion analitica relevante sin contaminar el contrato primario de modelado.

Artefactos v2.0 listos para Fase 6:

- `outputs/feature_matrix_mvp.csv`: `43 x 138`.
- `outputs/MVP_AUDITABLE.xlsx`: 17 hojas.
- `outputs/phase6_ready/phase6_modeling_contract.yaml`: version `0.2`, incluye `Q5`, `Q6`, `Y_Q5_population_usage`, `Y_Q6_public_sector`, `Y_Q6_public_sector_aux` y `overlap_y_variables`.
- `outputs/phase6_ready/phase6_ready_manifest.json`: version `0.2`, hashes regenerados.
- `outputs.v1.0.backup/`: respaldo pre-update para auditoria de preservacion v1.0.

Validacion ejecutada:

```bash
python3 -m FASE5.src.build
python3 -m FASE5.src.validate
python3 -m pytest tests/ -v
```

Resultado:

- Build Fase 5 v2.0: OK.
- Validador Fase 5: OK.
- Tests Fase 5: 28 passed.
- Fase 3 hashes intactos: 74/74.
- Bundle sin artefactos PCA.
