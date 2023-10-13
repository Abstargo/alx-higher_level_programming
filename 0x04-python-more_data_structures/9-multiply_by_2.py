#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Write a function that returns a new dictionary"""

    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return (new_dict)
