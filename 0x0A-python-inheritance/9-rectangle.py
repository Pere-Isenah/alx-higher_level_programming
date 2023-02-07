#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle object"""

    def __init__(self, width, height):
        """Initializes a Rectangle object"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return "[Rectangle] {:d} / {:d}".format(self.__width, self.__height)

    def area(self):
        """calculate and return the area of rectangle"""
        return self.__height * self.__width
