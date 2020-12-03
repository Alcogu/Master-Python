import mysql.connector
import datetime

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "master_python",
    port = 3306
)

#print(database) Validar conexion a la DB

cursor = database.cursor(buffered=True) #objeto que nos permitira hacer las consultas

class Usuario:

    def __init__(self, nombre, apellidos, email, password): #contructor = es el primer metodo que se ejecuta cuando se crea un objeto
        self.nombre = nombre #va a ser igual al parametro que ingrese el usuario
        self.apellidos = apellidos #va a ser igual al parametro que ingrese el usuario
        self.email = email #va a ser igual al parametro que ingrese el usuario
        self.password = password #va a ser igual al parametro que ingrese el usuario

    def registrar(self):

        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)

        cursor.execute(sql, usuario) #ejecutar la consulta y los datos a sustituir
        database.commit() #ejecuta consultas y guardan los datos en la DB

        return [cursor.rowcount, self] #devuelve lista con cantidad de registros que se modifican y el propio objeto

    def identificar(self):
        return self.nombre