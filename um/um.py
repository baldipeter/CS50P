import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Find all 'um's
    if ums := re.findall(r"([a-z]*um[a-z]*)", s, re.IGNORECASE):
        # Make it case insensitive, source for the pythonic way:
        # https://stackoverflow.com/questions/59383120/converting-a-list-to-lowercase-in-python
        ums_lower = [word.lower() for word in ums]
        return ums_lower.count("um")

    else:
        return 0


if __name__ == "__main__":
    main()
