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
	@echo "    make install              install project in system (global)"
	@echo "    make check                check PEP8 compliance (and others)"
	@echo "    make test                 run tests (use 'sudo' to run all)"
	@echo "    make check-coverage       run tests and check coverage (use 'sudo' to run all)"
	@echo "    make clean                cleanup temporary files"
	@echo "    make install-develop      install project in develop mode (virtual environment)"
	@echo "    make prepare              prepare stuff (build, dist, etc) before publishing"
	@echo "    make publish-test         test publishing a version (PyPI Test)"
	@echo "    make install-pypitest     test install project (from PyPI Test)"
	@echo "    make publish              publish a version (GitHub / PyPI)"


# Tests

check:
	check-manifest
	flake8 $(PACKAGE) $(TEST_PACKAGE)

test:
	python setup.py test

test-with-coverage:
	coverage run setup.py test
	coverage lcov

check-coverage: test-with-coverage
	coverage html
	@echo
	@echo "Check coverage results at"
	@echo
	@tput setaf 2
	@echo "    http://localhost:8000"
	@tput sgr0
	@echo
	cd htmlcov && python -m http.server


# Install

install: 
	python setup.py install


# Development

install-develop:
	virtualenv $(VENV)
	. $(VENV)/bin/activate && pip install --upgrade pip
	. $(VENV)/bin/activate && pip install -r requirements-dev.txt
	. $(VENV)/bin/activate && python setup.py develop

install-pypitest:
	virtualenv $(VENV)
	. $(VENV)/bin/activate && pip install \
		--index-url https://test.pypi.org/simple/ $(NAME)==$(VERSION)


# Publish (release)

prepare:
	python setup.py sdist
	python setup.py bdist_wheel

# To use this command, you should have pypitest configured in your ~/.pypirc.
publish-pypitest: prepare
	twine upload --repository testpypi dist/*

publish-pypi: prepare
	twine upload dist/*

publish-github:
	git tag "v$(VERSION)"
	git push origin "v$(VERSION)"

check-publish-test:
	pip index versions --index https://testpypi.python.org/pypi/ $(NAME) | grep -o "Available versions: $(VERSION)"

after-publish-sleep:
	sleep 30

check-publish:
	pip index versions $(NAME) | grep -o "Available versions: $(VERSION)"

publish-test: publish-pypitest after-publish-sleep check-publish-test

publish: publish-github publish-pypi after-publish-sleep check-publish


# Clean

clean-build:
	rm -Rf build/
	rm -Rf dist/
	rm -Rf *.egg-info

clean-coverage-report:
	rm -f .coverage
	rm -f coverage.lcov
	rm -Rf htmlcov

clean-pyc:
	find . -name "*.pyc" -type f -delete

clean: clean-build clean-coverage-report clean-pyc

