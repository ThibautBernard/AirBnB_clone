#!/usr/bin/python3
import json
import os.path
import sys
from os import path
from models.base_model import BaseModel
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        name_class = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({name_class : obj})

    def save(self):
        for i in FileStorage.__objects:
            FileStorage.__objects[i] = FileStorage.__objects[i].to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                json_f = f.read()
                deserial = json.loads(json_f)
            for i in deserial:
                FileStorage.__objects[i] = BaseModel(**deserial[i])
            #FileStorage.__objects = deserial
