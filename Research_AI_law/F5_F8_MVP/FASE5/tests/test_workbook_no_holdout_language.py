from pathlib import Path
import openpyxl

WORKBOOK = Path("FASE5/outputs/MVP_AUDITABLE.xlsx")

FORBIDDEN_PHRASES = [
    "split para modelado",
    "partición train/test",
    "particion train/test",
    "test set independiente",
    "holdout externo",
    "phase6_train_test_split",
    "mvp_train_test_split",
]


def test_workbook_no_holdout_language():
    if not WORKBOOK.exists():
        return
    wb = openpyxl.load_workbook(WORKBOOK, data_only=True)
    texts = []
    for ws in wb.worksheets:
        for row in ws.iter_rows(values_only=True):
            for cell in row:
                if isinstance(cell, str):
                    texts.append(cell.lower())
    joined = "\n".join(texts)
    for phrase in FORBIDDEN_PHRASES:
        assert phrase.lower() not in joined, f"Forbidden phrase in workbook: {phrase}"
