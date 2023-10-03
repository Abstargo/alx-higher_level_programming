#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


Last_di = number % 10

if Last_di > 5:
    print(f"Last digit of {number} is {Last_di} and is greater than 5")
elif Last_di == 0:
    print(f"Last digit of {number} is {Last_di} and is 0")
elif Last_di < 6:
    print(f"Last digit of {number} is {Last_di} and is less than 6 and not 0")
