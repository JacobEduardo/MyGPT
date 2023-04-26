from db import GetConextion

def Post(documento):
    collection = GetConextion()
    documento = documento
    collection.insert_one(documento)
    print("estas aqui")
