#!/usr/bin/python3
"""
    Module containing MyList class
"""


class MyList(list):
    """The class extends functionality from the `list` class.
    """

    def print_sorted(self):
        """Prints a list (of integers) in ascending order
        """
        print(sorted(self))
