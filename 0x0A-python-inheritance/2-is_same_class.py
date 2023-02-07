#!/usr/bin/python3
"""Has a function to check object instance"""


def is_same_class(obj, a_class):
    """
Check if the object is an instance of the same class.
Args:
    obj (object): The object to check.
    a_class (type): The class to compare against.

Returns:
    bool: True if the object is an instance of the same class, False otherwise.
"""
    return type(obj) is a_class
