#!/usr/bin/python3
"""
    This is a module for testing the Amenity class.
"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """Test Amenity clas"""
    def setUp(self):
        self.a1 = Amenity()

    def testType(self):
        self.assertTrue(type(self.a1) is Amenity)
        self.assertIsInstance(self.a1, BaseModel)

    def testClassAttrs(self):
        self.assertEqual(type(Amenity.name), str)
