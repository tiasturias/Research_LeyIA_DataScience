"""Utilidades de clasificación: binarización, Logistic, Random Forest."""

from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import (
    cross_val_score, RepeatedKFold, StratifiedKFold, LeaveOneOut, cross_val_predict,
)
from sklearn.metrics import (
    roc_auc_score, confusion_matrix, classification_report,
)


def binarize_by_median(s: pd.Series) -> tuple[pd.Series, float]:
    """Y_binary = 1 si país está sobre la mediana."""
    median = float(s.median())
    return (s >= median).astype(int), median


def fit_logistic_cv(
    df: pd.DataFrame, y_binary: str, x_cols: list[str],
    cv_repeats: int = 10, cv_splits: int = 5, seed: int = 42,
) -> dict:
    """Logistic regression con CV repetida + LOOCV sanity."""
    sub = df[[y_binary] + x_cols].dropna()
    if len(sub) < 20:
        return {"status": "insufficient_n", "n": len(sub)}
    X = sub[x_cols].values
    y = sub[y_binary].values

    cv = RepeatedKFold(n_splits=cv_splits, n_repeats=cv_repeats, random_state=seed)
    logreg = LogisticRegression(
        penalty="l2", C=1.0, max_iter=1000,
        class_weight="balanced", random_state=seed,
    )
    auc_cv = cross_val_score(logreg, X, y, cv=cv, scoring="roc_auc")

    loo = LeaveOneOut()
    auc_loo = cross_val_score(logreg, X, y, cv=loo, scoring="roc_auc").mean()

    full = LogisticRegression(
        penalty="l2", C=1.0, max_iter=1000,
        class_weight="balanced", random_state=seed,
    ).fit(X, y)

    try:
        y_pred = cross_val_predict(logreg, X, y, cv=StratifiedKFold(n_splits=cv_splits, shuffle=True, random_state=seed), method="predict")
        cm = confusion_matrix(y, y_pred)
        cm_tn, cm_fp, cm_fn, cm_tp = int(cm[0, 0]), int(cm[0, 1]), int(cm[1, 0]), int(cm[1, 1])
    except Exception:
        cm_tn, cm_fp, cm_fn, cm_tp = None, None, None, None

    return {
        "status": "ok",
        "n": len(sub),
        "n_class_0": int((y == 0).sum()),
        "n_class_1": int((y == 1).sum()),
        "auc_cv_5fold_mean": float(auc_cv.mean()),
        "auc_cv_5fold_std": float(auc_cv.std()),
        "auc_loocv": float(auc_loo),
        "logistic_coef": dict(zip(x_cols, full.coef_[0].tolist())),
        "logistic_intercept": float(full.intercept_[0]),
        "confusion_tn": cm_tn,
        "confusion_fp": cm_fp,
        "confusion_fn": cm_fn,
        "confusion_tp": cm_tp,
    }


def fit_random_forest_cv(
    df: pd.DataFrame, y_binary: str, x_cols: list[str],
    n_estimators: int = 300, max_depth: int = 4,
    min_samples_leaf: int = 3, seed: int = 42,
    cv_repeats: int = 10, cv_splits: int = 5,
) -> dict:
    """Random Forest con CV repetida + feature importance."""
    sub = df[[y_binary] + x_cols].dropna()
    if len(sub) < 20:
        return {"status": "insufficient_n", "n": len(sub)}
    X = sub[x_cols].values
    y = sub[y_binary].values

    cv = RepeatedKFold(n_splits=cv_splits, n_repeats=cv_repeats, random_state=seed)
    rf = RandomForestClassifier(
        n_estimators=n_estimators, max_depth=max_depth,
        min_samples_leaf=min_samples_leaf, random_state=seed,
    )
    auc_cv = cross_val_score(rf, X, y, cv=cv, scoring="roc_auc")

    loo = LeaveOneOut()
    auc_loo = cross_val_score(rf, X, y, cv=loo, scoring="roc_auc").mean()

    full = RandomForestClassifier(
        n_estimators=n_estimators, max_depth=max_depth,
        min_samples_leaf=min_samples_leaf, random_state=seed,
    ).fit(X, y)

    return {
        "status": "ok",
        "n": len(sub),
        "auc_cv_5fold_mean": float(auc_cv.mean()),
        "auc_cv_5fold_std": float(auc_cv.std()),
        "auc_loocv": float(auc_loo),
        "feature_importance": dict(zip(x_cols, full.feature_importances_.tolist())),
    }
