Changelog
=========

1.1.0
-----

- Docs with more usage examples

1.0.3
-----

- **Fix:** Error message when config file not found 

1.0.2
-----

- **Fix:** Close config file as soon as possible 
    - Before, we were using `readfp` and keeping the config file opened forever
- Multiple improvements and more automation in the build/publish process
    - Notadably, the release process now uses a CI/CD pipeline via GitHub Actions

1.0.1
-----

- Minor fixes in the build/publish process

1.0.0
-----

- The global config file (`/etc/update-conf.py.conf`) is not auto-installed when running `python setup.py install` as root anymore;
- Support to Python 2 was removed;
    - Code simplified to support only Python 3 (3.7 or newer);
- Switching CI from Travis to GitHub Actions

0.4.5
-----

- Python3 compatibility changed to 3.3 or newer (including Python 3.5).

0.4.4
-----

- Python 3 (3.2 or newer) compatibility added;
- Improvements in the build process;
- `CONTRIBUTING.md` added and a fix in `README.md`.

0.4.3
-----

- Python 2.6 compatibility added;
- Project integrated with Travis and Coveralls;
    - It passes in all tests (Python 2.6 and 2.7) and has 100% code coverage.

0.4.2
-----

- Docs about config files added.
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
