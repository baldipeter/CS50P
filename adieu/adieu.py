import inflect

p = inflect.engine()

def main():
    # Prompt for names, handle EOFError
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    # Print all names
    names = p.join(names)
    print("Adieu, adieu, to", names)

if __name__ == "__main__":
    main()
