import pandas as pd
from pathlib import Path
import re

BASE = Path("/home/pablo/Research_LeyIA_DataScience/Research_AI_law/FUENTES/TECHIERAY")
df = pd.read_csv(BASE / "tr_regulatory_metadata.csv").fillna("None")

for _, row in df.iterrows():
    iso = row['iso3']
    md_file = list(BASE.glob(f"{iso}-*.md"))
    if not md_file: continue
    md_file = md_file[0]
    
    content = md_file.read_text(encoding="utf-8")
    raw_match = re.split(r'## Checklist', content)
    raw_text = raw_match[0]
    
    new_checklist = f"""## Checklist

### Nivel 1 — Todos los países (6 variables)

- [x] `tr_ley_ia_vigente:` {row['tr_ley_ia_vigente']}
- [x] `tr_proyecto_ley_ia:` {row['tr_proyecto_ley_ia']}
- [x] `tr_estrategia_nacional_ia:` {row['tr_estrategia_nacional_ia']}
- [x] `tr_tiene_guia_softlaw:` {row['tr_tiene_guia_softlaw']}
- [x] `tr_tiene_autoridad_dedicada:` {row['tr_tiene_autoridad_dedicada']}
- [x] `tr_categoria_obligatoriedad:` {row['tr_categoria_obligatoriedad']}

### Nivel 2 — Si el RAW tiene suficiente info (7 variables)

- [x] `tr_n_leyes_relacionadas:` {row['tr_n_leyes_relacionadas']}
- [x] `tr_n_autoridades:` {row['tr_n_autoridades']}
- [x] `tr_sandbox_regulatorio:` {row['tr_sandbox_regulatorio']}
- [x] `tr_marcos_voluntarios:` {row['tr_marcos_voluntarios']}
- [x] `tr_instituto_seguridad_ia:` {row['tr_instituto_seguridad_ia']}
- [x] `tr_herramientas_testing:` {row['tr_herramientas_testing']}
- [x] `tr_modelo_gobernanza:` {row['tr_modelo_gobernanza']}

### Nivel 3 — Validación (si aplica)

- [x] `tr_adhiere_oecd:` {row['tr_adhiere_oecd']}
- [x] `tr_adopto_unesco:` {row['tr_adopto_unesco']}

---
> IAPP crosscheck: `iapp_ley_ia_vigente=` / `iapp_proyecto_ley_ia=`
"""
    md_file.write_text(raw_text + new_checklist, encoding="utf-8")

print("✅ Todos los archivos Markdown han sido actualizados con los checklists auditados.")
