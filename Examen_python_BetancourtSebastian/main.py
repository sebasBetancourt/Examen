from funciones.funciones import *
from menssaje.menssaje import *
from module.administrador import *
from module.usuarios import *

while True:
    print(menuPrincipal)

    opcion = getInt('Ingrese una opcion :')
    pressEnter()
    match opcion:
        case 1:
            usuarios()
        case 2:
            administrador()
        case 3:
            break
        case _:
            print('Opcion Invalida')


    
baseDatos = abrirArchivo(RUTA_BASE_DATOS)