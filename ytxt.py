import yt_dlp
import argparse
import re

parser = argparse.ArgumentParser(prog="YTxt")
parser.add_argument(nargs='?', type=str, help="Playlist/channel URL. (str)", dest="url")
args = parser.parse_args()


def download_vtt_file():
    ydl_opts = {  # YT-DLP OPTIONS
        'subtitlesformat': "vtt",
        'writesubtitles': True,
        'skip_download': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # SPECIAL YT-DLP OBJECT WITH YDL_OPTS (OPTIONS)
        try:
            ydl.extract_info(args.url, download=True)  # WE WANT INFO WITHOUT DOWNLOADING THE VIDEO
        except yt_dlp.utils.DownloadError:  # SILLY YOU, THAT IS NOT A VALID
            quit()


class SubtitleTXT:
    def __init__(self, name="Quantum Physics for 7 Year Olds _ Dominic Walliman _ TEDxEastVan [ARWBdfWpDyc].en.vtt"):
        self.file_name = name

    def delete_first_4_lines(self):
        with open(self.file_name, 'rt') as vtt_file:
            lines = vtt_file.readlines()

        with open(self.file_name, 'wt') as vtt_file:
            vtt_file.writelines(lines[7:])

    def delete_newlines(self):
        regex = r"\n+"
        with open(self.file_name, 'rt') as vtt_file:
            file_contents = vtt_file.read()
            file_contents_removed = re.sub(regex, ' ', file_contents)

        with open(self.file_name, 'wt') as vtt_file:
            vtt_file.write(file_contents_removed)

    def delete_timestamps(self):
        regex = r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}"
        with open(self.file_name, 'rt') as vtt_file:
            file_contents = vtt_file.read()
            without_timestamps = re.sub(regex, '', file_contents)

        with open(self.file_name, 'wt') as vtt_file:
            vtt_file.write(without_timestamps)


SubTxt = SubtitleTXT()
download_vtt_file()
SubTxt.delete_first_4_lines()
SubTxt.delete_timestamps()
SubTxt.delete_newlines()
