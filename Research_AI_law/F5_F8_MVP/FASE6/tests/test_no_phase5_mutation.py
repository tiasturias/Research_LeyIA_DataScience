"""Test no Phase 5 mutation: hashes Fase 5 iguales antes/después de Fase 6."""

import hashlib
import json
from pathlib import Path

FASE6_ROOT = Path(__file__).resolve().parents[1]
FASE5_BUNDLE = FASE6_ROOT.parent / "FASE5" / "outputs" / "phase6_ready"


def test_fase5_hashes_unchanged():
    pre_file = FASE6_ROOT / "_fase5_hashes_pre_fase6.json"
    assert pre_file.exists(), "Pre-Fase6 hash file missing"
    with open(pre_file) as f:
        pre = json.load(f)
    for fname, expected_hash in pre["hashes"].items():
        p = FASE5_BUNDLE / fname
        if not p.exists():
            continue
        actual = hashlib.sha256(p.read_bytes()).hexdigest()
        assert actual == expected_hash, f"Fase 5 mutated: {fname}"
