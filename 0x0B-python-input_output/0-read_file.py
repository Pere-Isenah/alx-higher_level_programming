#!/usr/bin/python3
"""A fuction that reads a file and print to stdout"""


def read_file(filename=""):
    """"Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read())
