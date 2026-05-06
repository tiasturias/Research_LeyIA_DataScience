# Reporte de calidad Fase 3

**Version:** `1.1` (revision quality fix country_name_canonical, 2026-05-06)
**Tag git:** `matriz-madre-v1.1`

Este reporte resume la aptitud de la Matriz Madre para alimentar Fase 4.

- Paises/entidades comparables en wide: 199
- Variables en diccionario: 397
- Variables core para EDA: 198
- Variables con cobertura <30%: 48
- Paises con `country_name_canonical` correctamente resuelto: 199/199 (post-fix v1.1)
- Paises clave verificados manualmente: ARG, AUS, FRA, COL, BRA, CAN, CHN, USA, GBR, CHL, SGP, ARE, IRL

## Estado de tests al cierre

- `pytest -q`: **20 passed** en 8.77s.
- `python -m src.fase3 validate`: **Fase 3 validation passed**.

## Cambios desde v1.0

Ver `FASE3_CIERRE_DOCUMENTACION_TECNICA.md` seccion 12.1 para detalle del fix de country_name_canonical aplicado el 2026-05-06. Las metricas de filas/columnas/cobertura no cambiaron — solo se corrigio el nombre humano de paises afectados.

## Variables por bloque
- adoption_diffusion: 14
- ecosystem_outcome: 124
- institutional_control: 31
- regulatory_treatment: 33
- socioeconomic_control: 28
- tech_infrastructure_control: 167

## Metricas
```text
                                        metric     value status                                        notes
                                    panel_rows 151938.00   info                                          NaN
                                 snapshot_rows  53596.00   info                                          NaN
                                     wide_rows    199.00   info                                          NaN
                                  wide_columns   1203.00   info                                          NaN
                          dictionary_variables    397.00   info                                          NaN
                             traceability_rows  53178.00   info                                          NaN
                             included_entities    199.00   info                                          NaN
                      wide_zero_value_entities      0.00   pass                                          NaN
                variables_under_30pct_complete     48.00   warn                                          NaN
                            core_eda_variables    198.00   info                                          NaN
                       panel_duplicate_cell_id      0.00   pass                                          NaN
                  trace_duplicate_cell_id_wide      0.00   pass                                          NaN
                 dictionary_duplicate_variable      0.00   pass                                          NaN
                               panel_rows_iapp    532.00   info                                          NaN
                          panel_rows_microsoft    441.00   info                                          NaN
                             panel_rows_oxford  24002.00   info                                          NaN
                                 panel_rows_wb  46475.00   info                                          NaN
                               panel_rows_wipo  68047.00   info                                          NaN
                           panel_rows_stanford   1153.00   info                                          NaN
                               panel_rows_oecd   9929.00   info                                          NaN
                          panel_rows_anthropic   1359.00   info                                          NaN
            variables_block_adoption_diffusion     14.00   info                                          NaN
             variables_block_ecosystem_outcome    124.00   info                                          NaN
         variables_block_institutional_control     31.00   info                                          NaN
          variables_block_regulatory_treatment     33.00   info                                          NaN
         variables_block_socioeconomic_control     28.00   info                                          NaN
   variables_block_tech_infrastructure_control    167.00   info                                          NaN
         countries_with_any_adoption_diffusion     91.96   info percent of wide rows with >=1 value in block
          countries_with_any_ecosystem_outcome     98.49   info percent of wide rows with >=1 value in block
      countries_with_any_institutional_control     98.99   info percent of wide rows with >=1 value in block
       countries_with_any_regulatory_treatment     75.88   info percent of wide rows with >=1 value in block
      countries_with_any_socioeconomic_control     99.50   info percent of wide rows with >=1 value in block
countries_with_any_tech_infrastructure_control    100.00   info percent of wide rows with >=1 value in block
                  traceability_blocking_issues      0.00   pass                                             
```