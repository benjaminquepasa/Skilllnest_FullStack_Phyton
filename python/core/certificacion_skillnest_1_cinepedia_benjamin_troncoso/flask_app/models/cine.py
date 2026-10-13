from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Tarea:
    db = "tasktrack_db"

    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.descripcion = data['descripcion']
        self.prioridad = data['prioridad']
        self.estado = data['estado']
        self.fecha_limite = data['fecha_limite']
        self.user_id = data['user_id']
        self.category_id = data['category_id']
        self.categoria_nombre = data.get('categoria_nombre', '')
        self.dias_restantes = data.get('dias_restantes', None)

    @classmethod
    def get_all_by_user(cls, user_id, filtros=None):
        query = """
            SELECT t.*, c.nombre as categoria_nombre 
            FROM tasks t 
            JOIN categories c ON t.category_id = c.id 
            WHERE t.user_id = %(user_id)s
        """
        data = {"user_id": user_id}
        if filtros:
            if filtros.get('estado') and filtros['estado'] != 'Todos':
                query += " AND t.estado = %(estado)s"
                data['estado'] = filtros['estado']
            if filtros.get('prioridad') and filtros['prioridad'] != 'Todas':
                query += " AND t.prioridad = %(prioridad)s"
                data['prioridad'] = filtros['prioridad']
            if filtros.get('busqueda'):
                query += " AND t.titulo LIKE %(busqueda)s"
                data['busqueda'] = f"%{filtros['busqueda']}%"
        query += " ORDER BY t.fecha_limite ASC;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return [cls(row) for row in results] if results else []

    @classmethod
    def get_upcoming_by_user(cls, user_id):
        query = """
            SELECT t.*, DATEDIFF(t.fecha_limite, NOW()) as dias_restantes 
            FROM tasks t 
            WHERE t.user_id = %(user_id)s AND t.estado != 'Completada' AND t.fecha_limite >= CURDATE()
            ORDER BY t.fecha_limite ASC LIMIT 5;
        """
        results = connectToMySQL(cls.db).query_db(query, {"user_id": user_id})
        return [cls(row) for row in results] if results else []

    @classmethod
    def get_resumen_by_user(cls, user_id):
        query = """
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN estado = 'Pendiente' THEN 1 ELSE 0 END) as pendientes,
                SUM(CASE WHEN estado = 'En progreso' THEN 1 ELSE 0 END) as en_progreso,
                SUM(CASE WHEN estado = 'Completada' THEN 1 ELSE 0 END) as completadas
            FROM tasks WHERE user_id = %(user_id)s;
        """
        result = connectToMySQL(cls.db).query_db(query, {"user_id": user_id})
        return result[0] if result else {}

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO tasks (titulo, descripcion, prioridad, estado, fecha_limite, user_id, category_id, created_at, updated_at) 
            VALUES (%(titulo)s, %(descripcion)s, %(prioridad)s, %(estado)s, %(fecha_limite)s, %(user_id)s, %(category_id)s, NOW(), NOW());
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_id(cls, task_id):
        query = """
            SELECT t.*, c.nombre as categoria_nombre 
            FROM tasks t 
            JOIN categories c ON t.category_id = c.id 
            WHERE t.id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query, {"id": task_id})
        return cls(result[0]) if result else False

    @classmethod
    def update(cls, data):
        query = """
            UPDATE tasks SET titulo = %(titulo)s, descripcion = %(descripcion)s, 
            prioridad = %(prioridad)s, estado = %(estado)s, fecha_limite = %(fecha_limite)s, 
            category_id = %(category_id)s, updated_at = NOW() WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update_estado(cls, task_id, estado):
        query = "UPDATE tasks SET estado = %(estado)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, {"id": task_id, "estado": estado})

    @classmethod
    def delete(cls, task_id):
        query = "DELETE FROM tasks WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, {"id": task_id})

    @staticmethod
    def validate_task(data):
        is_valid = True
        if len(data['titulo']) < 3:
            flash("El título debe tener al menos 3 caracteres.", "task")
            is_valid = False
        if len(data['descripcion']) < 10:
            flash("La descripción debe tener al menos 10 caracteres.", "task")
            is_valid = False
        return is_valid