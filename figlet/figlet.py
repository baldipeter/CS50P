from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()
    list_of_fonts = figlet.getFonts()

    # Check if cmd line arg is correct and get font
    font = font_check(list_of_fonts)

    txt = input("Input: ")
    figlet.setFont(font=font)
    print("Output: ")
    print(figlet.renderText(txt))


def font_check(fonts):
    if len(sys.argv) == 1:
        f = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        f = sys.argv[2]
        if f not in fonts:
            sys.exit("Invalid font")
    else:
        sys.exit("Invalid command-line arguments")
    return f

if __name__ == "__main__":
    main()
