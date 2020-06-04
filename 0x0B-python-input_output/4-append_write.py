#!/usr/bin/python3
"""
Module for function that append strings
"""


def append_write(filename="", text=""):
    """Append a text"""
    a = 0
    with open(filename, mode='a', encoding='UTF-8') as file:
        a = file.write(text)
        return a
