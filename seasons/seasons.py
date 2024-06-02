from datetime import date
import inflect
import sys


def main():
    birthdate = time(input("Date of Birth: "))
    today = date.today()

    min_passed = d_to_m(today - birthdate)

    p = inflect.engine()
    print(f"{p.number_to_words(min_passed, andword=" ").capitalize()} minutes")


def time(time):
    try:
        year, month, day = time.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        time = date(year, month, day)
    except ValueError:
        sys.exit("correct format: YYYY-MM-DD")
    else:
        return time


def d_to_m(days):
    days = days.days
    return days * 24 * 60


if __name__ == "__main__":
    main()
