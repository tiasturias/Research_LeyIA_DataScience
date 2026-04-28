# Variables Microsoft AI Economy Institute — AI Diffusion Report

## Proposito

Este documento consolida, con criterio de auditoria, la trazabilidad completa de la fuente Microsoft AI Economy Institute (AIEI) usada para construir la variable `ai_adoption_rate` del estudio.

Su objetivo es dejar documentado de forma profesional:
- que se extrajo exactamente;
- desde que URLs y activos se obtuvo;
- como se transformo el contenido crudo en tablas utilizables;
- que archivos finales se generaron;
- que controles de calidad se ejecutaron;
- que limitaciones y exclusiones siguen vigentes.

## Resumen Ejecutivo

Microsoft AIEI aporta la variable target de adopcion `ai_adoption_rate`, definida como el porcentaje de la poblacion en edad de trabajar que usa activamente IA generativa.

La fuente fue explotada al maximo disponible en formato tabular:
- se identificaron y extrajeron las 2 tablas HTML completas de la pagina oficial;
- se normalizaron los 147 registros globales del reporte;
- se completo el mapeo ISO3 para los 147 paises/territorios presentes en la fuente;
- se construyeron 4 tablas operativas para uso raw, muestra, panel y snapshot;
- se valido la consistencia de valores clave contra el reporte publicado.

En la muestra del estudio, la cobertura final es 75 de 86 paises:
- 58 de 63 paises ACTIVOS;
- 17 de 23 paises SOLO Y;
- 11 paises de la muestra no estan presentes en el dataset de Microsoft, por lo que su ausencia responde a cobertura de fuente y no a errores de scraping o mapeo.

## Fuente Y Proveniencia

| campo | detalle |
|---|---|
| emisor | Microsoft AI Economy Institute (AIEI) |
| producto | Microsoft AI Diffusion Report |
| fuente primaria | `https://www.microsoft.com/en-us/research/group/aiei/ai-diffusion/` |
| PDF H1 verificado | `https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/Microsoft-AI-Diffusion-Report.pdf` |
| PDF H2 verificado | `https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/Microsoft-AI-Diffusion-Report-2025-H2.pdf` |
| tipo de acceso | HTML publico en pagina WordPress |
| API publica | No disponible |
| CSV descargable | No disponible |
| cobertura visible | 147 paises/territorios |
| periodos visibles | H1 2025, H2 2025 |
| fecha de extraccion | 2026-04-08 |
| notebook de extraccion | `notebooks/01_recoleccion.ipynb` |
| carpeta de salida | `data/raw/Microsoft/` |

### Activos inspeccionados durante el discovery

| activo | estado | uso final |
|---|---|---|
| pagina HTML AIEI | exploitable | Fuente definitiva del scraping |
| tablas HTML embebidas | exploitable | Fuente efectiva de los 147 registros |
| PDF del reporte H1 2025 | inspeccionado | Verificacion documental, no usado para tabla |
| PDF del reporte H2 2025 | inspeccionado | Verificacion documental, no usado para tabla |
| indices Frontier / Infrastructure | no tabulares | Excluidos del ETL |

## Alcance De Extraccion

### Contenido tabular efectivamente extraido

La pagina contiene 2 tablas HTML con la misma estructura:

| tabla | filas de datos | columnas |
|---|---|---|
| tabla_1 | 74 | Economy, H1 2025 AI Diffusion, H2 2025 AI Diffusion, Change |
| tabla_2 | 73 | Economy, H1 2025 AI Diffusion, H2 2025 AI Diffusion, Change |

Columnas del reporte:
- `Economy`
- `H1 2025 AI Diffusion`
- `H2 2025 AI Diffusion`
- `Change`

Total consolidado: 147 filas de datos.

### Contenido no extraido

No se extrajeron los indices compuestos del reporte porque no estan expuestos como tabla estructurada en HTML o CSV y en el PDF aparecen como graficos, no como dataset tabular recuperable de forma robusta.

## Variable Canonica Y Campos Auxiliares

### Variable canonica del estudio

| campo | detalle |
|---|---|
| canonical_name | `ai_adoption_rate` |
| nombre funcional en la fuente | AI Diffusion |
| definicion operativa | porcentaje de la poblacion en edad de trabajar que usa activamente IA generativa |
| rol metodologico | Y core |
| unidad | porcentaje |
| periodo canonico | H2 2025 |
| periodo complementario | H1 2025 |
| granularidad | pais |

### Campos auxiliares conservados en los outputs

| campo | descripcion |
|---|---|
| `country_name_ms` | nombre del pais tal como aparece en Microsoft |
| `iso3` | codigo ISO 3166-1 alpha-3 normalizado |
| `ai_user_share_h1_2025` | valor de adopcion H1 2025 |
| `ai_user_share_h2_2025` | valor de adopcion H2 2025 |
| `ai_user_share_change_pp` | cambio en puntos porcentuales entre H2 y H1 |
| `source` | identificador de la fuente en los CSV |
| `report_edition` | etiqueta de cobertura temporal del raw |
| `report_url` | URL exacta de la pagina fuente |
| `year` | anio normalizado para outputs canonicos |
| `period` | periodo semestral normalizado (`H1` / `H2`) |

## Inventario De Tablas Generadas

| archivo | nivel | descripcion | filas | llave principal |
|---|---|---|---|---|
| `microsoft_ai_diffusion_raw.csv` | raw global | tabla cruda normalizada con los 147 registros de Microsoft | 147 | `country_name_ms` |
| `microsoft_ai_diffusion_study.csv` | raw muestra | subconjunto de la muestra de 86 paises con cobertura en Microsoft | 75 | `iso3` |
| `microsoft_ai_adoption_panel.csv` | panel | una fila por `iso3 x year x period` | 294 | `iso3`, `year`, `period` |
| `microsoft_ai_diffusion_snapshot.csv` | canonico | snapshot H2 2025 con `ai_adoption_rate` listo para modelamiento | 147 | `iso3` |

## Diccionario De Columnas

### `microsoft_ai_diffusion_raw.csv`

| columna | tipo esperado | descripcion |
|---|---|---|
| `country_name_ms` | string | nombre original de Microsoft |
| `iso3` | string | ISO3 normalizado |
| `ai_user_share_h1_2025` | float | porcentaje H1 2025 |
| `ai_user_share_h2_2025` | float | porcentaje H2 2025 |
| `ai_user_share_change_pp` | float | variacion H2 - H1 en puntos porcentuales |
| `source` | string | valor fijo: `Microsoft_AIEI` |
| `report_edition` | string | valor fijo: `H1_2025+H2_2025` |
| `report_url` | string | URL de la pagina fuente |

### `microsoft_ai_diffusion_study.csv`

Mantiene la misma estructura del raw global, filtrada a los paises de la muestra con cobertura efectiva en Microsoft.

### `microsoft_ai_adoption_panel.csv`

| columna | tipo esperado | descripcion |
|---|---|---|
| `iso3` | string | ISO3 normalizado |
| `country_name_ms` | string | nombre original en Microsoft |
| `year` | int | 2025 |
| `period` | string | `H1` o `H2` |
| `ai_adoption_rate` | float | porcentaje de adopcion para el periodo |
| `source` | string | valor fijo: `Microsoft_AIEI` |

### `microsoft_ai_diffusion_snapshot.csv`

| columna | tipo esperado | descripcion |
|---|---|---|
| `iso3` | string | ISO3 normalizado |
| `country_name_ms` | string | nombre original en Microsoft |
| `ai_user_share_h1_2025` | float | valor complementario H1 |
| `ai_adoption_rate` | float | valor canonico H2 2025 |
| `ai_user_share_change_pp` | float | variacion H2 - H1 |
| `year` | int | 2025 |
| `period` | string | `H2` |

## Metodologia De Extraccion Y Transformacion

### Flujo aplicado

1. Se inspecciono la pagina fuente y se confirmo que las tablas estaban embebidas en HTML, sin necesidad de renderizado JavaScript.
2. Se localizaron las 2 tablas relevantes y se consolidaron sus filas en una sola estructura tabular.
3. Se normalizaron los porcentajes eliminando `%` y el signo `+` del campo `Change`.
4. Se mapearon los nombres de pais a ISO3 mediante un diccionario explicito `MS_NAME_TO_ISO3` construido para maximizar cobertura global.
5. Se generaron 4 outputs con finalidades distintas: raw global, raw estudio, panel y snapshot.
6. Se realizo verificacion cruzada con la muestra de 86 paises del estudio.

### Decisiones de estandarizacion

| decision | implementacion |
|---|---|
| campo canonico del estudio | `ai_adoption_rate = ai_user_share_h2_2025` |
| periodo auxiliar | conservar H1 2025 como referencia comparativa |
| nombre del eje temporal en panel | `period` en vez de `semester`, para mantener consistencia con el CSV real |
| metadata temporal del raw | `report_edition = H1_2025+H2_2025` |
| mapeo territorial | se aceptan codigos ISO3 validos para paises y territorios presentes en la fuente |

## Cobertura Final

### Cobertura global

| metrica | valor |
|---|---|
| registros en Microsoft | 147 |
| registros extraidos | 147 |
| registros con ISO3 | 147 |
| registros sin ISO3 | 0 |
| porcentaje de normalizacion global | 100.0% |

### Cobertura en la muestra del estudio

| metrica | valor |
|---|---|
| paises de la muestra | 86 |
| paises con `ai_adoption_rate` | 75 |
| cobertura total | 87.2% |
| ACTIVOS cubiertos | 58 de 63 |
| SOLO Y cubiertos | 17 de 23 |
| faltantes de fuente | 11 |

### Paises de la muestra sin cobertura en Microsoft

Estos 11 paises no estan presentes en el dataset AIEI. La ausencia responde a cobertura de fuente, no a problemas de parsing o mapeo.

| iso3 | pais | estado_estudio |
|---|---|---|
| BHR | Bahrain | SOLO Y |
| BLZ | Belize | SOLO Y |
| BRB | Barbados | SOLO Y |
| CYP | Cyprus | ACTIVO |
| EST | Estonia | ACTIVO |
| ISL | Iceland | ACTIVO |
| LUX | Luxembourg | ACTIVO |
| LVA | Latvia | ACTIVO |
| MLT | Malta | SOLO Y |
| MUS | Mauritius | SOLO Y |
| SYC | Seychelles | SOLO Y |

## Controles De Calidad Aplicados

### Controles estructurales

| control | resultado |
|---|---|
| tablas HTML detectadas | 2 |
| filas consolidadas | 147 |
| columnas esperadas presentes | si |
| registros globales con ISO3 | 147/147 |
| registros de panel | 294 |
| registros de snapshot | 147 |

### Controles de valores

Valores contrastados contra el reporte publicado:

| iso3 | pais | esperado H2 2025 | obtenido H2 2025 | resultado |
|---|---|---|---|---|
| ARE | United Arab Emirates | 64.0 | 64.0 | ok |
| SGP | Singapore | 60.9 | 60.9 | ok |
| NOR | Norway | 46.4 | 46.4 | ok |
| IRL | Ireland | 44.6 | 44.6 | ok |
| FRA | France | 44.0 | 44.0 | ok |
| USA | United States | 28.3 | 28.3 | ok |

### Estadisticos globales H2 2025

| estadistico | valor |
|---|---|
| count | 147 |
| mean | 17.39 |
| std | 11.37 |
| min | 5.10 |
| p25 | 9.05 |
| median | 13.40 |
| p75 | 23.60 |
| max | 64.00 |

## Interpretacion Metodologica

### Fortalezas

- cobertura muy alta para la muestra del estudio;
- observacion muy reciente, enfocada en adopcion de GenAI durante 2025;
- disponibilidad de H1 y H2, lo que permite analizar cambio intraanual;
- normalizacion global completa a ISO3, util para cruces futuros fuera de la muestra base.

### Limitaciones vigentes

- solo hay 2 periodos, por lo que no existe una serie historica larga;
- la fuente no expone una metodologia de microdato replicable ni un API publica;
- parte de la cobertura puede reflejar sesgos de ecosistema/plataforma Microsoft;
- 11 paises de la muestra siguen ausentes porque Microsoft no los publica.

## Uso Recomendado En El Estudio

- usar `microsoft_ai_diffusion_snapshot.csv` como tabla canonica para modelos cross-section 2025;
- usar `microsoft_ai_adoption_panel.csv` solo para analisis exploratorio de sensibilidad entre H1 y H2;
- preservar `microsoft_ai_diffusion_raw.csv` como respaldo auditable de la extraccion original;
- documentar explicitamente que los 11 faltantes son faltantes de fuente y no faltantes de ETL.

## Estado Final De La Fuente

La fuente Microsoft AI Diffusion queda cerrada, documentada y utilizable para auditoria futura con los siguientes criterios cumplidos:
- extraccion completa del contenido tabular disponible;
- cobertura global 147/147 mapeada a ISO3;
- metadata alineada con los CSV finales;
- trazabilidad de transformaciones y controles de calidad documentada;
- cobertura de muestra y exclusiones de fuente explicitadas.

## Historial

| fecha | accion |
|---|---|
| 2026-04-08 | Extraccion inicial y cierre documental de la fuente Microsoft AIEI. 147 registros globales extraidos, 147/147 mapeados a ISO3, 75/86 paises del estudio cubiertos, 4 CSVs generados y documentacion de auditoria completada. |
