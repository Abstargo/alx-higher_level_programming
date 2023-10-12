#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Write a function that adds all unique integers in a list"""

    unique_set = set(my_list)
    return sum(unique_set)
