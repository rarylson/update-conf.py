update-conf.py
==============

[![Pypi - Downloads](https://img.shields.io/pypi/dm/update-conf.py.svg)](https://pypi.python.org/pypi/update-conf.py/)
[![Pypi - Version](https://img.shields.io/pypi/v/update-conf.py.svg)](https://pypi.python.org/pypi/update-conf.py/)
[![Licence](https://img.shields.io/pypi/l/update-conf.py.svg)](LICENCE)
[![Pypi - Status](https://pypip.in/status/update-conf.py/badge.svg)](https://pypi.python.org/pypi/update-conf.py/)
[![Pypi - Wheel](https://pypip.in/wheel/update-conf.py/badge.svg)](https://pypi.python.org/pypi/update-conf.py/)

Generate config files from `conf.d` like directories.

Split your config file into smaller files in a `conf.d` like directory. The generated config file will be the concatenation of all splitted config files (also called snippets). The spplited files will be merged in the lexical order of their names.

Files ending with `.bak`, `.old` and other similar terminations will be ignored.

This project was based in the [update-conf.d project](https://github.com/Atha/update-conf.d).

Install
-------

This project requires Python 2.6 or newer.

**PS:** It's possible to use Python 3 also. However, it is not well tested.

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

If you run:

```sh
update-conf.py -f /etc/snmp/snmpd.conf
```

The script will merge the splitted config files in the directory `/etc/snmp/snmpd.conf.d` into the file `/etc/snmp/snmpd.conf`.

If the directory containing the splitted files uses a diferent name pattern, you can pass its name as an argument:

```sh
update-conf.py -f /etc/snmp/snmpd.conf -d /etc/snmp/snmpd.d
```

It's also possible to define frequent used options in a config file. For example, in `/etc/update-conf.py.conf`:

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

`update-conf.py` can use config files. It will use a global config file (`/etc/update-conf.py.conf`) or a user-home config file (`~/.update-conf.py.conf`) if they exist.

When installing via `setuptools` or via the source distribution, the global system config (`/etc/update-conf.py.conf`) will be automatically created.

However, when installing via the binary wheel distribution, the config file installation will be skipped. But you can use the sample config file as a start:

```sh
cp {prefix}/share/update-conf.py /etc/update-conf.py.conf
```

It's also possible to use a custom config file:

```sh
update-conf.py -c my_custom_config.conf -n snmpd
```

License
-------

This software is released under the [Revised BSD License](LICENSE).

Changelog
---------

You can see the changelog [here](CHANGELOG.md).

TODO
----

- Publish this software in a Ubuntu PPA;
    - Ubuntu 12.04 and Ubuntu 14.04;
- Use Travis as a continuous integration server;
- Hide "bugtracker_url" warning when running setup.py with setuptools;
- Use code coverage (`coverage`);
    - Flags: https://github.com/z4r/python-coveralls
- Create tests for 100% code coverage;
- Code covarage after tests:
    - `cd htmlcov && python -m SimpleHTTPServer 8888 && open http://localhost:8888`;
- https://pypi.python.org/pypi/bumpversion/ in `Makefile`;
- check-manifest in `Makefile` / `setup.py`;
- should `README.rst` be in `MANIFEST.in`?;
- https://github.com/blog/1184-contributing-guidelines
