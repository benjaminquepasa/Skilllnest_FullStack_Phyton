from flask import Flask

app = Flask(__name__)

@app.toute("/")
def inicio():
    return "<h1>¡Hola munco!</h1><p> Esto es un parrafo </p>"