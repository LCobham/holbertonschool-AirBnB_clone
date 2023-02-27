#!/usr/bin/python3
"""
    This module creates the City Class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)
