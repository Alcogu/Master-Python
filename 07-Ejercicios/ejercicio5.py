#EJercicio 5
"""
Mostrar todos los numeros entre dos numeros que muestre el usuario
"""
v1 = int(input("Por favor ingrese el primer dato "))
v2 = int(input("Por favor ingrese el segundo dato "))

if v1 < v2:

    for cont in range(v1, (v2+1)):

        print(cont)

else:
    print("¡¡¡Cuidado!!!")
    print("El primer valor debe ser menor al segundo")