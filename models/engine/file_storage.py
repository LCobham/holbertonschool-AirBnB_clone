#!/usr/bin/python3
"""
    This module creates the FileStorage class to serialize instances
    to a JSON file and deserialize a JSON file to instances.
"""

import json


class FileStorage:
    """
        FileStorage class - used to serialize instances to JSON
        and deserialize JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns the '__objects' dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            Creates new entry in the '__objects' dictionary:
            key = <obj class name>.id
            value = obj 
        """
        new_key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[new_key] =  obj

    def save(self):
        """
            Serializes the '__objects' dictionary to the JSON file
            with path = __file_path
        """
        all_objs = self.all()
        to_dump = {key: value.to_dict() for key, value in all_objs.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(to_dump, f, indent=2)

    def reload(self):
        """
            Deserializes the JSON file to __objects if the path specified
            in __file_path exists.
        """
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                loaded = json.load(f)
            for key, value in loaded.items():
                loaded[key] = BaseModel(**value)
            FileStorage.__objects = loaded

        except FileNotFoundError:
            pass
