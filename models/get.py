from .db import GetCollection
from bson.objectid import ObjectId

def GetConversationsInfo():
    collection = GetCollection("Gpt")
    allconversations = list(collection.find({}, {"dialogue": 0 , "resume": 0}))
    return allconversations

def GetConversation(id):
    collection = GetCollection("Gpt")
    conversation = collection.find_one({"_id": ObjectId(id)})
    return conversation

def GetAdaConversations():
    collection = GetCollection("Ada")
    allconversations = list(collection.find({}, {"dialogue": 0 , "resume": 0}))
    return allconversations

def GetAdaConversation(id):
        collection = GetCollection("Ada")
        conversation = collection.find_one({"_id": ObjectId(id)})
        return conversation
