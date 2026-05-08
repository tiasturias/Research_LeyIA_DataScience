from pathlib import Path

FASE5_OUTPUTS = Path("FASE5/outputs")


def test_no_train_test_outputs_exist():
    forbidden = [
        FASE5_OUTPUTS / "mvp_train_test_split.csv",
        FASE5_OUTPUTS / "phase6_ready" / "phase6_train_test_split.csv",
    ]
    for path in forbidden:
        assert not path.exists(), f"Forbidden split output exists: {path}"
