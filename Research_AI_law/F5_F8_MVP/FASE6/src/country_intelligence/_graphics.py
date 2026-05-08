"""Generación de gráficos profesionales para Fase 6.2."""

from pathlib import Path
import textwrap
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HIGHLIGHTS = {"CHL", "SGP", "EST", "IRL", "ARE", "USA", "CHN", "BRA", "URY"}


def _savefig(fig, path_base: Path):
    path_base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path_base.with_suffix(".png"), dpi=180, bbox_inches="tight")
    fig.savefig(path_base.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def plot_q_ranking(rankings: pd.DataFrame, question_id: str, outdir: Path):
    q = rankings[rankings["question_id"] == question_id].copy()
    if q.empty:
        return []

    agg = (
        q.groupby(["iso3", "country_name"], dropna=False)
         .agg(percentile=("percentile", "mean"))
         .reset_index()
         .sort_values("percentile", ascending=True)
    )
    if agg.empty:
        return []

    fig, ax = plt.subplots(figsize=(9, max(6, len(agg) * 0.18)))
    y = range(len(agg))
    colors = ["#e74c3c" if iso == "CHL" else ("#2ecc71" if iso == "SGP" else ("#3498db" if iso in HIGHLIGHTS else "#95a5a6")) for iso in agg["iso3"]]
    ax.barh(y, agg["percentile"], color=colors, alpha=0.85)
    ax.set_yticks(list(y))
    ax.set_yticklabels([f"{r.iso3} — {r.country_name}" for r in agg.itertuples()], fontsize=7)
    ax.set_xlim(0, 1)
    ax.set_xlabel("Percentil descriptivo dentro de la muestra")
    ax.set_title(f"{question_id}: ranking país por desempeño relativo", fontsize=13)
    ax.text(
        0, -1.4,
        "Nota: posicionamiento descriptivo in-sample; no es predicción independiente ni causalidad.",
        fontsize=8
    )
    path = outdir / "q_rankings" / f"{question_id.lower()}_ranking"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def plot_heatmap_country_by_q(profile_wide: pd.DataFrame, outdir: Path):
    q_cols = [c for c in profile_wide.columns if c.endswith("_percentile")]
    if not q_cols:
        return []

    df = profile_wide.sort_values("overall_country_profile_score", ascending=False).copy()
    mat = df[q_cols].astype(float).values
    fig, ax = plt.subplots(figsize=(8, max(7, len(df) * 0.18)))
    im = ax.imshow(mat, aspect="auto", vmin=0, vmax=1, cmap="RdYlGn")
    ax.set_yticks(range(len(df)))
    ax.set_yticklabels([f"{r.iso3} — {r.country_name}" for r in df.itertuples()], fontsize=7)
    ax.set_xticks(range(len(q_cols)))
    ax.set_xticklabels([c.replace("_percentile", "") for c in q_cols], rotation=45, ha="right")
    ax.set_title("Mapa comparado país × pregunta: percentiles descriptivos", fontsize=13)
    fig.colorbar(im, ax=ax, label="Percentil")
    if "Q4_regulatory_profile" in df.columns:
        for i, (_, r) in enumerate(df.iterrows()):
            q4_info = r.get("Q4_regulatory_profile")
            if pd.notna(q4_info):
                ax.text(len(q_cols) + 0.15, i, str(q4_info)[:30], fontsize=5, va="center", color="#34495e")
        ax.text(len(q_cols) + 0.15, -1, "Q4 (cluster)", fontsize=7, fontweight="bold", va="bottom")
    ax.text(
        0, -3.0,
        "Nota: ranking descriptivo dentro de la muestra preregistrada; no es causalidad. Q4 es tipología de cluster, no percentil.",
        fontsize=8
    )
    path = outdir / "q_heatmaps" / "heatmap_country_by_q_percentiles"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def plot_country_radar(profile_wide: pd.DataFrame, iso3: str, outdir: Path):
    row = profile_wide[profile_wide["iso3"] == iso3]
    if row.empty:
        return []
    row = row.iloc[0]
    q_cols = [c for c in profile_wide.columns if c.endswith("_percentile")]
    labels = [c.replace("_percentile", "") for c in q_cols]
    values = [row[c] if pd.notna(row[c]) else 0 for c in q_cols]
    if not values:
        return []

    q4_profile = row.get("Q4_regulatory_profile", None)
    subtitle = f"Q4: {q4_profile}" if pd.notna(q4_profile) else "Q4: sin datos de cluster"

    angles = np.linspace(0, 2*np.pi, len(values), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, values, linewidth=2, color="#2c3e50")
    ax.fill(angles, values, alpha=0.20, color="#3498db")
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1)
    ax.set_title(f"{iso3} — perfil Q1–Q6\n{subtitle}", fontsize=11)
    fig.text(
        0.1, 0.02,
        "Nota: percentiles descriptivos in-sample; no causalidad. Q4 es tipología de cluster, no ranking normativo.",
        fontsize=8
    )
    path = outdir / "country_cards" / f"{iso3}_country_card_radar"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def plot_chile_vs_singapore(profile_wide: pd.DataFrame, outdir: Path):
    sub = profile_wide[profile_wide["iso3"].isin(["CHL", "SGP"])].copy()
    q_cols = [c for c in profile_wide.columns if c.endswith("_percentile")]
    if len(sub) < 2 or not q_cols:
        return []

    chl_q4 = sub[sub["iso3"]=="CHL"]["Q4_regulatory_profile"].iloc[0] if "Q4_regulatory_profile" in sub.columns and not sub[sub["iso3"]=="CHL"]["Q4_regulatory_profile"].isna().all() else "N/A"
    sgp_q4 = sub[sub["iso3"]=="SGP"]["Q4_regulatory_profile"].iloc[0] if "Q4_regulatory_profile" in sub.columns and not sub[sub["iso3"]=="SGP"]["Q4_regulatory_profile"].isna().all() else "N/A"

    fig, ax = plt.subplots(figsize=(8, 5))
    x = range(len(q_cols))
    colors = {"CHL": "#e74c3c", "SGP": "#2ecc71"}
    for _, r in sub.iterrows():
        ax.plot(x, [r[c] for c in q_cols], marker="o", label=f"{r['iso3']} — {r['country_name']}", color=colors.get(r['iso3'], '#3498db'), linewidth=2)
    ax.set_xticks(x)
    ax.set_xticklabels([c.replace("_percentile", "") for c in q_cols], rotation=45, ha="right")
    ax.set_ylim(0, 1)
    ax.set_ylabel("Percentil")
    ax.set_title(f"Chile vs Singapur — perfil comparado Q1–Q6\nQ4 CHL: {chl_q4} | Q4 SGP: {sgp_q4}", fontsize=11)
    ax.legend()
    ax.text(
        0, -0.24,
        "Nota: comparación descriptiva dentro de la muestra. Q4 es tipología de cluster, no ranking normativo.",
        transform=ax.transAxes,
        fontsize=8
    )
    path = outdir / "chile_vs_benchmarks" / "chile_vs_singapore_q_profile"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def plot_top_bottom_panel(profile_wide: pd.DataFrame, outdir: Path):
    q_cols = [c for c in profile_wide.columns if c.endswith("_percentile")]
    if not q_cols:
        return []

    nq = len(q_cols)
    fig, axes = plt.subplots(nq, 2, figsize=(12, nq * 2.5))
    if nq == 1:
        axes = np.array([axes])

    for i, col in enumerate(q_cols):
        q_label = col.replace("_percentile", "")
        valid = profile_wide[["iso3", "country_name", col]].dropna()
        top5 = valid.nlargest(5, col).sort_values(col, ascending=True)
        bottom5 = valid.nsmallest(5, col).sort_values(col, ascending=True)

        ax_top = axes[i, 0]
        ax_top.barh(range(len(top5)), top5[col], color="#2ecc71", alpha=0.8)
        ax_top.set_yticks(range(len(top5)))
        ax_top.set_yticklabels([f"{r.iso3}" for r in top5.itertuples()], fontsize=8)
        ax_top.set_xlim(0, 1)
        ax_top.set_title(f"{q_label} — Top 5")

        ax_bot = axes[i, 1]
        ax_bot.barh(range(len(bottom5)), bottom5[col], color="#e74c3c", alpha=0.8)
        ax_bot.set_yticks(range(len(bottom5)))
        ax_bot.set_yticklabels([f"{r.iso3}" for r in bottom5.itertuples()], fontsize=8)
        ax_bot.set_xlim(0, 1)
        ax_bot.set_title(f"{q_label} — Bottom 5")

    fig.suptitle("Top 5 y Bottom 5 por dimensión", fontsize=14)
    fig.text(0.5, 0.01, "Nota: posicionamiento descriptivo in-sample; no causalidad.", ha="center", fontsize=8)
    path = outdir / "pioneer_vs_laggard" / "top_bottom_by_q_panel"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def plot_residuals(residuals: pd.DataFrame, outdir: Path):
    if residuals.empty or "observed_value" not in residuals.columns or "fitted_value" not in residuals.columns:
        return []

    sub = residuals.dropna(subset=["observed_value", "fitted_value"]).copy()
    if sub.empty:
        return []

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(sub["fitted_value"], sub["observed_value"], alpha=0.6, color="#34495e")
    lims = [
        sub[["fitted_value", "observed_value"]].min().min(),
        sub[["fitted_value", "observed_value"]].max().max(),
    ]
    ax.plot(lims, lims, "r--", alpha=0.5)
    ax.set_xlabel("Valor ajustado (fitted)")
    ax.set_ylabel("Valor observado")
    ax.set_title("Observado vs Ajustado — residuales descriptivos")
    ax.text(
        0, -0.12,
        "Nota: modelo interno descriptivo; no predicción independiente ni causalidad.",
        transform=ax.transAxes,
        fontsize=8
    )
    path = outdir / "residuals" / "observed_vs_expected_selected_outcomes"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def plot_q4_regulatory_profile_map(profile_wide: pd.DataFrame, outdir: Path):
    if "Q4_regulatory_profile" not in profile_wide.columns:
        return []

    valid = profile_wide.copy()
    if valid.empty:
        return []

    clus = valid.groupby("Q4_regulatory_profile").apply(lambda g: ";".join(sorted(g["iso3"].tolist()))).reset_index(name="countries")
    clus["n"] = clus["countries"].str.count(";") + 1
    clus = clus.sort_values("n", ascending=True)

    n_total = len(valid)
    fig, ax = plt.subplots(figsize=(12, max(5, len(clus) * 0.9)))
    colors_cl = ["#95a5a6", "#3498db", "#e67e22", "#2ecc71", "#9b59b6"]
    bars = ax.barh(range(len(clus)), clus["n"], color=colors_cl[:len(clus)], alpha=0.85)
    ax.set_yticks(range(len(clus)))
    ax.set_yticklabels([f"{r.Q4_regulatory_profile[:65]}" for r in clus.itertuples()], fontsize=7.5)
    ax.set_xlabel(f"Número de países (total: {n_total})")
    ax.set_title(f"Q4 — Perfil Regulatorio: {n_total} países (IAPP + corpus legal)", fontsize=12)

    for i, (_, r) in enumerate(clus.iterrows()):
        ax.text(r["n"] + 0.2, i, f"({r['n']} países)", fontsize=8, va="center")
        countries_short = r["countries"][:90] + ("..." if len(r["countries"]) > 90 else "")
        ax.text(0.5, i - 0.30, countries_short, fontsize=5.5, va="top", color="#7f8c8d")

    source_info = profile_wide["Q4_data_source"].value_counts().to_dict() if "Q4_data_source" in profile_wide.columns else {}
    source_text = f"Fuentes: {source_info}" if source_info else ""
    ax.text(0, -1.8, f"Nota: Q4 combina clustering IAPP (18 países) + conteo de instrumentos regulatorios del corpus legal para los demás países. No es ranking normativo. {source_text}", fontsize=8)
    path = outdir / "clusters" / "q4_regulatory_profile_map"
    _savefig(fig, path)
    return [str(path.with_suffix(".png")), str(path.with_suffix(".svg"))]


def build_graphics(rankings, profile_wide, residuals, outdir: Path) -> pd.DataFrame:
    paths = []
    paths += plot_heatmap_country_by_q(profile_wide, outdir)
    for q in ["Q1", "Q2", "Q3", "Q5", "Q6"]:
        paths += plot_q_ranking(rankings, q, outdir)
    paths += plot_q4_regulatory_profile_map(profile_wide, outdir)
    for iso in ["SGP", "CHL", "EST", "IRL", "ARE", "KOR", "USA", "CHN", "BRA", "URY"]:
        paths += plot_country_radar(profile_wide, iso, outdir)
    paths += plot_chile_vs_singapore(profile_wide, outdir)
    paths += plot_top_bottom_panel(profile_wide, outdir)
    paths += plot_residuals(residuals, outdir)
    return pd.DataFrame({
        "figure_path": paths,
        "figure_type": [Path(p).parent.name for p in paths],
        "methodology_note": "descriptive in-sample positioning; not causal or external prediction",
    })
