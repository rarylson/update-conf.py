"""Module that contains shared functions to the test classes
"""

import os
from os.path import join, abspath, dirname, isdir
import shutil

# Consts to be used by the test classes
APP = "update-conf.py"
TESTS_DIR = abspath(dirname(__file__))
SNIPPETS_DIR = join(TESTS_DIR, "snippets")
TMP_DIR = join(TESTS_DIR, "tmp")
CONF_FILE = join(TESTS_DIR, "config", "update-conf.py.conf")
USER_CONF_FILE = join(TESTS_DIR, "config", "user-update-conf.py.conf")
RESULTS_DIR = join(TESTS_DIR, "expected_results")
ROOT_DIR = join(TESTS_DIR, os.pardir)


def clean_tmp():
    """Clean the TMP_DIR directory
    """
    if isdir(TMP_DIR):
        shutil.rmtree(TMP_DIR)
    os.mkdir(TMP_DIR)
