import sys
from PIL import Image, ImageOps
import os.path


def main():
    before, after = defense()
    image, shirt = get_images(before)
    image = fit_images(image, shirt)
    image.save(after)


# Check for CMD-line args, and file extension
def defense():
    if len(sys.argv) != 3:
        sys.exit("Too few or too many command-line arguments.")

    be = sys.argv[1]
    af = sys.argv[2]
    list_of_types = [".jpg", ".jpeg", ".png"]

    if os.path.splitext(be)[-1] not in list_of_types:
        print(os.path.splitroot(before)[2])
        sys.exit("Invalid before file extension.")
    elif os.path.splitext(af)[-1] not in list_of_types:
        sys.exit("Invalid after file extension.")
    elif os.path.splitext(be)[-1] != os.path.splitext(af)[-1]:
        sys.exit("Different file extensions.")
    else:
        return be, af


# Tries to get the images
def get_images(input):
    try:
        im = Image.open(input)
        sh = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("File not found")
    else:
        return im, sh


# Resizes the before image and pastes the shirt
def fit_images(im, sh):
    im = ImageOps.fit(im, sh.size)
    im.paste(sh, sh)
    return im


if __name__ == "__main__":
    main()
