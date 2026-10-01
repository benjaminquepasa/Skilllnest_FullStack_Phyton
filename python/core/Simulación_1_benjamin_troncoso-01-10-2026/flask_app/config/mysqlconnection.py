import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', '1234'),
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                print("Running Query:", query, data)
                cursor.execute(query, data)
                if query.strip().lower().startswith("insert"):
                    return cursor.lastrowid
                elif query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                else:
                    return None
            except Exception as e:
                print("Something went wrong:", e)
                return False
            finally:
                self.connection.close()

def connect_to_mysql(db):
    return MySQLConnection(db)