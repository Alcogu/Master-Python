#POO - Programación Orienteda a Objetos
#Definir la clase

class Coche:

    #Atributos o propiedades (Variables en progra funcional)
    #Caracteristicas del objeto
    color = "Verde"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Metodos, Acciones que hace el objeto(Funciones en progra funucional)
    #Self accede a las propiedades de la clase

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self): 
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

#Fin definicion clase
#Crear objetos / Instanciar clase

coche = Coche()

print("COCHE 1: ")

coche.setColor("Azul")
coche.setModelo("Cacas")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print("Velocidad actual: ", coche.getVelocidad())

print("----------------------------------------")
#Crear mas objetos

coche2 = Coche()

coche2.setColor("Marron")
coche2.setModelo("Pichirilo")


print("COCHE 2: ")
print(coche2.marca, coche2.getModelo(), coche.getColor())