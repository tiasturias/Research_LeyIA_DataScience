from __future__ import annotations

from _common.load import load_wide
from FASE5.src.sample import filter_to_mvp_sample, get_mvp_iso3


def test_mvp_sample_has_43_preregistered_entities():
    iso3 = get_mvp_iso3()

    assert len(iso3) == 43
    assert len(set(iso3)) == 43
    assert "CHL" in iso3


def test_mvp_sample_entities_exist_and_are_countries():
    wide = load_wide()
    wide_mvp = filter_to_mvp_sample(wide)

    assert wide_mvp.shape[0] == 43
    assert set(wide_mvp["iso3"]) == set(get_mvp_iso3())
    assert wide_mvp["entity_type"].eq("country_iso3").all()
    assert wide_mvp["country_name_canonical"].notna().all()
