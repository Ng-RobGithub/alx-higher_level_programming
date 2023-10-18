#!/usr/bin/python3
# test_square.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines unittests for models/square.py."""

import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""


def test_is_base(self):
    self.assertIsInstance(Square(10), Base)


def test_is_square(self):
    self.assertIsInstance(Square(10), Square)


def test_no_args(self):
    with self.assertRaises(TypeError):
        Square()


def test_one_arg(self):
    s1 = Square(10)
    s2 = Square(11)
    self.assertEqual(s1.id, s2.id - 1)


def test_two_args(self):
    s1 = Square(10, 2)
    s2 = Square(2, 10)
    self.assertEqual(s1.id, s2.id - 1)


def test_three_args(self):
    s1 = Square(10, 2, 2)
    s2 = Square(2, 2, 10)
    self.assertEqual(s1.id, s2.id - 1)


def test_four_args(self):
    self.assertEqual(7, Square(10, 2, 2, 7).id)


def test_more_than_four_args(self):
    with self.assertRaises(TypeError):
        Square(1, 2, 3, 4, 5)


def test_size_private(self):
    with self.assertRaises(AttributeError):
        print(Square(10, 2, 3, 4).__size)


def test_size_getter(self):
    self.assertEqual(5, Square(5, 2, 3, 9).size)


def test_size_setter(self):
    s = Square(4, 1, 9, 2)
    s.size = 8
    self.assertEqual(8, s.size)


def test_width_getter(self):
    s = Square(4, 1, 9, 2)
    s.size = 8
    self.assertEqual(8, s.width)


def test_height_getter(self):
    s = Square(4, 1, 9, 2)
    s.size = 8
    self.assertEqual(8, s.height)


def test_x_getter(self):
    self.assertEqual(0, Square(10).x)


def test_y_getter(self):
    self.assertEqual(0, Square(10).y)


class TestSquareSize(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""


def test_none_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(None)


def test_str_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square("invalid")


def test_float_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(5.5)


def test_complex_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(complex(5))


def test_dict_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square({"a": 1, "b": 2}, 2)


def test_bool_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(True, 2, 3)


def test_list_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square([1, 2, 3])


def test_set_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square({1, 2, 3}, 2)


def test_tuple_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square((1, 2, 3), 2, 3)


def test_frozenset_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(frozenset({1, 2, 3, 1}))


def test_range_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(range(5))


def test_bytes_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(b'Python')


def test_bytearray_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(bytearray(b'abcdefg'))


def test_memoryview_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(memoryview(b'abcdefg'))


def test_inf_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(float('inf'))


def test_nan_size(self):
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        Square(float('nan'))


# Test size values
def test_negative_size(self):
    with self.assertRaisesRegex(ValueError, "width must be > 0"):
        Square(-1, 2)


def test_zero_size(self):
    with self.assertRaisesRegex(ValueError, "width must be > 0"):
        Square(0, 2)


class TestSquareX(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""


def test_none_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, None)


def test_str_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, "invalid")


def test_float_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, 5.5)


def test_complex_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, complex(5))


def test_dict_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, {"a": 1, "b": 2}, 2)


def test_bool_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, True)


def test_list_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, [1, 2, 3])


def test_set_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, {1, 2, 3})


def test_tuple_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, (1, 2, 3))


def test_frozenset_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, frozenset({1, 2, 3, 1}))


def test_range_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, range(5))


def test_bytes_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, b'Python')


def test_bytearray_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, bytearray(b'abcdefg'))


def test_memoryview_x(self):
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        Square(1, memoryview(b'abcdefg'))


class TestSquareY(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""


def test_none_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, None)


def test_str_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, "invalid")


def test_float_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, 5.5)


def test_complex_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, complex(5))


def test_dict_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, {"a": 1, "b": 2})


def test_bool_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, True)


def test_list_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, [1, 2, 3])


def test_set_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, {1, 2, 3})


def test_tuple_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, (1, 2, 3))


def test_frozenset_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, frozenset({1, 2, 3, 1}))


def test_range_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, range(5))


def test_bytes_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, b'Python')


def test_bytearray_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, bytearray(b'abcdefg'))


def test_memoryview_y(self):
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        Square(1, 2, memoryview(b'abcdefg'))


class TestSquareUpdateArgs(unittest.TestCase):
    """Unittests for testing the update method of the Square class with args.
    """


def test_update_no_args(self):
    s = Square(1)
    s.update()
    self.assertEqual(str(s), "[Square] (1) 0/0 - 1")


def test_update_one_arg(self):
    s = Square(1)
    s.update(2)
    self.assertEqual(str(s), "[Square] (2) 0/0 - 1")


def test_update_two_args(self):
    s = Square(1)
    s.update(2, 3)
    self.assertEqual(str(s), "[Square] (2) 0/0 - 3")


def test_update_three_args(self):
    s = Square(1)
    s.update(2, 3, 4)
    self.assertEqual(str(s), "[Square] (2) 4/0 - 3")


def test_update_four_args(self):
    s = Square(1)
    s.update(2, 3, 4, 5)
    self.assertEqual(str(s), "[Square] (2) 4/5 - 3")


def test_update_five_args(self):
    s = Square(1)
    s.update(2, 3, 4, 5, 6)
    self.assertEqual(str(s), "[Square] (2) 4/5 - 3")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittests for testing the update method of the Square class with
    kwargs.
    """


def test_update_kwargs_id(self):
    s = Square(1)
    s.update(id=2)
    self.assertEqual(str(s), "[Square] (2) 0/0 - 1")


def test_update_kwargs_size(self):
    s = Square(1)
    s.update(size=2)
    self.assertEqual(str(s), "[Square] (1) 0/0 - 2")


def test_update_kwargs_x(self):
    s = Square(1)
    s.update(x=2)
    self.assertEqual(str(s), "[Square] (1) 2/0 - 1")


def test_update_kwargs_y(self):
    s = Square(1)
    s.update(y=2)
    self.assertEqual(str(s), "[Square] (1) 0/2 - 1")


def test_update_kwargs_size_x_y_id(self):
    s = Square(1)
    s.update(size=2, x=3, y=4, id=5)
    self.assertEqual(str(s), "[Square] (5) 3/4 - 2")


def test_update_kwargs_invalid_key(self):
    s = Square(1)
    s.update(invalid_key=2)
    self.assertEqual(str(s), "[Square] (1) 0/0 - 1")


class TestSquareToDictionary(unittest.TestCase):
    """Unittests for testing the to_dictionary method of the Square class."""


def test_to_dictionary(self):
    s = Square(2, 3, 4, 5)
    self.assertEqual(
            s.to_dictionary(),
            {
                'id': 5,
                'size': 2,
                'x': 3,
                'y': 4,
                }
            )


def test_to_dictionary_no_args(self):
    s = Square(1)
    self.assertEqual(
            s.to_dictionary(),
            {
                'id': 1,
                'size': 1,
                'x': 0,
                'y': 0,
                }
            )


def test_to_dictionary_args_and_kwargs(self):
    s = Square(2, 3, 4, 5)
    s.update(6, 7, 8, 9, 10)
    self.assertEqual(
            s.to_dictionary(),
            {
                'id': 10,
                'size': 7,
                'x': 8,
                'y': 9,
                }
            )


if __name__ == '__main__':
    unittest.main()
