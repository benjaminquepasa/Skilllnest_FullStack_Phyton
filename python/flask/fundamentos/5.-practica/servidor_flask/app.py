from flask import Flask

app = Flask(__name__)
 
@app.route('/')
def inicio():
    return "<h1>¡Bienvenido a mi servidor Flask!</h1><p>Usa las rutas para interactuar.</p>"

@app.route('/info')
def info():
    return "Esta es una página estática con información del servidor."
 
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f"¡Hola, {nombre}! Qué bueno tenerte por aquí."

@app.route('/repetir/<mensaje>/<int:cantidad>')
def repetir_mensaje(mensaje, cantidad):

    resultado = f"{mensaje} " * cantidad
    return f"<h3>Resultado:</h3><p>{resultado}</p>"
 

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "<h2>Lo sentimos, esta ruta no existe. ¡Vuelve al inicio!</h2>", 404
 

if __name__ == "__main__":
    app.run(debug=True)