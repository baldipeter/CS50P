def main():
    day_time = input("What time is it? ")
    meal = convert(day_time)
    if 7.0 <= meal <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal <= 13.0:
        print("lunch time")
    elif 18.0 <= meal <= 19.0:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    # Support for 12-hour format
    try:
        minute, meridiem = minute.split(" ")
        hour = float(hour)
        minute = float(minute) / 60
        if meridiem == "a.m.":
            return hour + minute
        elif meridiem == "p.m.":
            return hour + minute + 12
    # If not 12 your format was used
    except ValueError:
        hour = float(hour)
        minute = float(minute) / 60
        return hour + minute

if __name__ == "__main__":
    main()
