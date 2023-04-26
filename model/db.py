from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os
from dotenv import load_dotenv
load_dotenv()

uri = os.getenv('MONGO_URL')
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["MyDbGpt"]
collection = db["Gpt"]

def GetConextion():
    return collection




