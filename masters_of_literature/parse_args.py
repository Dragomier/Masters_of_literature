import argparse
from masters_of_literature.my_types import positive_int

def create_args(argv = None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
    '--dictionary',
        nargs = '+',
        help = "Sets a dictionary to analyze Master's work",
    )

    parser.add_argument(
    '--dictionary-stats',
        help = "Displays basic statistics about the dictionary, e.g. number of lines, number of words etc.",
        action = "store_true"
    )

    parser.add_argument(
        '--works',
        help = "Master's work to analyze",
        nargs = '+'
    )

    # Change sent by request via e-mail by prof. Jabłonowski 24.06 to name this flag file-stats
    parser.add_argument(
        '--file-stats',
        help = "Displays basic statistics about the Master's works, e.g. number of lines, number of words, words with top 10 occurences",
        action = "store_true"
    )

    parser.add_argument(
        '--no-words',
        help = "For each work, it displays the words, which are used by Master, but are not found in the modern dictionary",
        action = "store_true"
    )

    parser.add_argument(
        '--frequencies',
        help = "For each work, it displays top n most frequently used words, in case there are more words with the same number of occurrences, program will show them.",
        nargs = 1,
        type = positive_int.positive_int
    )

    parser.add_argument(
        '--prob-function',
        help="For each pair of works, it displays the probability that they were written by the same author",
        action = "store_true"
    )
    return parser.parse_args(argv)