import pymysql.cursors
from flask_app import DATABASE

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query, data)
                if query.lower().startswith("insert"):
                    return cursor.lastrowid
                elif query.lower().startswith("select"):
                    return cursor.fetchall()
                else:
                    return None
            except Exception as e:
                print("Something went wrong", e)
                return False
            finally:
                self.connection.close()

def connect_to_mysql(db):
    return MySQLConnection(db)