#!/usr/bin/env python

"""Generate config files from 'conf.d' like directories

Split your config file into smaller files in a 'conf.d' like directory.

NOTE: This software was based in the 'update-conf.d' project.
      See: https://github.com/Atha/update-conf.d
"""

from __future__ import print_function

import sys
import os
import shutil
import subprocess
from tempfile import mkstemp

import argparse
from ConfigParser import SafeConfigParser

# About
__author__ = "Rarylson Freitas"
__email__ = "rarylson@gmail.com"
__version__ = "0.1.0"

# Consts
DEFAULT_CONFIG = "/etc/update-conf.py.conf"
DEFAULT_DIR_EXT = "d"
IGNORE_FILES_EXT = ["bak", "backup", "old", "inactive"]
BACKUP_EXT = "bak"


# Parse args and config file

# Parse args
parser = argparse.ArgumentParser(
    description="Generate config files from 'conf.d' like directories")
parser.add_argument(
    "-f", "--file", help="config file to be generated")
parser.add_argument(
    "-d", "--dir",
    help="directory whith the splitted files (default FILE_PATH/FILE_NAME.{0})".format(
        DEFAULT_DIR_EXT))
parser.add_argument(
    "-n", "--name",
    help="name of the section (defined in the config file) to be used while generating a "
    "config file")
parser.add_argument(
    "-c", "--config",
    help="update-conf.py config file (default {0})", default=DEFAULT_CONFIG)
parser.add_argument(
    "-v", "--version", action="version", version=__version__)
args = parser.parse_args()

# Parse config file
if args.name:
    config_parser = SafeConfigParser()
    # Open config file
    try:
        config_parser.readfp(open(args.config, 'r'))
    except IOError:
        parser.error("config file '{}' not found".format(args.config))
    # Section not found error
    if not config_parser.has_section(args.name):
        parser.error("section name '{}' not found in config file".format(args.name))
    # Get options from config file (options from command line take precedence)
    if not args.file and config_parser.has_option(args.name, 'file'):
        args.file = config_parser.get(args.name, 'file')
    if not args.dir and config_parser.has_option(args.name, 'dir'):
        args.dir = config_parser.get(args.name, 'dir')

# Required 'file' error
if not args.file:
    parser.error("'file' is required (you must set it via config file or cmd arg)")

# Default value of 'dir'
if not args.dir:
    args.dir = "{0}.{1}".format(args.file, DEFAULT_DIR_EXT)


# Get all splitted files
splitted_files = []
try:
    for entry in os.listdir(args.dir):
        entry_path = os.path.join(args.dir, entry)
        entry_is_valid = True
        if not os.path.isfile(entry_path):
            continue
        for ext in IGNORE_FILES_EXT:
            if entry.endswith(ext):
                entry_is_valid = False
                break
        if entry_is_valid:
            splitted_files.append(entry_path)
except OSError:
    print("Error: Dir '{0}' not found".format(args.dir))
    sys.exit(1)
# No splitted file error
if not splitted_files:
    print("Error: No splitted files found in dir '{0}'".format(args.dir))
    sys.exit(1)


# Generate new config file

# Generate in a temp file
temp_file_fd, temp_file = mkstemp()
# Convert 'temp_file_fd' to a Python file object
# See: http://www.logilab.org/blogentry/17873
temp_file_fd = os.fdopen(temp_file_fd, 'w')
for splitted in splitted_files:
    with open(splitted, 'r') as splitted_fd:
        temp_file_fd.write(splitted_fd.read())
temp_file_fd.close()

# Backup the old config file
if os.path.isfile(args.file):
    os.rename(args.file, "{0}.{1}".format(args.file, BACKUP_EXT))

# Use the new config file
# Using shutil.move because the tmp file can be in a different filesystem
shutil.move(temp_file, args.file)

