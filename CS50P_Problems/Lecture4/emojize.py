import emoji
"""
Because emoji aren't quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, for instance, 
:thombs_up:, which will be automatically converted to 👍.
    
Implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) 
therein to their corresponding emoji.
"""

def main():
    phrase = input("Input: ")
    print(emoji.emojize(phrase, language='alias'))

main()