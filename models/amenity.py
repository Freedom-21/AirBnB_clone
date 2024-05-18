#!/usr/bin/python3
"""
Amenity module
Defines the Amenity class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an Amenity"""

    name = ""
