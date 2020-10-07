"""
cont = 0
resultado = 0

for cont in range(0, 10):
    print("Voy por el "+ str(cont))

    resultado += cont
print(f"El resultado es {resultado}")
"""
# Ejemplo

num = int(input("Ingrese el numero a multiplicar:"))
cont = 0

for cont in range (1, 11):
    print(f" {num} x {cont} = {cont*num}")
else:
    print("Terminamos")