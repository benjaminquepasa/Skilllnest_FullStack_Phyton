from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Categoria:
    db = "tasktrack_db"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.user_id = data['user_id']
        self.cantidad_tareas = data.get('cantidad_tareas', 0)

    @classmethod
    def get_all_by_user(cls, user_id):
        query = """
            SELECT c.id, c.nombre, c.user_id, 
            (SELECT COUNT(t.id) FROM tasks t WHERE t.category_id = c.id) as cantidad_tareas 
            FROM categories c 
            WHERE c.user_id = %(user_id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, {"user_id": user_id})
        return [cls(row) for row in results] if results else []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO categories (nombre, user_id, created_at, updated_at) VALUES (%(nombre)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_id(cls, category_id):
        query = "SELECT * FROM categories WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, {"id": category_id})
        return cls(result[0]) if result else False

    @classmethod
    def delete(cls, category_id):
        query = "DELETE FROM categories WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, {"id": category_id})

    @staticmethod
    def validate_category(data, user_id):
        is_valid = True
        if len(data['nombre']) < 3:
            flash("El nombre debe tener al menos 3 caracteres.", "category")
            is_valid = False
            print("Error validación: Nombre muy corto (< 3 caracteres)")
            
        query = "SELECT * FROM categories WHERE nombre = %(nombre)s AND user_id = %(user_id)s;"
        result = connectToMySQL(Categoria.db).query_db(query, {"nombre": data['nombre'], "user_id": user_id})
        if result:
            flash("El nombre de la categoría ya existe.", "category")
            is_valid = False
            print("Error validación: La categoría ya existe para este usuario")
            
        return is_valid