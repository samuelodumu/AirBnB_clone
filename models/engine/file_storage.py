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
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_data = {}
        # turn each object to its JSON representation
        for key in self.__objects:
            # print(f'key: {key}, value: {self.__objects[key]}')
            json_data[key] = self.__objects[key].to_dict()
        # print(json_data)

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects if __file_path exists"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                except json.JSONDecodeError:
                    return

                for key, value in obj_dict.items():
                    # extract the class name
                    class_name = key.split(".")[0]
                    # instantiate the object by calling the constructor
                    # globals()[class_name] will evaluate to BaseModel
                    obj = globals()[class_name](**value)
                    # store the object
                    FileStorage.__objects[key] = obj

                    # another way to do it if BaseModel or whatever class_name
                    # is is not listed in the globals() dictionary
                    # if 'BaseModel' in key:
                    #     FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            return
