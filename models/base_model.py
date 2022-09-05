#!/usr/bin/python3

"""
File: base_model.py
Author: theMaskedOtaku
Email: yourname@email.com
Github: https://github.com/Funkycodes
Description: Contains BaseModel class that defines common attributes/methods \
for other classes

Methods:
        __init__(): initializes class, sets the value of key instance\
attributes.
        save(): Save the instances of object to memory using the storage class
        to_dict(): Returns dictionary representation of the class

"""

from datetime import datetime as dt
import time
import uuid
import models


class BaseModel(object):

    """ for BaseModel.

    Sets a template for other application classes and also defines core applic\
    ation class methods
    """

    def __init__(self, *args, **kwargs):

        """
        Init method

        Sets all the relevant instance attributes
        """

        if kwargs:
            for key, value in kwargs.items():
                if "__class__" == key:
                    pass
                elif "created_at" == key:
                    self.created_at = dt.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = dt.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)

    def __str__(self):
        """
        Overrides and implements custom dunder method.
        Prints the string representation of the instance
        """

        return ("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__))

    def __repr__(self):
        """Returns string representation of Object
        """

        return (self.__str__())

    def save(self):
        """Handles storage mechanism for BaseModel and all descendant classes
        """

        time.sleep(0.00003)
        self.updated_at = dt.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns the dictonary representation of the instance"""

        dict_repr = {}
        dict_repr['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, (dt, )):
                dict_repr[key] = dt.isoformat(value)
            else:
                dict_repr[key] = value
        return dict_repr
