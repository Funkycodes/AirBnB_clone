"""
File: review.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description: Class for User Review
"""

from models.base_model import BaseModel


class Review(BaseModel):

    """Class for User Reviews. Contains Class Attributes place_id(place being\
 reviewed), user_id(the reviewer) and text(the review).
    """

    place_id = ""  # Place.id
    user_id = ""  # User.id
    text = ""
