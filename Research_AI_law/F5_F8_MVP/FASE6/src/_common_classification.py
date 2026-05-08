import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score


def fit_binary_median_sensitivity(X, y_binary):
    """Modelo logístico solo para sensibilidad alta/baja, nunca headline."""
    result = {
        "analysis_role": "sensitivity_binary_median",
        "primary_analysis": False,
        "holdout_used": False,
        "validation_scope": "internal_resampling_not_external_test",
    }
    if len(set(y_binary.dropna())) < 2:
        result.update({
            "auc_repeated_kfold": np.nan,
            "auc_note": "not_computed_single_class",
            "loocv_auc": np.nan,
            "loocv_note": "not_computed_auc_undefined_for_single_observation_test_folds",
        })
        return result

    min_class = y_binary.value_counts().min()
    if min_class < 3:
        result.update({
            "auc_repeated_kfold": np.nan,
            "auc_note": "not_computed_too_few_cases_per_class",
            "loocv_auc": np.nan,
            "loocv_note": "not_computed_auc_undefined_for_single_observation_test_folds",
        })
        return result

    k = min(5, int(min_class))
    cv = RepeatedStratifiedKFold(n_splits=k, n_repeats=20, random_state=20260508)
    clf = LogisticRegression(max_iter=2000, solver="liblinear")
    auc = cross_val_score(clf, X, y_binary, scoring="roc_auc", cv=cv)
    result.update({
        "auc_repeated_kfold": float(np.nanmean(auc)),
        "auc_sd": float(np.nanstd(auc)),
        "auc_note": "repeated_stratified_kfold_internal_not_external_test",
        "loocv_auc": np.nan,
        "loocv_note": "not_computed_auc_undefined_for_single_observation_test_folds",
    })
    return result
