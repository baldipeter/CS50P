def main():
    formula = input("Expression: ")
    x, y, z = formula.split(" ")
    x = int(x)
    z = int(z)
    interpret(x, y, z)

def interpret(n, char, m):
    match char:
        case "+":
            print(float(n + m))
        case "-":
            print(float(n - m))
        case "*":
            print(float(n * m))
        case "/":
            print(float(n / m))


main()
