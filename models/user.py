"""
File: user.py
Author: theMaskedOtaku
Email: otakuS3nnin@email.com
Github: https://github.com/Funkycodes
Description: Contains User class that defines set of behavior and actions made
available to the user
"""


from models.base_model import BaseModel


class User(BaseModel):

    """User class defines set of methods and attributes to be associated with
    User of the platform. Inherits from BaseModel, does not implement any over\
    ride, """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
