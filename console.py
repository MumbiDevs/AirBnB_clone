#!/usr/bin/python3
"""
Command interpreter for AirBnB clone project.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        # Add other classes here if implemented
    }

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[args_list[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on class name and id."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = f"{args_list[0]}.{args_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = f"{args_list[0]}.{args_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        objects = storage.all()
        if args:
            if args not in self.classes:
                print("** class doesn't exist **")
                return
            objs_list = [str(obj) for key, obj in objects.items() if args in key]
        else:
            objs_list = [str(obj) for obj in objects.values()]
        print(objs_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = f"{args_list[0]}.{args_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        if len(args_list) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args_list[2]
        attr_value = args_list[3].strip('"')
        try:
            if '.' in attr_value:
                attr_value = float(attr_value)
            else:
                attr_value = int(attr_value)
        except ValueError:
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_EOF(self, line):
        """Handles EOF to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
