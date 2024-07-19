#!/usr/bin/python3
"""contains `FileStorage` class"""
import json
import os
from models.base_model import BaseModel


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
        existing_data = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    pass
                FileStorage.__objects.update(existing_data)

        else:
            FileStorage.__objects.update(existing_data)

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)
            # print(f"Type of existing_data: {type(existing_data)}")

    def reload(self):
        """deserializes the JSON file to __objects if __file_path exists"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                except json.JSONDecodeError:
                    return

                for key, value in obj_dict.items():
                    class_name = key.split(".")[0]
                    obj = globals()[class_name](**value)
                    FileStorage.__objects[key] = obj

                    # another way to do it if BaseModel or whatever class_name
                    # is is not listed in the globals() dictionary.
                    # if 'BaseModel' in key:
                    #     FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            return
