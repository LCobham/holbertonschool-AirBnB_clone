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
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)
