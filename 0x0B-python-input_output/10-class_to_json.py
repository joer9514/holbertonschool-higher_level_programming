#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """
    My class module
    """

    def __init__(self, name):
        self.name = name
        self.number = 0
    """
    My class module
    """

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
