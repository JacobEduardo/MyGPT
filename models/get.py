from .db import GetCollection
from bson.objectid import ObjectId

def GetConversations():
    collection = GetCollection()
    allconversations = list(collection.find())
    return allconversations

def GetConversation(id):
    collection = GetCollection()
    conversation = collection.find_one({"_id": ObjectId(id)})
    return conversation