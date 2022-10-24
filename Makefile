# update-conf.py Makefile

PACKAGE=update_conf_py
NAME=update-conf.py
CONF=$(NAME).conf
PREFIX=/usr/local
ETC=/etc
VENV=venv
TEST_PACKAGE=tests

VERSION=$(shell python setup.py --version)


all: help

help:
	@echo "Usage:"
	@echo
	@echo "    make install                  install project in system (global)"
	@echo "    make install-develop          install project in develop mode (virtual env with test and build tools)"
	@echo "    make check                    run checks (like PEP8 compliance)"
	@echo "    make test                     run tests (use 'sudo' to run all)"
	@echo "    make test-with-coverage       run tests with coverage (use 'sudo' to run all)"
	@echo "    make coverage-report          generate coverage report in html"
	@echo "    make build                    build (sdist and bdist_wheel)"
	@echo "    make check-and-test-publish   run checks and test the process of publishing a version (using Test PyPI)"
	@echo "    make tag-for-publish          push tag version on GitHub (which triggers the CI/CD pipeline to publish the version on PyPI"
	@echo "    make clean                    cleanup temporary files"


# Install

install:
	python setup.py install


# Development

install-develop:
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate && python -m pip install -r requirements-dev.txt
	. $(VENV)/bin/activate && python setup.py develop
	@echo
	@echo "Environment setup done. Remember to activate your virtual env."
	@echo
	@tput setaf 2
	@echo "    . $(VENV)/bin/activate"
	@tput sgr0


# Tests and checks

check:
	check-manifest
	flake8 $(PACKAGE) $(TEST_PACKAGE)

test:
	python setup.py test

test-with-coverage:
	coverage run setup.py test
	coverage lcov

coverage-report:
	coverage html
	@echo
	@echo "Check coverage results at"
	@echo
	@tput setaf 2
	@echo "    http://localhost:8000"
	@tput sgr0
	@echo
	cd htmlcov && python -m http.server

check-build:
	check-wheel-contents dist/*.whl
	python -m twine check dist/*

install-from-testpipy:
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate && python -m pip install -i https://test.pypi.org/simple/ $(NAME)==$(VERSION)


# Build

build: clean-build clean-dist
	python setup.py sdist bdist_wheel


# Test publish

publish-testpypi:
	twine upload -r testpypi dist/*

check-and-test-publish: build check-build publish-testpypi
	@echo
	@echo "Test of publishing on Test PyPI done. If necessary, remember to test install from Test PyPI."
	@echo
	@tput setaf 2
	@echo "    deactivate"
	@echo "    rm -Rf $(VENV)"
	@echo "    make install-from-testpypi"
	@tput sgr0


# Tag for publish

# It will trigger a CI/CD pipeline that will ending up on publishing on PyPI.
tag-for-publish:
	git tag "v$(VERSION)"
	git push origin "v$(VERSION)"


# Clean

clean-build:
	python setup.py clean --all

clean-dist:
	rm -Rf dist

clean-egg:
	rm -Rf *.egg-info
	rm -Rf .eggs

clean-coverage:
	rm -f .coverage
	rm -f coverage.lcov
	rm -Rf htmlcov

clean-pyc:
	find . -name "*.pyc" -type f -delete

clean: clean-build clean-dist clean-egg clean-coverage clean-pyc
