from pymongo import MongoClient

block_schema = {
    'hash': 'string',
    'blockNum': {
        'type': 'int',
        'unique': True,
        'required': True,
        'index': True
    },
    'blockInfo': 'object'
}

def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017"
    
    client = MongoClient(CONNECTION_STRING)
    
    return client['blockservice_py']

