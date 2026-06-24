"""
Testing functions in module read_text.py!
"""

from masters_of_literature.read_input import read_text as read


def test_cleaning_extra_spaces():
    line = "pies ma                  kota"
    assert read.clean_text_line(line) == ["pies", "ma", "kota"]

def test_cleaning_upper_letters():
    line = "ALA MA KOTA"
    assert read.clean_text_line(line) == ["ala", "ma", "kota"]

def test_cleaning_special_characters_in_text():
    line = "!,--.:;"
    assert read.clean_text_line(line) == []

def test_how_many_lines(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Ala ma kota \n Jaś ma pingwina \n Jacek nie ma zwierząt", encoding = "utf-8")
    assert read.read_work(file)["how_many_lines"] == 3

def test_does_dictionary_read_all_words(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("ja, mój, kto \npalec, kocham, biceps", encoding = "utf-8")
    assert len(read.read_work(file)["list_of_words"]) == 6

def test_does_dictionary_read_empty_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("")
    assert len(read.read_work(file)["list_of_words"]) == 0

