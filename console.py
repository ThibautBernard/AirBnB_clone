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
    """
    prompt : the prompt of interpreter.
    exist_class : array of all class that exits.
    obj : instance of FileStorage class to call method
    after.
    dict_obj : dictionary of all instance created
    """
    prompt = '(hbtn) '
    exist_class = ["BaseModel"]
    obj = FileStorage()
    dict_obj = obj.all()

    """ ***************************** """
    """    Utilities methods below     """
    """ ***************************** """

    def check_command(self, line):
        """Method that check arguments of a command
            Return True if all argument are valid
            Return False if argument none vali
        """
        if len(line) == 0:
            print("** class name missing **")
            return False
        elif line[0] not in HBNBCommand.exist_class:
            print("** class doesn't exist **")
            return False
        elif len(line) == 1:
            print("** instance id missing **")
            return False
        else:
            object_to_print = self.split(HBNBCommand.dict_obj, line[1])
            if object_to_print is None:
                print("** no instance found **")
                return False
        return True

    def split(self, dict_obj, id_to_match):
        """ Search in dict if there is an
            object with the same id
            If yes, return the object
        """
        for i in dict_obj:
            if dict_obj[i].id == id_to_match:
                return dict_obj[i]
        return None

    """ ***************************** """
    """    Commands methods below     """
    """ ***************************** """

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

    def do_all(self, line):
        """ Print all object from a class in a list """
        s = line.split()
        arr = []
        if len(s) == 0:
            for i in HBNBCommand.dict_obj:
                arr.append(str(HBNBCommand.dict_obj[i]))
            print(arr)
        elif s[0] in HBNBCommand.exist_class:
            for i in HBNBCommand.dict_obj:
                name_class = i.split('.')
                if name_class[0] == s[0]:
                    arr.append(str(HBNBCommand.dict_obj[i]))
            print(arr)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Show an object """
        s = line.split()
        if self.check_command(s):
            object_to_print = self.split(HBNBCommand.dict_obj, s[1])
            print(object_to_print)

    def do_update(self, line):
        """ Update or add attribute of the object (class name and id given)
            id, created_at and updated_at can't be updated
        """
        s = line.split()
        if self.check_command(s):
            if len(s) <= 2:
                print("** attribute name missing **")
            elif len(s) <= 3:
                print("** value missing **")
            else:
                obj_and_id = s[0] + '.' + s[1]
                for i in HBNBCommand.dict_obj:
                    if i == obj_and_id:
                        if s[3][0] == '"' and s[3][-1] == '"':
                            value = s[3][1:-1]
                        else:
                            value = s[3]
                        setattr(HBNBCommand.dict_obj[i], s[2], value)
                        HBNBCommand.obj.save()

    def do_destroy(self, line):
        """ Destroy an object """
        s = line.split()
        if self.check_command(s):
            obj_and_id = s[0] + '.' + s[1]
            for i in HBNBCommand.dict_obj:
                if i == obj_and_id:
                    delet_key = 1
                    break
            if delet_key:
                del HBNBCommand.dict_obj[i]
                HBNBCommand.obj.save()

    def do_quit(self, s):
        """ Quit command """
        return True

    def do_EOF(self, line):
        """ EOF """
        print("")
        return True

    def emptyline(self):
        """Empty line send """
        pass

    """ ***************************** """
    """ Documentation commands below """
    """ ***************************** """

    def help_quit(self):
        """ Documentation to quit command """
        print("Quit command to exit the program")

    def help_EOF(self):
        """ Documentation to EOF"""
        print("EOF to exit the program")

    def help_all(self):
        """Documentation of <all> command """
        print("Prints all string representation of all instance " +
              "based or not on the class name")
        print("--- Usage ---")
        print("-> (hbtn) all")
        print("-> (hbtn) all <class_name>")

    def help_create(self):
        """Documentation of create command """
        print("Creates a new instance and print the id")
        print("--- Usage ---")
        print("-> (hbtn) create <class_name>")

    def help_show(self):
        """Documentation of show command """
        print("Prints the string representation of an instance " +
              "based on the class name and id")
        print("--- Usage ---")
        print("-> (hbtn) show <class_name> <id_instance>")

    def help_destroy(self):
        """Documentation of destroy command """
        print("Deletes an instance based on the class name and id")
        print("--- Usage ---")
        print("-> (hbtn) destroy <class_name> <id_instance>")

    def help_update(self):
        """Documentation of update command """
        print("Updates an instance based on the class name " +
              "and id by adding or updating attribute")
        print("! Only one attribute can be updated at the time")
        print("! id, created_at and updated_at cant’ be updated")
        print("--- Usage ---")
        print("-> (hbtn) update <class name> <id> " +
              "<attribute name> \"<attribute value>\"")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
