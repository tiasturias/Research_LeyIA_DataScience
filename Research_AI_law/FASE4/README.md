# FASE4 - EDA Principal

Proyecto: Research_AI_law  
Version objetivo: 1.0  
Fuente unica de datos: API publica de Fase 3 (`fase3.api` / `src.fase3.api`)

## Proposito

Fase 4 convierte la Matriz Madre de Fase 3 en una cartografia estadistica
reproducible para preparar Feature Engineering y modelado. No imputa datos,
no decide variables Y/X, no selecciona una muestra final unica y no interpreta
correlaciones como causalidad.

## Comandos reproducibles

Desde este directorio:

```bash
python3 -m src.fase4 build-all
python3 -m src.fase4 validate
pytest tests/fase4 -v
```

Notebook auditable:

```bash
jupyter lab notebooks/03_eda_principal.ipynb
```

## Outputs principales

Los artefactos finales viven en:

```text
outputs/eda_principal/
```

Incluyen CSVs de cobertura, estadistica univariada, correlaciones, redundancia,
perfiles pais, Chile, deep dives, taxonomias exploratorias, sensibilidad
temporal, submuestras candidatas, mapeo Q1-Q4, gaps, recomendaciones para
Fase 5, reporte HTML y manifest con hashes.

## API para Fase 5

```python
from fase4.api import (
    load_candidates,
    load_submuestras,
    load_question_mapping,
    load_taxonomy,
    load_chile_profile,
)

candidates = load_candidates()
submuestras = load_submuestras()
q1 = load_question_mapping("Q1_investment")
binding = load_taxonomy("binding")
chile = load_chile_profile()
```

## Estado metodologico

- Fase 3 no se modifica.
- Los datos faltantes se documentan como gaps, no se imputan.
- Outliers como USA, SGP, ARE, IRL y EST se preservan.
- Las seis submuestras son candidatas para multiverse analysis.
- `eda_decisions_for_fase5.yaml` requiere revision/firma humana antes de Fase 5.
