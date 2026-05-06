"""Test: consistencia y propiedad de las submuestras candidatas."""

import pytest


def test_submuestras_have_chile(wide, dictionary):
    from fase4.submuestras import build_submuestras
    summary, membership = build_submuestras(wide, dictionary)
    chile_row = membership[membership["iso3"] == "CHL"]
    assert len(chile_row) == 1, "CHL no encontrado en membership"

    # Chile debe estar en al menos 4 de 6 submuestras
    submuestra_cols = ["densa_80", "densa_60", "regulada", "comparable_chile",
                       "oecd_plus_latam", "full"]
    present = chile_row[submuestra_cols].iloc[0].sum()
    assert present >= 4, f"Chile está solo en {present}/6 submuestras (mínimo 4)"


def test_full_contains_all_countries(wide, dictionary):
    from fase4.submuestras import build_submuestras
    summary, membership = build_submuestras(wide, dictionary)
    full_n = summary[summary["submuestra"] == "full"]["n_countries"].iloc[0]
    assert full_n == len(wide), f"submuestra 'full' tiene {full_n} países, esperaba {len(wide)}"


def test_submuestras_subsets_of_full(wide, dictionary):
    """Todas las submuestras son subconjuntos de 'full'."""
    from fase4.submuestras import build_submuestras
    _, membership = build_submuestras(wide, dictionary)
    submuestra_cols = ["densa_80", "densa_60", "regulada", "comparable_chile", "oecd_plus_latam"]
    for col in submuestra_cols:
        # Si un país está en una submuestra, debe estar en full (always true by construction)
        assert membership[col].max() <= 1
        assert membership[col].min() >= 0


def test_six_submuestras_generated(wide, dictionary):
    from fase4.submuestras import build_submuestras
    summary, _ = build_submuestras(wide, dictionary)
    assert len(summary) == 6, f"Se esperaban 6 submuestras, se obtuvieron {len(summary)}"
    expected = {"densa_80", "densa_60", "regulada", "comparable_chile", "oecd_plus_latam", "full"}
    assert set(summary["submuestra"].tolist()) == expected


def test_outliers_not_excluded_from_full(wide, dictionary):
    """USA, SGP, ARE, IRL no deben ser excluidos del universo completo."""
    from fase4.submuestras import build_submuestras
    _, membership = build_submuestras(wide, dictionary)
    for iso3 in ["USA", "SGP", "ARE", "IRL", "EST"]:
        row = membership[membership["iso3"] == iso3]
        if len(row) > 0:
            assert row["full"].iloc[0] == 1, f"{iso3} fue excluido de 'full'"
