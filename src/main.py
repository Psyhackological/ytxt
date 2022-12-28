"""
ytxt module
(YouTube text)

This module downloads subtitles in .vtt file format
then it opens it as a regular .txt file
removes not needed stuff and in the end
it saves to a clean looking .txt file with the same name.
"""
import glob
import sys

sys.path.append("./ytxt")
sys.path.append("./src/ytxt")

from ytxt import argument_parsing, subtitle_cleaning, yt_dlp_stuff


def main():
    """Main function to make explicit script execution flow."""
    if argument_parsing.args.print_langs is False:
        argument_parsing.args.urls = [r"https://youtu.be/F1Hq8eVOMHs"]
        yt_dlp_stuff.download_vtt_file()
        vtt_files_list = glob.glob("*.vtt")
        for vtt_file in vtt_files_list:
            sub_txt = subtitle_cleaning.SubtitleTxt(vtt_file)
            sub_txt.clean_to_txt()
    else:
        yt_dlp_stuff.show_subs_langs()


if __name__ == "__main__":
    main()
