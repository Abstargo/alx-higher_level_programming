#!/usr/bin/puthon3
for char in range (ord('a'), ord('z')+1):
    if chr(char) != 'q' and chr(char) != 'e':
        print(chr(char), end="")
