def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) < 2 or len(s) > 6:
        return False

    # “All vanity plates must start with at least two letters.”
    if s[0].isnumeric() == True or s[1].isnumeric() == True:
        return False

    # “Numbers cannot be used in the middle of a plate; they must come at the end.
    # The first number used cannot be a ‘0’.”

    # Find first number
    for c in s:
        if c.isnumeric() == True:
            _, second, third = s.partition(c)

            # The first number used cannot be a ‘0’.
            if second == "0":
                return False

            # Check the remainder for letters
            for k in third:
                if k.isnumeric() == False:
                    return False
            break


    # “No periods, spaces, or punctuation marks are allowed.”
    return False if (s.isalnum() == False) else True


if __name__ == "__main__":
    main()
