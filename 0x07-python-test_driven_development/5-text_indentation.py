#!/usr/bin/python3
"""
Program that return a text with a newline
"""


def text_indentation(text):
    """ prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    new_lines = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must be a string")
    # Remove the space after special char
    idx = 0
    for i in text:
        if i in new_lines:
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1
    # Jump after the special char
    idx = 0
    for i in text:
        if i in new_lines:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1
    print(text, end='')
