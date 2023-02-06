#!/usr/bin/python3
#from 7-base_geometry import BaseGeometry

class BaseGeometry:
    pass
    
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value,int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseException):
    def __init__(self, width, height):
       BaseException.integer_validator(self,width,height)