from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DATABASE
from flask import flash

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.genre = data['genre']
        self.publication_date = data['publication_date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posted_by = data.get('posted_by')
        self.favorites_count = data.get('favorites_count', 0)

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, author, genre, publication_date, description, user_id, created_at, updated_at) VALUES (%(title)s, %(author)s, %(genre)s, %(publication_date)s, %(description)s, %(user_id)s, NOW(), NOW());"
        return connect_to_mysql(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """
            SELECT books.*, users.first_name as posted_by, 
            (SELECT COUNT(*) FROM favorites WHERE favorites.book_id = books.id) as favorites_count 
            FROM books JOIN users ON books.user_id = users.id;
        """
        results = connect_to_mysql(DATABASE).query_db(query)
        books = []
        if results:
            for row in results:
                books.append(cls(row))
        return books

    @classmethod
    def get_by_id(cls, data):
        query = """
            SELECT books.*, users.first_name as posted_by, 
            (SELECT COUNT(*) FROM favorites WHERE favorites.book_id = books.id) as favorites_count 
            FROM books JOIN users ON books.user_id = users.id WHERE books.id = %(id)s;
        """
        result = connect_to_mysql(DATABASE).query_db(query, data)
        if not result:
            return None
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE books SET title = %(title)s, author = %(author)s, genre = %(genre)s, publication_date = %(publication_date)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s;"
        return connect_to_mysql(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM books WHERE id = %(id)s;"
        return connect_to_mysql(DATABASE).query_db(query, data)

    @classmethod
    def add_to_favorites(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) VALUES (%(user_id)s, %(book_id)s);"
        return connect_to_mysql(DATABASE).query_db(query, data)

    @classmethod
    def get_favorites_by_user(cls, data):
        query = """
            SELECT books.*, users.first_name as posted_by, 
            (SELECT COUNT(*) FROM favorites WHERE favorites.book_id = books.id) as favorites_count 
            FROM books JOIN favorites ON books.id = favorites.book_id JOIN users ON books.user_id = users.id WHERE favorites.user_id = %(user_id)s;
        """
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return [cls(row) for row in results] if results else []

    @classmethod
    def get_users_who_favorited(cls, data):
        query = "SELECT users.id, users.first_name, users.last_name FROM users JOIN favorites ON users.id = favorites.user_id WHERE favorites.book_id = %(book_id)s;"
        return connect_to_mysql(DATABASE).query_db(query, data)

    @staticmethod
    def validate_book(book):
        is_valid = True
        if len(book['title']) < 2:
            flash("El título debe tener al menos 2 caracteres.", "book")
            is_valid = False
        if len(book['author']) < 2:
            flash("El autor es obligatorio y debe tener al menos 2 caracteres.", "book")
            is_valid = False
        if not book['genre']:
            flash("Debe seleccionar un género.", "book")
            is_valid = False
        if not book['publication_date']:
            flash("La fecha de publicación es obligatoria.", "book")
            is_valid = False
        if len(book['description']) < 10:
            flash("La descripción debe tener al menos 10 caracteres.", "book")
            is_valid = False
        return is_valid