update-conf.py
==============

Generate config files from `conf.d` like directories.

Split your config file into smaller files in a `conf.d` like directory. The generated config file will be the concatenation of all splitted config files (also called snippets). The spplited files will be merged in the lexical order of their names.

Files ending with `.bak`, `.old` and other similar terminations will be ignored.

This project was based in the [update-conf.d project](https://github.com/Atha/update-conf.d).

Install
-------

This project requires Python 2.6 or newer.

**PS:** It's possible to use Python 3. However, it is not well tested.

In Ubuntu/Debian:

```sh
apt-get install python
```

To install:

```sh
pip install update-conf.py
```

It's also possible to clone the project in Github and install via `setuptools`:

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

It's also possible to define frequent used options in a config file (`/etc/update-conf.py.conf`). For example:

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

License
-------

This software is released under the [Revised BSD License](LICENSE).

TODO
----

- Publish this software in a Ubuntu PPA;
    - Ubuntu 12.04 and Ubuntu 14.04.
