import pandas as pd
import numpy as np

def how_many_lines(work):
    return work["how_many_lines"]

def how_many_words(work):
    return len(work["list_of_words"])

def how_many_unique_words(work):
    return len(set(work["list_of_words"]))

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

def most_common_words(work, how_many = 10):
    words = pd.DataFrame({'word': work["list_of_words"]})
    common_words = words.groupby("word").size().reset_index(name='count')
    common_words = common_words.sort_values(by = ["count", "word"], ascending= [False, True])
    if len(common_words) > how_many:
        common_words = common_words[common_words["count"] >= int(common_words.iloc[how_many - 1]["count"])]
    common_words.index = range(1, len(common_words) + 1)
    return common_words

def print_stats(work):
    print(f"Total number of lines: {how_many_lines(work)} \n")
    print(f"Total number of words: {how_many_lines(work)} \n")
    print(f"Total number of unique words: {how_many_unique_words(work)} \n")
    print(f"Average length of a word: {average_length_of_words(work)} \n")
    print(f"Words with the most number of occurrences: \n {most_common_words(work)}")

def give_stats(work):
    return [how_many_lines(work), how_many_words(work), how_many_unique_words(work), unique_words_percentage(work),
            average_length_of_words(work)]