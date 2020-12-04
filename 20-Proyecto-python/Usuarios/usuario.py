import datetime
import hashlib
import Usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]#0 es donde se tiene la bd
cursor = connect[1]#1 es donde se tiene el indice

class Usuario:

    def __init__(self, nombre, apellidos, email, password): #contructor = es el primer metodo que se ejecuta cuando se crea un objeto
        self.nombre = nombre #va a ser igual al parametro que ingrese el usuario
        self.apellidos = apellidos #va a ser igual al parametro que ingrese el usuario
        self.email = email #va a ser igual al parametro que ingrese el usuario
        self.password = password #va a ser igual al parametro que ingrese el usuario

    def registrar(self):

        fecha = datetime.datetime.now()
        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))#pasan un dato apra que lo cifre
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:

            cursor.execute(sql, usuario) #ejecutar la consulta y los datos a sustituir
            database.commit() #ejecuta consultas y guardan los datos en la DB
            result = [cursor.rowcount, self] #devuelve lista con cantidad de registros que se modifican y el propio objeto
        except:
            result = [0, self]
        

        return result

    def identificar(self):

        #comprobar que exista el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        #Cifrar contraseña
        cifrado = hashlib.sha256()
        #pasan un dato apra que lo cifre
        cifrado.update(self.password.encode('utf8'))

        #datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result