import random
"""
I'm thinking of a number between 1 and 100… ! Implement a programa that radom a number between 1 and n randomly. 

If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.

"""


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError
            break
        except ValueError:
            print("", end="")

    number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1 or guess > level:
                raise ValueError
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("", end="")


main()
