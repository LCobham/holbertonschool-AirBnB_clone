#!/usr/bin/python3
"""
   This module creates a Base class that will define all
   common attributes and methods for other classes.
"""

import json
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class that defines all common attributes and methods.
    """
    def __init__(self, *args, **kwargs):
        """
            Initialize BaseModel instance. If a dictionary with attributes
            is provided, initialize with given attributes. Else, initialize
            a new instance with a new ID and a new created_at / updated_at
            value.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
            Tidy print of a BaseModel object. Prints class
            name, ID, and dict.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
           Updates the 'updated_at' attribute.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Create a dictionary representationof the BaseModel object.
            Aside from all public instance attributes, it also includes a
            __class__ key with the class as a value, and the datetime variables
            are presented in ISO format.
        """
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = type(self).__name__

        return my_dict
