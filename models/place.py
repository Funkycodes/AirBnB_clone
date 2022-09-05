#!/usr/bin/python3
"""
File: place.py
Author: theMaskedOtaku
Email: otakuS3nnin@gmail.com
Github: https://github.com/Funkycodes
Description:
"""

from models.base_model import BaseModel


class Place(BaseModel):

    """Describe the properties of the lodgings offered. Describe the price,
    location, owner, name, number of guests, number of rooms, and the elevation
    """

    city_id = ""  # City.id
    user_id = ""  # User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # ids of all amenities it has
