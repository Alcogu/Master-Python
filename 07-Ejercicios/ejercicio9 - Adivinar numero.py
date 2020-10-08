"""
hacer un programa que pida numeros al usuario indefinidamente hasta que ingrese el 111
"""

contador = 1

while contador < 100:

    numero = int(input("Ingresa un numero e intenta adivinar el número secreto "))

    if numero == 111:
        print("¡¡¡Adivinaste!!!")
        break

    else:
        print("Sigue intentando ")