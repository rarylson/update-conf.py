from __future__ import absolute_import

import sys
import os
from os.path import join
import subprocess
import filecmp

# Import unittest2 for Python 2.6 compatibility
import unittest2 as unittest

from update_conf_py import main
from . import utils


class ScriptTest(unittest.TestCase):
    """Tests that use the final script
    """

    def setUp(self):
        utils.clean_tmp()
        # These tests must be done from the root dir
        self.chdir_old = os.getcwd()
        os.chdir(utils.ROOT_DIR)

    def tearDown(self):
        os.chdir(self.chdir_old)

    def test_script_cmd(self):
        """Script must merge files using cmd args
        """
        file_path = join(utils.TMP_DIR, "test1")
        expected_path = join(utils.RESULTS_DIR, "test1")
        dir_path = join(utils.SNIPPETS_DIR, "test1_2")
        args = [utils.APP]
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
        section_name = "test2"
        expected_path = join(utils.RESULTS_DIR, "test2")
        args = [utils.APP]
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
        args = [utils.APP]
        args += ["-f", file_path, "-d", dir_path]
        with self.assertRaises(subprocess.CalledProcessError):
            subprocess.check_call(args, stderr=subprocess.STDOUT)

    def test_script_verbose(self):
        """Script must print verbose messages when verbose is set
        """
        file_path = join(utils.TMP_DIR, "test1")
        dir_path = join(utils.SNIPPETS_DIR, "test1_2")
        args = [utils.APP]
        args += ["-f", file_path, "-d", dir_path]
        subprocess.call(args)
        # Set verbose flag
        args += ["-v"]
        # Using subprocess.Popen instead of subprocess.check_output for Python
        # 2.6 compatibility.
        # See: http://stackoverflow.com/a/4814985/2530295
        output = subprocess.Popen(
            args, stdout=subprocess.PIPE).communicate()[0]
        # In Python 3, it's necessary a conversion to str.
        output = str(output)
        self.assertTrue(
            "Skiping" in output and "Merging" in output and
            "Backing up" in output)

    def test_run(self):
        """Test a call to the run function

        Unfortunately, the previous tests from this module are not detected
        by 'coverage'. We are testing this function directaly (the test is
        equal to the 'test_script_cmd'). So, 'coverage' will consider that the
        'run' function is tested.
        """
        file_path = join(utils.TMP_DIR, "test1")
        expected_path = join(utils.RESULTS_DIR, "test1")
        dir_path = join(utils.SNIPPETS_DIR, "test1_2")
        args = [utils.APP]
        args += ["-f", file_path, "-d", dir_path]
        # Mock sys.argv
        self.argv_old = sys.argv
        sys.argv = args
        main.run()
        # The second call forces a backup
        main.run()
        self.assertTrue(
            filecmp.cmp(file_path, expected_path, shallow=False))
        self.assertTrue(filecmp.cmp(
            "{0}.bak".format(file_path), expected_path, shallow=False))
        sys.argv = self.argv_old


if __name__ == "__main__":
    unittest.main()
