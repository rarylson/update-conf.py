# update-conf.py Makefile

BIN=update-conf.py
PACKAGE=update_conf_py
CONF=$(BIN).conf
PREFIX=/usr/local
ETC=/etc
PYTHON_REQUIREMENTS=requirements.txt
PYTHON_SETUP=setup.py
VENV=venv
TEST_DIR=tests
TESTS=$(wildcard $(TEST_DIR)/*.py)


# Tests

test-pep8:
	pep8 $(PACKAGE)/*.py $(BIN) $(TEST_DIR)/*.py

test:
	$(foreach TEST, $(TESTS), python $(TEST);)

test-all: test test-pep8


# Install

uninstall:
	rm $(PREFIX)/bin/$(BIN)
	rm -Rf $(PREFIX)/share/$(BIN)

purge: uninstall
	rm $(ETC)/$(CONF)

requirements:
	pip install -r $(PYTHON_REQUIREMENTS)

# TODO Update to 'setup.py'
install: 
	cp $(BIN) $(PREFIX)/bin/$(BIN)
	mkdir -p $(PREFIX)/share/$(BIN)
	cp $(CONF).sample $(PREFIX)/share/$(BIN)/$(CONF).sample
	if [ ! -f $(ETC)/$(CONF) ]; then cp $(CONF).sample $(ETC)/$(CONF); fi

install-all: requirements install


# Development

deps-ubuntu-dev:
	apt-get install -y pandoc

install-dev:
	virtualenv $(VENV)
	. $(VENV)/bin/activate && pip install -r $(PYTHON_REQUIREMENTS)
	cp $(CONF).sample $(CONF)

# Util when using long description in setup.py and Pypi
readme-rst:
	pandoc --from=markdown --to=rst --output=README.rst README.md
# Post-fix: License broken link
	sed -i -e 's/`Revised BSD License <LICENSE>`__/**Revised BSD License**/' README.rst
# MacOS clean: for some reason, MacOSX is creating a '-e' file
	rm README.rst-e &>/dev/null
