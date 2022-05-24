import datetime
import pandas as pd
# Agrega la función de MongoClient desde pymongo
from pymongo import MongoClient
# Se crea la conexión con MongoDB
con = MongoClient("localhost", 27017)
db = con['sta_clara']


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
    # print(FunctionSelect(collection, {}, 'all'))
    SaveLogs(tabla, 'insert')

def FunctionUpdate(tabla, find, values):
    collection = db[tabla]
    new_values = {"$set": values}
    if type(find) == list:
        collection.update_many(find, new_values)
    else:
        collection.update_one(find, new_values)
    print(FunctionSelect(collection, {}, 'all'))
    SaveLogs(tabla, 'update')

def FunctionDelete(tabla, datos):
    if type(datos) == list:
        tabla.delete_many(datos)
    else:
        tabla.delete_one(datos)
    print(FunctionSelect(tabla, {}, 'all'))


def Trigger_ofertas(buscar, precio):
    # Actualizar el producto por nombre y cambiar precio
    FunctionUpdate('productos', buscar, precio)
    # Seleccionamos la coleccion
    collection = db['productos']
    # Busca en la coleccion por nombre para traer un elemento
    resultado = collection.find_one(buscar)
    # Verficacion para no duplicar dos ofertas del mismo producto
    collection_ofertas = db['ofertas']
    resultado_oferta = collection_ofertas.find_one(
        {"producto_id": resultado['_id']})

    if resultado_oferta == None:
        # Declaramos el documento que se guarde en ofertas
        datos_ofertas = {
            'producto_id': resultado['_id'],
            'precio': resultado['precio']
        }
        FunctionInsert('ofertas', datos_ofertas)
    else:
        print("Ya existe está oferta")

# current_time = datetime.datetime.now().strftime


def SaveLogs(table, action):
    current_time = datetime.datetime.now()
    collection = db['logs']
    data_logs = {
        'action': action,
        'date': current_time,
        'table': table
    }
    collection.insert_one(data_logs)


def FunctionExport(tabla, action):
    if action == 'one':
        collection = db[tabla]
        datos = list(collection.find())
        df = pd.DataFrame(datos)
        df.to_csv(tabla+'.csv', index=False)
        df.to_excel(tabla+'.xlsx', index=False)
    else:
        collections = db.list_collection_names()
        for dato in collections:
            collection = db[dato]
            datos = list(collection.find())
            df = pd.DataFrame(datos)
            df.to_csv(tabla+'.csv', index=False)
            df.to_excel(tabla+'.xlsx', index=False)


def exportar_datos(formato):
    # Obtener todos los nombres de las colecciones
    lista_collect = db.list_collection_names()
    for name in lista_collect:
        collection = db[name]
        datos = list(collection.find())
        df = pd.DataFrame(datos)

        if formato == 'CSV':
            df.to_csv(name + '.csv', index=False)
        elif formato == 'XLSX':
            df.to_excel(name + '.xlsx', index=False)
