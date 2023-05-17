from models.db import GetCollection
from datetime import datetime
from bson.objectid import ObjectId
from gpt import GetResponseGpt

def UpdateDialogue(id, question, answer, collection, resume):
    conversation = GetCollection(collection)
    question = question
    answer = answer
    myquery = {"_id": ObjectId(id)}
    newvalues = {
    "$push": {"dialogue": {"question": question, "answer": answer}},
    "$set": {"resume": resume}
}
    conversation.update_one(myquery, newvalues)

def CreateDialogue(title, question, answer, collection, base="", training="", resume=""):
    answer = answer
    conversation = GetCollection(collection)
    new_dialigue = conversation.insert_one({
        "name":title,
        "dialogue":[{
            "question":question,
            "answer":answer
            }],
        "resume": str(resume),
        "base": base,
        "training": training,
        "data": datetime.now()
        })
    id = new_dialigue.inserted_id
    print(base)
    return id