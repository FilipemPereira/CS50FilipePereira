import re

"""
An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to 
a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. But each # should be a 
number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! If only NUMB3RS had validated the 
address in that scene!

Implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, 
respectively, if that input is a valid IPv4 address or not.
"""

# Verify if a string represents an IPv4
def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)
    
    if match:
        return all(0 <= int(part) <= 255 for part in match.groups())
    else:
        return False

# Main function
def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()
