#!/usr/bin/python3

output = []

for digit1 in range(0, 9):
    for digit2 in range(digit1 + 1, 10):
        output.append("{:02d}".format(digit1 * 10 + digit2))

print(", ".join(output))