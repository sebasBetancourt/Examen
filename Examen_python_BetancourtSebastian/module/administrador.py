from funciones.funciones import *
from menssaje.menssaje import *
from module.DatosJSON import *


#COMPLETADO-------------------------------------------------
def createUser():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    cedula = getInt('Ingrese cedula del nuevo Usuario :')
    cedula = str(cedula)
    nombre = input('Escriba el nombre del usuario :')
    contacto = getInt('Escriba su numero de Telefono :')
    contacto = str(contacto)

    user = {
        "nombre": nombre,
        "contacto": contacto,
        "cedula": cedula,
        "cliente": {
            "nuevo": True,
            "regular": False,
            "leal": False
        },
        "servicio": "",
        "mensajes": {
            "consultas": "",
            "reclamaciones": "",
            "sugerencias": ""
        }
    }

    datos['usuarios'].append(user)
    guardarArchivo(RUTA_BASE_DATOS, datos)
    pressEnter()
#----------------------------------------------------------------------

def viewUser():
    datos = abrirArchivo(RUTA_BASE_DATOS)
    cedula = getInt('Escriba cedula del usuario :')
    cedula = str(cedula)
    encontrado = False
    for usuario in datos['usuarios']:
        if cedula == usuario["cedula"]:
            encontrado = True
            print(menuVerUsuario)
            opcion = getInt(':)')
            match opcion:
                case 1:
                    for servicios in datos['servicios']:
                        print(f'{servicios["servicio"]}')
                    op = input('¿Que servicio desseas agregarle al usuario? .')
                    if servicios["servicio"] == op:
                        usuario["servicio"] = op
                        pressEnter()
                    else:
                        print('El servicio que ingresaste no existe')
                case 2:
                    print(f'Nombre: {usuario["nombre"]}')
                    print(f'Contacto: {usuario["contacto"]}')
                    print(f'Cedula: {usuario["cedula"]}')
                    if usuario['cliente']["nuevo"] == True:
                        print(f'Cliente: Nuevo')
                    elif usuario['cliente']["regular"] == True:
                        print(f'Cliente: Corriente')
                    elif usuario['cliente']["leal"] == True:
                        print(f'Cliente: Leal')
                    print(f'Servicio: {usuario["servicio"]}')
                    pressEnter()
                case 3:
                    for estado in usuario['cliente']:
                        print(f'{estado}')
                    op = input('¿Que estado desseas cambiar :')
                    if usuario["cliente"] == op:
                        estado["cliente"] = True
                        pressEnter()
                    else:
                        print('El estado que ingresaste no existe')

                case 4:
                    for mensajes in usuario['mensajes']:
                        print(f'{mensajes}')
                    pressEnter()
                case 5:
                    if usuario['serivicio'] != "":
                        for servicios in datos['servicios']:
                            if usuario['servicio'] == servicios:
                                print(f'{servicios["promociones"]}')
                                pressEnter()

                    else:
                        print('Todavia no tiene servicio')
                    #Personalizacion de servicio
                    pass
                case 6:
                    #bonificacion
                    pass
                case 7:
                    break
                case _:
                    print('Opcion Invalida')


    if not encontrado:
        print('El usuario no existe!!!')
    guardarArchivo(RUTA_BASE_DATOS, datos)




def editUser():

    pass

def deleteUser():

    pass


#OPCION 1------------------------------------------------
def user():
    while True:
        print(menuUsuarios)
        opcion  = getInt(':)')
        pressEnter()
        match opcion:
            case 1:
                createUser()
                #Ya          
            case 2:
                viewUser()
                #Falta
            case 3:
                editUser()
                #Falta
            case 4:
                deleteUser()
                #Falta
            case 5:
                break
            case _:
                print('Ingresa una opcion valida')

#OPCION 2---------------------------------------
def servicios():

    pass

#OPCION 3-----------------------------------
def reportes():

    pass


#ADMIN-.......................................................
def administrador():
    while True:
        print(menuAdministrador)
        opcion  = getInt(':)')
        pressEnter()
        match opcion:
            case 1:
                user()
                pass
            case 2:
                servicios()
                pass
            case 3:
                reportes()
                pass
            case 4:
                break
            case _:
                print('Ingresa una opcion valida')

    