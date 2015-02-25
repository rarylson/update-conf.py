# Makefile from update-conf.py project

# Tests
pep8:
	pep8 update-conf.py

# Install
install: 
	cp update-conf.py /usr/local/bin
	cp update-conf.py.conf.sample /etc
