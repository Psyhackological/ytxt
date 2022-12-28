"""
argument_parsing module

In this module all of the magic happens when
you pass the arguments to main script.
"""

import argparse

# Documentation: https://docs.python.org/3/library/argparse.html
# Tutorial:      https://docs.python.org/3/howto/argparse.html#
parser = argparse.ArgumentParser(prog="YouTube Video to TXT")
parser.add_argument(nargs="*", type=str, help="YouTube Video URL (str)", dest="urls")
parser.add_argument(
    "-l",
    "--language",
    type=list[str],
    help="subtitles languages (default=['en']) (list)",
    dest="languages",
    default=["en", "en-GB"],
)
parser.add_argument(
    "-f",
    "--format",
    nargs="?",
    type=str,
    help="subtitles format (default='vtt') (str)",
    dest="format",
    default="vtt",
)
parser.add_argument(
    "-sl",
    "--sub-langs",
    action="store_true",
    help="prints all available subtitles languages",
    dest="print_langs",
)
args = parser.parse_args()

args.urls = [r"https://youtu.be/F1Hq8eVOMHs"]
