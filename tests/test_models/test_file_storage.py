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


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class"""
    def testStorageVar(self):
        self.assertTrue(type(storage) is FileStorage)

    def testStorageAll(self):
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
        current = storage.all()
        from_current = current.get(f"{type(new_bm).__name__}.{new_bm.id}")
        self.assertTrue(str(from_current), str(new_bm))
