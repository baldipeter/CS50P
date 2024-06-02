from twttr import shorten

def test_basic():
    assert shorten("twitter") == "twttr"


def test_multiple_words():
    assert shorten("What's your name") == "Wht's yr nm"


def test_no_vovel():
    assert shorten("CS50") == "CS50"


def test_vovels():
    assert shorten("AaEeIiOoUu") == ""


def test_punctuation():
    assert shorten("What?!") == "Wht?!"
