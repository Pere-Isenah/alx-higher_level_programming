#!/usr/bin/python3
# models/square.py
import json
from models.rectangle import Rectangle

"""Defines a class Square that inherits from Rectangle."""


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    """
        if args:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set the size of the square.

    Args:
        value (int): The new size of the square.
    """
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
