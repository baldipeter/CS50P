import csv
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Too few or too many command-line arguments")
    before = sys.argv[1]
    after = sys.argv[2]
    defence(before, after)
    name_list = open_file(before)
    separated_names = separator(name_list)
    write_file(after, separated_names)


def defence(b, a):
    # Correct command-line
    if b.endswith(".csv") == False and a.endswith(".csv") == False:
        sys.exit("Invalid files")


def open_file(before_file):
    # Read file into list
    list = []
    try:
        with open(before_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                list.append({"name": row[0], "house": row[1]})
    except FileNotFoundError:
        sys.exit("File not found")
    else:
        return list


def separator(lista):
    # Separate names
    new_lista = []
    for line in lista[1:]:
        last, first = line["name"].split(", ")
        new_lista.append({"first": first, "last": last, "house": line["house"]})
    return new_lista


def write_file(file_name, new_list):
    # Write new file
    with open(file_name, "w", newline="\n") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for line in new_list:
            writer.writerow(
                {"first": line["first"], "last": line["last"], "house": line["house"]}
            )
    sys.exit(0)


if __name__ == "__main__":
    main()
