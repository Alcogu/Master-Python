class Coche:

    #Atributos o propiedades (Variables en progra funcional)
    #Caracteristicas del objeto
    color = "Verde"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    def __init__(self, color, marca, modelo, velocidad, caballaje):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje

    #Metodos, Acciones que hace el objeto(Funciones en progra funucional)
    #Self accede a las propiedades de la clase

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

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

    def getInfo(self):

        info =  "------Informacion del Carro------"
        info += "\n Color " + self.getColor()
        info += "\n Marca " + self.getMarca()
        info += "\n Modelo " + self.getModelo()
        info += "\n velocidad " + str(self.getVelocidad())
        
        return info


#Fin definicion clase