"""
Redefine the bank.py program with the following structure  
"""

# Return the value (int) according to the greeting
def value(greeting):
    if greeting.startswith("hello") or greeting.startswith(" "):
        salutation = 0
    elif greeting[0] == 'h' and greeting != "hello":
        salutation = 20
    else:
        salutation = 100
    return salutation

# Program logic
def main():
    salutation = input("Greeting: ")
    # Threats every word as lower case
    salutation = salutation.lower()

    print(value(salutation))

if __name__ == "__main__":
    main()


