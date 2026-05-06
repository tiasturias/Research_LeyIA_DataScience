# Matriz Madre Fase 3

**Version actual:** `1.1` (base `1.0` + quality fix `country_name_canonical`, 2026-05-06)
**Tag git base:** `matriz-madre-v1.0`
**Tag git revision:** `matriz-madre-v1.1`

Implementacion autocontenida en `FASE3/`, generada desde fuentes reales y outputs EDA de Fase 2.

## Dimensiones

- Panel largo: 151,938 filas x 22 columnas.
- Snapshot largo: 53,596 filas x 26 columnas.
- Matriz wide: 199 entidades comparables x 1,203 columnas.
- Diccionario: 397 variables unicas x 20 columnas.
- Trazabilidad: 53,178 celdas wide no nulas trazadas a panel.
- Universo principal incluido: 199 entidades `country_iso3`.
- Excel human-readable: 13 hojas, 28.4 MB.

## Principios

- 0 datos sinteticos.
- 0 imputacion.
- `Matriz_EJEMPLO.xlsx` no fue usado como fuente de valores.
- Cada celda no nula de la wide apunta a una fila real del panel por `cell_id_panel`.
- Fase 4 debe consumir la matriz via `from src.fase3.api import load_wide`.
- Regiones, agregados globales, organizaciones, territorios no aprobados y entidades sin datos fueron excluidos de la matriz principal y conservados en outputs de auditoria.

## API publica para Fase 4

```python
from src.fase3.api import (
    load_wide,         # 199 paises x 1,203 columnas
    load_panel,        # 151,938 filas (verdad temporal)
    load_snapshot,     # 53,596 filas (post-regla temporal)
    load_dictionary,   # 397 variables x 20 columnas
    get_block,         # subset por bloque tematico
    get_chile_snapshot,
    list_versions,
)

wide = load_wide()                              # version=None acepta v1.x actual
regulatory = get_block("regulatory_treatment")  # 199 x 111 cols
chile = get_chile_snapshot()
```

## Cambios en v1.1 (2026-05-06)

Quality fix backwards-compatible. Sin cambio de schema, sin cambio de semantica de datos.

**Bug corregido:** El campo `country_name_canonical` venia con el ISO3 en lugar del nombre real para 86/199 paises (43%) de la matriz wide y proporcional en panel/snapshot/trazabilidad.

**Causa raiz:** El modulo `src/fase3_pipeline/geo.py` resolvia el nombre con `country_name_best_effort.split(' | ')[0]`, que para entradas como `"ARG | Argentina"` retornaba `"ARG"` en vez de `"Argentina"`.

**Solucion:**
1. Script de fix quirurgico (`scripts/fix_country_names.py`) actualizo todos los CSVs en O(n).
2. `scripts/regenerate_excel.py` regenero `Matriz_Madre_Fase3.xlsx` desde los CSVs corregidos.
3. `scripts/update_manifest.py` actualizo `manifest.json` con nuevos SHA-256.
4. Fix permanente del pipeline en `geo.py` (funcion `_resolve_name()` + 35 overrides manuales).

**Verificacion post-fix:**

| Output | Filas con `iso3 == country_name_canonical` |
|---|---:|
| `matriz_madre_wide.csv` | 0/199 |
| `fase3_universo_geografico.csv` | 5/259 (los 5 son agregados regionales AFE/AFW/IDB/LDC/EAR, EXCLUIDOS de la wide) |
| `matriz_larga_panel.csv` | 0/151,938 |
| `matriz_larga_snapshot.csv` | 0/53,596 |

Paises clave verificados: ARG=Argentina, AUS=Australia, FRA=France, COL=Colombia, BRA=Brazil, CAN=Canada, CHN=China, USA=United States, GBR=United Kingdom, CHL=Chile, SGP=Singapore, ARE=United Arab Emirates, IRL=Ireland.

## Tests al cierre

```text
pytest -q                          -> 20 passed in 8.77s
python -m src.fase3 validate       -> Fase 3 validation passed
```

## Archivos

| Archivo | Rol |
|---|---|
| `matriz_madre_wide.csv` | Matriz principal pais x atributo (Fase 4 input) |
| `matriz_larga_panel.csv` | Verdad larga panel (todos los anos) |
| `matriz_larga_snapshot.csv` | Post-regla temporal |
| `matriz_madre_trazabilidad.csv` | Mapa celda wide -> panel/fuente |
| `fase3_diccionario_variables.csv` | Diccionario metodologico |
| `fase3_universo_geografico.csv` | Universo geografico clasificado |
| `fase3_geo_crosswalk_manual.csv` | Crosswalk Microsoft + reglas geograficas |
| `fase3_reglas_temporales.csv` | Reglas temporales por fuente |
| `fase3_reporte_calidad_matriz.csv` / `.md` | Metricas y reporte humano |
| `Matriz_Madre_Fase3.xlsx` | Entrega Excel 13 hojas |
| `manifest.json` | Version, hashes SHA-256, changelog |

## Detalles tecnicos completos

Ver `FASE3_CIERRE_DOCUMENTACION_TECNICA.md` (seccion 12.1 para revision v1.1).
