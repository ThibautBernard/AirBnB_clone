#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
class TestBase_model(unittest.TestCase):
	
	"""
		Basic instanciation object
		__init__
	"""
	def test_is_id_created(self):
		""" Test id created """
		obj = BaseModel()
		self.assertTrue(obj.id is not None)
	
	def test_is_id_is_string(self):
		""" Test id is a string"""
		obj = BaseModel()
		self.assertTrue(type(obj.id) ==  str)

	def test_is_id_different_multiple_instance(self):
		""" Test that id is different with two instance object """
		obj = BaseModel()
		obj2 = BaseModel()
		self.assertTrue(obj.id != obj2.id)

	def test_is__created_date_is_created(self):
		""" Test that a date has been well created """
		obj = BaseModel()
		self.assertTrue(obj.created_at is not None)
	
	def test_is_created_date_is_created(self):
		""" Test that a date has been well created """
		obj = BaseModel()
		obj2 = BaseModel()
		self.assertTrue(obj.created_at is not None and obj2.created_at is not None)
	
	def test_is__created_date_is_object_datatime(self):
		""" Test that created_at is a object date"""
		obj = BaseModel()
		self.assertTrue(type(obj.created_at) == datetime)

	def test_is_updated_at_is_created(self):
		""" Test that updated_at attribute has been well created """
		obj = BaseModel()
		self.assertTrue(obj.updated_at is not None)

	def test_is_updated_at_is_created_multiple_instance(self):
		""" Test that updated_at attribute has been well created with multiple instance"""
		obj = BaseModel()
		obj2 = BaseModel()
		self.assertTrue(obj.updated_at is not None and obj2.updated_at is not None)
	
	def test_is_updated_at_is_object_datatime(self):
		""" Test that updated_at is a object date"""
		obj = BaseModel()
		self.assertTrue(type(obj.updated_at) == datetime)

	"""
		Method to_dict()
	"""
	def test_is_to_dict_return_a_dict(self):
		""" Test that the to_dict() method return well a dictionnary """
		obj = BaseModel()
		s = obj.to_dict()
		self.assertTrue(type(s) is dict)

	def test_is_to_dict_created_at_is_str(self):
		""" Test that to_dict() created_at is str in dictionary"""
		obj = BaseModel()
		s = obj.to_dict()
		for i in s:
			if i == "created_at":
				self.assertTrue(type(s[i]) is str)

	def test_is_to_dict_updated_at_is_str(self):
		""" Test that to_dict() updated_at is str in dictionary"""
		obj = BaseModel()
		s = obj.to_dict()
		for i in s:
			if i == "updated_at":
				self.assertTrue(type(s[i]) is str)


	"""	
		Method __str__
	"""
	def test_is_str_return_a_string(self):
		""" Test that __str__return well a string """
		obj = BaseModel()
		s = str(obj)
		self.assertTrue(type(s) is str)

	"""
		Method save()
	"""
	def test_is_save_update_well(self):
		""" Test that save() update updated_at of the object """
		obj = BaseModel()
		obj.save()
		self.assertTrue(obj.created_at != obj.updated_at)
	
	def test_is_save_update(self):
		""" Test that save() update updated_at of the object """
		obj = BaseModel()
		h = obj.updated_at
		obj.save()
		self.assertTrue(h != obj.updated_at)
	
	
