#!/usr/bin/python3
"""
Class load from json file
"""
import json


def load_from_json_file(filename):
    """function open"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
