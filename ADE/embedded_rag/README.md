# embedded_rag — Datos Completos para Embedding de IA Regulatoria

## Overview

Este directorio contiene **TODOS los datos analizados del proyecto** para embedding en legal-rag:
- Datos cuantitativos ADE (72 países)
- Corpus legal completo (22 países)
- **ANÁLISIS TEXTUAL COMPLETO**: SOURCES + CANDIDATES + FINDINGS

## Estructura v3.0 (FINAL)

```
embedded_rag/
├── master_index.json           # Índice maestro
├── README.md                 # Este archivo
├── [ISO3]/
│   ├── country_profile.json       # Metadata + ecosistema + controls + governance
│   ├── regulatory_framework.json # X1 regulatorio
│   ├── documents_index.json     # Índice de PDFs descargados
│   ├── legal_corpus_full.json   # Docs + metadata
│   ├── full_corpus_text.json   # SOURCES + CANDIDATES + FINDINGS (TEXTO COMPLETO)
│   ├── embedding_chunks.json   # Chunks básicos
│   ├── embedding_chunks_rich.json # Chunks RICOS con texto literal ⭐
│   └── meta_chunks.md         # Markdown para embedding
└── ...
```

## embedding_chunks_rich.json (FORMATO FINAL)

Cada país key (9 países) tiene **11-13 chunks** con **texto literal completo**:

| Chunk ID | Chunk Type | Content | Relevancia |
|---------|----------|---------|----------|
| `{ISO3}_profile` | profile | Todas las métricas del país en texto | 0.99 |
| `{ISO3}_regulatory` | regulatory | Marco regulatorio completo | 0.99 |
| `{ISO3}_doc_1` | document | Doc 1 con notes literales | 0.95 |
| `{ISO3}_doc_2` | document | Doc 2 con notes literales | 0.95 |
| ... | document | ... | 0.95 |
| `{ISO3}_sources` | sources | **TODO SOURCES.md** (citas APA) | 0.98 |
| `{ISO3}_candidates` | candidates | **TODO CANDIDATES.md** | 0.98 |
| `{ISO3}_findings` | findings | **TODO FINDINGS.md** (análisis diferencial) | 0.99 |

## Países con Análisis Completo (9 key countries)

| ISO3 | Docs | SOURCES | CANDIDATES | FINDINGS | Total Chars |
|------|------|--------|-----------|----------|------------|
| GBR | 6 | 12,506 | 9,009 | 7,829 | 29,344 |
| AUS | 7 | 12,551 | 9,595 | 9,297 | 31,443 |
| CAN | 7 | 10,267 | 19,782 | 7,000 | 37,049 |
| DEU | 8 | 15,039 | 15,079 | 6,378 | 36,496 |
| SGP | 7 | 10,898 | 22,255 | 6,645 | 39,798 |
| FRA | 5 | 11,299 | 10,274 | 6,343 | 27,916 |
| NLD | 5 | 9,754 | 9,468 | 7,594 | 26,816 |
| ESP | 5 | 10,738 | 9,722 | 6,161 | 26,621 |
| DNK | 4 | 8,115 | 10,938 | 5,506 | 24,559 |

Total texto analítico: **~280,000 caracteres** (sin repetir PDFs)

## Ejemplo: embedding_chunks_rich.json para GBR

```json
[
  {
    "chunk_id": "GBR_profile",
    "chunk_type": "profile", 
    "content": "GBR COUNTRY PROFILE:\nRegion: Europe\nOECD Member: True\n...\nAI Readiness Score: 77.75/100 (year 2025)\nAI Adoption Rate: 38.9%\n...",
    "relevance": 0.99
  },
  {
    "chunk_id": "GBR_findings", 
    "chunk_type": "findings",
    "content": "# GBR — Hallazgo Diferencial\n\n## 1. Tesis del hallazgo diferencial\n\n**Reino Unido presenta la paradoja regulatoria más notable del corpus: el país con mayor liderazgo global en seguridad IA (AISI — primer instituto estatal de seguridad IA del mundo, lanzado en Bletchley Park noviembre 2023)...**",
    "relevance": 0.99
  }
]
```

## Estadísticas Totales

- **Países procesados**: 73 (completo ADE)
- **Países con corpus legal**: 22
- **Países con análisis completo**: 9 (GBR, AUS, CAN, DEU, SGP, FRA, NLD, ESP, DNK)
- **Tamaño total**: 3.2MB
- **Chunks de embedding**: ~100 por país con corpus completo

## Uso para Ingest a legal-rag

1. **Para países key (9)**: Usar `embedding_chunks_rich.json`
   - Contiene TODO el texto analítico
   - Listo para chunking y embedding directo

2. **Para países con corpus (22)**: Usar `embedding_chunks.json`
   - Chunks estructurados con métricas

3. **Para países restantes (51)**: Usar `country_profile.json` + `regulatory_framework.json`

## Fuente de Datos

- **Datos ADE**: `/home/pablo/Research_LeyIA_DataScience/data/interim/sample_ready_cross_section.csv`
- **Corpus legal**: `/home/pablo/Research_LeyIA_DataScience/data/raw/legal_corpus/{ISO3}/`
  - manifest.csv
  - SOURCES.md (citas APA 7)
  - CANDIDATES.md (recodificación + citas)
  - FINDINGS.md (análisis diferencial)
  - PDFs descargados

---

**Generado**: 2026-04-22 | **Schema**: v3.0 (MAXIMALISTA)