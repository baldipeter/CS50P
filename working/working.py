import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Group important parts
    time = re.search(
        r"^([0-9]{1,2}):?([0-9]{2})? ([APM]{2}) to ([0-9]{1,2}):?([0-9]{2})? ([APM]{2})$",
        s,
    )

    if time == None:
        raise ValueError

    # Check if hour is correct

    first = int(time.group(1))
    last = int(time.group(4))

    if first < 1 or 12 < first or last < 1 or 12 < last:
        raise ValueError

    # Check for ante meridiem or post meridiem
    if time.group(3) == "PM" and first != 12:
        first = first + 12
    elif time.group(3) == "AM" and first == 12:
        first = 0
    if time.group(6) == "PM" and last != 12:
        last = last + 12
    elif time.group(6) == "AM" and last == 12:
        last = 0

    # Check if minute is correct/there
    if time.group(2) != None:
        first_min = int(time.group(2))
    else:
        first_min = 0

    if time.group(5) != None:
        last_min = int(time.group(5))
    else:
        last_min = 0

    if first_min < 0 or 60 <= first_min or last_min < 0 or 60 <= last_min:
        raise ValueError

    return f"{first:02}:{first_min:02} to {last:02}:{last_min:02}"


if __name__ == "__main__":
    main()
