from pathlib import Path

BUNDLE = Path("FASE5/outputs/phase6_ready")


def test_phase6_bundle_has_membership_not_split():
    if not BUNDLE.exists():
        return
    assert (BUNDLE / "phase6_analysis_sample_membership.csv").exists()
    assert not (BUNDLE / "phase6_train_test_split.csv").exists()
