from ngram_frequencies import NgramFrequencies


def test_add_item():
    """Tests the add_item method"""
    nf = NgramFrequencies()
    nf.add_item("unigram")
    nf.add_item("bi gram")
    nf.add_item("t ri gram")
    assert nf.unigrams_counts["unigram"] == 1
    assert nf.bigrams_counts["bi_gram"] == 1
    assert nf.trigrams_counts["t_ri_gram"] == 1


def test_top_n_freqs():
    """Tests the top_n_freqs method"""
    nf = NgramFrequencies()
    nf.add_item("unigram")
    nf.add_item("bi gram")
    nf.add_item("t ri gram")
    assert nf.top_n_freqs("unigrams")[0] == ("unigram", 1)
    assert nf.top_n_freqs("bigrams")[0] == ("bi_gram", 1)
    assert nf.top_n_freqs("trigrams")[0] == ("t_ri_gram", 1)


def test_top_n_counts():
    """Tests the top_n_counts method"""
    nf = NgramFrequencies()
    nf.add_item("unigram")
    nf.add_item("bi gram")
    nf.add_item("t ri gram")
    assert nf.top_n_counts("unigrams")[0] == ("unigram", 1)
    assert nf.top_n_counts("bigrams")[0] == ("bi_gram", 1)
    assert nf.top_n_counts("trigrams")[0] == ("t_ri_gram", 1)


def test_frequency():
    """Tests the frequency method"""
    nf = NgramFrequencies()
    nf.add_item("unigram")
    nf.add_item("un1gram")
    nf.add_item("bi gram")
    nf.add_item("b1 gram")
    nf.add_item("t ri gram")
    nf.add_item("t r1 gram")
    assert nf.frequency(("unigram", 1)) == 0.5
    assert nf.frequency(("bi_gram", 1)) == 0.5
    assert nf.frequency(("t_ri_gram", 1)) == 0.5
