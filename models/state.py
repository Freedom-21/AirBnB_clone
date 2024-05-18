#!/usr/bin/python3
"""
State module
refines the State class that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """represents a State"""

    name = ""
