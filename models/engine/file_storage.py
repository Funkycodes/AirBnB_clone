"""
File: file_storage.py
Author: theMaskedOtiaku
Email: otakuS3nnin@email.com
Github: https://github.com/Funkycodes
Description: Contains FileStorage class responsible for storage of instances
"""

import json
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.state import State


class FileStorage(object):

    """Docstring for FileStorage. """
    # NOTE: Why not have every core class have its own FileStorage object rath\
    # er than have a single storage handler. I mean to use composition to give
    # every core class a storage object.

    __file_path = "file.json"
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "City": City,
        "User": User,
        "Review": Review,
        "Place": Place,
        "Amenity": Amenity,
        "State": State
    }

    def __init__(self):
        """Empty init method, empty because there are not instance attributes
        to be defined
        """

        pass

    def all(self):
        """Return dictionary containing all existing object instances"""

        return FileStorage.__objects

    def new(self, obj):
        """
        Adds new object to the record of instantiated objects
        """

        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """
        Saves file to __file_path.json
        """
        dict_repr = {}
        for id, obj in FileStorage.__objects.items():
            dict_repr[id] = obj.to_dict()

        with open(FileStorage.__file_path, 'w+', encoding='utf8') as file:
            json.dump(dict_repr, file)

    def reload(self):
        """
        Loads json files from file and returns instances record object
        """

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf8') as file:
                new_obj = json.load(file)
                for v in new_obj.values():
                    obj = FileStorage.class_dict[v['__class__']](**v)
                    self.new(obj)
        except FileNotFoundError:
            pass
