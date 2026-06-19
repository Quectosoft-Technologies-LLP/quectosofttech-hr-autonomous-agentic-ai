.PHONY: install test lint typecheck verify run
install:
	pip install -e .[dev]

test:
	pytest -q

lint:
	ruff check src tests

typecheck:
	mypy src

verify:
	python setup.py && pytest -q && ruff check src tests

run:
	uvicorn quectosoft_hr.api:app --host 0.0.0.0 --port 8000 --workers 2
