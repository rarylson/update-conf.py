import sys
from os.path import join
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

    def test_short_cmd_args(self):
        """Test parsing of cmd args (short options)
        """
        # Mock 'argv' with the new cmd args
        sys.argv = [
            sys.argv[0], "-f", self.file_path, "-d", self.snippets_path,
            "-p", "$"]
        args = app._parse_all()
        self.assertEqual(args.file, self.file_path)
        self.assertEqual(args.dir, self.snippets_path)
        self.assertEqual(args.comment_prefix, "$")


if __name__ == '__main__':
    unittest.main()
