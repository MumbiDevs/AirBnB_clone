#!/usr/bin/python3
"""
Entry point for the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
import shlex

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel}

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = shlex.split(arg)
        objects = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def help_quit(self):
        """Help information for the quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help information for the EOF command."""
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
