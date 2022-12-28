import sys
import yt_dlp
from argument_parsing import args


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
