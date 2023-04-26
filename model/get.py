from db import GetConextion

def GetDatas():
    collection = GetConextion()
    collection.find()
