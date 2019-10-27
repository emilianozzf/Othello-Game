from text_cleaner import TextCleaner


def test_keep_required_characters():
    """Tests the keep_required_characters method"""
    tc = TextCleaner("file_name")
    text = "hello, i'm jerry (emiliano). you can call me mr. zhu."
    clean_text = tc.keep_required_characters(text)
    assert clean_text == "hello, i'm jerry emiliano. you can call me mr. zhu."


def test_render_comma_tokens():
    """Tests the render_comma_tokens method"""
    tc = TextCleaner("file_name")
    text = "hello, i'm jerry emiliano. you can call me mr. zhu."
    clean_text = tc.render_comma_tokens(text)
    assert clean_text == ("hello COMMA i'm jerry emiliano." +
                          " you can call me mr. zhu.")


def test_clean_other_periods():
    """Tests the test_clean_other_periods method"""
    tc = TextCleaner("file_name")
    text = "hello COMMA i'm jerry emiliano. you can call me mr. zhu."
    clean_text = tc.clean_other_periods(text)
    assert clean_text == ("hello COMMA i'm jerry emiliano." +
                          " you can call me mr zhu.")


def test_split_with_periods():
    """Tests the split_with_periods method"""
    tc = TextCleaner("file_name")
    text = "hello COMMA i'm jerry emiliano. you can call me mr zhu. "
    clean_sentences = tc.split_with_periods(text)
    assert clean_sentences[0] == "hello COMMA i'm jerry emiliano"
    assert clean_sentences[1] == "you can call me mr zhu"
