import mysql.connector

#Conexion

database = mysql.connector.connect(#Metodo
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

#¿cómo saber si la conexión fue exitosa?
#print(database)

cursor = database.cursor()#hacer consultar por el cursor

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:#COmprobar bases de datos creadas
    print(bd)