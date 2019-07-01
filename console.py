#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Command Class """

    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        'Create command to create a new instance'
        if not arg:
            print("** class name missing **")
        elif arg == 'BaseModel':
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")


    def do_show(self, arg1, arg2):
        'Show command to show an existing instance.'
        if not arg1:
            print("** class name missing **")
        elif not arg2:
            print("** instance id missing **")


        else:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
