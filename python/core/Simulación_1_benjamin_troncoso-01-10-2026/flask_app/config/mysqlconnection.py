import os
import pymysql.cursors
from dotenv import load_dotenv

# Cargamos las credenciales desde el entorno
load_dotenv()

class MySQLConnection:
    def __init__(self, db):
        # Establecemos la conexión con el servidor MySQL local
        connection = pymysql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', '1234'),
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor, # Retorna los datos organizados como diccionarios de Python
            autocommit=True
        )
        self.connection = connection

    def query_db(self, query, data=None):
        """ Método encargado de ejecutar consultas SQL (SELECT, INSERT, UPDATE, DELETE) """
        with self.connection.cursor() as cursor:
            try:
                print("Ejecutando consulta:", query, data)
                cursor.execute(query, data)
                
                # Si la consulta es un INSERT, retornamos el ID del último registro insertado
                if query.strip().lower().startswith("insert"):
                    return cursor.lastrowid
                
                # Si la consulta es un SELECT, retornamos todos los registros encontrados
                elif query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                else:
                    return None
            except Exception as e:
                print("Error en la consulta SQL:", e)
                return False
            finally:
                self.connection.close()

def connect_to_mysql(db):
    """ Función auxiliar para instanciar la conexión a la base de datos """
    return MySQLConnection(db)