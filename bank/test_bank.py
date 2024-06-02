from bank import value


def test_hello():
    assert value("Hello") == 0
    assert value("Hello Newmann") == 0


def test_h():
    assert value("How you doin?") == 20


def test_not_start_h():
    assert value("What... hi there!") == 100
    assert value("Why... Hello there!") == 100


def test_no_h():
    assert value("Goodday to you!") == 100


def case_sense():
    assert value("helLO") == 0
    assert value("hOW ya DoIN'?") == 20
    assert value("gOoOD Day") == 100
