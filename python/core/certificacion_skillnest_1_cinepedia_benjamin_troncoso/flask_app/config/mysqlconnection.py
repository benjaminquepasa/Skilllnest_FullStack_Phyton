import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()

class MySQLConnection:
    def __init__(self, db):
        self.db = os.getenv("DB_NAME", db)
        connection = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "1234"),
            database=self.db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query_stripped = query.strip().lower()
                query_mogrified = cursor.mogrify(query, data)
                print("--- SQL QUERY ---:", query_mogrified)
                cursor.execute(query, data)
                if query_stripped.startswith("insert"):
                    return cursor.lastrowid
                elif query_stripped.startswith("select"):
                    return cursor.fetchall()
                else:
                    return cursor.rowcount
            except Exception as e:
                print("❌ ERROR EN MYSQL:", e)
                return False

def connectToMySQL(db):
    return MySQLConnection(db)