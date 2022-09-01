from datetime import datetime as dt
import uuid
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import models

"""
File: base_model.py
Author: theMaskedOtaku
Email: yourname@email.com
Github: https://github.com/Funkycodes
Description: Contains BaseModel class that defines common attributes/methods \
for other classes
"""


class BaseModel(object):

    """Docstring for BaseModel. """

    def __init__(self, *args, **kwargs):
        """
        Init method

        Sets all the relevant instance attributes
        """
        if kwargs:
            for k, v in kwargs.items():
                if "__class__" == k:
                    pass
                elif "created_at" == k:
                    self.created_at = dt.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == k:
                    self.updated_at = dt.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        print("[{}] ({}) <{}>".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """docstring for s"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """docstringfor to_dict"""
        dict_repr = {}
        dict_repr['__class__'] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (dt, )):
                dict_repr[k] = dt.isoformat(v)
            else:
                dict_repr[k] = v
        return dict_repr


base1 = BaseModel()
print(models.storage.all())
base1.save()
