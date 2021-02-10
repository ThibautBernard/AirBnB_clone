#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

"""
    HBNBCommand - command line interpreter to manage
    our object/classess
"""


class HBNBCommand(cmd.Cmd):
    prompt = '(hbtn) '
    exist_class = ["BaseModel"]

    def help_quit(self):
        """ Documentation to quit command """
        print("Quit command to exit the program")

    def help_EOF(self):
        """ Documentation to EOF"""
        print("EOF to exit the program")

    def do_create(self, line):
        """ Create an instance """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.exist_class:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """ Show an object """
        s = line.split()
        if len(s) == 0:
            print("** class name missing **")
        elif s[0] not in HBNBCommand.exist_class:
            print("** class doesn't exist **")
        elif len(s) == 1:
            print("** instance id missing **")
        else:
            obj = FileStorage()
            dict_obj = obj.all()
            object_to_print = self.split(dict_obj, s[1])
            if object_to_print is None:
                print("** no instance found **")
            else:
                print(object_to_print)

    def split(self, dict_obj, id_to_match):
        """ Search in dict if there is an
            object with the same id
            If yes, return the object
        """
        for i in dict_obj:
            if dict_obj[i].id == id_to_match:
                return dict_obj[i]
        return None

    def do_quit(self, s):
        """ Quit command """
        return True

    def do_EOF(self, line):
        """ EOF """
        return True

    def emptyline(self):
        """Empty line send """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
