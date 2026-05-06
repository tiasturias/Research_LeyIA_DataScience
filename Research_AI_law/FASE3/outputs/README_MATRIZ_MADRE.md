# Matriz Madre Fase 3

Implementacion autocontenida en `FASE3/`, generada desde fuentes reales y outputs EDA de Fase 2.

- Panel largo: 151,938 filas.
- Snapshot largo: 53,596 filas.
- Matriz wide: 199 entidades comparables x 1,203 columnas.
- Diccionario: 397 variables unicas.
- Trazabilidad: 53,178 celdas wide no nulas trazadas a panel.
- Universo principal incluido: 199 entidades `country_iso3`.

Principios:
- 0 datos sinteticos.
- 0 imputacion.
- `Matriz_EJEMPLO.xlsx` no fue usado como fuente de valores.
- Cada celda no nula de la wide apunta a una fila real del panel por `cell_id_panel`.
- Fase 4 debe consumir la matriz via `from src.fase3.api import load_wide`.
- Regiones, agregados globales, organizaciones, territorios no aprobados y entidades sin datos fueron excluidos de la matriz principal y conservados en outputs de auditoria.
