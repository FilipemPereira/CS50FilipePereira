import re

"""
Implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding 
str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and 
that there will be a space before each. Assume that these times are representative of actual times, not necessarily 
9:00 AM and 5:00 PM specifically.
"""

# put the hour number in the 24 format
def to_24_format(h, time_period):
    if time_period == "AM" and h == "12":
        h = "00"
    elif time_period == "PM":
        match h:
            case "01":
                h = "13"
            case "02":
                h = "14"
            case "03":
                h = "15"
            case "04":
                h = "16"
            case "05":
                h = "17"
            case "06":
                h = "18"
            case "07":
                h = "19"
            case "08":
                h = "20"
            case "09":
                h = "21"
            case "10":
                h = "22"
            case "11":
                h = "23"
            case "12":
                h = "12"
            case _:
                h = ""
    return h

# Convert one time
def timeConversion(t):
    time_period = t.split(" ")[1]
    new_t = t.replace(time_period, "").replace(" ", "")

    if ":" not in t:
        h = new_t
        m = "00"
    else:
        h, m = new_t.split(":")

    new_h = to_24_format(h.zfill(2), time_period)

    return f"{new_h}:{m.zfill(2)}"

# verify if times are well formatted
def valid(t1,t2):
    t1_time_period = t1.split(" ")[1]
    t2_time_period = t2.split(" ")[1]

    new_t1 = t1.replace(t1_time_period, "")
    new_t2 = t2.replace(t2_time_period, "")

    if ":" not in t1:
        h = int(new_t1)
        valid_t1_numbers =  0 <= h <= 12
    else:
        h1, m1 = map(int, new_t1.split(":"))
        valid_t1_numbers = (0 <= h1 <= 12 and 0 <= m1 <= 59)

    if ":" not in t2:
        h = int(new_t2)
        valid_t2_numbers =  0 <= h <= 12
    else:
        h2, m2 = map(int, new_t2.split(":"))
        valid_t2_numbers = (0 <= h2 <= 12 and 0 <= m2 <= 59)


    # validate hours
    valid_numbers = valid_t1_numbers and valid_t2_numbers

    # validate first AM second PM ou first PM and second AM
    valid_time_period = (t1_time_period == "AM" and t2_time_period == "PM") or (t1_time_period == "PM" and t2_time_period == "AM")

    # verify if this is a period of 8 hours
    return valid_numbers and valid_time_period

def convert(hours):
    pattern = r"^(\d{1,2}|\d{1,2}:\d{1,2}) (AM|PM) to (\d{1,2}|\d{1,2}:\d{1,2}) (AM|PM)$"
    matches = re.match(pattern, hours, re.ASCII)

    if matches:
        t1 = matches.group(1) + " " + matches.group(2)
        t2 = matches.group(3) + " " + matches.group(4)

        if valid(t1, t2):
            #convert to 24 format
            format_24 = f"{timeConversion(t1)} to {timeConversion(t2)}"
        else:
            raise ValueError
    else:
        raise ValueError
    return format_24

def main():
    print(convert(input("Hours: ")))

if __name__ == "__main__":
    main()
