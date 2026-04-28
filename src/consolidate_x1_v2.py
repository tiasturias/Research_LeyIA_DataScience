"""Consolida recodificaciones X1 propuestas por la skill `corpus-legal-ia`.

Lee los CANDIDATES.md de cada pais procesado en data/raw/legal_corpus/{ISO3}/
y extrae las variables propuestas (regulatory_intensity, thematic_coverage,
regulatory_regime_group, has_ai_law). Genera data/interim/x1_master_v2.csv
con columnas paralelas *_iapp y *_proposed.

Patron principal: bloque "Diff summary" con formato
    has_ai_law:              0 -> 0
    regulatory_intensity:    6 -> 7
    thematic_coverage:       12 -> 13
    regulatory_regime_group: strategy_only -> soft_framework

Uso:
    python src/consolidate_x1_v2.py
"""
from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
LEGAL_CORPUS = ROOT / "data" / "raw" / "legal_corpus"
OUT = ROOT / "data" / "interim" / "x1_master_v2.csv"

DIFF_LINE = re.compile(
    r"^\s*(has_ai_law|regulatory_intensity|thematic_coverage|regulatory_regime_group|enforcement_level|regulatory_approach)\s*:\s*"
    r"(\S[^->]*?)\s*->\s*(\S[^\(\n]*?)\s*(?:\([^)]*\))?\s*$",
    re.MULTILINE,
)

REGIME_VALUES = {"no_framework", "strategy_only", "soft_framework", "binding_regulation"}
ENFORCEMENT_VALUES = {"none", "low", "medium", "high"}


def clean_value(raw: str, var: str):
    """Normaliza valor extraido del diff summary (quita backticks, asteriscos, etc.)."""
    s = raw.strip().strip("*").strip("`").strip()
    if s in {"—", "-", "N/A", "NA", ""}:
        return None
    if var in {"has_ai_law"}:
        try:
            return int(float(s))
        except ValueError:
            return None
    if var in {"regulatory_intensity", "thematic_coverage"}:
        try:
            return int(float(s))
        except ValueError:
            return None
    if var == "regulatory_regime_group":
        s = s.lower().replace(" ", "_")
        return s if s in REGIME_VALUES else s
    if var == "enforcement_level":
        s = s.lower()
        return s if s in ENFORCEMENT_VALUES else s
    return s


def parse_candidates(path: Path) -> dict:
    """Devuelve dict con valores _iapp y _proposed extraidos del CANDIDATES.md."""
    text = path.read_text(encoding="utf-8")
    out: dict = {"iso3": path.parent.name}

    # Primer pase: diff summary (formato mas estandarizado)
    for match in DIFF_LINE.finditer(text):
        var, before, after = match.group(1), match.group(2), match.group(3)
        out[f"{var}_iapp"] = clean_value(before, var)
        out[f"{var}_proposed"] = clean_value(after, var)

    # Header del archivo: status propuesto
    m = re.search(r"\*\*Status propuesto:\*\*\s*`?([a-z_]+)`?", text)
    if m and "regulatory_regime_group_proposed" not in out:
        v = m.group(1).lower()
        if v in REGIME_VALUES:
            out["regulatory_regime_group_proposed"] = v

    # Confidence
    m = re.search(r"[Cc]onfidence[^:]*:\s*([a-z]+(?:-[a-z]+)?)\s*(?:→|->)\s*([a-z]+(?:-[a-z]+)?)", text)
    if m:
        out["confidence_iapp"] = m.group(1).strip()
        out["confidence_proposed"] = m.group(2).strip()

    # Numero de documentos: contar PDFs en el directorio
    pdfs = list(path.parent.glob("*.pdf"))
    out["ai_corpus_n_documents"] = len(pdfs)

    # Total paginas y span anos: leer manifest.csv si existe
    manifest = path.parent / "manifest.csv"
    if manifest.exists():
        try:
            mdf = pd.read_csv(manifest)
            if "pages" in mdf.columns:
                out["ai_corpus_total_pages"] = int(pd.to_numeric(mdf["pages"], errors="coerce").fillna(0).sum())
            if "publication_date" in mdf.columns:
                years = pd.to_datetime(mdf["publication_date"], errors="coerce").dt.year.dropna()
                if len(years) > 0:
                    out["ai_corpus_first_doc_year"] = int(years.min())
                    out["ai_corpus_last_doc_year"] = int(years.max())
                    out["ai_corpus_years_span"] = int(years.max() - years.min())
        except Exception as e:
            out["_manifest_parse_error"] = str(e)

    # Heuristica: has_dedicated_ai_authority
    # Buscar mencion de autoridad IA-especifica designada en el texto
    has_authority = bool(re.search(
        r"(autoridad IA[- ]espec[ií]fica|AI Office|dedicated AI authority|"
        r"AESIA|Traficom|RTR GmbH|AI Service Office|National AI Authority|"
        r"AI Safety Institute|KRiBSI|Data Protection Board.*IA|"
        r"AI Office.*establish)", text, re.IGNORECASE))
    out["has_dedicated_ai_authority"] = int(has_authority) if has_authority else 0

    # ai_law_pathway_declared: mencion de bill/draft con fecha
    pathway = bool(re.search(
        r"(bill[_ ]pending|policy_draft|draft_under_review|"
        r"pathway[_ ]declared|legislative pathway|bill in parliament|"
        r"AI Act 20[2-3][0-9]|projet de loi|hallituksen esitys|HE \d+/\d{4})",
        text, re.IGNORECASE))
    out["ai_law_pathway_declared"] = int(pathway) if pathway else 0

    return out


def main():
    rows = []
    iso_dirs = sorted(d for d in LEGAL_CORPUS.iterdir() if d.is_dir() and len(d.name) == 3)

    for iso_dir in iso_dirs:
        candidates = iso_dir / "CANDIDATES.md"
        if not candidates.exists():
            continue
        try:
            row = parse_candidates(candidates)
            rows.append(row)
        except Exception as e:
            print(f"  [WARN] {iso_dir.name}: {e}")

    df = pd.DataFrame(rows)

    # Reordenar columnas
    priority = [
        "iso3",
        "has_ai_law_iapp", "has_ai_law_proposed",
        "regulatory_intensity_iapp", "regulatory_intensity_proposed",
        "thematic_coverage_iapp", "thematic_coverage_proposed",
        "regulatory_regime_group_iapp", "regulatory_regime_group_proposed",
        "enforcement_level_iapp", "enforcement_level_proposed",
        "regulatory_approach_iapp", "regulatory_approach_proposed",
        "confidence_iapp", "confidence_proposed",
        "has_dedicated_ai_authority",
        "ai_law_pathway_declared",
        "ai_corpus_n_documents",
        "ai_corpus_total_pages",
        "ai_corpus_first_doc_year",
        "ai_corpus_last_doc_year",
        "ai_corpus_years_span",
    ]
    cols = [c for c in priority if c in df.columns] + [c for c in df.columns if c not in priority]
    df = df[cols].sort_values("iso3").reset_index(drop=True)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)
    print(f"[OK] {len(df)} paises procesados -> {OUT}")
    print(f"     Columnas: {len(df.columns)}")
    print(f"     Diff summary detectado en: {df['regulatory_intensity_proposed'].notna().sum()} paises")
    print()
    print("Resumen por pais (subset relevante):")
    summary_cols = [c for c in [
        "iso3", "regulatory_regime_group_proposed", "regulatory_intensity_proposed",
        "thematic_coverage_proposed", "ai_corpus_n_documents", "ai_corpus_total_pages"
    ] if c in df.columns]
    print(df[summary_cols].to_string(index=False))


if __name__ == "__main__":
    main()
