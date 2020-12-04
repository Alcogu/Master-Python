import mysql.connector

def conectar():

    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "master_python",
        port = 3306
    )

#print(database) Validar conexion a la DB

#objeto que nos permitira hacer las consultas
    cursor = database.cursor(buffered=True)

    #devuelve la base de datos y el cursor para importaciones
    return [database, cursor]