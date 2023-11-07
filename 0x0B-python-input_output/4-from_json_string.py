#!/usr/bin/python3

"""Define a function"""


def from_json_string(my_str):
    """
    Args:
        my_str (str): The JSON string.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    import json
    return json.loads(my_str)
