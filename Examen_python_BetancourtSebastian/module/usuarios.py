from module.DatosJSON import *

def usuarios():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    for usuario in datos['usuarios']:
        print('Paials')