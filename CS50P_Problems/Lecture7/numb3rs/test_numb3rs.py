from numb3rs import validate

# Tests to validate function

def test_validate1_true():
    assert validate("192.45.2.0") == True

def test_validate1_false():
    assert validate("275.3.6.28") == False

def test_validate2_true():
    assert validate("192.45.2.0") == True

def test_validate2_false():
    assert validate("175.300.6.28") == False

def test_validate3_true():
    assert validate("192.45.2.0") == True

def test_validate3_false():
    assert validate("175.3.257.28") == False

def test_validate4_true():
    assert validate("192.45.2.0") == True

def test_validate4_false():
    assert validate("175.3.2.280") == False
