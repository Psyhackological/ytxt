import re
from pathlib import Path


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

    def delete_start_and_end_whitespace(self):
        """Deletes any of the start or end whitespace and saves it to a self.file_text"""
        regex = r"(^\s|\s$)"
        self.file_text = re.sub(regex, "", self.file_text)

    def delete_double_or_more_whitespace(self):
        """Deletes double or more whitespace and saves it to a self.file_text"""
        regex = r"\s{2,}"
        self.file_text = re.sub(regex, "", self.file_text)

    def make_file(self):
        """Creates the .txt file with the same basename as .vtt file."""
        with open(f"{self.filename}.txt", "wt", encoding="utf-8") as clean_txt:
            clean_txt.write(self.file_text)

    def clean_to_txt(self):
        """Class method wrapper to make cleaning procces explicit and easier to use."""
        print("Deleting subtitles heading...")
        self.delete_not_needed_stuff()
        print("Done 1/5")

        print("Deleting subtitles timestamps...")
        self.delete_timestamps()
        print("Done 2/5")

        print("Deleting subtitles newlines...")
        self.delete_newlines()
        print("Done 3/5")

        print("Deleting start and end whitespace...")
        self.delete_start_and_end_whitespace()
        print("Done 4/5")

        print("Deleting double or more whitespace...")
        self.delete_double_or_more_whitespace()
        print("Done. 5/5")

        print("Creating the txt file...")
        self.make_file()
        print(f"Finished saving {self.filename}.txt")
