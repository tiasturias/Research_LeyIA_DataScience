"""Test: análisis de cobertura y missingness."""

import pytest


def test_missingness_by_variable_shape(wide, dictionary):
    from fase4.coverage import compute_missingness_by_variable
    result = compute_missingness_by_variable(wide, dictionary)
    assert len(result) == len(dictionary), \
        f"Missingness by variable: {len(result)} rows, expected {len(dictionary)}"
    assert "pct_complete" in result.columns


def test_missingness_by_country_shape(wide, dictionary):
    from fase4.coverage import compute_missingness_by_country
    result = compute_missingness_by_country(wide, dictionary)
    assert len(result) == len(wide)
    assert "pct_vars_available" in result.columns


def test_iapp_coverage_bottleneck(wide, dictionary):
    """IAPP debe mostrar cobertura ~14% (~28 países) — bottleneck documentado."""
    from fase4.coverage import compute_missingness_by_block
    result = compute_missingness_by_block(wide, dictionary)
    reg = result[result["bloque_tematico"] == "regulatory_treatment"]
    assert len(reg) == 1
    # La cobertura IAPP debe ser baja (bottleneck). El bloque regulatorio
    # también contiene variables Stanford con mayor cobertura, por eso el
    # diagnóstico correcto se hace sobre columnas iapp_*.
    coverage = reg["n_countries_with_any_iapp_data"].iloc[0]
    assert coverage <= 50, \
        f"regulatory_treatment tiene {coverage} países — más de lo esperado para IAPP"


def test_tech_infrastructure_full_coverage(wide, dictionary):
    """tech_infrastructure_control debe tener cobertura del 100%."""
    from fase4.coverage import compute_missingness_by_block
    result = compute_missingness_by_block(wide, dictionary)
    tech = result[result["bloque_tematico"] == "tech_infrastructure_control"]
    assert len(tech) == 1
    pct = tech["pct_countries_with_any_data"].iloc[0]
    assert pct >= 95, f"tech_infrastructure tiene {pct}% cobertura, esperado ≥95%"
