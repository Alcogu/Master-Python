#capturar excepciones y manejar errores
#en codigo suceptible a fallos
"""
try:
    nombre = input("Cual es tu nombre? ")

    if len(nombre) > 1:
        nusuario = "El nombre es " + nombre

    print(nusuario)

except:
    print("A ocurrido un error, ingresa el nombre")

else:
    print("Todo salio bien")

finally:
    print("¡¡¡Fin de la iteración!!!")
"""

#Multiples excepciones

"""
try:
    numero = int(input("Digita un numero para elevarlo al cuadrado "))
    print("El cuadrado es: " +str (numero * numero))

except TypeError:
    print("Debes convertir las cadenas a enteros")
except ValueError:
    print("Introduce un valor conrrecto(Numerico)")
"""

#Excepsiones personalizadas
try:
    nombre = input("Ingresa nombre ")
    edad = int(input("Ingresa la edad "))

    if edad < 5 or edad >110:
        raise ValueError ("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError ("EL nombre no es correcto")
    else:
        print(f"Bienvenido al Master en Python {nombre}")

except ValueError:
    print("Ingresa los datos correctos")

except Exception as e:
    print("Existe un error: ", e)