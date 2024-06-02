from fuel import convert, gauge
import pytest


def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("A/B")
        convert("1/B")
        convert("A/1")
        convert("5/4")
        convert("-1/10")


def test_convert_valid():
    assert convert("1/10") == 10
    assert convert("2/4") == 50


def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_gauge_half():
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"


def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
