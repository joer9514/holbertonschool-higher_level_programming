#!/usr/bin/python3
"""
    Module containing loopup function
"""


def lookup(obj):
    """ Returns all available attributes and methods of an object
    Args:
        obj: An object
    Returns: A list of all available attribues and methods.
    """
    return dir(obj)
