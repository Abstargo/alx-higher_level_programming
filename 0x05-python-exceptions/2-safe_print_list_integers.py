#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Write a function that prints the first x elements of a list"""
    printed = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                printed += 1
        print()
        return (printed)
    except (TypeError):
        print()
        return (printed)
