import os
from flask import Flask
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_KEY", "clave_por_defecto")
bcrypt = Bcrypt(app)