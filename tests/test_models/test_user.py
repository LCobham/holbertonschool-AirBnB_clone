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
        self.u1.first_name = "John"
        self.u1.last_name = "Doe"
        self.u1.email = "jdoe@email.com"
        self.u1.password = "password"

    def testUserType(self):
        self.assertTrue(type(self.u1) is User)
        self.assertIsInstance(self.u1, BaseModel)

    def testInheritedAttrs(self):
        self.assertTrue(type(getattr(self.u1, 'id')) is str)
        self.assertTrue(type(getattr(self.u1, 'created_at')) is datetime)
        self.assertTrue(type(getattr(self.u1, 'updated_at')) is datetime)

    def testNewAttrs(self):
        for attr in ("email", "password", "first_name", "last_name"):
            self.assertTrue(type(getattr(self.u1, attr)) is str)
        self.u1.first_name = "Paul"
        self.assertEqual(self.u1.first_name, "Paul")
        self.assertEqual(self.u1.last_name, "Doe")
        self.assertEqual(self.u1.email, "jdoe@email.com")
        self.assertEqual(self.u1.password, "password")

    def testSerializationDeserialization(self):
        my_dict = self.u1.to_dict()
        self.assertTrue(type(my_dict) is dict)
        self.assertEqual(my_dict.get("__class__"), "User")
        new_user = User(**my_dict)
        for key in my_dict.keys():
            self.assertEqual(getattr(self.u1, key), getattr(new_user, key))
