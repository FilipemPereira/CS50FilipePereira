from seasons import calculate_total_minutes, check_dob_string
import pytest

def test_calculate_1():
    assert calculate_total_minutes("2023-08-29") == "Five hundred twenty-seven thousand forty minutes"

def test_calculate_2():
    assert calculate_total_minutes("2022-08-29") == "One million, fifty-two thousand, six hundred forty minutes"

def test_check_1():
     with pytest.raises(ValueError):
        check_dob_string("January 1, 2000")