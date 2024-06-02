def main():
    n = int(input("m: "))
    einstein(n)


def einstein(m):
    c = 300000000
    E = m * (c ** 2)
    print(E)

main()
