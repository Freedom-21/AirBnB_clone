#!/usr/bin/python3
"""
User module
Defines the User class that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """represents a User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
