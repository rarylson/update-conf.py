from __future__ import absolute_import

import os
from os.path import join, isfile
import shutil
import tempfile
import filecmp

# Import unittest2 for Python 2.6 compatibility
import unittest2 as unittest

from update_conf_py import main
from . import utils


class TempToFileTest(unittest.TestCase):
    """Tests of moving a config temp file to its final location
    """

    def setUp(self):
        utils.clean_tmp()

    def test_temp_to_file(self):
        """Moves a temp file created to its final place
        """
        config_file = join(utils.TMP_DIR, "test1")
        temp_file = join(tempfile.gettempdir(), "test1")
        expected_file = join(utils.RESULTS_DIR, "test1")
        # Simulating a temp file (in the system tmp dir)
        shutil.copy(expected_file, temp_file)
        try:
            main._temp_to_file(temp_file, config_file)
            self.assertTrue(
                filecmp.cmp(config_file, expected_file, shallow=False))
        finally:
            if isfile(temp_file):
                os.remove(temp_file)

    def test_move_with_backup(self):
        """App must make a backup of the current config when generating a
        new one
        """
        config_file = join(utils.TMP_DIR, "test1")
        temp_file = join(tempfile.gettempdir(), "test1")
        expected_file = join(utils.RESULTS_DIR, "test1")
        expected_file_bak = join(utils.RESULTS_DIR, "test2")
        shutil.copy(expected_file, temp_file)
        # Creating a previous config file
        shutil.copy(expected_file_bak, config_file)
        try:
            main._temp_to_file(temp_file, config_file)
            self.assertTrue(
                filecmp.cmp(config_file, expected_file, shallow=False))
            self.assertTrue(
                filecmp.cmp(
                    "{0}.bak".format(config_file), expected_file_bak,
                    shallow=False))
        finally:
            if isfile(temp_file):
                os.remove(temp_file)


if __name__ == "__main__":
    unittest.main()
