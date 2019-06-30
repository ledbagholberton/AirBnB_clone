#!usr/bin/python3
""" class file_storage """
import json

class FileStorage:
    """ Clase file Storage"""

    __file_path = "my_file.json"
    __objects = {}

    def __init__(self):
        """ Init """
        pass

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict.update({key: value.to_dict()})
        json_file = json.dumps(new_dict)
        with open(FileStorage.__file_path, "w") as my_file:
            my_file.write(json_file)

    def reload(self):
        json_file = ""
        try:
            with open(FileStorage.__file_path, "r") as my_file:
                json_file = my_file.read()
                FileStorage.__objects = json.loads(json_file)
        except:
            pass
