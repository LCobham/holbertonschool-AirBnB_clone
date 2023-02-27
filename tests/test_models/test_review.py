#!/usr/bin/python3
"""
    This is a module for testing the City class.
"""


import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    """Test Review class"""
    def setUp(self):
        self.a1 = Review()

    def testType(self):
        self.assertTrue(type(self.a1) is Review)
        self.assertIsInstance(self.a1, BaseModel)

    def testClassAttrs(self):
        self.assertEqual(type(Review.place_id), str)
        self.assertEqual(type(Review.user_id), str)
        self.assertEqual(type(Review.text), str)
