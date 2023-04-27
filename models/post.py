from models.db import GetCollection
from datetime import datetime
from bson.objectid import ObjectId

def Post(documento):
    collection = GetCollection()
    documento = documento
    collection.insert_one(documento)

def UpdateDialogue(id, question, answer):
    conversation = GetCollection()
    question = question
    answer = answer.strip()
    myquery = {"_id": ObjectId(id)}
    newvalues = { "$push": {"dialogue": {"question": question, "answer": answer}}}
    conversation.update_one(myquery, newvalues)
    print("Esta es la conversacion:")
    print(conversation, question, "y la respuesta es;" , answer)

def CreateDialogue(title, question, answer):
    answer = answer.strip()
    conversation = GetCollection()
    new_dialigue = conversation.insert_one({
        "name":title,
        "dialogue":[{
            "question":question,
            "answer":answer
            }],
        "resume":"este es un resumen",
        "data": datetime.now()
        })
    print("Esta es la conversacion:",new_dialigue)
    id = new_dialigue.inserted_id
    return id