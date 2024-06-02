cost = 50

while True:
    print("Amount Due:", cost)
    change = int(input("Insert coin: "))
    if change == 25 or change == 10 or change == 5:
        cost = cost - change
        if cost <= 0:
            print("Change Owed:", (-1 * cost))
            break
