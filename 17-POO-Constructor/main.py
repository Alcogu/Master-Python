from coche import Coche

carro = Coche("Rojo", "Mazada", "2010", 152, 200)
carro1 = Coche("Amarillo", "Cacas", "AAA", 152, 200)
carro2 = Coche("Azul", "Mazada", "2014", 168, 170)
carro3 = Coche("Marron", "Mazada", "2015", 200, 180)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#Visibilidad

print(carro.soypublico)
print(carro.getPrivado())