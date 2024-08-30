import sys
"""
Implement a program that count the lines of a program, except the ones that are comments or are blanks.
"""

# read the file
def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    return lines

# count the number of lines that contain code
def count_lines(lines):
    count = 0
    for line in lines:
        if line.lstrip().startswith("# ") or line.lstrip().startswith("#") or line.isspace():
            continue
        else:
            count += 1
    return count

# Program logic
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not ".py" in sys.argv[1]:
        sys.exit("Not a Python file")

    lines = read_file(sys.argv[1])
    n = count_lines(lines)

    print(n)

main()
