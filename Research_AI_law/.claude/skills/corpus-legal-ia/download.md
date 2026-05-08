# Pipeline técnico de descarga

## Herramienta estándar

```bash
curl -sLk \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept: application/pdf,text/html;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Referer: {URL_REFERRER_LOGICA}" \
  -w "HTTP:%{http_code} SIZE:%{size_download}\n" \
  -o {ISO3}_{ShortDocName}_{Year}.pdf \
  "{URL}"
```

**Flags:**
- `-s` silent
- `-L` follow redirects
- `-k` ignorar SSL cuando aplicable
- UA Chrome completo (crítico para sitios con bloqueos anti-scraping tipo AGC Singapore, portales gov africanos, UNDP a veces).
- Referer = URL lógica de "desde dónde vendrías" al PDF. Crítico en sso.agc.gov.sg, legalinfo.mn, algunos portales UE.

## Patrones de error observados

| Síntoma | Causa probable | Solución |
|---|---|---|
| HTTP 403 con UA "Mozilla/5.0" simple | WAF bloquea UA genérico | UA Chrome completo + headers Accept + Referer |
| HTTP 500 con URL de PDF aparente | Endpoint de export dinámico (no URL estable) | Buscar mirror verificable o WebFetch la página para extraer URL real |
| File tipo "HTML document" tras HTTP 200 | Redirect implícito a login / bot challenge | Revisar response headers, agregar cookies si necesario |
| File tipo "JSON data" tras HTTP 200/404 | Endpoint API sin credenciales | URL alternativa en página pública |
| Loop 301 infinito | Documento retirado, redirect a página padre | Buscar mirror gubernamental regional o confirmar retirada |
| HTTP 200 pero size < 2KB | Página de error con status 200 | Validar con `file` que sea PDF real |

**Siempre validar:** `file {archivo}.pdf` debe reportar `PDF document` (no `HTML`, no `JSON data`, no `empty`).

## Nombrado de archivos

Patrón: `{ISO3}_{ShortDocName}_{Year}.pdf`

Ejemplos reales:
- `SGP_PDPA_2012.pdf`
- `MNG_CyberSecurityLaw_2021.pdf`
- `GHA_NAIS_2023-2033.pdf`
- `BGD_NAIP_2026-2030_v2.0_DRAFT.pdf`

Reglas:
- Sin espacios → `_`.
- Sin caracteres especiales (`(`, `)`, `&`, `,`).
- Year = año de publicación / rango si estrategia cubre período (ej. `2023-2033`).
- Si hay versión (v1, v2), incluirla: `_v2.0_DRAFT`.

## Validación post-descarga

```bash
file *.pdf          # Confirmar "PDF document"
shasum -a 256 *.pdf # SHA-256 para manifest.csv
```

Si `pdfminer.six` está disponible, extraer texto de primeras páginas para verificar autoría/emisor:

```python
from pdfminer.high_level import extract_text
text = extract_text("doc.pdf", maxpages=3)
```

Si no está disponible: `python3 -m pip install --quiet pdfminer.six`.

## Descarga en paralelo

Agrupar descargas independientes en UN solo `Bash` tool call con `&&` para eficiencia:

```bash
cd /ruta/al/corpus/SGP && \
curl ... -o doc1.pdf "URL1" && \
curl ... -o doc2.pdf "URL2" && \
curl ... -o doc3.pdf "URL3" && \
shasum -a 256 *.pdf
```

## Pipeline Selenium (sitios con JS/WAF)

Para sitios que bloquean curl (finlex.fi, e-gov.go.jp, meti.go.jp, parliament.am, etc.),
usar el scraper Selenium del proyecto:

### Instalación (una vez)

```bash
pip install --break-system-packages selenium webdriver-manager undetected-chromedriver pdfminer.six
```

### Descarga de PDFs desde páginas gubernamentales

```bash
# Descargar PDFs encontrados en una página (navega con Chrome headless)
python3 scripts/run_scraper.py download \
  --country JPN \
  --urls "https://www8.cao.go.jp/cstp/ai/" \
  --output-dir data/raw/legal_corpus/JPN \
  --bypass-cloudflare

# Descargar un PDF directo (navega al PDF y lo baja)
python3 scripts/run_scraper.py download \
  --country FIN \
  --urls "https://www.finlex.fi/fi/laki/alkup/2025/20251377" \
  --output-dir data/raw/legal_corpus/FIN \
  --direct-pdf \
  --bypass-cloudflare\
  --visible  # modo visible para debug
```

### Extracción de texto legal estructurado

```bash
# Extraer texto de una ley (con JS rendering)
python3 scripts/run_scraper.py extract \
  --url "https://laws.e-gov.go.jp/law/507AC0000000053" \
  --output data/raw/legal_corpus/JPN/JPN_AI_Act_text.json \
  --site-type e-gov.go.jp

# Extracción genérica (auto-detecta el tipo de sitio)
python3 scripts/run_scraper.py extract \
  --url "https://www.finlex.fi/fi/laki/alkup/2025/20251377" \
  --output data/raw/legal_corpus/FIN/FIN_Law_1377_text.json
```

### Verificar estado de descargas

```bash
python3 scripts/run_scraper.py state --country-dir data/raw/legal_corpus/JPN
```

### Uso programático desde Python

```python
from scripts.scraper import download_pdfs, extract_law_text, StateManager

# Descargar PDFs
results = download_pdfs(
    urls=["https://www8.cao.go.jp/cstp/ai/"],
    output_dir="data/raw/legal_corpus/JPN",
    bypass_cloudflare=True,
    headless=True,
)

# Extraer texto de ley
law_data = extract_law_text(
    url="https://laws.e-gov.go.jp/law/507AC0000000053",
    site_type="e-gov.go.jp",
    output_file="data/raw/legal_corpus/JPN/JPN_AI_Act_2025.json",
)

# Verificar estado incremental
sm = StateManager("data/raw/legal_corpus/JPN")
if sm.should_download("JPN_AI_Act_2025.pdf"):
    # proceed with download
    pass
```

### Cuándo usar curl vs Selenium

| Situación | Método |
|---|---|
| Sitio .gov sirve PDFs directamente (cao.go.jp, ppc.go.jp) | `curl -sLk` (rápido) |
| Sitio requiere JS para renderizar contenido (e-gov.go.jp, finlex.fi) | `run_scraper.py extract` |
| Sitio con Cloudflare/WAF (parliament.am, omd.gh) | `run_scraper.py download --bypass-cloudflare` |
| Sitio sirve PDFs solo enlaces en páginas HTML | `run_scraper.py download` (busca links PDF) |
| Necesitas texto estructurado (artículos, secciones) | `run_scraper.py extract --site-type e-gov.go.jp` |
| Curl devuelve HTML con status 200 | `file` → si es HTML, reintentar con Selenium |

### Módulos del scraper

| Archivo | Función |
|---|---|
| `scripts/scraper/browser.py` | Setup Chrome driver (headless/visible/anti-detect) |
| `scripts/scraper/cloudflare_bypass.py` | Detección y bypass de Cloudflare/WAF challenges |
| `scripts/scraper/downloader.py` | Búsqueda y descarga de PDFs desde páginas |
| `scripts/scraper/law_extractor.py` | Extracción de texto legal estructurado (JS injection) |
| `scripts/scraper/state_manager.py` | Verificación incremental vs manifest.csv |
| `scripts/run_scraper.py` | CLI wrapper para invocación directa |

## Sitios útiles por región

- **SSO / legalinfo.mn / AGC Singapore:** portales legislativos oficiales asiáticos. Headers completos obligatorios.
- **IMDA.gov.sg / PDPC.gov.sg:** agencias IA/data Singapur.
- **legalinfo.mn mirrors:** CYRILLA (cyrilla.org), GRATA (gratanet.com), DLA Piper.
- **UNDP repo (undp.org/sites/g/files/):** AILAs, readiness assessments.
- **UNESCO Digital Library:** RAMs co-firmados.
- **moj.go.kr / bareun-gov / korea.kr:** Corea del Sur.
- **csa.gov.gh / nita.gov.gh / moc.gov.gh:** Ghana.
- **go.gov.sg:** servicio oficial de URL cortas Singapur.
- **aiverifyfoundation.sg:** subsidiaria IMDA.
- **cao.go.jp / www8.cao.go.jp:** Cabinet Office Japón (PDFs directos).
- **ppc.go.jp:** Personal Information Protection Commission Japón (PDFs directos).
- **e-gov.go.jp / laws.e-gov.go.jp:** Portal legislativo Japón (requiere JS → usar Selenium).
- **meti.go.jp:** METI Japón (timeout frecuente → usar Selenium con bypass).
- **finlex.fi:** Portal legislativo Finlandia (requiere JS → usar Selenium).
