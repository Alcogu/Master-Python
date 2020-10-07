#condicional IF
"""
Comparacion

== igual
!= diferente
< menor que
> mayor que


color = "rojo"

if color == "rojo":
    print("El color es rojo")

else:
    print("El color no es rojo")

print("------------Ejemplo2--------------")

year = int(input("¿en qué año estamos?"))

if year >= 2021:
    print("Ya paso el 2020")

else:
    print("No a pasado el 2020")
"""

# IF anidados
"""
nombre = "Alexander"
ciudad = "Pereira"
continente = "America"
edad = 27
mEdad = 18

if edad >= mEdad:
    print(f"{nombre} si es mayor de edad")

    if ciudad == "Pereira":
        print(f"{nombre} es Colombiano")
    else:
        print(f"{nombre} no es Colombiano")

else:
    print(f"{nombre} no es mayor de edad")
    """

#Elif
"""
dia = int(input("¿Qué día es:?"))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("es fin de semana")
    """

#Ejemplo 5
"""
edadMinima = 18
edadMaxima = 65
edad = int(input("¿Cuantos años tienes?"))

if edad > 18 & edad < 65:
    print("Tiene buena edad para trabajar")

else:
    print("No tiene edad para trabajar")
"""
#ejemplo 6
"""
pais = "Alemania"

if pais == "Mexico" or pais == "Colombia" or pais == "España":
    print(f"{pais} es un pais de habla hispana")

else:
    print(f"{pais} no es un pais de habla hispana")
"""
#ejemplo 7
"""
pais = "España"

if not (pais == "Mexico" or pais == "Colombia" or pais == "España"):
    print(f"{pais} no es un pais de habla hispana")

else:
    print(f"{pais}  es un pais de habla hispana")
    """

    #Ejemplo 8 

pais = "Colombia"

if pais != "Mexico" or pais == "Colombia" or pais != "España":
    print(f"{pais} es un pais de habla hispana")

else:
    print(f"{pais} no es un pais de habla hispana")