from working import convert
import pytest

def test_convert1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_convert3():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"

def test_convert4():
    assert convert("10 AM to 08:00 PM") == "10:00 to 20:00"

# test times where "to" are omitted
def test_convert5():
     with pytest.raises(ValueError):
        convert("9 AM 5 PM")

# test out of range times
def test_convert6():
     with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
