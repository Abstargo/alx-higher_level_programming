#!/usr/bin/python3

"""Define a function"""


def inheritss_from(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, False
              otherwise.
    """
    return issubclass(type(obj), a_class)
