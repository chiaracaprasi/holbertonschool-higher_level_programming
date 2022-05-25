#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from xml.dom.minidom import Element
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_module_docstring(self):
        """Tests for module docsting"""
        mod = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        func = max_integer.__doc__
        self.assertTrue(len(func) > 1)

    def test_regular_use(self):
        """Test with a regular list of ints: should return the max result"""
        test = [1, 2, 3, 4, 5]
        result = max_integer(test)
        self.assertEqual(result, 5)

    def test_none(self):
        """Tests for none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int(self):
        """Tests for a non-int"""
        test = [1, 2, 3, "Hello", 5]
        with self.assertRaises(TypeError):
            max_integer(test)

    def test_empty_list(self):
        """Tests result of empty list []"""
        test = []
        self.assertIsNone(max_integer(test))

    def test_same_values(self):
        """Tests result of same values in list []"""
        test = [1, 5, 5, 5]
        result = max_integer(test)
        self.assertEqual(result, 5)

    def test_same_values(self):
        """Tests result of same values in list []"""
        test = [1, 5, 5, 5]
        result = max_integer(test)
        self.assertEqual(result, 5)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        test = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(test), -1)


if __name__ == "__main__":
    unittest.main()
