#!/usr/bin/python3
"""Has a function to check object instance"""


def is_kind_of_class(obj, a_class):
    """
This function checks if an object is an instance of
a specified class or any of its subclasses
Args:
    obj (object): The object to be checked.
    a_class (class): The class to be checked against.

    Returns:
    bool: True if the object is an instance of a_class or its subclass,
     False otherwise
"""
    return isinstance(obj, a_class)
