#!/usr/bin/python3

"""Define a function"""


def lookup(obj):
    """
    Returns a list of avaible attributes and methods
    of an object.
    Args:
        obj: The object to inspect.
    Returns:
        list: A list containing the names of attributes
        and methods of the object.
    """
    return dir(obj)
