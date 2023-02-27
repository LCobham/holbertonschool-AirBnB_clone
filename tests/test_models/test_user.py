#!/usr/bin/python3
"""
    This is a module for testing the User class.
"""


import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test User class"""
    def setUp(self):
        self.u1 = User()

    def testUserType(self):
        self.assertTrue(type(self.u1) is User)
        self.assertIsInstance(self.u1, BaseModel)

    def testInheritedAttrs(self):
        self.assertTrue(type(getattr(self.u1, 'id')) is str)
        self.assertTrue(type(getattr(self.u1, 'created_at')) is datetime)
        self.assertTrue(type(getattr(self.u1, 'updated_at')) is datetime)

    def testClassAttrs(self):
        self.assertEqual(User.email, '')
        self.assertEqual(User.password, '')
        self.assertEqual(User.first_name, '')
        self.assertEqual(User.password, '')
