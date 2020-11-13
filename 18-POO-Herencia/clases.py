#Posibilidad de compartir atributos y metodos entre clases

class persona:
    """
    nombre
    apellidos
    altura
    edad
    """

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellidos(self,apellidos):
        self.apellidos = apellidos

    def setEdad(self,edad):
        self.edad = edad

    def setAltura(self,altura):
        self.altura = altura

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"

class Informatico(Persona):

print("HOlaaaa")
