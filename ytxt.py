import yt_dlp
import argparse
import re

parser = argparse.ArgumentParser(prog="YouTube Video to TXT")
parser.add_argument(nargs='?', type=str, help="YouTube Video URL (str)", dest="url")
args = parser.parse_args()

args.url = r"https://www.youtube.com/watch?v=Pj-h6MEgE7I"


# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L180
def download_vtt_file():
    ydl_opts = {  # YT-DLP OPTIONS
        'subtitlesformat': "vtt",
        'writesubtitles': True,
        'skip_download': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # SPECIAL YT-DLP OBJECT WITH YDL_OPTS (OPTIONS)
        try:
            result = ydl.extract_info(args.url, download=True)  # WE WANT INFO WITHOUT DOWNLOADING THE VIDEO
            subtitles_langs = result["subtitles"]
            video_title = result["title"]
            video_id = result["id"]

            return subtitles_langs, video_title, video_id
        except yt_dlp.utils.DownloadError:  # SILLY YOU, THAT IS NOT A VALID
            quit()


class SubtitleTXT:
    def __init__(self):
        with open(f"{vid_title} [{vid_id}].en.vtt", 'rt') as vtt_file:
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
        regex = r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*"
        self.file_text = re.sub(regex, '', self.file_text)

    def make_file(self):
        with open("clean.txt", "wt") as clean_txt:
            clean_txt.write(self.file_text)

    def clean_to_txt(self):
        self.delete_not_needed_stuff()
        self.delete_timestamps()
        self.delete_newlines()
        self.make_file()


subs_langs, vid_title, vid_id = download_vtt_file()
SubTxt = SubtitleTXT()
SubTxt.clean_to_txt()
