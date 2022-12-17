import yt_dlp
import argparse
import re
import glob
from pathlib import Path

# Documentation: https://docs.python.org/3/library/argparse.html
# Tutorial:      https://docs.python.org/3/howto/argparse.html#
parser = argparse.ArgumentParser(prog="YouTube Video to TXT")
parser.add_argument(nargs='*', type=str, help="YouTube Video URL (str)", dest="urls")
parser.add_argument('-l', "--language", type=list, help="subtitles languages (default=['en']) (list)", dest="languages", default=["en", "en-GB"])
parser.add_argument('-f', "--format", nargs='?', type=str, help="subtitles format (default='vtt') (str)", dest="format", default="vtt")
parser.add_argument('-sl', "--sub-langs", action="store_true", help="prints all available subtitles languages", dest="print_langs")
args = parser.parse_args()

args.urls = [r"https://youtu.be/F1Hq8eVOMHs"]

# ydl_opts: https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L180
def show_subs_langs():
    ydl_opts = {  # YT-DLP OPTIONS
        'listsubtitles': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            for url in args.urls:
                ydl.extract_info(url, download=False)
        except yt_dlp.utils.DownloadError:
            quit()


def download_vtt_file():
    ydl_opts = {  # YT-DLP OPTIONS
        'skip_download': True,
        'writesubtitles': True,
        'subtitleslangs': args.languages,
        'subtitlesformat': args.format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            error_code = ydl.download(args.urls)

        except yt_dlp.utils.DownloadError:
            quit()


class SubtitleTXT:
    def __init__(self, vtt_file_name):
        with open(f"{vtt_file_name}", 'rt') as vtt_file:
            self.filename = Path(vtt_file_name).stem
            self.file_text = vtt_file.read()

    def delete_not_needed_stuff(self):
        # regex = r"^00:00:\d{2}\.\d{3} --> 00:00:\d{2}\.\d{3}.*"
        regex = r"\d{2}:\d{2}:\d{2}\.\d{3} --> .+"
        match = re.search(regex, self.file_text)
        if match is not None:
            self.file_text = self.file_text[match.start():]

    def delete_newlines(self):
        regex = r"(\n|&nbsp;|​)+"
        self.file_text = re.sub(regex, ' ', self.file_text)

    def delete_timestamps(self):
        # regex = r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*"
        regex = r"\d{2}:\d{2}:\d{2}(,|\.){1}\d{3} .+ \d{2}:\d{2}:\d{2}(,|\.){1}\d{3}"
        self.file_text = re.sub(regex, '', self.file_text)

    def make_file(self):
        with open("clean.txt", "wt") as clean_txt:
            clean_txt.write(self.file_text)

    def clean_to_txt(self):
        print("Deleting subtitles heading...")
        self.delete_not_needed_stuff()
        print("Done. 1/3")

        print("Deleting subtitles timestamps...")
        self.delete_timestamps()
        print("Done. 2/3")

        print("Deleting subtitles newlines...")
        self.delete_newlines()
        print("Done. 3/3")

        print("Creating the txt file...")
        self.make_file()
        print(f"Finished saving {self.filename}.txt")


if args.print_langs is False:
    download_vtt_file()
    vtt_files = glob.glob("*.vtt")
    for vtt_file in vtt_files:
        SubTxt = SubtitleTXT(vtt_file)
        SubTxt.clean_to_txt()
else:
    show_subs_langs()
