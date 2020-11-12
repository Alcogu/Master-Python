"""
Hacer una lista con 8 enteros
    Recorrerla y mostrar
        (harcerla en una funcion)
    Ordenarla y mostrarla
    Longitud
    Mostrar un elemento que se pida
"""
numeros = [2, 4, 6, 8, 1, 3, 5, 7]

#Recorrer y mostrar

"""
print("------------ Recorrer y mostrar ------------")

for numero in numeros:
    print(numero)
"""

#Crear Funcion que recorra la lista y devuelva string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += str(elemento)
        resultado += "\n"


    return resultado
"""
print("------------ Recorrer y mostrar ------------")

print(mostrarLista(numeros))
"""

#Ordenar y mostrar
"""
print("------------ Ordenar y Mostrar ------------")


numeros.sort()

print(mostrarLista(numeros))
"""
"""
print("------------  Mostrar Longitud ------------")

print(f"La longitud es: ")
print(len(numeros))
"""

print("------------  Busqueda en la lista ------------")

try:

    busqueda = int(input("ingresa un número "))

    comprobar = isinstance(busqueda, int) #verifica que si sea un entero

    while not comprobar or busqueda <= 0:
        busqueda = int(input("ingresa un número"))
    else:
        print(f"Has introducido el {busqueda}")

    print(f"------------  Busqueda en la lista el número {busqueda} ------------")

except:
    print("Ingresa un numero")
    
try:
    search = numeros.index(busqueda) #Index busca en la lista
    print(f"EL número buscando existe en la lista, es el indice {search}")

except:
    print("EL número no esta en la lista, lo siento")