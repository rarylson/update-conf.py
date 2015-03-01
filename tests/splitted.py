import sys
from os.path import join, basename
from StringIO import StringIO

import unittest

import utils

# App module
app = utils.import_app()


class SplittedFilesTest(unittest.TestCase):
    """Tests to verify if the '_get_splitted' function works
    """

    def setUp(self):
        utils.clean_tmp()

    def test_splitted(self):
        """App must return all splitted files in the correct order
        """
        the_dir = join(utils.SNIPPETS_DIR, "test1")
        files = app._get_splitted(the_dir)
        self.assertEqual(
            map(basename, files),
            ["00-conf_0", "01-conf_1", "02-conf_2", "99-conf_99",
                "other_name-conf", "some_name-conf"])

    def test_splitted_skip(self):
        """App must skip all invalid splitted files
        """
        the_dir = join(utils.SNIPPETS_DIR, "test1_2")
        files = app._get_splitted(the_dir)
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
                app._get_splitted("/non-existent")
            output = sys.stderr.getvalue()
            self.assertTrue("Dir" in output and "not found" in output)
        finally:
            sys.stderr = stderr_old
        # Empty dir
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                app._get_splitted(utils.TMP_DIR)
            output = sys.stderr.getvalue()
            self.assertTrue("No splitted" in output and "found" in output)
        finally:
            sys.stderr = stderr_old

    def test_splitted_verbose(self):
        """App must print verbose messages about skips when verbosity is
        active
        """
        app.VERBOSE = True
        the_dir = join(utils.SNIPPETS_DIR, "test1_2")
        stdout_old, sys.stdout = sys.stdout, StringIO()
        try:
            app._get_splitted(the_dir)
            output = sys.stdout.getvalue()
            self.assertTrue("Skiping" in output and "01-conf_1.bak" in output)
            self.assertTrue(
                "Skiping" in output and "03-conf_3.disabled" in output)
        finally:
            sys.stdout = stdout_old


if __name__ == '__main__':
    unittest.main()
