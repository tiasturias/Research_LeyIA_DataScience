"""Exportación de country cards data para países clave."""

from pathlib import Path
import pandas as pd

KEY_COUNTRIES = ["CHL", "SGP", "EST", "IRL", "ARE", "KOR", "JPN", "USA", "CHN", "BRA", "URY"]


def write_country_card_data(
    profile_wide: pd.DataFrame,
    profile_long: pd.DataFrame,
    rankings_group: pd.DataFrame,
    contributions: pd.DataFrame,
    residuals: pd.DataFrame,
    outdir: Path,
):
    card_dir = outdir / "country_cards_data"
    card_dir.mkdir(parents=True, exist_ok=True)

    written = []
    for iso in KEY_COUNTRIES:
        pieces = []
        pw = profile_wide[profile_wide["iso3"] == iso].copy()
        if not pw.empty:
            pw["section"] = "summary"
            pieces.append(pw)

        pl = profile_long[profile_long["iso3"] == iso].copy()
        if not pl.empty:
            pl["section"] = "q_profile_long"
            pieces.append(pl)

        rg = rankings_group[rankings_group["iso3"] == iso].copy()
        if not rg.empty:
            rg["section"] = "group_rankings"
            pieces.append(rg)

        co = contributions[contributions["iso3"] == iso].copy() if not contributions.empty else pd.DataFrame()
        if not co.empty:
            co["section"] = "model_contributions"
            pieces.append(co)

        rs = residuals[residuals["iso3"] == iso].copy() if not residuals.empty else pd.DataFrame()
        if not rs.empty:
            rs["section"] = "residuals"
            pieces.append(rs)

        if pieces:
            card = pd.concat(pieces, ignore_index=True, sort=False)
            path = card_dir / f"{iso}_country_card_data.csv"
            card.to_csv(path, index=False)
            written.append(str(path))

    readme = card_dir / "README_country_cards.md"
    readme.write_text(
        "# Country cards data\n\n"
        "Estos archivos consolidan datos descriptivos país-por-país para Fase 8. "
        "No son predicciones independientes ni inferencias causales.\n",
        encoding="utf-8"
    )
    return written
