.PHONY: fase5-build fase5-test fase5-validate fase5-notebook fase5-all

fase5-build:
	python3 -m FASE5.src.build

fase5-test:
	pytest FASE5/tests -v

fase5-validate:
	python3 -m FASE5.src.validate

fase5-notebook:
	jupyter nbconvert --to notebook --execute --inplace FASE5/notebooks/05_data_preparation.ipynb

fase5-all: fase5-build fase5-test fase5-validate fase5-notebook
