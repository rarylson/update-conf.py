import sys
from os.path import join, basename
from StringIO import StringIO

# Import unittest2 for Python 2.6 compatibility
import unittest2 as unittest

from update_conf_py import main
import utils


class GetSplittedTest(unittest.TestCase):
    """Tests to verify if the '_get_splitted' function works
    """

    def setUp(self):
        utils.clean_tmp()

    def tearDown(self):
        main.VERBOSE = False

    def test_splitted(self):
        """App must return all splitted files in the correct order
        """
        the_dir = join(utils.SNIPPETS_DIR, "test1")
        files = main._get_splitted(the_dir)
        self.assertEqual(
            map(basename, files),
            ["00-conf_0", "01-conf_1", "02-conf_2", "99-conf_99",
                "other_name-conf", "some_name-conf"])

    def test_splitted_skip(self):
        """App must skip all invalid splitted files
        """
        the_dir = join(utils.SNIPPETS_DIR, "test1_2")
        files = main._get_splitted(the_dir)
        self.assertEqual(
            map(basename, files),
            ["00-conf_0", "01-conf_1", "02-conf_2", "99-conf_99",
                "other_name-conf", "some_name-conf"])

    def test_splitted_wrong_dir(self):
        """App must prints an error and exists if wrong dirs are used

        Empty dirs and non-existend dirs are the two tested cases.
        """
        # Non-existent dir
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                main._get_splitted("/non-existent")
            output = sys.stderr.getvalue()
            self.assertTrue("dir" in output and "not found" in output)
        finally:
            sys.stderr = stderr_old
        # Empty dir
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                main._get_splitted(utils.TMP_DIR)
            output = sys.stderr.getvalue()
            self.assertTrue("no splitted" in output and "found" in output)
        finally:
            sys.stderr = stderr_old

    def test_splitted_verbose(self):
        """App must print verbose messages about skips when verbosity is
        active
        """
        main.VERBOSE = True
        the_dir = join(utils.SNIPPETS_DIR, "test1_2")
        stdout_old, sys.stdout = sys.stdout, StringIO()
        try:
            main._get_splitted(the_dir)
            output = sys.stdout.getvalue()
            self.assertTrue("Skiping" in output and "01-conf_1.bak" in output)
            self.assertTrue(
                "Skiping" in output and "03-conf_3.disabled" in output)
        finally:
            sys.stdout = stdout_old


if __name__ == '__main__':
    unittest.main()
