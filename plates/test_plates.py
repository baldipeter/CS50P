from plates import is_valid


def test_len():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False


def test_start():
    assert is_valid("1A") == False
    assert is_valid("A1") == False


def test_num_start():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


def test_num_not_middle():
    assert is_valid("CSP50") == True
    assert is_valid("CS50P") == False


def test_punctuation():
    assert is_valid("CS 50") == False
    assert is_valid("CS50 ") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS50.") == False
    assert is_valid("CS!50") == False
    assert is_valid("CS50!") == False
