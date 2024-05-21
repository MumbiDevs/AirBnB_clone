#!/usr/bin/python3

""" Console Module """

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.actor import Actor
from models.movie import Movie
from models.genre import Genre


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand Class """
    prompt = "(hbnb) "

    class_name = ["User", "BaseModel", "Actor",
                  "Review", "Movie", "Genre"]

    def do_quit(self, arg):
        """ quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        print()
        return True

    def emptyline(self):
        """ emptyline method """
        pass

    def do_create(self, arg):
        """ create method """
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            inst = eval(args[0])()
            inst.save()
            print(inst.id)
        except NameError:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """ show method """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.class_name:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """ destroy method """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.class_name:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        storage.all().pop(key)
        storage.save()

    def do_all(self, arg):
        """ all method """
        if not arg:
            print([str(v) for v in storage.all().values()])
            return
        args = arg.split()
        if args[0] not in self.class_name:
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in storage.all().items() if args[0] in k])

    def do_update(self, arg):
        """ update method """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.class_name:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}". format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            value = int(args[3])
        except ValueError:
            try:
                value = float(args[3])
            except ValueError:
                value = args[3]
        if isinstance(value, str):
            value = value.replace("_", " ")
            value = value[1:-1]
        setattr(storage.all()[key], args[2], value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
