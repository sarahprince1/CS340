from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:53937' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:53937')
        self.database = self.client['project']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary 
            if insert!=0:
                return True
            else:
                return False           
        else:
            raise Exception("Nothing to save, because data parameter is empty")


    # Create method to implement the R in CRUD.
    def read(self,criteria=None):

        # If data applicable, it will return all rows which match criteria
        if criteria:
         # {'_id':False}, no ID will be placed in row(s)       
            
            data = self.database.animals.find(criteria,{"_id":False})
        else: 
            data = self.database.animals.find( {} , {"_id":False})

        return data
    
        # Create method to implement the C in CRUD
    def update(self, data, newData):
        if data is not None:
            return self.AAC.animals.update_one(data, {'$set': newData})

        else:
            print("Nothing to update, because data parameter is empty")
            return False

       
    # Create method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            return self.AAC.animals.delete_one(data)
            print("data deleted")
        else:
            return False
