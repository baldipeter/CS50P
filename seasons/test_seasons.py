from seasons import time, d_to_m
from datetime import date, timedelta
import pytest


def test_time_correct():
    assert time("1999-01-01") == date(1999, 1, 1)
    assert time("2008-12-31") == date(2008, 12, 31)
    assert time("2008-02-29") == date(2008, 2, 29)


def test_time_incorrect():
    with pytest.raises(SystemExit):
        time("2007-02-29")
        time("2007-02")
        time("cat")
        time("January 01, 1999")


def test_d_to_m():
    assert d_to_m(timedelta(1)) == 1440
    assert d_to_m(timedelta(365)) == 525600
