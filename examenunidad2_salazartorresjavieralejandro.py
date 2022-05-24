from pymongo import MongoClient
from bson.objectid import ObjectId
con = MongoClient("localhost", 27017)
db = con['sistema_escolares']


# Función para traer datos desde la db
def FunctionSelect(tabla, buscar, tipo):
    collection = db[tabla]
    if tipo == 'one':
        resultados = collection.find_one(buscar)
    elif tipo == 'all':
        # Creando de un query una lista para poder obtener la info
        resultados = list(collection.find(buscar))
        # Print a variable resultados
    return resultados

def FunctionInsert(tabla, datos):
    collection = db[tabla]
    if type(datos) == list:
        collection.insert_many(datos)
    else:
        collection.insert_one(datos)

def FunctionUpdate(tabla, find, values):
    collection = db[tabla]
    new_values = {"$set": values}
    if type(find) == list:
        collection.update_many(find, new_values)
    else:
        collection.update_one(find, new_values)

def Trigger_kardex(buscar_alum, buscar_mat, calif):
    FunctionUpdate('calificaciones', buscar_mat, calif)
    collection = db['calificaciones']
    resultado = collection.find(buscar_alum)
    prom = 0
    for result in resultado:
        prom = result['calificacion'] + prom        
    promedio = prom / 2
    datos_promedio = {
        'promedio': promedio
    }
    FunctionUpdate('kardex', buscar_alum, datos_promedio)


# Trigger_kardex({'alumno_id': ObjectId('622676359daa6d619bd0f5a4')}, {'materia_id': ObjectId('622676e542bddcbda86f9306')}, {'calificacion': 90})
# print(FunctionSelect('kardex',{},'all'))
# print(FunctionSelect('calificaciones',{},'all'))

