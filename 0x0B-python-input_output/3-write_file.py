#!/usr/bin/python3
"""
Module that writes a string
"""


def write_file(filename="", text=""):
    """Write a text"""
    writer = 0
    with open(filename, mode='w', encoding='UTF-8') as file:
        writer = file.write(text)
        return writer
