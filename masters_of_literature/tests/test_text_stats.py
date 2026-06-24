"""
Testing functions in module text_stats.py!
"""

from masters_of_literature.text_analysis import text_stats as stats


def test_empty_work():
    work = {"list_of_words": []}
    assert stats.how_many_words(work) == 0

def test_three_words_to_how_many_words_function():
    work = {"list_of_words": ["word", "word", "word"]}
    assert stats.how_many_words(work) == 3

def test_work_with_two_different_words_unique_function():
    work = {"list_of_words": ["word", "ward"]}
    assert stats.how_many_unique_words(work) == 2

def test_work_with_two_same_words_unique_function():
    work = {"list_of_words": ["word", "word"]}
    assert stats.how_many_unique_words(work) == 1

def average_word_length_for_empty_list_is_zero():
    work = {"list_of_words": []}
    assert stats.average_length_of_words(work) == 0

def average_word_length_for_two_words():
    work = {"list_of_words": ["Ala", "ma"]}
    assert stats.average_length_of_words(work) == 2.5

def test_more_than_ten_most_common_words():
    work = {"list_of_words": [chr(ord('a') + i) for i in range(11)]}
    assert stats.most_common_words(work).shape[0] == 11

def test_less_than_ten_most_common_words():
    work = {"list_of_words": 11 * ["word"]}
    assert stats.most_common_words(work).shape[0] == 1

def test_print_stats_if_good_message(capsys):
    work = {"how_many_lines": 11, "list_of_words": 11 * ["word"]}
    stats.print_stats(work)
    captured = capsys.readouterr()
    assert captured.out.startswith("Total number of lines: 11")


