#!/usr/bin/python3
"""
    This is a module for testing the FileStorage class.
"""


import unittest
from models.base_model import BaseModel
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
            self.assertTrue(type(v) is BaseModel)
            point_idx = k.find('.')
            self.assertEqual(k[:point_idx], type(v).__name__)
            self.assertEqual(k[point_idx + 1:], v.id)

    def testStorageNewSaveAndReload(self):
        now = datetime.now().isoformat()
        new_bm = BaseModel(id=str(random.randrange(1, 1000)), created_at=now, updated_at=now, random_attr="Random")
        previous = storage.all().copy()
        storage.new(new_bm)
        storage.save()
        updated = storage.all().copy()
        self.assertNotEqual(previous, updated)
        self.assertTrue(len(previous) + 1 == len(updated))
        for key in previous.keys():
            del updated[key]
        self.assertEqual(len(updated), 1)
        new_name = "BaseModel." + new_bm.id
        self.assertEqual(str(updated.get(new_name)), str(new_bm))

        before = storage.all().copy()
        check_reloaded = FileStorage()
        check_reloaded.reload()
        reload_storage = check_reloaded.all()
        for k, v in reload_storage.items():
            self.assertTrue(k in before.keys())
            self.assertEqual(str(v), str(before[k]))

