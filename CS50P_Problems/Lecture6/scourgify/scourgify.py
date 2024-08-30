import sys
import csv

"""
Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into 
one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space. 
Implement a program that:
Expects the user to provide two command-line arguments, 
    the name of an existing CSV file to read as input (whose columns are assumed to be, in order, name and house);
    the name of a new CSV to write as output, whose columns should be, in order, first, last, and house;
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will 
have both a first name and last name
"""

# write the new file with in the correct format
def write_new_file(reader, new_file):
    with open(new_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for r in reader:
            last, first = r["name"].split(",")
            house = r["house"]
            writer.writerow({"first": first.lstrip(), "last": last, "house": house})

# read the csv file
def process_csv_file(file_name):
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            write_new_file(reader, sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


# Program logic
def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    
    process_csv_file(sys.argv[1])

main()