#!/usr/bin/python3
import cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Command Class """

    my_class = {"BaseModel" : BaseModel, "User" : User, "State" : State,
                "City" : City, "Amenity" : Amenity, "Place" : Place,
                "Review" : Review}
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
        my_class = {"BaseModel" : BaseModel, "User" : User, "State" : State,
                    "City" : City, "Amenity" : Amenity, "Place" : Place,
                    "Review" : Review}
        if not arg:
            print("** class name missing **")
        elif arg in self.my_class:
            for key, value in my_class.items():
                if key == arg:
                    new_instance = my_class[key]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")


    def do_show(self, arg):
        'Show command to show an existing instance.'
        my_arg = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif my_arg[0] not in self.my_class:
            print("** class doesn't exist **")
        elif len(my_arg) >= 1:
            try:
                my_objects = FileStorage.all(self)
                my_key = my_arg[0] + "." + my_arg[1]
                flag = 0
                for key, values in my_objects.items():
                    if key == my_key:
                        flag = 1
                        print(values)
                if flag == 0:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")


    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        my_arg = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif my_arg[0] not in self.my_class:
            print("** class doesn't exist **")
        elif len(my_arg) >= 1:
            try:
                my_objects = FileStorage.all(self)
                my_key = my_arg[0] + "." + my_arg[1]
                try:
                    my_objects.pop(my_key)
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            except IndexError:
                    print("** instance id missing **")

    def do_all(self, arg):
        'Show all instances based on class name.'
        my_arg = arg.split(" ")
        if not arg:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                my_list.append(str(values))
            print(my_list)
        elif my_arg[0] not in self.my_class:
            print("** class doesn't exist **")
        else:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                my_key = key.split(".")
                if my_key[0] == my_arg[0]:
                    my_list.append(str(values))
            print(my_list)

    def do_update(self, arg):
        'Update the instances based on class name and id.'
        my_arg = arg.split(" ")
        if len(my_arg) == 0:
            print("** class name missing **")
        elif len(my_arg) == 1:
            print("** instance id missing **")
        elif len(my_arg) == 2:
            print("** attribute name missing **")
        elif len(my_arg) == 3:
            print("** value missing **")
        elif my_arg[0] not in self.my_class:
            print("** class doesn't exist **")
        else:
            my_objects = FileStorage.all(self)
            my_key = my_arg[0] + "." + my_arg[1]
            try:
                for key, values in my_objects.items():
                    if key == my_key:
                        my_values = my_objects.get(key)
                        setattr(values, my_arg[2], my_arg[3])
                        values.save()
            except KeyError:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
