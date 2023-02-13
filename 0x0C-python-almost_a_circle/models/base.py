#!/usr/bin/python3
import json
"""base class"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base class with id and increment the class attribute
        nb_objects if id is not passed"""
        if not id:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Accepts list of dictionaries and returns JSON string"""
        if not list_dictionaries:
            """convert objects to dictionaries and add to list"""
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """create a list to store dictionaries of objects"""
        list_obj_dicts = []
        if list_objs is not None:
            """ # if list of objects is not empty"""
            for obj in list_objs:
                """ convert objects to dictionaries and add to list"""
                list_obj_dicts.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as file:
            """ open a file with the name of the class
            and write the json string to it"""
            file.write(cls.to_json_string(list_obj_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Accepts a JSON string and returns a list of dictionaries"""
        if not json_string:
            """if json string is empty, return empty list"""
            json_string = '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Accepts a dictionary and returns an instance of the class
        with attributes set according to the dictionary"""
        if cls.__name__ == 'Rectangle':
            """ create a dummy object of class 'Rectangle' or 'Square'"""
            dummy = cls(1, 1)
        else:
            """update the dummy object with values from dictionary"""
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances of the class
        by reading the .json file of the class name"""
        instances = []
        try:
            """read the json string from file"""
            with open(cls.__name__ + ".json", "r") as file:
                """ convert json string to list of dictionaries"""
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                for obj_dict in list_dicts:
                    """ create object for each dictionary and add to list"""
                    instances.append(cls.create(**obj_dict))
        except FileNotFoundError:
            """return empty list if file not found"""
            return []
        return instances
