import pandas as pd
import numpy as np
from collections import Counter

def how_many_lines(work):
    return work["how_many_lines"]

def how_many_words(work):
    return len(work["list_of_words"])

def how_many_unique_words(work):
    return len(set(work["list_of_words"]))

def how_many_unique_words_in_many_works(works):
    if len(works) ==  1:
        return how_many_words(works[0])
    else:
        words = works[0]["list_of_words"]
        for i in range(1, len(works)):
            words += works[i]["list_of_words"]
        return len(set(words))

def unique_words_percentage(work):
    unique_percentage = np.array(10 * [0])
    len_work1 = len(work["list_of_words"])

    for i in range(10):
        random_indices1 = np.random.choice(len_work1, 1000, replace=True)

        random_words1 = [work["list_of_words"][i] for i in random_indices1]

        unique_words1 = round(len(set(random_words1))/1000, 2) * 100

        unique_percentage[i] = unique_words1
    return f"{unique_percentage.mean()}%"

def average_length_of_words(work):
    lengths = np.array([len(word) for word in work["list_of_words"]])
    return np.mean(lengths)

def letter_distribution(work):
    string_with_all_words = "".join(work["list_of_words"])
    letter_counter = Counter(string_with_all_words)
    letter_data = pd.DataFrame(list(letter_counter.items()), columns=["word", "count"])
    letter_data.sort_values("count", ascending = False, inplace = True)
    return letter_data

def most_common_words(work, how_many = 10):
    words = pd.DataFrame({'word': work["list_of_words"]})
    common_words = words.groupby("word").size().reset_index(name='count')
    common_words = common_words.sort_values(by = ["count", "word"], ascending= [False, True])
    if len(common_words) > how_many:
        common_words = common_words[common_words["count"] >= int(common_words.iloc[how_many - 1]["count"])]
    common_words.index = range(1, len(common_words) + 1)
    return common_words

def merge_most_common_stuff(works, how_many = 10):
    common_words = works[0]
    for i in range(1, len(works)):
        common_words = pd.merge(common_words, works[i], how="outer", on="word")
        common_words = common_words.fillna(0)

    column_names = [f"count{i}" for i in range(1, len(works) + 1)]
    column_names.insert(0, "word")
    common_words.columns = column_names

    common_words["total"] = common_words[[f"count{i}" for i in range(1, len(works) + 1)]].sum(axis = 1)
    common_words.sort_values(by = ["total"], ascending = False, inplace = True)
    if len(common_words) > how_many:
        common_words = common_words[common_words["total"] >= int(common_words.iloc[how_many - 1]["total"])]
    common_words.index = range(1, len(common_words) + 1)
    return common_words[["word", "total"]]

def give_stats(work):
    return [how_many_lines(work), how_many_words(work), how_many_unique_words(work), unique_words_percentage(work),
            average_length_of_words(work), letter_distribution(work), most_common_words(work)]

def print_stats(works):
    data = [give_stats(work) for work in works]
    if len(data) > 1:
        for i in range(len(data)):
            print(f"=======WORK no. {i + 1}=======")
            print(f"Total number of lines: {data[i][0]} \n")
            print(f"Total number of words: {data[i][1]} \n")
            print(f"Total number of unique words: {data[i][2]} \n")
            print(f"Distribution of letters are: \n {data[i][5]} \n")
            print(f"Words with the most number of occurrences: \n {data[i][6]} \n")

    print(f"=======TOTAL STATISTICS=======")
    print(f"Total number of lines: {sum([data[i][0] for i in range(len(data))])}\n")
    print(f"Total number of words: {sum([data[i][1] for i in range(len(data))])}\n")
    print(f"Total number of unique words: {how_many_unique_words_in_many_works(works)}\n")
    print(
        f"Distribution of letters are: \n {merge_most_common_stuff([data[i][5] for i in range(len(data))], len(data[0][5]))} \n")
    print(
        f"Words with the most number of occurrences: {merge_most_common_stuff([data[i][6] for i in range(len(data))])}")


