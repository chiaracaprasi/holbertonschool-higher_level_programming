#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest

from models import base
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    def test_module_docstring(self):
        """ Tests for docstring"""
        self.assertTrue(lenm(Base.__doc__) >= 1)


class TestBase(unittest.TestCase):
    """ Tests functionality of class"""
    def test_id_none(self):
        b_1 = Base()
        self.asserEqual(b_1.id, 1)

    def test_id_assigned(self):
        b_2 = Base(8)
        self.assertEqual(b_2.id, 8)
