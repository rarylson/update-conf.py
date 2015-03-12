Changelog
=========

0.4.2
-----

- **Fix:** More bugs while installing in Linux;
    - `MANIFEST.in` created so the required files are now in the source distribution (used by Linux).

0.4.1
-----

- **Fix:** Some bugs while installing in Linux;
    - Fixed logic to install `{prefix}/share/update-conf.py` and `/etc/update-conf.py.conf`.

0.4.0
-----

- It's possible to use a user home config file (`~/.update-conf.py.conf`);
- **Fix:** Skip copy of system config file (`/etc/update-conf.py.conf`) when installing using a non-privileged user;
- Project data in `{prefix}/share/update-conf.py`;
    - For now, only the sample config file is being put there.

0.3.4
-----

- First release.
