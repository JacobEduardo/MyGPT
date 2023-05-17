from models.db import GetCollection
from datetime import datetime
from bson.objectid import ObjectId
from gpt import GetResponseGpt

def UpdateDialogue(id, question, answer, collection):
    conversation = GetCollection(collection)
    question = question
    answer = answer.strip()
    myquery = {"_id": ObjectId(id)}
    newvalues = { "$push": {"dialogue": {"question": question, "answer": answer}}}
    conversation.update_one(myquery, newvalues)

def CreateDialogue(title, question, answer, collection, base, training, resume= "none"):
    answer = answer.strip()
    conversation = GetCollection(collection)
    new_dialigue = conversation.insert_one({
        "name":title,
        "dialogue":[{
            "question":question,
            "answer":answer
            }],
        "resume": resume,
        "base": base,
        "training": training,
        "data": datetime.now()
        })
    id = new_dialigue.inserted_id
    return id