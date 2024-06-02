from um import count


def test_count_um():
    assert count("um") == 1
    assert count("UM, um, uM") == 3


def test_count_in_word():
    assert count("Yummy") == 0
    assert count("um, yummy") == 1
    assert count("Um, thanks for the album.") == 1


def test_count_multiple_um():
    assert count("umumumumum") == 0
    assert count("um, umumumumum, yummum, umyum, yum") == 1

def test_count_punct():
    assert count("Um!") == 1
    assert count("Um?") == 1
    assert count("?Um.!") == 1
