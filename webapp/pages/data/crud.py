from webapp import client
from bson.json_util import dumps

class AnimalShelter(object):
    '''AnimalShelter database access class. Provides access to the database upon instantiation. 
    Represents methods for basic create, read, update, and delete operations'''
    
    def __init__(self):
        
        # Connect to MongoClient upon object initialization
        self.client = client
        if self.client:
            print("Successfully connected")
        else:
            raise Exception("Unable to Connect")
        
        # Connect to AAC database
        self.database = self.client['AAC']
        
        if self.database is not None:
            print("Records found")
        else:
            raise Exception("Error connecting to database")
        
        # Access the animals collection
        self.collection = self.database['animals']
    
    def create(self, data):
        '''Add a new animal to the collection'''
        if data is not None:
            new_entry = self.collection.insert_one(data)
            if new_entry is not None:
                print('Success')
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save because data parameter is empty")
        
    def read(self, query=None):
        '''
        Retrieve animals from the collection.
        If query parameter is provided, retrieve only the documents that match the query parameter.
        If no query parameter is provided, retrieve all the documents.
        '''
        if query is not None:
            all_animals = self.collection.find(query, {"_id": 0})
            return all_animals
        else:
            all_animals = self.collection.find({"_id": 0})
        
    
    def update(self, query, data):
        '''
        Updates an existing animal document if the animal is in the collection.
        If the document is not in the collection, the update method will add the
        document to the collection as a new document.
        '''
        if query is not None:
            result = self.collection.find_one(query)
            updated_rec = self.collection.update_one(query, {"$set": data})
            new_record = self.collection.find_one(data)
            return new_record
        else:
            raise Exception("No record to update")
        
    def delete(self, data):
        '''Remove an animal from the collection.'''
        if data is not None:
            deleted_rec = self.collection.delete_one(data)
            return dumps(self.read(data))
        else:
            raise Exception("Nothing to delete because data parameter is empty")
        

        
