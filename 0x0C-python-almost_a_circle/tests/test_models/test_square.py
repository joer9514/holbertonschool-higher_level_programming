#!/usr/bin/python3
import unittest
import contextlib
import io
import os
import pep8
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        if os.path.isfile('Square.json'):
            os.remove('Square.json')
        if os.path.isfile('Square.csv'):
            os.remove('Square.csv')

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_rectangle_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/square.py'])
        self.assertEqual(result.total_errors, 0)

    def test_square_instance(self):
        obj = Square(1)
        self.assertIsInstance(obj, Square)

    def test_square_inherits_rectangle(self):
        obj = Square(1)
        self.assertIsInstance(obj, Rectangle)

    def test_square_noargs(self):
        self.assertRaises(TypeError, Square)

    def test_square_required_attrs_exists(self):
        obj = Square(1)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'width'))
        self.assertTrue(hasattr(obj, 'height'))
        self.assertTrue(hasattr(obj, 'size'))
        self.assertTrue(hasattr(obj, 'x'))
        self.assertTrue(hasattr(obj, 'y'))

    def test_square_getters_setters(self):
        obj = Square(1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.size = 4
        obj.x = 5
        obj.y = 6
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 6)

    def test_square_defaults(self):
        obj = Square(1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_square_update_valid_args(self):
        obj = Square(1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(111)
        self.assertEqual(obj.id, 111)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(12, 2)
        self.assertEqual(obj.id, 12)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(13, 14, 15)
        self.assertEqual(obj.id, 13)
        self.assertEqual(obj.size, 14)
        self.assertEqual(obj.x, 15)
        self.assertEqual(obj.y, 0)
        obj.update(100, 200, 300, 400)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.size, 200)
        self.assertEqual(obj.x, 300)
        self.assertEqual(obj.y, 400)
        obj.update(10, 20, 30, 40, 50)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.size, 20)
        self.assertEqual(obj.x, 30)
        self.assertEqual(obj.y, 40)
        obj.update(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_rectangle_update_args_type_validation(self):
        obj = Square(1)

        with self.assertRaises(TypeError) as context:
            obj.update(1, 'b')
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(1, 2, {})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(1, 1, 1, {'a': 1})
        self.assertIn('y must be an integer', str(context.exception))

    def test_square_display(self):
        out = []
        stdout_data = [io.StringIO() for i in range(6)]
        squares = [Square(1),
                   Square(1, 2),
                   Square(2, 2, 2),
                   Square(3, 3, 3, 3),
                   Square(4, 4),
                   Square(4, 6, 2, 3)]
        target = ['#\n',
                  '  #\n',
                  '\n\n  ##\n  ##\n',
                  '\n\n\n   ###\n   ###\n   ###\n',
                  '    ####\n    ####\n    ####\n    ####\n',
                  '\n\n      ####\n      ####\n      ####\n      ####\n']
        for i in range(6):
            with contextlib.redirect_stdout(stdout_data[i]):
                squares[i].display()
            out.append(stdout_data[i].getvalue())
        self.assertListEqual(out, target)

    def test_square_display_str(self):
        out = []
        stdout_data = [io.StringIO() for i in range(7)]
        squares = [Square(1, 2, 3, 4),
                   Square(4, 3, 2, 1),
                   Square(1, 1),
                   Square(2, 2, id=666),
                   Square(4, 5, 6, 999),
                   Square(4, 6, 9),
                   Square(9, 8, y=7)]
        target = ['[Square] (4) 2/3 - 1\n',
                  '[Square] (1) 3/2 - 4\n',
                  '[Square] (1) 1/0 - 1\n',
                  '[Square] (666) 2/0 - 2\n',
                  '[Square] (999) 5/6 - 4\n',
                  '[Square] (2) 6/9 - 4\n',
                  '[Square] (3) 8/7 - 9\n']
        for i in range(7):
            with contextlib.redirect_stdout(stdout_data[i]):
                print(squares[i])
            out.append(stdout_data[i].getvalue())
        self.assertListEqual(out, target)

    def test_square_update_valid_kwargs(self):
        obj = Square(1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(id=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(size=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(x=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 0)
        obj.update(y=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 2)
        obj.update(id=1, size=1, x=1, y=1)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 1)
        self.assertEqual(obj.y, 1)
        obj.update(y=98, x=98, size=98, id=98)
        self.assertEqual(obj.id, 98)
        self.assertEqual(obj.size, 98)
        self.assertEqual(obj.x, 98)
        self.assertEqual(obj.y, 98)
        obj.update(y=99, x=99, width=99, id=99)
        self.assertEqual(obj.id, 99)
        self.assertEqual(obj.size, 99)
        self.assertEqual(obj.x, 99)
        self.assertEqual(obj.y, 99)
        obj.update(x=100, size=100, id=100)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.size, 100)
        self.assertEqual(obj.x, 100)
        self.assertEqual(obj.y, 99)
        obj.update(x=101, size=101)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.size, 101)
        self.assertEqual(obj.x, 101)
        self.assertEqual(obj.y, 99)

    def test_rectangle_update_invalid_kwargs(self):
        obj = Square(1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

        with self.assertRaises(TypeError) as context:
            obj.update(size='3')
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(x={'a': 1})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(y=[31])
        self.assertIn('y must be an integer', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(size=0)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(size=-20)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(x=-30)
        self.assertIn('x must be >= 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(y=-80)
        self.assertIn('y must be >= 0', str(context.exception))

    def test_rectangle_update_skip_kwargs(self):
        obj = Square(1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, id=4)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, id=13, size=14)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, 5, id=13, size=14, x=15)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, 5, 6, id=13, size=14, x=15, y=16)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 6)
        obj.update(3, 4, 5, 6, 7, id=13, width=14, height=15, x=16, y=17)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 6)

    def test_square_to_dictionary(self):
        obj = Square(1)
        target = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(obj.to_dictionary(), target)
        obj.update(3, 4, 5, 6)
        target = {'id': 3, 'size': 4, 'x': 5, 'y': 6}
        self.assertDictEqual(obj.to_dictionary(), target)

    def test_square_load_from_file(self):
        s1 = Square(6)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertNotEqual(list_squares_input, list_squares_output)

    def test_square_save_csv(self):
        file_exists = False
        s1 = Square(2, 3, 4, 5)
        s2 = Square(3, 3, 3, 3)
        s3 = Square(9, 8, 7, 6)
        sq_lst = [s1, s2, s3]
        Square.save_to_file_csv(sq_lst)
        if os.path.isfile('Square.csv'):
            file_exists = True
        self.assertTrue(file_exists)
        out = Square.load_from_file_csv()
        for i in range(len(out)):
            self.assertEqual(sq_lst[i].id, out[i].id)
            self.assertEqual(sq_lst[i].size, out[i].size)
            self.assertEqual(sq_lst[i].x, out[i].x)
            self.assertEqual(sq_lst[i].y, out[i].y)

    def test_square_save_empty_csv_file(self):
        Square.save_to_file_csv([])
        out = Square.load_from_file_csv()
        self.assertEqual(out, [])

    def test_square_load_empty_csv_file(self):
        out = Square.load_from_file_csv()
        self.assertListEqual(out, [])