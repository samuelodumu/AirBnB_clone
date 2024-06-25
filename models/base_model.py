#!/usr/bin/python3
"""Contains `BaseModel` class"""

import datetime
import json
import uuid

class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """Initializing instance ids"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates `updated_at` attribute with the current datetime"""
        self.updated_at = datetime.datetime.now()
        return self.updated_at

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        instance_dict_rep = self.__dict__.copy()
        instance_dict_rep["created_at"] = datetime.datetime.isoformat(self.created_at)
        instance_dict_rep["updated_at"] = datetime.datetime.isoformat(self.updated_at)
        instance_dict_rep["__class__"] = self.__class__.__name__
        return instance_dict_rep
