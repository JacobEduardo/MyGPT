from .db import GetCollection
from bson.objectid import ObjectId

def GetConversationsInfo(collection):
    collection = GetCollection(collection)
    allconversations = list(collection.find({}, {"dialogue": 0 , "resume": 0}))
    return allconversations

def GetConversation(id,collection):
    collection = GetCollection(collection)
    conversation = collection.find_one({"_id": ObjectId(id)})
    return conversation
