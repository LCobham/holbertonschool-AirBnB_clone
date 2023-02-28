#!/usr/bin/python3
"""
    This module defines the console to add / delete / modify
    users and perform other backend functions on the AirBnB
    clone.
"""

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import cmd
import sys


intro = """
            -----------------------------------------
            |       Welcome to the hbtn CLI.        |
            |       For help, input 'help'          |
            |       To quit, type 'quit'            |
            -----------------------------------------
    """


class HBNBCommand(cmd.Cmd):
    """
        Class for the AirBnB Clone command line interpreter.
    """

    prompt = "(hbnb) "
    doc_header = "Documented commands (type help <topic>):"

    cls_dict = {"BaseModel": BaseModel, "User": User,
                "Amenity": Amenity, "City": City,
                "Place": Place, "Review": Review,
                "State": State}

    error_msg = {
        'no_class': "** class name missing **",
        'wrong_class': "** class doesn't exist **",
        'no_id': "** instance id missing **",
        'wrong_id': "** no instance found **",
        'no_attr': "** attribute name missing **",
        'no_value': "** value missing **"
    }

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """
            Quit command to exit the program
            Syntax: (hbtn) quit
        """
        sys.exit()

    def do_EOF(self, arg):
        """
            Quit command to exit the program
            Syntax: `Ctrl + D`
            Or: (hbtn) EOF
        """
        sys.exit()

    def do_create(self, arg):
        """
            Creates a new instance of a given class, saves it to file.json
            and prints the id of the newly created instance.
            Syntax: (hbtn) create <class name>
        """
        argv = parse(arg)
        if len(argv) == 0:
            print(HBNBCommand.error_msg["no_class"])

        elif argv[0] not in HBNBCommand.cls_dict.keys():
            print(HBNBCommand.error_msg["wrong_class"])

        else:
            new = HBNBCommand.cls_dict[argv[0]]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """
            Display the string representation of a model with a specific ID.
            Syntax: (hbtn) show <class name> <id>
        """
        argv = parse(arg)
        if len(argv) == 0:
            print(HBNBCommand.error_msg["no_class"])
        elif argv[0] not in HBNBCommand.cls_dict.keys():
            print(HBNBCommand.error_msg["wrong_class"])
        elif len(argv) < 2:
            print(HBNBCommand.error_msg["no_id"])
        else:
            current_objs = storage.all()
            key = argv[0] + "." + argv[1]
            obj = current_objs.get(key)
            if obj is None:
                print(HBNBCommand.error_msg["wrong_id"])
            else:
                print(obj)

    def do_destroy(self, arg):
        """
            Destroys an instance of a a given model.
            Syntax: (hbtn) destroy <class name> <id>
        """
        argv = parse(arg)
        if len(argv) == 0:
            print(HBNBCommand.error_msg["no_class"])
        elif argv[0] not in HBNBCommand.cls_dict.keys():
            print(HBNBCommand.error_msg["wrong_class"])
        elif len(argv) < 2:
            print(HBNBCommand.error_msg["no_id"])
        else:
            current_objs = storage.all()
            key = argv[0] + '.' + argv[1]
            if current_objs.get(key) is None:
                print(HBNBCommand.error_msg["wrong_id"])
            else:
                del current_objs[key]
                storage.save()

    def do_all(self, arg):
        """
            Prints all instances of a given class.
            If no arguments are given, prints every instance.
            Syntax: all <class name>
        """
        argv = parse(arg)
        current_objs = storage.all()
        li = []

        if len(argv) == 0:
            for key in current_objs.keys():
                li.append(str(current_objs.get(key)))
            print(li)

        elif argv[0] in HBNBCommand.cls_dict.keys():
            for key, value in current_objs.items():
                if type(value).__name__ == argv[0]:
                    li.append(str(current_objs.get(key)))
            print(li)

        else:
            print(HBNBCommand.error_msg["wrong_class"])

    def do_update(self, arg):
        """
            Updates an instance of a model (adds an attribute).
            Syntax: (hbtn) update <class name> <id> <attr name> <attr value>
        """
        argv = parse(arg)
        length = len(argv)
        if length == 0:
            print(HBNBCommand.error_msg["no_class"])

        elif argv[0] not in HBNBCommand.cls_dict.keys():
            print(HBNBCommand.error_msg["wrong_class"])

        elif length < 2:
            print(HBNBCommand.error_msg["no_id"])

        else:
            current_objs = storage.all()
            key = argv[0] + '.' + argv[1]
            if current_objs.get(key) is None:
                print(HBNBCommand.error_msg["wrong_id"])

            else:
                if length < 3:
                    print(HBNBCommand.error_msg["no_attr"])

                elif length < 4:
                    print(HBNBCommand.error_msg["no_value"])

                else:
                    obj = current_objs.get(key)
                    setattr(obj, argv[2], argv[3])
                    obj.save()


def parse(arg):
    return tuple(arg.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
