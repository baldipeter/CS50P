import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    nums = re.search(r"^([0-9]{0,3})\.([0-9]{0,3})\.([0-9]{0,3})\.([0-9]{0,3})$", ip)
    if nums == None:
        return False
    for group in nums.groups():
        if 0 > int(group) or int(group) > 255:
            return False
    return True


if __name__ == "__main__":
    main()
