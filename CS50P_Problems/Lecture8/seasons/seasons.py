import sys
import inflect
import re
from datetime import date

"""
Implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old 
they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from 
'Rent', without any and between words.
"""


def check_dob_string(dob_string):
    if re.match(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", dob_string):
        dob_list = dob_string.split("-")
        year, month, day = map(int, dob_list)
        return year, month, day
    else:
        raise ValueError

def calculate_total_minutes(dob_string: str):
    try:
        year, month, day = check_dob_string(dob_string)
    except ValueError:
        sys.exit("Invalid date")

    date_of_birth = date(year, month, day)
    today_date = date.today()

    age = today_date - date_of_birth
    age_minutes = age.days * 60 * 24

    p = inflect.engine()
    words_to_numbers = p.number_to_words(age_minutes, andword="")
    desired_output = words_to_numbers.capitalize() + " minutes"

    return desired_output

def main():
    dob_string = input("Date Of Birth: ")
    desired_output = calculate_total_minutes(dob_string)
    print(desired_output)


if __name__ == "__main__":
    main()