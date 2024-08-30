"""
The U.S. Food & Drug Administration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw 
in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the 
relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of 
calories in one portion of that fruit, per the FDA's poster for fruits, which is also available as text. Capitalization aside, assume that users will 
input exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn't a fruit.
"""

def calories(fruit):
    match fruit.lower():
        case "apple":
            calories = 130
        case "banana":
            calories = 110
        case "pear" | "sweet cherries":
            calories = 100
        case "kiwifruit":
            calories = 90
        case "orange"| "watermelon":
            calories = 80
        case "plums":
            calories = 70
        case "grapefruit" | "nectarine" | "peach":
            calories = 60 
        case "avocado" | "cantaloupe" | "honeydew melon" | "pineapple" | "strawberries" | "tangerine":
            calories = 50  
        case "lime":
            calories = 20
        case "lemon":
            calories = 15
        case _:
            return "Error! Fruit not found"
    return calories

def main():
    fruit = input("Item: ")
    print("Calories: ", calories(fruit))

main()
        
        