#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


# BaseGeometry class
class BaseGeometry:
    """Represent a Base Geometry class"""

    # area method (not implemented)
    def area(self):
        """Calculate the area of the geometric object.
        This method is not implemented in the BaseGeometry class,
        so it raises an Exception."""
        raise Exception("area() is not implemented")

    # integer_validator method
    def integer_validator(self, name, value):
        """Validate that the value passed in is an integer and greater than 0.

        Args:
        name (str): The name of the value being validated.
        value (int): The value being validated.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
