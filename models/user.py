#!/usr/bin/python3
from models.base_model import BaseModel
"""
    class that represent an User
"""


class User(BaseModel):
    """
    Class User that does a lot of things
    Email: email of user
    password: pwd of user
    first_name: first_name of the user
    last_name: last_name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()
