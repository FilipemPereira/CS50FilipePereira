from twttr import shorten

def test_shorten_vowel_replacement_lowercase():
    assert shorten("twitter") == "twttr"

def test_shorten_vowel_replacement_uppercase():
    assert shorten("twItter") == "twttr"

def test_shorten_vowel_replacement_with_numbers():
    assert shorten("4ever") == "4vr"

def test_shorten_vowel_replacement_with_punctuation():
    assert shorten("Done!") == "Dn!"
