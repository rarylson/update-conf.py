# update-conf.py Makefile

PACKAGE=update_conf_py
NAME=update-conf.py
CONF=$(NAME).conf
PREFIX=/usr/local
ETC=/etc
VENV=venv
TEST_PACKAGE=tests


all: help

# TODO Create a help!
help:
	@echo "Did you mean 'make install'?"


# Tests

test-pep8:
	pep8 $(PACKAGE)/*.py $(TEST_PACKAGE)/*.py setup.py

test:
	python setup.py test

test-pypitest:
	pip search --index http://testpypi.python.org/pypi/ $(NAME)

test-pypi:
	pip search $(NAME)

test-all: test test-pep8


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


# Development / Release

dev-deps-ubuntu:
	apt-get install -y pandoc

dev-install:
	virtualenv $(VENV)
	. $(VENV)/bin/activate && python setup.py develop
# FIXME Config file should be instaled in other location than the hardcoded
# path /etc.
	cp $(CONF) /etc

generate-rst:
	python setup.py generate_rst

generate-dist:
	python setup.py sdist
	python setup.py bdist_wheel

# To use this command, you should have pypitest configured in your ~/.pypirc.
testpypi-publish: generate-rst generate-dist
	twine upload dist/* -r pypitest

pypi-publish: generate-rst generate-dist
	twine upload dist/*

clean-rst:
	rm -f README.rst

clean-build:
	rm -Rf build/
	rm -Rf dist/
	rm -Rf *.egg-info

clean-pyc:
	find . -name "*.pyc" -type f -delete

clean: clean-rst clean-build clean-pyc
