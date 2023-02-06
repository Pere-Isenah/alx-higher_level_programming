#!/usr/bin/python3

"""
This function checks if the object is an instance of a class
or a subclass of the specified class.
"""


def inherits_from(obj, a_class):

    """
Check if an object is an instance of a class or subclass
of the specified class.

Args:
    obj (object): The object to be checked.
    a_class (class): The class to be checked against.

Returns:
    bool: True if the object is an instance of a class or a subclass
    of the specified class, otherwise False.
"""

    return issubclass(type(obj), a_class)
