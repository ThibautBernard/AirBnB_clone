#!/usr/bin/python3
from models.base_model import BaseModel
"""
    Class that represent a Review
"""


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    # def __init__(self, **kwargs):
    #    super().__init__(kwargs)
