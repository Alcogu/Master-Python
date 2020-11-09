"""
Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y mostrar la lista
Plus: usar While y for
"""

numero = []
"""
for contador in range(0,120):
    numero.append(f"Elemento - {contador}")
    print("mostar el: " + numero[contador])
"""
contador = 0

while contador < 120:
    numero.append(f"Elemento - {contador}")
    print("Mostrando el: " + numero[contador])
    contador += 1