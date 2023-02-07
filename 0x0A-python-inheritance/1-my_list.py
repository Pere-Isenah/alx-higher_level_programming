#!/usr/bin/python3
n = []

"""Define a class MyList that inherits from the built-in list class"""


class MyList(list):
    """ Initialize the class and call the superclass's constructor"""
    def __init__(self):
        super().__init__(n)

    """ Method to print the list sorted"""
    def print_sorted(self):
        print(sorted(self))
