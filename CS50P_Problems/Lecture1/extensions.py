"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file's media type if the file's name
ends, case-insensitively, in any of these suffixes:

images - gif, jpg, jpeg, png
application - pdf, zip
text/plain - txt
"""

# match equivalent to switch in c and other c based languages

# find(<substring>) - return the index where occur the first occurrence of the substring

def extension(fileName) -> any:
    fileName = fileName.lower()
    if '.' in fileName:
            i = fileName.find(".")
            extension = fileName[i + 1:]
    else:
         extension = " "
    if '.' in extension:
        p1, p2 = map(str, extension.split('.'))
        match p2:
            case "gif" | "png":
                print(f"image/{p2}")
            case "jpg" | "jpeg":
                print("image/jpeg")
            case "pdf" | "zip":
                print(f"application/{p2}")
            case "txt":
                print("text/plain")
            case _:
                print("application/octet-stream")
    else:
        match extension:
            case "gif" | "png":
                print(f"image/{extension}")
            case "jpg" | "jpeg":
                print("image/jpeg")
            case "pdf" | "zip":
                print(f"application/{extension}")
            case "txt":
                print("text/plain")
            case _:
                print("application/octet-stream")

def main():
    fileName = input("File name:").rstrip().lstrip()
    extension(fileName)

main()