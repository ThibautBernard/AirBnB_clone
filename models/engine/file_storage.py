#!/usr/bin/python3
import json
import os.path
import sys
from os import path
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models.user import User
"""
    Store objects - Serialization/Deserialization
"""


class FileStorage:
    """ serialize, deserialize"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return dictionnary of all object stored """
        return FileStorage.__objects

    def new(self, obj):
        """ Add object in dictionnary __objects """
        if obj is not None:
            name_class = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects.update({name_class: obj})

    def save(self):
        """
            Serialize
            Save objects from dictionnary __objects into a file (format json)
        """
        d = {}
        if len(FileStorage.__objects) > 0:
            for i in FileStorage.__objects:
                    if FileStorage.__objects[i] is dict:
                        d[i] = FileStorage.__objects[i]
                        # FileStorage.__objects[i] = FileStorage.__objects[i]
                    else:
                        d[i] = FileStorage.__objects[i].to_dict()
            with open(self.__file_path, 'w') as f:
                f.write(json.dumps(d))
        else:
            with open(self.__file_path, 'w') as f:
                f.write("")

    def reload(self):
        """ Deserialize
        Load object from the file into python objects
        to dictionnary __objects
        """
        file_not_empty = 0
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                json_f = f.read()
                if len(json_f) > 0:
                    file_not_empty = 1
                    deserial = json.loads(json_f)
            if file_not_empty:
                for i in deserial:
                    name_class_only = i.split('.')
                    # FileStorage.__objects[i] = o(**deserial[i])
                    if name_class_only[0] == "BaseModel":
                        FileStorage.__objects[i] = BaseModel(**deserial[i])
                    elif name_class_only[0] == "User":
                        FileStorage.__objects[i] = User(**deserial[i])
                    elif name_class_only[0] == "State":
                        FileStorage.__objects[i] = State(**deserial[i])
                    elif name_class_only[0] == "Place":
                        FileStorage.__objects[i] = Place(**deserial[i])
                    elif name_class_only[0] == "City":
                        FileStorage.__objects[i] = City(**deserial[i])
                    elif name_class_only[0] == "Amenity":
                        FileStorage.__objects[i] = Amenity(**deserial[i])
                    elif name_class_only[0] == "Review":
                        FileStorage.__objects[i] = Review(**deserial[i])
