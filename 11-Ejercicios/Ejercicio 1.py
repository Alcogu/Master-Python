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

print("------------  Mostrar Longitud ------------")
""
print(f"La longitud es: ")
print(len(numeros))
""