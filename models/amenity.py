#!/usr/bin/python3
"""
    This module creates the Amenity Class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ''

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)
