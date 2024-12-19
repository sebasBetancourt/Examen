

def getInt(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except Exception:
            print('Opcion Invalida, ingrese un valor valido.')


def pressEnter ():
    print ("Hecho")
    input('Press Enter...........................')