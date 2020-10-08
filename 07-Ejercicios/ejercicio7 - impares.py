"""
mostar los números impares entre dos numeros que de el cliente
"""
v1 = int(input("Elija un valor "))
v2 = int (input("Elija un segundo valor "))

if v1 < v2:
    for cont in range (v1, (v2+1)):
        if cont%2 != 0:
            print(f"{cont} es impar ")
        else:
            print(f"{cont} es par ")
else:
    print("El primer valor debe ser inferior al segundo")