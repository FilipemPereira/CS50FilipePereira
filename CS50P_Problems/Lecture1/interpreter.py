"""
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a 
floating-point value formatted to one decimal place. Assume that the user's input will be formatted as x y z, with one space between x and y and one space
between y and z, wherein:
x is an integer, y is a operator symbol and z is an integer too.
"""

# However a give the name x and y to the 2 operands respectively
def mathInterpreter(input) -> str:
    # unpack the list
    x, operator, y = input.split(" ")
    n1 = float(x)
    n2 = float(y)
    match operator:
        case "+":
            result = n1 + n2
        case "-":
            result = n1 - n2
        case "*":
            result = n1 * n2
        case "/":
            result = n1 / n2
        case _:
            result = "ERROR!"

    return result

def main():
    line = input("Expression: ")
    print(mathInterpreter(line))

main()