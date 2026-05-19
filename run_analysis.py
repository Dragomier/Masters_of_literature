import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
    '--dictionary',
        help = "Sets a dictionary to analyze Master's work",
        default = "dictionaries/pl.txt"
    )

    parser.add_argument(
    '--dictionary-stats',
        help = "Displays basic statistics about the dictionary, e.g. number of lines, number of words etc."
    )

    parser.add_argument(
        '--works',
        help = "Master's work to analyze",
        default = "texts/pan_tadeusz.txt"
    )

    parser.add_argument(
        '--work-stats',
        help = "Displays basic statistics about the Master's works, e.g. number of lines, number of words, words with top 10 occurences"
    )

    parser.add_argument(
        '--no-words',
        help = "For each work, it displays the words, which are used by Master, but are not found in the modern dictionary"
    )

    parser.add_argument(
        '--frequencies',
        help = "For each work, it displays top n most frequently used words, in case there are more words with the same number of occurences, program will show them akk, ",
        default = 100
    )
    args = parser.parse_args()
    return args

args = parse_args()
print(args.frequencies)