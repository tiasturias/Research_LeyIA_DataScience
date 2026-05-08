from pathlib import Path
import pandas as pd

FASE6_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = FASE6_ROOT / "outputs"


def test_no_loocv_auc_or_r2_as_valid_metric():
    if not OUTPUTS.exists():
        return
    for path in OUTPUTS.glob("q*_results.csv"):
        df = pd.read_csv(path)
        for col in df.columns:
            lc = col.lower()
            if "loocv" in lc and ("auc" in lc or "r2" in lc):
                # Puede existir, pero debe ser NaN y tener nota explicativa.
                assert df[col].isna().all(), f"{path.name}:{col} debe ser NaN"
        note_cols = [c for c in df.columns if "loocv_note" in c.lower()]
        for c in note_cols:
            assert df[c].astype(str).str.contains("undefined|not_computed|not applicable", case=False, na=False).any()
