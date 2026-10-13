from flask_app.config.mysqlconnection import connectToMySQL

class Categoria:
    db = "cine_pedia"
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']