def main():
    answer = input("Input: ").strip()
    nswr = shorten(answer)
    print(nswr)

def shorten(word):
    vovels = ["A", "E", "I", "O", "U"]
    twttr = ""
    for c in word:
        if c.upper() not in vovels:
            twttr += c
    return twttr

if __name__ == "__main__":
    main()
