from random import randint

# Get num
while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level > 0:
            break
        else:
            pass

# random int
solution = randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            pass
    except ValueError:
        pass
    else:
        if guess < solution:
            print("Too small!")
        elif guess > solution:
            print("Too large!")
        else:
            print("Just right!")
            break
