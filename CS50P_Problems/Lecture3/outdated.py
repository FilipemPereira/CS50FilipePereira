"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad 
design. Dates in that format can't be easily sorted because the date's year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, 
and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 
9/8/1636 could also be interpreted as August 9, 1636!

Implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month
in the latter might be any of the values in the list with the months' names
"""

# Months' list
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Convert some month to the corresponding number in the year
def convert(month):
    match month:
        case "January":
            n = 1
        case "February":
            n = 2
        case "March":
            n = 3
        case "April":
            n = 4
        case "May":
            n = 5
        case "June":
            n = 6
        case "July":
            n = 7
        case "August":
            n = 8
        case "September":
            n = 9
        case "October":
            n = 10
        case "November":
            n = 11
        case "December":
            n = 12
        case _:
            n = 0
    return n


# Add zeroes if the number has length 1
def leadingZeroes(number: str) -> str:
    if 0 < len(number) < 2:
        return number.zfill(2)
    else:
        return number


# Verify is the date is valid
def isValid(date):
    # Expects n1n1/n2n2/n3n3n3n3
    if "/" in date:
        month, day, year = map(str, date.split("/"))
        if month in months:
            return False
        return 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and len(year) == 4

    if " " in date and ',' in date:
        month, day, year = map(str, date.split(" "))
        n, s = map(str, day.split(","))
        return month in months and 1 <= int(n) <= 31 and len(year) == 4

# Optimize the formatted date
def optimalDate(validDate):
    if "/" in validDate:
        month, day, year = map(str, validDate.split("/"))
        return year + "-" + leadingZeroes(month) + "-" + leadingZeroes(day)

    if " " in validDate:
        month, day, year = map(str, validDate.split(" "))
        n, s = map(str, day.split(","))
        return year + "-" + leadingZeroes(str(convert(month))) + "-" + leadingZeroes(n)

# Program logic
def main():
    while True:
        date = input("Date: ").title().rstrip().lstrip()
        if isValid(date):
            print(optimalDate(date))
            break


main()
