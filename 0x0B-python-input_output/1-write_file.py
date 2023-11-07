#!/usr/bin/python3

"""Define a function"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters
    writes.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='UTF-8') as file:
        return (file.write(text))
