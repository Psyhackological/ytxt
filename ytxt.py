"""
ytxt module
(YouTube text)

This module downloads subtitles in .vtt file format
then it opens it as a regular .txt file
removes not needed stuff and in the end
it saves to a clean looking .txt file with the same name.
"""
import argparse
import re
import glob
from pathlib import Path
import sys

import yt_dlp

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

# ydl_opts: https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L180
def show_subs_langs():
    """Shows all of the available subtitles to choose."""
    ydl_opts = {
        "listsubtitles": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            for url in args.urls:
                ydl.extract_info(url, download=False)
        except yt_dlp.utils.DownloadError:
            sys.exit()


def download_vtt_file():
    """Downlads the .vtt file with chosen subtitles languages."""
    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "subtitleslangs": args.languages,
        "subtitlesformat": args.format,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download(args.urls)

        except yt_dlp.utils.DownloadError:
            sys.exit()


class SubtitleTxt:
    """SubtitleTxt class that reads .vtt file and saves it to clean .txt file."""

    def __init__(self, vtt_file_name: str):
        with open(f"{vtt_file_name}", "rt", encoding="utf-8") as vtt_file_handle:
            self.filename = Path(vtt_file_name).stem
            self.file_text = vtt_file_handle.read()

    def delete_not_needed_stuff(self):
        """Deletes heading stuff and saves it to a self.file_text"""
        regex = r"\d{2}:\d{2}:\d{2}\.\d{3} --> .+"
        match = re.search(regex, self.file_text)
        if match is not None:
            self.file_text = self.file_text[match.start() :]

    def delete_newlines(self):
        """Deletes any kind of newlines and saves it to a self.file_text."""
        regex = r"(\n|&nbsp;|\u200B)+"
        self.file_text = re.sub(regex, " ", self.file_text)

    def delete_timestamps(self):
        """Deletes any of the timestamps and saves it to a self.file_text."""
        # regex = r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*"
        regex = r"\d{2}:\d{2}:\d{2}(,|\.){1}\d{3} .+ \d{2}:\d{2}:\d{2}(,|\.){1}\d{3}"
        self.file_text = re.sub(regex, "", self.file_text)

    def delete_start_and_end_spaces(self):
        """Deletes any of the start or end spaces and saves it to a self.file_text"""
        regex = r"(^\s|\s$)"
        self.file_text = re.sub(regex, "", self.file_text)

    def make_file(self):
        """Creates the .txt file with the same basename as .vtt file."""
        with open(f"{self.filename}.txt", "wt", encoding="utf-8") as clean_txt:
            clean_txt.write(self.file_text)

    def clean_to_txt(self):
        """Class method wrapper to make cleaning procces explicit and easier to use."""
        print("Deleting subtitles heading...")
        self.delete_not_needed_stuff()
        print("Done. 1/4")

        print("Deleting subtitles timestamps...")
        self.delete_timestamps()
        print("Done. 2/4")

        print("Deleting subtitles newlines...")
        self.delete_newlines()
        print("Done. 3/4")

        print("Deleting start and end spaces...")
        self.delete_start_and_end_spaces()
        print("Done. 4/4")

        print("Creating the txt file...")
        self.make_file()
        print(f"Finished saving {self.filename}.txt")


def main():
    """Main function to make explicit script execution flow."""
    if args.print_langs is False:
        download_vtt_file()
        vtt_files_list = glob.glob("*.vtt")
        for vtt_file in vtt_files_list:
            sub_txt = SubtitleTxt(vtt_file)
            sub_txt.clean_to_txt()
    else:
        show_subs_langs()


if __name__ == "__main__":
    main()
