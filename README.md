update-conf.py
==============

[![Travis CI - Build Status](https://img.shields.io/travis/rarylson/update-conf.py/master.svg)](https://travis-ci.org/rarylson/update-conf.py)
[![Coveralls - Coverage Percentage](https://img.shields.io/coveralls/rarylson/update-conf.py/master.svg)](https://coveralls.io/r/rarylson/update-conf.py)
[![Pypi - Downloads](https://img.shields.io/pypi/dm/update-conf.py.svg)](https://pypi.python.org/pypi/update-conf.py/)
[![Pypi - Version](https://img.shields.io/pypi/v/update-conf.py.svg)](https://pypi.python.org/pypi/update-conf.py/)
[![License](https://img.shields.io/pypi/l/update-conf.py.svg)](LICENSE)

Generate config files from `conf.d` like directories.

Split your config file into smaller files, called snippets, in a `conf.d` like directory. The generated config file will be the concatenation of all snippets, with snippets ordered by the lexical order of their names.

Files ending with `.bak`, `.old` and other similar terminations will be ignored.

This project was based on the [update-conf.d project](https://github.com/Atha/update-conf.d).

Install
-------

This project works in Python 2 (2.6 or newer) and Python 3 (3.3 or newer).

To install:

```sh
pip install update-conf.py
```

It's possible to clone the project in Github and install it via `setuptools`:

```sh
git clone git@github.com:rarylson/update-conf.py.git
cd update-conf.py
python setup.py install
```

Usage
-----

To generate a config file, you can run something like this:

```sh
update-conf.py -f /etc/snmp/snmpd.conf
```

The example above will merge the snippets in the directory `/etc/snmp/snmpd.conf.d` into the file `/etc/snmp/snmpd.conf`.

If the directory containing the snippets uses a diferent name pattern, you can pass its name as an argument:

```sh
update-conf.py -f /etc/snmp/snmpd.conf -d /etc/snmp/snmpd.d
```

It's also possible to define frequently used options in a config file. For example, in `/etc/update-conf.py.conf`:

```ini
[snmpd]
file = /etc/snmp/snmpd.conf
dir = /etc/snmp/snmpd.d
```

Now, you can run:

```sh
update-conf.py -n snmpd
```

To get help:

```sh
update-conf.py --help
```

### Config files

`update-conf.py` will use the global config file (`/etc/update-conf.py.conf`) or the user-home config file (`~/.update-conf.py.conf`) if they exist.

When installing via the source distribution, the global config file (`/etc/update-conf.py.conf`) will be automatically created.

However, when installing via the binary wheel distribution, the config file installation will be skipped. But you can use the sample config file as a start point:

```sh
cp {prefix}/share/update-conf.py/update-conf.py.conf /etc/update-conf.py.conf
```

It's also possible to pass a custom config file via command line args:

```sh
update-conf.py -c my_custom_config.conf -n snmpd
```

License
-------

This software is released under the [Revised BSD License](LICENSE).

Changelog
---------

Check the [CHANGELOG](CHANGELOG.md) page.

Contributing
------------

If you want to contribute with this project, check the [CONTRIBUTING](CONTRIBUTING.md) page.

TODO
----

- Publish this software in a Ubuntu PPA;
    - Remove dependencies from argparse e configparser before pubishing in the PPA;
    - Ubuntu 12.04 and Ubuntu 14.04.
