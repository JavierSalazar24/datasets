# Agrega la función de MongoClient desde pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
# Se crea la conexión con MongoDB
con = MongoClient("localhost", 27017)
db = con['escolares']
collection = db['prealumnos']


def FunctionSelect(tabla):
    resultados = list(tabla.find())
    print(resultados)


def FunctionInsert(tabla, datos):
    if type(datos) == list:
        tabla.insert_many(datos)
    else:
        tabla.insert_one(datos)
    FunctionSelect(tabla)


def FunctionDelete(tabla, datos):
    if type(datos) == list:
        tabla.delete_many(datos)
    else:
        tabla.delete_one(datos)
    FunctionSelect(tabla)


datos = {
    '_id': ObjectId("6214aabe4e67234ba75d0534"),
    '_id': ObjectId("6210705295e5b90c532f711f")
}

FunctionDelete(collection, datos)
