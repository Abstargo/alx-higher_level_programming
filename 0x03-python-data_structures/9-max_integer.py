#!/usr/bin/python3

def max_integer(my_list=[]):
    """A function that finds the biggest integer of a list"""

    if len(my_list) == 0:
        return (None)
    
    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return (big)
