""""
In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 
(otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned 
unchanged.
"""

def replace(phrase):
    # replace - replace a substring for another in the original str object
    phrase = phrase.replace(":)", "🙂")
    phrase = phrase.replace(":(", "🙁")
    return phrase

def main():
    phrase = input()
    print(replace(phrase))

main()