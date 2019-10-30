from bracket_match import BracketMatch


def test_brackets_match():
    """Test the brackets_match method"""
    bm = BracketMatch()
    assert bm.brackets_match("()")
    assert bm.brackets_match(r"a(a[a])a({a})")
    assert not bm.brackets_match("(")
    assert not bm.brackets_match("(}")
    assert not bm.brackets_match("a(a(a)a(a)")
    assert not bm.brackets_match("aa(a))a(a)")
