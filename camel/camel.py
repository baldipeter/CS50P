name = input("camelCase: ")

if name.islower():
    print("snake_case:", name)
else:
    for i in range(len(name)):
        if name[i].isupper() == True:
            #print(name[i])
            first, second, third = name.partition(name[i])
            name = first + "_" + second.lower() + third
print(name)
