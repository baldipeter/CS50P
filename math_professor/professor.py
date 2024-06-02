import random


def main():
    lvl = get_level()
    problems = generate_integer(lvl)
    counter, points = 0, 0

    # Iterates over the problems, pops the solved ones
    while problems:
        try:
            answer = int(input(f"{problems[0][0]} + {problems[0][1]} = "))
        except ValueError:
            print("EEE")
            counter += 1
        else:
            if answer == problems[0][2]:
                points += 1
                problems.pop(0)
                counter = 0
            else:
                print("EEE")
                counter += 1

        if counter == 3:
            print(f"{problems[0][0]} + {problems[0][1]} = {problems[0][2]}")
            problems.pop(0)
            counter = 0

    # When all problems has been pop'd, prints the score
    print("Score:", points)

# Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if n in [1, 2, 3]:
                return n


# Randomly generates ten math problems formatted as X + Y = ,  X and Y is a non-negative integer with n digits.
def generate_integer(level):
    # Gets the min - max digit number
    if level == 1:
        a, b = 0, 9
    else:
        a = 10 ** (level - 1)
        b = (10 ** level) - 1

    # Lists the math problems
    problemset = []
    for _ in range(10):
        x, y = random.randint(a, b), random.randint(a, b)
        z = x + y
        list = [x, y, z]
        problemset.append(list)
    return problemset

if __name__ == "__main__":
    main()
