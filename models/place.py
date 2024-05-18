#!/usr/bin/python3
"""
Place module
Defines the Place class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a Place"""

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
