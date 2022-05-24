from bson.objectid import ObjectId
from crud import *


def join(tabla, tablajoin, id):
    producto = FunctionSelect(tabla, {'_id': id}, 'one')
    oferta = FunctionSelect(tablajoin, {'producto_id': id}, 'one')

    oferta.update({'producto': producto})
    print(oferta)


join('productos', 'ofertas', ObjectId('6216aa833a8285013f79b80d'))
