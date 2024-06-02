from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar = Jar(-1)
        jar = Jar("cat")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(9)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(3)


def test_deposit_capacity():
    jar = Jar(50)
    jar.deposit(50)
    assert jar.size == 50
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(2)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_withdraw_capacity():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(5)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
