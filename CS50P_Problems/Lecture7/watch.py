import re

"""
Implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that's the value of a 
src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. Expect 
that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes.
And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, 
return None.
"""

# Convert a embed link back to shorter, sharable url
def parse(s):
    # map until the end of the src value
    matches = re.search("<iframe[^>]*src=\"(http://|https://|https://www.)(youtube.com.*?)\"", s)

    if matches:
        if matches[1] == "http://":
            protocol = "https://"
            url = protocol + matches[2]
        else:
            url = matches[1] + matches[2]

        url1 = url.replace("www.", "").replace("youtube.com", "youtu.be").replace("/embed", "")

        return url1

    else:
        return None

# Main function
def main():
    print(parse(input("HTML: ")))

main()
