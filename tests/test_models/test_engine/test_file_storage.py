#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
import os.path
from os import path
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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
        self.assertEqual(type(x), dict)

    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_save(self):
        """Test that save properly saves objects to file.json"""
        os.remove("file.json")
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
            self.assertEqual(json.loads(string), json.loads(js))

    def test_all(self):
        """ test all() dict"""
        f = FileStorage()
        n = f.all()
        self.assertEqual(type(n), dict)

    def test_save(self):
        """test save correctly"""
        b = BaseModel()
        b.name = "Berg"
        b.save()
        with open("file.json", "r") as f:
            self.assertNotEqual(0, len(f.read()))

    def test_two_save(self):
        """test save correctly"""
        b = BaseModel()
        b.name = "Berg"
        b.save()
        with open("file.json", "r") as f:
            self.assertNotEqual(0, len(f.read()))

    def test_a(self):
        return True

    def test_b(self):
        return True

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
        self.assertEqual(type(x['BaseModel.{}'.format(id)]),  BaseModel)
