"""
argument_parsing module

In this module all of the magic happens when
you pass the arguments to main script.
"""

# Documentation: https://docs.python.org/3/library/argparse.html
# Tutorial:      https://docs.python.org/3/howto/argparse.html#
import argparse
import sys


parser = argparse.ArgumentParser(prog="YTXT - YouTube Video to TXT")


def parse_args():
    """
    parse_args()

    This function is used to parse command-line arguments passed to the script.

    Args:
    -l, --languages (list, optional): list of subtitles languages. default is ["en", "en-GB"].
    -sl, --sub-langs (bool, optional): prints all available subtitles languages
    urls (list, required): YouTube video URLs

    Returns:
    argparse.Namespace: An object containing the arguments as attributes

    Example usage:
    args = parse_args()
    print(args.languages)
    """
    parser.add_argument(
        "-l",
        "--languages",
        nargs="*",
        type=str,
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

    parser.add_argument(
        nargs="+", type=str, help="YouTube video URLs", metavar="URL", dest="urls"
    )

    return parser.parse_args()


if len(sys.argv) <= 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
