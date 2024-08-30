"""
Implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d.
After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign and formatted to 
two decimal places. Treat the user's input case insensitively.
"""

# Dictionary of items
items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Program logic
def main():
    sum = 0.0
    while True:
        try:
            item = input("Item: ")
            sum += items[item.title()]
            print(f"${sum:.2f}")
        except KeyboardInterrupt:
            break
        except EOFError:
            break
        except KeyError:
            continue

main()
