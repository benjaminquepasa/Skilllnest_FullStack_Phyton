import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @staticmethod
    def validar_usuario(usuario):
        es_valido = True
        if not usuario["nombre"]:
            flash("El nombre es obligatorio.", "nombre")
            es_valido = False
        if not usuario["apellido"]:
            flash("El apellido es obligatorio.", "apellido")
            es_valido = False
        if not usuario["email"]:
            flash("El email es obligatorio.", "email")
            es_valido = False
        elif not EMAIL_REGEX.match(usuario["email"]):
            flash("El email no tiene un formato válido.", "email")
            es_valido = False
        return es_valido
    @classmethod
    def get_all(cls):
        query = "SELECT id, nombre, apellido, email, created_at, updated_at FROM usuarios ORDER BY id DESC;"
        resultados = connectToMySQL("esquema_usuarios").query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT id, nombre, apellido, email, created_at, updated_at FROM usuarios WHERE id = %(id)s;"
        data = {"id": id}
        resultados = connectToMySQL("esquema_usuarios").query_db(query, data)
        if resultados:
            return cls(resultados[0])
        return None
    @classmethod
    def email_existe(cls, email):
        query = "SELECT id FROM usuarios WHERE email = %(email)s;"
        data = {"email": email}
        resultados = connectToMySQL("esquema_usuarios").query_db(query, data)
        return bool(resultados)
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s, %(email)s);"
        return connectToMySQL("esquema_usuarios").query_db(query, data)