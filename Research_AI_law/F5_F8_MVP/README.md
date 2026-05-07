# F5_F8_MVP

MVP end-to-end para las Fases 5 a 8 del proyecto `Research_AI_law`.

Este directorio se construye sobre:

- `FASE3/`: Matriz Madre v1.1.
- `FASE4/`: EDA Principal v1.0 revisado metodologicamente.

## Estado actual

Solo `FASE5/` debe considerarse activa en este momento. FASE6-FASE8 se
implementaran despues de cerrar Fase 5.

## Regla de oro

El MVP solo lee Fase 3 y Fase 4. No modifica sus outputs.

## Fase 5

```bash
cd /home/pablo/Research_LeyIA_DataScience/Research_AI_law/F5_F8_MVP
python3 -m FASE5.src.build
pytest FASE5/tests -v
python3 -m FASE5.src.validate
```

Flujo completo:

```bash
make fase5-all
```

Artefactos principales:

- `FASE5/outputs/feature_matrix_mvp.csv`
- `FASE5/outputs/MVP_AUDITABLE.xlsx` con guia, matriz 43 x 46, matriz tecnica 43 x 138 y diccionario de columnas
- `FASE5/outputs/phase6_ready/` con el bundle tecnico para modelado en Fase 6
- `FASE5/outputs/fase5_manifest.json`
- `FASE5/notebooks/05_data_preparation.ipynb`
