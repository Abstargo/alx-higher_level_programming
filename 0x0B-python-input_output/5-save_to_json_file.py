#!/usr/bin/python3

"""Define a function"""


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: The object to be serialized and saved to a file.
        filename (str): The name of the file to save.

    Returns:
        None
    """
    import json
    with open(filename, mode="w", encoding='utf-8') as file:
        json.dump(my_obj, file)
