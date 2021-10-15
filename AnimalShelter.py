import json
from typing import Collection
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo import *
from pymongo.results import DeleteResult
import json
from bson import json_util


class AnimalShelter():
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.username = username
        self.password = password
        #27017 41920
        self.client = MongoClient('mongodb://%s:%s@localhost:27017' % (self.username, self.password))


        #self.client = MongoClient("mongodb://localhost:27017")
        self.database = self.client["AAC"]
        self.collection = self.database["animals"]

        #self.test()

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.collection.insert(data)  # data should be dictionary
            return True
        else:
            # raise Exception("Nothing to save, because data parameter is empty")
            return False

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            results = self.collection.find(data, {'_id': False})
            return results
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")


    def update(self, filter, update):
        if filter and update is not None:
            data_result = self.collection.update_one(filter, update)
            return data_result
        else:
            raise Exception("Nothing to update, because data param is empty")

    def delete(self, data):
        if data is not None:
            self.collection.delete_one(data)
        else:
            raise Exception("Nothing to delete, because data parameter is empty")

