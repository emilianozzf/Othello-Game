from word_ladder import WordLadder


def test_make_ladder():
    """Test the make_ladder method"""
    english_words = load_words()
    wl1 = WordLadder("cat", "hat", english_words[len("cat")])
    wl2 = WordLadder("love", "hate", english_words[len("love")])
    wl3 = WordLadder("angel", "devil", english_words[len("angel")])
    wl4 = WordLadder("earth", "ocean", english_words[len("earth")])
    wl5 = WordLadder("hello", "hi", english_words[len("hello")])

    assert wl1.make_ladder().items == ["cat", "hat"]
    assert wl2.make_ladder().items == ["love", "hove", "have", "hate"]
    assert wl3.make_ladder().items == ["angel", "anger", "aeger", "leger",
                                       "lever", "level", "devel", "devil"]
    assert wl4.make_ladder().items == ["earth", "barth", "barih", "baris",
                                       "batis", "bitis", "aitis", "antis",
                                       "antas", "antal", "ontal", "octal",
                                       "octan", "ocean"]
    assert not wl5.make_ladder()


def load_words():
    """Load words from complete wordlist file"""
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    return valid_words
