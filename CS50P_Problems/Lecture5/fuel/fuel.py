"""
Redefine the fuel.py program with the following structure  
"""

# Convert the input formatted as 'X/Y' in a int -> percentage between 0 and 100. 
# The function should handling exceptions like ValueError, ZeroDivisionError
def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))

            if x > y:
                raise ValueError
            elif y == 0:
                raise ZeroDivisionError
            else:
                return round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            continue

# Should output E, F or the percentage plus the % sign
def gauge(percentage):
    if percentage <= 1:
        output = 'E'
    elif percentage >= 99:
        output = 'F'
    else:
        output = str(percentage) + '%'
    return output

# Program logic
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(f"{gauge(percentage)}")

if __name__ == "__main__":
    main()
