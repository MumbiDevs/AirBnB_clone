#!/usr/bin/python3
"""
Entry point for the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = '(hbnb) '  # Custom prompt

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
