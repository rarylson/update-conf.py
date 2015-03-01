# update-conf.py Makefile

# Tests

test-pep8:
	pep8 update-conf.py

test:
	echo "Not implemented yet!"

test-all: test-code test-pep8


# Install

uninstall:
	rm /usr/local/bin/update-conf.py
	rm -Rf /usr/share/update-conf.py

requirements:
	pip install -r requirements.txt

install: 
	cp update-conf.py /usr/local/bin
	mkdir -p /usr/share/update-conf.py
	cp update-conf.py.conf.sample /usr/share/update-conf.py
	if [ ! -f /etc/update-conf.py.conf ]; then cp update-conf.py.conf.sample /etc/update-conf.py.conf; fi

install-all: requirements install


# Development

install-dev:
	virtualenv venv
	. venv/bin/activate && pip install -r requirements.txt
	cp update-conf.py.conf.sample update-conf.py.conf
