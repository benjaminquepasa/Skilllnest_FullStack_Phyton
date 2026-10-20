# Importar Flask y módulos necesarios
import os
from flask import Flask, redirect
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

# Cargar variables de entorno
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_KEY", "clave_por_defecto")
bcrypt = Bcrypt(app)

# Importar controladores con Blueprints
from flask_app.controllers.usuarios import usuarios_bp
from flask_app.controllers.entradas import entradas_bp

# Registrar los Blueprints en la app
app.register_blueprint(usuarios_bp)
app.register_blueprint(entradas_bp)

# Ruta de validación para rutas perdidas (Error 404)
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return redirect('/dashboard')