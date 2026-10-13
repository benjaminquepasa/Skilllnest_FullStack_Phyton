from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    db = "tasktrack_db"
    
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, {"email": email})
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        if len(user['nombre']) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "register")
            is_valid = False
        if len(user['apellido']) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Email con formato inválido.", "register")
            is_valid = False
        else:
            if Usuario.get_by_email(user['email']):
                flash("El correo electrónico ya está registrado.", "register")
                is_valid = False
        if len(user['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "register")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Las contraseñas no coinciden.", "register")
            is_valid = False
        return is_valid