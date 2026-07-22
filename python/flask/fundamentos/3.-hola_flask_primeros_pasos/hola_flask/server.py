from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route("/")          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
   return '!Hola a todos¡'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route("/nosotros")          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def nosotros():
   return '<h1>conocenos un poco mas </h1>'

#productos
@app.route("/productos")          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def productos():
   return 'compre una leche y 3 panes'

#contactos
@app.route("/contactos")          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def contactos():
   return 'tengo muchos contactos'

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente   
   app.run(debug=True)    # Ejecuta la aplicación en modo de depuración/debug para detectar cualquier cambio y recargarlo