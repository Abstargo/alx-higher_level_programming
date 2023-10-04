#!/usr/bin/python3

output = ""

for digit1 in range(0, 9):
    for digit2 in range(digit1 + 1, 10):
        output += "{:02d}".format(digit1 * 10 + digit2)
        if digit1 != 8 or digit2 != 9:
            output += ", "

print(output)
