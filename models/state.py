#!/usr/bin/python3
""" class user """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    def __init__(self, *args, **kwargs):
        """ Init """
        name = ""

        super().__init__(*args, **kwargs)
