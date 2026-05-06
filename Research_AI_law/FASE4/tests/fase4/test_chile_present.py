"""Test: Chile aparece correctamente en todos los outputs relevantes."""

import pytest
from pathlib import Path

OUTPUTS = Path(__file__).resolve().parents[2] / "outputs" / "eda_principal"


def test_chile_in_country_profiles(wide, dictionary):
    from fase4.countries import compute_country_profiles
    profiles = compute_country_profiles(wide, dictionary)
    assert "CHL" in profiles["iso3"].values, "Chile no está en country_profiles"


def test_chile_profile_has_key_blocks(wide, dictionary):
    from fase4.countries import compute_country_profiles, compute_chile_profile
    profiles = compute_country_profiles(wide, dictionary)
    chile = compute_chile_profile(wide, dictionary, profiles)
    assert "iso3" in chile
    assert chile["iso3"] == "CHL"
    # Chile debe tener cobertura en bloques principales
    for block in ["ecosystem_outcome", "socioeconomic_control", "institutional_control"]:
        assert f"pct_coverage_{block}" in chile, f"Falta cobertura de {block} en perfil Chile"
        assert chile[f"pct_coverage_{block}"] > 50, f"Cobertura de Chile en {block} es muy baja"


def test_chile_in_submuestras(wide, dictionary):
    from fase4.submuestras import build_submuestras
    summary, membership = build_submuestras(wide, dictionary)
    chile = membership[membership["iso3"] == "CHL"]
    assert len(chile) == 1
    # Al menos en oecd_plus_latam y full
    assert chile["oecd_plus_latam"].iloc[0] == 1, "Chile no está en oecd_plus_latam"
    assert chile["full"].iloc[0] == 1, "Chile no está en full"


def test_coverage_analysis_runs(wide, dictionary):
    from fase4.coverage import compute_quality_overview
    overview = compute_quality_overview(wide, dictionary)
    assert len(overview) > 0
    metrics = overview["metric"].tolist()
    assert "n_countries" in metrics
    assert "chile_pct_coverage" in metrics
