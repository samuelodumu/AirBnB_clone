#!/usr/bin/python3
"""Contains `BaseModel` class"""

import uuid

class BaseModel:
    """defines all common attributes/methods for other classes"""
    id = str(uuid.uuid4())

    created_at = 
    updated_at = 

    def __str__(self):
        """string representation"""
        return f"[{class.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates `updated_at` attribute with the current datetime"""
        BaseModel.updated_at = 
        return BaseModel.updated_at
