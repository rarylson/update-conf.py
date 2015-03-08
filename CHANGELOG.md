Changelog
=========

0.4.0
-----

- It's possible to use config file from `/etc/update-conf.py.conf` or `~/.update-conf.py.conf`;
- Bugfix: Skipping global config file when instaling from a non-privileged user;
    - If isn't possible to create the `/etc/update-conf.py.conf` file, a warning will be showed instead of stopping the install.
- Sample config file installed in `{prefix}/share/update-conf.py.conf`.

0.3.4
-----

- First release in Pypi;
- First stable version.
