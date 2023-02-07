#!/usr/bin/python3
"""A fuction that write to file"""


def write_file(filename="", text=""):
        """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'w') as file:
        return file.write(text)  
