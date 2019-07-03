#!/usr/bin/python3
""" class review """
from models.base_model import BaseModel
from models.place import Place
from models.user import User

text = ""
user_id = ""
place_id = ""


class Review(BaseModel):
    """ Review class """
    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
