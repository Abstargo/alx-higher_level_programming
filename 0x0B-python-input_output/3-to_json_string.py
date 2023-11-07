#!/usr/bin/python3

"""Define a function"""


def to_json_string(my_obj):
    """
    Args:
        my_obj: The object to be converted to JSON.
    Returns:
        str: The JSON representation of the object.
    """
    import json
    return json.dumps(my_obj)
