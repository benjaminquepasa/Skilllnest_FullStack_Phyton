# Importar conexión y herramientas de validación
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

# Expresión regular para validar formato de correo
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    db = "querido_diario"
    
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.edad = data['edad']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # Método para guardar un nuevo usuario
    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, edad, password) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(edad)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    # Método para buscar usuario por email
    @classmethod
    def obtener_por_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultado = connectToMySQL(cls.db).query_db(query, {'email': email})
        if not resultado:
            return False
        return cls(resultado[0])

    # Método para buscar usuario por ID
    @classmethod
    def obtener_por_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultado = connectToMySQL(cls.db).query_db(query, {'id': id})
        if not resultado:
            return False
        return cls(resultado[0])

    # Método estático para validar el formulario de registro
    @staticmethod
    def validar_registro(formulario):
        es_valido = True
        if len(formulario['nombre']) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            es_valido = False
        if len(formulario['apellido']) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            es_valido = False
        if not EMAIL_REGEX.match(formulario['email']):
            flash("El email debe tener un formato válido.", "registro")
            es_valido = False
        else:
            usuario_existente = Usuario.obtener_por_email(formulario['email'])
            if usuario_existente:
                flash("El email no puede repetirse en la BD.", "registro")
                es_valido = False
        if formulario['edad'] == "" or int(formulario['edad']) < 18:
            flash("Debe tener al menos 18 años.", "registro")
            es_valido = False
        if len(formulario['password']) < 8:
            flash("La contraseña debe ser la correspondiente a la BD (mínimo 8 caracteres).", "registro")
            es_valido = False
        if formulario['password'] != formulario['conf_password']:
            flash("Contraseña y Confirmación deben de ser iguales.", "registro")
            es_valido = False
        return es_valido