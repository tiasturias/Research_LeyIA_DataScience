"""Test bundle integrity: hashes Fase 5 11/11."""

import hashlib
import json
from pathlib import Path

FASE5_BUNDLE = Path(__file__).resolve().parents[2] / "FASE5" / "outputs" / "phase6_ready"


def test_bundle_hashes_all_ok():
    with open(FASE5_BUNDLE / "phase6_ready_manifest.json") as f:
        manifest = json.load(f)
    errors = []
    for fname, meta in manifest.get("files", {}).items():
        p = FASE5_BUNDLE / fname
        assert p.exists(), f"Missing: {fname}"
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        if h != meta["sha256"]:
            errors.append(f"Hash mismatch: {fname}")
    assert not errors, f"Bundle integrity FAIL: {errors}"


def test_bundle_has_11_hashed_files():
    with open(FASE5_BUNDLE / "phase6_ready_manifest.json") as f:
        manifest = json.load(f)
    assert len(manifest["files"]) == 11


def test_feature_matrix_shape():
    import pandas as pd
    fm = pd.read_csv(FASE5_BUNDLE / "phase6_feature_matrix.csv")
    assert fm.shape == (43, 138), f"Expected (43, 138), got {fm.shape}"
