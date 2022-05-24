# Agrega la libreria genera de pymongo
import pymongo
# Agrega la funxion de MongoClient desde pymongo
from pymongo import MongoClient
# Se crea la conexion con Mongodb
con = MongoClient('localhost', 27017)
# Selecciona la base de datos
db = con['santa_clara']


def FunctionSelect(tabla):
    # Creando de un query una lista para poder obtener la info
    resultados = list(tabla.find())
    # Print a variable resultados
    print(resultados)


def FunctionInsert(tabla, datos):
    # Selecciona la coleccion
    collection = db[tabla]
    # Preguntar si es una lista de datos o uno solo
    if type(datos) == list:
        collection.insert_many(datos)
    else:
        collection.insert_one(datos)
    # Llamar a la función select para imprimir resultados
    FunctionSelect(collection)


def FunctionUpdate(tabla, find, values):
    # Selecciona la coleccion
    collection = db[tabla]
    # Preguntar si es una lista de datos o uno solo

    new_values = {"$set": values}
    if type(find) == list:
        collection.update_many(find, new_values)
    else:
        collection.update_one(find, new_values)
    # Llamar a la función select para imprimir resultados
    FunctionSelect(collection)


find = {
    "nombre": "Paracetamol"
}

datos_producto = {
    "nombre": "Aspirina",
    "precio": 82
}

FunctionUpdate('productos', find, datos_producto)

datos_usuarios = [
    {
        'nombre': 'Rocio Salazar',
        'email': 'rociosalazar3457@gmail.com',
        'telefono': 6182612810,
        'direccion': {
            'calle': 'Valle Florido',
            'col_fracc': 'Valle del Mezquital',
            'num_ext': '109',
            'num_int': '',
            'municipio': 'Durango',
            'estado': 'Durango',
            'pais': 'México',
            'cp': '30162'
        },
        'edad': 20,
        'sexo': 'F',
        'password': 'quememiras',
        'token_de_pago': '1234567890987654321r'
    },
    {
        'nombre': 'Javier Salazar',
        'email': 'javieralejandrosalazartorres@gmail.com',
        'telefono': 6181535898,
        'direccion': {
            'calle': 'Juan E. Garcia',
            'col_fracc': 'Barrio de Tierra Blanca',
            'num_ext': '1129',
            'num_int': '',
            'municipio': 'Durango',
            'estado': 'Durango',
            'pais': 'México',
            'cp': '30139',
        },
        'edad': 21,
        'sexo': 'M',
        'password': 'quememiras',
        'token_de_pago': '1234567890987654321j'
    }
]

# find = {
#     "nombre": "Rocio Salazar"
# }

# datos_usuarios = {
#     "direccion.num_int": "24",
#     "direccion.cp": "34120",
#     "token_de_pago": "12345qe8fg98vb54sk21r"
# }

datos_producto = [
    {
        'lote': '25a5223',
        'nombre': 'Paracetamol',
        'desc': 'Medicamento para aliviar el dolor muscular',
        'precio': 32,
        'departamento': 'Analgésico',
        'receta': False,
        'stock': '2000',
        'descuento': 0
    },
    {
        'lote': '30a0332',
        'nombre': 'Amoxicilina',
        'desc': 'Medicamento para tratar algunas infecciones provocadas por bacterias',
        'precio': 110,
        'departamento': 'Antibiotico',
        'receta': True,
        'stock': 500,
        'descuento': 0
    }
]


# FunctionInsert('productos', datos_producto)
