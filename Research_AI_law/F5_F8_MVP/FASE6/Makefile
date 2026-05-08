.PHONY: fase6-env fase6-all fase6-test fase6-notebook fase6-validate-no-pca fase6-2 fase6-2-test

fase6-env:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -e ..

fase6-all:
	python3 -m src.run_all
	python3 -m FASE6.src.country_intelligence.run_country_intelligence

fase6-2:
	python3 -m FASE6.src.country_intelligence.run_country_intelligence

fase6-test:
	python3 -m pytest tests/ -v

fase6-2-test:
	python3 -m pytest tests/test_phase6_2_country_intelligence.py -v

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

fase6-2-validate-preservation:
	@echo "Validating original Phase 6 outputs preserved..."
	@for f in fase6_manifest.json q1_results.csv q2_results.csv q2_scores_per_country.csv q3_results.csv q4_clusters.csv q4_distance_matrix.csv q5_results.csv q5_scores_per_country.csv q6_results.csv q6_scores_per_country.csv; do \
		test -f outputs/$$f || (echo "FAIL: $$f missing" && exit 1); \
	done
	@echo "PASS: All 11 original outputs preserved"
