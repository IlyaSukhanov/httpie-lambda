.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

format: ## auto format all code
	isort httpie_lambda.py setup.py tests
	black httpie_lambda.py setup.py tests

isort: ## check imports with isort
	isort -c httpie_lambda.py setup.py tests

black: ## check formatting with black
	black --check httpie_lambda.py setup.py tests

lint: ## check style with flake8
	flake8 httpie_lambda.py setup.py tests

test-security:
	bandit httpie_lambda.py

test: ## run tests quickly with the default Python
	py.test tests --cov=httpie_lambda --cov-fail-under=100 --cov-report term-missing -s

test-all: isort black lint test-security test

install: clean ## install the package to the active Python's site-packages
	pip install . --upgrade

install-dev: clean
	pip install -e '.[testing]' --upgrade

publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*
