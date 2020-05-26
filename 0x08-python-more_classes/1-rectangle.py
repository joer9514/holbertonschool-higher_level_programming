#!/usr/bin/python3
"""Creates a rectangle class that defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle weight and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width.
        check if value is an int an if value < 0
        """
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height
        check if value is an int an if value < 0
        """
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
