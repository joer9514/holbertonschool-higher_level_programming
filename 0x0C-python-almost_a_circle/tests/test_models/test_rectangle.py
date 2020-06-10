#!/usr/bin/python3
import unittest
import contextlib
import io
import os
import pep8
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def setUp(self):
        if os.path.isfile('Rectangle.json'):
            os.remove('Rectangle.json')
        if os.path.isfile('Rectangle.csv'):
            os.remove('Rectangle.csv')

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_rectangle_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_rectangle_noargs(self):
        self.assertRaises(TypeError, Rectangle)

    def test_rectangle_one_arg(self):
        self.assertRaises(TypeError, Rectangle, 1)

    def test_rectangle_instance(self):
        obj = Rectangle(1, 1)
        self.assertIsInstance(obj, Rectangle)

    def test_rectangle_inherits_base(self):
        obj = Rectangle(1, 1)
        self.assertIsInstance(obj, Base)

    def test_rectangle_required_attrs_exists(self):
        obj = Rectangle(3, 4)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, '_Rectangle__width'))
        self.assertTrue(hasattr(obj, '_Rectangle__height'))
        self.assertTrue(hasattr(obj, '_Rectangle__x'))
        self.assertTrue(hasattr(obj, '_Rectangle__y'))

    def test_rectangle_getters_setters(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.width = 10
        obj.height = 20
        obj.x = 5
        obj.y = 6
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 20)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 6)

    def test_rectangle_defaults(self):
        obj = Rectangle(1, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_rectangle_type_validation(self):
        with self.assertRaises(TypeError) as context:
            obj = Rectangle('a', 2)
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj = Rectangle(2, {})
        self.assertIn('height must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj = Rectangle(1, 1, {'a': 1})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj = Rectangle(1, 1, 4, [31])
        self.assertIn('y must be an integer', str(context.exception))

    def test_rectangle_value_validation(self):
        with self.assertRaises(ValueError) as context:
            obj = Rectangle(0, 1)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(-20, 1)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, 0)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, -69)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, 1, -30)
        self.assertIn('x must be >= 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, 1, 1, -80)
        self.assertIn('y must be >= 0', str(context.exception))

    def test_rectangle_area_method(self):
        obj = Rectangle(1, 1)
        self.assertEqual(obj.area(), 1)

        obj = Rectangle(2, 2)
        self.assertEqual(obj.area(), 4)

        obj = Rectangle(123456789, 987654321)
        self.assertEqual(obj.area(), 121932631112635269)

        obj = Rectangle(0xCACA, 0xB0BA)
        self.assertEqual(obj.area(), 2348693188)

        obj = Rectangle(0b01010101010101001, 0b1010000111001001001)
        self.assertEqual(obj.area(), 14475782193)

        obj = Rectangle(0o3542157, 0o775422315)
        self.assertEqual(obj.area(), 129269575248099)

    def test_rectangle_display_without_xy(self):
        out = []
        stdout_data = [io.StringIO() for i in range(6)]
        rectangles = [Rectangle(1, 1),
                      Rectangle(1, 2),
                      Rectangle(2, 1),
                      Rectangle(2, 2),
                      Rectangle(4, 4),
                      Rectangle(4, 6)]
        target = ['#\n',
                  '#\n#\n',
                  '##\n',
                  '##\n##\n',
                  '####\n####\n####\n####\n',
                  '####\n####\n####\n####\n####\n####\n']
        for i in range(6):
            with contextlib.redirect_stdout(stdout_data[i]):
                rectangles[i].display()
            out.append(stdout_data[i].getvalue())
        self.assertListEqual(out, target)

    def test_rectangle_display_str(self):
        out = []
        stdout_data = [io.StringIO() for i in range(7)]
        rectangles = [Rectangle(1, 2, 3, 4),
                      Rectangle(4, 3, 2, 1),
                      Rectangle(1, 1),
                      Rectangle(2, 2, id=666),
                      Rectangle(4, 5, 6, 7, 999),
                      Rectangle(4, 6, 9),
                      Rectangle(9, 8, y=7)]
        target = ['[Rectangle] (1) 3/4 - 1/2\n',
                  '[Rectangle] (2) 2/1 - 4/3\n',
                  '[Rectangle] (3) 0/0 - 1/1\n',
                  '[Rectangle] (666) 0/0 - 2/2\n',
                  '[Rectangle] (999) 6/7 - 4/5\n',
                  '[Rectangle] (4) 9/0 - 4/6\n',
                  '[Rectangle] (5) 0/7 - 9/8\n']
        for i in range(7):
            with contextlib.redirect_stdout(stdout_data[i]):
                print(rectangles[i])
            out.append(stdout_data[i].getvalue())
        self.assertListEqual(out, target)

    def test_rectangle_display_with_xy(self):
        out = []
        stdout_data = [io.StringIO() for i in range(6)]
        rectangles = [Rectangle(1, 1, 2, 2),
                      Rectangle(1, 2, 2, 3),
                      Rectangle(2, 1, 7, 2),
                      Rectangle(2, 3, 2, 2),
                      Rectangle(4, 4, 1, 1),
                      Rectangle(3, 2, 1, 0)]
        target = ['\n\n  #\n',
                  '\n\n\n  #\n  #\n',
                  '\n\n       ##\n',
                  '\n\n  ##\n  ##\n  ##\n',
                  '\n ####\n ####\n ####\n ####\n',
                  ' ###\n ###\n']
        for i in range(6):
            with contextlib.redirect_stdout(stdout_data[i]):
                rectangles[i].display()
            out.append(stdout_data[i].getvalue())
        self.assertListEqual(out, target)

    def test_rectangle_update_valid_args(self):
        obj = Rectangle(1, 1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(111)
        self.assertEqual(obj.id, 111)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(12, 2)
        self.assertEqual(obj.id, 12)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(13, 14, 15)
        self.assertEqual(obj.id, 13)
        self.assertEqual(obj.width, 14)
        self.assertEqual(obj.height, 15)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(100, 200, 300, 400)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.width, 200)
        self.assertEqual(obj.height, 300)
        self.assertEqual(obj.x, 400)
        self.assertEqual(obj.y, 0)
        obj.update(10, 20, 30, 40, 50)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 20)
        self.assertEqual(obj.height, 30)
        self.assertEqual(obj.x, 40)
        self.assertEqual(obj.y, 50)
        obj.update(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)

    def test_rectangle_update_args_type_validation(self):
        obj = Rectangle(1, 1)

        with self.assertRaises(TypeError) as context:
            obj.update(1, 'b')
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(1, 2, {})
        self.assertIn('height must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(1, 1, 1, {'a': 1})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(1, 1, 1, 4, [31])
        self.assertIn('y must be an integer', str(context.exception))

    def test_rectangle_update_args_value_validation(self):
        obj = Rectangle(1, 1)

        with self.assertRaises(ValueError) as context:
            obj.update(1, 0)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(1, -20, 1)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(1, 1, 0)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(1, 1, -69)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(1, 1, 1, -30)
        self.assertIn('x must be >= 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(1, 1, 1, 1, -80)
        self.assertIn('y must be >= 0', str(context.exception))

    def test_rectangle_update_valid_kwargs(self):
        obj = Rectangle(1, 1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(id=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(width=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(height=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(x=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 0)
        obj.update(y=2)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 2)
        obj.update(id=1, width=1, height=1, x=1, y=1)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 1)
        self.assertEqual(obj.y, 1)
        obj.update(y=98, x=98, height=98, width=98, id=98)
        self.assertEqual(obj.id, 98)
        self.assertEqual(obj.width, 98)
        self.assertEqual(obj.height, 98)
        self.assertEqual(obj.x, 98)
        self.assertEqual(obj.y, 98)
        obj.update(y=99, x=99, width=99, id=99)
        self.assertEqual(obj.id, 99)
        self.assertEqual(obj.width, 99)
        self.assertEqual(obj.height, 98)
        self.assertEqual(obj.x, 99)
        self.assertEqual(obj.y, 99)
        obj.update(x=100, width=100, id=100)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.width, 100)
        self.assertEqual(obj.height, 98)
        self.assertEqual(obj.x, 100)
        self.assertEqual(obj.y, 99)
        obj.update(x=101, width=101)
        self.assertEqual(obj.id, 100)
        self.assertEqual(obj.width, 101)
        self.assertEqual(obj.height, 98)
        self.assertEqual(obj.x, 101)
        self.assertEqual(obj.y, 99)

    def test_rectangle_update_skip_kwargs(self):
        obj = Rectangle(1, 1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, id=4)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, id=13, width=14)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, 5, id=13, width=14, height=15)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 5)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, 5, 6, id=13, width=14, height=15, x=16)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 5)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 0)
        obj.update(3, 4, 5, 6, 7, id=13, width=14, height=15, x=16, y=17)
        self.assertEqual(obj.id, 3)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 5)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 7)

    def test_rectangle_update_invalid_kwargs(self):
        obj = Rectangle(1, 1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

        with self.assertRaises(TypeError) as context:
            obj.update(width='b')
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(height={})
        self.assertIn('height must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(x={'a': 1})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj.update(y=[31])
        self.assertIn('y must be an integer', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(width=0)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(width=-20)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(height=0)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(height=-69)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(x=-30)
        self.assertIn('x must be >= 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj.update(y=-80)
        self.assertIn('y must be >= 0', str(context.exception))

    def test_rectangle_to_dictionary(self):
        obj = Rectangle(1, 1)
        target = {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(obj.to_dictionary(), target)
        obj.update(3, 4, 5, 6, 7)
        target = {'id': 3, 'width': 4, 'height': 5, 'x': 6, 'y': 7}
        self.assertDictEqual(obj.to_dictionary(), target)

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(list_rectangles_input, list_rectangles_output)

    def test_rectangle_save_csv(self):
        file_exists = False
        r1 = Rectangle(2, 3, 4, 5, 6)
        r2 = Rectangle(3, 3, 3, 3, 3)
        r3 = Rectangle(9, 8, 7, 6, 5)
        rect_lst = [r1, r2, r3]
        Rectangle.save_to_file_csv(rect_lst)
        if os.path.isfile('Rectangle.csv'):
            file_exists = True
        self.assertTrue(file_exists)
        out = Rectangle.load_from_file_csv()
        for i in range(len(out)):
            self.assertEqual(rect_lst[i].id, out[i].id)
            self.assertEqual(rect_lst[i].width, out[i].width)
            self.assertEqual(rect_lst[i].height, out[i].height)
            self.assertEqual(rect_lst[i].x, out[i].x)
            self.assertEqual(rect_lst[i].y, out[i].y)

    def test_rectangle_save_empty_csv_file(self):
        Rectangle.save_to_file_csv([])
        out = Rectangle.load_from_file_csv()
        self.assertEqual(out, [])

    def test_rectangle_load_empty_csv_file(self):
        out = Rectangle.load_from_file_csv()
        self.assertListEqual(out, [])