from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os
from dotenv import load_dotenv
load_dotenv()

uri = os.getenv('MONGO_URL')
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["MyDbGpt"]

def GetCollection(CollectionName): 
    if CollectionName in db.list_collection_names():
        return db[CollectionName]
    else:
        db.create_collection(CollectionName)
        return db[CollectionName]