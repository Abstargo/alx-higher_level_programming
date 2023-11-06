#!/usr/bin/python3

"""Define a function"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to check against.
    Retuns:
        bool: True if obj is an instance of a_class or its subclasses,
        False otherwise.
    """
    return isinstance(obj, a_class)
