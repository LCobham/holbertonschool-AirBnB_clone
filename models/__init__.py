#!/usr/bin/python3
"""
    Initialization code for the package.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
