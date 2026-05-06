"""Paths and constants for the self-contained Fase 3 implementation."""

from pathlib import Path

PHASE_DIR = Path(__file__).resolve().parents[2]
ROOT = PHASE_DIR.parent
OUTPUT_DIR = PHASE_DIR / "outputs"
CONFIG_DIR = PHASE_DIR / "config"
FASE3_CONFIG_DIR = CONFIG_DIR / "fase3"
NOTEBOOK_DIR = PHASE_DIR / "notebooks"
EDA_DIR = ROOT / "outputs" / "eda_preliminar"

SOURCES = {
    "iapp": ROOT / "IAPP" / "iapp_dataset_unificado.xlsx",
    "microsoft": ROOT / "MICROSOFT" / "Microsoft_AI_Reports_Data_unificado.xlsx",
    "oxford": ROOT / "Oxford Insights" / "data_index" / "UNIFICADO" / "Oxford_Insights_Unificado.xlsx",
    "wb": ROOT / "World Bank WDI" / "WB_WDI_WGI_unificado.xlsx",
    "wipo": ROOT / "WIPO Global Innovation Index" / "data_wipo_gii" / "WIPO_GII_2021_2025_UNIFICADO.xlsx",
    "stanford": ROOT / "STANFORD AI INDEX 26" / "PUBLIC DATA_ 2026 AI INDEX REPORT" / "completo" / "stanford_ai_index_2026_unificado.csv",
    "oecd": ROOT / "OECD" / "OECD_Data_Central_unificado.xlsx",
    "anthropic": ROOT / "ANTROPHIC" / "data_unificada" / "antrophic_economic_index.xlsx",
}

SOURCE_ORDER = ["iapp", "microsoft", "oxford", "wb", "wipo", "stanford", "oecd", "anthropic"]

BLOCKS = [
    "regulatory_treatment",
    "ecosystem_outcome",
    "adoption_diffusion",
    "socioeconomic_control",
    "institutional_control",
    "tech_infrastructure_control",
]

OUTPUT_FILES = [
    "README_MATRIZ_MADRE.md",
    "fase3_fuentes_usadas.csv",
    "fase3_diccionario_variables.csv",
    "fase3_universo_geografico.csv",
    "fase3_geo_crosswalk_manual.csv",
    "fase3_tablas_seleccionadas.csv",
    "fase3_reglas_temporales.csv",
    "fase3_decisiones_metodologicas.csv",
    "fase3_variables_excluidas.csv",
    "matriz_larga_panel.csv",
    "matriz_larga_snapshot.csv",
    "matriz_madre_wide.csv",
    "matriz_madre_trazabilidad.csv",
    "fase3_reporte_calidad_matriz.csv",
    "fase3_issue_resolution_log.csv",
    "fase3_human_review_log.csv",
    "fase3_entidades_excluidas_geografia.csv",
    "fase3_auditoria_muestra_valores.csv",
    "fase3_reporte_calidad_matriz.md",
    "manifest.json",
    "Matriz_Madre_Fase3.xlsx",
]

EXCEL_SHEETS = [
    "README",
    "Matriz Madre",
    "Matriz Larga Panel",
    "Matriz Larga Snapshot",
    "Diccionario Variables",
    "Fuentes Usadas",
    "Reglas Temporales",
    "Crosswalk Geografico",
    "Trazabilidad",
    "Issues Resueltos",
    "Decision Log",
    "Chile_Snapshot",
    "Chile_vs_Peers",
]
