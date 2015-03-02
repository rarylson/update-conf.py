import sys
import os
from os.path import join
import subprocess
import filecmp

import unittest

import utils


class ScriptTest(unittest.TestCase):
    """Tests uing the final script
    """

    def setUp(self):
        utils.clean_tmp()
        # These tests must be done from the app dir
        self.chdir_old = os.getcwd()
        os.chdir(utils.APP_DIR)

    def tearDown(self):
        os.chdir(self.chdir_old)

    def test_script_cmd(self):
        """Script must merge files using cmd args
        """
        file_path = join(utils.TMP_DIR, "test1")
        expected_path = join(utils.RESULTS_DIR, "test1")
        dir_path = join(utils.SNIPPETS_DIR, "test1_2")
        args = [utils.SCRIPT]
        args += ["-f", file_path, "-d", dir_path]
        subprocess.call(args)
        # The second call forces a backup
        subprocess.call(args)
        self.assertTrue(
            filecmp.cmp(file_path, expected_path, shallow=False))
        self.assertTrue(filecmp.cmp(
            "{0}.bak".format(file_path), expected_path, shallow=False))

    def test_script_config(self):
        """Script must merge files using args from config
        """
        file_path = join(utils.TMP_DIR, "test2")
        config_path = utils.CONF_FILE
        section_name = "test2"
        expected_path = join(utils.RESULTS_DIR, "test2")
        args = [utils.SCRIPT]
        args += ["-c", utils.CONF_FILE, "-n", section_name]
        subprocess.call(args)
        # The second call forces a backup
        subprocess.call(args)
        self.assertTrue(
            filecmp.cmp(file_path, expected_path, shallow=False))
        self.assertTrue(filecmp.cmp(
            "{0}.bak".format(file_path), expected_path, shallow=False))

    def test_script_error(self):
        """Script must prints an error and exists if something wrong ocour

        Only some tests are done, because most of them are already tested
        in the test cases of inner level functions.
        """
        file_path = join(utils.TMP_DIR, "test1")
        dir_path = "/non-existent"
        args = [utils.SCRIPT]
        args += ["-f", file_path, "-d", dir_path]
        output = ""
        with self.assertRaises(subprocess.CalledProcessError):
            subprocess.check_output(args, stderr=subprocess.STDOUT)

    def test_script_verbose(self):
        """Script must print verbose messages when verbose is set
        """
        file_path = join(utils.TMP_DIR, "test1")
        expected_path = join(utils.RESULTS_DIR, "test1")
        dir_path = join(utils.SNIPPETS_DIR, "test1_2")
        args = [utils.SCRIPT]
        args += ["-f", file_path, "-d", dir_path]
        subprocess.call(args)
        # Set verbose flag
        args += ["-v"]
        output = subprocess.check_output(args)
        self.assertTrue(
            "Skiping" in output and "Merging" in output and
            "Backing up" in output)


if __name__ == '__main__':
    unittest.main()
