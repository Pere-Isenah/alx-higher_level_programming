#!/usr/bin/python3
""" a function that returns an object (Python data structure)
represented by a JSON string:"""
import json


def from_json_string(my_str):
    """"
    Return the object representation of  JSON string.
    arg:
    my_str: object
    """
    return json.loads(my_str)

