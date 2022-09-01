"""
File: file_storage.py
Author: theMaskedOtiaku
Email: otakuS3nnin@email.com
Github: https://github.com/Funkycodes
Description: Contains FileStorage class responsible for storage of instances
"""
import json
from datetime import datetime as dt
import uuid


class BaseModel(object):

    """Docstring for BaseModel"""

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
            storage.new(self)

    def to_dict(self):
        """docstring for to_dict"""

        dict_repr = {}
        dict_repr['__class__'] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (dt, )):
                dict_repr[k] = dt.isoformat(v)
            else:
                dict_repr[k] = v
        return dict_repr


class FileStorage(object):

    """Docstring for FileStorage. """
    # NOTE: Why not have every core class have its own FileStorage object rath\
    # er than have a single storage handler. I mean to use composition to give
    # every core class a storage object.

    __file_path = "file.json"
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel
    }

    def __init__(self):

        pass

    def all(self):
        """docstring for all"""

        return FileStorage.__objects

    def new(self, obj):
        """
        Adds new object to the record of instantiated objects
        """

        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
            obj.id)] = obj.to_dict()

    def save(self):
        """
        Saves file to __file_path.json
        """

        with open(FileStorage.__file_path, 'w+', encoding='utf8') as file:
            json.dump(FileStorage.__objects, file)

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


if __name__ == "__main__":
    storage = FileStorage()
    model1 = BaseModel()
    storage.new(model1)
    storage.save()
    FileStorage.__objects = {}
    storage.reload()
    print(storage.all())
