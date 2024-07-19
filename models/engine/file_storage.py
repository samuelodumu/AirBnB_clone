#!/usr/bin/python3
"""contains `FileStorage` class"""

import json
import os


class FileStorage:
    """serializes instances to a JSON file and deserializes a
    JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects if __file_path exists"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)

                except json.JSONDecodeError:
                    return
                for key, value in FileStorage.__objects.items():
                    class_name = key.split(".")[0]
                    obj = globals()[class_name](**obj_dict[key])
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
