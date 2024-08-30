from pyfiglet import Figlet
from random import choice
import sys

def main():
    figlet = Figlet()
    if len(sys.argv) == 2 or len(sys.argv) == 3 and (sys.argv[1] not in ["-f","--font"] or sys.argv[2] not in figlet.getFonts()):
        print("Invalid usage")
        sys.exit(1)
        
    string = input("Input: ")
    if len(sys.argv) == 1:
        figlet.setFont(font=choice(figlet.getFonts()))
        print("Output: ")
        print(figlet.renderText(string))
    elif len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
        print("Output:")
        print(figlet.renderText(string))

main()

