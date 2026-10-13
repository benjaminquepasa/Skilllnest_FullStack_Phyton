from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    db = "cine_pedia"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def obtener_por_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultado = connectToMySQL(cls.db).query_db(query, data)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])

    @staticmethod
    def validar_registro(formulario):
        is_valid = True
        if len(formulario['nombre']) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            is_valid = False
        if len(formulario['apellido']) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            is_valid = False
        if not EMAIL_REGEX.match(formulario['email']):
            flash("El email debe tener un formato válido.", "registro")
            is_valid = False
        else:
            usuario_existe = Usuario.obtener_por_email({'email': formulario['email']})
            if usuario_existe:
                flash("El email no puede repetirse en la BD.", "registro")
                is_valid = False
        if len(formulario['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            is_valid = False
        if formulario['password'] != formulario['confirm_password']:
            flash("Contraseña y Confirmación deben de ser iguales.", "registro")
            is_valid = False
        return is_valid