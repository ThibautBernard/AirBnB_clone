#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
import os.path
from os import path
class TestAmenity(unittest.TestCase):

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    """Basic instanciation object__init__"""
    def test_user_id_created(self):
        """ Test id created """
        obj = Amenity()
        self.assertTrue(obj.id is not None)
        self.assertTrue(type(obj) is Amenity)

    def test_user_is_instance_object_user(self):
        """ Test id created """
        obj = Amenity()
        self.assertTrue(type(obj) is Amenity)
        
    def test_is_id_is_string(self):
        """ Test id is a string"""
        obj = Amenity()
        self.assertTrue(type(obj.id) ==  str)

    def test_is_id_different_multiple_instance(self):
        """ Test that id is different with two instance object """
        obj = Amenity()
        obj2 = Amenity()
        self.assertTrue(obj.id != obj2.id)

    def test_is__created_date_is_created(self):
        """ Test that a date has been well created """
        obj = Amenity()
        self.assertTrue(obj.created_at is not None)

    def test_is_created_date_is_created(self):
        """ Test that a date has been well created """
        obj = Amenity()
        obj2 = Amenity()
        self.assertTrue(obj.created_at is not None and obj2.created_at is not None)

    def test_is__created_date_is_object_datatime(self):
        """ Test that created_at is a object date"""
        obj = Amenity()
        self.assertTrue(type(obj.created_at) == datetime)

    def test_is_updated_at_is_created(self):
        """ Test that updated_at attribute has been well created """
        obj = Amenity()
        self.assertTrue(obj.updated_at is not None)

    def test_is_updated_at_is_created_multiple_instance(self):
        """ Test that updated_at attribute has been well created with multiple instance"""
        obj = Amenity()
        obj2 = Amenity()
        self.assertTrue(obj.updated_at is not None and obj2.updated_at is not None)

    def test_is_updated_at_is_object_datatime(self):
        """ Test that updated_at is a object date"""
        obj = Amenity()
        self.assertTrue(type(obj.updated_at) == datetime)
    
    def test_is_name_updated(self):
        """ Test that name attribute is well updated"""
        obj = Amenity()
        obj.name = "Thibaut"
        self.assertTrue(obj.name == "Thibaut")
    
    """
        kwargs
    """
    def test_is_kwargs_instance(self):
        """ Test that kwargs instance well """
        obj = Amenity()
        save_dict = obj.to_dict()
        new_obj = Amenity(**save_dict)
        self.assertTrue(save_dict == new_obj.to_dict())

    def test_is_kwargs_created_at_date_object(self):
        """ Test that kwargs is instance created_at to date object """
        obj = Amenity()
        save_dict = obj.to_dict()
        new_obj = Amenity(**save_dict)
        self.assertTrue(type(new_obj.created_at) is datetime)
    """ 
    def test_is_kwargs_ignore_one_attribute(self):
        obj = BaseModel()
        save_dict = obj.to_dict()
        new_obj = BaseModel(**save_dict)
        with self.assertRaises(AttributeError):
            new_obj.__class__
    """
    """ 
    Method to_dict()
    """
    def test_is_to_dict_return_a_dict(self):
        """ Test that the to_dict() method return well a dictionnary """
        obj = Amenity()
        s = obj.to_dict()
        self.assertTrue(type(s) is dict)

    def test_is_to_dict_updated_at_is_str(self):
        """ Test that to_dict() updated_at is str in dictionary"""
        obj = Amenity()
        s = obj.to_dict()
        for i in s:
            if i == "updated_at":
                self.assertTrue(type(s[i]) is str)

    """	
        Method __str__
    """
    def test_is_str_return_a_string(self):
        """ Test that __str__return well a string """
        obj = Amenity()
        s = str(obj)
        self.assertTrue(type(s) is str)
    
    def test_is_str_return_the_correct_class_name(self):
        """ Test that __str__ user as class name """
        obj = Amenity()
        s = str(obj)
        self.assertTrue("Amenity" in s)

    """
        Method save()
    
    def test_is_save_update_well(self):
        x = BaseModel()
        x.save()
        self.assertTrue(x.created_at != x.updated_at)

    def test_is_save_update(self):
        s = BaseModel()
        h = s.updated_at
        s.save()
        self.assertTrue(h != s.updated_at)
    """
