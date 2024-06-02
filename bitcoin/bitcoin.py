import requests
import sys

def main():
    # Make sure command-line is in order
    number = defense()

    # Get the value of a bitcoin and print it correctly
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Request error!")
    else:
        r = r.json()
        try:
            r = r["bpi"]["USD"]["rate"].replace(",", "")
            bitcoin = float(r) * number
        except ValueError:
            print("possibly the JSON format changed")
        else:
            print(f"${bitcoin:,.4f}")


def defense():
    if len(sys.argv) != 2:
        sys.exit("Correct input: bitcoin.py number_of_bitcoins")

    try:
        num = float(sys.argv[1])
    except ValueError:
        sys.exit("Correct input: bitcoin.py float(number_of_bitcoins)")
    else:
        return num

if __name__ == "__main__":
    main()
