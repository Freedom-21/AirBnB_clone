#!/usr/bin/python3
"""
Amenity module
defines the Amenity class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """represents an Amenity"""

    name = ""
