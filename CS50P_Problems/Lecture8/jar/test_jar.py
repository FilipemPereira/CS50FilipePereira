from jar import Jar
import pytest

def test_init1():
    jar = Jar()
    assert jar.capacity == 12

def test_init2():
    jar = Jar(capacity=24, n_cookies=12)
    assert jar.capacity == 24

def test_init3():
    jar = Jar(capacity=24, n_cookies=12)
    assert jar.size == 12

def test_str1():
    jar = Jar()
    assert str(jar) == ""

def test_str1():
    jar = Jar()
    jar.deposit(9)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit1():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1

def test_deposit2():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar(n_cookies=10)
    jar.withdraw(8)
    assert jar.size == 2

def test_withdraw2():
    jar = Jar(n_cookies=10)
    with pytest.raises(ValueError):
        jar.withdraw(11)