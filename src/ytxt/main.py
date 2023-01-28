"""
ytxt module
(YouTube text)

This module downloads subtitles in .vtt file format
then it opens it as a regular .txt file
removes not needed stuff and in the end
it saves to a clean looking .txt file with the same name.
"""
import glob
from ytxt.lib import subtitle_cleaning, yt_dlp_stuff
from ytxt.lib.argument_parsing import parse_args


def main():
    """Main function to make explicit script execution flow."""
    args = parse_args()
    if args.print_langs is False:
        yt_dlp_stuff.download_vtt_file(args)
        vtt_files_list = glob.glob("*.vtt")
        for vtt_file in vtt_files_list:
            sub_txt = subtitle_cleaning.SubtitleTxt(vtt_file)
            sub_txt.clean_to_txt()
    else:
        yt_dlp_stuff.show_subs_langs(args)


if __name__ == "__main__":
    main()
