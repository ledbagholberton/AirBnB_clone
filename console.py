#!/usr/bin/python3
import cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ Command Class """

    prompt = '(hbnb) '
    file = None
    my_class = ['BaseModel', 'User', 'Place', 'Review', 'Amenity', 'State', 'City']

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
        elif arg in self.my_class:
            new_instance = BaseModel()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")


    def do_show(self, arg):
        'Show command to show an existing instance.'
        my_arg = arg.split(" ")
        if len(my_arg) == 0:
            print("** class name missing **")
        elif len(my_arg) == 1:
            print("** instance id missing **")
        elif my_arg[0] not in self.my_class:
            print("** class doesn't exist **")
        elif len(my_arg) >= 2:
            my_objects = FileStorage.all(self)
            my_key = my_arg[0] + "." + my_arg[1]
            flag = 0
            for key, values in my_objects.items():
                if key == my_key:
                    flag = 1
                    print(values)
            if flag == 0:
                print("** no instance found **")


    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        my_arg = arg.split(" ")
        if len(my_arg) == 0:
            print("** class name missing **")
        elif len(my_arg) == 1:
            print("** instance id missing **")
        elif my_arg[0] not in self.my_class:
            print("** class doesn't exist **")
        elif len(my_arg) >= 2:
            my_objects = FileStorage.all(self)
            my_key = my_arg[0] + "." + my_arg[1]
            flag = 0
            try:
                my_objects.pop(my_key)
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        'Show all instances based on class name.'
        my_arg = arg.split(" ")
        if len(my_arg) == 0:
            print("** class name missing **")
        elif my_arg[0] not in self.my_class:
            print("** class doesn't exist **")
        else:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
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
#                        setattr(values, 'updated_at', datetime.now())
                        values.save()
                        print ("______", values)

            except KeyError:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
