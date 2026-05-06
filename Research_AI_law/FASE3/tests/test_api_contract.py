from src.fase3.api import (
    get_block,
    get_chile_snapshot,
    list_versions,
    load_dictionary,
    load_panel,
    load_snapshot,
    load_wide,
)


def test_public_api_loaders_work():
    assert not load_wide().empty
    assert not load_panel().empty
    assert not load_snapshot().empty
    assert not load_dictionary().empty
    assert "1.0" in list_versions()


def test_public_api_block_and_chile():
    regulatory = get_block("regulatory_treatment")
    chile = get_chile_snapshot()
    assert "iso3" in regulatory.columns
    assert (chile["iso3"] == "CHL").all()
    assert not chile.empty
