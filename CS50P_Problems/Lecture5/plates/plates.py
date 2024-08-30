from string import punctuation

"""
Redefine the plates.py program with the following structure  
"""

# Verify the middle of the string
def verify_middle(plate):
    if plate.isalpha():
        return True
    
    for c in plate:
        if c.isdigit():
            i = plate.find(c)
            break
    return plate[i:].isdigit() and plate[i:][0] != '0'


# Verify if the plate have punctuation or white spaces
def have_punctuation(string):
    for s in string:
        if s in [' ', punctuation]:
            return True
    return False

# Verify if all conditions are satisfied
def is_valid(plate):
    return plate[:2].isalpha() and 2 <= len(plate) <= 6 and verify_middle(plate) and not have_punctuation(plate)

# Program logic
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
