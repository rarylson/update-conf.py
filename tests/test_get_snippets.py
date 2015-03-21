from __future__ import absolute_import

import sys
from os.path import join, basename
# Use 'io.StringIO' for Python 3 compatibility. In Python 2, still use
# 'StringIO.StringIO' to avoid unicode errors.
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

# Import unittest2 for Python 2.6 compatibility
import unittest2 as unittest

from update_conf_py import main
from . import utils


class GetSnippetsTest(unittest.TestCase):
    """Tests to verify if the '_get_snippets' function works
    """

    def setUp(self):
        utils.clean_tmp()

    def tearDown(self):
        main.VERBOSE = False

    def test_snippets(self):
        """App must return all snippets in the correct order
        """
        the_dir = join(utils.SNIPPETS_DIR, "test1")
        files = main._get_snippets(the_dir)
        files = [basename(f) for f in files]
        expected_files = [
            "00-conf_0", "01-conf_1", "02-conf_2", "99-conf_99",
            "other_name-conf", "some_name-conf"]
        self.assertEqual(files, expected_files)

    def test_snippets_skip(self):
        """App must skip all invalid snippet filenames
        """
        the_dir = join(utils.SNIPPETS_DIR, "test1_2")
        files = main._get_snippets(the_dir)
        files = [basename(f) for f in files]
        expected_files = [
            "00-conf_0", "01-conf_1", "02-conf_2", "99-conf_99",
            "other_name-conf", "some_name-conf"]
        self.assertEqual(files, expected_files)

    def test_snippets_wrong_dir(self):
        """App must print an error and exists if wrong dirs are used

        Empty dirs and non-existend dirs are the two tested cases.
        """
        # Non-existent dir
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                main._get_snippets("/non-existent")
            output = sys.stderr.getvalue()
            self.assertTrue("dir" in output and "not found" in output)
        finally:
            sys.stderr = stderr_old
        # Empty dir
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                main._get_snippets(utils.TMP_DIR)
            output = sys.stderr.getvalue()
            self.assertTrue("no snippet" in output and "found" in output)
        finally:
            sys.stderr = stderr_old

    def test_snippets_verbose(self):
        """App must print verbose messages about skips when verbosity is
        active
        """
        main.VERBOSE = True
        the_dir = join(utils.SNIPPETS_DIR, "test1_2")
        stdout_old, sys.stdout = sys.stdout, StringIO()
        try:
            main._get_snippets(the_dir)
            output = sys.stdout.getvalue()
            self.assertTrue("Skiping" in output and "01-conf_1.bak" in output)
            self.assertTrue(
                "Skiping" in output and "03-conf_3.disabled" in output)
        finally:
            sys.stdout = stdout_old


if __name__ == "__main__":
    unittest.main()
