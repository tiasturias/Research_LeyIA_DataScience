# FASE5 - Data Preparation MVP

Fase 5 es la etapa de preparacion de datos del MVP end-to-end. Su trabajo no es modelar todavia; su trabajo es dejar una base limpia, trazable y entendible para que Fase 6 pueda estimar modelos sin rehacer decisiones metodologicas.

## Que hace Fase 5

1. Define la muestra MVP de 43 paises.
2. Selecciona 46 variables observadas reales, todas verificadas contra el diccionario oficial de Fase 3.
3. Construye una matriz humana `43 x 46` para auditoria sustantiva.
4. Construye una matriz tecnica `43 x 138` para modelado en Fase 6.
5. Genera transformaciones auditables: log, signed log, robust z-score, one-hot categorico y agregados regulatorios.
6. Preserva los valores faltantes. No imputa.
7. Congela un split `train/test` reproducible para modelado inicial.
8. Produce un Excel auditable pensado para lectura humana, no solo para programadores.

## Por que esta fase es importante

Fase 5 es el puente entre la evidencia descriptiva y el modelado. Si esta fase queda confusa, Fase 6 puede parecer matematica pero estar mal fundada. Por eso aqui quedan explicitados:

- que paises entran al MVP;
- que variables entran al estudio real;
- cuales columnas son metadatos o transformaciones tecnicas;
- que datos faltan y por que no se rellenan;
- que decisiones vienen de Fase 4;
- que artefactos debe consumir Fase 6.

## Que consume de Fase 3

Fase 5 consume Fase 3 como fuente oficial de datos estructurados:

- `load_wide()`: Matriz Madre wide con paises, metadata y variables.
- `load_dictionary()`: diccionario de variables oficiales.
- `matriz_madre_trazabilidad.csv`: solo para auditar origen de celdas en Excel.

Fase 5 no modifica Fase 3. El manifiesto hashea los insumos usados para comprobar inmutabilidad.

## Que consume de Fase 4

Fase 5 consume Fase 4 como fuente metodologica:

- decisiones EDA para Fase 5;
- taxonomia regulatoria `binding / non_binding / hybrid`;
- criterios de submuestra revisados;
- cautelas sobre cobertura, redundancia y variables admisibles.

Fase 5 no modifica Fase 4. Sus outputs tambien quedan hasheados en el manifiesto.

## Por que sirve para Fase 6

Fase 6 necesita una matriz lista para modelar, no una coleccion de CSV sueltos. Fase 5 entrega:

- una matriz tecnica con las 46 variables observadas y sus features derivadas;
- roles analiticos de cada variable: regulacion, inversion, adopcion, innovacion y controles;
- split train/test congelado;
- parametros de transformacion;
- un diccionario de columnas para evitar confundir variables reales con columnas tecnicas.

Fase 6 debe consumir preferentemente `FASE5.src.api`, especialmente:

- `load_phase6_feature_matrix()`
- `load_phase6_schema()`
- `load_phase6_column_groups()`
- `load_phase6_modeling_contract()`
- `load_phase6_ready_manifest()`
- `load_phase6_llm_context()`

Tambien existe un paquete tecnico independiente en `outputs/phase6_ready/`. Esta carpeta no esta pensada para lectura politica ni didactica; es el contrato maquina-a-maquina entre Fase 5 y Fase 6.

## Resultados obtenidos

- Muestra MVP: 43 paises.
- Variables observadas reales: 46.
- Matriz humana auditable: 43 paises x 46 variables, mas 4 columnas identificadoras.
- Feature matrix para Fase 6: 43 filas x 138 columnas.
- Cobertura minima de las 46 variables: 41.86%.
- Umbral preregistrado de cobertura: 30%.
- Outputs Fase 3/Fase 4 modificados: 0.
- Imputaciones realizadas: 0.
- Tests Fase 5: 28 passed.
- Notebook auditable: ejecuta sin cambiar outputs oficiales.

## Como leer `MVP_AUDITABLE.xlsx`

El Excel esta disenado para auditoria humana. Las hojas principales son:

- `0_Leer_Primero`: lectura ejecutiva en lenguaje simple.
- `1_Hipotesis`: hipotesis principal y subpreguntas Q1-Q6.
- `2_Como_Auditar`: pasos concretos para auditoria human-in-the-loop.
- `3_Paises_43`: muestra de paises, region, grupo de ingreso, motivo de inclusion y notas.
- `4_Ingreso_Region`: definicion de `income_group`, conteos y regiones.
- `5_Variables_40`: catalogo de variables reales del estudio, con ID V01-V46, codigo exacto, rol, transformacion y forma de auditoria.
- `5b_Variables_46_Detalle`: detalle de las 6 variables agregadas en v2.0 para Q6.
- `6_Matriz_40_Humana`: matriz humana principal. Aqui estan los 43 paises y las 46 variables observadas. Esta es la hoja mas importante para lectura sustantiva.
- `7_Leyenda_Colores`: explica exactamente cada color usado en los encabezados.
- `8_Casos_Atencion`: paises/casos que requieren cuidado, incluyendo Taiwan.
- `9_Normalizacion`: explica por que se normaliza, que se hizo, que no corrige y como se audita.
- `10_Cobertura`: cobertura variable por variable dentro de la muestra MVP.
- `11_Features_Fase6`: matriz tecnica completa para modelado.
- `11b_Features_Fase6_v2`: matriz tecnica completa v2.0.
- `12_Diccionario_Cols`: explica cada una de las 138 columnas de la matriz tecnica.
- `13_Trazabilidad`: origen de los datos desde Fase 3.
- `14_Transformaciones`: parametros y metodos usados para logs y z-scores.

En el Excel, las 46 variables observadas aparecen destacadas con color. Las columnas tecnicas tienen colores distintos para que no se confundan con el nucleo del estudio.

## Sobre `income_group`

`income_group` es una metadata de pais heredada de Fase 3, basada en clasificacion de ingreso tipo World Bank. No es una variable creada por Fase 5 ni un resultado del modelo.

En esta muestra aparecen:

- `High income`: 35 paises.
- `Upper middle income`: 6 paises.
- `Lower middle income`: 1 pais.
- sin clasificacion disponible en metadata Fase 3: 1 entidad.

## Outputs

- `outputs/feature_matrix_mvp.csv`: matriz tecnica para Fase 6, 43 x 138.
- `outputs/coverage_report_mvp.csv`: cobertura de las 46 variables observadas.
- `outputs/mvp_countries.csv`: muestra MVP documentada.
- `outputs/mvp_variables_catalog.csv`: catalogo de variables y roles analiticos.
- `outputs/mvp_transform_params.csv`: metodos log y robust z-score.
- `outputs/mvp_train_test_split.csv`: split reproducible 80/20.
- `outputs/MVP_AUDITABLE.xlsx`: Excel auditable con 17 hojas explicativas.
- `outputs/phase6_ready/`: version 100% tecnica para Fase 6.
- `outputs/fase5_manifest.json`: hashes de insumos, implementacion y outputs.

## Bundle tecnico para Fase 6

`outputs/phase6_ready/` contiene:

- `phase6_feature_matrix.csv`: matriz unica de modelado.
- `phase6_schema.csv` y `phase6_schema.json`: schema columna por columna.
- `phase6_column_groups.yaml`: grupos de columnas para seleccion de features.
- `phase6_modeling_contract.yaml`: contrato de modelado, reglas y roles.
- `phase6_missingness_by_column.csv`: faltantes por columna.
- `phase6_missingness_by_country.csv`: faltantes por pais.
- `phase6_variables_catalog.csv`: catalogo tecnico de variables.
- `phase6_transform_params.csv`: parametros de transformacion.
- `phase6_train_test_split.csv`: split congelado.
- `phase6_llm_context.json`: indice estructurado para LLM/codigo.
- `phase6_ready_manifest.json`: hashes del bundle.

## Comandos

Desde `F5_F8_MVP/`:

```bash
python3 -m FASE5.src.build
pytest FASE5/tests -v
python3 -m FASE5.src.validate
jupyter nbconvert --to notebook --execute --inplace FASE5/notebooks/05_data_preparation.ipynb
```

O todo junto:

```bash
make fase5-all
```
