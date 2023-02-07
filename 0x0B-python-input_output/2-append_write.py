#!/usr/bin/python3
"""a function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'a') as file:
        return file.write(text)
