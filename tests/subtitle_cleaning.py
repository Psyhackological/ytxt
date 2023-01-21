"""
This module contains tests for the subtitle_cleaning module.
It tests each of the cleaning methods individually and also the
main wrapper method clean_to_txt. It tests if the cleaning
methods are working correctly and also if the resulting txt
file is correctly created.
"""
import re
import glob
from src.ytxt.lib.subtitle_cleaning import SubtitleTxt


vtt_files_list = glob.glob("*.vtt")


def test_delete_not_needed_stuff():
    """Tests whether the delete_not_needed_stuff() method removes the heading
    information from the .vtt file."""
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)

        match_before = re.search(
            r"^WEBVTT\nKind: captions\nLanguage: en(?:\-GB)?", sub_txt.file_text
        )
        sub_txt.delete_not_needed_stuff()
        match_after = re.search(
            r"^WEBVTT\nKind: captions\nLanguage: en(?:\-GB)?", sub_txt.file_text
        )
        assert match_before is not None
        assert match_after is None


def test_delete_newlines():
    """Tests whether the delete_newlines() method removes newlines,
    and \u200B from the .vtt file."""
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)

        match_before = re.search(r"(\n|&nbsp;|\u200B)+", sub_txt.file_text)
        sub_txt.delete_newlines()
        match_after = re.search(r"(\n|&nbsp;|\u200B)+", sub_txt.file_text)

        assert match_before is not None
        assert match_after is None


def test_delete_timestamps():
    """Test delete_timestamps method of SubtitleTxt class
    This method should be able to remove timestamps in the format
    'HH:MM:SS,mmm --> HH:MM:SS,mmm' or 'HH:MM:SS.mmm --> HH:MM:SS.mmm'
    from the file_text attribute of SubtitleTxt class instances.
    """
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)

        match_before = re.search(
            r"\d{2}:\d{2}:\d{2}(,|\.){1}\d{3} .+ \d{2}:\d{2}:\d{2}(,|\.){1}\d{3}",
            sub_txt.file_text,
        )
        sub_txt.delete_timestamps()

        match_after = re.search(
            r"\d{2}:\d{2}:\d{2}(,|\.){1}\d{3} .+ \d{2}:\d{2}:\d{2}(,|\.){1}\d{3}",
            sub_txt.file_text,
        )

        assert match_before is not None
        assert match_after is None


def test_delete_start_and_end_whitespace():
    """This test function checks whether the
    delete_start_and_end_whitespace method of SubtitleTxt class
    removes any whitespaces at the start and end of the text."""
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)

        match_before = re.search(r"(^\s|\s$)", sub_txt.file_text)
        sub_txt.delete_start_and_end_whitespace()
        match_after = re.search(r"(^\s|\s$)", sub_txt.file_text)

        assert match_before is not None
        assert match_after is None


def test_delete_double_or_more_whitespace():
    """Test for delete_double_or_more_whitespace method in subtitle_cleaning module."""
    for vtt_file in vtt_files_list:
        sub_txt = SubtitleTxt(vtt_file)

        match_before = re.search(r"\s{2,}", sub_txt.file_text)
        sub_txt.delete_double_or_more_whitespace()
        match_after = re.search(r"\s{2,}", sub_txt.file_text)

        assert match_before is not None
        assert match_after is None
