# update-conf.py Makefile

PACKAGE=update_conf_py
NAME=update-conf.py
CONF=$(NAME).conf
PREFIX=/usr/local
ETC=/etc
VENV=venv
TEST_DIR=tests
TESTS=$(wildcard $(TEST_DIR)/*.py)


all:
	echo "Did you mean 'make install'?"

# Tests

test-pep8:
	pep8 $(PACKAGE)/*.py $(TEST_DIR)/*.py setup.py

test:
	$(foreach TEST, $(TESTS), python $(TEST);)

test-testpypi:
	pip search --index http://testpypi.python.org/pypi/ $(NAME)

test-pypi:
	pip search $(NAME)

test-all: test test-pep8


# Install

# setup.py does not have a uninstall command. We're only showing a tip.
# See: http://stackoverflow.com/a/1550235/2530295
uninstall:
	echo "'setup.py' does not have a uninstall command."
	echo "You can run the follow command to get a list of installed files and "
	echo "then removing them:"
	echo
	echo "    python setup.py install --record files.txt"
	echo
	echo "It's also a good practice using 'pip' in a production env."

install: 
	python setup.py install


# Development

dev-deps-ubuntu:
	apt-get install -y pandoc

# TODO Use pyandoc in setup.py
# See: https://coderwall.com/p/qawuyq/use-markdown-readme-s-in-python-modules
readme-rst:
	pandoc --from=markdown --to=rst --output=README.rst README.md
# Post-fix: License broken link
	sed -i -e 's/`Revised BSD License <LICENSE>`__/**Revised BSD License**/' \
	    README.rst
# MacOS clean: for some reason, MacOSX is creating a '-e' file after sed.
	rm README.rst-e &>/dev/null

dev-install:
	python setup.py develop
