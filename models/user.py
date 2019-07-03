#!/usr/bin/python3
""" class user """
from models.base_model import BaseModel

email = ""
password = ""
first_name = ""
last_name = ""


class User(BaseModel):
    """ User class """
    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
