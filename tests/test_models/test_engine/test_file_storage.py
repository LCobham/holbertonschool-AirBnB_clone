#!/usr/bin/python3
"""
    This is a module for testing the FileStorage class.
"""


import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
import random
import json


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class"""
    def testStorageVar(self):
        self.assertTrue(type(storage) is FileStorage)

    def testStorageAll(self):
        # Make sure dict is not empy
        new = BaseModel()

        in_storage = storage.all()
        self.assertTrue(type(in_storage) is dict)

        for k, v in in_storage.items():
            point_idx = k.find('.')
            self.assertEqual(k[:point_idx], type(v).__name__)
            self.assertEqual(k[point_idx + 1:], v.id)

    def testNew(self):
        now = datetime.now().isoformat()
        new_bm = BaseModel(id=str(random.randrange(1, 1000)), created_at=now,
                           updated_at=now, random_attr="Random")
        storage.new(new_bm)
        storage.save()
        current = storage.all()
        self.assertTrue(current.get(f"BaseModel.{new_bm.id}") is not None)

    def testSave(self):
        first_len = len(storage.all())
        new = BaseModel()
        new.save()
        self.assertTrue(f"BaseModel.{new.id}" in storage.all().keys())
        self.assertEqual(len(storage.all()), first_len + 1)

    def testReload(self):
        other = FileStorage()
        other.reload()
        current_S, current_R = storage.all(), other.all()
        for key in current_S:
            self.assertEqual(str(current_S[key]), str(current_R[key]))
        new = BaseModel()

        with open(storage._FileStorage__file_path, 'r', encoding='utf-8') as f:
            loaded = json.load(f)

        self.assertTrue(type(loaded) is dict)
        for k, v in loaded.items():
            self.assertTrue(type(v) is dict)
            self.assertIsInstance(current_R[k], BaseModel)

    def testFilePath(self):
        self.assertTrue(type(storage._FileStorage__file_path) is str)

    def testObjects(self):
        self.assertTrue(type(storage._FileStorage__objects) is dict)
