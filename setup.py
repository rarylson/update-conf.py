"""update-conf.py setup.py file
"""

import os
from os.path import abspath, dirname, join
from setuptools import setup

from update_conf_py import main


# Consts
GITHUB_URL = "https://github.com/rarylson/update-conf.py"
README = "README.md"

# Important vars
cur_dir = abspath(dirname(__file__))
readme = join(cur_dir, README)
sample_config = join("samples", main.CONFIG_NAME)
# Get description from the first line of the module docstring.
description = main.__doc__.split('\n')[0]
long_description = ""
with open(readme, 'r') as f:
    long_description = f.read()


# Setup
setup(
    # Main software info
    name=main.__program__,
    version=main.__version__,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=main.__license__,
    author=main.__author__,
    author_email=main.__email__,
    url=GITHUB_URL,
    keywords="system unix config split merge snippets sysadmin",
    packages=["update_conf_py"],

    # Requirements
    python_requires=">=3.7",

    # Classifiers
    # See: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],

    # Entry points
    # The script itself is defined here.
    entry_points={
        "console_scripts": [
            "update-conf.py = update_conf_py:run",
        ],
    },

    # Data files
    data_files=[
        (join("share", main.__program__), [sample_config, ]),
    ],

    # Tests
    test_suite="tests",
)
