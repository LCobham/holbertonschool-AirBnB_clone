#!/usr/bin/python3
"""
    This is a module for testing the City class.
"""


import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """Test City class"""
    def setUp(self):
        self.a1 = City()

    def testType(self):
        self.assertTrue(type(self.a1) is City)
        self.assertIsInstance(self.a1, BaseModel)

    def testClassAttrs(self):
        self.assertEqual(type(City.name), str)
        self.assertEqual(type(City.state_id), str)
