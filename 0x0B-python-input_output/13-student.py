#!/usr/bin/python3
"""
class Student that defines a student
"""


class Student:
    """
    defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Dictionary retrieving
        """
        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            tmp = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
                if i in self.__dict__.keys():
                    tmp[i] = self.__dict__[i]
            return tmp

    def reload_from_json(self, json):
        """
        Replace with json's
        """
        for items in json.keys():
            self.__dict__[items] = json[items]
