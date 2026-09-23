from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, row):
        self.id = row["id"]
        self.nombre = row["nombre"]
        self.apellido = row["apellido"]
        self.email = row["email"]
        self.created_at = row["created_at"]
        self.updated_at = row["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios ORDER BY id ASC;"
        resultados = connectToMySQL("esquema_usuarios").query_db(query)
        return [cls(row) for row in resultados] if resultados else []

    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = {"id": user_id}
        resultado = connectToMySQL("esquema_usuarios").query_db(query, data)
        return cls(resultado[0]) if resultado else None

    @classmethod
    def save(cls, form_data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        return connectToMySQL("esquema_usuarios").query_db(query, form_data)

    @classmethod
    def update(cls, form_data):
        query = """
            UPDATE usuarios
            SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL("esquema_usuarios").query_db(query, form_data)

    @classmethod
    def delete(cls, user_id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        data = {"id": user_id}
        return connectToMySQL("esquema_usuarios").query_db(query, data)