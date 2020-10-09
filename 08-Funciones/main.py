"""
Una función es un conjunto de instrucciones agrupadas bajo un
mismo nombre que pueden reutilizarse llamando a la función
"""
print("---------Ejemplo 1---------")
"""
def muestraNombres():
    print("Alexander Correa Gutierrez")
    print("Alejando Correa Gutierrez")
    print("Pepito Perez")
    print("\n")

# Invocar Función

muestraNombres()
"""
print("---------Ejemplo 2---------")
"""
def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Eres mayor de edad")

nombre = input("Ingresa tu nombre ")
edad = int(input("¿Cual es tu edad? "))
mostrarTuNombre(nombre, edad)
"""
print("---------Ejemplo 3---------")
"""
def tablasDeMultiplicar(numero):
    print(f"Tabla de multiplicar del número {numero}")

    for contador in range(1, 11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

numero = int(input("¿Cual es el número de la tabla qué quieres ver? "))
tablasDeMultiplicar(numero)
"""
print("---------Ejemplo 4---------")
#Parametros opcionales
"""
def getEmpleado(nombre, id = False):
    print("Empleado")
    print(f"Nombre : {nombre}")

    if id != False:
        print(f"ID : {id}")

getEmpleado("Alex",12345)

"""
print("---------Ejemplo 5---------")
"""
#Parametros opcionales y return o devolver datos

def saludame(nombre):
    saludo = (f"Hola, saludos {nombre}")

    return saludo

print(saludame("Alex Correa"))
"""

print("---------Ejemplo 6---------")
"""
def calculadora(n1, n2, opc = False):

    suma = n1 + n2
    resta = n1 - n2
    multi = n1 * n2
    divi = n1/n2

    cadena="" #Se define vacia

    if opc !=False:

        cadena += ("Suma: " + str(suma))
        cadena += ("\n")
        cadena += ("Resta " + str(resta))
        cadena += ("\n")

    else:
        cadena += ("Multiplicacion " + str(multi))
        cadena += ("\n")
        cadena += ("División " + str(divi))

    return cadena

print(calculadora(10,2, True))
"""

print("---------Ejemplo 7---------")
"""
def getNombre(nombre):
    texto = (f"el nombre es: {nombre}")
    return texto

def getApellido(apellido):
    texto = (f"el apelido es: {apellido}")
    return texto

def devuelveAll(nombre, apellido):
    texto = (getNombre(nombre) + "\n" + getApellido(apellido))
    return texto

print(devuelveAll("Alexander", "Correa Gutiérrez"))
"""

print("---------Ejemplo 8---------")

# Funcion landa

año = lambda year: (f"El año es {year}")

