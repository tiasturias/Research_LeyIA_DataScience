.PHONY: fase6-env fase6-all fase6-test fase6-notebook fase6-validate-no-pca

fase6-env:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -e ..

fase6-all:
	python3 -m src.run_all

fase6-test:
	python3 -m pytest tests/ -v

fase6-notebook:
	jupyter nbconvert --to notebook --execute --inplace notebooks/06_modeling.ipynb

fase6-validate-no-pca:
	@echo "Checking no PCA files in outputs..."
	@test ! -f outputs/pca_*.csv || (echo "FAIL: pca_* files found" && exit 1)
	@echo "Checking no _common_diagnostics.py in src..."
	@test ! -f src/_common_diagnostics.py || (echo "FAIL: _common_diagnostics.py found" && exit 1)
	@echo "Checking no sklearn.decomposition.PCA imports..."
	@grep -r "sklearn.decomposition" src/ && (echo "FAIL: PCA import found" && exit 1) || true
	@echo "PASS: No PCA artifacts found"
