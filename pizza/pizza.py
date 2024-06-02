import csv
from tabulate import tabulate
import sys

if len(sys.argv) != 2:
    sys.exit("Too few or too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Invalid file")

table = []

try:
    with open(sys.argv[1]) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            table.append(row)
except FileNotFoundError:
    sys.exit("File not found")

print(tabulate(table, headers="firstrow", tablefmt="grid"))
