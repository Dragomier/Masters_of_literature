from . import text_differences as diff
from . import text_stats as stats
from collections import Counter

def diversity_comparison(work1, work2):
    percentage_of_uniqueness1, percentage_of_uniqueness2 = stats.unique_words_percentage(work1), stats.unique_words_percentage(work2)
    percentage_of_uniqueness1 = float(percentage_of_uniqueness1[:-1])
    percentage_of_uniqueness2 = float(percentage_of_uniqueness2[:-1])
    return max(100 - round(abs(percentage_of_uniqueness1 - percentage_of_uniqueness2)/20, 2) * 100, 0)

def similarity_comparison(work1, work2):
    common_for_both = diff.give_characteristic_words(work1, work2)
    return min(round(common_for_both.shape[0]/20, 2) * 100, 100)

def print_average_len_of_word_comparison(work1, work2):
    lengths1 = [len(word) for word in work1["list_of_words"]]
    lengths2 = [len(word) for word in work2["list_of_words"]]

    data_1 = Counter(lengths1)
    data_2 = Counter(lengths2)
    return [data_1, data_2]

def average_len_of_word_comparison(work1, work2):
    avg1 = stats.average_length_of_words(work1)
    avg2 = stats.average_length_of_words(work2)
    return max(100 - 100 * abs(avg1 - avg2), 0)

def probability_function(work1, work2):
    result = round(0.4 * diversity_comparison(work1, work2)+0.4 * similarity_comparison(work2, work1)+0.2 * average_len_of_word_comparison(work1, work2), 2)
    return f"{result}%"