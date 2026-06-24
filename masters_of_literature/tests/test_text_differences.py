from masters_of_literature.text_analysis import text_differences as diff
from masters_of_literature.read_input import read_text as read


def test_words_which_are_not_in_polish_dict():
    work = {"list_of_words": ["kfajdslkf", "sjfdhfj"]}
    no_words = diff.differences(work, read.read_dictionary("masters_of_literature/dictionaries/pl.txt"))
    assert (no_words.set_index("word").loc["kfajdslkf", "count"]) == 1

def test_characteristic_words():
    work1 = {"list_of_words": ["kfajdslkf"]}
    work2 = {"list_of_words": ["kfajdslkf"]}
    common_words = diff.give_characteristic_words(work1, work2)
    assert (common_words.set_index("word").loc["kfajdslkf", "first_work"]) == 1 and (common_words.set_index("word").loc["kfajdslkf", "second_work"]) == 1

def test_characteristic_words_with_no_common_words():
    work1 = {"list_of_words": ["kfajdslkf"]}
    work2 = {"list_of_words": ["hsgohw"]}
    common_words = diff.give_characteristic_words(work1, work2)
    assert common_words.shape[0] == 0