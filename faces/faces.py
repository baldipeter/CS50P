def main():
    answer = input("What's your input? ")
    answer = convert(answer)
    print(answer)

def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

main()
