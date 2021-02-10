#!/usr/bin/python3
from datetime import datetime
import uuid
"""
    BaseModel class - defines all common attributes/methods for other classes
    All classes inherit from this class
    Id object, date, Serialization & Deserialization
"""


class BaseModel:
    def __init__(self):
        """Initialisation"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Return representation str of the object"""
        return "[BaseModel] ({}) <{}>".format(self.id, self.__dict__)

    def save(self):
        """ Update attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return a dict of object attributes and methods"""
        special_case = ["updated_at", "created_at"]
        dicto = {}
        for i in self.__dict__:
            if i in special_case:
                tmp = getattr(self, i).isoformat()
                dicto[i] = tmp
            else:
                dicto[i] = getattr(self, i)
        dicto["__class__"] = "BaseModel"
        return dicto
