import os
from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave_secreta_bookhub_secure")
bcrypt = Bcrypt(app)

DATABASE = os.getenv("DB_NAME", "bookhub_schema")