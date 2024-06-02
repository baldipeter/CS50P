def main():
    while True:
        fuel = input("Fraction: ")
        try:
            percent = convert(fuel)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            print(gauge(percent))
            break


def convert(fraction):
    x, y = fraction.split("/")
    if y == "0":
        raise ZeroDivisionError
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError
    else:
        fraction = round(x / y * 100)
        if fraction > 100 or fraction < 0:
            raise ValueError
        return fraction


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
