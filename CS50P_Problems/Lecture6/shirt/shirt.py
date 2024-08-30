import sys
import os
from PIL import Image
from PIL import ImageOps

"""
Implement a program that expects exactly two command-line arguments: the name or path of a image file to read and another 
name or path of an image to save.
Then the program should overlay shirt.png (which has a transparent background) on the input after resizing and cropping 
the input to be the same size, saving the result as its output.
The program should exit if: 
if the user does not specify exactly two command-line arguments;
if the input and output is not an image;
if the input's name does not have the same extension as the output's name;
if the specified input does not exist.

Use the Pillow library. 
"""

# Read the input image and process it with the Pillow library
def read_image(input_img):
    try:
        with Image.open(input_img) as img:
            with Image.open("shirt.png") as shirt_img:
                size = shirt_img.size
                # Resize input image to fit shirt
                new_img = ImageOps.fit(img, size)
                # Past shirt in input image
                new_img.paste(shirt_img, mask = shirt_img)
                # Create an output file with the new image
                new_img.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Invalid input")

# Verify if the extensions of the both files are equals and if the extension corresponds to an image extension (jpg, jpeg, png)
def check_file_extensions(input_image, output_image):
    extension1 = os.path.splitext(input_image)
    extension2 = os.path.splitext(output_image)

    if extension1[1].lower() != extension2[1].lower():
        sys.exit("Input and output have different extensions")
    elif extension1[1].lower() not in [".png", ".jpg", ".jpeg"]:
        sys.exit("Invalid input")
    elif extension2[1].lower() not in [".png", ".jpg", ".jpeg"]:
        sys.exit("Invalid output")

# Program logic
def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")

    check_file_extensions(sys.argv[1], sys.argv[2])
    read_image(sys.argv[1])

main()
