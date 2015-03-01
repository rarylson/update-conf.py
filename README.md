update-conf.py
==============

Generate config files from `conf.d` like directories.

Split your config file into smaller files in a `conf.d` like directory. The generated config file will be the concatenation of all splitted config files. The spplited files will be merged in the lexical sort order of their names. 

Files ending with `.bak`, `.old` and other similar terminations will be ignored.

This project was based in the [update-conf.d project](https://github.com/Atha/update-conf.d).

Install
-------

At first, we need Python 2.6 or newer. It's possible to use Python 3 too.

In Ubuntu/Debian:

```sh
apt-get install python
```

After, install the requirements:

```sh
pip install -r requirements.txt
```

At last, install the script:

```sh
make install
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

- Improve the `Makefile`. Currently, `make install` overrides the config file;
    - There could be a `make requirements` option too;
- Add tests
    - There is no `make test` function;
    - Add global command line tests;
    - Add python unit tests.
