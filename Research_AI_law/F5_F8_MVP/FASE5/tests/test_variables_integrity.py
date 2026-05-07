from __future__ import annotations

from _common.load import load_dictionary
from FASE5.src.variables import (
    build_variable_catalog,
    get_mvp_variables,
    validate_mvp_variables_exist,
)


def test_mvp_variables_are_real_unique_phase3_variables():
    dictionary = load_dictionary()
    variables = get_mvp_variables()

    validate_mvp_variables_exist(dictionary)
    assert len(variables) == 46
    assert len(set(variables)) == 46
    assert set(variables).issubset(set(dictionary["variable_matriz"]))


def test_mvp_variable_catalog_is_complete():
    catalog = build_variable_catalog()

    assert catalog.shape[0] == 46
    assert catalog["variable_matriz"].is_unique
    assert catalog["rol_mvp"].notna().all()
    assert catalog["razon"].notna().all()
