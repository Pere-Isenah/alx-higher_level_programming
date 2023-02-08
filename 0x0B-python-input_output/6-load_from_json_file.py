#!/usr/bin/python3

import json


def load_from_json_file(filename):
    """Write an object to a text file using JSON representation."""
    return json.loads(filename)
