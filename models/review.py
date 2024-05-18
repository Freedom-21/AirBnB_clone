#!/usr/bin/python3
"""
Review module
Defines the Review class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review"""

    place_id = ""
    user_id = ""
    text = ""
