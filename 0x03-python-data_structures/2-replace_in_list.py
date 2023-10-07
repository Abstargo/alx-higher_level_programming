#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """A function that replaces an element of a list at a specific positon (like in C)"""

    if idx < 0 or idx >= len(my_list):
        return (my_list)
    my_list[idx] = element
    return (my_list)