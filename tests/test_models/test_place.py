#!/usr/bin/python3
"""
    This is a module for testing the Place class.
"""


import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """Test Place class"""
    def setUp(self):
        self.a1 = Place()

    def testType(self):
        self.assertTrue(type(self.a1) is Place)
        self.assertIsInstance(self.a1, BaseModel)

    def testClassAttrs(self):
        self.assertEqual(type(Place.city_id), str)
        self.assertEqual(type(Place.user_id), str)
        self.assertEqual(type(Place.name), str)
        self.assertEqual(type(Place.description), str)
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(type(Place.price_by_night), int)
        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(type(Place.amenity_ids), list)
