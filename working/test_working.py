from working import convert
import pytest


def test_convert_wo_min():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_convert_min():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_convert_error_oufofrange():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
        convert("9:00 AM to 17:00 PM")


# I truly don't know why it doesn't catch " to " omission...
def test_convert_error_input():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
        convert("9:00 AM 5:00 PM")
        convert("9:60 AM to 5:60")
        convert("9 AM - 5 PM")
        convert("9 AM 5 PM")
        convert("9 AM to 5")
