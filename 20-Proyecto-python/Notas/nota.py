import Usuarios.conexion as conexion
import datetime

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):

        fecha = datetime.datetime.now()

        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, %s)"
        nota = (self.usuario_id, self.titulo, self.descripcion, fecha)

        try:
            cursor.execute(sql, nota) #ejecutar la consulta y los datos a sustituir
            database.commit() #ejecuta consultas y guardan los datos en la DB
            result = [cursor.rowcount, self] #devuelve lista con cantidad de registros que se modifican y el propio objeto
        except:
            result = [0, self]
        
        return result