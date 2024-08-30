'''
Implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... 
(i.e., three periods).
'''

""""
replace - Replace the space character with 3 dots (or 3 periods)
main - where the program will run
"""

# isspace - return True if the function found a space and False if don't
# replace - replace one substring for another in a string (type str)

def replace(phrase):
    for word in phrase:
        if word.isspace():
            phrase = phrase.replace(" ", "...")
    return phrase

def main():
    phrase = input()
    print(replace(phrase))

main()