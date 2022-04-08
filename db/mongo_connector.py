from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017"
    
    client = MongoClient(CONNECTION_STRING)
    
    return client['blockservice_py']

