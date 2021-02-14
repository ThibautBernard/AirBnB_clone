#!/usr/bin/python3
import unittest
from io import StringIO
from console import HBNBCommand 
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os.path
from os import path
class TestConsole(unittest.TestCase):
    
    b = BaseModel()
    
    def setUp(self):
        FileStorage._FileStorage__objects = {}
        #if os.path.exists("file.json"):
        #    os.remove("file.json")

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
    """
        Create cmd
    """

    def test_create_command_save_to_json_f(self):
        """ Test that create save to a json file """
        #self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertTrue(os.path.exists("file.json"))

    def test_create_name_class_missing_err_msg(self):
        """ Test that create return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual("** class name missing **", f.getvalue().strip())
        
    def test_create_wrong_name_class_err_msg(self):
        """ Test that create return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create ijd")
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    
    """
        show cmd
    """

    def test_show_name_class_missing_err_msg(self):
        """ Test that show return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual("** class name missing **", f.getvalue().strip())
        
    def test_show_wrong_name_class_err_msg(self):
        """ Test that show return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show ijd")
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_show_no_id_given_err_msg(self):
        """ Test that show return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_show_instance_doesnt_exist_err_msg(self):
        """ Test that show return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 654448")
        self.assertEqual("** no instance found **", f.getvalue().strip())
    
    """
        destroy cmd
    """

    def test_destroy_name_class_missing_err_msg(self):
        """ Test that destroy return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual("** class name missing **", f.getvalue().strip())
        
    def test_destroy_wrong_name_class_err_msg(self):
        """ Test that destroy return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy ijd")
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_destroy_no_id_given_err_msg(self):
        """ Test that destroy return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_destroy_instance_doesnt_exist_err_msg(self):
        """ Test that destroy return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 654448")
        self.assertEqual("** no instance found **", f.getvalue().strip())

    """
        all cmd
    """

    def test_all_class_doesnt_exist_missing_err_msg(self):
        """ Test that all return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all udzhdz")
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    """
        update cmd
    """

    def test_update_name_class_missing_err_msg(self):
        """ Test that update return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual("** class name missing **", f.getvalue().strip())
        
    def test_update_wrong_name_class_err_msg(self):
        """ Test that update return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update ijd")
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_update_no_id_given_err_msg(self):
        """ Test that update return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_update_instance_doesnt_exist_err_msg(self):
        """ Test that update return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 654448")
        self.assertEqual("** no instance found **", f.getvalue().strip())
    
    def test_update_attribute_name_missing_exist_err_msg(self):
        """ Test that update return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {}".format(self.b.id))
        self.assertEqual("** attribute name missing **", f.getvalue().strip())

    def test_update_value_not_exist__err_msg(self):
        """ Test that update return a msg error """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} ddzdz".format(self.b.id))
        self.assertEqual("** value missing **", f.getvalue().strip())
    

    """
        help cmd
    """
    def test_help_show_cmd(self):
        """ Test help on show command """
        s = """Prints the string representation of an instance based on the class name and id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertTrue(s in f.getvalue().strip())
    
    """
        quit cmd

    """
    def test_quit__cmd(self):
        """ Test quit command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    """
        class_name.cmd()
    """

    def test_dot_all_wrong_class_name_cmd(self):
        """ Test .all() with wrong class name command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseMod.all()")
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())
    
    def test_dot_count_wrong_class_name_cmd(self):
        """ Test .count() with wrong class name command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Bzdz.all()")
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_dot_show_wrong_class_name_cmd(self):
        """ Test .show() with wrong class name command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Bzdz.show()")
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_dot_show_no_id_cmd(self):
        """ Test .show() with no id command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_dot_show_id_not_exist_cmd(self):
        """ Test .show() with id not exist command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(54)")
        self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_dot_show_class_name_missing_cmd(self):
        """ Test .show() with class name missing command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".show()")
        self.assertEqual("** class name missing **", f.getvalue().strip())
    
    def test_dot_destroy_class_name_missing_cmd(self):
        """ Test .destroy() with class name missing command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".destroy()")
        self.assertEqual("** class name missing **", f.getvalue().strip())
    """
    def test_dot_destroy_class_name_missing_two_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy()")
        self.assertEqual("** class name missing **", f.getvalue().strip())
    """
    def test_dot_destroy_wrong_class_name_cmd(self):
        """ Test .destroy() with wrong class name command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Bzdz.destroy()")
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_dot_destroy_no_id_cmd(self):
        """ Test .destroy() with no id command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
        self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_dot_destroy_id_not_exist_cmd(self):
        """ Test .destroy() with id not exist command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(54)")
        self.assertEqual("** no instance found **", f.getvalue().strip())


    def test_dot_update_wrong_class_name_cmd(self):
        """ Test .update() with wrong class name command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Bzdz.update()")
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_dot_update_no_id_cmd(self):
        """ Test .update() with no id command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
        self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_dot_update_id_not_exist_cmd(self):
        """ Test .update() with id not exist command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(54)")
        self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_dot_update_class_name_missing_cmd(self):
        """ Test .update() with class name missing command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".update()")
        self.assertEqual("** class name missing **", f.getvalue().strip())
    
    def test_dot_update_attribute_missing_cmd(self):
        """ Test .update() with attribute missing command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update({})".format(self.b.id))
        self.assertEqual("** attribute name missing **", f.getvalue().strip())
    
    def test_dot_update_value_missing_cmd(self):
        """ Test .update() with value missing command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update({}, lol)".format(self.b.id))
        self.assertEqual("** value missing **", f.getvalue().strip())
    
    def test_dot_update_id_missing_cmd(self):
        """ Test .update() with id missing command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()".format(self.b.id))
        self.assertEqual("** instance id missing **", f.getvalue().strip())
    """
    def test_dot_all_with_no_class_name_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
        self.assertEqual("** class name missing **", f.getvalue().strip())
    """
    """def test_dot_all_cmd(self):
        HBNBCommand().onecmd("create BaseModel")
        r = ""
        with open('file.json', 'r') as o:
            r = o.read()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
        self.assertEqual(r, f.getvalue().strip())
    """
