"""
Crear un scrip que tenga 4 variables, una lista, un string,
un entero y un booleano y que imprima un mensaje segun el
tipo de dato de cada variable
"""

def traductor(tipo):
    result = None
    if tipo == list:
        result ="Lista"
    elif tipo == str:
        result = "Cadena de texto"
    elif tipo == int:
        result = "Numero entero"
    elif tipo == bool:
        result = "Booleano"

    return result

def comprobar(dato, tipo):

    test = isinstance(dato, tipo)

    if test:
        print(f"El dato es tipo {traductor(tipo)}")
    else:
        print("El resultado no es correcto")


lista = ["Holi Holi"]
texto = "Nalgas de amorcito"
numero = 100
opcion = True

comprobar(lista, list)
comprobar(texto, str)
comprobar(numero, int)
comprobar(opcion, bool)