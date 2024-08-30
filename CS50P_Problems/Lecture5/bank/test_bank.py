from bank import value

def test_value_hello():
    assert value("hello") == 0

def test_value_hello_with_uppercase():
    assert value("Hello") == 0

def test_value_starts_h():
    assert value("hi") == 20

def test_value_other_word():
    assert value("bye") == 100

def test_value_other_word_uppercase():
    assert value("Bye") == 100
