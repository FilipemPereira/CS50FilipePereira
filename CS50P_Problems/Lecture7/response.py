from validator_collection import checkers

"""
Using either validator-collection or validators from PyPI, implement a program that prompts the user for an email 
address via input and then prints Valid or Invalid, respectively, if the input is a syntactically valid email address. 
You may not use re. And do not validate whether the email address's domain name actually exists.
"""


def is_valid_email(email: str):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"

def main():
    print(is_valid_email(input("What's your email address? ")))


main()