#!/usr/bin/python3
"""
class save to json file
"""
import json


def save_to_json_file(my_obj, filename):
    """fuction open sys"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
