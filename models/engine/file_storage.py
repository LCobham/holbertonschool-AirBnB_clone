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
        name = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[name] = obj

    def save(self):
        """
            Serializes the '__objects' dictionary to the JSON file
            with path = __file_path
        """

    def reload(self):
        """
            Deserializes the JSON file to __objects if the path specified
            in __file_path exists.
        """
