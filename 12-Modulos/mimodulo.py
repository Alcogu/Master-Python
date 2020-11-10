
def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

def calculadora(n1, n2, opc = False):

    suma = n1 + n2
    resta = n1 - n2
    multi = n1 * n2
    divi = n1/n2

    cadena="" #Se define vacia

    if opc !=False:

        cadena += ("Suma: " + str(suma))
        cadena += ("\n")
        cadena += ("Resta " + str(resta))
        cadena += ("\n")

    else:
        cadena += ("Multiplicacion " + str(multi))
        cadena += ("\n")
        cadena += ("División " + str(divi))

    return cadena

#print(calculadora(10,2, True))