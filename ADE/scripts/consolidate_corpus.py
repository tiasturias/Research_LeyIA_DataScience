#!/usr/bin/env python3
"""Consolidar corpus legal-IA por pais en una estructura unica y rica.

Usage:
    python scripts/consolidate_corpus.py
    python scripts/consolidate_corpus.py --dry-run
"""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Rutas
SOURCE_EMBEDDED = Path("/home/pablo/Research_LeyIA_DataScience/ADE/embedded_rag")
SOURCE_LEGAL = Path("/home/pablo/Research_LeyIA_DataScience/data/raw/legal_corpus")
SOURCE_SAMPLE_READY = Path(
    "/home/pablo/Research_LeyIA_DataScience/data/interim/sample_ready_cross_section.csv"
)
DEST_DIR = Path("/home/pablo/Research_LeyIA_DataScience/ADE/corpus_consolidated")

# Paises de la muestra ADE (73)
COUNTRIES_73 = [
    "ARE", "ARG", "ARM", "AUS", "AUT", "BEL", "BGD", "BGR", "BLR", "BRA",
    "CAN", "CHE", "CHL", "CHN", "CMR", "COL", "CRI", "CZE", "DEU", "DNK",
    "ECU", "EGY", "ESP", "FIN", "FRA", "GBR", "GHA", "GRC", "HRV", "HUN",
    "IDN", "IND", "IRL", "ISR", "ITA", "JOR", "JPN", "KAZ", "KEN", "KOR",
    "LBN", "LKA", "LTU", "MEX", "MNG", "MYS", "NGA", "NLD", "NOR", "NZL",
    "PAN", "PER", "PHL", "POL", "PRT", "ROU", "RUS", "SAU", "SGP", "SRB",
    "SVK", "SVN", "SWE", "THA", "TUN", "TUR", "TWN", "UGA", "UKR", "URY",
    "USA", "VNM", "ZAF",
]

COUNTRY_NAMES = {
    "ARE": "Emiratos Arabes Unidos", "ARG": "Argentina", "ARM": "Armenia",
    "AUS": "Australia", "AUT": "Austria", "BEL": "Belgica", "BGD": "Banglades",
    "BGR": "Bulgaria", "BLR": "Bielorrusia", "BRA": "Brasil", "CAN": "Canada",
    "CHE": "Suiza", "CHL": "Chile", "CHN": "China", "CMR": "Camerun",
    "COL": "Colombia", "CRI": "Costa Rica", "CZE": "Republica Checa",
    "DEU": "Alemania", "DNK": "Dinamarca", "ECU": "Ecuador", "EGY": "Egipto",
    "ESP": "Espana", "FIN": "Finlandia", "FRA": "Francia", "GBR": "Reino Unido",
    "GHA": "Ghana", "GRC": "Grecia", "HRV": "Croacia", "HUN": "Hungria",
    "IDN": "Indonesia", "IND": "India", "IRL": "Irlanda", "ISR": "Israel",
    "ITA": "Italia", "JOR": "Jordania", "JPN": "Japon", "KAZ": "Kazajistan",
    "KEN": "Kenia", "KOR": "Corea del Sur", "LBN": "Libano", "LKA": "Sri Lanka",
    "LTU": "Lituania", "MEX": "Mexico", "MNG": "Mongolia", "MYS": "Malasia",
    "NGA": "Nigeria", "NLD": "Paises Bajos", "NOR": "Noruega", "NZL": "Nueva Zelanda",
    "PAN": "Panama", "PER": "Peru", "PHL": "Filipinas", "POL": "Polonia",
    "PRT": "Portugal", "ROU": "Rumania", "RUS": "Rusia", "SAU": "Arabia Saudita",
    "SGP": "Singapur", "SRB": "Serbia", "SVK": "Eslovaquia", "SVN": "Eslovenia",
    "SWE": "Suecia", "THA": "Tailandia", "TUN": "Tunez", "TUR": "Turquia",
    "TWN": "Taiwan", "UGA": "Uganda", "UKR": "Ucrania", "URY": "Uruguay",
    "USA": "Estados Unidos", "VNM": "Vietnam", "ZAF": "Sudafrica",
}

STUDY_CONTEXT = {
    "question": (
        "Existe una asociacion estadisticamente significativa entre las "
        "caracteristicas de la regulacion de inteligencia artificial de un pais "
        "y el desarrollo de su ecosistema de IA, despues de controlar por "
        "factores socioeconomicos e institucionales."
    ),
    "policy_context": (
        "El estudio busca informar la discusion chilena sobre Ley Marco de IA "
        "(Boletin 16821-19) con evidencia comparativa internacional."
    ),
    "design": "Cross-section comparativo 2025 con 86 paises y una submuestra ADE de 73.",
    "primary_dataset": "data/interim/sample_ready_cross_section.csv",
    "recommended_tier": "complete_confounded",
}

SOURCE_SPECS = (
    {
        "source": "IAPP + OECD (X1 regulatorio)",
        "purpose": "Caracterizar el marco regulatorio de IA del pais.",
        "variables": (
            ("has_ai_law", "Tiene ley IA", None),
            ("regulatory_approach", "Enfoque regulatorio", None),
            ("regulatory_intensity", "Intensidad regulatoria", None),
            ("year_enacted", "Ano promulgacion", None),
            ("enforcement_level", "Enforcement", None),
            ("thematic_coverage", "Cobertura tematica", None),
            ("regulatory_status_group", "Grupo regulatorio", None),
            ("x1_source", "Fuente X1 consolidada", None),
        ),
    },
    {
        "source": "Stanford AI Index",
        "purpose": "Medir inversion, startups y patentes del ecosistema IA.",
        "variables": (
            ("ai_investment_usd_bn_cumulative", "Inversion IA acumulada (USD bn)", "investment_year"),
            ("ai_startups_cumulative", "Startups IA acumuladas", "startups_year"),
            ("ai_patents_per100k", "Patentes IA por 100k", "patents_year"),
        ),
    },
    {
        "source": "Microsoft AI Diffusion Report",
        "purpose": "Capturar adopcion efectiva de IA generativa.",
        "variables": (
            ("ai_adoption_rate", "Adopcion IA", "adoption_period"),
        ),
    },
    {
        "source": "Oxford Insights",
        "purpose": "Medir readiness gubernamental para IA.",
        "variables": (
            ("ai_readiness_score", "AI readiness score", "readiness_year"),
        ),
    },
    {
        "source": "WIPO Global Innovation Index",
        "purpose": "Controlar capacidad general de innovacion y region.",
        "variables": (
            ("gii_score", "GII score", "gii_year"),
            ("region", "Region", None),
        ),
    },
    {
        "source": "World Bank WDI",
        "purpose": "Agregar controles socioeconomicos y de economia digital.",
        "variables": (
            ("gdp_per_capita_ppp", "PIB per capita PPP", "gdp_per_capita_ppp_year"),
            ("internet_penetration", "Penetracion internet", "internet_penetration_year"),
            ("rd_expenditure", "Gasto I+D", "rd_expenditure_year"),
            ("tertiary_education", "Educacion terciaria", "tertiary_education_year"),
            ("ict_service_exports_pct", "Exportaciones ICT", "ict_service_exports_pct_year"),
            ("high_tech_exports_pct", "Exportaciones high-tech", "high_tech_exports_pct_year"),
        ),
    },
    {
        "source": "World Bank WGI",
        "purpose": "Controlar calidad institucional y gobernanza.",
        "variables": (
            ("regulatory_quality", "Regulatory quality", "regulatory_quality_year"),
            ("rule_of_law", "Rule of law", "rule_of_law_year"),
            ("government_effectiveness", "Government effectiveness", "government_effectiveness_year"),
            ("control_of_corruption", "Control of corruption", "control_of_corruption_year"),
        ),
    },
    {
        "source": "GDPR / proteccion de datos",
        "purpose": "Capturar tradicion regulatoria digital preexistente.",
        "variables": (
            ("has_gdpr_like_law", "Tiene ley GDPR-like", None),
            ("gdpr_similarity_level", "Nivel de similitud GDPR", None),
            ("dp_law_year", "Ano ley DP", None),
            ("has_dpa", "Tiene DPA", None),
            ("eu_status", "Status UE/adequacy", None),
            ("enforcement_active", "Enforcement activo DP", None),
        ),
    },
    {
        "source": "Freedom House",
        "purpose": "Controlar tipo de regimen politico y libertades.",
        "variables": (
            ("fh_total_score", "Freedom House total", "fh_year"),
            ("fh_status", "FH status", None),
            ("fh_democracy_level", "Nivel democracia FH", None),
        ),
    },
    {
        "source": "Legal Origin",
        "purpose": "Capturar tradicion juridica como confounder institucional.",
        "variables": (
            ("legal_origin", "Legal origin", None),
            ("is_common_law", "Common law", None),
        ),
    },
    {
        "source": "OECD robustez",
        "purpose": "Variables adicionales de sensibilidad y robustez.",
        "variables": (
            ("ai_investment_vc_proxy", "VC proxy", "vc_proxy_year"),
            ("ai_publications_frac", "Publicaciones IA", "ai_publications_frac_year"),
        ),
    },
)

COMPLETENESS_KEYS = (
    "complete_principal",
    "complete_confounded",
    "complete_digital",
    "complete_regime",
    "complete_legal_tradition",
    "complete_extended",
    "complete_strict",
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _read_json(path: Path) -> dict[str, Any] | list[Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _clean(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    return "" if text.lower() in {"", "nan", "none", "null"} else text


def _has_value(value: Any) -> bool:
    return bool(_clean(value))


def _to_bool(value: Any) -> bool | None:
    text = _clean(value).lower()
    if text in {"1", "true", "yes", "si", "sí"}:
        return True
    if text in {"0", "false", "no"}:
        return False
    return None


def _format_value(value: Any) -> str:
    text = _clean(value)
    if not text:
        return "N/A"
    return text


def _format_bool(value: Any) -> str:
    parsed = _to_bool(value)
    if parsed is True:
        return "Si"
    if parsed is False:
        return "No"
    return _format_value(value)


def _format_metric(value: Any, year: Any = None, suffix: str = "") -> str:
    rendered = _format_value(value)
    if rendered == "N/A":
        return rendered
    if suffix:
        rendered = f"{rendered}{suffix}"
    year_text = _clean(year)
    if year_text:
        return f"{rendered} (ref. {year_text})"
    return rendered


def _load_sample_ready_index() -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}
    with SOURCE_SAMPLE_READY.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            iso3 = _clean(row.get("iso3"))
            if iso3:
                index[iso3] = row
    return index


def _extract_documents_count(docs_data: dict[str, Any] | list[Any] | None) -> int:
    if docs_data is None:
        return 0
    docs = docs_data if isinstance(docs_data, list) else docs_data.get("documents", [])
    return len(docs)


def _extract_pages_total(docs_data: dict[str, Any] | list[Any] | None) -> int:
    if docs_data is None:
        return 0
    docs = docs_data if isinstance(docs_data, list) else docs_data.get("documents", [])
    total = 0
    for doc in docs:
        try:
            total += int(float(str(doc.get("pages", "0")).strip() or 0))
        except ValueError:
            continue
    return total


def _build_source_inventory(
    row: dict[str, str] | None,
    *,
    has_legal_corpus: bool,
    legal_files: list[str],
) -> list[dict[str, Any]]:
    inventory: list[dict[str, Any]] = []
    if row:
        for spec in SOURCE_SPECS:
            variables = []
            for key, label, year_key in spec["variables"]:
                raw_value = row.get(key)
                if not _has_value(raw_value):
                    continue
                year_value = row.get(year_key) if year_key else ""
                variables.append(
                    {
                        "key": key,
                        "label": label,
                        "value": _clean(raw_value),
                        "reference": _clean(year_value),
                    }
                )
            if variables:
                inventory.append(
                    {
                        "source": spec["source"],
                        "purpose": spec["purpose"],
                        "variables": variables,
                    }
                )

    if has_legal_corpus:
        inventory.append(
            {
                "source": "Corpus legal manual por pais",
                "purpose": (
                    "Aportar evidencia documental, citas, inventario y hallazgos "
                    "diferenciales del caso nacional."
                ),
                "variables": [
                    {"key": "legal_corpus", "label": name, "value": "disponible", "reference": ""}
                    for name in legal_files
                ],
            }
        )
    return inventory


def _build_completeness_flags(row: dict[str, str] | None) -> dict[str, bool]:
    flags: dict[str, bool] = {}
    for key in COMPLETENESS_KEYS:
        flags[key] = _to_bool(row.get(key) if row else None) is True
    return flags


def _build_data_inventory(
    iso3: str,
    country_name: str,
    row: dict[str, str] | None,
    profile_data: dict[str, Any] | None,
    reg_data: dict[str, Any] | None,
    docs_data: dict[str, Any] | list[Any] | None,
    *,
    has_legal_corpus: bool,
    legal_files: list[str],
) -> dict[str, Any]:
    return {
        "generated_at": _now_iso(),
        "iso3": iso3,
        "country_name": country_name,
        "study_context": STUDY_CONTEXT,
        "completeness_flags": _build_completeness_flags(row),
        "source_inventory": _build_source_inventory(
            row,
            has_legal_corpus=has_legal_corpus,
            legal_files=legal_files,
        ),
        "documents_summary": {
            "count": _extract_documents_count(docs_data),
            "pages_total": _extract_pages_total(docs_data),
        },
        "country_profile": profile_data or {},
        "regulatory_framework": reg_data or {},
        "sample_ready_row": row or {},
    }


def _build_country_dossier(
    iso3: str,
    country_name: str,
    *,
    row: dict[str, str] | None,
    profile_data: dict[str, Any] | None,
    reg_data: dict[str, Any] | None,
    docs_data: dict[str, Any] | list[Any] | None,
    data_inventory: dict[str, Any],
    legal_texts: dict[str, str],
) -> str:
    docs = docs_data if isinstance(docs_data, list) else (docs_data or {}).get("documents", [])
    meta = (profile_data or {}).get("metadata", {})
    eco = (profile_data or {}).get("ecosystem_ia", {})
    ctrl = (profile_data or {}).get("controls", {})
    gov = (profile_data or {}).get("governance", {})
    reg_status = (reg_data or {}).get("regulatory_status", {})
    reg_approach = (reg_data or {}).get("regulatory_approach", {})
    reg_intensity = (reg_data or {}).get("regulatory_intensity", {})
    enforcement = (reg_data or {}).get("enforcement_level", {})
    thematic = (reg_data or {}).get("thematic_coverage", {})
    dp = (reg_data or {}).get("data_protection", {})

    lines = [
        f"# {country_name} ({iso3}) - Dossier consolidado Legal-IA",
        "",
        "## 1. Proposito analitico",
        STUDY_CONTEXT["question"],
        "",
        STUDY_CONTEXT["policy_context"],
        "",
        f"- Diseno del estudio: {STUDY_CONTEXT['design']}",
        f"- Dataset base: {STUDY_CONTEXT['primary_dataset']}",
        f"- Tier recomendada: {STUDY_CONTEXT['recommended_tier']}",
        "",
        "## 2. Estado del pais dentro del estudio",
        f"- Grupo regulatorio: {_format_value(row.get('regulatory_status_group') if row else reg_status.get('group'))}",
        f"- Tiene corpus legal manual: {'Si' if legal_texts else 'No'}",
        f"- Documentos legales identificados: {_extract_documents_count(docs_data)}",
        f"- Paginas totales del corpus legal: {_extract_pages_total(docs_data)}",
    ]

    completeness = data_inventory["completeness_flags"]
    if completeness:
        lines.extend(
            [
                f"- complete_principal: {'Si' if completeness['complete_principal'] else 'No'}",
                f"- complete_confounded: {'Si' if completeness['complete_confounded'] else 'No'}",
                f"- complete_digital: {'Si' if completeness['complete_digital'] else 'No'}",
                f"- complete_regime: {'Si' if completeness['complete_regime'] else 'No'}",
                f"- complete_legal_tradition: {'Si' if completeness['complete_legal_tradition'] else 'No'}",
            ]
        )

    lines.extend(
        [
            "",
            "## 3. Datos recopilados por fuente y proposito",
        ]
    )
    for source_entry in data_inventory["source_inventory"]:
        lines.append(f"### {source_entry['source']}")
        lines.append(f"- Proposito: {source_entry['purpose']}")
        for variable in source_entry["variables"]:
            ref = variable["reference"]
            if ref:
                lines.append(f"- {variable['label']}: {variable['value']} (ref. {ref})")
            else:
                lines.append(f"- {variable['label']}: {variable['value']}")
        lines.append("")

    lines.extend(
        [
            "## 4. Perfil cuantitativo del pais",
            f"- Region: {_format_value(meta.get('region'))}",
            f"- OECD member: {_format_bool(meta.get('oecd_member'))}",
            f"- Legal origin: {_format_value(meta.get('legal_origin'))}",
            f"- Common law: {_format_bool(meta.get('is_common_law'))}",
            f"- Poblacion: {_format_value(meta.get('population'))}",
            f"- GDP actual USD: {_format_value(meta.get('gdp_current_usd'))}",
            f"- AI readiness: {_format_metric(eco.get('ai_readiness_score', {}).get('value'), eco.get('ai_readiness_score', {}).get('year'))}",
            f"- Adopcion IA: {_format_metric(eco.get('ai_adoption_rate', {}).get('value'), eco.get('ai_adoption_rate', {}).get('period'), '%')}",
            f"- Inversion IA acumulada: {_format_metric(eco.get('ai_investment_usd_bn', {}).get('cumulative'), eco.get('ai_investment_usd_bn', {}).get('year'))}",
            f"- Startups IA acumuladas: {_format_metric(eco.get('ai_startups', {}).get('cumulative'), eco.get('ai_startups', {}).get('year'))}",
            f"- Patentes IA por 100k: {_format_metric(eco.get('ai_patents_per100k', {}).get('value'), eco.get('ai_patents_per100k', {}).get('year'))}",
            f"- GDP per capita PPP: {_format_metric(ctrl.get('gdp_per_capita_ppp', {}).get('value'), ctrl.get('gdp_per_capita_ppp', {}).get('year'))}",
            f"- GII score: {_format_metric(ctrl.get('gii_score', {}).get('value'), ctrl.get('gii_score', {}).get('year'))}",
            f"- Internet penetration: {_format_metric(ctrl.get('internet_penetration', {}).get('value'), ctrl.get('internet_penetration', {}).get('year'), '%')}",
            f"- R&D expenditure: {_format_metric(ctrl.get('rd_expenditure', {}).get('value'), ctrl.get('rd_expenditure', {}).get('year'))}",
            f"- Tertiary education: {_format_metric(ctrl.get('tertiary_education', {}).get('value'), ctrl.get('tertiary_education', {}).get('year'))}",
            f"- Regulatory quality: {_format_metric(gov.get('regulatory_quality', {}).get('value'), gov.get('regulatory_quality', {}).get('year'))}",
            f"- Rule of law: {_format_metric(gov.get('rule_of_law', {}).get('value'), gov.get('rule_of_law', {}).get('year'))}",
            f"- Freedom House: {_format_metric(gov.get('fh_total_score', {}).get('value'), gov.get('fh_total_score', {}).get('year'))}",
            "",
            "## 5. Marco regulatorio y confounders",
            f"- Grupo: {_format_value(reg_status.get('group'))}",
            f"- Tiene ley IA: {_format_bool(reg_status.get('has_ai_law'))}",
            f"- Enfoque: {_format_value(reg_approach.get('value'))}",
            f"- Intensidad: {_format_metric(reg_intensity.get('value'), reg_intensity.get('scale'))}",
            f"- Enforcement: {_format_value(enforcement.get('value'))}",
            f"- Cobertura tematica: {_format_metric(thematic.get('value'), thematic.get('max'))}",
            f"- GDPR-like law: {_format_bool(dp.get('has_gdpr_like_law'))}",
            f"- GDPR similarity level: {_format_value(dp.get('gdpr_similarity_level'))}",
            f"- Tiene DPA: {_format_bool(dp.get('has_dpa'))}",
        ]
    )

    if docs:
        lines.extend(
            [
                "",
                "## 6. Inventario de documentos legales",
                f"El corpus legal del pais contiene {len(docs)} documentos identificados.",
            ]
        )
        for idx, doc in enumerate(docs[:10], start=1):
            lines.append(
                f"- Doc {idx}: {doc.get('title', 'Sin titulo')} | tipo={doc.get('type', 'N/A')} | "
                f"fecha={doc.get('date', 'N/A')} | paginas={doc.get('pages', 'N/A')}"
            )
    else:
        lines.extend(
            [
                "",
                "## 6. Inventario de documentos legales",
                "No existe un corpus legal manual descargado para este pais; la evidencia disponible se apoya en perfil, codificacion regulatoria y meta-analisis.",
            ]
        )

    lines.extend(
        [
            "",
            "## 7. Analisis cualitativo disponible",
            f"- meta_analysis chars: {len(legal_texts.get('04_meta_analysis.md', ''))}",
            f"- SOURCES chars: {len(legal_texts.get('05_sources.md', ''))}",
            f"- CANDIDATES chars: {len(legal_texts.get('06_candidates.md', ''))}",
            f"- FINDINGS chars: {len(legal_texts.get('07_findings.md', ''))}",
        ]
    )
    if legal_texts.get("07_findings.md"):
        preview = legal_texts["07_findings.md"][:800].replace("\n", " ")
        lines.append(f"- Preview hallazgo diferencial: {preview}")
    elif legal_texts.get("04_meta_analysis.md"):
        preview = legal_texts["04_meta_analysis.md"][:800].replace("\n", " ")
        lines.append(f"- Preview meta analisis: {preview}")

    lines.extend(
        [
            "",
            "## 8. Nota de uso para ingesta",
            (
                "La estrategia objetivo es 1 documento por pais con multiples metachunks: "
                "contexto del estudio, perfil cuantitativo, marco regulatorio, inventario "
                "documental, hallazgo/meta-analisis y evidencia legal/manual cuando exista."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def consolidate_country(
    iso3: str,
    *,
    sample_ready_index: dict[str, dict[str, str]],
    dry_run: bool = False,
) -> dict[str, Any]:
    """Consolidar toda la informacion disponible de un pais."""

    country_name = COUNTRY_NAMES.get(iso3, iso3)
    source_dir = SOURCE_EMBEDDED / iso3
    legal_dir = SOURCE_LEGAL / iso3
    dest_dir = DEST_DIR / iso3
    row = sample_ready_index.get(iso3)

    result: dict[str, Any] = {
        "iso3": iso3,
        "country_name": country_name,
        "status": "pending",
        "has_embedded_data": source_dir.exists(),
        "has_legal_corpus": legal_dir.exists(),
        "files_created": [],
    }
    if not source_dir.exists():
        result["status"] = "missing_embedded"
        return result

    if not dry_run:
        dest_dir.mkdir(parents=True, exist_ok=True)

    profile_data = None
    reg_data = None
    docs_data = None
    legal_texts: dict[str, str] = {}

    copy_specs = (
        ("country_profile.json", "01_profile.json"),
        ("regulatory_framework.json", "02_regulatory.json"),
        ("documents_index.json", "03_documents_index.json"),
        ("meta_chunks.md", "04_meta_analysis.md"),
    )
    for src_name, dst_name in copy_specs:
        src_path = source_dir / src_name
        if not src_path.exists():
            continue
        if src_path.suffix == ".json":
            data = _read_json(src_path)
            if src_name == "country_profile.json":
                profile_data = data if isinstance(data, dict) else {}
            elif src_name == "regulatory_framework.json":
                reg_data = data if isinstance(data, dict) else {}
            elif src_name == "documents_index.json":
                docs_data = data
            if not dry_run:
                (dest_dir / dst_name).write_text(
                    json.dumps(data, indent=2, ensure_ascii=False),
                    encoding="utf-8",
                )
        else:
            text = _read_text(src_path)
            legal_texts[dst_name] = text
            if not dry_run:
                (dest_dir / dst_name).write_text(text, encoding="utf-8")
        result["files_created"].append(dst_name)

    rich_chunks = source_dir / "embedding_chunks_rich.json"
    basic_chunks = source_dir / "embedding_chunks.json"
    chunks_src = rich_chunks if rich_chunks.exists() else basic_chunks
    if chunks_src.exists():
        chunk_data = _read_json(chunks_src)
        if not dry_run:
            (dest_dir / "embedding_chunks.json").write_text(
                json.dumps(chunk_data, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
        result["files_created"].append("embedding_chunks.json")
        result["n_chunks"] = len(chunk_data) if isinstance(chunk_data, list) else 0

    full_analysis_src = source_dir / "legal_corpus_full.json"
    if full_analysis_src.exists():
        full_analysis = _read_json(full_analysis_src)
        if not dry_run:
            (dest_dir / "08_full_analysis.json").write_text(
                json.dumps(full_analysis, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
        result["files_created"].append("08_full_analysis.json")

    legal_files: list[str] = []
    for src_name, dst_name in (
        ("SOURCES.md", "05_sources.md"),
        ("CANDIDATES.md", "06_candidates.md"),
        ("FINDINGS.md", "07_findings.md"),
    ):
        src_path = legal_dir / src_name
        if not src_path.exists():
            continue
        text = _read_text(src_path)
        legal_texts[dst_name] = text
        legal_files.append(dst_name)
        if not dry_run:
            (dest_dir / dst_name).write_text(text, encoding="utf-8")
        result["files_created"].append(dst_name)

    result["n_documents"] = _extract_documents_count(docs_data)
    result["n_pages"] = _extract_pages_total(docs_data)

    data_inventory = _build_data_inventory(
        iso3,
        country_name,
        row,
        profile_data,
        reg_data,
        docs_data,
        has_legal_corpus=legal_dir.exists(),
        legal_files=legal_files,
    )
    dossier = _build_country_dossier(
        iso3,
        country_name,
        row=row,
        profile_data=profile_data,
        reg_data=reg_data,
        docs_data=docs_data,
        data_inventory=data_inventory,
        legal_texts=legal_texts,
    )

    if not dry_run:
        (dest_dir / "09_data_inventory.json").write_text(
            json.dumps(data_inventory, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        (dest_dir / "10_country_dossier.md").write_text(dossier, encoding="utf-8")
    result["files_created"].extend(["09_data_inventory.json", "10_country_dossier.md"])

    completeness = data_inventory["completeness_flags"]
    master_record = {
        "iso3": iso3,
        "country_name": country_name,
        "consolidated_at": _now_iso(),
        "has_embedded_data": source_dir.exists(),
        "has_legal_corpus": legal_dir.exists(),
        "files": result["files_created"],
        "n_documents": result["n_documents"],
        "n_pages": result["n_pages"],
        "n_chunks": result.get("n_chunks", 0),
        "completeness": completeness,
        "source_inventory": data_inventory["source_inventory"],
        "metrics": {
            "region": (profile_data or {}).get("metadata", {}).get("region"),
            "oecd_member": (profile_data or {}).get("metadata", {}).get("oecd_member"),
            "ai_readiness": (profile_data or {}).get("ecosystem_ia", {}).get("ai_readiness_score", {}).get("value"),
            "ai_adoption": (profile_data or {}).get("ecosystem_ia", {}).get("ai_adoption_rate", {}).get("value"),
            "ai_investment": (profile_data or {}).get("ecosystem_ia", {}).get("ai_investment_usd_bn", {}).get("cumulative"),
            "gdp_per_capita": (profile_data or {}).get("controls", {}).get("gdp_per_capita_ppp", {}).get("value"),
            "internet_penetration": (profile_data or {}).get("controls", {}).get("internet_penetration", {}).get("value"),
            "regulatory_quality": (profile_data or {}).get("governance", {}).get("regulatory_quality", {}).get("value"),
            "rule_of_law": (profile_data or {}).get("governance", {}).get("rule_of_law", {}).get("value"),
        },
        "regulatory": {
            "group": (reg_data or {}).get("regulatory_status", {}).get("group"),
            "has_ai_law": (reg_data or {}).get("regulatory_status", {}).get("has_ai_law"),
            "approach": (reg_data or {}).get("regulatory_approach", {}).get("value"),
            "intensity": (reg_data or {}).get("regulatory_intensity", {}).get("value"),
            "thematic_coverage": (reg_data or {}).get("thematic_coverage", {}).get("value"),
            "has_gdpr_like_law": (reg_data or {}).get("data_protection", {}).get("has_gdpr_like_law"),
            "gdpr_similarity_level": (reg_data or {}).get("data_protection", {}).get("gdpr_similarity_level"),
        },
    }

    if not dry_run:
        (dest_dir / "master_record.json").write_text(
            json.dumps(master_record, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
    if "master_record.json" not in result["files_created"]:
        result["files_created"].append("master_record.json")
    result["regulatory"] = master_record["regulatory"]
    result["completeness"] = completeness
    result["status"] = "completed"
    return result


def create_master_index(results: list[dict[str, Any]]) -> dict[str, Any]:
    """Crear indice maestro de todos los paises consolidados."""

    index = {
        "generated_at": _now_iso(),
        "n_countries": len(results),
        "n_with_corpus": sum(1 for r in results if r.get("has_legal_corpus")),
        "n_without_corpus": sum(1 for r in results if not r.get("has_legal_corpus")),
        "countries": {},
        "regulatory_groups": {
            "binding_regulation": [],
            "strategy_only": [],
            "soft_framework": [],
            "no_framework": [],
        },
    }
    for result in results:
        iso3 = result["iso3"]
        country_entry = {
            "country_name": result["country_name"],
            "status": result["status"],
            "has_corpus": result.get("has_legal_corpus", False),
            "n_documents": result.get("n_documents", 0),
            "n_pages": result.get("n_pages", 0),
            "n_chunks": result.get("n_chunks", 0),
            "files": result.get("files_created", []),
            "completeness": result.get("completeness", {}),
        }
        index["countries"][iso3] = country_entry
        group = (result.get("regulatory") or {}).get("group")
        if group in index["regulatory_groups"]:
            index["regulatory_groups"][group].append(iso3)
    return index


def main(dry_run: bool = False) -> dict[str, Any]:
    """Consolidar todos los paises de la muestra ADE."""

    print("=" * 60)
    print("CONSOLIDACION CORPUS LEGAL-IA")
    print("=" * 60)
    print(f"Fuente embedded: {SOURCE_EMBEDDED}")
    print(f"Fuente legal_corpus: {SOURCE_LEGAL}")
    print(f"Sample ready: {SOURCE_SAMPLE_READY}")
    print(f"Destino: {DEST_DIR}")
    print(f"Dry run: {dry_run}")
    print()

    sample_ready_index = _load_sample_ready_index()
    if not dry_run:
        DEST_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    for iso3 in COUNTRIES_73:
        print(f"Procesando {iso3}...", end=" ")
        result = consolidate_country(
            iso3,
            sample_ready_index=sample_ready_index,
            dry_run=dry_run,
        )
        n_files = len(result.get("files_created", []))
        has_corpus = "Si" if result.get("has_legal_corpus") else "No"
        print(f"{result['status']} | {n_files} files | corpus: {has_corpus}")
        results.append(result)

    print()
    print("Creando master_index.json...")
    master_index = create_master_index(results)
    if not dry_run:
        (DEST_DIR / "master_index.json").write_text(
            json.dumps(master_index, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    print()
    print("=" * 60)
    print("RESUMEN")
    print("=" * 60)
    print(f"Paises procesados: {len(results)}")
    print(f"Con corpus legal: {master_index['n_with_corpus']}")
    print(f"Sin corpus legal: {master_index['n_without_corpus']}")
    print()
    print("Grupos regulatorios:")
    for group, countries in master_index["regulatory_groups"].items():
        print(f"  {group}: {len(countries)} paises")

    return master_index


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
