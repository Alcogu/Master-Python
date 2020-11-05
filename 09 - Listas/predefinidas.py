cantantes = ['Freddy Mercuri' , 'Gustavo Cerati' , 'Michael Jackson' , 'Steven Tyler']
numeros = [1, 2, 5, 8, 3, 4]

#Ordenar una lista
#print(numeros)
numeros.sort()
#print(numeros)

#Agregar Elementos a una lista

cantantes.append('Bon Jovi')
cantantes.insert(1, 'Sting')

#print(cantantes)

#Eliminar Elementos

cantantes.pop(0)
cantantes.remove('Bon Jovi')
#print(cantantes)

#dar la vuelta

#print(numeros)
numeros.reverse()
#print(numeros)

#Buscar dentro de una lista

#print('Gustavo Cerati' in cantantes)

#Contar Elementos

#print(cantantes)
#print(len(cantantes))

#Cuantas veces aparece un elemento

#print(numeros.count(8))

#Conseguir indice

#print(cantantes.index("Michael Jackson"))

#Unir Listas

cantantes.extend(numeros)

print(cantantes)