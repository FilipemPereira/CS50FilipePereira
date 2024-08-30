from tabulate import tabulate
import csv
import sys

""" 
Implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio's format, 
and outputs a table formatted as ASCII art using tabulate. 
Format the table using the library's grid format. If the user does not specify exactly one command-line argument, or if 
the specified file's name does not end in `.csv`, or if the specified file does not exist, the program should instead exit 
via sys.exit.
"""
# read the csv file and draw the table
def read_csv_file(file_name):
    try:
        with open(file_name, "r") as csvfile:
            # read the csv file to an dictionary
            reader = csv.DictReader(csvfile)
            # create the table using the dictionary
            reader_tabulate = tabulate(reader, headers="keys", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")

    return reader_tabulate

# Program logic
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not ".csv" in sys.argv[1]:
        sys.exit("Not a CSV file")

    table = read_csv_file(sys.argv[1])
    print(table)

main()
