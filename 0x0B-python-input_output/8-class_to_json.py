#!/usr/bin/python3

"""Define a funcion"""


def class_to_json(obj):
    """
    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representing the object in a serializable format.
    """
    return obj.__dict__
