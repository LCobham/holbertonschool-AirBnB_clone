#!/usr/bin/python3
"""
    This is a module for testing the City class.
"""


import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """Test State class"""
    def setUp(self):
        self.a1 = State()

    def testType(self):
        self.assertTrue(type(self.a1) is State)
        self.assertIsInstance(self.a1, BaseModel)

    def testClassAttrs(self):
        self.assertEqual(type(State.name), str)
