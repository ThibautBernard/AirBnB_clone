#!/usr/bin/python3
from models.base_model import BaseModel
"""
    Class that represent a city
"""


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
