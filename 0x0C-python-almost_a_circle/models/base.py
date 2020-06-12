#!/usr/bin/python3
"""Module contains Base class"""
import json
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts dictionary representation to JSON"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Loads a JSON string"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a instance by a given dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Base":
            dummy = cls()
            return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a JSON string to a file"""
        list_dicts = []
        with open('{}.json'.format(cls.__name__), mode="w+") as file:
            if not list_objs:
                file.write("[]")
            else:
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                file.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Loads a JSON string from a file"""
        objs = []
        try:
            f = open('{}.json'.format(cls.__name__), 'r')
            content = f.read()
            items = cls.from_json_string(content)
            for item in items:
                objs.append(cls.create(**item))
            f.close()
            return objs
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects into a CSV"""
        lines = []
        row = []
        for obj in list_objs:
            obj_dict = obj.to_dictionary()
            if cls.__name__ == 'Rectangle':
                row = [obj_dict['id'],
                       obj_dict['width'],
                       obj_dict['height'],
                       obj_dict['x'],
                       obj_dict['y']]
            elif cls.__name__ == 'Square':
                row = [obj_dict['id'],
                       obj_dict['size'],
                       obj_dict['x'],
                       obj_dict['y']]
            lines.append(row)
        with open('{}.csv'.format(cls.__name__), 'w+') as file:
            writer = csv.writer(file)
            for line in lines:
                writer.writerow(line)

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV"""
        answer = []
        try:
            csv_file = open('{}.csv'.format(cls.__name__), 'r')
            reader = csv.reader(csv_file)
            for line in reader:
                if cls.__name__ == 'Rectangle':
                    obj = cls(int(line[1]),
                              int(line[2]),
                              int(line[3]),
                              int(line[4]),
                              int(line[0]))
                elif cls.__name__ == 'Square':
                    obj = cls(int(line[1]),
                              int(line[2]),
                              int(line[3]),
                              int(line[0]))
                answer.append(obj)
            csv_file.close()
            return answer
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw using a turtle like the ol times"""
        def turtle_draw_rect(tur, w, h, x, y):
            tur.penup()
            tur.forward(x)
            tur.right(90)
            tur.forward(y)
            tur.left(90)
            tur.pendown()
            tur.forward(w)
            tur.right(90)
            tur.forward(h)
            tur.right(90)
            tur.forward(w)
            tur.right(90)
            tur.forward(h)
            tur.penup()
            tur.home()

        tortu = turtle.Turtle()
        for rect in list_rectangles:
            turtle_draw_rect(tortu, rect.width, rect.height, rect.x, rect.y)
        for sq in list_squares:
            turtle_draw_rect(tortu, sq.size, sq.size, sq.x, sq.y)
