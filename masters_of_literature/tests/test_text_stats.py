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

def test_many_works_one_word():
    work1 = {"list_of_words": ["word", "word"]}
    work2 = {"list_of_words": ["word", "word"]}
    work3 = {"list_of_words": ["word", "word"]}
    assert stats.how_many_unique_words_in_many_works([work1, work2, work3]) == 1

def test_many_works_different_words():
    work1 = {"list_of_words": ["work", "word"]}
    work2 = {"list_of_words": ["wora", "word"]}
    work3 = {"list_of_words": ["wordfs", "word"]}
    assert stats.how_many_unique_words_in_many_works([work1, work2, work3]) == 4

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

def test_letter_distribution():
    work = {"list_of_words": ["lalaland"]}
    letter_dist = stats.letter_distribution(work)
    assert letter_dist[letter_dist["word"] == "l"]["count"].iloc[0] == 3

def test_letter_distribution_in_many_woks():
    work1 = {"list_of_words": ["lalaland"]}
    work2 = {"list_of_words": ["lalaland"]}
    work3 = {"list_of_words": ["lalaland"]}
    letter_dist = stats.merge_most_common_stuff([stats.letter_distribution(work1),
                                                 stats.letter_distribution(work2),
                                                 stats.letter_distribution(work3)])
    assert letter_dist[letter_dist["word"] == "l"]["total"].iloc[0] == 9

def test_print_stats_if_total_statistics_is_displayed_once(capsys):
    work = {"how_many_lines": 11, "list_of_words": 11 * ["word"]}
    stats.print_stats([work])
    captured = capsys.readouterr()
    assert captured.out.startswith("=======TOTAL STATISTICS=======")

def test_print_stats_if_more_than_one_work(capsys):
    work1 = {"how_many_lines": 11, "list_of_words": 11 * ["word"]}
    work2 = {"how_many_lines": 11, "list_of_words": 11 * ["word"]}
    stats.print_stats([work1, work2])
    captured = capsys.readouterr()
    assert "=======WORK no. 1=======" in captured.out



