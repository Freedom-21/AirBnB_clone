#!/usr/bin/python3
"""
Console module
Contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):

    """Command interpreter class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show an instance based on class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]
            key = f"{class_name}.{instance_id}"
            try:
                instance = storage.all()[key]
                print(instance)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance based on class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]
            key = f"{class_name}.{instance_id}"
            try:
                del storage.all()[key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all instances, or all instances of a class"""
        if not arg:
            for obj in storage.all().values():
                print(obj)
        else:
            try:
                eval(arg)  # Check if class exists
                for obj in storage.all().values():
                    if obj.__class__.__name__ == arg:
                        print(obj)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        args = arg.split()
        if len(args) < 3:
            print("** class name missing **" if len(args) == 0 else
                  "** instance id missing **" if len(args) == 1 else
                  "** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            class_name, instance_id, attribute_name, attribute_value\
                = args[0], args[1], args[2], args[3]
            key = f"{class_name}.{instance_id}"
            try:
                instance = storage.all()[key]
                setattr(instance, attribute_name, attribute_value.strip('"'))
                instance.save()
            except KeyError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
