from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Entrada:
    db = "querido_diario"
    
    def __init__(self, data):
        self.id = data['id']
        self.fecha_entrada = data['fecha_entrada']
        self.notas = data['notas']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creador = data.get('creador_nombre')

    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO entradas (fecha_entrada, notas, usuario_id) VALUES (%(fecha_entrada)s, %(notas)s, %(usuario_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def obtener_por_usuario(cls, usuario_id):
        query = "SELECT entradas.*, usuarios.nombre as creador_nombre FROM entradas JOIN usuarios ON entradas.usuario_id = usuarios.id WHERE usuarios.id = %(usuario_id)s ORDER BY entradas.fecha_entrada DESC;"
        resultados = connectToMySQL(cls.db).query_db(query, {'usuario_id': usuario_id})
        if not resultados:
            return []
        return [cls(fila) for fila in resultados]

    @classmethod
    def obtener_por_id(cls, id):
        query = "SELECT entradas.*, usuarios.nombre as creador_nombre FROM entradas JOIN usuarios ON entradas.usuario_id = usuarios.id WHERE entradas.id = %(id)s;"
        resultado = connectToMySQL(cls.db).query_db(query, {'id': id})
        if not resultado:
            return False
        return cls(resultado[0])

    @classmethod
    def buscar_por_termino(cls, termino, usuario_id):
        query = "SELECT entradas.*, usuarios.nombre as creador_nombre FROM entradas JOIN usuarios ON entradas.usuario_id = usuarios.id WHERE entradas.usuario_id = %(usuario_id)s AND entradas.notas LIKE %(termino)s ORDER BY entradas.fecha_entrada DESC;"
        data = {
            'usuario_id': usuario_id,
            'termino': f"%{termino}%"
        }
        resultados = connectToMySQL(cls.db).query_db(query, data)
        if not resultados:
            return []
        return [cls(fila) for fila in resultados]

    @classmethod
    def actualizar(cls, data):
        query = "UPDATE entradas SET fecha_entrada = %(fecha_entrada)s, notas = %(notas)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def eliminar(cls, id):
        query = "DELETE FROM entradas WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, {'id': id})

    @staticmethod
    def validar_entrada(formulario):
        es_valido = True
        if not formulario['fecha_entrada']:
            flash("Fecha Entrada no puede estar vacía.", "entrada")
            es_valido = False
        else:
            fecha_ingresada = datetime.strptime(formulario['fecha_entrada'], '%Y-%m-%d').date()
            if fecha_ingresada > datetime.now().date():
                flash("No puede ingresar una fecha en el futuro.", "entrada")
                es_valido = False
        if len(formulario['notas'].strip()) == 0:
            flash("Notas no puede estar vacía.", "entrada")
            es_valido = False
        return es_valido