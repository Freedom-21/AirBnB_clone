#!/usr/bin/python3
"""
City module
defines the City class that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """represents a City"""

    state_id = ""
    name = ""
