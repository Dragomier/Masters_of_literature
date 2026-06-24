from masters_of_literature.text_analysis import text_authorship_prob as prob

def test_diversity_all_words_the_same_in_both():
    work1 = {"list_of_words": ["a"] * 1000}
    work2 = {"list_of_words": ["a"] * 1000}

    assert prob.diversity_comparison(work1, work2) == 100

def test_diversity_all_different_in_first_the_same_in_second():
    work1 = {"list_of_words": [str(i) for i in range(1000)]}
    work2 = {"list_of_words": ["a"] * 1000}

    assert prob.diversity_comparison(work1, work2) == 0

def test_similarity_all_words_the_same_and_not_in_stopwords():
    work1 = {"list_of_words": ["karma"] * 1000}
    work2 = {"list_of_words": ["karma"] * 1000}

    assert prob.similarity_comparison(work1, work2) == 5.0

def test_similarity_all_words_the_same_in_stopwords():
    work1 = {"list_of_words": ["a"] * 1000}
    work2 = {"list_of_words": ["a"] * 1000}

    assert prob.similarity_comparison(work1, work2) == 0

def test_average_word_all_words_the_same():
    work1 = {"list_of_words": ["a"] * 1000}
    work2 = {"list_of_words": ["a"] * 1000}

    assert prob.average_len_of_word_comparison(work1, work2) == 100

def test_average_word_words_not_the_same_length():
    work1 = {"list_of_words": ["a"]}
    work2 = {"list_of_words": ["bb"]}

    assert prob.average_len_of_word_comparison(work1, work2) == 0

def test_average_word_words_not_the_same_length_50_percent():
    work1 = {"list_of_words": ["a", "ab"]}
    work2 = {"list_of_words": ["bb"]}

    assert prob.average_len_of_word_comparison(work1, work2) == 50.0
