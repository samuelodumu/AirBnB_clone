#!/usr/bin/python3
"""Contains `BaseModel` class"""

import datetime as dt
import json
import uuid


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """Initializing instance ids"""
        self.id = str(uuid.uuid4())
        self.created_at = dt.datetime.now()
        self.updated_at = dt.datetime.now()

    def __str__(self):
        """string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates `updated_at` attribute with the current datetime"""
        self.updated_at = dt.datetime.now()
        return self.updated_at

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        instance_dict_rep = self.__dict__.copy()
        instance_dict_rep["created_at"] = self.created_at.isoformat()
        instance_dict_rep["updated_at"] = self.updated_at.isoformat()
        instance_dict_rep["__class__"] = self.__class__.__name__
        return instance_dict_rep
