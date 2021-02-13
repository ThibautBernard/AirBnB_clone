#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os.path
from os import path
class Testfile_storage(unittest.TestCase):

    def setUp(self):
        FileStorage._FileStorage__objects = {}
    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_is_object_save_in_file(self):
        """ Test if save() save to a file """
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        obj.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_is_all_return_dict_not_empty_(self):
        """ Test if all() return dict and not empty"""
        obj = BaseModel()
        f = FileStorage()
        obj.name = "Holberton"
        obj.my_number = 89
        obj.save()
        f.reload()
        x = f.all()
        self.assertTrue(len(x) > 0)
        self.assertTrue(type(x) is dict)

    def test_reload_to_attribute_dict(self):
        """ Test that reload() reload from json file to an oject value"""
        obj = BaseModel()
        f = FileStorage()
        obj.name = "Holberton"
        obj.my_number = 89
        obj.save()
        id = obj.id
        f.reload()
        x = f.all()
        self.assertTrue(type(x['BaseModel.{}'.format(id)]) is BaseModel)
    
