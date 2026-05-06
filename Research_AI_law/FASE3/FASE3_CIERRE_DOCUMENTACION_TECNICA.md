# Fase 3 - Cierre tecnico documentado de la Matriz Madre

Proyecto: Research_AI_law  
Fase: 3 - Preparacion de datos / Matriz Madre  
Directorio raiz de fase: `/home/pablo/Research_LeyIA_DataScience/Research_AI_law/FASE3`  
Version cerrada: `1.1`  
Tag git base: `matriz-madre-v1.0`  
Tag git revision: `matriz-madre-v1.1` (quality fix backwards-compatible)  
Proposito de este documento: servir como contexto inicial para futuros LLM, investigadores o agentes que deban entender que se hizo en Fase 3, que entregables existen, como se validaron y que limites metodologicos deben respetarse.

---

## 1. Resumen ejecutivo

La Fase 3 construyo una Matriz Madre profesional, auditable y reproducible para alimentar la Fase 4 del estudio Research_AI_law. El objetivo fue transformar ocho fuentes auditadas en Fase 2 en un sistema de datos pais x atributo, con trazabilidad celda-a-fuente y sin imputacion.

El resultado principal no es solo un CSV ancho. La Fase 3 entrega un sistema compuesto por:

- matriz larga panel como verdad historica de valores extraidos;
- matriz larga snapshot como version colapsada mediante reglas temporales;
- matriz wide pais x atributo para EDA principal;
- diccionario de variables;
- trazabilidad de celdas;
- universo geografico depurado;
- logs de decisiones metodologicas y revision humana;
- reporte de calidad;
- Excel human-readable;
- API estable para fases posteriores.

La matriz wide final quedo con 199 entidades comparables, 1,203 columnas y cero filas sin valores analiticos.

---

## 2. Principios que rigen esta fase

La Fase 3 debe entenderse bajo estos principios:

- Cero datos sinteticos.
- Cero imputacion en Fase 3.
- Ningun valor se extrae desde `Matriz_EJEMPLO.xlsx`.
- Ningun valor se extrae desde resumenes narrativos.
- Cada celda no nula de la matriz wide debe apuntar a una fila de panel.
- Cada fila de panel debe tener fuente, hoja, variable original y row identifier.
- La matriz wide es util para EDA, pero la verdad auditora es la matriz larga panel.
- Fase 3 no decide variable outcome, tratamiento causal ni modelo estadistico final.
- Fase 3 prepara datos para Fase 4-6; no responde por si sola la hipotesis principal.

---

## 3. Fuentes usadas

La Fase 3 usa solo las ocho fuentes validadas en Fase 2:

- `IAPP/iapp_dataset_unificado.xlsx`
- `MICROSOFT/Microsoft_AI_Reports_Data_unificado.xlsx`
- `Oxford Insights/data_index/UNIFICADO/Oxford_Insights_Unificado.xlsx`
- `World Bank WDI/WB_WDI_WGI_unificado.xlsx`
- `WIPO Global Innovation Index/data_wipo_gii/WIPO_GII_2021_2025_UNIFICADO.xlsx`
- `STANFORD AI INDEX 26/PUBLIC DATA_ 2026 AI INDEX REPORT/completo/stanford_ai_index_2026_unificado.csv`
- `OECD/OECD_Data_Central_unificado.xlsx`
- `ANTROPHIC/data_unificada/antrophic_economic_index.xlsx`

Los hashes SHA-256 de estas fuentes estan registrados en:

```text
outputs/manifest.json
outputs/fase3_fuentes_usadas.csv
```

No se agregaron fuentes externas nuevas.

---

## 4. Inputs de Fase 2 usados como mapa

La Fase 3 lee los 11 outputs de Fase 2 desde:

```text
../outputs/eda_preliminar/
```

Archivos:

- `inventario_fuentes.csv`
- `inventario_tablas.csv`
- `inventario_variables.csv`
- `cobertura_pais_fuente.csv`
- `cobertura_temporal_fuente.csv`
- `cobertura_pais_atributo.csv`
- `data_quality_issues.csv`
- `entidades_no_pais_o_sin_iso3.csv`
- `variables_candidatas_snapshot.csv`
- `recomendaciones_wrangling.csv`
- `resumen_eda_preliminar.md`

Estos archivos se usan como mapa metodologico y de auditoria. Los valores finales de la matriz se reextraen desde las fuentes originales.

---

## 5. Rescate profesional realizado

La implementacion inicial de Fase 3 estaba incompleta para cierre profesional. Se realizo un rescate tecnico que corrigio los bloqueantes principales.

### 5.1 Estado previo preservado

Antes de regenerar outputs, se archivo la version previa en:

```text
outputs/_archive/fase3_pre_rescate_20260506/
```

Tambien se creo una auditoria de linea base:

```text
outputs/auditoria_cierre/auditoria_inicial_pre_rescate.md
outputs/auditoria_cierre/baseline_outputs_pre_rescate.csv
```

La version archivada no debe usarse para Fase 4.

### 5.2 Universo geografico corregido

Problema corregido: la version previa aceptaba cualquier codigo alfabetico de tres letras como pais. Eso permitia agregados y entidades no comparables como `AFE`, `AFW`, `EAR`, `IDB`, `LDC`, `ANT`, entre otros.

Correccion:

- se implemento clasificacion geografica estricta;
- se separaron paises, territorios, regiones, globales, organizaciones y entidades obsoletas;
- se excluyeron agregados y entidades sin comparabilidad pais-pais;
- se eliminaron filas wide sin datos analiticos;
- se mantuvieron entidades excluidas en output auxiliar.

Output relevante:

```text
outputs/fase3_universo_geografico.csv
outputs/fase3_entidades_excluidas_geografia.csv
```

La wide final no contiene regiones, agregados globales, organizaciones ni entidades sin valores.

### 5.3 Crosswalk Microsoft reconstruido

Microsoft no traia ISO3 de forma directa. Se reconstruyo el crosswalk con columnas de auditoria:

- `source_id`
- `raw_entity_name`
- `raw_geo_code`
- `candidate_iso3`
- `final_iso3`
- `country_name_canonical`
- `entity_type_final`
- `match_method`
- `confidence_score`
- `action`
- `review_status`
- `reviewer`
- `review_date`
- `evidence`
- `notes`

Output:

```text
outputs/fase3_geo_crosswalk_manual.csv
config/fase3/geo_crosswalk.yaml
```

Resultado: 147 matches Microsoft quedaron con `approved_by_human` bajo politica documentada de exact-match.

### 5.4 Diccionario fortalecido

El diccionario paso a tener 20 columnas metodologicas:

- `variable_matriz`
- `source_id`
- `table_id`
- `original_variable`
- `tipo_original`
- `tipo_matriz`
- `unit`
- `direction`
- `bloque_tematico`
- `regla_temporal_default`
- `regla_transformacion`
- `is_primary`
- `redundant_with`
- `pct_complete`
- `n_countries_available`
- `fase4_role`
- `included_in_fase4_eda`
- `known_limitations`
- `human_review_status`
- `notes`

Correcciones importantes:

- WGI de World Bank usa unidad `wgi_-2.5_2.5`.
- Variables de tertiary enrollment se tratan como porcentaje cuando corresponde.
- WIPO ya no queda completamente asignado a infraestructura; se redistribuyo entre ecosystem, institutional, socioeconomic y tech infrastructure.
- Variables redundantes se marcaron con `is_primary` y `redundant_with`.
- Variables con baja cobertura quedan marcadas para cautela en Fase 4.

Output:

```text
outputs/fase3_diccionario_variables.csv
config/fase3/variable_dictionary.yaml
```

### 5.5 API publica creada

Fase 4 no debe leer CSV manualmente si puede evitarlo. Se creo una API estable:

```python
from src.fase3.api import (
    load_wide,
    load_panel,
    load_snapshot,
    load_dictionary,
    get_block,
    get_chile_snapshot,
    list_versions,
)
```

Archivo:

```text
src/fase3/api.py
```

Ejemplo:

```python
from src.fase3.api import load_wide, get_block, get_chile_snapshot

wide = load_wide()
regulatory = get_block("regulatory_treatment")
chile = get_chile_snapshot()
```

### 5.6 Configuracion auditable

Se crearon archivos de configuracion en:

```text
config/fase3/
```

Archivos:

- `geo_crosswalk.yaml`
- `temporal_rules.yaml`
- `variable_dictionary.yaml`
- `decisions.yaml`

Estos archivos documentan decisiones que antes estaban implicitas o hard-codeadas.

### 5.7 Reglas temporales

Las reglas temporales usadas son:

- IAPP: cross-section 2026-01.
- Microsoft: H2 2025 para difusion principal; H1 y cambio se conservan como variables separadas.
- Oxford: excluir 2019 por escala incompatible; usar ultimo anio disponible 2020+.
- World Bank: ultimo anio disponible por pais-variable.
- WIPO: 2025 si existe; fallback ultimo anio.
- Stanford: ultimo anio disponible por figura seleccionada.
- OECD: ultimo anio disponible por pais-variable.
- Anthropic: ventana mas reciente disponible.

Output:

```text
outputs/fase3_reglas_temporales.csv
config/fase3/temporal_rules.yaml
```

### 5.8 Notebook de revision humana

Se reemplazo el notebook minimo por una interfaz de revision:

```text
notebooks/02_matriz_madre.ipynb
```

Permite revisar:

- crosswalk Microsoft;
- territorios y entidades excluidas;
- variables de baja cobertura;
- redundancias;
- cobertura de Chile por bloque.

La logica reusable sigue en `src/`.

---

## 6. Outputs finales principales

Los outputs finales estan en:

```text
outputs/
```

Principales artefactos:

| Archivo | Rol |
|---|---|
| `matriz_larga_panel.csv` | Verdad larga panel. Todos los valores extraidos antes del snapshot. |
| `matriz_larga_snapshot.csv` | Version post-regla temporal. Base directa para wide. |
| `matriz_madre_wide.csv` | Matriz pais x atributo para Fase 4. |
| `matriz_madre_trazabilidad.csv` | Mapa de cada celda wide no nula hacia panel/fuente. |
| `fase3_diccionario_variables.csv` | Diccionario metodologico para interpretar variables. |
| `fase3_universo_geografico.csv` | Universo geografico completo con inclusiones y exclusiones. |
| `fase3_entidades_excluidas_geografia.csv` | Entidades excluidas y motivo. |
| `fase3_geo_crosswalk_manual.csv` | Crosswalk Microsoft y reglas geograficas auditables. |
| `fase3_reglas_temporales.csv` | Reglas temporales por fuente. |
| `fase3_decisiones_metodologicas.csv` | Decisiones metodologicas resumidas. |
| `fase3_human_review_log.csv` | Log de revision humana/documentada. |
| `fase3_reporte_calidad_matriz.csv` | Metricas de calidad machine-readable. |
| `fase3_reporte_calidad_matriz.md` | Reporte de calidad human-readable. |
| `fase3_auditoria_muestra_valores.csv` | Muestra de valores para auditoria manual. |
| `Matriz_Madre_Fase3.xlsx` | Entrega Excel human-readable con 13 hojas. |
| `manifest.json` | Version, hashes, inputs, fuentes, outputs y metadata. |
| `README_MATRIZ_MADRE.md` | README ejecutivo de outputs. |

---

## 7. Dimensiones finales

Dimensiones al cierre:

```text
matriz_madre_wide.csv:          199 filas x 1,203 columnas
matriz_larga_panel.csv:         151,938 filas x 22 columnas
matriz_larga_snapshot.csv:      53,596 filas x 26 columnas
fase3_diccionario_variables.csv: 397 variables x 20 columnas
matriz_madre_trazabilidad.csv:  53,178 filas x 14 columnas
```

La matriz wide no contiene filas con cero valores analiticos.

---

## 8. Bloques tematicos

Cada variable se asigna a exactamente un bloque:

- `regulatory_treatment`
- `ecosystem_outcome`
- `adoption_diffusion`
- `socioeconomic_control`
- `institutional_control`
- `tech_infrastructure_control`

Los bloques son taxonomia de auditoria y exploracion. No son todavia Y, X1 o X2 definitivos.

Distribucion aproximada de variables:

- `tech_infrastructure_control`: 167
- `ecosystem_outcome`: 124
- `regulatory_treatment`: 33
- `institutional_control`: 31
- `socioeconomic_control`: 28
- `adoption_diffusion`: 14

---

## 9. Chile

Chile queda presente y cubierto en todos los bloques relevantes:

- regulatory treatment;
- ecosystem outcome;
- adoption diffusion;
- socioeconomic control;
- institutional control;
- tech infrastructure control.

Hay una hoja dedicada en el Excel:

```text
Chile_Snapshot
Chile_vs_Peers
```

`Chile_vs_Peers` es una ayuda preliminar para Fase 4, no una muestra causal final.

---

## 10. Validaciones ejecutadas

Validaciones al cierre:

```bash
pytest -q
# 20 passed

python3 -m src.fase3 validate
# Fase 3 validation passed
```

La suite valida:

- existencia de outputs requeridos;
- Excel con 13 hojas;
- schemas pandera;
- unicidad de claves;
- correspondencia diccionario-wide;
- trazabilidad wide-panel;
- ausencia de agregados/no-paises en wide;
- Microsoft aprobado;
- Oxford 2019 excluido;
- WIPO rank excluido;
- Chile cubierto en bloques clave;
- API publica funcional;
- fuentes fisicas existentes;
- valores no vacios;
- manifest con hashes validos.

---

## 11. Comandos reproducibles

Desde la raiz `FASE3`:

```bash
python3 -m src.fase3 build-all
python3 -m src.fase3 validate
pytest -q
```

Para cargar datos en Fase 4:

```python
from src.fase3.api import load_wide, load_dictionary, get_block, get_chile_snapshot

wide = load_wide()
dictionary = load_dictionary()
regulatory = get_block("regulatory_treatment")
chile = get_chile_snapshot()
```

---

## 12. Versionado

Commits relevantes:

```text
7520548 feat(fase3): rescue and close matriz madre v1
7086c06 chore(fase3): record rescue manifest git sha
(pendiente) fix(fase3): country_name_canonical resolution bug v1.1
```

Tags:

```text
matriz-madre-v1.0   (base)
matriz-madre-v1.1   (quality fix: country names)
```

Nota: el manifest excluye su propio hash por politica anti-recursion.

### 12.1 Revision v1.1 - country_name_canonical fix

**Fecha:** 2026-05-06
**Tipo:** Quality fix backwards-compatible (no schema change, no data semantics change).
**Origen del bug:** El modulo `src/fase3_pipeline/geo.py` resolvia el nombre canonico haciendo `country_name_best_effort.split(' | ')[0]`. Como el campo de Fase 2 venia con formato `"ARG | Argentina"`, el split tomaba el ISO3 como nombre.

**Impacto medido:**

| Output | Filas afectadas |
|---|---|
| `matriz_madre_wide.csv` | 86/199 paises (43%) |
| `fase3_universo_geografico.csv` | 99/259 entidades |
| `matriz_larga_panel.csv` | 10,103 filas (6.6%) sobre 202 ISO3 unicos |
| `matriz_larga_snapshot.csv` | 2,003 filas (3.7%) |
| `matriz_madre_trazabilidad.csv` | proporcional |
| `Matriz_Madre_Fase3.xlsx` | propagado a todas las hojas |

Ejemplos: `ARG -> ARG` (deberia ser `Argentina`), `AUS -> AUS` (`Australia`), `FRA -> FRA` (`France`), `COL -> COL` (`Colombia`), `USA -> USA` (`United States`), `CHN -> CHN` (`China`).

**Solucion aplicada:**

Script de fix quirurgico en:

```text
scripts/fix_country_names.py
scripts/regenerate_excel.py
scripts/update_manifest.py
```

Logica:
1. Construir mapping ISO3 -> nombre canonico extrayendo el componente NO-ISO3 de `country_name_best_effort` (split por `|`, descartar el componente igual al ISO3).
2. Aplicar 35 overrides manuales para casos donde el nombre best_effort tenia abreviaciones o queriamos un label oficial (ej: `USA -> United States` en vez de `United States of America`, `KOR -> South Korea`, `XKX -> Kosovo`, etc.).
3. Patchear todos los CSVs en O(n) vectorizado.
4. Regenerar Excel desde los CSVs corregidos (no patch in-place — preserva integridad zip).
5. Actualizar manifest con nuevos SHA-256 + bytes + entrada en `changelog`.

**API pública:**

`src/fase3/api.py` ahora acepta `version=None` (cualquier 1.x compatible) o exact match. Esto permite que Fase 4 use `load_wide()` sin pasar version explicita y siga funcionando ante futuras revisiones backwards-compatible.

**Tests:**

Suite continua pasando 20/20. Tests modificados:
- `test_manifest.py::test_manifest_version_and_configs` ahora acepta cualquier version `1.x` (antes hardcodeaba `"1.0"`).
- `test_api_contract.py::test_public_api_loaders_work` ahora valida que exista alguna version `1.x` (antes hardcodeaba `"1.0"`).

**Verificacion post-fix:**

```text
matriz_madre_wide.csv:                0/199 paises sin resolver
fase3_universo_geografico.csv:        5/259 sin resolver (los 5 son agregados regionales AFE, AFW, IDB, LDC, EAR que estan EXCLUIDOS de la wide por entity_type != country_iso3)
Matriz_Madre_Fase3.xlsx:              13 hojas, todos los paises clave verificados
pytest -q:                            20 passed
python -m src.fase3 validate:         Fase 3 validation passed
```

Paises clave verificados manualmente en Excel y CSVs: ARG, AUS, FRA, COL, BRA, CAN, CHN, USA, GBR, CHL, SGP, ARE, IRL — todos con nombre humano correcto.

**Reglas para LLMs futuros:**

- Si se vuelve a regenerar Fase 3 desde scratch corriendo `python -m src.fase3 build-all`, el bug volvera a aparecer porque `geo.py` no fue modificado (el fix se aplico via script post-procesado).
- Para hacer el fix permanente al pipeline, hay que modificar `_world_bank_geo_metadata` o las llamadas a `split(' | ')[0]` en `geo.py` para usar el componente NO-ISO3.
- El script `scripts/fix_country_names.py` puede re-aplicarse idempotentemente: solo modifica filas donde `iso3 == country_name_canonical`.

---

## 13. Limites conocidos

La Fase 3 esta lista para Fase 4, pero no contiene todo lo necesario para preguntas futuras mas finas.

No contiene directamente:

- permisos de construccion de datacenters;
- impuesto corporativo completo;
- corpus legal medioambiental completo;
- cumplimiento real de leyes;
- separacion subnacional de EEUU por estado;
- analisis causal final.

Estas tareas pertenecen a Fase 4-6 o a una futura extension de datos, por ejemplo `Fase 3B` o `Fase 5`.

---

## 14. Reglas para futuros LLM o agentes

Si un futuro LLM trabaja con esta fase, debe respetar:

1. No modificar `outputs/_archive/`.
2. No usar `Matriz_EJEMPLO.xlsx` como fuente de datos.
3. No imputar en Fase 3.
4. No mezclar paises con regiones, globales u organizaciones.
5. No decidir Y/X1/X2 dentro de Fase 3.
6. Usar `src.fase3.api` para Fase 4.
7. Consultar `fase3_diccionario_variables.csv` antes de interpretar cualquier columna.
8. Consultar `matriz_madre_trazabilidad.csv` antes de defender cualquier celda.
9. Usar `matriz_larga_panel.csv` si se desea cambiar una regla temporal.
10. Reejecutar tests y validacion despues de cualquier cambio.

---

## 15. Conclusión

La Fase 3 queda cerrada como una base profesional, trazable y suficientemente robusta para iniciar Fase 4. La matriz no responde aun la hipotesis principal, pero entrega una base limpia y defendible para realizar EDA principal, feature engineering y modelado posterior.

