#!/usr/bin/python3
""" class review """
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """ Review class """
    def __init__(self, *args, **kwargs):
        """ Init """
        text = ""
        user_id = ""
        place_id = ""

        super().__init__(*args, **kwargs)
