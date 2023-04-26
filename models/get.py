from db import GetCollection

def GetConversations():
    collection = GetCollection()
    allconversations = list(collection.find())
    return allconversations

print( GetConversations() )