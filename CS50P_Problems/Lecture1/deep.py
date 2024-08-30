"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user
inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""

def TheGreatQuestion(answer) -> str: 
    check = str()
    if answer ==  "42" or answer.lower() == "forty two" or answer.lower() == "forty-two":
        check = "Yes"
    else:
        check = "No"
    return check

def main():
    answer = input("What is the Great Question of Life, the Universe and Everything?").rstrip().lstrip()
    print(TheGreatQuestion(answer))

main()
    
