import re
import glob
from ytxt.lib.subtitle_cleaning import SubtitleTxt


vtt_files_list = glob.glob("*.vtt")


def test_delete_not_needed_stuff():
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)
        sub_txt.clean_to_txt()
        sub_txt = SubtitleTxt(vtt_file)
        sub_txt.delete_not_needed_stuff()
        match = re.search(r"\d{2}:\d{2}:\d{2}\.\d{3} --> .+", sub_txt.file_text)
        assert match is None


def test_delete_newlines():
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)
        sub_txt.delete_newlines()
        match = re.search(r"(\n|&nbsp;|\u200B)+", sub_txt.file_text)
        assert match is None


def test_delete_timestamps():
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)
        sub_txt.delete_timestamps()
        match = re.search(
            r"\d{2}:\d{2}:\d{2}(,|\.){1}\d{3} .+ \d{2}:\d{2}:\d{2}(,|\.){1}\d{3}",
            sub_txt.file_text,
        )
        assert match is None


def test_delete_start_and_end_whitespace():
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)
        sub_txt.delete_start_and_end_whitespace()
        match = re.search(r"(^\s|\s$)", sub_txt.file_text)
        assert match is None


def test_delete_double_or_more_whitespace():
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)
        sub_txt.delete_double_or_more_whitespace()
        match = re.search(r"\s{2,}", sub_txt.file_text)
        assert match is None


def test_clean_to_txt(tmpdir):
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)
        sub_txt.clean_to_txt()
        assert sub_txt.file_text == ""
        assert (tmpdir / f"{sub_txt.filename}.txt").exists()
