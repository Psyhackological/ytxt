"""
argument_parsing module

In this module all of the magic happens when
you pass the arguments to main script.
"""

import argparse
import sys

# Documentation: https://docs.python.org/3/library/argparse.html
# Tutorial:      https://docs.python.org/3/howto/argparse.html#
parser = argparse.ArgumentParser(prog="YTXT - YouTube Video to TXT")
parser.add_argument(
    "urls", nargs="*", type=str, help="YouTube video URLs", metavar="URL"
)
parser.add_argument(
    "-l",
    "--languages",
    nargs="+",
    type=list[str],
    help="subtitles languages (default=['en', 'en-GB']) (list)",
    default=["en", "en-GB"],
    metavar="LANG",
)
parser.add_argument(
    "-sl",
    "--sub-langs",
    action="store_true",
    help="prints all available subtitles languages",
    dest="print_langs",
)
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
