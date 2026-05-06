# README EDA Principal - Fase 4

Proyecto: Research_AI_law
Fase: 4 - EDA Principal
Version: 1.0
Fecha de generación: 2026-05-06T12:39:47.519739+00:00

## Propósito

Esta fase transforma la Matriz Madre de Fase 3 en una cartografía estadística
para preparar Feature Engineering y modelado. No responde causalmente la
pregunta del estudio, no imputa datos, no decide Y/X y no selecciona una
muestra final única.

## Entregables principales

- `EDA_Principal_Fase4.html`: reporte autocontenido con narrativa ejecutiva.
- `manifest_eda_principal.json`: hashes de inputs Fase 3 y outputs Fase 4.
- `eda_candidates_for_feature_engineering.csv`: 380 variables clasificadas para Fase 5.
- `eda_submuestras_candidatas.csv`: 6 submuestras para multiverse analysis.
- `eda_data_gaps.csv`: 6 gaps formales para Fase 3B/Fase 5.
- `eda_question_q*.csv`: mapeo de las cuatro sub-preguntas a variables reales observadas.

## Reglas metodológicas preservadas

- Fase 4 consume Fase 3 mediante API pública (`fase3.api` / `src.fase3.api`).
- Fase 4 no modifica archivos de Fase 3.
- Estadística robusta primero: mediana, IQR, MAD, Spearman.
- FDR/Holm se reportan como diagnóstico de multiplicidad.
- Outliers como USA, SGP, ARE, IRL y EST se preservan y documentan.
- El cuello de botella IAPP/regulatorio se reporta explícitamente.

## Uso desde Fase 5

```python
from fase4.api import load_candidates, load_submuestras, load_chile_profile

candidates = load_candidates()
submuestras = load_submuestras()
chile = load_chile_profile()
```

## Comandos de reproducción

```bash
python3 -m src.fase4 build-all
python3 -m src.fase4 validate
pytest tests/fase4 -v
```
