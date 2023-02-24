#!/usr/bin/python3
"""
    This is a module for testing the BaseModel class.
"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """BaseModel test class"""
    def setUp(self):
        self.m1 = BaseModel()
        self.m2 = BaseModel()
        self.m3 = BaseModel()
        self.list_of_models = [self.m1, self.m2, self.m3]

    def testAttrTypes(self):
        for model in self.list_of_models:
            self.assertEqual(type(model), BaseModel)
            self.assertEqual(type(model.id), str)
            self.assertEqual(type(model.created_at), datetime)
            self.assertEqual(type(model.updated_at), datetime)

    def testIdUniqueness(self):
        id_list = []
        NUMBER_OF_TESTS = 500
        for i in range(NUMBER_OF_TESTS):
            m = BaseModel()
            id_list.append(m.id)
        self.assertTrue(len(set(id_list)) == NUMBER_OF_TESTS)

    def testSave(self):
        for model in self.list_of_models:
            self.assertTrue(model.created_at == model.updated_at)
            model.save()
            self.assertTrue(model.created_at < model.updated_at)

    def testString(self):
        for model in self.list_of_models:
            self.assertEqual(str(model)[:11], "[BaseModel]")
            self.assertEqual(str(model)[12:50], f"({model.id})")
            self.assertEqual(str(model)[51:], str(model.__dict__))

    def testToDict(self):
        for model in self.list_of_models:
            model.name = 'New name'
            to_dict = model.to_dict()
            self.assertEqual(to_dict.get('__class__'), type(model).__name__)
            self.assertEqual(to_dict['name'], model.name)
            self.assertEqual(to_dict['id'], model.id)
            self.assertTrue(type(to_dict.get('created_at')) == str)
            self.assertTrue(type(to_dict.get('updated_at')) == str)

            # If dates are not ISO the following code will throw an exception
            datetime.fromisoformat(to_dict['created_at'])
            datetime.fromisoformat(to_dict['updated_at'])

    def testKwargs(self):
        for model in self.list_of_models:
            my_dict = model.to_dict()
            kwm = BaseModel(**my_dict)
            self.assertEqual(str(kwm), str(model))
            self.assertFalse(kwm is model)

        kwm = BaseModel(id='101')
        self.assertEqual(kwm.id, '101')
        self.assertTrue(type(kwm) == BaseModel)
        kwm_to_dict = kwm.to_dict()
        self.assertTrue(getattr(kwm, 'created_at', "No attr"), "No attr")
        self.assertTrue(getattr(kwm, 'updated_at', "No attr"), "No attr")

        now = datetime.now().isoformat()
        kwm = BaseModel(1, 2, 3, "Hello world",
                        id='101', name='Test',
                        created_at=now, updated_at=now)
        self.assertEqual(kwm.name, 'Test')
        self.assertTrue(type(getattr(kwm, 'created_at', "No attr")), datetime)
        self.assertTrue(type(getattr(kwm, 'updated_at', "No attr")), datetime)
        self.assertEqual(len(kwm.to_dict()), 5)  # 5 vars in dict w __class__
