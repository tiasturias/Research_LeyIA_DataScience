# Plan de Extracción del Corpus Legal de IA — Tarea C (Fase 1)

**Fecha:** 2026-04-15
**Estado:** Plan aprobado, implementación pendiente
**Dependencia previa:** Cierre de Tarea A (confounders) + Tarea B (recodificación)
**Tiempo estimado total:** 25-35 horas
**Alcance:** 86 países del estudio — solo leyes y estrategias nacionales VIGENTES, fuentes primarias oficiales

---

## 1. Propósito y motivación

La Tarea C cierra la Fase 1 del proyecto con la construcción de un **corpus de documentos legales y
estrategias nacionales de IA**, uno por país cuando exista. Este corpus alimentará la Fase 5 (NLP)
del proyecto para responder la pregunta Q4:

> *¿Qué temáticas regulatorias de IA dominan en qué países, y cómo se agrupan los países
> según el contenido semántico de su regulación?*

La auditoría cientifica (`docs/feedback-llm-14-04.md`, Problema #7) diagnosticó que el corpus
actual (~20 documentos mixtos) es insuficiente para producir clustering temático estable. La
Tarea C eleva el corpus a **~75 documentos vigentes** obtenidos **directamente de fuentes
primarias oficiales de cada gobierno**, con traducción unificada a inglés y metadata rica.

---

## 2. Alcance y restricciones (decisiones del diseño)

### 2.1. Alcance temporal
- **Incluir:** documentos VIGENTES (en vigor) al 2026-04-15.
- **Excluir:** borradores sin promulgar, proyectos en trámite legislativo, versiones preliminares,
  white papers no adoptados, consultas públicas cerradas sin resolucion formal.

Motivacion: la pregunta de investigacion mide el efecto de regulacion IA **vigente** sobre
ecosistemas IA actuales. Los borradores introducen ruido por dos razones:
1. Pueden no convertirse nunca en ley (ver USA Executive Order 14110, revocado 2025-01).
2. No ejercen efecto regulatorio real hasta su entrada en vigor.

### 2.2. Tipos documentales incluidos
Solo dos categorias:

| Tipo | Definicion operativa | Cobertura esperada |
|---|---|---|
| **L — Law** | Ley, reglamento, decreto o acto normativo con **fuerza legal vinculante** promulgado por autoridad competente, especifico a IA o con seccion IA explicita. | ~35 paises (binding_regulation + algunos strategy_only con leyes sectoriales IA) |
| **S — Strategy** | Plan, estrategia, politica o agenda nacional de IA adoptada formalmente por gobierno central. Documento oficial publicado por ministerio/gabinete competente. | ~75 paises (casi universal) |

Quedan **explicitamente excluidos**: D (drafts), G (guidelines blandas), W (white papers).
Esta exclusion implementa la directriz del usuario y reduce el corpus de ~100+ documentos
potenciales a ~75 documentos de calidad asegurada.

### 2.3. Fuente canonica por documento
Requisito duro: **cada documento del corpus debe provenir directamente del sitio web oficial
del gobierno emisor** (parlamento, gabinete, ministerio, boletin oficial, diario oficial,
agencia regulatoria). Los agregadores (OECD.AI, IAPP, FLI) se usan **solo como indice** para
descubrir la URL oficial, nunca como fuente del texto.

Motivacion:
- Reproducibilidad academica: el reviewer debe poder verificar la fuente en el sitio original.
- Integridad: los agregadores pueden tener versiones resumidas, traducciones no-oficiales, o
  estar desactualizados.
- Autoridad: un policy paper citado por el gobierno chileno requiere que las fuentes sean
  autoritativas, no de terceros.

### 2.4. Unidad de observacion
Una fila = un documento. Si un pais tiene multiple leyes IA vigentes (ej. China tiene 3
reglamentos distintos del CAC), cada una es una fila separada pero comparten `iso3`.

---

## 3. Definicion operativa del corpus

### 3.1. Criterios de inclusion duros
Un documento `d` entra al corpus si y solo si cumple TODOS los siguientes:

1. **Vigencia:** fecha de entrada en vigor <= 2026-04-15, sin derogacion posterior.
2. **Autoridad oficial:** publicado por organismo gubernamental central del pais (parlamento,
   presidencia, ministerio, agencia regulatoria federal). No organismos sub-nacionales salvo
   casos especificos documentados (ej. Colorado AI Act para USA por ausencia de ley federal).
3. **Especificidad IA:** cumple UNO de:
   - (a) Es especifico a IA: mencion en titulo y >= 80% del texto sobre sistemas IA/algoritmos.
   - (b) Es ley sectorial con **capitulo o seccion explicita** dedicada a IA (>= 5% del texto).
4. **Formato recuperable:** disponible como PDF, HTML o DOC accesible via URL publica o archivo
   descargable. No se admiten imagenes escaneadas sin OCR.
5. **Idioma identificable:** tiene un idioma primario detectable (evita multi-lingual glue docs).

### 3.2. Criterios de exclusion explicitos
- Documentos internos de una agencia sin publicacion oficial.
- Versiones consolidadas de terceros (ej. UNCTAD consolidations).
- Resumenes ejecutivos sin el texto completo.
- Documentos sub-nacionales (estados/provincias) EXCEPTO cuando el pais carece de ley federal
  (USA, Canada — documentar en metadata).
- Traducciones no-oficiales (se traduce solo en paso C.4, el original primario es el del gobierno).

### 3.3. Tratamiento de casos agregados
- **Bloque EU (27 paises):** se incluye **un solo documento** canonico = Reglamento (UE)
  2024/1689 (EU AI Act), publicado en Diario Oficial de la UE, citado como EU-supranational.
  Cada miembro EU ademas tiene su propia fila con su ESTRATEGIA nacional (tipo S).
  - Rationale: evita el problema #3 de la auditoria (contaminacion de varianza por replicacion).
  - Implementacion: manifiesto tiene `iso3=EUU` para el AI Act + filas individuales S por miembro.
- **Estados Unidos:** ausencia de ley federal al 2026-04. Se incluye NIST AI RMF (soft-law vinculante
  para agencias federales, publicado por NIST como guidance oficial pero con status "effectively
  binding" en el ecosistema tech USA). Colorado AI Act (2024) se incluye por ser la primera ley
  estatal binding con alcance significativo; se documenta como excepcion sub-nacional.
- **China:** tres reglamentos del Cyberspace Administration (CAC) son leyes vigentes
  independientes con fechas de promulgacion distintas. Tres filas separadas con `iso3=CHN`.

---

## 4. Estrategia de fuentes — jerarquia y protocolo

### 4.1. Jerarquia de tres capas

| Capa | Rol | Uso |
|---|---|---|
| **Capa 1 — Indice** | Descubrir que documentos existen y donde | OECD.AI, IAPP, FLI, Library of Congress |
| **Capa 2 — Verificacion** | Confirmar vigencia, fecha, autoridad emisora | EU EUR-Lex, national legal databases |
| **Capa 3 — Descarga** | Obtener el PDF/HTML final del corpus | Sitio oficial del gobierno emisor |

Un documento NO entra al corpus hasta que se obtiene Capa 3.

### 4.2. Capa 1 — Indices globales

Estas fuentes no se citan en el paper; son herramientas de descubrimiento.

- **OECD.AI Policy Observatory** — https://oecd.ai/en/dashboards/policy-initiatives
  - Filtrable por pais e instrumento. API JSON publica.
  - Mantenido por OECD, ~800+ policy initiatives indexadas.
  - **Uso:** extraccion programatica de URL oficiales (campo `source_url`).

- **IAPP Global AI Law and Policy Tracker** — https://iapp.org/resources/article/global-ai-legislation-tracker/
  - Tabla actualizada mensualmente por IAPP con leyes IA por jurisdiccion.
  - PDF ya descargado en `docs/IAPP-global_ai_law_policy_tracker.pdf`.
  - **Uso:** cross-check de nuestra codificacion X1 + links a leyes.

- **FLI AI Policy Database** — https://futureoflife.org/ai-policy/
  - Mantenido por Future of Life Institute, enfasis en leyes de "safety".
  - **Uso:** fill-gap para paises con cobertura debil en OECD/IAPP.

- **Library of Congress — Regulation of AI in Selected Jurisdictions** — https://tile.loc.gov/storage-services/service/ll/llglrd/2019668143/2019668143.pdf y actualizaciones
  - Reportes academicos de la LoC con citas exactas de leyes en ~20 paises.
  - **Uso:** referencia canonica para paises sin cobertura OECD (Saudi, Iran, etc.).

- **GPAI — Global Partnership on AI** — https://gpai.ai
  - Repositorio de iniciativas en paises miembros GPAI.
  - **Uso:** complementario a OECD.AI.

### 4.3. Capa 2 — Verificacion juridica

Antes de descargar el texto, se confirma:
- Estatus legal actual (vigente / derogado / modificado).
- Fecha exacta de entrada en vigor.
- Numero oficial de la norma.
- Autoridad emisora.

Bases de datos juridicas usadas:

- **EUR-Lex** (EU + miembros): https://eur-lex.europa.eu — sistema oficial UE.
- **LegiFrance** (Francia): https://www.legifrance.gouv.fr
- **Gesetze-im-Internet** (Alemania): https://www.gesetze-im-internet.de
- **BOE** (Espana): https://www.boe.es
- **National Law Information Center** (Korea): https://www.law.go.kr
- **e-Gov** (Japon): https://elaws.e-gov.go.jp
- **Diario Oficial de la Federacion** (Mexico): https://dof.gob.mx
- **Diario Oficial da Uniao** (Brasil): https://www.in.gov.br
- **Diario Oficial** (Chile): https://www.diariooficial.interior.gob.cl
- **Legislation.gov.uk** (UK): https://www.legislation.gov.uk
- **Federal Register / Code of Federal Regulations** (USA): https://www.federalregister.gov
- **Canada Gazette**: https://gazette.gc.ca

### 4.4. Capa 3 — Descarga de fuente primaria

La URL final debe ser del dominio gubernamental oficial. Se rechaza:
- Dominios .com, .org, .net salvo excepciones documentadas.
- Mirrors academicos.
- Archive.org solo si el sitio oficial caducado tiene snapshot verificable (ultimo recurso).

Lista blanca preliminar de dominios aceptables (indicativa, no exhaustiva):
```
.gov, .gov.xx, .gouv.xx, .gob.xx, .govt.xx, .mil, .int,
europa.eu, eur-lex.europa.eu,
bund.de, bmj.de, bmi.de, bmwk.de (Alemania),
legifrance.gouv.fr, gouvernement.fr (Francia),
*.cn (sitios .gov.cn, CAC, MIIT),
*.gov.kr, msit.go.kr (Korea),
presidencia.gob.*, diputados.gob.*, senado.gob.* (LATAM),
gov.uk, ico.org.uk, aisi.gov.uk (UK),
etc.
```

---

## 5. Registro de fuentes primarias por pais

A continuacion, las fuentes primarias identificadas para cada pais de la muestra. La columna
"URL oficial" es el dominio raiz desde donde se debe partir la busqueda/scraping.

### 5.1. Union Europea y miembros (27 paises + EU supranacional)

Un documento L supranacional + 27 filas S (estrategias nacionales de IA).

| iso3 | Documento L | Documento S (estrategia) | URL oficial |
|---|---|---|---|
| EUU | **EU AI Act — Regulamento (UE) 2024/1689** (L) | EU Coordinated Plan on AI 2021 (S) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj |
| AUT | hereda EU AI Act | AIM AT 2030 (Artificial Intelligence Mission Austria) | https://www.bmk.gv.at |
| BEL | hereda EU AI Act | AI 4 Belgium | https://ai4belgium.be |
| BGR | hereda EU AI Act | Concept for AI Development in Bulgaria | https://www.mtc.government.bg |
| CYP | hereda EU AI Act | National AI Strategy of Cyprus | https://www.mof.gov.cy |
| CZE | hereda EU AI Act | National AI Strategy CR | https://www.mpo.cz |
| DEU | hereda EU AI Act | KI-Strategie Deutschland 2018 (actualizada 2020) | https://www.ki-strategie-deutschland.de |
| DNK | hereda EU AI Act | Denmark National Strategy for AI | https://en.digst.dk |
| ESP | hereda EU AI Act | ENIA — Estrategia Nacional de Inteligencia Artificial 2024 | https://www.mineco.gob.es |
| EST | hereda EU AI Act | Estonia Kratt AI Strategy | https://www.kratid.ee |
| FIN | hereda EU AI Act | Artificial Intelligence 4.0 Programme | https://tem.fi |
| FRA | hereda EU AI Act | Strategie Nationale pour l'IA | https://www.economie.gouv.fr |
| GRC | hereda EU AI Act | National Strategy for AI (Bible of Digital Transformation 2020-2025) | https://mindigital.gr |
| HRV | hereda EU AI Act | Strategija razvoja umjetne inteligencije | https://mingo.gov.hr |
| HUN | hereda EU AI Act | Artificial Intelligence Strategy of Hungary 2020-2030 | https://digitalisjoletprogram.hu |
| IRL | hereda EU AI Act | AI — Here for Good National AI Strategy | https://www.enterprise.gov.ie |
| ITA | hereda EU AI Act | Strategia italiana per l'intelligenza artificiale 2024-2026 | https://www.agid.gov.it |
| LTU | hereda EU AI Act | Lithuanian AI Strategy | https://eimin.lrv.lt |
| LUX | hereda EU AI Act | AI: a strategic vision for Luxembourg | https://digital-luxembourg.public.lu |
| LVA | hereda EU AI Act | Latvian AI Strategy | https://www.varam.gov.lv |
| MLT | hereda EU AI Act | Malta AI Strategy and Vision 2030 | https://malta.ai |
| NLD | hereda EU AI Act | Strategisch Actieplan voor AI | https://www.rijksoverheid.nl |
| POL | hereda EU AI Act | Polityka dla rozwoju sztucznej inteligencji w Polsce | https://www.gov.pl |
| PRT | hereda EU AI Act | AI Portugal 2030 | https://www.incode2030.gov.pt |
| ROU | hereda EU AI Act | National Strategy in the field of AI 2024-2027 | https://www.adr.gov.ro |
| SVK | hereda EU AI Act | Action Plan for Digital Transformation of Slovakia 2019-2022 (AI cap) | https://mirri.gov.sk |
| SVN | hereda EU AI Act | National Program for AI 2025 (NpUI) | https://www.gov.si |
| SWE | hereda EU AI Act | National approach for AI (Swedish Government) | https://www.regeringen.se |

**Nota de implementacion:** para EU miembros, el campo `has_binding_ai_law=1` en el manifiesto,
pero el texto L descargado apunta al EU AI Act en EUR-Lex. El texto S es la estrategia
nacional especifica. Esto preserva la trazabilidad del bloque sin contaminar la varianza.

### 5.2. EEA + paises europeos no-UE

| iso3 | Documento L | Documento S | URL oficial |
|---|---|---|---|
| GBR | AI Regulation White Paper implementation (soft-binding sectoral) | National AI Strategy 2021 | https://www.gov.uk |
| NOR | — | National Strategy for AI (2020) | https://www.regjeringen.no |
| ISL | — | Iceland AI Policy (2021) | https://www.stjornarradid.is |
| CHE | — | Swiss AI Strategy guidance | https://www.sbfi.admin.ch |
| SRB | — | Strategy for the Development of AI 2020-2025 | https://www.srbija.gov.rs |
| UKR | — | Concept of AI Development 2021-2030 | https://www.kmu.gov.ua |
| BLR | — | National AI Strategy (limited) | https://pravo.by |

### 5.3. Norteamerica

| iso3 | Documento L | Documento S | URL oficial |
|---|---|---|---|
| USA | NIST AI RMF 1.0 (NIST 100-1) + Colorado AI Act (SB 24-205) | National AI R&D Strategic Plan 2023 Update | https://www.nist.gov + https://leg.colorado.gov |
| CAN | Directive on Automated Decision-Making (Treasury Board) | Pan-Canadian AI Strategy (Phase 2) | https://www.canada.ca |
| MEX | — | Agenda Nacional Mexicana de IA (2020) | https://www.gob.mx |

### 5.4. Latinoamerica y Caribe

| iso3 | Documento L | Documento S | URL oficial |
|---|---|---|---|
| ARG | Disposicion 2/2023 ADM (principios para IA etica en admin publica) | Plan Nacional de IA 2030 | https://www.argentina.gob.ar |
| BRA | Resolucao ANPD sobre uso de IA (2024) | EBIA — Estrategia Brasileira de IA | https://www.gov.br/mcti |
| CHL | — | Politica Nacional de Inteligencia Artificial (2021) + Plan de Accion | https://minciencia.gob.cl |
| COL | CONPES 3975 (politica de IA) | Marco Etico para IA en Colombia | https://www.dnp.gov.co |
| CRI | — | Estrategia Nacional de IA Costa Rica 2024-2027 | https://www.micitt.go.cr |
| ECU | — | Agenda Digital del Ecuador 2022-2025 (cap IA) | https://www.telecomunicaciones.gob.ec |
| PER | Ley 31814 (Ley que promueve el uso de la IA, 2023) | Estrategia Nacional de IA 2021-2026 | https://www.gob.pe |
| PAN | — | Agenda Digital de Panama 2025-2030 (cap IA) | https://innovacion.gob.pa |
| URY | Estrategia de IA para el Gobierno Digital (AGESIC, 2020) | Estrategia Nacional de IA | https://www.gub.uy |
| BLZ | — | National ICT / AI component (limitado) | https://www.mpsg.gov.bz |
| BRB | — | Barbados Digital Transformation Strategy | https://www.gov.bb |

### 5.5. Asia-Pacifico

| iso3 | Documento L | Documento S | URL oficial |
|---|---|---|---|
| CHN | (1) Generative AI Measures 2023 (2) Algorithmic Recommendations 2021 (3) Deep Synthesis 2022 — todos CAC | Next Generation AI Development Plan 2017 (State Council) | http://www.cac.gov.cn + http://www.gov.cn |
| JPN | — (AI Act draft pendiente) | AI Strategy 2022 + Social Principles of Human-Centric AI | https://www.cao.go.jp + https://www.meti.go.jp |
| KOR | AI Framework Act (Ley 20766, promulgada 2024-12, vigente 2026-01) | National AI Strategy 2019 | https://www.msit.go.kr + https://www.law.go.kr |
| SGP | — | National AI Strategy 2.0 (2023) + AI Verify (principles) | https://www.smartnation.gov.sg |
| AUS | — | Australia's AI Action Plan 2021 | https://www.industry.gov.au |
| NZL | — | AI Strategy (AI Forum NZ government-endorsed) | https://www.mbie.govt.nz |
| IND | — | National Strategy for AI (NITI Aayog 2018) + India AI Mission 2024 | https://www.niti.gov.in + https://indiaai.gov.in |
| IDN | — | National Strategy for AI 2020-2045 (Stranas KA) | https://ai-innovation.id |
| MYS | — | AI Roadmap 2021-2025 | https://mosti.gov.my |
| PHL | — | National AI Strategy Roadmap | https://dti.gov.ph |
| THA | — | Thailand National AI Strategy and Action Plan 2022-2027 | https://ai.in.th |
| VNM | — | National Strategy on R&D and Application of AI to 2030 | https://chinhphu.vn |
| BGD | — | National Strategy for AI 2020-2025 (draft formalizado) | https://ictd.gov.bd |
| PAK | — | National AI Policy 2023 | https://moitt.gov.pk |
| LKA | — | National AI Strategy (MoT) | https://www.mot.gov.lk |
| MNG | — | National Program on AI | https://mdigital.gov.mn |
| KAZ | — | Concept of AI Development in Kazakhstan 2024-2029 | https://www.gov.kz |
| TWN | — | Taiwan AI Action Plan 2.0 | https://www.ey.gov.tw |

### 5.6. Medio Oriente y Norte de Africa (MENA)

| iso3 | Documento L | Documento S | URL oficial |
|---|---|---|---|
| ARE | Dubai AI Principles + UAE AI Code (sector-specific binding docs) | UAE Strategy for AI 2031 | https://ai.gov.ae |
| SAU | — | Saudi Data and AI Authority Strategy (SDAIA) | https://sdaia.gov.sa |
| ISR | — | National AI Program (Innovation Authority) | https://innovationisrael.org.il |
| JOR | — | Jordan National AI Strategy and Roadmap 2023-2027 | https://www.modee.gov.jo |
| LBN | — | Lebanon Digital Transformation Strategy (cap IA) | https://www.presidency.gov.lb |
| EGY | — | Egypt National AI Strategy | https://mcit.gov.eg |
| MAR | — | Morocco Digital Strategy 2025 (cap IA) | https://www.mmsp.gov.ma |
| TUN | — | Strategie Nationale IA Tunisie | https://www.mtc.gov.tn |
| BHR | — | Bahrain National Strategy for AI | https://www.iga.gov.bh |
| TUR | — | National AI Strategy 2021-2025 | https://cbddo.gov.tr |

### 5.7. Africa Sub-Sahariana

| iso3 | Documento L | Documento S | URL oficial |
|---|---|---|---|
| ZAF | — | South Africa National AI Plan (Presidential Commission) | https://www.gov.za |
| NGA | — | National AI Strategy (2024) | https://fmcide.gov.ng |
| KEN | — | Kenya National AI Strategy (draft pendiente; descartado) | https://www.ict.go.ke |
| GHA | — | Ghana National AI Strategy | https://moc.gov.gh |
| UGA | — | Uganda National AI Strategy (pendiente) | https://ict.go.ug |
| CMR | — | Cameroon Digital Strategic Plan 2020 (cap IA limitado) | https://www.minpostel.gov.cm |
| MUS | — | Mauritius AI Strategy 2018 | https://mitci.govmu.org |
| SYC | — | Seychelles Digital Strategy (cap IA) | https://www.ict.gov.sc |

### 5.8. Otros

| iso3 | Documento L | Documento S | URL oficial |
|---|---|---|---|
| RUS | Executive Order on AI Development (Presidencial, 2019) + strategy updates | National Strategy for AI Development to 2030 | http://government.ru + http://kremlin.ru |
| ARM | — | Armenia Digital Transformation Strategy (cap IA) | https://www.hti.am |

**Nota:** Las estimaciones de disponibilidad son al 2026-04. Si un pais aparece con `—` en L no
significa que nunca legislara, sino que al 2026-04-15 no hay ley IA vigente identificable.

**Resumen de cobertura proyectada del corpus:**
- Documentos L: ~35-40 (EU AI Act cuenta como 1; tres CAC China cuentan como 3)
- Documentos S: ~75 (uno por pais con estrategia formal)
- Total del corpus: ~110 documentos, pero tras deduplicacion (EU herencia) efectivamente
  ~75-80 documentos textuales unicos.

---

## 6. Infraestructura tecnica del pipeline

### 6.1. Manifiesto maestro

Archivo: `data/raw/AI_Corpus/manifest.csv`
Construccion: manual inicial (~8h de curacion); luego update programatico de `fetch_status`.

Columnas obligatorias:
```
doc_id              : str   # hash-estable: <iso3>_<type>_<yyyy>_<slug>
iso3                : str   # ISO-3 del pais (EUU para UE supranacional)
country_name        : str
doc_type            : L|S
title_original      : str   # titulo en idioma original
title_english       : str   # traduccion manual del titulo
authority           : str   # organismo emisor (ministerio, parlamento)
year_enacted        : int   # ano de promulgacion o publicacion oficial
in_force_date       : date  # fecha de entrada en vigor
status              : in_force | repealed | superseded
canonical_url       : str   # URL oficial final del documento
source_repo         : str   # fuente de descubrimiento (OECD.AI | IAPP | FLI | manual)
language_original   : str   # ISO 639-1 (es, en, zh, ko, ja, ar, pt, fr, de, ...)
fetch_status        : pending | ok | failed | redirect | dead_url
fetch_date          : date
file_format         : pdf | html | docx
file_path_raw       : str   # path relativo al archivo cacheado
sha256              : str   # checksum del archivo descargado
word_count          : int   # post-parse
inclusion_rationale : str   # por que este doc entra al corpus
notes               : str
```

### 6.2. Scripts del pipeline

Tres scripts nuevos en `src/`:

#### `src/fetch_ai_corpus.py`
- Lee `manifest.csv`, itera por filas con `fetch_status=pending`.
- Descarga cada URL con `requests` (timeout 60s, retry 3 con backoff exponencial).
- Respeta `robots.txt` via `urllib.robotparser`.
- User-Agent identificado: `LeyIA-DataScience-Research/1.0 (contact: brunel.fr99@gmail.com)`.
- Output: `data/raw/AI_Corpus/{iso3}/{doc_id}.{pdf,html,docx}`.
- Calcula SHA-256, actualiza manifiesto.
- Logs estructurados a `data/raw/AI_Corpus/fetch.log`.
- **Rate limiting:** 1 request/3s por dominio para evitar abuso a sitios gubernamentales.

#### `src/parse_ai_corpus.py`
- Extrae texto desde PDF/HTML/DOCX:
  - PDF: `pdfplumber` (primero) → `pypdf` (fallback) → OCR con `pytesseract` solo si el PDF
    es escaneado (detectado por ratio texto/imagenes).
  - HTML: `BeautifulSoup` con extractor de main-content (trafilatura como fallback).
  - DOCX: `python-docx`.
- Limpieza basica:
  - Remover headers/footers recurrentes (regex de patrones).
  - Normalizar whitespace, unicode NFC.
  - Detectar idioma con `langdetect` → cross-check con `language_original` del manifest.
  - Contar palabras, guardar `word_count`.
- Output: `data/interim/ai_corpus_text/{iso3}/{doc_id}.txt`.
- **Validacion dura:** rechazar documentos con <500 palabras o con ratio de caracteres no
  imprimibles > 5% (PDFs corruptos).

#### `src/translate_ai_corpus.py`
- Traduce cada `.txt` original a ingles usando DeepL API Pro.
- Preserva la estructura de parrafos (traduccion por chunks de ~5000 caracteres).
- Output: `data/interim/ai_corpus_en/{iso3}/{doc_id}.txt`.
- Cache-aware: si `sha256(original) + lang_target` ya existe en cache, no re-traduce.
- Costo estimado: 80 docs × 15k palabras avg × $20/1M caracteres = **~$70 one-time**.
- Alternativa gratuita (fallback): `transformers` con modelos Helsinki-NLP `opus-mt-{src}-en`
  via HuggingFace. Menor calidad pero sin costo.

### 6.3. Estructura de directorios final

```
data/
  raw/
    AI_Corpus/
      manifest.csv                       (74+ filas)
      fetch.log
      {iso3}/
        {doc_id}.pdf
        {doc_id}.html
        ...
  interim/
    ai_corpus_text/
      {iso3}/{doc_id}.txt                (texto original limpio)
    ai_corpus_en/
      {iso3}/{doc_id}.txt                (traduccion EN)
    ai_corpus_embeddings.parquet         (matriz 80x384)
    ai_corpus_coverage.csv               (auditoria)

src/
  fetch_ai_corpus.py
  parse_ai_corpus.py
  translate_ai_corpus.py
  audit_ai_corpus.py

info_data/
  METODOLOGIA_AI_CORPUS.md               (metodologia formal)
  CORPUS_NLP_COBERTURA.md                (reporte final)
```

---

## 7. Protocolo de traduccion

### 7.1. Por que traducir todo a ingles

La Fase 5 (NLP) debe comparar contenido tematico cross-country. Un vectorizador
multilingue (como `paraphrase-multilingual-mpnet-base-v2`) puede embedir textos en 50+
idiomas al mismo espacio vectorial, PERO:
- La calidad de embedding degrada en idiomas con poca data de entrenamiento (mongol,
  amharico, bengali).
- El clustering con distancias cosine se vuelve sensible a artefactos linguisticos
  (ej. chino se clusteriza con chino por estilo, no por tema).
- Los top-terms interpretables por cluster necesitan un idioma comun para que el humano
  pueda etiquetarlos.

La traduccion previa elimina estas dos fuentes de ruido a costo de introducir ruido de
traduccion (~5-10% de error semantico con DeepL). Para TF-IDF y LDA es obligatorio.
Para embeddings se puede usar dual-path (ver C.8).

### 7.2. Engine de traduccion: DeepL vs alternativas

| Opcion | Calidad | Costo | Cobertura idiomas |
|---|---|---|---|
| **DeepL API Pro** | Alta (estado del arte) | ~$25/mes o pay-as-you-go | 31 idiomas (incluye zh, ko, ja, ar, ru, pt, es, fr, de) |
| Google Cloud Translation | Media-alta | $20/1M chars | 133 idiomas |
| Helsinki-NLP opus-mt | Media | Gratis | 200+ pares via HuggingFace |
| GPT-4 / Claude translation | Muy alta | Alto por costo LLM | Todos |

**Recomendacion:** DeepL Pro por balance calidad-costo. Total estimado $50-100 one-time para
el corpus completo. Fallback a Helsinki-NLP si el usuario veta el gasto.

### 7.3. Validacion de traducciones

- Muestra aleatoria 10% del corpus → back-translation al idioma original con el mismo motor.
- Calcular BLEU entre original y back-translation; si BLEU < 0.6 marcar para revision manual.
- Spot-check humano: el usuario (hispanoparlante) valida traducciones es→en personalmente.
  Los otros idiomas dependen del proxy de BLEU.

### 7.4. Preservacion del texto original

Por cada `{doc_id}.txt` en ingles, se preserva `{doc_id}.txt` original en
`data/interim/ai_corpus_text/`. Auditabilidad y reproducibilidad.

---

## 8. Auditoria, cobertura, y criterios de exito

### 8.1. Quality gates antes de Fase 5

Antes de declarar la Tarea C cerrada, se deben cumplir TODAS las siguientes condiciones
(reportadas automaticamente por `src/audit_ai_corpus.py`):

| Gate | Criterio | Rationale |
|---|---|---|
| G1 — Tamaño | Corpus total >= 75 documentos | Minimo para estabilidad de clustering |
| G2 — binding coverage | >= 90% de los 32 paises `binding_regulation` con al menos 1 doc L o S | El grupo tratamiento no puede estar subrepresentado |
| G3 — strategy coverage | >= 85% de los 39 paises `strategy_only` con al menos 1 doc S | El grupo comparador mayoritario debe estar robusto |
| G4 — fetch integrity | 0 documentos con `fetch_status=failed`. Todos los pending resueltos. | Sin huecos no documentados |
| G5 — idioma | Al menos 10 idiomas distintos representados | Heterogeneidad minima |
| G6 — length | Media de word_count entre 2000 y 50000 por doc | Filtra documentos defectuosos/boilerplate |
| G7 — SHA uniqueness | Sin colisiones SHA-256 (no duplicados exactos) | Deduplicacion robusta |
| G8 — translation coverage | 100% de los docs con texto original tambien tienen traduccion EN | Corpus analizable |

### 8.2. Reporte de cobertura

Archivo: `info_data/CORPUS_NLP_COBERTURA.md`, generado automaticamente tras correr audit.

Secciones:
- Tabla pais × tipo (L/S) con links al documento
- Distribucion de idiomas originales
- Distribucion de `year_enacted`
- Histograma de word_count
- Matriz regulatory_status_group × cobertura
- Lista de paises sin ningun documento (declarar exclusion de Fase 5)

### 8.3. Manejo de paises sin documento

Para paises donde no existe ningun documento vigente (al 2026-04) que cumpla los criterios:
- Se documenta en CORPUS_NLP_COBERTURA.md con razon.
- El pais se excluye del analisis Fase 5 pero permanece en Fases 2-4.
- Campo `has_corpus_doc=0` agregado a `sample_ready_cross_section.csv`.

Paises en riesgo de quedar sin corpus (codificados `no_framework` + paises pequeños):
BLZ, BRB, CMR, SYC. Se documenta la exclusion si ocurre.

---

## 9. Desafios tecnicos anticipados y mitigaciones

### 9.1. Geo-restricciones y acceso

**Problema:** algunos sitios gubernamentales restringen o degradan trafico desde fuera del pais.
Especialmente conocido: sitios `.gov.cn` pueden ser lentos/caidos desde LATAM.

**Mitigacion:**
- Usar Archive.org Wayback Machine como fallback documentado:
  `https://web.archive.org/web/YYYY*/URL_original`
- Proxy residencial solo si el documento es critico y no hay mirror academico.
- Documentar en `notes` del manifiesto cuando se usa fallback.

### 9.2. Documentos solo disponibles en formato imagen (PDF escaneado)

**Problema:** paises con sistemas legales menos digitalizados publican leyes en PDF escaneado.
Casos potenciales: CMR, LBN, UGA, algunos docs historicos de RUS.

**Mitigacion:**
- Deteccion automatica en `parse_ai_corpus.py`: si pdfplumber extrae <100 palabras de un PDF
  >10 paginas, se considera escaneado.
- OCR con Tesseract + idioma especifico (`-l ara+eng` para LBN, etc.).
- Quality check: confianza OCR >= 85%, si no marcar para recodificacion manual.

### 9.3. Idiomas de alfabetos no-latinos

**Problema:** chino, japones, coreano, arabe, ruso, tailandes requieren manejo cuidadoso
de encoding y tokenizacion.

**Mitigacion:**
- Encoding: forzar UTF-8 en todo el pipeline; detectar con `chardet` como sanity check.
- Para tokenizacion previa (pre-traduccion): no se requiere; DeepL maneja la segmentacion.
- Post-traduccion (EN): tokenizacion estandar con spaCy `en_core_web_sm`.

### 9.4. Redireccciones y URLs inestables

**Problema:** sitios gubernamentales cambian su estructura URL frecuentemente. Lo que hoy
esta en `/ai-strategy.pdf` mañana esta en `/nuevo-sitio/ia-estrategia-2024.pdf`.

**Mitigacion:**
- `requests.get(..., allow_redirects=True, timeout=60)` con logging de la URL final.
- Si el manifest tiene una URL canonica pero el fetch la redirige a otra con contenido
  diferente (verificado por SHA post-descarga), marcar para revision manual.
- Re-auditoria programada cada 6 meses (script separado `src/revalidate_urls.py`) para
  detectar `dead_url` y actualizar el manifiesto.

### 9.5. Documentos oficiales con versiones consolidadas vs originales

**Problema:** muchos parlamentos publican tanto la ley original como versiones consolidadas
(con todas las enmiendas). Cual usar?

**Decision:** preferir la **version consolidada vigente** al 2026-04 cuando exista. Es la
que refleja el estado de derecho actual. Documentar la fuente exacta en `canonical_url`.

### 9.6. Paywalls y login requirements

**Problema:** algunos sitios gubernamentales sofisticados (ej. algunos PDF en gov.uk legacy)
requieren login o tienen paywalls academicos.

**Mitigacion:**
- Lista de fuentes con paywall debe ser 0 para entrar al corpus (criterio de inclusion).
- Si un documento solo esta detras de paywall, se escala a la biblioteca academica o se
  excluye.

### 9.7. Riesgo de drift temporal durante la construccion del corpus

**Problema:** si la construccion del corpus toma 2-3 semanas, documentos pueden cambiar de
status (nuevas leyes aprobadas, existentes derogadas).

**Mitigacion:**
- Fecha de corte unica: 2026-04-15 (hoy). Todos los documentos reflejan el estado vigente
  a esa fecha. Documentos aprobados despues quedan fuera del analisis pero se anotan para
  futuras versiones.
- Re-snapshot recomendado si publicacion del paper se retrasa mas de 6 meses.

---

## 10. Caso especial: tratamiento del bloque EU

El problema #3 de la auditoria (contaminacion por replicacion EU) requiere tratamiento
especifico en la construccion del corpus:

### 10.1. Corpus-level: una sola fila L para EU
- `iso3 = EUU`, `doc_type = L`, fila unica con texto completo del EU AI Act.
- Esta fila entra al analisis NLP como un documento mas.
- Los 27 miembros EU NO tienen entrada L propia, pero heredan el contenido via dummy
  `eu_ai_act_inherited=1` en la metadata.

### 10.2. Dataset-level: dummy en sample_ready
- Se agrega columna `eu_ai_act_inherited` en `sample_ready_cross_section.csv`:
  - 1 si el pais es miembro EU/EEA y hereda el EU AI Act.
  - 0 en caso contrario.
- Este dummy se usa en Fase 4 como efecto fijo para absorber el shock comun.

### 10.3. Analisis tematico dual
Cuando se corra el clustering NLP en Fase 5:
- **Analisis A (todos los documentos):** incluye EU AI Act como doc individual.
- **Analisis B (sin EU):** excluye la fila EUU. Mide heterogeneidad tematica entre paises
  que legislaron o estrategizaron independientemente.

Las dos versiones se reportan en el paper final.

---

## 11. Caso especial: tratamiento de paises fragmentados (USA, China)

### 11.1. USA — ausencia de ley federal
- **Doc L1:** NIST AI Risk Management Framework 1.0 (NIST AI 100-1, enero 2023).
  Fuente: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
  Estatus: guidance federal oficial, "effectively binding" para contratistas federales
  via Executive directives posteriores.
- **Doc L2 (sub-nacional documentado):** Colorado AI Act (SB 24-205, mayo 2024).
  Fuente: https://leg.colorado.gov/bills/sb24-205
  Rationale: primera ley estatal binding con alcance comprehensivo en USA; importante
  en ausencia federal.
- **Doc S:** National AI R&D Strategic Plan (2023 Update).
  Fuente: https://www.whitehouse.gov/wp-content/uploads/2023/05/National-AI-Research-and-Development-Strategic-Plan-2023-Update.pdf

### 11.2. China — tres reglamentos del CAC
- **Doc L1:** Interim Measures for the Management of Generative AI Services (2023).
  Fuente: http://www.cac.gov.cn (publicacion original julio 2023).
- **Doc L2:** Provisions on the Management of Algorithmic Recommendations of Internet
  Information Services (2021).
  Fuente: http://www.cac.gov.cn
- **Doc L3:** Provisions on the Administration of Deep Synthesis Internet Information
  Services (2022).
  Fuente: http://www.cac.gov.cn
- **Doc S:** Next Generation AI Development Plan (State Council, 2017, vigente).
  Fuente: http://www.gov.cn/zhengce

Cada uno es una fila separada con `iso3=CHN`. Esto incrementa el peso analitico de China
en el corpus temático (4 docs vs 1 de otros paises), lo cual es defendible dado que China
ha legislado mas que cualquier otro pais individual en el universo del estudio.

### 11.3. Otros paises con multiples documentos
- **KOR:** 1 doc L (AI Framework Act) + 1 doc S (National AI Strategy) = 2 filas.
- **ARE:** multiples iniciativas pero se consolidan en "UAE AI Strategy 2031" (S) +
  "Dubai AI Principles" (L sub-nacional con alcance significativo).
- **RUS:** Executive Order (L) + National Strategy (S) = 2 filas.

---

## 12. Entregables y criterios de cierre

Al cerrar la Tarea C (antes de avanzar a Fase 2 o Fase 5):

**Archivos creados:**
- [ ] `data/raw/AI_Corpus/manifest.csv` (75+ filas validadas)
- [ ] `data/raw/AI_Corpus/{iso3}/*.{pdf,html,docx}` (archivos cacheados)
- [ ] `data/raw/AI_Corpus/fetch.log`
- [ ] `data/interim/ai_corpus_text/{iso3}/*.txt`
- [ ] `data/interim/ai_corpus_en/{iso3}/*.txt`
- [ ] `src/fetch_ai_corpus.py`
- [ ] `src/parse_ai_corpus.py`
- [ ] `src/translate_ai_corpus.py`
- [ ] `src/audit_ai_corpus.py`
- [ ] `info_data/METODOLOGIA_AI_CORPUS.md`
- [ ] `info_data/CORPUS_NLP_COBERTURA.md`

**Documentacion actualizada:**
- [ ] `info_data/DATA_DECISIONS_LOG.md` con entrada D-017 (Construccion corpus NLP Tarea C)
- [ ] `info_data/ETL_RUNBOOK.md` con paso 4 (NLP corpus)
- [ ] `info_data/GUIA_VARIABLES_ESTUDIO_ETL.md` con variables derivadas del NLP

**Auditoria aprobada:**
- [ ] Los 8 quality gates (G1-G8) pasados.
- [ ] Reporte de cobertura publicado.

---

## 13. Cronograma sugerido

| Bloque | Actividad | Horas | Dependencias |
|---|---|---|---|
| C.0 | Revision y validacion del manifiesto inicial (86 paises) | 8h | — |
| C.1 | Implementacion de `fetch_ai_corpus.py` | 3h | C.0 |
| C.2 | Ejecucion de fetch (3-5 dias calendario con rate limiting) | 2h activas | C.1 |
| C.3 | Implementacion de `parse_ai_corpus.py` | 3h | C.2 parcial |
| C.4 | Parse de todos los documentos + resolucion OCR | 2h | C.3 |
| C.5 | Implementacion de `translate_ai_corpus.py` + DeepL setup | 2h | — |
| C.6 | Ejecucion de traduccion | 1h activa + 4h API | C.4, C.5 |
| C.7 | Implementacion de `audit_ai_corpus.py` | 2h | — |
| C.8 | Validacion, revision de gaps, re-fetch de fallas | 5h | C.7 |
| C.9 | Documentacion (METODOLOGIA + COBERTURA) | 3h | C.8 |
| **TOTAL** | | **~30h** | |

---

## 14. Decisiones de diseño abiertas (para confirmar con el usuario)

1. **Motor de traduccion:** DeepL Pro (~$70) vs Helsinki-NLP gratis. Recomendacion: DeepL.
2. **Tratamiento de versiones consolidadas:** priorizar siempre la consolidada vigente. Confirmar.
3. **Documentos sub-nacionales:** solo cuando el pais carezca de ley federal (USA, Canada).
   Confirmar excepcion de Colorado AI Act.
4. **Extension del corpus a paises del grupo `no_framework`:** solo si tienen estrategia S
   documentada. Caso a caso.
5. **Manejo de textos en imagenes escaneadas:** OCR con Tesseract o exclusion. Recomendacion:
   OCR con quality check >= 85%.
6. **Re-validacion periodica:** cronograma de 6 meses para detectar URL rot. Confirmar.

---

## 15. Integracion con el pipeline existente

La Tarea C produce inputs para Fase 5 pero NO modifica `sample_ready_cross_section.csv`
directamente. La integracion con el dataset principal ocurre en Fase 5 via:
- `has_corpus_doc` (0/1): columna agregada post-Tarea C.
- `num_corpus_docs` (int): numero de documentos en corpus para ese pais.
- `corpus_primary_lang` (str): idioma principal del doc mas importante.

La trazabilidad desde el manifiesto hasta el dataset final se documenta en el campo
`doc_id` del manifiesto, que es estable y referenciable en el paper.

---

## 16. Riesgos residuales y asunciones

1. **Asuncion:** los gobiernos mantendran sus URLs oficiales accesibles al menos durante
   la construccion del corpus. Riesgo: mitigado por fetching en batch y archive.org fallback.

2. **Asuncion:** DeepL produce traducciones de calidad academica para documentos legales.
   Riesgo: algunos documentos muy tecnicos pueden requerir revision humana. Buffer: 10% del
   corpus en validacion manual.

3. **Asuncion:** el corpus final N=75 es suficiente para clustering estable.
   Riesgo: si el Silhouette score < 0.3 en Fase 5, podriamos necesitar ampliar a 100+ docs
   con guidelines blandas. Plan B: reabrir la tarea si Fase 5 falla.

4. **Asuncion:** los documentos S (estrategias) son comparables a L (leyes) en contenido
   tematico.
   Riesgo: estrategias pueden ser mas aspiracionales/programaticas mientras leyes son mas
   prescriptivas. Mitigacion: analisis separado por tipo en Fase 5 + analisis combinado.

---

## 17. Referencias metodologicas

- Auditoria cientifica del proyecto: `docs/feedback-llm-14-04.md` (Problema #7).
- Metodologia del paper: `context_llm/guia_metodologia.md`.
- Decisiones de variables: `info_data/GUIA_VARIABLES_ESTUDIO_ETL.md`.
- Construccion de X1 (regulatory variables): `src/build_source_masters.py::build_x1_master()`.
- Referencia academica sobre clustering de texto legal multilingue:
  Zhong et al. (2020) "How does NLP benefit legal system: A summary of legal AI".

---

**Fin del plan Tarea C.**
