import sys
from os.path import join
from StringIO import StringIO

import unittest

import utils

# App module
app = utils.import_app()


class ParseTest(unittest.TestCase):
    """Tests of command line parsing and config parsing
    """

    def setUp(self):
        self.file_path = join(utils.TMP_DIR, "test1")
        self.snippets_path = join(utils.SNIPPETS_DIR, "test1")
        self.config_path = utils.CONF_FILE
        self.section_name = "test1"
        self.config_file_path = "tests/tmp/test1"
        self.config_dir_path = "tests/tmp/test1.d"

    def test_short_cmd_args(self):
        """App must sucessfully parse cmd args (short options)
        """
        # Mock 'argv' with the new cmd args
        sys.argv = [
            sys.argv[0], "-f", self.file_path, "-d", self.snippets_path,
            "-p", "$"]
        args = app._parse_all()
        self.assertEqual(args.file, self.file_path)
        self.assertEqual(args.dir, self.snippets_path)
        self.assertEqual(args.comment_prefix, "$")

    def test_long_cmd_args(self):
        """App must sucessfully parse cmd args (full options)
        """
        sys.argv = [
            sys.argv[0], "--file", self.file_path, "--dir", self.snippets_path,
            "--comment-prefix", "$"]
        args = app._parse_all()
        self.assertEqual(args.file, self.file_path)
        self.assertEqual(args.dir, self.snippets_path)
        self.assertEqual(args.comment_prefix, "$")

    def test_wrong_cmd_args(self):
        """App must print an error and exit on wrong cmd args
        """
        sys.argv = [
            sys.argv[0], "--dir", self.snippets_path,
            "--comment-prefix", "$"]
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                app._parse_all()
            output = sys.stderr.getvalue()
            self.assertTrue("file" in output and "required" in output)
        finally:
            sys.stderr = stderr_old

    def test_config_parse(self):
        """App must parse options from a config file
        """
        sys.argv = [sys.argv[0], "-c", self.config_path, "-n", "test1"]
        args = app._parse_all()
        self.assertEqual(args.file, self.config_file_path)
        self.assertEqual(args.dir, self.config_dir_path)
        self.assertEqual(args.comment_prefix, "#")
        self.assertEqual(args.config, self.config_path)
        self.assertEqual(args.name, self.section_name)

    def test_nonexistent_config_parse(self):
        """App must print an error and exit when no config file was found
        """
        sys.argv = [sys.argv[0], "-c", "/non-existent", "-n", "test1"]
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                app._parse_all()
            output = sys.stderr.getvalue()
            self.assertTrue("config" in output and "not found" in output)
        finally:
            sys.stderr = stderr_old


if __name__ == '__main__':
    unittest.main()
