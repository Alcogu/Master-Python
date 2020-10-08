"""
sacar porcentaje de un número
"""
numero = int(input("Ingrese el número al cual le desea sacar un porcentaje "))
porcentaje = int(input("¿Qué valor porcentual le quiere sacar al primer valor? "))
operacion = ((numero/100)*porcentaje)

print(f"el {porcentaje}% de {numero} es {operacion}")