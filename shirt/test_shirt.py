from shirt import defense
import pytest
import sys

try:
    from unittest.mock import patch
except ImportError:
    sys.exit("No mock")

def test_correct_args():
    testargs = ["shirt.py", "before1.jpg", "after.jpg"]
    with patch.object(sys, "argv", testargs):
        assert defense() == ("before1.jpg", "after.jpg")


def test_few_args():
    testargs = ["shirt.py", "before1.jpg"]
    with patch.object(sys, "argv", testargs):
        with pytest.raises(SystemExit):
            defense()


def test_many_args():
    testargs = ["shirt.py", "before1.jpg", "after.jpg", "selfie.jpg"]
    with patch.object(sys, "argv", testargs):
        with pytest.raises(SystemExit):
            defense()

def test_different_args():
    testargs = ["shirt.py", "before1.png", "after.jpg"]
    with patch.object(sys, "argv", testargs):
        with pytest.raises(SystemExit):
            defense()


# Sadly I can't seem to wrap my head around Image unittesting for now :(
