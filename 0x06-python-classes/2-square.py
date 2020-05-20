#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Square class with a construction method"""

    def __init__(self, size=0):
        """Initialize Square with size attribute"""

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
