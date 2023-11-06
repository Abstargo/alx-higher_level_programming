#!/usr/bin/python3

"""Define a function"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly is an instance

    Args:
        obj: The objects to check
        a_class: The class to check against

    Returns:
        bool: True if obj is an instance of a_class, False otherwise
    """
    return type(obj) == a_class
