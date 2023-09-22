#!/usr/bin/python3
# test_rectangle.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines unittests for models/rectangle.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""


def setUp(self):
    self.r1 = Rectangle(10, 2)
    self.r2 = Rectangle(2, 10)


def test_rectangle_is_base(self):
    self.assertIsInstance(self.r1, Base)


def test_no_args(self):
    with self.assertRaises(TypeError):
        Rectangle()


def test_one_arg(self):
    with self.assertRaises(TypeError):
        Rectangle(1)


def test_two_args(self):
    self.assertEqual(self.r1.id, self.r2.id - 1)


def test_three_args(self):
    r1 = Rectangle(2, 2, 4)
    r2 = Rectangle(4, 4, 2)
    self.assertEqual(r1.id, r2.id - 1)


def test_four_args(self):
    r1 = Rectangle(1, 2, 3, 4)
    r2 = Rectangle(4, 3, 2, 1)
    self.assertEqual(r1.id, r2.id - 1)


def test_five_args(self):
    self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)


def test_more_than_five_args(self):
    with self.assertRaises(TypeError):
        Rectangle(1, 2, 3, 4, 5, 6)


def test_width_private(self):
    with self.assertRaises(AttributeError):
        print(self.r1.__width)


def test_height_private(self):
    with self.assertRaises(AttributeError):
        print(self.r1.__height)


def test_x_private(self):
    with self.assertRaises(AttributeError):
        print(self.r1.__x)


def test_y_private(self):
    with self.assertRaises(AttributeError):
        print(self.r1.__y)


def test_width_getter(self):
    r = Rectangle(5, 7, 7, 5, 1)
    self.assertEqual(5, r.width)


def test_width_setter(self):
    r = Rectangle(5, 7, 7, 5, 1)
    r.width = 10
    self.assertEqual(10, r.width)


def test_height_getter(self):
    r = Rectangle(5, 7, 7, 5, 1)
    self.assertEqual(7, r.height)


def test_height_setter(self):
    r = Rectangle(5, 7, 7, 5, 1)
    r.height = 10
    self.assertEqual(10, r.height)


def test_x_getter(self):
    r = Rectangle(5, 7, 7, 5, 1)
    self.assertEqual(7, r.x)


def test_x_setter(self):
    r = Rectangle(5, 7, 7, 5, 1)
    r.x = 10
    self.assertEqual(10, r.x)


def test_y_getter(self):
    r = Rectangle(5, 7, 7, 5, 1)
    self.assertEqual(5, r.y)


def test_y_setter(self):
    r = Rectangle(5, 7, 7, 5, 1)
    r.y = 10
    self.assertEqual(10, r.y)


class TestRectangleWidth(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""


def test_none_width(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Rectangle(None, 2)


def test_str_width(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Rectangle("invalid", 2)


def test_float_width(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Rectangle(5.5, 1)


def test_complex_width(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Rectangle(complex(5), 2)


def test_dict_width(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Rectangle({"a": 1, "b": 2}, 2)


def test_bool_width(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Rectangle(True, 2)


def test_list_width(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Rectangle([1, 2, 3], 2)


def test_set_width(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Rectangle({1, 2, 3}, 2)


def test_tuple_width(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Rectangle((1, 2, 3), 2)


def test_negative_width(self):
    with self.assertRaisesRegex(ValueError, "width must be > 0"):
        Rectangle(-5, 1)


def test_zero_width(self):
    with self.assertRaisesRegex(ValueError, "width must be > 0"):
        Rectangle(0, 1)


class TestRectangleHeight(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""


def test_none_height(self):
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        Rectangle(2, None)


def test_str_height(self):
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        Rectangle(2, "invalid")


def test_float_height(self):
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        Rectangle(1, 5.5)


def test_complex_height(self):
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        Rectangle(2, complex(5))


def test_dict_height(self):
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        Rectangle(2, {"a": 1, "b": 2})


def test_bool_height(self):
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        Rectangle(2, True)


def test_list_height(self):
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        Rectangle(2, [1, 2, 3])


def test_set_height(self):
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        Rectangle(2, {1, 2, 3})


def test_tuple_height(self):
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        Rectangle(2, (1, 2, 3))


def test_negative_height(self):
    with self.assertRaisesRegex(ValueError, "height must be > 0"):
        Rectangle(1, -5)


def test_zero_height(self):
    with self.assertRaisesRegex(ValueError, "height must be > 0"):
        Rectangle(1, 0)


class TestRectangleX(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""


def test_none_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Rectangle(2, 3, None, 1)


def test_str_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Rectangle(2, 3, "invalid", 1)


def test_float_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Rectangle(2, 3, 5.5, 1)


def test_complex_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Rectangle(2, 3, complex(5), 1)


def test_dict_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Rectangle(2, 3, {"a": 1, "b": 2}, 1)


def test_bool_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Rectangle(2, 3, True, 1)


def test_list_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Rectangle(2, 3, [1, 2, 3], 1)


def test_set_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Rectangle(2, 3, {1, 2, 3}, 1)


def test_tuple_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Rectangle(2, 3, (1, 2, 3), 1)


def test_negative_x(self):
    with self.assertRaisesRegex(ValueError, "x must be >= 0"):
        Rectangle(2, 3, -5, 1)


class TestRectangleY(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""


def test_none_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Rectangle(2, 3, 1, None)


def test_str_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Rectangle(2, 3, 1, "invalid")


def test_float_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Rectangle(2, 3, 1, 5.5)


def test_complex_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Rectangle(2, 3, 1, complex(5))


def test_dict_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Rectangle(2, 3, 1, {"a": 1, "b": 2})


def test_bool_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Rectangle(2, 3, 1, True)


def test_list_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Rectangle(2, 3, 1, [1, 2, 3])


def test_set_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Rectangle(2, 3, 1, {1, 2, 3})


def test_tuple_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Rectangle(2, 3, 1, (1, 2, 3))


def test_negative_y(self):
    with self.assertRaisesRegex(ValueError, "y must be >= 0"):
        Rectangle(2, 3, 1, -5)


class TestRectangleArea(unittest.TestCase):
    """Unittests for testing the area() method of the Rectangle class."""


def test_area_valid(self):
    r = Rectangle(3, 4)
    self.assertEqual(r.area(), 12)


def test_area_zero(self):
    r = Rectangle(0, 5)
    self.assertEqual(r.area(), 0)


def test_area_negative(self):
    r = Rectangle(-2, 7)
    self.assertEqual(r.area(), 0)


class TestRectangleStr(unittest.TestCase):
    """Unittests for testing the __str__() method of the Rectangle class."""


def test_str_default(self):
    r = Rectangle(4, 6, 2, 1, 12)
    self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")


def test_str_no_args(self):
    r = Rectangle(2, 2)
    self.assertEqual(r.__str__(), "[Rectangle] (1) 0/0 - 2/2")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Unittests for testing the update() method of the Rectangle class with
    *args.
    """


def test_update_valid_args(self):
    r = Rectangle(3, 4)
    r.update(5, 6, 7, 8)
    self.assertEqual(r.__str__(), "[Rectangle] (5) 0/0 - 6/7")


def test_update_no_args(self):
    r = Rectangle(3, 4)
    r.update()
    self.assertEqual(r.__str__(), "[Rectangle] (1) 0/0 - 3/4")


def test_update_one_arg(self):
    r = Rectangle(3, 4)
    r.update(5)
    self.assertEqual(r.__str__(), "[Rectangle] (5) 0/0 - 3/4")


def test_update_two_args(self):
    r = Rectangle(3, 4)
    r.update(5, 6)
    self.assertEqual(r.__str__(), "[Rectangle] (5) 0/0 - 6/4")


def test_update_three_args(self):
    r = Rectangle(3, 4)
    r.update(5, 6, 7)
    self.assertEqual(r.__str__(), "[Rectangle] (5) 0/0 - 6/7")


def test_update_four_args(self):
    r = Rectangle(3, 4)
    r.update(5, 6, 7, 8)
    self.assertEqual(r.__str__(), "[Rectangle] (5) 0/0 - 6/7")


def test_update_five_args(self):
    r = Rectangle(3, 4)
    r.update(5, 6, 7, 8, 9)
    self.assertEqual(r.__str__(), "[Rectangle] (5) 7/8 - 6/7")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Unittests for testing the update() method of the Rectangle class with
    **kwargs.
    """


def test_update_valid_kwargs(self):
    r = Rectangle(3, 4)
    r.update(width=6, height=7, x=8, y=9, id=5)
    self.assertEqual(r.__str__(), "[Rectangle] (5) 8/9 - 6/7")


def test_update_invalid_kwargs(self):
    r = Rectangle(3, 4)
    r.update(invalid=6, nonsense=7)
    self.assertEqual(r.__str__(), "[Rectangle] (1) 0/0 - 3/4")


if __name__ == '__main__':
    unittest.main()
