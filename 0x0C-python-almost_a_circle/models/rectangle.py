#!/usr/bin/python3
# models/rectangle.py

""" Import the base class from the models/base.py file"""
from models.base import Base

""" Class definition for the Rectangle class
 that inherits from the Base class"""


class Rectangle(Base):

    """ Initializer method that sets the instance variables of the rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Call the parent class' initializer to set the id attribute"""
        super().__init__(id)

        """ Set the width, height, x, and y attributes for the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Property for the height attribute,
      returns the value stored in __height"""
    @property
    def height(self):
        return self.__height

    """ Property for the width attribute,
      returns the value stored in __width"""
    @property
    def width(self):
        return self.__width

    """ Setter method for the width attribute, raises an error
      if the value is not an integer or less than or equal to 0"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ Setter method for the height attribute, raises an error
    if the value is not an integer or less than or equal to 0"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """Property for the x attribute, returns the value stored in __x"""
    @property
    def x(self):
        return self.__x

    """ Setter method for the x attribute, raises an error
      if the value is not an integer or less than 0"""
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """ Property for the y attribute, returns the value stored in __y"""
    @property
    def y(self):
        return self.__y

    """ Setter method for the y attribute, raises an error
    if the value is not an integer or less than 0"""
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """Method that calculates and returns the area of the rectangle"""
    def area(self):
        return self.height * self.width

    """Method that displays the rectangle to the console"""
    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            """This method returns the string representation
              of the rectangle object"""
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ This method returns the string representation
          of the rectangle object"""

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ This method updates the attributes of the rectangle object"""
        if args:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This method returns a dictionary representation
          of the rectangle object"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
