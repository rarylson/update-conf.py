import sys
import os
from os.path import join
import filecmp
from io import StringIO

import unittest

from update_conf_py import main
from . import utils


class CreateTempConfigTest(unittest.TestCase):
    """Tests of creating a new config temp file

    This tests the autogenerated comments too.
    """

    def setUp(self):
        self.snippets_1 = []
        self.snippets_2 = []

        the_dir = join(utils.SNIPPETS_DIR, "test1")
        snippets = [
            "00-conf_0", "01-conf_1", "02-conf_2", "99-conf_99",
            "other_name-conf", "some_name-conf"]
        self.snippets_1 = [join(the_dir, s) for s in snippets]
        the_dir = join(utils.SNIPPETS_DIR, "test2")
        snippets = ["00-conf_0", "some_name-conf"]
        self.snippets_2 = [join(the_dir, s) for s in snippets]

    def tearDown(self):
        main.VERBOSE = False

    def test_tmpconfig_1(self):
        """App must merge sucessfully all snippets from test1

        It must to add the correct autogenerated message too.
        """
        temp_file = main._create_temp_config(
            self.snippets_1, comment_prefix="#")
        try:
            self.assertTrue(filecmp.cmp(
                temp_file, join(utils.RESULTS_DIR, "test1"), shallow=False))
        finally:
            os.remove(temp_file)

    def test_tmpconfig_2(self):
        """App must merge sucessfully all snippets from test2

        It must to add the correct autogenerated message too.
        """
        temp_file = main._create_temp_config(
            self.snippets_2, comment_prefix=";")
        try:
            self.assertTrue(filecmp.cmp(
                temp_file, join(utils.RESULTS_DIR, "test2"), shallow=False))
        finally:
            os.remove(temp_file)

    def test_tmpconfig_verbose(self):
        """App must print verbose messages about merged files
        """
        main.VERBOSE = True
        stdout_old, sys.stdout = sys.stdout, StringIO()
        try:
            temp_file = main._create_temp_config(
                self.snippets_2, comment_prefix=";")
            output = sys.stdout.getvalue()
            self.assertTrue("Merging" in output and "00-conf_0" in output)
            self.assertTrue("Merging" in output and "some_name-conf" in output)
        finally:
            sys.stdout = stdout_old
            os.remove(temp_file)


if __name__ == "__main__":
    unittest.main()
