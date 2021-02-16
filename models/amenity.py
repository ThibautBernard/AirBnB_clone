#!/usr/bin/python3
from models.base_model import BaseModel
"""
    Class that represent about Amenity
"""


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
