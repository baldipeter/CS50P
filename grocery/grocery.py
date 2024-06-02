groceries = []
while True:
    try:
        item = input().upper()
        groceries.append(item)
    except EOFError:
        groceries.sort()
        while groceries:
            for i in groceries:
                print(groceries.count(i), i)
                del groceries[0:groceries.count(i)]
        break
