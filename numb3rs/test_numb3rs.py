from numb3rs import validate


def test_validate_incorrect_input():
    assert validate("cat") == False
    assert validate("0") == False
    assert validate("0.0") == False
    assert validate("255.255.255.255.") == False
    assert validate("255.255.255.255.255") == False


def test_validate_not_in_range():
    assert validate("255.255.255.256") == False
    assert validate("-1.0.0.0") == False


def test_validate_correct():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
