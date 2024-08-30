import random

"""
Implement a program that simulates a little professor.
The program should:
Prompts the user for a level, n. if the user does not input 1, 2, or 3, the program should prompt again;
Randomly generates 10 math problems formatted as 'X + Y = ', wherein each of X and Y is a non-negative integer with n digits. 
Only support addition;
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output 'EEE' 
and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly 
after three tries, the program should output the correct answer;
The program should ultimately output the user's score: the number of correct answers out of 10.
"""

# Ask level to the user
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
               break
        except:
            continue
    return level


# Generate integers according to the level
def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    elif level == 3:
        n = random.randint(100, 999)
    return n

# Program logic
def main():
    score = 0
    level = get_level()
    # 10 questions
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        # 3 tries
        for i in range(3):
            try:
                res = int(input(f"{x} + {y} = "))
                if res == result:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                if i != 2:
                    print("EEE")
                else:
                    print(f"{x} + {y} = {result}")
    # Print the user's score
    print("Score: " + str(score))


main()