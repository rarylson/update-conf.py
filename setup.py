"""update-conf.py setup.py file
"""

from setuptools import setup
from os.path import abspath, dirname, join

from update_conf_py import main

# Consts
GITHUB_URL = "https://github.com/rarylson/update-conf.py"
README = "README.rst"
LICENSE = "LICENSE"

# Important vars
cur_dir = abspath(dirname(__file__))
# Get description from the first line of the module docstring.
description = main.__doc__.split('\n')[0]
# Get the long description from the 'README.rst' file (if it exists). Else,
# use the module doc string.
# Note: You MUST generate the 'README.rst' before uploading to Pypi.
long_description = ""
try:
    with open(join(cur_dir, README), 'r') as f:
        long_description = f.read()
except IOError:
    long_description = main.__doc__
# Get license from a file because the license is not listed in any Pypi
# classifier.
# TODO Maybe we should use 'main.__license__' instead. We need to read more
# about Pypi!
license = open(join(cur_dir, LICENSE), 'r').read()

# Setup
setup(
    # Main software info
    name=main.__program__,
    version=main.__version__,
    description=description,
    long_description=long_description,
    license=license,
    author=main.__author__,
    author_email=main.__email__,
    url=GITHUB_URL,
    # Currently, setuptools do not undestand this option. Ignore the warning
    # and manually set it in the Pypi web interface.
    bugtrack_url="{0}/issues".format(GITHUB_URL),
    download_url="{0}/tarball/{1}".format(GITHUB_URL, main.__version__),
    keywords="system unix config split snippets sysadmin",
    packages=["update_conf_py"],

    # Requirements
    install_requires=[
        "argparse>=1.2",
        "configparser>=2.3",
    ],

    # Classifiers
    # See: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],

    # Entry points
    # The script itself is defined here.
    entry_points={
        "console_scripts": [
            "update-conf.py = update_conf_py.run",
        ],
    },

    # Data files
    # The script config file is defined here.
    data_files=[
        ("/etc", ['samples/update-conf.py.conf', ]),
    ],

    # Extra
    extras_require={
        "dev": [
            "setuptools>=0.8",
            "pyandoc>=0.0.1",
        ],
    }
)
