#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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
    exist_class = [
            "BaseModel", "User", "State",
            "City", "Amenity", "Place", "Review"
            ]
    obj = FileStorage()
    obj.save()
    dict_obj = obj.all()

    """ ***************************** """
    """    Utilities methods below     """
    """ ***************************** """

    def check_command(self, line):
        """Method that check arguments of a command
            Return True if all argument are valid
            Return False if argument none vali
        """
        if len(line) == 0 or line[0] == "()":
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

    def remove_quote(self, arr):
        """
        loop to a list and remove double quote or simple
        quote from value
        """
        if arr[0] != '' and len(arr) >= 1:
            for idx, element in enumerate(arr):
                if element[0] == '"' and element[-1] == '"':
                    arr[idx] = element[1:-1]
                elif element[0] == "'" and element[-1] == "'":
                    arr[idx] = element[1:-1]

    def type_casting(self, attr_type, value_to_type):
        """ Check the type of attribute
            and cast the value to the type
            of the attribute of the class
        """
        if attr_type is int:
            return int(value_to_type)
        elif attr_type is float:
            return float(value_to_type)
        elif attr_type is str:
            return str(value_to_type)
        elif attr_type is tuple:
            return tuple(value_to_type)
        elif attr_type is list:
            return list(value_to_type)
        elif attr_type is dict:
            return dict(value_to_type)

    def check_attr_exist(self, obj, atr_to_find, value_to_cast):
        """Check attribute exist in a class
           if exist get the value of this attribute
           and get the type of the value
           then call type_casting to cast the value_to_cast
           with the type of the attribute
        """
        if hasattr(obj, atr_to_find):
            value_attr = getattr(obj, atr_to_find)
            type_attr = type(value_attr)
            value_to_cast = self.type_casting(type_attr, value_to_cast)
            return value_to_cast
        return value_to_cast

    def check_and_concat_string_from_list(self, class_name, l):
        """
        Check a list of arguments if correctly filled
        and return a string from this
        ex: miss arg2, concat with a space
        l : list of arguments
        For .update(<arg1>, <arg2>, <arg3>)
        """
        length_arr = len(l)
        s = ""
        if length_arr == 3:
            s = class_name + " " + l[0] + " " + l[1] + " " + l[2]
        elif length_arr == 2:
            s = class_name + " " + l[0] + " " + l[1] + " " + ""
        elif length_arr == 1:
            s = class_name + " " + l[0] + " " + "" + " " + ""
        else:
            s = class_name + " " + "" + " " + "" + " " + ""
        return s

    """ ***************************** """
    """    Commands methods below     """
    """ ***************************** """

    def default(self, line):
        """
        Method called if unknow command
        Overwrite if command is in cmd
        usage : name_class.cmd(<value>)
        remove the string into tokens by dot, to have
        the name class alone and cmd + value in other
        remove the cmd from parentheses and take value inside
        parenthese into an array, then call method to the cmd
        called
        """
        cmd = ['all', 'count', 'show', 'destroy', 'update']
        tokens = line.split('.', 1)
        if len(tokens) > 1 and tokens[1].split('(')[0] in cmd:
            method_cmd = tokens[1].split('(')[0]
            v = [p.split(')')[0] for p in tokens[1].split('(') if ')' in p]
            if len(v) > 0:
                tmp = v[0].split(", ")
            # Test below
            # d_string = str(tmp[1]) + " " + str(tmp[2])
            # string_d = d_string[1:-1].split(': ')
            # self.remove_quote(string_d)
            # print(dict(string_d))
            # test end
            self.remove_quote(tmp)
            class_name = tokens[0]
            if method_cmd == "all":
                self.do_all(class_name)
            elif method_cmd == "count":
                self.do_count(class_name)
            elif method_cmd == "show":
                self.do_show(class_name + " " + tmp[0])
            elif method_cmd == "destroy":
                self.do_destroy(class_name + " " + tmp[0])
            elif method_cmd == "update":
                if len(tmp) == 1 and type(tmp[0]) is dict:
                    self.do_update(class_name + " " + tmp[0])
                else:
                    s = self.check_and_concat_string_from_list(class_name, tmp)
                    self.do_update(s)
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_count(self, class_name):
        """ Count number of instance created for the
        class_name
        """
        counter_instance = 0
        if len(class_name) == 0 or len(class_name) == 2:
            print("** class name missing **")
        elif class_name in HBNBCommand.exist_class:
            for i in HBNBCommand.dict_obj:
                name_class = i.split('.')[0]
                if name_class == class_name:
                    counter_instance += 1
            print(counter_instance)
        else:
            print("** class doesn't exist **")

    def do_create(self, line):
        """ Create an instance """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.exist_class:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                obj = BaseModel()
                obj.save()
                print(obj.id)
            elif line == "User":
                user = User()
                user.save()
                print(user.id)
            elif line == "State":
                s = State()
                s.save()
                print(s.id)
            elif line == "City":
                c = City()
                c.save()
                print(c.id)
            elif line == "Amenity":
                a = Amenity()
                a.save()
                print(a.id)
            elif line == "Place":
                p = Place()
                p.save()
                print(p.id)
            elif line == "Review":
                r = Review()
                r.save()
                print(r.id)

    def do_all(self, line):
        """ Print all object from a class in a list """
        # HBNBCommand.obj.reload()
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
        "print(s)"
        if self.check_command(s):
            object_to_print = self.split(HBNBCommand.dict_obj, s[1])
            print(object_to_print)

    def do_update(self, line):
        """ Update or add attribute of the object (class name and id given)
            id, created_at and updated_at can't be updated
        """
        HBNBCommand.obj.reload()
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
                            vlue = s[3][1:-1]
                        elif s[3][0] == "'" and s[3][-1] == "'":
                            vlue = s[3][1:-1]
                        else:
                            vlue = s[3]
                        if s[0] == "Place":
                            vlue = self.check_attr_exist(Place, s[2], vlue)
                        elif s[0] == "BaseModel":
                            vlue = self.check_attr_exist(BaseModel, s[2], vlue)
                        elif s[0] == "User":
                            vlue = self.check_attr_exist(User, s[2], vlue)
                        elif s[0] == "City":
                            vlue = self.check_attr_exist(City, s[2], vlue)
                        elif s[0] == "State":
                            vlue = self.check_attr_exist(State, s[2], vlue)
                        elif s[0] == "Amenity":
                            vlue = self.check_attr_exist(Amenity, s[2], vlue)
                        elif s[0] == "Review":
                            vlue = self.check_attr_exist(Review, s[2], vlue)
                        setattr(HBNBCommand.dict_obj[i], s[2], vlue)
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
