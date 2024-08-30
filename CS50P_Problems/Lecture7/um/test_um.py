from um import count

# Tests to validate count function

def test_count1():
    assert count("hello, um, world") == 1

def test_count2():
    assert count("Um, hello world") == 1

def test_count3():
    assert count("Um, what is regular expressions? Um Let me see what it is about?") == 2

def test_count4():
    assert count("Question number 1: What is Regex") == 0
