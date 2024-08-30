"""
Implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then
bid adieu to those names, separating two names with one 'and', three names with two commas and one and, and names with commas and one and, as in the below:
"""

def write_names(names):
    n = len(names)
    out = ""
    for i in range(n - 1):
        name = names[i] + ', '
        out += name
    out += "and " + names[n -1]
    return "\nAdieu, adieu, to " + out

def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    if len(names) == 1:
        print("\nAdieu, adieu, to " + names[0])
    elif len(names) == 2:
        print("\nAdieu, adieu, to " + names[0] + " and " + names[1])
    else:
        print(write_names(names))

main()
