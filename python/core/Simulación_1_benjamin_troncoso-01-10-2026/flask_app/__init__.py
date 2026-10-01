import os
from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

# Cargamos las variables de entorno definidas en el archivo .env
load_dotenv()

# Inicializamos la aplicación principal de Flask
app = Flask(__name__)

# Definimos la clave secreta utilizada para cifrar y proteger las sesiones del usuario
app.secret_key = os.getenv("SECRET_KEY", "clave_secreta_bookhub_secure")

# Inicializamos Bcrypt para realizar el hash y verificación segura de contraseñas
bcrypt = Bcrypt(app)

# Obtenemos el nombre de la base de datos desde las variables de entorno
DATABASE = os.getenv("DB_NAME", "bookhub_schema")