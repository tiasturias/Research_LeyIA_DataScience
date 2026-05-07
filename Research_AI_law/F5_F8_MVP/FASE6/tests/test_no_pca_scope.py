"""Test no PCA scope: no pca_* files, no _common_diagnostics.py, no PCA imports."""

from pathlib import Path
import ast

FASE6_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE6_ROOT / "outputs"
SRC = FASE6_ROOT / "src"


def test_no_pca_files_in_outputs():
    pca_files = [f for f in OUTPUTS.iterdir() if "pca" in f.name.lower()]
    assert not pca_files, f"PCA files found in outputs: {pca_files}"


def test_no_common_diagnostics_module():
    diag = SRC / "_common_diagnostics.py"
    assert not diag.exists(), "_common_diagnostics.py should not exist"


def test_no_pca_imports_in_src():
    for py_file in SRC.glob("*.py"):
        if py_file.name == "__init__.py":
            continue
        content = py_file.read_text()
        assert "sklearn.decomposition" not in content, \
            f"{py_file.name} imports sklearn.decomposition (PCA)"
        assert "from sklearn.decomposition" not in content, \
            f"{py_file.name} imports from sklearn.decomposition"
