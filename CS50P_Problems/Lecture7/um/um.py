import re
import string

"""
Implement a function called count that expects a line of text as input as a str and returns, as an int, the number of 
times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. 
"""

def clean(phrase):
    for i in phrase:
        if i in string.punctuation:
            phrase = phrase.replace(i, "")
    return phrase

def count(phrase):
    count = 0
    new_phrase = clean(phrase)

    words = new_phrase.split(" ")

    for word in words:
        if re.fullmatch("um", word, re.IGNORECASE):
            count += 1
    return count 

def main():
    print(count(input("Text: ")))


if __name__ == "__main__":
    main()
