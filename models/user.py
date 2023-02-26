#!/usr/bin/python3
"""
    This module creates the User class.
"""

from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """
        User class
    """

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        storage.new(self)
