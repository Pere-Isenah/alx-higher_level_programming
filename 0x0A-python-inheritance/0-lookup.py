#!/usr/bin/python3
"""define a lookup function"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return dir(obj)
