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
	@echo "    make uninstall            show tips for uninstalling"
	@echo "    make check                check PEP8 compliance (and others)"
	@echo "    make test                 run tests (use 'sudo' to run all)"
	@echo "    make check-coverage       run tests and check coverage (use 'sudo' to run all)"
	@echo "    make clean                cleanup temporary files"
	@echo "    make install-develop      install project in develop mode (virtual environment)"
	@echo "    make develop-deps-ubuntu  install software dependencies (valid only in Ubuntu)"
	@echo "    make prepare              prepare stuff (build, dist, etc) before publishing"
	@echo "    make publish-test         test publishing a version (PyPI Test)"
	@echo "    make install-pypitest     test install project (from PyPI Test)"
	@echo "    make publish              publish a version (GitHub / PyPI)"


# Tests

check:
	CHECK_MANIFEST=True check-manifest
	python setup.py flake8
# Ignore 'N802' (function name should be lowercase) in tests because we need
# to inherit from the unittest class (that defines the setUp / tearDown
# functions)
	flake8 --ignore=N802 $(TEST_PACKAGE)

test:
	python setup.py test

test-with-coverage:
	coverage run setup.py test

check-coverage: test-with-coverage
	coverage html
	@echo
	@echo "Check coverage results at"
	@echo
	@tput setaf 2
	@echo "    http://localhost:8000"
	@tput sgr0
	@echo
	cd htmlcov && python -m SimpleHTTPServer


# Install

# setup.py does not have a uninstall command. We're only showing a tip.
# See: http://stackoverflow.com/a/1550235/2530295
uninstall:
	@echo "'setup.py' does not have a uninstall command."
	@echo "You can run the follow command to get a list of installed files and "
	@echo "then removing them:"
	@echo
	@echo "    python setup.py install --record files.txt"
	@echo
	@echo "It's also a good practice using 'pip' in a production env."

install: 
	python setup.py install


# Development

develop-deps-ubuntu:
	apt-get install -y pandoc

install-develop:
	virtualenv $(VENV)
	. $(VENV)/bin/activate && pip install -r requirements-dev.txt
	. $(VENV)/bin/activate && python setup.py develop

install-pypitest:
	virtualenv $(VENV)
	. $(VENV)/bin/activate && pip install -r requirements.txt
	. $(VENV)/bin/activate && pip install \
		--index-url=https://testpypi.python.org/pypi/ $(NAME)==$(VERSION)


# Publish (release)

prepare:
	python setup.py generate_rst
	python setup.py sdist
	python setup.py bdist_wheel

# To use this command, you should have pypitest configured in your ~/.pypirc.
publish-pypitest: prepare
	twine upload dist/* -r pypitest

publish-pypi: prepare
	twine upload dist/*

publish-github:
	git tag "v$(VERSION)"
	git push origin "v$(VERSION)"

check-publish-test:
	pip search --index https://testpypi.python.org/pypi/ $(NAME) | grep -o $(VERSION)

check-publish:
	pip search $(NAME) | grep -o $(VERSION)

publish-test: publish-pypitest check-publish-test

publish: publish-github publish-pypi check-publish


# Clean

clean-rst:
	rm -f README.rst

clean-build:
	rm -Rf build/
	rm -Rf dist/
	rm -Rf *.egg-info

clean-coverage-report:
	rm -f .coverage
	rm -Rf htmlcov

clean-pyc:
	find . -name "*.pyc" -type f -delete

clean: clean-rst clean-build clean-coverage-report clean-pyc
