from fuel import convert
from fuel import gauge
import pytest

def test_convert_correct():
    assert convert("1/2") == 50

# test that raises an exception
def test_convert_valueError():
    with pytest.raises(ValueError):
        convert("2/1")

def test_convert_zeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge__returns_E():
    assert gauge(1) == "E"

def test_gauge__returns_percentage():
    assert gauge(50) == "50%"

def test_gauge__returns_F():
    assert gauge(99) == "F"
