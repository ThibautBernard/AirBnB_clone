#!/usr/bin/python3
from datetime import datetime
import models
import uuid
"""
    BaseModel class - defines all common attributes/methods for other classes
    All classes inherit from this class
    Id object, date, Serialization & Deserialization
"""


class BaseModel:
    """
        Class that does a lot of things
    """
    def __init__(self, *args, **kwargs):
        """Initialisation"""
        if len(kwargs) == 0 or kwargs is None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            reserved_attribute = ['created_at', 'updated_at']
            for i in kwargs:
                if i not in "__class__" and i not in reserved_attribute:
                    setattr(self, i, kwargs[i])
                elif i in reserved_attribute:
                    date_str = kwargs[i]
                    f = '%Y-%m-%dT%H:%M:%S.%f'
                    date_obj = datetime.strptime(date_str, f)
                    setattr(self, i, date_obj)

    def __str__(self):
        """ Return representation str of the object"""
        name_class_obj = self.__class__.__name__
        return "[{}] ({}) {}".format(name_class_obj, self.id, self.__dict__)

    def save(self):
        """ Update attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

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
        dicto["__class__"] = self.__class__.__name__
        return dicto
