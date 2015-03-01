"""Module that contain shared functions to be used by the test classes
"""

import os
from os.path import join, dirname
import sys
import shutil
import glob

# Consts
APP = "update-conf.py"
TESTS_DIR = dirname(__file__)
APP_DIR = join(TESTS_DIR, os.pardir)

# Consts to be used by the test classes
SNIPPETS_DIR = join(TESTS_DIR, "snippets")
TMP_DIR = join(TESTS_DIR, "tmp")
CONF_FILE = join(TESTS_DIR, "config", "update-conf.py.conf")
EXPECTED_RESULTS_DIR = join(TESTS_DIR, "expected_results")


def import_app():
    """Load the app script as a module

    This function is necessary for two reasons:

    - The script is not in the python path;
    - The Python "import" statement can't load modules that contains the "-"
      and "." characters in its name.

    See: http://stackoverflow.com/questions/7583652/python-module-with-a-dash-
             or-hyphen-in-its-name
         http://stackoverflow.com/questions/678236/how-to-get-the-filename-
             without-the-extension-from-a-path-in-python
    """
    sys.path.append(APP_DIR)
    app_module = APP.split(".")[0]

    return __import__(app_module)


def clean_tmp():
    """Clean the TMP_DIR directory
    """
    for entry in glob.iglob(join(TMP_DIR, "*")):
        shutil.rmtree(entry)
