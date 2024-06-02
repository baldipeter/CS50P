from scourgify import defence
from scourgify import open_file
from scourgify import separator
from scourgify import write_file
import pytest
import sys


def test_defence():
    with pytest.raises(SystemExit):
        defence("before.py", "after.py")
        defence("before.csv", "after.py")
        defence("before.py", "after.csv")
    assert defence("before.csv", "after.csv") == None


def test_open_file():
    assert open_file("test_before.csv") == [
        {"name": "name", "house": "house"},
        {"name": "Abbott, Hannah", "house": "Hufflepuff"},
        {"name": "Bell, Katie", "house": "Gryffindor"},
    ]


def test_separator():
    list = [
        {"name": "name", "house": "house"},
        {"name": "Abbott, Hannah", "house": "Hufflepuff"},
        {"name": "Bell, Katie", "house": "Gryffindor"},
    ]
    assert separator(list) == [
        {"first": "Hannah", "last": "Abbott", "house": "Hufflepuff"},
        {"first": "Katie", "last": "Bell", "house": "Gryffindor"},
    ]


def test_write_file():
    try:
        with open("test_after.csv"):
            with pytest.raises(SystemExit):
                write_file(
                    "file_name",
                    [
                        {"first": "Hannah", "last": "Abbott", "house": "Hufflepuff"},
                        {"first": "Katie", "last": "Bell", "house": "Gryffindor"},
                    ],
                )
    except FileNotFoundError:
        assert 1 == 0
