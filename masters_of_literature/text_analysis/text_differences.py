from masters_of_literature.text_analysis import text_stats as stats
from masters_of_literature.read_input import read_text as read
import pandas as pd

def differences(work, dictionary):
    dict_words = set(dictionary["list_of_words"])
    ancient_words = []
    for word in work["list_of_words"]:
        if word not in dict_words:
            ancient_words.append(word)
    return stats.most_common_words({"list_of_words": ancient_words}, len(ancient_words))

def give_characteristic_words(work1, work2):
    common_words_work1 = stats.most_common_words(work1, len(work1["list_of_words"]))
    common_words_work2 = stats.most_common_words(work2, len(work2["list_of_words"]))
    popular_nowadays = read.read_dictionary(r"masters_of_literature/dictionaries/polish_stopwords.txt")
    set_of_popular_words = set(popular_nowadays["list_of_words"])

    common_words_work1 = common_words_work1[~common_words_work1["word"].isin(set_of_popular_words)].iloc[:100]
    common_words_work2 = common_words_work2[~common_words_work2["word"].isin(set_of_popular_words)].iloc[:100]

    common_for_both = pd.merge(common_words_work1, common_words_work2, on="word")
    common_for_both["total"] = common_for_both["count_x"] + common_for_both["count_y"]
    common_for_both = common_for_both.sort_values(by=["total"], ascending=False)
    common_for_both.index = range(1, len(common_for_both) + 1)
    common_for_both.columns = ["word", "first_work", "second_work", "total"]
    return common_for_both[["word", "first_work", "second_work"]]


