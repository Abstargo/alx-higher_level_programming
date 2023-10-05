#!/usr/bin/python3
# First difining the variables a and b
a = 10
b = 5

""" Second thing is to import the function from the 
other file called calculator_1.py """
from calculator_1 import add, sub, mul, div

# Next, we store the functions values into different variables
result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

#Last thing is to print the results using the format function by an (:d) integer
print("{} + {} = {}".format(a, b, result_add))
print("{} - {} = {}".format(a, b, result_sub))
print("{} * {} = {}".format(a, b, result_mul))
print("{} / {} = {}".format(a, b, result_div))
