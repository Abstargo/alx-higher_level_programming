#!/usr/bin/python3

if __name__ == "__main__":
    # First difining the variables a and b

    """ Second thing is to import the function from the 
    other file called calculator_1.py """
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    #Last thing is to print the results using the format function by an (:d) integer
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
