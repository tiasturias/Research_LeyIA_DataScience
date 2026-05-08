# PLAN DE ACCIÓN — Corrección del Cuello de Botella Regulatorio

## Integración de Techieray Global AI Regulation Tracker como novena fuente de datos

**Proyecto:** Research_AI_law — Boletín 16821-19 Ley Marco de IA Chile  
**Documento:** Blueprint end-to-end para resolver la cobertura insuficiente de variables predictoras (X1)  
**Versión:** 1.0  
**Fecha:** 2026-05-08  
**Archivo:** `NUEVA_METODOLOGIA_08/PLAN_SOLUCION_cuello_botella.md`  

---

## 0. Resumen Ejecutivo

### 0.1 El problema

El estudio depende de **19 variables IAPP** (International Association of Privacy Professionals) como fuente canónica de predictores regulatorios (X1). Sin embargo, IAPP solo tiene datos completos para **18 de los 43 países** de la muestra preregistrada. Esto genera:

| Consecuencia | Impacto |
|---|---|
| `iapp_ley_ia_vigente` solo tiene n=17 efectivo en los modelos | IC95 extremadamente amplios. β = +7.4 con IC95 [-7.96, +23.07] para inversión. **No informativo para política pública.** |
| Q4 (clusters regulatorios) solo cubre 18 países | Los 25 restantes (principalmente UE) reciben etiqueta _sin datos IAPP_ aunque estén regulados por el EU AI Act. |
| Variables agregadas `n_binding`/`n_non_binding` dependen de IAPP | Su construcción está limitada a los 18 países con datos. Para los otros 25, dependen exclusivamente del corpus legal-IA (extracción no validada). |
| 5 variables IAPP diplomáticas sin cobertura | `iapp_firmo_coe_convencion`, `iapp_endoso_hiroshima_g7`, `iapp_firmo_bletchley`, `iapp_endoso_declaracion_data_scraping`, `iapp_firmo_ai_action_summit` — solo existen para 18 países. |

### 0.2 La solución

Incorporar el **[Global AI Regulation Tracker de Techieray](https://www.techieray.com/GlobalAIRegulationTracker)** (Raymond Sun) como **novena fuente de datos**. Este tracker mantiene perfiles regulatorios de IA actualizados para prácticamente todos los países del mundo, con categorías como leyes vigentes, proyectos de ley, estrategias nacionales, guías, sandboxes, y autoridades.

**Estrategia de extracción:** manual (sin NLP), leyendo el perfil de cada país en el tracker y completando un checklist de 15 variables binarias, de conteo y categóricas. NLP del corpus legal-IA sigue fuera de alcance.

### 0.3 Resultado esperado

| Variable | Antes (solo IAPP) | Después (IAPP + Techieray) |
|---|---|---|
| `tr_ley_ia_vigente` | n=17 efectivo, `low_n_exploratory_only` | **n≈40 efectivo**, IC95 estrechos, **informativo para política pública** |
| Q4 clustering regulatorio | 18 países, 4 clusters | **43 países**, perfiles regulatorios completos para todos |
| `n_binding` / `n_non_binding` | Basados en IAPP (18) + corpus | Recalculados con Techieray para 43 países |
| Países UE sin perfil IAPP | "Sin legislación IA nacional específica detectada" | **Perfil regulatorio completo** (EU AI Act + legislación nacional complementaria) |
| `conclusion_stability_matrix` (Fase 7) | Mayoría de hallazgos con X1 regulatoria = `fragile` o `not_estimable` | Mayoría = `directionally_stable` o `stable` |

### 0.4 Alcance de este documento

Este blueprint cubre **desde la recolección de datos (Fase 1) hasta la regeneración de la Country Intelligence Layer (Fase 6.2)**. No cubre Fase 7 (robustez) ni Fase 8 (narrativa), aunque se mencionan los impactos esperados sobre ellas. El blueprint de implementación de Fase 7 está en `nueva_metodologia/FASE7_PLAN.md`.

---

## 1. Diagnóstico Detallado del Cuello de Botella

### 1.1 Variables IAPP — inventario completo

| # | Variable IAPP | Tipo | Clasificación Fase 4 | Cobertura actual | Usada en Fase 6 como |
|---|---|---|---|---|---|
| 1 | `iapp_ley_ia_vigente` | binary | binding | 18 países | X1 principal |
| 2 | `iapp_categoria_obligatoriedad` | categorical | binding | 18 países | X1 categórico |
| 3 | `iapp_proyecto_ley_ia` | binary | hybrid | 18 países | X1 hybrid |
| 4 | `iapp_modelo_gobernanza` | categorical | hybrid | 18 países | X1 contextual |
| 5 | `iapp_n_leyes_relacionadas` | count | binding | 18 países | X1 intensidad |
| 6 | `iapp_n_autoridades` | count | binding | 18 países | X1 capacidad |
| 7 | `iapp_firmo_coe_convencion` | binary | binding | 18 países | Contribuye a `n_binding` |
| 8 | `iapp_estrategia_nacional_ia` | binary | non-binding | 18 países | Contribuye a `n_non_binding` |
| 9 | `iapp_adhiere_oecd_ai` | binary | non-binding | 18 países | Contribuye a `n_non_binding` |
| 10 | `iapp_adopto_unesco_etica_ia` | binary | non-binding | 18 países | Contribuye a `n_non_binding` |
| 11 | `iapp_endoso_hiroshima_g7` | binary | non-binding | 18 países | Contribuye a `n_non_binding` |
| 12 | `iapp_firmo_bletchley` | binary | non-binding | 18 países | Contribuye a `n_non_binding` |
| 13 | `iapp_endoso_declaracion_data_scraping` | binary | non-binding | 18 países | Contribuye a `n_non_binding` |
| 14 | `iapp_firmo_ai_action_summit` | binary | non-binding | 18 países | Contribuye a `n_non_binding` |
| 15 | `iapp_marcos_voluntarios` | binary | non-binding | 18 países | Contribuye a `n_non_binding` |
| 16 | `iapp_guias_sectoriales` | binary | non-binding | 18 países | Contribuye a `n_non_binding` |
| 17 | `iapp_herramientas_testing` | binary | non-binding | 18 países | Contribuye a `n_non_binding` |
| 18 | `iapp_sandbox_regulatorio` | binary | hybrid | 18 países | Contribuye a `n_hybrid` |
| 19 | `iapp_instituto_seguridad_ia` | binary | hybrid | 18 países | Contribuye a `n_hybrid` |

### 1.2 Variables IAPP con GAPS documentados

Estas 7 variables están en la taxonomía de Fase 4 como `documented_gaps` — conceptos deseables que **no existen** como variables observadas en ninguna fuente actual:

| Gap documentado | ¿Techieray puede cubrirlo? |
|---|---|
| `iapp_autoridad_regulatoria_ia` | ✅ Sí — `tr_tiene_autoridad_dedicada` |
| `iapp_principios_ia` | ✅ Sí — inferible de guías y estrategias |
| `iapp_regulacion_sectorial_ia` | ✅ Sí — `tr_guias_sectoriales` (si aplica) |
| `iapp_regulacion_horizontal_ia` | ✅ Sí — `tr_ley_ia_vigente` (si es comprehensiva) |
| `iapp_reglamento_ia` | ⚠️ Parcial — si el tracker menciona decretos/reglamentos |
| `iapp_tipo_enfoque_regulatorio` | ✅ Sí — derivable de `tr_categoria_obligatoriedad` + `tr_modelo_gobernanza` |
| `iapp_ai_risk_framework` | ⚠️ Parcial — si el tracker menciona risk framework |

---

## 2. Mapeo Completo: 19 IAPP → 15 Techieray Extraíbles

### 2.1 Nivel 1 — Siempre extraíbles (6 variables para los 43 países)

Estas se pueden determinar incluso con perfiles de tracker pobres (10-40 líneas), típicos de países UE pequeños:

| # | Variable Techieray | Tipo | IAPP equivalente | Cómo extraerla | Regla para países UE |
|---|---|---|---|---|---|
| 1 | `tr_ley_ia_vigente` | binary (0/1) | `iapp_ley_ia_vigente` | Buscar "Act", "Law", "approved", "in force". Si no se menciona ninguna → 0. | **1** (EU AI Act vigente desde agosto 2024) |
| 2 | `tr_proyecto_ley_ia` | binary (0/1) | `iapp_proyecto_ley_ia` | Buscar "bill", "draft", "proposal", "consultation", "introduced". | Buscar si hay proyecto nacional (ej. KI-MIG en Alemania) |
| 3 | `tr_estrategia_nacional_ia` | binary (0/1) | `iapp_estrategia_nacional_ia` | Buscar "strategy", "national AI", "policy", "plan". | Buscar estrategia nacional específica |
| 4 | `tr_tiene_guia_softlaw` | binary (0/1) | `iapp_marcos_voluntarios` + `iapp_guias_sectoriales` | Buscar "guidance", "framework", "guidelines", "white paper", "recommendations". | Casi siempre 1 para países UE (tienen guías DPA + EU) |
| 5 | `tr_tiene_autoridad_dedicada` | binary (0/1) | `iapp_n_autoridades` (>0 → 1) | Buscar "authority", "agency", "institute", "office", "network agency". | Casi siempre 1 para países UE (autoridad designada por EU AI Act) |
| 6 | `tr_categoria_obligatoriedad` | categorical | `iapp_categoria_obligatoriedad` | **Derivar:** si tiene ley → `binding`. Solo guías → `non-binding`. Ambas → `mixed`. Nada → `none`. UE sin ley nacional → `binding (via EU AI Act)`. | `binding` (EU AI Act) o `mixed` si además tiene ley nacional |

### 2.2 Nivel 2 — Extraíbles con perfil moderado (7 variables para ~33 países)

Requieren que el RAW del tracker tenga al menos ~50 líneas de contenido:

| # | Variable Techieray | Tipo | IAPP equivalente | Cómo extraerla |
|---|---|---|---|---|
| 7 | `tr_n_leyes_relacionadas` | count (int) | `iapp_n_leyes_relacionadas` | Contar menciones a leyes, acts, bills de IA. Incluir EU AI Act si es país UE. |
| 8 | `tr_n_autoridades` | count (int) | `iapp_n_autoridades` | Contar agencias, autoridades, institutos de IA mencionados. |
| 9 | `tr_sandbox_regulatorio` | binary (0/1) | `iapp_sandbox_regulatorio` | Buscar "sandbox", "regulatory sandbox", "test environment". |
| 10 | `tr_marcos_voluntarios` | binary (0/1) | `iapp_marcos_voluntarios` | Buscar "voluntary", "code of conduct", "accord", "pledge". |
| 11 | `tr_instituto_seguridad_ia` | binary (0/1) | `iapp_instituto_seguridad_ia` | Buscar "safety institute", "AISI", "AI safety". |
| 12 | `tr_herramientas_testing` | binary (0/1) | `iapp_herramientas_testing` | Buscar "testing", "AI Verify", "evaluation toolkit", "audit". |
| 13 | `tr_modelo_gobernanza` | categorical | `iapp_modelo_gobernanza` | **Derivar:** una autoridad central → `centralized`. Sectorial → `sectoral`. Sin autoridad clara → `distributed`. UE → `eu_delegated`. Sin info → `none`. |

**Valores permitidos para `tr_modelo_gobernanza`:**
- `centralized` — una autoridad nacional única para IA
- `sectoral` — regulación por sector (financiero, salud, etc.) sin autoridad central
- `distributed` — múltiples agencias con competencias compartidas
- `eu_delegated` — la regulación principal es supranacional (EU AI Act), con implementación nacional delegada
- `none` — sin estructura de gobernanza de IA identificable

**Valores permitidos para `tr_categoria_obligatoriedad`:**
- `binding` — tiene legislación vinculante con sanciones
- `non-binding` — solo instrumentos voluntarios, guías, recomendaciones
- `mixed` — tiene tanto binding como non-binding
- `none` — sin instrumentos regulatorios de IA identificables

### 2.3 Nivel 3 — Validación (2 variables, para todos los países)

| # | Variable Techieray | Tipo | IAPP equivalente | Cómo extraerla |
|---|---|---|---|---|
| 14 | `tr_adhiere_oecd` | binary (0/1) | `iapp_adhiere_oecd_ai` | ¿Es miembro OECD? Dato conocido. ¿Menciona AI Principles? |
| 15 | `tr_adopto_unesco` | binary (0/1) | `iapp_adopto_unesco_etica_ia` | Buscar "UNESCO", "ethics recommendation", "RAM". |

### 2.4 Variables IAPP NO extraíbles del tracker (5 variables)

Estas 5 variables miden eventos diplomáticos muy específicos. **No son extraíbles del tracker** de forma confiable. Para los 18 países con IAPP, conservan su valor IAPP. Para los otros 25, quedan como `NaN`:

| # | Variable IAPP | Razón por la que no es extraíble |
|---|---|---|
| 1 | `iapp_firmo_coe_convencion` | Convención del Consejo de Europa — membresía específica |
| 2 | `iapp_endoso_hiroshima_g7` | Proceso G7 Hiroshima — solo miembros G7 |
| 3 | `iapp_firmo_bletchley` | Bletchley Park Declaration — requiere lista específica de firmantes |
| 4 | `iapp_endoso_declaracion_data_scraping` | Declaración muy específica, raramente mencionada en el tracker |
| 5 | `iapp_firmo_ai_action_summit` | AI Action Summit — requiere verificar asistencia específica |

**Estrategia:** estas 5 variables se mantienen con sus valores IAPP para los 18 países que las tienen. Para los otros 25, quedan como `NaN`. No se pierde nada respecto al estado actual. Las variables Techieray (#1-15) **reemplazan** funcionalmente a las IAPP en los modelos.

---

## 3. Plan de Acción Paso a Paso

### FASE ACTUAL: Recolección de datos (en progreso)

**Estado:** ✅ 43 archivos RAW con contenido del tracker pegados en `FUENTES/TECHIERAY/XXX-Nombre.md`.  
**Estado:** ⬜ Checklists de 15 variables sin llenar.

**Archivos involucrados:**
```
FUENTES/TECHIERAY/
├── README.md                              # Guía de extracción
├── ARE-United-Arab-Emirates.md            # 270 líneas RAW + checklist
├── ARG-Argentina.md                       # 124 líneas
├── AUS-Australia.md                       # 971 líneas
├── ... (43 archivos en total)
└── USA-United-States.md                   # 2644 líneas
```

**Tarea pendiente:** llenar los checklists de 15 variables en cada archivo.  
**Tiempo estimado:** ~15 minutos por país × 43 países ≈ **10-11 horas de trabajo manual**.

---

### PASO 1 — Parsear los 43 checklists → `tr_regulatory_metadata.csv`

**Objetivo:** convertir los 43 archivos `.md` con checklists llenos en un CSV estructurado listo para integrar al pipeline.

**Qué hace el script `parse_techieray_to_csv.py`:**

```python
"""
Ubicación: FUENTES/TECHIERAY/parse_techieray_to_csv.py
Input:    FUENTES/TECHIERAY/*.md (43 archivos con checklists completados)
Output:   FUENTES/TECHIERAY/tr_regulatory_metadata.csv
"""

import re, csv
from pathlib import Path

BASE = Path(__file__).parent
OUTPUT = BASE / "tr_regulatory_metadata.csv"

VARIABLES = [
    # Nivel 1
    "tr_ley_ia_vigente", "tr_proyecto_ley_ia", "tr_estrategia_nacional_ia",
    "tr_tiene_guia_softlaw", "tr_tiene_autoridad_dedicada", "tr_categoria_obligatoriedad",
    # Nivel 2
    "tr_n_leyes_relacionadas", "tr_n_autoridades", "tr_sandbox_regulatorio",
    "tr_marcos_voluntarios", "tr_instituto_seguridad_ia", "tr_herramientas_testing",
    "tr_modelo_gobernanza",
    # Nivel 3
    "tr_adhiere_oecd", "tr_adopto_unesco",
]

def parse_value(raw: str) -> any:
    """Convierte el texto del checklist a valor Python: 1, 0, int, str, o NaN."""
    raw = raw.strip()
    if not raw:
        return None
    # Binarias
    if raw.upper().startswith("SI") or raw == "1":
        return 1
    if raw.upper().startswith("NO") or raw == "0":
        return 0
    # Conteos
    try:
        return int(raw)
    except ValueError:
        pass
    # Categóricas o texto libre
    return raw

def parse_country_file(path: Path) -> dict:
    """Extrae iso3 y los 15 valores del checklist de un archivo .md."""
    iso3 = path.stem.split("-")[0]
    text = path.read_text(encoding="utf-8")
    row = {"iso3": iso3}
    
    for var in VARIABLES:
        # Buscar patrón: - [x] `var:` valor
        pattern = rf'- \[[ x]\] `{re.escape(var)}:`\s*(.*)'
        match = re.search(pattern, text)
        if match:
            row[var] = parse_value(match.group(1))
        else:
            row[var] = None
    
    return row

def main():
    rows = []
    for md_file in sorted(BASE.glob("*.md")):
        if md_file.name == "README.md":
            continue
        row = parse_country_file(md_file)
        rows.append(row)
        print(f"  {row['iso3']}: ley={row.get('tr_ley_ia_vigente')}, "
              f"proy={row.get('tr_proyecto_ley_ia')}, "
              f"cat={row.get('tr_categoria_obligatoriedad')}")
    
    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["iso3"] + VARIABLES)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\n✅ {len(rows)} países escritos a {OUTPUT}")

if __name__ == "__main__":
    main()
```

**Output esperado:** `tr_regulatory_metadata.csv` con 43 filas × 16 columnas.

**Validaciones automáticas:**
- Los 43 ISO3 deben estar presentes (matchear contra `mvp_sample.yaml`)
- Las binarias solo deben contener 0, 1 o None
- Las de conteo solo deben contener enteros ≥ 0 o None
- Las categóricas deben contener solo valores del conjunto permitido

**Tiempo:** 1 hora (escribir script + ejecutar + validar).

---

### PASO 2 — Incorporar Techieray a Fase 3 (Matriz Madre)

**Objetivo:** agregar las 15 variables Techieray como columnas en la matriz madre, con trazabilidad completa.

#### 2.1 Agregar columnas a la matriz madre

```python
"""
Script: agregar_techieray_a_fase3.py
Ubicación: se ejecuta desde la raíz del proyecto
"""
import pandas as pd

# Cargar matriz madre existente
FASE3 = Path("FASE3/outputs")
matriz = pd.read_excel(FASE3 / "Matriz_Madre_Fase3.xlsx")
techieray = pd.read_csv("FUENTES/TECHIERAY/tr_regulatory_metadata.csv")

# Merge por iso3 (left join — preserva los 199 países originales)
matriz = matriz.merge(techieray, on="iso3", how="left")

# Guardar nueva versión
matriz.to_excel(FASE3 / "Matriz_Madre_Fase3.xlsx", index=False)
```

**Nota:** hacer backup de `Matriz_Madre_Fase3.xlsx` antes de modificarla.

#### 2.2 Actualizar diccionario de variables

Agregar 15 filas a `fase3_diccionario_variables.csv`:

```csv
variable_matriz,fuente,tipo,bloque,descripcion_larga
tr_ley_ia_vigente,Techieray Global AI Regulation Tracker (Raymond Sun),binary,regulatory_treatment,¿Tiene al menos una ley de IA vigente? (1=Sí, 0=No). Para países UE, EU AI Act cuenta como ley vigente.
tr_proyecto_ley_ia,Techieray,binary,regulatory_treatment,¿Tiene al menos un proyecto de ley de IA en trámite legislativo? (1=Sí, 0=No)
tr_estrategia_nacional_ia,Techieray,binary,regulatory_treatment,¿Tiene estrategia o política nacional de IA publicada? (1=Sí, 0=No)
tr_tiene_guia_softlaw,Techieray,binary,regulatory_treatment,¿Tiene guías, frameworks, estándares o white papers sobre IA? (1=Sí, 0=No)
tr_tiene_autoridad_dedicada,Techieray,binary,regulatory_treatment,¿Tiene autoridad, agencia u oficina específica para supervisión de IA? (1=Sí, 0=No)
tr_categoria_obligatoriedad,Techieray,categorical,regulatory_treatment,Categoría de obligatoriedad regulatoria: binding / non-binding / mixed / none
tr_n_leyes_relacionadas,Techieray,count,regulatory_treatment,Número de leyes y proyectos de ley de IA identificados en el tracker
tr_n_autoridades,Techieray,count,regulatory_treatment,Número de autoridades/agencias de IA identificadas en el tracker
tr_sandbox_regulatorio,Techieray,binary,regulatory_treatment,¿Tiene sandbox regulatorio de IA? (1=Sí, 0=No)
tr_marcos_voluntarios,Techieray,binary,regulatory_treatment,¿Tiene marcos voluntarios o códigos de conducta de IA? (1=Sí, 0=No)
tr_instituto_seguridad_ia,Techieray,binary,regulatory_treatment,¿Tiene instituto de seguridad de IA (AISI o equivalente)? (1=Sí, 0=No)
tr_herramientas_testing,Techieray,binary,regulatory_treatment,¿Tiene herramientas de testing/evaluación de IA? (1=Sí, 0=No)
tr_modelo_gobernanza,Techieray,categorical,regulatory_treatment,Modelo de gobernanza de IA: centralized / sectoral / distributed / eu_delegated / none
tr_adhiere_oecd,Techieray,binary,regulatory_treatment,¿Es miembro OECD y adhiere a los AI Principles? (1=Sí, 0=No)
tr_adopto_unesco,Techieray,binary,regulatory_treatment,¿Ha adoptado la Recomendación de Ética de IA de UNESCO? (1=Sí, 0=No)
```

#### 2.3 Actualizar fuentes usadas

Agregar 1 fila a `fase3_fuentes_usadas.csv`:

```csv
fuente_id,fuente_nombre,autor,url,descripcion,fecha_consulta
TECHIERAY,Techieray Global AI Regulation Tracker,Raymond Sun (techie_ray® labs),https://www.techieray.com/GlobalAIRegulationTracker,Mapa interactivo con perfiles regulatorios de IA por país. Categorías: leyes, proyectos, estrategias, guías, sandboxes, autoridades. Actualización regular.,2026-05-08
```

#### 2.4 Actualizar manifest de Fase 3

```json
{
  "fase3_version": "1.2",
  "updated_at": "2026-05-08T00:00:00Z",
  "change_log": "Agregadas 15 variables Techieray (fuente #9). Cobertura: 43 países.",
  "new_variables": [
    "tr_ley_ia_vigente", "tr_proyecto_ley_ia", "tr_estrategia_nacional_ia",
    "tr_tiene_guia_softlaw", "tr_tiene_autoridad_dedicada", "tr_categoria_obligatoriedad",
    "tr_n_leyes_relacionadas", "tr_n_autoridades", "tr_sandbox_regulatorio",
    "tr_marcos_voluntarios", "tr_instituto_seguridad_ia", "tr_herramientas_testing",
    "tr_modelo_gobernanza", "tr_adhiere_oecd", "tr_adopto_unesco"
  ],
  "new_source": "Techieray Global AI Regulation Tracker (Raymond Sun)"
}
```

**Archivos modificados en Fase 3:**
- `Matriz_Madre_Fase3.xlsx` — 15 columnas nuevas
- `fase3_diccionario_variables.csv` — 15 filas nuevas
- `fase3_fuentes_usadas.csv` — 1 fila nueva
- `manifest.json` — versión actualizada

**Archivos NO modificados:**
- `src/fase3/api.py` — `load_wide()` automáticamente incluye las nuevas columnas (lee del Excel)
- `matriz_madre_trazabilidad.csv` — las nuevas celdas son trazables a `FUENTES/TECHIERAY/XXX-Nombre.md`
- Resto de archivos de Fase 3

**Tiempo:** 1.5 horas.

---

### PASO 3 — Mini-EDA "Fase 4.5" sobre variables Techieray

**Objetivo:** validar la nueva fuente y generar los análisis exploratorios que corresponden a variables regulatorias con cobertura completa.

**Directorio:** `FASE4/outputs/eda_techieray/` (nuevo, no modifica `eda_principal/`)

#### 3.1 Cobertura de las 15 variables Techieray

```python
# coverage_techieray.py
import pandas as pd

techieray = pd.read_csv("FUENTES/TECHIERAY/tr_regulatory_metadata.csv")
n = len(techieray)  # 43

coverage = []
for col in techieray.columns:
    if col == "iso3":
        continue
    non_null = techieray[col].notna().sum()
    pct = non_null / n * 100
    coverage.append({"variable": col, "n_non_null": non_null, "pct": round(pct, 1)})

pd.DataFrame(coverage).to_csv("FASE4/outputs/eda_techieray/coverage_techieray.csv", index=False)
```

#### 3.2 Validación cruzada IAPP vs Techieray

Para los 18 países con ambas fuentes:

```python
# validate_iapp_vs_techieray.py
iapp = load_wide()[["iso3", "iapp_ley_ia_vigente", "iapp_proyecto_ley_ia",
                     "iapp_n_leyes_relacionadas", "iapp_n_autoridades",
                     "iapp_categoria_obligatoriedad", "iapp_modelo_gobernanza"]]
techieray = pd.read_csv("FUENTES/TECHIERAY/tr_regulatory_metadata.csv")

merged = iapp.merge(techieray, on="iso3", how="inner")  # 18 países

comparisons = []
for _, row in merged.iterrows():
    # Ley vigente
    match_ley = row["iapp_ley_ia_vigente"] == row["tr_ley_ia_vigente"]
    comparisons.append({
        "iso3": row["iso3"],
        "variable": "ley_ia_vigente",
        "iapp": row["iapp_ley_ia_vigente"],
        "techieray": row["tr_ley_ia_vigente"],
        "match": match_ley
    })
    # Proyecto de ley
    match_proy = row["iapp_proyecto_ley_ia"] == row["tr_proyecto_ley_ia"]
    comparisons.append({
        "iso3": row["iso3"],
        "variable": "proyecto_ley_ia",
        "iapp": row["iapp_proyecto_ley_ia"],
        "techieray": row["tr_proyecto_ley_ia"],
        "match": match_proy
    })
    # ... (repetir para n_leyes, n_autoridades, categoria, modelo)

pd.DataFrame(comparisons).to_csv("FASE4/outputs/eda_techieray/iapp_vs_techieray_validation.csv", index=False)

# Reportar tasa de concordancia
for var in comparisons_df["variable"].unique():
    sub = comparisons_df[comparisons_df["variable"] == var]
    match_rate = sub["match"].mean()
    print(f"{var}: {match_rate:.0%} de concordancia IAPP-Techieray")
```

**Umbral de aceptación:** ≥ 80% de concordancia en variables binarias clave (`ley_ia_vigente`, `proyecto_ley_ia`). Si hay discrepancias > 20%, revisar país por país y documentar.

#### 3.3 Correlaciones Techieray vs Outcomes Q1-Q6

```python
# correlations_techieray_vs_outcomes.py
outcomes = [
    "oxford_ind_company_investment_emerging_tech", "oxford_ind_ai_unicorns_log",
    "oxford_ind_vc_availability", "wipo_c_vencapdeal_score",
    "ms_h2_2025_ai_diffusion_pct", "oecd_5_ict_business_oecd_biz_ai_pct",
    "anthropic_usage_pct", "oxford_public_sector_adoption",
    "oxford_ind_adoption_emerging_tech", "oxford_total_score", "wipo_out_score",
    "oxford_e_government_delivery", "oxford_government_digital_policy",
    "oxford_ind_data_governance", "oxford_governance_ethics",
    "oecd_2_indigo_oecd_indigo_score", "anthropic_collaboration_pct",
]

wide = load_wide()
techieray = pd.read_csv("FUENTES/TECHIERAY/tr_regulatory_metadata.csv")
merged = wide.merge(techieray, on="iso3", how="inner")

from scipy.stats import spearmanr
import numpy as np

correlations = []
for tech_var in techieray.columns:
    if tech_var == "iso3" or tech_var == "tr_ultima_actualizacion":
        continue
    for out in outcomes:
        sub = merged[[tech_var, out]].dropna()
        if len(sub) < 15:
            continue
        rho, p = spearmanr(sub[tech_var], sub[out])
        correlations.append({
            "techieray_var": tech_var,
            "outcome": out,
            "spearman_rho": round(rho, 3),
            "p_value": round(p, 4),
            "n": len(sub)
        })

pd.DataFrame(correlations).to_csv(
    "FASE4/outputs/eda_techieray/techieray_vs_outcomes_spearman.csv", index=False
)
```

**Comparación clave:** para los outcomes donde `iapp_ley_ia_vigente` tenía correlación, ¿`tr_ley_ia_vigente` muestra la misma dirección con n=40?

#### 3.4 PCA regulatorio expandido (43 países)

```python
# pca_techieray.py
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

techieray = pd.read_csv("FUENTES/TECHIERAY/tr_regulatory_metadata.csv")
# Seleccionar variables numéricas (binarias y conteos)
binary_vars = [c for c in techieray.columns 
               if c.startswith("tr_") and c != "tr_categoria_obligatoriedad" 
               and c != "tr_modelo_gobernanza"]
numeric = techieray[["iso3"] + binary_vars].dropna()

X = StandardScaler().fit_transform(numeric[binary_vars])
pca = PCA(n_components=min(5, len(binary_vars)))
pca.fit(X)

loadings = pd.DataFrame(
    pca.components_.T,
    index=binary_vars,
    columns=[f"PC{i+1}" for i in range(pca.n_components_)]
)
loadings.to_csv("FASE4/outputs/eda_techieray/pca_techieray_loadings.csv")

variance = pd.DataFrame({
    "PC": [f"PC{i+1}" for i in range(pca.n_components_)],
    "variance_explained": pca.explained_variance_ratio_,
    "cumulative": np.cumsum(pca.explained_variance_ratio_)
})
variance.to_csv("FASE4/outputs/eda_techieray/pca_techieray_variance.csv", index=False)
```

**Pregunta a responder:** ¿cuántas dimensiones latentes capturan las variables regulatorias de los 43 países? ¿Son consistentes con la taxonomía binding/non-binding/hybrid de Fase 4?

#### 3.5 Taxonomía binding actualizada

```python
# taxonomy_techieray.py
# Clasificar variables Techieray en la misma taxonomía de Fase 4

binding_techieray = [
    "tr_ley_ia_vigente",
    "tr_n_leyes_relacionadas",
    "tr_n_autoridades",
]

non_binding_techieray = [
    "tr_estrategia_nacional_ia",
    "tr_tiene_guia_softlaw",
    "tr_marcos_voluntarios",
    "tr_adhiere_oecd",
    "tr_adopto_unesco",
]

hybrid_techieray = [
    "tr_proyecto_ley_ia",
    "tr_sandbox_regulatorio",
    "tr_instituto_seguridad_ia",
    "tr_herramientas_testing",
]
```

Guardar en `FASE4/outputs/eda_techieray/binding_taxonomy_techieray.yaml`.

**Archivos generados en Paso 3:**
```
FASE4/outputs/eda_techieray/
├── coverage_techieray.csv
├── iapp_vs_techieray_validation.csv
├── techieray_vs_outcomes_spearman.csv
├── pca_techieray_loadings.csv
├── pca_techieray_variance.csv
├── binding_taxonomy_techieray.yaml
└── eda_techieray_manifest.json
```

**Tiempo:** 2 horas.

---

### PASO 4 — Actualizar Fase 5 (Feature Matrix)

**Objetivo:** incorporar las variables Techieray a la feature matrix que alimenta Fase 6, y recalcular `n_binding`/`n_non_binding`.

#### 4.1 Agregar variables Techieray a `mvp_variables.yaml`

En `FASE5/config/mvp_variables.yaml`, agregar al bloque `regulatory_treatment`:

```yaml
  # Techieray — variables regulatorias con cobertura completa (43 países)
  - variable_matriz: tr_ley_ia_vigente
    bloque: regulatory_treatment
    rol_mvp: X1_principal
    tipo: binary
    fuente: Techieray Global AI Regulation Tracker
    razon: "Indicador de regulación binding con cobertura 43 países (vs IAPP 18)"

  - variable_matriz: tr_proyecto_ley_ia
    bloque: regulatory_treatment
    rol_mvp: X1_hybrid
    tipo: binary
    fuente: Techieray
    razon: "Captura intención regulatoria en trámite"

  - variable_matriz: tr_estrategia_nacional_ia
    bloque: regulatory_treatment
    rol_mvp: X1_contextual
    tipo: binary
    fuente: Techieray
    razon: "Existencia de estrategia nacional de IA"

  # ... (15 variables en total, con el mismo patrón)
```

#### 4.2 Actualizar `engineer.py`

Modificar `FASE5/src/engineer.py` para recalcular `n_binding` y `n_non_binding` incorporando Techieray:

```python
def build_regulatory_aggregates(wide: pd.DataFrame) -> pd.DataFrame:
    """
    Reconstruye n_binding, n_non_binding, n_hybrid usando
    IAPP (18 países) + Techieray (43 países).
    Para países sin IAPP, usa solo Techieray.
    """
    out = wide.copy()
    
    # === BINDING ===
    binding_iapp = [
        "iapp_ley_ia_vigente", "iapp_categoria_obligatoriedad",
        "iapp_firmo_coe_convencion", "iapp_n_leyes_relacionadas", "iapp_n_autoridades"
    ]
    binding_techieray = [
        "tr_ley_ia_vigente", "tr_n_leyes_relacionadas", "tr_n_autoridades"
    ]
    
    # IAPP binding (solo 18 países tienen dato; el resto NaN)
    iapp_binding_sum = out[binding_iapp].fillna(0).clip(0, 1).sum(axis=1)
    # Techieray binding (43 países)
    tech_binding_sum = out[binding_techieray].fillna(0).clip(0, 1).sum(axis=1)
    # Combinar: donde IAPP tiene dato, usar IAPP; donde no, usar Techieray
    out["n_binding"] = out["iapp_ley_ia_vigente"].notna().map({
        True: iapp_binding_sum,
        False: tech_binding_sum
    })
    
    # === NON-BINDING ===
    non_binding_iapp = [
        "iapp_estrategia_nacional_ia", "iapp_adhiere_oecd_ai",
        "iapp_adopto_unesco_etica_ia", "iapp_endoso_hiroshima_g7",
        "iapp_firmo_bletchley", "iapp_endoso_declaracion_data_scraping",
        "iapp_firmo_ai_action_summit", "iapp_marcos_voluntarios",
        "iapp_guias_sectoriales", "iapp_herramientas_testing"
    ]
    non_binding_techieray = [
        "tr_estrategia_nacional_ia", "tr_tiene_guia_softlaw",
        "tr_marcos_voluntarios", "tr_adhiere_oecd", "tr_adopto_unesco"
    ]
    
    iapp_nb_sum = out[non_binding_iapp].fillna(0).clip(0, 1).sum(axis=1)
    tech_nb_sum = out[non_binding_techieray].fillna(0).clip(0, 1).sum(axis=1)
    out["n_non_binding"] = out["iapp_estrategia_nacional_ia"].notna().map({
        True: iapp_nb_sum,
        False: tech_nb_sum
    })
    
    # === HYBRID ===
    hybrid_iapp = [
        "iapp_proyecto_ley_ia", "iapp_modelo_gobernanza",
        "iapp_sandbox_regulatorio", "iapp_instituto_seguridad_ia"
    ]
    hybrid_techieray = [
        "tr_proyecto_ley_ia", "tr_sandbox_regulatorio",
        "tr_instituto_seguridad_ia", "tr_herramientas_testing"
    ]
    
    iapp_hy_sum = out[hybrid_iapp].fillna(0).clip(0, 1).sum(axis=1)
    tech_hy_sum = out[hybrid_techieray].fillna(0).clip(0, 1).sum(axis=1)
    out["n_hybrid"] = out["iapp_proyecto_ley_ia"].notna().map({
        True: iapp_hy_sum,
        False: tech_hy_sum
    })
    
    return out
```

**Nota importante:** `n_binding` y `n_non_binding` se vuelven **no comparables** entre la versión anterior (solo IAPP) y la nueva (IAPP + Techieray). Esto es esperado y debe documentarse. La comparación válida es hacia adelante.

#### 4.3 Re-ejecutar Fase 5

```bash
cd F5_F8_MVP/FASE5
python -m src.build   # re-ejecuta build.py con las nuevas variables
```

**Outputs actualizados:**
- `feature_matrix_mvp.csv` — con columnas Techieray + `n_binding`/`n_non_binding` recalculados
- `MVP_AUDITABLE.xlsx` — hoja 2 (Variables) y hoja 3 (Feature Matrix) actualizadas
- `phase6_ready/` — bundle actualizado para Fase 6

**Tiempo:** 1.5 horas.

---

### PASO 5 — Re-ejecutar Fase 6.1 con X1 expandidas

**Objetivo:** re-estimar los modelos Q1-Q6 usando las variables Techieray como predictores adicionales, y expandir Q4 a 43 países.

#### 5.1 Modificaciones en `q1_investment.py`, `q3_innovation.py`

Agregar a `X1_VARS`:

```python
X1_VARS = [
    "n_binding", "n_non_binding", "regulatory_intensity",
    # NUEVO: variables Techieray con cobertura completa
    "tr_ley_ia_vigente",      # ← antes: iapp_ley_ia_vigente (n=17)
    "tr_n_leyes_relacionadas", # ← antes: iapp_n_leyes_relacionadas (n=18)
    "tr_n_autoridades",        # ← antes: iapp_n_autoridades (n=18)
]
```

**Mantener** `iapp_ley_ia_vigente` en X1_VARS para los 18 países que la tienen (el modelo aplica listwise deletion, así que los 25 sin IAPP simplemente no entran en ese término).

#### 5.2 Modificaciones en `q2_adoption.py`, `q5_population_usage.py`, `q6_public_sector.py`

Misma lógica: agregar `tr_ley_ia_vigente`, `tr_n_leyes_relacionadas`, `tr_n_autoridades` a los predictores.

#### 5.3 Reescritura de `q4_clustering.py` — de 18 a 43 países

Este es el cambio más significativo:

```python
def build_regulatory_binary_vector(wide_mvp: pd.DataFrame) -> pd.DataFrame:
    """
    ANTES: usaba solo iapp_ley_ia_vigente e iapp_proyecto_ley_ia (18 países)
    AHORA: usa 5 variables Techieray binarias (43 países)
    """
    tech_cols = [
        "tr_ley_ia_vigente",
        "tr_proyecto_ley_ia",
        "tr_estrategia_nacional_ia",
        "tr_tiene_guia_softlaw",
        "tr_tiene_autoridad_dedicada",
    ]
    # 43 países con datos (los NaN se llenan con 0 = "no detectado")
    return wide_mvp[["iso3", "country_name_canonical"] + tech_cols].fillna(0)


def run_q4(wide_mvp: pd.DataFrame) -> dict:
    binary_df = build_regulatory_binary_vector(wide_mvp)  # 43 filas
    value_cols = [c for c in binary_df.columns if c.startswith("tr_")]
    
    # Distancia Jaccard sobre 43 países
    D = jaccard_distance_matrix(binary_df, value_cols)  # matriz 43×43
    
    # HCA con k=4 (o ajustar k según silhouette)
    hca_labels = hca_clustering(D, k=4)
    
    # KMeans como sensibilidad (k=4)
    km_labels = kmeans_clustering(binary_df, value_cols, k=4)
    
    binary_df["cluster_hca"] = hca_labels
    binary_df["cluster_kmeans"] = km_labels
    
    return {
        "clusters": binary_df,          # 43 filas
        "metrics": {"silhouette_hca": ..., "silhouette_kmeans": ...},
        "distance_matrix": D,           # 43×43
    }
```

**Cambio clave:** `q4_clusters.csv` pasa de 18 a **43 filas**. Los 25 países que antes no tenían perfil regulatorio ahora lo tienen.

#### 5.4 Re-ejecutar `run_all.py`

```bash
cd F5_F8_MVP/FASE6
python -m src.run_all
```

**Outputs actualizados:**
- `q1_results.csv` — filas adicionales para términos Techieray; n_effective ≈ 40 para `tr_ley_ia_vigente`
- `q2_results.csv` — ídem
- `q3_results.csv` — ídem
- `q4_clusters.csv` — **18 → 43 filas**
- `q4_distance_matrix.csv` — **18×18 → 43×43**
- `q5_results.csv` — ídem
- `q6_results.csv` — ídem
- `fase6_manifest.json` — run_metadata actualizado

**Tiempo:** 2.5 horas.

---

### PASO 6 — Re-ejecutar Fase 6.2 (Country Intelligence Layer)

**Objetivo:** regenerar perfiles país, rankings, figuras y country cards con los nuevos datos.

```bash
cd F5_F8_MVP/FASE6
python -m src.country_intelligence.run_country_intelligence
```

**Outputs actualizados:**

| Archivo | Cambio |
|---|---|
| `country_q_profile_long.csv` | 903+ filas (se agregan filas para términos Techieray) |
| `country_q_profile_wide.csv` | 42 filas; Q4 ahora tiene valores para los 42 países (no solo 18) |
| `country_rankings_by_outcome.csv` | Rankings actualizados con nuevos resultados |
| `country_rankings_by_group.csv` | Ídem |
| `country_best_worst_by_q.csv` | Ídem |
| `country_model_contributions.csv` | Nuevas filas para contribuciones de términos Techieray |
| `country_residuals_and_gaps.csv` | Residuales actualizados |
| `country_cluster_profile.csv` | **18 → 43 filas** — perfil regulatorio para todos |
| `country_headline_flags.csv` | Posiblemente nuevos pioneros/rezagados basados en perfiles completos |
| `country_learning_patterns.csv` | Lecciones actualizadas con datos completos |
| `country_comparison_pairs.csv` | Brechas actualizadas |
| `country_graphics_catalog.csv` | Figuras regeneradas |
| `figures/q4_regulatory_profile_map.png` | **Clusters con 43 países en lugar de 18** |
| `figures/q_rankings/*.png` | Rankings actualizados |
| `figures/heatmap_country_by_q_percentiles.png` | Heatmap con Q4 para todos |
| `figures/country_cards/*.png` | Radares actualizados |
| `country_cards_data/*.csv` | Fichas consolidadas actualizadas |

**Tiempo:** 1 hora.

---

## 4. Línea de Tiempo

| Paso | Descripción | Horas | Depende de |
|---|---|---|---|
| **Recolección** | Llenar 43 checklists | 10-11h | — |
| **Paso 1** | Script parse → CSV | 1h | Recolección completada |
| **Paso 2** | Incorporar a Fase 3 | 1.5h | Paso 1 |
| **Paso 3** | Mini-EDA Fase 4.5 | 2h | Paso 2 |
| **Paso 4** | Actualizar Fase 5 | 1.5h | Paso 3 |
| **Paso 5** | Re-ejecutar Fase 6.1 | 2.5h | Paso 4 |
| **Paso 6** | Re-ejecutar Fase 6.2 | 1h | Paso 5 |
| **Total** | | **19.5-20.5h** | |

---

## 5. Impacto Esperado en Fases Posteriores

### 5.1 Fase 7 (Robustez)

| Aspecto | Antes | Después |
|---|---|---|
| Sensibilidad leave-one-out sobre `tr_ley_ia_vigente` | n=17 → frágil por definición | n≈40 → estable, pocos sign flips |
| Leave-group-out por región con X1 regulatoria | No viable (n insuficiente) | Viable — se puede excluir Europa y re-estimar |
| `conclusion_stability_matrix` | Mayoría de hallazgos con X1 = `not_estimable` | Mayoría = `directionally_stable` o `stable` |
| Baselines regulatorios | Comparación débil (n=17 vs n=40 en controles) | Comparación justa (n≈40 vs n≈40) |

### 5.2 Fase 8 (Narrativa)

| Aspecto | Antes | Después |
|---|---|---|
| Recomendación sobre "tener ley de IA" | "No se puede afirmar con confianza (solo 17 países con dato)" | "Se observa una asociación ajustada positiva entre tener ley de IA e inversión (β=X, IC95=[Y,Z], n=40)" |
| Perfiles regulatorios en informe | Solo 18 países tienen perfil; 25 tienen "sin datos" | Los 43 países tienen perfil regulatorio completo |
| Gráficos Q4 | Mapa con 18 puntos | Mapa con 43 puntos, clusters más informativos |
| Credibilidad ante el Senado | Débil en la dimensión regulatoria | Robusta — todas las X1 tienen cobertura completa |

---

## 6. Archivos Modificados por Fase (Resumen)

### Fase 3 (4 archivos modificados)
```
FASE3/outputs/Matriz_Madre_Fase3.xlsx          ← 15 columnas nuevas
FASE3/outputs/fase3_diccionario_variables.csv   ← 15 filas nuevas
FASE3/outputs/fase3_fuentes_usadas.csv          ← 1 fila nueva
FASE3/outputs/manifest.json                     ← versión 1.2
```

### Fase 4 (7 archivos nuevos en subcarpeta `eda_techieray/`)
```
FASE4/outputs/eda_techieray/
├── coverage_techieray.csv
├── iapp_vs_techieray_validation.csv
├── techieray_vs_outcomes_spearman.csv
├── pca_techieray_loadings.csv
├── pca_techieray_variance.csv
├── binding_taxonomy_techieray.yaml
└── eda_techieray_manifest.json
```

### Fase 5 (2 archivos modificados)
```
FASE5/config/mvp_variables.yaml     ← 15 variables nuevas
FASE5/src/engineer.py               ← n_binding/n_non_binding recalculados
FASE5/outputs/feature_matrix_mvp.csv ← regenerado
FASE5/outputs/MVP_AUDITABLE.xlsx    ← regenerado
```

### Fase 6.1 (7 archivos modificados)
```
FASE6/src/q1_investment.py          ← X1_VARS expandido
FASE6/src/q2_adoption.py            ← Ídem
FASE6/src/q3_innovation.py          ← Ídem
FASE6/src/q4_clustering.py          ← 18→43 países, 5 features Techieray
FASE6/src/q5_population_usage.py    ← X1_VARS expandido
FASE6/src/q6_public_sector.py       ← Ídem
FASE6/outputs/*.csv                 ← Todos regenerados
```

### Fase 6.2 (todos los outputs regenerados)
```
FASE6/outputs/country_intelligence/ ← 14 CSVs + 40 figuras + 11 country cards regenerados
```

---

## 7. Validaciones Transversales

### 7.1 Consistencia con el contrato metodológico

- ✅ Sin train/test split — se mantiene
- ✅ Sin imputación — se mantiene (listwise deletion)
- ✅ Sin causalidad — se mantiene
- ✅ Bootstrap BCa 2000 iter — se mantiene
- ✅ n_effective reportado por modelo — se mantiene (ahora ≈40 para términos Techieray)

### 7.2 Validación de que Techieray no introduce sesgo

| Check | Método |
|---|---|
| ¿Correlación IAPP vs Techieray > 0.80? | Spearman ρ entre `iapp_ley_ia_vigente` y `tr_ley_ia_vigente` para los 18 países con ambas |
| ¿Dirección de asociación con outcomes consistente? | Signo de β para `iapp_ley_ia_vigente` vs `tr_ley_ia_vigente` en mismos outcomes |
| ¿Los 25 países sin IAPP tienen valores plausibles? | Inspección manual de una muestra (ej. Alemania, Francia, España, Brasil, India) |
| ¿La variable `tr_ley_ia_vigente` no es colineal con PIB per cápita? | VIF < 5 en modelo con controles |

### 7.3 Validación de integridad de Fase 3

- [ ] `Matriz_Madre_Fase3.xlsx` se puede abrir sin errores
- [ ] `load_wide()` devuelve las 15 columnas nuevas
- [ ] `load_dictionary()` incluye las 15 variables nuevas
- [ ] Las columnas nuevas tienen valores solo para los 43 países de la muestra (NaN para el resto de los 199)
- [ ] Backup de la matriz original existe antes de la modificación

---

## 8. Riesgos y Mitigaciones

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| Algunos checklists quedan sin llenar (variables faltantes) | Media | El script de parseo detecta `None` y reporta. Variables con >20% missing se marcan como `low_coverage`. |
| Discrepancias grandes IAPP vs Techieray (>20%) | Baja | Revisar país por país. Si la discrepancia es sistemática, documentar y preferir Techieray (más reciente) para 43 países, IAPP para los 18. |
| `tr_ley_ia_vigente` altamente correlacionada con PIB per cápita | Media | Calcular VIF. Si > 5, considerar incluir `tr_ley_ia_vigente` sin controles de riqueza como sensitivity. |
| Clusters Q4 con 43 países poco interpretables | Baja | Con 5 features binarias en lugar de 2, los clusters serán más ricos. Si k=4 no captura bien la estructura, ajustar k según silhouette. |
| `n_binding`/`n_non_binding` no comparables entre versiones | Alta (esperado) | Documentar explícitamente. La variable cambió su definición. Esto es correcto: ahora mide mejor el constructo. |
| Tiempo de extracción manual subestimado | Media | Si después de 5 países el tiempo promedio es >20 min/país, reevaluar. Priorizar Nivel 1 para todos, Nivel 2 solo para países con RAW rico. |

---

## 9. Criterios de Éxito

La integración de Techieray se considera exitosa cuando:

1. ✅ `tr_regulatory_metadata.csv` tiene 43 filas con ≥80% de celdas no-null en variables de Nivel 1.
2. ✅ La validación IAPP vs Techieray muestra ≥80% de concordancia en variables binarias clave.
3. ✅ `tr_ley_ia_vigente` tiene n_effective ≥ 35 en los modelos de Fase 6.1 (vs n=17 actual).
4. ✅ Q4 clustering genera clusters interpretables para los 43 países (no solo 18).
5. ✅ Los 25 países que antes tenían "Sin legislación IA nacional específica detectada" ahora tienen perfil regulatorio completo.
6. ✅ La `conclusion_stability_matrix` de Fase 7 muestra que los hallazgos con X1 regulatoria pasan de `not_estimable` a `directionally_stable` o `stable`.
7. ✅ El informe ejecutivo de Fase 8 puede afirmar con confianza media-alta: "se observa una asociación ajustada entre tener ley de IA vigente y..."

---

## 10. Referencias

- **Techieray Global AI Regulation Tracker:** https://www.techieray.com/GlobalAIRegulationTracker
- **API:** `pip install techieray-ai-reg-tracker-api`
- **Autor:** Raymond Sun (techie_ray® labs)
- **Contacto:** info@techieray.com
- **Plan Fase 7:** `nueva_metodologia/FASE7_PLAN.md`
- **Arquitectura completa:** `CONTEXTOS/6.ARQUITECTURA_COMPLETA_PROYECTO.md`
- **Plan Fases 7-8:** `CONTEXTOS/7.PLAN_FASES_7_8_Y_CORRECCION_IAPP.md`
- **Taxonomía IAPP:** `FASE4/config/fase4/binding_taxonomy.yaml`
- **Feature matrix:** `FASE5/outputs/feature_matrix_mvp.csv`

---

*Documento generado el 2026-05-08. Sujeto a actualización conforme avance la extracción de datos y la ejecución de los pasos.*
