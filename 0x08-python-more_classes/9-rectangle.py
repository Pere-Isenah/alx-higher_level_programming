#!/usr/bin/python3

class Rectangle():

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._rectangle__width = value

    @property
    def height(self):
        return self._rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._rectangle__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return self.height * 2 + self.width * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rect = []
        for i in range(self.height):
            rect.append("#" * self.width)
        return "\n".join(rect)

    def __repr__(self):
        return f"Rectangle({self.width!r},{self.height!r})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        new_list = []
        for i in range(self.height):
            new_list.append(str(self.print_symbol) * self.width)
        return "\n".join(new_list)

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
