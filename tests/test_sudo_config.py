from __future__ import absolute_import

import sys
import os
from os.path import join, isfile
import shutil
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


@unittest.skipIf(
    os.geteuid() != 0, "supported only if the user is a superuser")
class SudoConfigTest(unittest.TestCase):
    """Tests for the config read feature, but that requires superuser
    privileges

    This tests SHOULD be run only in DEVELOPMENT envs. There are risks of
    destroying your original config files. Keep CAUTION!
    """

    def setUp(self):
        self.section_name = "test1"
        self.expected_file_global = "tests/tmp/test1"
        self.expected_file_user = "/nonexistent/home"
        self.backup_global = join(utils.TMP_DIR, "config_global.bak")
        self.backup_user = join(utils.TMP_DIR, "config_user.bak")
        utils.clean_tmp()
        # Mock 'argv' with the new cmd args
        self.argv_old = sys.argv
        sys.argv = [sys.argv[0], "-n", self.section_name]
        # Move/backup original config files
        if isfile(main.SYSTEM_CONFIG):
            shutil.move(main.SYSTEM_CONFIG, self.backup_global)
        if isfile(main.USER_CONFIG):
            shutil.move(main.USER_CONFIG, self.backup_user)

    def tearDown(self):
        sys.argv = self.argv_old
        # Clean config files. If they exist, they are test files.
        if isfile(main.SYSTEM_CONFIG):
            os.remove(main.SYSTEM_CONFIG)
        if isfile(main.USER_CONFIG):
            os.remove(main.USER_CONFIG)
        # Restore original config files
        if isfile(self.backup_global):
            shutil.move(self.backup_global, main.SYSTEM_CONFIG)
        if isfile(self.backup_user):
            shutil.move(self.backup_user, main.USER_CONFIG)

    def test_system_config(self):
        """App must read config file from system etc if it exits
        """
        shutil.copy(utils.CONF_FILE, main.SYSTEM_CONFIG)
        args = main._parse_all()
        self.assertEqual(args.file, self.expected_file_global)

    def test_user_config(self):
        """App must read config file from user home if it exits
        """
        shutil.copy(utils.USER_CONF_FILE, main.USER_CONFIG)
        args = main._parse_all()
        self.assertEqual(args.file, self.expected_file_user)

    def test_system_user_config(self):
        """Options from user config file MUST take precedence over the
        system one
        """
        shutil.copy(utils.CONF_FILE, main.SYSTEM_CONFIG)
        shutil.copy(utils.USER_CONF_FILE, main.USER_CONFIG)
        args = main._parse_all()
        self.assertEqual(args.file, self.expected_file_user)

    def test_default_config_not_found(self):
        """App must print a error if none of the default config files were
        found
        """
        stderr_old, sys.stderr = sys.stderr, StringIO()
        try:
            with self.assertRaises(SystemExit):
                main._parse_all()
            output = sys.stderr.getvalue()
            self.assertTrue(
                "neither" in output and "nor" in output and
                main.SYSTEM_CONFIG in output and main.USER_CONFIG in output)
        finally:
            sys.stderr = stderr_old


if __name__ == "__main__":
    unittest.main()
