from plates import is_valid

# May start with 2 letters
def test_beginning_alphabetical():
    assert is_valid("CS") == True
    assert is_valid("C1") == False

# 2 < length < 6
def test_length():
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False

# Test number placement
def test_number_placement():
    assert is_valid("AAA222") == True
    assert is_valid("AA22A") == False

# Test if the first number cannot be 0
def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS01") == False

# Test if punctuation sign exist
def test_punctuation():
    assert is_valid("AA-222") == False
    assert is_valid("AAA222") == True