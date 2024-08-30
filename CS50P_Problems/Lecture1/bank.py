"""
In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an 
“h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user's greeting, and treat the user's greeting case-insensitively.
"""

def greeting(salutation):
    salutation = salutation.lower()
    if salutation.startswith("hello") or salutation.startswith(" "):
        salutation = "$0"
    elif salutation[0] == 'h' and salutation != "hello":
        salutation = "$20"
    else:
        salutation = "$100"
    return salutation

def main():
    salutation = input("Greeting: ")
    print(greeting(salutation))

main()