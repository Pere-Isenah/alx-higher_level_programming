#!/usr/bin/python3
# 1-my_list.py
"""Define a class MyList that inherits from the built-in list class"""


class MyList(list):
    """subclas olistf a """
    def __init__(self):
        """ Initialize the class and call the superclass's constructor"""
        super().__init__()

    def print_sorted(self):
        """ Method to print the list sorted"""
        print(sorted(self))
