import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if src := re.search(r'src="https?://(?:w{3}\.)?youtube.com/embed/(\w*)"', s):
        return f"https://youtu.be/{src.group(1)}"
    else:
        return src


if __name__ == "__main__":
    main()
