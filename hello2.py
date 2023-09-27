from flask import Flask
from flask_script import Manager #usamos manager de flask_script
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hola Lucero</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/suma/<int:numero>')
def suma(numero):
    numero3= numero+numero
    return '<h1>La suma es, %s</h1>' % numero3

if __name__ == '__main__':
    manager.run()
#dicen que flask-script esta desfazado
#a mi me daba muchos errores
#cambie flask._compat por flask_script._compat en __init__ de flask-script del venv