from db import GetConextion

def InsertData():
    collection = GetConextion()
    documento = {"nombre": "Pedro", "edad": 30}
    collection.insert_one(documento)
    print("estas aqui")
