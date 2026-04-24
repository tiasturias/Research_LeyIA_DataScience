# Plan de Accion — Recuperacion Datos Oxford Insights 2024

## Estado y Prioridad

| atributo | valor |
|---|---|
| prioridad | **COMPLETADO** |
| estado | **RESUELTO** — extraccion PDF ejecutada el 2026-04-08 |
| tipo de gap | Oxford Insights no publico XLSX/CSV oficial para 2024 |
| impacto original | faltaba un año completo del panel temporal (brecha 2023 → 2025) |
| resolucion | Estrategia 1 (pdfplumber) ejecutada con exito: 188 paises, 0 errores, 86/86 muestra |
| metodologia afectada | v2 (3 pilares, 9 dimensiones, 0-100) — mismo regimen que 2020-2023 |
| fecha de este analisis | 2026-04-08 |

---

## Hallazgo Clave: Los Datos Estan en el PDF

El reporte PDF oficial `2024_government_ai_readiness_index.pdf` (50 paginas, 4.17 MB) **contiene las tablas de scores en las paginas 43-50**. Cada pagina tiene una tabla con 5 columnas:

```
Country | Total | Government | Technology Sector | Data and Infrastructure
```

Inspeccion con `pdfplumber` ejecutada el 2026-04-08 confirma:

| paginas | tablas detectadas | filas aprox. | muestra de datos |
|---|---|---|---|
| 43 | 1 tabla x 5 cols | 23 filas | Afghanistan: Total=16.92, Gov=8.27, Tech=22.46, D&I=20.05 |
| 44 | 1 tabla x 5 cols | 27 filas | Brazil: Total=65.89, Gov=74.51, Tech=44.78, D&I=78.38 |
| 45 | 1 tabla x 5 cols | 27 filas | Ecuador-Indonesia range |
| 46 | 1 tabla x 5 cols | 27 filas | Indonesia-Mali range |
| 47 | 1 tabla x 5 cols | 28 filas | Mali-Malta range |
| 48 | 1 tabla x 5 cols | 26 filas | Portugal: Total=70.93, Gov=79.47, Tech=52.49, D&I=80.83 |
| 49 | 1 tabla x 5 cols | 24 filas | SriLanka, StateofPalestine |
| 50 | 1 tabla x 5 cols | 7 filas | Uzbekistan: Total=53.45, Gov=64.71, Tech=33.50, D&I=62.14 |

> **Nota de extraccion**: algunos nombres de pais aparecen concatenados sin espacios (ej. `SriLanka`, `StateofPalestine`, `UnitedArabEmirates`). El parser debe manejar esto con el diccionario Oxford→ISO3 existente o con normalizacion por regex.

Valores de referencia mencionados en el texto narrativo del PDF (para validacion posterior):
- USA: Total = 87.03 (pag. 14)
- Canada: Total = 78.18 (pag. 14)
- France: Total = 79.36 (pag. 18)
- United Kingdom: Total = 78.88 (pag. 18)
- Singapore: Total = 84.25 (pag. 22)
- Korea (Republic of): Total = 79.98 (pag. 22)
- Estonia: Total = 72.62 (pag. 20)
- Brazil: Total = 65.89 (pag. 16)
- India: Total = 62.81 (pag. 26)
- Australia: Total = 76.44 (pag. 28)
- Mauritius: Total = 53.94 (pag. 30)
- South Africa: Total = 52.91 (pag. 30)

---

## Estrategia 1 (Recomendada): Extraccion Automatizada con pdfplumber

**Complejidad:** Media | **Tiempo estimado:** 1-2 horas | **Intervencion humana:** minima

### Prerequisitos

```bash
# pdfplumber ya esta instalado en el venv del proyecto
pip install pdfplumber  # si no
```

El PDF ya esta descargado en:
```
data/raw/Oxford Insights/reports/2024_government_ai_readiness_index.pdf
```

### Algoritmo de extraccion

```python
import pdfplumber
import pandas as pd
from pathlib import Path

PDF_PATH = Path('data/raw/Oxford Insights/reports/2024_government_ai_readiness_index.pdf')
SCORE_PAGES = list(range(43, 51))  # paginas 43-50 (0-indexed: 42-49)

rows = []
with pdfplumber.open(PDF_PATH) as pdf:
    for page_num in SCORE_PAGES:
        pg = pdf.pages[page_num - 1]
        tables = pg.extract_tables()
        for table in tables:
            for row in table:
                # Ignorar filas de encabezado y filas vacias
                if row[0] in (None, '', 'Country', 'GovernmentPillar'):
                    continue
                if len(row) >= 5 and row[1] is not None:
                    rows.append({
                        'country_name_oxford': row[0],
                        'ai_readiness_score':  float(row[1]),
                        'pillar_government':    float(row[2]),
                        'pillar_technology_sector': float(row[3]),
                        'pillar_data_and_infrastructure': float(row[4]),
                    })

df_raw = pd.DataFrame(rows)
print(f'Paises extraidos: {len(df_raw)}')
print(df_raw.sort_values('ai_readiness_score', ascending=False).head(10))
```

### Normalizacion de nombres a ISO3

Reutilizar el diccionario `OXFORD_NAME_TO_ISO3` ya construido en `notebooks/01_recoleccion.ipynb` (celda de setup Oxford). Casos especiales conocidos a agregar o verificar:

| nombre en PDF | ISO3 esperado | nota |
|---|---|---|
| `SriLanka` | LKA | concatenado sin espacio |
| `StateofPalestine` | PSE | concatenado |
| `UnitedStates` | USA | concatenado probable |
| `UnitedKingdom` | GBR | concatenado probable |
| `UnitedArabEmirates` | ARE | concatenado probable |
| `Korea(RepublicOf)` | KOR | parentesis incluido |
| `Iran(IslamicRepublicof)` | IRN | ya detectado en tabla |
| `NewZealand` | NZL | concatenado probable |
| `SaudiArabia` | SAU | concatenado probable |
| `SouthAfrica` | ZAF | concatenado probable |
| `CostaRica` | CRI | concatenado probable |
| `DominicanRepublic` | DOM | concatenado probable |
| `ElSalvador` | SLV | concatenado probable |
| `PapuaNewGuinea` | PNG | concatenado probable |
| `BosniaandHerzegovina` | BIH | con minuscula 'and' |

Estrategia de normalizacion sugerida:

```python
import re

def normalize_oxford_name(raw_name: str) -> str:
    """Insertar espacios antes de mayusculas para nombres concatenados."""
    # "SriLanka" -> "Sri Lanka", "UnitedStates" -> "United States"
    spaced = re.sub(r'(?<=[a-z])([A-Z])', r' \1', raw_name)
    # Casos con parentesis: "Korea(RepublicOf)" -> "Korea (Republic Of)"
    spaced = re.sub(r'([a-zA-Z])\(', r'\1 (', spaced)
    return spaced.strip()
```

### Schema de salida esperado

La tabla 2024 debe integrarse al panel existente con el mismo esquema que 2020-2023 (regimen v2):

```
year                             = 2024
iso3                             = ISO3 normalizado
country_name_std                 = nombre estandarizado
country_name_oxford              = nombre raw del PDF
ai_readiness_score               = Total (columna 2 del PDF)
ai_readiness_score_original      = mismo valor (ya en 0-100 nativo)
score_scale_original             = '0_to_100'
pillar_government                = columna 3
pillar_technology_sector         = columna 4
pillar_data_and_infrastructure   = columna 5
oxford_rank_reported             = rank derivado por orden de score (no aparece en tabla PDF)
methodology_regime               = 'v2_2020_2023_3_pillars_9_dimensions_scale_0_to_100'
comparability_group              = 'v2_comparable'
source_name                      = 'Oxford Insights'
source_dataset                   = '2024_government_ai_readiness_index.pdf'
report_url                       = 'https://oxfordinsights.com/wp-content/uploads/2024/12/2024-Government-AI-Readiness-Index-1.pdf'
data_asset_url                   = 'https://oxfordinsights.com/wp-content/uploads/2024/12/2024-Government-AI-Readiness-Index-1.pdf'
source_tier                      = 'official_pdf_extracted'
coverage_level                   = 'country'
report_edition                   = '2024'
methodology_url                  = ''
```

> **Nota importante:** `source_tier = 'official_pdf_extracted'` distingue este año de los demas (que tienen `'official_primary'`). Esto permite que un auditor identifique inmediatamente que 2024 viene de extraccion PDF, no de XLSX oficial.

> **Nota sobre dimensiones:** El PDF 2024 solo publica scores a nivel de pilar (3 columnas). No hay datos de las 9 dimensiones (vision, governance_ethics, digital_capacity, etc.). Por lo tanto `oxford_ai_readiness_dimensions_long.csv` y `oxford_ai_readiness_pillars_long.csv` tendran datos parciales para 2024 — solo pilares, no dimensiones.

### Controles de calidad post-extraccion

1. Contar paises: El PDF describe ~193 paises incluidos. Validar que se extraen entre 185-200 filas.
2. Rango de scores: min > 10, max < 92 (consistente con ediciones v2).
3. Spot-checks contra valores del texto narrativo del PDF (ver tabla arriba).
4. Duplicados: 0 paises repetidos.
5. ISO3 sin mapear: 0 (o documentar los que no tengan mapeo).
6. Muestra del estudio: verificar cuantos de los 86 paises del estudio aparecen.

---

## Estrategia 2 (Complementaria): Busqueda de Dataset Oficial No Descubierto

**Complejidad:** Baja | **Tiempo estimado:** 30 min | **Resultado esperado:** muy probablemente negativo

Antes de ejecutar la extraccion PDF, vale la pena un ultimo intento de encontrar el XLSX oficial, en caso de que Oxford lo haya publicado en una ubicacion no convencional.

### Pasos

```bash
# 1. Buscar en la API de wordpress con terminos alternativos
curl -L -s 'https://oxfordinsights.com/wp-json/wp/v2/media?search=2024&per_page=100' \
  | python3 -c "import sys,json; [print(m.get('source_url','')) for m in json.load(sys.stdin) if 'xlsx' in m.get('source_url','').lower() or 'csv' in m.get('source_url','').lower()]"

# 2. Buscar en la pagina de landing del indice 2024 (si existe)
curl -L -s -o /dev/null -w '%{http_code}' 'https://oxfordinsights.com/ai-readiness/government-ai-readiness-index-2024/'

# 3. Buscar via Wayback Machine
curl -L -s 'https://archive.org/wayback/available?url=oxfordinsights.com/ai-readiness/government-ai-readiness-index-2024/'

# 4. Buscar en la pagina consolidada del indice
curl -L -s 'https://oxfordinsights.com/ai-readiness/ai-readiness-index/' | grep -i '2024' | grep -i 'xlsx\|csv\|data'
```

Si cualquiera de estos devuelve una URL de XLSX, usar ese archivo como fuente primaria en lugar de la extraccion PDF y actualizar `source_tier = 'official_primary'`.

---

## Estrategia 3 (Fallback Manual): Contacto con Oxford Insights

**Complejidad:** Baja | **Tiempo estimado:** 1-2 semanas (depende de respuesta) | **Intervencion:** alta

Solo usar si la extraccion PDF produce resultados inconsistentes o si se necesitan datos de dimensiones (no presentes en la tabla del PDF).

### Pasos

1. Ir a `https://oxfordinsights.com/contact/`
2. Enviar solicitud indicando:
   - Contexto: investigacion academica sobre el impacto de regulacion IA en ecosistemas de IA
   - Pedido: dataset estructurado (XLSX o CSV) de la edicion 2024 del Government AI Readiness Index
   - Referencia: el PDF 2024 descargado tiene scores totales pero no datos a nivel de dimension
   - Uso: exclusivamente para investigacion sin fines comerciales

### Template de correo sugerido

```
Subject: Request for structured dataset — Government AI Readiness Index 2024

Dear Oxford Insights team,

I am conducting academic research on the impact of AI regulatory frameworks on AI 
ecosystem development across countries. Your Government AI Readiness Index is a key 
data source for this study.

I have accessed all structured datasets for 2019–2023 and 2025 from your website. 
However, I was unable to find a structured dataset (XLSX or CSV) for the 2024 edition 
— only the PDF report is available.

Would it be possible to receive the 2024 public dataset in structured format? Even 
the pillar-level scores would be very helpful. I will credit Oxford Insights in any 
publication resulting from this research.

Thank you very much for your consideration.
```

---

## Integracion al Notebook 01_recoleccion.ipynb

Una vez obtenida la tabla de 2024 (por cualquier estrategia), integrarla al panel Oxford siguiendo este orden en el notebook:

1. Agregar una nueva celda de codigo en la seccion Oxford (despues de la celda de hotfix 2025).
2. La celda debe:
   - Ejecutar la extraccion PDF con pdfplumber
   - Aplicar normalizacion de nombres → ISO3
   - Construir un DataFrame con el schema exacto de v2 (mismo que 2020-2023)
   - Hacer `pd.concat` con `oxford_raw_df` existente
   - Actualizar `oxford_study_df`, `oxford_long_df`, `oxford_snapshot_latest_df` (snapshot sigue siendo 2025)
   - Re-ejecutar la celda de save/verify para regenerar los CSVs
3. Actualizar `download_manifest.csv`: cambiar la entrada `year=2024, available=False` a `available=True` con la ruta del PDF como fuente y `source_tier = 'official_pdf_extracted'`.
4. Actualizar `VARIABLES_OXFORD_INSIGHTS.md`: seccion de cobertura global (agregar fila 2024), tabla de activos, y nota en la seccion Gap 2024 indicando que fue resuelto por extraccion PDF.
5. Actualizar `SEGUIMIENTO_PAISES_MUESTRA.md`: cobertura de `ai_readiness_score` para 2024.

---

## Orden de Ejecucion Recomendado

```
[AHORA — posible]   Estrategia 2 (busqueda API) → 30 min, bajo esfuerzo
       |
       v
[AHORA — posible]   Estrategia 1 (extraccion PDF) → 1-2 horas, alta probabilidad de exito
       |
       v
[A FUTURO]          Estrategia 3 (contacto Oxford) → si se necesitan datos de dimensiones
```

La Estrategia 1 (extraccion PDF) es ejecutable inmediatamente y tiene muy alta probabilidad de exito dado que el PDF tiene tablas estructuradas detectables con pdfplumber. Solo producira datos a nivel de pilar (no dimension). Si se necesitan las 9 dimensiones para el analisis, la unica via es contactar Oxford directamente.

---

## Archivos de Referencia

| archivo | proposito |
|---|---|
| `data/raw/Oxford Insights/reports/2024_government_ai_readiness_index.pdf` | Fuente primaria para extraccion |
| `data/raw/Oxford Insights/metadata/wp_media_search_government_ai_readiness.json` | Evidencia de busqueda API negativa |
| `data/raw/Oxford Insights/metadata/wp_media_search_public_data.json` | Evidencia de busqueda API negativa |
| `data/raw/Oxford Insights/download_manifest.csv` | Actualizar cuando se resuelva el gap |
| `info_data/VARIABLES_OXFORD_INSIGHTS.md` | Documentacion Oxford — actualizar tras integracion |
| `info_data/SEGUIMIENTO_PAISES_MUESTRA.md` | Seguimiento paises — actualizar tras integracion |
| `notebooks/01_recoleccion.ipynb` | Notebook donde se integra el codigo de extraccion |

---

## Definicion de Hecho (Definition of Done)

El gap 2024 se considera **resuelto** cuando:

- [x] `oxford_ai_readiness_all_raw.csv` pasa de 1095 a ~1285 filas — **RESULTADO: 1283 filas** ✓
- [x] `oxford_ai_readiness_study.csv` incluye year=2024 con 85-86 paises de la muestra — **RESULTADO: 86/86** ✓
- [x] `oxford_ai_readiness_pillars_long.csv` incluye year=2024 — **RESULTADO: 3852 filas (era 3288)** ✓
- [x] Spot-checks validados: USA≈87.03, SGP≈84.25, FRA≈79.36, GBR≈78.88, CAN≈78.18 — **TODOS OK** ✓
- [x] `download_manifest.csv` tiene `available=True` para year=2024 — **status=extracted_from_pdf** ✓
- [x] `VARIABLES_OXFORD_INSIGHTS.md` actualizado con cobertura 2024 ✓
- [x] `SEGUIMIENTO_PAISES_MUESTRA.md` actualizado con cobertura 2024 ✓
