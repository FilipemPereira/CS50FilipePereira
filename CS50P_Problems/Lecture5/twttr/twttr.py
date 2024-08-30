"""
Redefine the twttr.py program with the following structure  
"""

# Verify if an letter is vowel
def is_vowel(letter):
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False

# Return the word the modifications (without vowels)
def shorten(word):
    output = ""
    for l in word:
        if is_vowel(l):
            output += ''
        else:
            output += l
    return output

# Program logic
def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")

# To ensure that the test file not call the main function on this file
if __name__ == "__main__":
    main()
