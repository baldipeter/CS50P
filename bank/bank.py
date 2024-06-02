def main():
    greet = input("Greeting: ")
    money = value(greet)
    print(f"${money}")


def value(greeting):
    greeting = greeting.strip().capitalize()
    if greeting.find("Hello") == 0:
        return 0
    elif greeting.find("H") == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
