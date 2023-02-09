#!/usr/bin/python3

import json

class FileStorage:

	"""Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """	
    __file_path = "file.json"
    __objects = {}

   def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as file:
            file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, encoding="UTF-8") as file:
                FileStorage.__objects = json.loads(file.read())
        except FileNotFoundError:
            pass 
