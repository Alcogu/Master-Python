from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

    return "<h1>Página de contacto</h1>"

@app.route('/lenguajes-de-programacion/')
def lenguajes():
    return "<h1>Página de lenguajes</h1>"

if __name__ == '__main__':
    app.run(debug=True)