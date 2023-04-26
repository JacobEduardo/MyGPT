from models.db import GetCollection

def Post(documento):
    collection = GetCollection()
    documento = documento
    collection.insert_one(documento)
    print("estas aqui")
