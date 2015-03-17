from __future__ import absolute_import

import sys
import os
from os.path import join
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


class ParseAllTest(unittest.TestCase):
    """Tests of command line parsing and config parsing
    """

    def setUp(self):
        self.file_path = join(utils.TMP_DIR, "test1")
        self.snippets_path = join(utils.SNIPPETS_DIR, "test1")
        self.config_path = utils.CONF_FILE
        self.section_name = "test1"
        self.config_file_path = "tests/tmp/test1"
        self.config_dir_path = "tests/tmp/test1.d"
        self.section_name_2 = "test2"
        self.config_file_path_2 = "tests/tmp/test2"
        self.config_dir_path_2 = "tests/snippets/test2"
        self.config_comment_prefix_2 = ";"
        # These tests must be done from the root dir
        self.chdir_old = os.getcwd()
        os.chdir(utils.ROOT_DIR)

    def tearDown(self):
        os.chdir(self.chdir_old)

    def test_short_cmd_args(self):
        """App must sucessfully parse cmd args (short options)
        """
        # Mock 'argv' with the new cmd args
        sys.argv = [
            sys.argv[0], "-f", self.file_path, "-d", self.snippets_path,
            "-p", "$"]
        args = main._parse_all()
        self.assertEqual(args.file, self.file_path)
        self.assertEqual(args.dir, self.snippets_path)
        self.assertEqual(args.comment_prefix, "$")

    def test_long_cmd_args(self):
        """App must sucessfully parse cmd args (full options)
        """
        sys.argv = [
            sys.argv[0], "--file", self.file_path, "--dir", self.snippets_path,
            "--comment-prefix", "$"]
        args = main._parse_all()
        self.assertEqual(args.file, self.file_path)
        self.assertEqual(args.dir, self.snippets_path)
        self.assertEqual(args.comment_prefix, "$")

    def test_default_parse(self):
        """App must set the correct default options

        It must set the default dir if no one is provided too.
        """
        sys.argv = [
            sys.argv[0], "--file", self.file_path]
        args = main._parse_all()
        self.assertEqual(args.file, self.file_path)
        self.assertEqual(args.dir, "{0}.d".format(self.file_path))
        self.assertEqual(args.comment_prefix, "#")
        self.assertEqual(args.config, [main.SYSTEM_CONFIG, main.USER_CONFIG])

    def test_wrong_cmd_args(self):
        """App must print an error and exit on wrong cmd args
        """
        sys.argv = [
            sys.argv[0], "--dir", self.snippets_path,
            "--comment-prefix", "$"]
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                main._parse_all()
            output = sys.stderr.getvalue()
            self.assertTrue("file" in output and "required" in output)
        finally:
            sys.stderr = stderr_old

    def test_config_parse(self):
        """App must parse options from a config file (and use defaut values
        from the other options)
        """
        sys.argv = [
            sys.argv[0], "-c", self.config_path, "-n", self.section_name]
        args = main._parse_all()
        self.assertEqual(args.file, self.config_file_path)
        self.assertEqual(args.dir, self.config_dir_path)
        self.assertEqual(args.comment_prefix, "#")
        self.assertEqual(args.config, self.config_path)
        self.assertEqual(args.name, self.section_name)

    def test_config_parse_full(self):
        """App must parse all options from a config file
        """
        sys.argv = [
            sys.argv[0], "-c", self.config_path, "-n", self.section_name_2]
        args = main._parse_all()
        self.assertEqual(args.file, self.config_file_path_2)
        self.assertEqual(args.dir, self.config_dir_path_2)
        self.assertEqual(args.comment_prefix, self.config_comment_prefix_2)
        self.assertEqual(args.config, self.config_path)
        self.assertEqual(args.name, self.section_name_2)

    def test_nonexistent_config_parse(self):
        """App must print an error and exit when no config file was found
        """
        sys.argv = [sys.argv[0], "-c", "/non-existent", "-n", "test1"]
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                main._parse_all()
            output = sys.stderr.getvalue()
            self.assertTrue("config" in output and "not found" in output)
        finally:
            sys.stderr = stderr_old

    def test_wrong_config_parse(self):
        """App must print an error and exit on wrong config args
        """
        sys.argv = [sys.argv[0], "-c", self.config_path, "-n", "non_existent"]
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                main._parse_all()
            output = sys.stderr.getvalue()
            self.assertTrue("section" in output and "not found" in output)
        finally:
            sys.stderr = stderr_old

    def test_config_and_args_parse(self):
        """App must parse options from config/cmd args

        It must consider that cmd args takes precedence too.
        """
        sys.argv = [
            sys.argv[0], "-c", self.config_path, "-n", "test1",
            "-d", self.snippets_path]
        args = main._parse_all()
        self.assertEqual(args.file, self.config_file_path)
        self.assertEqual(args.dir, self.snippets_path)
        self.assertEqual(args.comment_prefix, "#")
        self.assertEqual(args.config, self.config_path)
        self.assertEqual(args.name, self.section_name)


if __name__ == "__main__":
    unittest.main()
