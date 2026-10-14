# importancias y dependencias

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# clase modelo pelciula

class Pelicula:
    db = "cine_pedia"

    def __init__(self, data):
        self.id = data['id']
        self.nombre_peli = data['nombre_peli']
        self.director = data['director']
        self.fecha_estreno = data['fecha_estreno']
        self.sinopsis = data['sinopsis']
        self.usuario_id = data['usuario_id']
        self.creador = data.get('creador', '')

    # metodo para guardawr la pelicula
    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO peliculas (nombre_peli, director, fecha_estreno, sinopsis, usuario_id) VALUES (%(nombre_peli)s, %(director)s, %(fecha_estreno)s, %(sinopsis)s, %(usuario_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    # metodo para obtener todas las peliculas

    @classmethod
    def obtener_todas(cls):
        query = "SELECT peliculas.*, CONCAT(usuarios.nombre, ' ', usuarios.apellido) as creador FROM peliculas JOIN usuarios ON peliculas.usuario_id = usuarios.id;"
        resultados = connectToMySQL(cls.db).query_db(query)
        return [cls(p) for p in resultados]

    # metodo para obtener la pelicula por id
    @classmethod
    def obtener_por_id(cls, data):
        query = "SELECT peliculas.*, CONCAT(usuarios.nombre, ' ', usuarios.apellido) as creador FROM peliculas JOIN usuarios ON peliculas.usuario_id = usuarios.id WHERE peliculas.id = %(id)s;"
        resultado = connectToMySQL(cls.db).query_db(query, data)
        if resultado:
            return cls(resultado[0])
        return None

    # metodo para actualizar la pelicula
    @classmethod
    def actualizar(cls, data):
        query = "UPDATE peliculas SET nombre_peli = %(nombre_peli)s, director = %(director)s, fecha_estreno = %(fecha_estreno)s, sinopsis = %(sinopsis)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    # metodo para eliminar la pelicula
    @classmethod
    def eliminar(cls, data):
        query = "DELETE FROM peliculas WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    # validacion de formulario de la pelicula
    @staticmethod
    def validar_pelicula(formulario):
        is_valid = True
        if len(formulario['nombre_peli']) < 3:
            flash("El nombre de la película debe tener al menos 3 caracteres.", "pelicula")
            is_valid = False
        if len(formulario['director']) < 3:
            flash("El director debe tener al menos 3 caracteres.", "pelicula")
            is_valid = False
        if not formulario['fecha_estreno']:
            flash("Fecha de Estreno no puede estar vacía.", "pelicula")
            is_valid = False
        if len(formulario['sinopsis']) < 3:
            flash("Sinopsis no puede estar vacía.", "pelicula")
            is_valid = False
        return is_valid