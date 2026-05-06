"""Pandera schemas for FASE3 outputs."""

from __future__ import annotations

import pandera.pandas as pa
from pandera import Check, Column

from .config import BLOCKS, SOURCE_ORDER

ENTITY_TYPES = [
    "country_iso3", "territory_iso3", "region", "subnational", "organization_or_group",
    "global", "obsolete_or_non_comparable", "unknown_requires_review", "unknown",
]
UNITS = ["pct", "score_0_100", "usd", "count", "rank", "wgi_-2.5_2.5", "binary", "categorical", "text"]
DIRECTIONS = ["higher_better", "lower_better", "categorical", "unknown"]
CONFIDENCE = ["verified", "extracted", "inferred", "missing_explicit", "missing_no_data"]


PanelSchema = pa.DataFrameSchema({
    "cell_id": Column(str, Check.str_matches(r"^[A-Z]{3}_[a-z]+_.+_(\d{4}|na)$"), unique=True),
    "iso3": Column(str, Check.str_matches(r"^[A-Z]{3}$")),
    "country_name_canonical": Column(str),
    "entity_type": Column(str, Check.isin(ENTITY_TYPES)),
    "source_id": Column(str, Check.isin(SOURCE_ORDER)),
    "table_id": Column(str),
    "original_variable": Column(str),
    "variable_matriz": Column(str),
    "year": Column(object, Check(lambda s: s.dropna().astype(int).between(2018, 2026).all()), nullable=True),
    "period": Column(str, nullable=True, coerce=True),
    "value_original": Column(str, nullable=False),
    "value_numeric": Column(float, nullable=True, coerce=True),
    "value_text": Column(str, nullable=True),
    "unit": Column(str, Check.isin(UNITS)),
    "direction": Column(str, Check.isin(DIRECTIONS)),
    "confidence_level": Column(str, Check.isin(CONFIDENCE)),
    "extraction_rule": Column(str),
    "source_file": Column(str),
    "source_sheet": Column(str),
    "row_identifier": Column(str),
    "extractor_version": Column(str),
    "created_at": Column(str),
}, strict=True, ordered=True, coerce=True)


SnapshotSchema = pa.DataFrameSchema({
    **PanelSchema.columns,
    "snapshot_rule": Column(str),
    "year_used": Column(str, nullable=True, coerce=True),
    "years_collapsed": Column(str, nullable=True, coerce=True),
    "temporal_warning": Column(str, nullable=True, coerce=True),
}, strict=True, ordered=True, coerce=True)


DictionarySchema = pa.DataFrameSchema({
    "variable_matriz": Column(str, unique=True),
    "source_id": Column(str, Check.isin(SOURCE_ORDER)),
    "table_id": Column(str),
    "original_variable": Column(str),
    "tipo_original": Column(str),
    "tipo_matriz": Column(str, Check.isin(["numeric", "binary", "ordinal", "categorical"])),
    "unit": Column(str, Check.isin(UNITS)),
    "direction": Column(str, Check.isin(DIRECTIONS)),
    "bloque_tematico": Column(str, Check.isin(BLOCKS)),
    "regla_temporal_default": Column(str),
    "regla_transformacion": Column(str),
    "is_primary": Column(bool, coerce=True),
    "redundant_with": Column(str, nullable=True, coerce=True),
    "pct_complete": Column(float, Check.in_range(0, 100), coerce=True),
    "n_countries_available": Column(int, Check.ge(0), coerce=True),
    "fase4_role": Column(str, Check.isin(["core_eda", "supporting_context", "excluded_from_eda"])),
    "included_in_fase4_eda": Column(bool, coerce=True),
    "known_limitations": Column(str, nullable=True, coerce=True),
    "human_review_status": Column(str),
    "notes": Column(str, nullable=True, coerce=True),
}, strict=True, ordered=True, coerce=True)


TraceabilitySchema = pa.DataFrameSchema({
    "cell_id_wide": Column(str, unique=True),
    "cell_id_snapshot": Column(str),
    "cell_id_panel": Column(str),
    "iso3": Column(str, Check.str_matches(r"^[A-Z]{3}$")),
    "variable_matriz": Column(str),
    "source_id": Column(str, Check.isin(SOURCE_ORDER)),
    "source_file": Column(str),
    "source_sheet": Column(str),
    "original_variable": Column(str),
    "row_identifier": Column(str),
    "year_used": Column(str, nullable=True, coerce=True),
    "snapshot_rule": Column(str),
    "confidence_level": Column(str, Check.isin(CONFIDENCE)),
    "extraction_rule": Column(str),
}, strict=True, ordered=True, coerce=True)


def validate_core(panel, snapshot, dictionary, traceability) -> None:
    PanelSchema.validate(panel, lazy=True)
    SnapshotSchema.validate(snapshot, lazy=True)
    DictionarySchema.validate(dictionary, lazy=True)
    TraceabilitySchema.validate(traceability, lazy=True)
