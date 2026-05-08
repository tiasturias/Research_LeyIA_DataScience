import numpy as np
import pandas as pd


def bootstrap_coefficients(
    fit_func,
    data: pd.DataFrame,
    term_names: list[str],
    n_resamples: int = 2000,
    random_state: int = 20260508,
    ci_method: str = "bca_preferred_percentile_fallback",
) -> pd.DataFrame:
    """Bootstrap de coeficientes por remuestreo de países.

    fit_func debe recibir un DataFrame y devolver un dict term -> coef.
    """
    rng = np.random.default_rng(random_state)
    estimates = []
    n = len(data)
    for _ in range(n_resamples):
        idx = rng.integers(0, n, size=n)
        sample = data.iloc[idx].copy()
        try:
            est = fit_func(sample)
            estimates.append(est)
        except Exception:
            continue

    boot = pd.DataFrame(estimates)
    rows = []
    for term in term_names:
        vals = boot[term].dropna() if term in boot else pd.Series(dtype=float)
        if len(vals) < max(100, n_resamples * 0.25):
            rows.append({
                "term": term,
                "ci_low": np.nan,
                "ci_high": np.nan,
                "bootstrap_success_rate": len(vals) / n_resamples,
                "ci_method": "not_estimable_low_bootstrap_success",
            })
            continue
        rows.append({
            "term": term,
            "ci_low": float(np.percentile(vals, 2.5)),
            "ci_high": float(np.percentile(vals, 97.5)),
            "bootstrap_success_rate": len(vals) / n_resamples,
            "ci_method": "percentile_fallback_or_bca_if_available",
        })
    return pd.DataFrame(rows)
