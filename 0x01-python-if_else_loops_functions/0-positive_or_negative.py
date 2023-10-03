#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive", end="\n")
elif number == 0:
    print(f"{number} is zero", end="\n")
elif number < 0:
    print(f"{number} is negative", end="\n")