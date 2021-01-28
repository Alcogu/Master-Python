from flask import Flask, redirect, url_for, render_template, request,flash
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'clave_secreta_flask'

#Conexion DB

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)

#Context procesors

@app.context_processor
def date_now():
    return{
        'now': datetime.utcnow()
    }

#Endpoints

@app.route('/')
def index():

    edad = 18
    personas = ['Alex', 'Alexito', 'Alexander']

    return render_template('index.html',
                            edad=edad,
                            dato1="Valor",
                            dato2="Valor2",
                            lista=["uno", "dos", "tres"],
                            personas=personas
                            )

@app.route('/informacion/')
@app.route('/informacion/<string:nombre>/')
def informacion(nombre = None):

    texto = ""
    if nombre != None:
        texto = f"Bienvenido, {nombre}"

    return render_template('informacion.html', texto=texto)

@app.route('/contacto/')
@app.route('/contacto/<redireccion>/')
def contacto(redireccion=None):

    if redireccion is not None:
        return redirect(url_for('lenguajes'))

    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion/')
def lenguajes():
    return render_template('lenguajes.html')

@app.route('/crear-coche/', methods=['GET', 'POST'])
def crear_coche():
    if request.method == 'POST':

        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL, %s, %s, %s, %s)", (marca, modelo, precio, ciudad))
        cursor.connection.commit()

        flash('Has creado un registro de coche')

        return redirect(url_for('index'))

    return render_template('crear_coche.html')

@app.route('/coches/')
def coches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches")
    coches = cursor.fetchall()
    cursor.close()

    return render_template('coches.html', coches=coches)

@app.route('/coche/<coche_id>/')
def coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coches = cursor.fetchall()
    cursor.close()

    return render_template('coche.html', coche=coche[0])

@app.route('/borrar-coche/<coche_id>/')
def borrar_coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM coches WHERE id = {coche_id}")
    mysql.connection.commit()

    flash('El coche ha sido eliminado')

    return redirect(url_for('coches'))

@app.route('/editar-coche/<coche_id>/', methods=['GET', 'POST'])
def editar_coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coches = cursor.fetchall()
    cursor.close()

    return render_template('crear_coche.html', coche=coche[0])

if __name__ == '__main__':
    app.run(debug=True)