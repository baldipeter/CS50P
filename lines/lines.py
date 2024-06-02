import sys

if len(sys.argv) != 2:
    sys.exit("Too few or too many command-line arguments.")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Invalid command-line arguments.")

lines = []
code_lines = 0

try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File not found")

for line in lines:
    if line.isspace() == True:
        pass
    elif line.strip().startswith("#"):
        pass
    else:
        code_lines += 1

print(code_lines)
