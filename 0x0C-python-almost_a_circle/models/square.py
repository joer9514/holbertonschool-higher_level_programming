#!/usr/bin/python3
"""Module Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id,
            self.x,
            self.y,
            self.size,
        )

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes using variadic args"""
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            valid_args = args[:4]
            args_list = ['id', 'size', 'x', 'y']
            for index in range(len(valid_args)):
                setattr(self, args_list[index], valid_args[index])

    def to_dictionary(self):
        """Returns a dictionary representation"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
