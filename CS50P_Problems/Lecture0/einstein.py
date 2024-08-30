"""
Calcule E = mc^2!
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number
of Joules as an integer. Assume that the user will input an integer.
"""

def calculation(mass):
    c: int = 300000000
    return mass * c**2

def main():
    mass = int(input("m:"))
    print(calculation(mass))

main()