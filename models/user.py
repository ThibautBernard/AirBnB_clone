#!/usr/bin/python3
from models.base_model import BaseModel
"""
    class that represent an User
"""


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
