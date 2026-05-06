"""Test: contrato de datos de Fase 3 (shape, Chile, bloques)."""

import pytest


def test_wide_shape(wide):
    assert wide.shape[0] == 199, f"Se esperaban 199 países, se obtuvieron {wide.shape[0]}"


def test_wide_has_expected_min_columns(wide):
    assert wide.shape[1] >= 100, "Wide tiene menos columnas de lo esperado"


def test_all_country_iso3(wide):
    assert (wide["entity_type"] == "country_iso3").all(), \
        "No todos los registros tienen entity_type == country_iso3"


def test_chile_present(wide):
    assert "CHL" in wide["iso3"].values, "Chile (CHL) no está en la wide"


def test_chile_coverage(wide, dictionary):
    from fase4.load import get_variable_cols
    var_cols = get_variable_cols(wide, dictionary)
    chile_row = wide[wide["iso3"] == "CHL"][var_cols]
    pct = chile_row.notna().sum().sum() / len(var_cols) * 100
    assert pct > 80, f"Chile tiene cobertura {pct:.1f}% < 80% esperado"


def test_blocks_in_dictionary(dictionary):
    from fase4.config import BLOCKS
    blocks_in_dict = dictionary["bloque_tematico"].unique().tolist()
    for block in BLOCKS:
        assert block in blocks_in_dict, f"Bloque {block} no encontrado en diccionario"


def test_country_name_canonical_no_iso3_leak(wide):
    """Verificar que country_name_canonical no contiene ISO3 raw (bug v1.0 corregido en v1.1)."""
    iso3_set = set(wide["iso3"].tolist())
    leaked = wide[wide["country_name_canonical"].isin(iso3_set)]
    assert len(leaked) == 0, \
        f"country_name_canonical contiene ISO3 raw en {len(leaked)} filas: {leaked['iso3'].tolist()[:5]}"


def test_no_duplicate_iso3(wide):
    assert wide["iso3"].duplicated().sum() == 0, "Hay ISO3 duplicados en wide"
