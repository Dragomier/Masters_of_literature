from masters_of_literature import parse_args as args
from masters_of_literature.read_input import read_text as read
from masters_of_literature.text_analysis import text_stats as stats, text_differences as diff, text_authorship_prob as prob

def main():
    my_args = args.create_args()
    dictionary_words = read.read_dictionary(my_args.dictionary[0])
    if my_args.dictionary_stats:
        stats.print_stats(dictionary_words)

    works = []
    for i, work in enumerate(my_args.works):
        works.append(read.read_work(work))
        if my_args.file_stats:
            stats.print_stats(works[i])

    if my_args.no_words:
        for index in range(len(works)):
            print(diff.differences(works[index], dictionary_words).head(50))

    if my_args.frequencies is not None:
        for index in range(len(works)):
            print(stats.most_common_words(works[index], int(my_args.frequencies[0])))

    if my_args.prob_function:
        how_many = len(works)
        for i in range(how_many):
            for j in range(i + 1, how_many):
                print(f"Probability that the same author wrote texts {i + 1} and {j + 1} is {prob.probability_function(works[i], works[j])}")
if __name__ == "__main__":
    main()