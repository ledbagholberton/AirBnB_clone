#!/user/bin/python3
from datetime import datetime
from uuid import uuid4
from models.__init__ import storage

class BaseModel:
    """ BaseModel for AirBnB project """
    def __init__(self, *args, **kwargs):
        """ Init method """
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = kwargs.get(key)
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f')
                if key == "my_number":
                    self.my_number = kwargs.get(key)
                if key == "name":
                    self.name = kwargs.get(key)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ __str__ """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Update the update_at """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary """
        my_dict = self.__dict__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return(my_dict)
